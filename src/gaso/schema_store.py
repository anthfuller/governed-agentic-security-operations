from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from .errors import ConformanceError, UsageError


def find_schema_directory() -> Path:
    candidates: list[Path] = []
    if configured := os.environ.get("GASO_SCHEMA_DIR"):
        candidates.append(Path(configured))
    candidates.extend(
        [
            Path.cwd() / "schemas",
            Path(__file__).resolve().parents[2] / "schemas",
            Path(sys.prefix) / "share" / "gaso" / "schemas",
        ]
    )
    for candidate in candidates:
        if (candidate / "index.json").is_file():
            return candidate
    raise UsageError("schema_directory_not_found", "Could not locate the GASO schema directory.")


class SchemaStore:
    def __init__(self, schema_directory: str | Path | None = None):
        self.directory = Path(schema_directory) if schema_directory else find_schema_directory()
        try:
            self.index = json.loads((self.directory / "index.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise UsageError("schema_index_error", f"Could not load schema index: {exc}") from exc
        self.schemas: dict[str, dict[str, Any]] = {}
        resources: list[tuple[str, Resource[Any]]] = []
        for path in sorted(self.directory.glob("*.schema.json")):
            try:
                schema = json.loads(path.read_text(encoding="utf-8"))
                Draft202012Validator.check_schema(schema)
                uri = schema["$id"]
            except (OSError, json.JSONDecodeError, KeyError) as exc:
                raise UsageError("schema_load_error", f"Could not load {path}: {exc}") from exc
            self.schemas[path.name] = schema
            resources.append((uri, Resource.from_contents(schema)))
        self.registry = Registry().with_resources(resources)

    def validate(self, artifact: dict[str, Any], source: str = "artifact") -> str:
        artifact_type = artifact.get("artifact_type")
        if not isinstance(artifact_type, str) or not artifact_type:
            raise ConformanceError("artifact_type_missing", f"{source}: artifact_type is required.")
        schema_name = self.index.get(artifact_type)
        if not schema_name:
            raise ConformanceError("artifact_type_unknown", f"{source}: no schema is registered for {artifact_type!r}.")
        schema = self.schemas.get(schema_name)
        if schema is None:
            raise UsageError("registered_schema_missing", f"Schema index references missing file: {schema_name}")
        validator = Draft202012Validator(schema, registry=self.registry, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(artifact), key=lambda error: list(error.absolute_path))
        if errors:
            formatted = []
            for error in errors[:20]:
                location = "/".join(str(part) for part in error.absolute_path) or "$"
                formatted.append(f"{location}: {error.message}")
            raise ConformanceError("schema_validation_failed", f"{source}: " + "; ".join(formatted))
        self._semantic_validation(artifact, source)
        return schema_name

    def _semantic_validation(self, artifact: dict[str, Any], source: str) -> None:
        if artifact.get("artifact_type") == "control_catalog":
            ids = [control["id"] for control in artifact["controls"]]
            if len(ids) != len(set(ids)):
                raise ConformanceError("duplicate_control_id", f"{source}: control IDs must be unique.")
            known = set(ids)
            referenced = {
                related_id
                for control in artifact["controls"]
                for related_id in control["related"]["controls"]
            }
            if unknown := sorted(referenced - known):
                raise ConformanceError("unknown_related_control", f"{source}: unknown related controls: {', '.join(unknown)}")
        if artifact.get("artifact_type") == "implementation_profile":
            catalog_path = self.directory.parent / "controls" / "control-catalog.yaml"
            if catalog_path.is_file():
                catalog = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
                known = {control["id"] for control in catalog["controls"]}
                selected = set(artifact["applicable_controls"])
                selected.update(item["control_id"] for item in artifact["conditional_controls"])
                unknown = sorted(selected - known)
                if unknown:
                    raise ConformanceError("unknown_control_reference", f"{source}: unknown controls: {', '.join(unknown)}")
        if artifact.get("artifact_type") == "reference_policy":
            names = [action["name"] for action in artifact["actions"]]
            if len(names) != len(set(names)):
                raise ConformanceError("duplicate_policy_action", f"{source}: policy action names must be unique.")
        if artifact.get("artifact_type") == "tool_contract":
            names = [operation["name"] for operation in artifact["operations"]]
            if len(names) != len(set(names)):
                raise ConformanceError("duplicate_tool_operation", f"{source}: tool operation names must be unique.")
        if artifact.get("artifact_type") in {"human_approval_record", "customer_approval_record"}:
            valid_from = datetime.fromisoformat(artifact["valid_from"].replace("Z", "+00:00"))
            valid_until = datetime.fromisoformat(artifact["valid_until"].replace("Z", "+00:00"))
            if valid_from > valid_until:
                raise ConformanceError("approval_window_invalid", f"{source}: valid_from must not be after valid_until.")
        if artifact.get("artifact_type") == "policy_decision_record":
            evaluated_at = datetime.fromisoformat(artifact["evaluated_at"].replace("Z", "+00:00"))
            expires_at = datetime.fromisoformat(artifact["expires_at"].replace("Z", "+00:00"))
            if evaluated_at >= expires_at:
                raise ConformanceError("decision_window_invalid", f"{source}: expires_at must be after evaluated_at.")
        if artifact.get("artifact_type") == "replay_result":
            sequences = [item["sequence"] for item in artifact["timeline"]]
            expected = list(range(1, len(sequences) + 1))
            if sequences != expected:
                raise ConformanceError("replay_sequence_invalid", f"{source}: replay sequence must be contiguous and start at 1.")
