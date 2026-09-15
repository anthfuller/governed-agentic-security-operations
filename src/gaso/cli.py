from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .audit import replay, verify_audit_chain
from .errors import ConformanceError, GasoError, UsageError
from .evidence import verify_evidence_manifest
from .io import load_artifact, load_jsonl, write_json
from .policy import evaluate_policy
from .schema_store import SchemaStore
from .scope import verify_scopes


def _add_format(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format", choices=("human", "json"), default="human", help="Output format.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gaso", description="Offline governance artifact validation and conformance checks.")
    subcommands = parser.add_subparsers(dest="command", required=True)

    validate = subcommands.add_parser("validate", help="Validate JSON or YAML artifacts against registered schemas.")
    validate.add_argument("artifacts", nargs="+", help="Artifact paths.")
    _add_format(validate)

    scope = subcommands.add_parser("verify-tenant-scope", help="Verify exact scope consistency across artifacts.")
    scope.add_argument("artifacts", nargs="+", help="Scoped artifact paths in one workflow.")
    _add_format(scope)

    policy = subcommands.add_parser("evaluate-policy", help="Evaluate a deterministic reference policy without executing an action.")
    policy.add_argument("request", help="Governed action request path.")
    policy.add_argument("--policy", required=True, help="Reference policy path.")
    policy.add_argument("--approvals", nargs="*", default=[], help="Human or customer approval record paths.")
    policy.add_argument("--output", help="Optional path for the generated policy decision JSON.")
    _add_format(policy)

    evidence = subcommands.add_parser("verify-evidence-manifest", help="Verify evidence metadata and derived-artifact lineage.")
    evidence.add_argument("manifest", help="Evidence manifest path.")
    evidence.add_argument("--lineage", nargs="*", default=[], help="Derived-artifact lineage record paths.")
    _add_format(evidence)

    audit = subcommands.add_parser("verify-audit-chain", help="Verify ordered, correlated, tamper-evident audit events.")
    audit.add_argument("events", help="JSONL audit event path.")
    _add_format(audit)

    replay_parser = subcommands.add_parser("replay", help="Reconstruct a verified audit timeline without re-execution.")
    replay_parser.add_argument("events", help="JSONL audit event path.")
    replay_parser.add_argument("--output", help="Optional path for the replay JSON.")
    _add_format(replay_parser)
    return parser


def _emit(payload: dict[str, Any], output_format: str) -> None:
    if output_format == "json":
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    status = payload.get("status", "UNKNOWN")
    command = payload.get("command", "gaso")
    print(f"{status}: {command}")
    for key, value in payload.items():
        if key in {"status", "command"}:
            continue
        rendered = json.dumps(value, indent=2, sort_keys=True) if isinstance(value, (dict, list)) else str(value)
        print(f"{key}: {rendered}")


def _validate_events(events: list[dict[str, Any]], schemas: SchemaStore) -> None:
    for index, event in enumerate(events, start=1):
        schemas.validate(event, f"audit event line {index}")


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    schemas = SchemaStore()
    if args.command == "validate":
        validated = []
        for artifact_path in args.artifacts:
            artifact = load_artifact(artifact_path)
            schema_name = schemas.validate(artifact, artifact_path)
            validated.append({"path": artifact_path, "artifact_type": artifact["artifact_type"], "schema": schema_name})
        return {"command": args.command, "status": "PASS", "validated": validated, "external_action_executed": False}, 0

    if args.command == "verify-tenant-scope":
        artifacts = []
        for artifact_path in args.artifacts:
            artifact = load_artifact(artifact_path)
            schemas.validate(artifact, artifact_path)
            artifacts.append((artifact_path, artifact))
        scope = verify_scopes(artifacts)
        return {"command": args.command, "status": "PASS", "scope": scope, "artifact_count": len(artifacts), "external_action_executed": False}, 0

    if args.command == "evaluate-policy":
        request = load_artifact(args.request)
        policy = load_artifact(args.policy)
        approvals = [load_artifact(path) for path in args.approvals]
        decision = evaluate_policy(request, policy, approvals, schemas)
        schemas.validate(decision, "generated policy decision")
        if args.output:
            write_json(args.output, decision)
        status = "PASS" if decision["outcome"] == "ALLOW" else "BLOCKED"
        return {"command": args.command, "status": status, "decision": decision, "external_action_executed": False}, 0 if status == "PASS" else 1

    if args.command == "verify-evidence-manifest":
        manifest = load_artifact(args.manifest)
        schemas.validate(manifest, args.manifest)
        lineage = []
        for path in args.lineage:
            artifact = load_artifact(path)
            schemas.validate(artifact, path)
            lineage.append(artifact)
        result = verify_evidence_manifest(manifest, lineage)
        return {"command": args.command, "status": "PASS", "verification": result, "external_action_executed": False}, 0

    if args.command in {"verify-audit-chain", "replay"}:
        events = load_jsonl(args.events)
        _validate_events(events, schemas)
        if args.command == "verify-audit-chain":
            result = verify_audit_chain(events)
        else:
            result = replay(events)
            schemas.validate(result, "generated replay result")
            if args.output:
                write_json(args.output, result)
        return {"command": args.command, "status": "PASS", "result": result, "external_action_executed": False}, 0

    raise UsageError("command_unknown", f"Unknown command: {args.command}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        payload, exit_code = run(args)
    except ConformanceError as exc:
        payload = {
            "command": args.command,
            "status": "FAIL_CLOSED",
            "error_code": exc.code,
            "message": exc.message,
            "external_action_executed": False,
        }
        if args.command == "evaluate-policy":
            payload["outcome"] = "FAIL_CLOSED"
        _emit(payload, getattr(args, "format", "human"))
        return 1
    except GasoError as exc:
        payload = {
            "command": args.command,
            "status": "ERROR",
            "error_code": exc.code,
            "message": exc.message,
            "external_action_executed": False,
        }
        _emit(payload, getattr(args, "format", "human"))
        return 2
    except Exception as exc:  # Defensive boundary: do not emit a traceback by default.
        payload = {
            "command": args.command,
            "status": "ERROR",
            "error_code": "unexpected_error",
            "message": str(exc),
            "external_action_executed": False,
        }
        _emit(payload, getattr(args, "format", "human"))
        return 2
    _emit(payload, getattr(args, "format", "human"))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
