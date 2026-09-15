# Audit Event Template

Audit events record a governed workflow without re-executing it. Each event includes an event ID, sequence, correlation ID, event type, time, actor, scope, outcome, details, previous-event hash, and event hash.

The hash chain uses canonical compact JSON with sorted keys after removing `event_hash`; each event records the preceding event hash. The first event uses `null` for `previous_event_hash`.

Use `gaso verify-audit-chain` for integrity checks and `gaso replay` for deterministic reconstruction. These checks do not make a local JSONL file an immutable production audit store.
