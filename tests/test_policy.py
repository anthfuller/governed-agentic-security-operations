from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from gaso.errors import ConformanceError
from gaso.policy import evaluate_policy
from gaso.schema_store import SchemaStore

ROOT = Path(__file__).resolve().parents[1]


def load(relative: str):
    return yaml.safe_load((ROOT / relative).read_text())


def evaluate(request=None, approvals=None):
    store = SchemaStore(ROOT / "schemas")
    return evaluate_policy(
        request or load("templates/governed-action-request.yaml"),
        load("policies/endpoint-response-policy.yaml"),
        approvals or [],
        store,
    )


def test_state_change_requires_both_approvals():
    result = evaluate()
    assert result["outcome"] == "REQUIRE_APPROVAL"
    assert set(result["required_approvals"]) == {"human", "customer"}


def test_matching_approvals_allow_reference_decision():
    result = evaluate(approvals=[load("templates/human-approval-record.yaml"), load("templates/customer-approval-record.yaml")])
    assert result["outcome"] == "ALLOW"
    assert result["executed_action"] is False


def test_one_approval_is_not_enough():
    result = evaluate(approvals=[load("templates/human-approval-record.yaml")])
    assert result["outcome"] == "REQUIRE_APPROVAL"
    assert "approval_missing_or_invalid:customer" in result["reason_codes"]


def test_unregistered_parameter_is_denied():
    request = load("templates/governed-action-request.yaml")
    request["parameters"]["force"] = True
    result = evaluate(request=request)
    assert result["outcome"] == "DENY"
    assert "parameter_not_allowed:force" in result["reason_codes"]


def test_unregistered_tool_is_denied():
    request = load("templates/governed-action-request.yaml")
    request["tool_id"] = "tool-example-unregistered"
    result = evaluate(request=request)
    assert result["outcome"] == "DENY"
    assert "tool_not_allowed_for_action" in result["reason_codes"]


def test_explicitly_prohibited_action_is_denied():
    request = load("templates/governed-action-request.yaml")
    request["action"] = "delete_endpoint_data"
    request["parameters"] = {"path": "/synthetic"}
    result = evaluate(request=request)
    assert result["outcome"] == "DENY"
    assert "action_explicitly_denied" in result["reason_codes"]


def test_mismatched_approval_scope_is_not_accepted():
    approval = deepcopy(load("templates/human-approval-record.yaml"))
    approval["scope"]["target_ids"] = ["host-example-002"]
    result = evaluate(approvals=[approval, load("templates/customer-approval-record.yaml")])
    assert result["outcome"] == "REQUIRE_APPROVAL"
    assert "approval_missing_or_invalid:human" in result["reason_codes"]


def test_request_change_invalidates_existing_approvals():
    request = load("templates/governed-action-request.yaml")
    request["parameters"]["reason"] = "Changed after approval"
    result = evaluate(
        request=request,
        approvals=[load("templates/human-approval-record.yaml"), load("templates/customer-approval-record.yaml")],
    )
    assert result["outcome"] == "REQUIRE_APPROVAL"
    assert set(result["reason_codes"]) == {
        "approval_missing_or_invalid:human",
        "approval_missing_or_invalid:customer",
    }


def test_retroactive_approval_is_not_accepted():
    approval = deepcopy(load("templates/human-approval-record.yaml"))
    approval["recorded_at"] = "2026-09-15T12:04:00Z"
    result = evaluate(approvals=[approval, load("templates/customer-approval-record.yaml")])
    assert result["outcome"] == "REQUIRE_APPROVAL"
    assert "approval_missing_or_invalid:human" in result["reason_codes"]


def test_target_must_be_in_declared_scope():
    request = load("templates/governed-action-request.yaml")
    request["target_id"] = "host-example-002"
    with pytest.raises(ConformanceError, match="target_id is not present"):
        evaluate(request=request)


def test_duplicate_policy_action_fails_closed():
    policy = load("policies/endpoint-response-policy.yaml")
    policy["actions"].append(deepcopy(policy["actions"][0]))
    with pytest.raises(ConformanceError, match="must be unique"):
        evaluate_policy(load("templates/governed-action-request.yaml"), policy, [], SchemaStore(ROOT / "schemas"))
