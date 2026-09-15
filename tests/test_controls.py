from pathlib import Path

import pytest
import yaml

from gaso.errors import ConformanceError
from gaso.schema_store import SchemaStore

ROOT = Path(__file__).resolve().parents[1]


def load(relative: str):
    return yaml.safe_load((ROOT / relative).read_text())


def test_external_verification_methods_name_a_dependency():
    catalog = load("controls/control-catalog.yaml")
    for control in catalog["controls"]:
        if any(item["type"] == "external" for item in control["verification"]):
            assert control["external_dependencies"], control["id"]


def test_assurance_result_cannot_claim_authority():
    artifact = load("templates/assurance-result.yaml")
    artifact["authoritative"] = True
    with pytest.raises(ConformanceError, match="False"):
        SchemaStore(ROOT / "schemas").validate(artifact, "authoritative assurance")


def test_tool_request_must_remain_validate_only():
    artifact = load("templates/tool-execution-request.yaml")
    artifact["execution_mode"] = "execute"
    with pytest.raises(ConformanceError, match="not valid"):
        SchemaStore(ROOT / "schemas").validate(artifact, "executable tool request")


def test_duplicate_tool_operation_fails_closed():
    artifact = load("templates/tool-contract.yaml")
    artifact["operations"].append(dict(artifact["operations"][0]))
    with pytest.raises(ConformanceError, match="must be unique"):
        SchemaStore(ROOT / "schemas").validate(artifact, "conflicting tool contract")


def test_reversed_approval_window_fails_closed():
    artifact = load("templates/human-approval-record.yaml")
    artifact["valid_from"], artifact["valid_until"] = artifact["valid_until"], artifact["valid_from"]
    with pytest.raises(ConformanceError, match="valid_from"):
        SchemaStore(ROOT / "schemas").validate(artifact, "reversed approval")
