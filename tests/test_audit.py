from copy import deepcopy
from pathlib import Path

import pytest

from gaso.audit import replay, verify_audit_chain
from gaso.errors import ConformanceError
from gaso.io import load_jsonl
from gaso.schema_store import SchemaStore

ROOT = Path(__file__).resolve().parents[1]


def events():
    return load_jsonl(ROOT / "tests" / "fixtures" / "audit-valid.jsonl")


def test_valid_chain_and_replay():
    result = verify_audit_chain(events())
    assert result["event_count"] == 3
    replay_result = replay(events())
    assert replay_result["chain_verified"] is True
    assert replay_result["external_action_executed"] is False


def test_modified_event_is_detected():
    modified = deepcopy(events())
    modified[1]["details"]["decision_id"] = "decision-example-modified"
    with pytest.raises(ConformanceError, match="hash"):
        verify_audit_chain(modified)


def test_reordered_event_is_detected():
    modified = events()
    modified[0], modified[1] = modified[1], modified[0]
    with pytest.raises(ConformanceError, match="sequence"):
        verify_audit_chain(modified)


def test_noncontiguous_replay_result_is_rejected():
    result = replay(events())
    result["timeline"][1]["sequence"] = 3
    with pytest.raises(ConformanceError, match="contiguous"):
        SchemaStore(ROOT / "schemas").validate(result, "invalid replay")
