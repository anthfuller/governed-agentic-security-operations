from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta, timezone
from typing import Any

from .errors import ConformanceError
from .schema_store import SchemaStore
from .scope import normalized_scope


def _timestamp(value: str, field: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise ConformanceError("timestamp_invalid", f"{field} must be an ISO-8601 timestamp.") from exc
    if parsed.tzinfo is None:
        raise ConformanceError("timestamp_timezone_missing", f"{field} must include a timezone.")
    return parsed.astimezone(timezone.utc)


def _approval_type(artifact_type: str) -> str | None:
    return {"human_approval_record": "human", "customer_approval_record": "customer"}.get(artifact_type)


def request_digest(request: dict[str, Any]) -> str:
    canonical = json.dumps(request, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _approval_matches(
    approval: dict[str, Any],
    required_type: str,
    request: dict[str, Any],
    request_scope: dict[str, Any],
    expected_decision_id: str,
) -> bool:
    if _approval_type(approval.get("artifact_type", "")) != required_type:
        return False
    if approval.get("decision") != "approved" or approval.get("request_id") != request["request_id"]:
        return False
    if approval.get("request_digest") != request_digest(request):
        return False
    if approval.get("policy_decision_id") != expected_decision_id:
        return False
    if request["action"] not in approval.get("approved_actions", []):
        return False
    if normalized_scope(approval, f"approval {approval.get('approval_id', '<unknown>')}") != request_scope:
        return False
    instant = _timestamp(request["requested_at"], "requested_at")
    return _timestamp(approval["valid_from"], "valid_from") <= instant <= _timestamp(approval["valid_until"], "valid_until")


def evaluate_policy(
    request: dict[str, Any],
    policy: dict[str, Any],
    approvals: list[dict[str, Any]],
    schemas: SchemaStore,
) -> dict[str, Any]:
    schemas.validate(request, "request")
    schemas.validate(policy, "policy")
    for index, approval in enumerate(approvals, start=1):
        schemas.validate(approval, f"approval[{index}]")

    request_scope = normalized_scope(request, "request")
    evaluated_at = _timestamp(request["requested_at"], "requested_at")
    expires_at = evaluated_at + timedelta(seconds=policy["decision_ttl_seconds"])
    decision_id = f"decision:{request['request_id']}:{policy['version']}"
    required_approvals: list[str] = []
    reasons: list[str] = []
    obligations = ["external enforcement must revalidate this decision", "no action was executed by gaso"]

    if request["profile"] != policy["profile"]:
        outcome = "DENY"
        reasons.append("profile_not_allowed")
    else:
        rule = next((item for item in policy["actions"] if item["name"] == request["action"]), None)
        if rule is None:
            outcome = "DENY"
            reasons.append("action_not_registered")
        elif not rule["allowed"]:
            outcome = "DENY"
            reasons.append("action_explicitly_denied")
        elif request["tool_id"] != rule["required_tool_id"]:
            outcome = "DENY"
            reasons.append("tool_not_allowed_for_action")
        elif request["target_id"] not in request_scope.get("target_ids", []):
            outcome = "DENY"
            reasons.append("target_not_in_request_scope")
        elif missing := [field for field in rule["required_scope_fields"] if field not in request_scope]:
            outcome = "FAIL_CLOSED"
            reasons.extend(f"scope_field_missing:{field}" for field in missing)
        elif extras := sorted(set(request["parameters"]) - set(rule["allowed_parameters"])):
            outcome = "DENY"
            reasons.extend(f"parameter_not_allowed:{name}" for name in extras)
        else:
            required_approvals = list(rule["required_approvals"])
            missing_approvals = [
                approval_type
                for approval_type in required_approvals
                if not any(
                    _approval_matches(item, approval_type, request, request_scope, decision_id)
                    for item in approvals
                )
            ]
            if missing_approvals:
                outcome = "REQUIRE_APPROVAL"
                reasons.extend(f"approval_missing_or_invalid:{item}" for item in missing_approvals)
            else:
                outcome = "ALLOW"
                reasons.append("reference_policy_requirements_satisfied")

    return {
        "artifact_type": "policy_decision_record",
        "schema_version": "1.0.0",
        "decision_id": decision_id,
        "request_id": request["request_id"],
        "policy_id": policy["policy_id"],
        "policy_version": policy["version"],
        "outcome": outcome,
        "scope": request["scope"],
        "reason_codes": reasons,
        "required_approvals": required_approvals,
        "obligations": obligations,
        "evaluated_at": evaluated_at.isoformat().replace("+00:00", "Z"),
        "expires_at": expires_at.isoformat().replace("+00:00", "Z"),
        "executed_action": False,
    }
