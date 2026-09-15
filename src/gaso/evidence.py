from __future__ import annotations

import re
from typing import Any

from .errors import ConformanceError
from .scope import normalized_scope

SHA256 = re.compile(r"^(?:sha256:)?[a-fA-F0-9]{64}$")


def verify_evidence_manifest(manifest: dict[str, Any], lineage: list[dict[str, Any]]) -> dict[str, Any]:
    scope = normalized_scope(manifest, "evidence manifest")
    evidence = manifest["evidence_objects"]
    evidence_ids = [item["evidence_id"] for item in evidence]
    if len(evidence_ids) != len(set(evidence_ids)):
        raise ConformanceError("duplicate_evidence_id", "Evidence object identifiers must be unique.")
    for item in evidence:
        if item["hash_algorithm"] != "sha256" or not SHA256.fullmatch(str(item["hash_value"])):
            raise ConformanceError("evidence_hash_invalid", f"Invalid SHA-256 value for {item['evidence_id']}.")

    declared = set(manifest["derived_artifact_ids"])
    provided = {item["derived_artifact_id"] for item in lineage}
    missing = sorted(declared - provided)
    unexpected = sorted(provided - declared)
    if missing:
        raise ConformanceError("lineage_record_missing", f"Missing lineage records for: {', '.join(missing)}")
    if unexpected:
        raise ConformanceError("lineage_record_unexpected", f"Lineage records not declared by manifest: {', '.join(unexpected)}")
    known_evidence = set(evidence_ids)
    for item in lineage:
        if normalized_scope(item, f"lineage {item['derived_artifact_id']}") != scope:
            raise ConformanceError("lineage_scope_mismatch", f"Lineage scope differs for {item['derived_artifact_id']}.")
        unknown_sources = sorted(set(item["source_evidence_ids"]) - known_evidence)
        if unknown_sources:
            raise ConformanceError("lineage_source_unknown", f"Unknown source evidence for {item['derived_artifact_id']}: {', '.join(unknown_sources)}")
    return {
        "manifest_id": manifest["manifest_id"],
        "evidence_object_count": len(evidence),
        "derived_artifact_count": len(lineage),
        "scope": scope,
        "factual_correctness_established": False,
        "forensic_validity_established": False,
    }
