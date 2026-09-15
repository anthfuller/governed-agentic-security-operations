from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .errors import ConformanceError, UsageError


def load_artifact(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    if not source.is_file():
        raise UsageError("file_not_found", f"Artifact not found: {source}")
    try:
        text = source.read_text(encoding="utf-8")
        if source.suffix.lower() == ".json":
            value = json.loads(text)
        elif source.suffix.lower() in {".yaml", ".yml"}:
            value = yaml.safe_load(text)
        else:
            raise UsageError("unsupported_file_type", f"Use a JSON, YAML, or YML artifact: {source}")
    except UsageError:
        raise
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        raise UsageError("artifact_parse_error", f"Could not parse {source}: {exc}") from exc
    if not isinstance(value, dict):
        raise UsageError("artifact_not_object", f"Artifact must contain one object: {source}")
    return value


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    source = Path(path)
    if not source.is_file():
        raise UsageError("file_not_found", f"Audit event file not found: {source}")
    events: list[dict[str, Any]] = []
    try:
        for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise UsageError("audit_event_not_object", f"Line {number} is not an object: {source}")
            events.append(value)
    except UsageError:
        raise
    except (OSError, json.JSONDecodeError) as exc:
        raise UsageError("audit_parse_error", f"Could not parse {source}: {exc}") from exc
    if not events:
        raise ConformanceError("audit_file_empty", f"No audit events found: {source}")
    return events


def write_json(path: str | Path, value: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
