from copy import deepcopy
import json
from pathlib import Path

import pytest
import yaml

from gaso.audit import replay, verify_audit_chain
from gaso.errors import ConformanceError
from gaso.evidence import verify_evidence_manifest
from gaso.io import load_jsonl
from gaso.policy import evaluate_policy
from gaso.schema_store import SchemaStore
from gaso.scope import verify_scopes

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "walkthroughs" / "artifacts"
SCENARIOS = ("mssp-endpoint-isolation", "mdr-cloud-iam-compromise", "dfir-local-llm-timeline")


def load(path: Path):
    if path.suffix == ".json":
        return json.loads(path.read_text())
    return yaml.safe_load(path.read_text())


def approvals(directory: Path):
    return [load(path) for path in sorted(directory.glob("*-approval.yaml"))]


@pytest.mark.parametrize("scenario", SCENARIOS)
def test_walkthrough_artifacts_policy_scope_audit_and_replay(scenario):
    directory = ARTIFACTS / scenario
    store = SchemaStore(ROOT / "schemas")
    for path in sorted(directory.iterdir()):
        if path.suffix in {".yaml", ".json"}:
            store.validate(load(path), str(path.relative_to(ROOT)))

    request = load(directory / "request.yaml")
    policy = load(directory / "policy.yaml")
    supplied_approvals = approvals(directory)
    blocked = evaluate_policy(request, policy, [], store)
    assert blocked["outcome"] == "REQUIRE_APPROVAL"
    allowed = evaluate_policy(request, policy, supplied_approvals, store)
    assert allowed["outcome"] == "ALLOW"
    assert allowed == load(directory / "policy-decision.yaml")

    scoped_paths = [directory / "request.yaml", directory / "policy-decision.yaml", directory / "tool-request.yaml"]
    scoped_paths.extend(sorted(directory.glob("*-approval.yaml")))
    scoped_paths.extend(
        path
        for path in (
            directory / "evidence-manifest.yaml",
            directory / "recommendation.yaml",
            directory / "assurance-result.yaml",
            directory / "timeline-lineage.yaml",
        )
        if path.exists()
    )
    verify_scopes([(str(path), load(path)) for path in scoped_paths])

    manifest = load(directory / "evidence-manifest.yaml")
    lineage_path = directory / "timeline-lineage.yaml"
    lineage = [load(lineage_path)] if lineage_path.exists() else []
    verify_evidence_manifest(manifest, lineage)

    tool_request = load(directory / "tool-request.yaml")
    assert tool_request["tool_id"] == request["tool_id"]
    assert tool_request["operation"] == request["action"]
    assert tool_request["target_id"] == request["target_id"]
    assert tool_request["parameters"] == request["parameters"]
    assert tool_request["policy_decision_id"] == allowed["decision_id"]
    assert set(tool_request["approval_ids"]) == {item["approval_id"] for item in supplied_approvals}
    tool_result = load(directory / "tool-result.yaml")
    assert tool_result["request_id"] == tool_request["request_id"]
    assert tool_result["status"] == "not_executed"

    events = load_jsonl(directory / "audit-events.jsonl")
    for event in events:
        store.validate(event, "walkthrough audit event")
    assert verify_audit_chain(events)["event_count"] == 4
    assert replay(events) == load(directory / "expected-replay.json")


def test_mssp_cross_target_request_fails_closed():
    directory = ARTIFACTS / "mssp-endpoint-isolation"
    request = load(directory / "negative" / "request-target-mismatch.yaml")
    with pytest.raises(ConformanceError, match="target_id"):
        evaluate_policy(request, load(directory / "policy.yaml"), approvals(directory), SchemaStore(ROOT / "schemas"))


def test_mdr_post_approval_parameter_change_requires_new_approvals():
    directory = ARTIFACTS / "mdr-cloud-iam-compromise"
    request = load(directory / "negative" / "request-changed-after-approval.yaml")
    result = evaluate_policy(request, load(directory / "policy.yaml"), approvals(directory), SchemaStore(ROOT / "schemas"))
    assert result["outcome"] == "REQUIRE_APPROVAL"


def test_dfir_unknown_lineage_source_fails_closed():
    directory = ARTIFACTS / "dfir-local-llm-timeline"
    manifest = load(directory / "evidence-manifest.yaml")
    lineage = load(directory / "negative" / "timeline-lineage-unknown-source.yaml")
    with pytest.raises(ConformanceError, match="Unknown source evidence"):
        verify_evidence_manifest(manifest, [lineage])


@pytest.mark.parametrize("scenario", SCENARIOS)
def test_walkthrough_audit_tampering_is_detected(scenario):
    events = load_jsonl(ARTIFACTS / scenario / "audit-events.jsonl")
    modified = deepcopy(events)
    modified[-1]["details"]["external_action_executed"] = True
    with pytest.raises(ConformanceError, match="hash"):
        verify_audit_chain(modified)
