from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from gaso.errors import ConformanceError
from gaso.evidence import verify_evidence_manifest

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    return yaml.safe_load((ROOT / "templates" / name).read_text())


def test_manifest_and_lineage_pass():
    result = verify_evidence_manifest(load("evidence-manifest.yaml"), [load("derived-artifact-lineage.yaml")])
    assert result["evidence_object_count"] == 1
    assert result["forensic_validity_established"] is False


def test_missing_lineage_fails_closed():
    with pytest.raises(ConformanceError, match="Missing lineage"):
        verify_evidence_manifest(load("evidence-manifest.yaml"), [])


def test_unknown_lineage_source_fails_closed():
    lineage = deepcopy(load("derived-artifact-lineage.yaml"))
    lineage["source_evidence_ids"] = ["evidence-example-unknown"]
    with pytest.raises(ConformanceError, match="Unknown source evidence"):
        verify_evidence_manifest(load("evidence-manifest.yaml"), [lineage])
