from __future__ import annotations

from typing import Any

from .errors import ConformanceError

SCOPE_KEYS = ("provider_id", "customer_id", "tenant_id", "case_id", "evidence_ids", "target_ids", "environment")


def normalized_scope(artifact: dict[str, Any], source: str = "artifact") -> dict[str, Any]:
    scope = artifact.get("scope")
    if not isinstance(scope, dict) or not scope:
        raise ConformanceError("scope_missing", f"{source}: an explicit scope object is required.")
    normalized: dict[str, Any] = {}
    for key in SCOPE_KEYS:
        if key not in scope:
            continue
        value = scope[key]
        if isinstance(value, list):
            if not value or any(not isinstance(item, str) or not item for item in value):
                raise ConformanceError("scope_value_invalid", f"{source}: {key} must contain non-empty strings.")
            normalized[key] = sorted(set(value))
        elif isinstance(value, str) and value:
            normalized[key] = value
        else:
            raise ConformanceError("scope_value_invalid", f"{source}: {key} must be a non-empty string or list.")
    if not normalized:
        raise ConformanceError("scope_empty", f"{source}: no recognized scope dimensions were provided.")
    target = artifact.get("target_id")
    if target is not None and target not in normalized.get("target_ids", []):
        raise ConformanceError("target_scope_mismatch", f"{source}: target_id is not present in scope.target_ids.")
    return normalized


def verify_scopes(artifacts: list[tuple[str, dict[str, Any]]]) -> dict[str, Any]:
    if not artifacts:
        raise ConformanceError("scope_input_empty", "At least one scoped artifact is required.")
    baseline_source, baseline_artifact = artifacts[0]
    baseline = normalized_scope(baseline_artifact, baseline_source)
    for source, artifact in artifacts[1:]:
        current = normalized_scope(artifact, source)
        if current != baseline:
            differing = sorted({*baseline.keys(), *current.keys()} - {key for key in baseline if baseline.get(key) == current.get(key)})
            raise ConformanceError("scope_mismatch", f"{source}: scope differs from {baseline_source} in: {', '.join(differing)}")
    return baseline
