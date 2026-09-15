from __future__ import annotations

import hashlib
import json
from typing import Any

from .errors import ConformanceError
from .scope import normalized_scope


def canonical_event_bytes(event: dict[str, Any]) -> bytes:
    unsigned = {key: value for key, value in event.items() if key != "event_hash"}
    return json.dumps(unsigned, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def calculate_event_hash(event: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_event_bytes(event)).hexdigest()


def _plain_hash(value: str | None) -> str | None:
    if value is None:
        return None
    return value.removeprefix("sha256:").lower()


def verify_audit_chain(events: list[dict[str, Any]]) -> dict[str, Any]:
    expected_previous: str | None = None
    expected_scope: dict[str, Any] | None = None
    expected_correlation: str | None = None
    seen_ids: set[str] = set()
    for expected_sequence, event in enumerate(events, start=1):
        event_id = event["event_id"]
        if event_id in seen_ids:
            raise ConformanceError("duplicate_audit_event", f"Duplicate event_id: {event_id}")
        seen_ids.add(event_id)
        if event["sequence"] != expected_sequence:
            raise ConformanceError("audit_sequence_gap", f"Expected sequence {expected_sequence}, got {event['sequence']}.")
        correlation = event["correlation_id"]
        if expected_correlation is None:
            expected_correlation = correlation
        elif correlation != expected_correlation:
            raise ConformanceError("audit_correlation_mismatch", f"Event {event_id} has a different correlation_id.")
        scope = normalized_scope(event, f"audit event {event_id}")
        if expected_scope is None:
            expected_scope = scope
        elif scope != expected_scope:
            raise ConformanceError("audit_scope_mismatch", f"Event {event_id} has a different scope.")
        if _plain_hash(event["previous_event_hash"]) != expected_previous:
            raise ConformanceError("audit_previous_hash_mismatch", f"Event {event_id} does not link to the previous event.")
        actual = calculate_event_hash(event)
        if _plain_hash(event["event_hash"]) != actual:
            raise ConformanceError("audit_event_hash_mismatch", f"Event {event_id} hash does not match its canonical content.")
        expected_previous = actual
    return {
        "correlation_id": expected_correlation,
        "event_count": len(events),
        "first_event_id": events[0]["event_id"],
        "last_event_id": events[-1]["event_id"],
        "chain_head": expected_previous,
        "scope": expected_scope,
    }


def replay(events: list[dict[str, Any]]) -> dict[str, Any]:
    verified = verify_audit_chain(events)
    return {
        "artifact_type": "replay_result",
        "schema_version": "1.0.0",
        "correlation_id": verified["correlation_id"],
        "chain_verified": True,
        "external_action_executed": False,
        "timeline": [
            {
                "sequence": event["sequence"],
                "event_time": event["event_time"],
                "event_type": event["event_type"],
                "actor_id": event["actor_id"],
                "outcome": event["outcome"],
                "details": event["details"],
            }
            for event in events
        ],
    }
