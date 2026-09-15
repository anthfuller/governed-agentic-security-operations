# Fail-Closed Behavior

Fail closed means the governed workflow does not continue when a required control state cannot be established. It is not the same as silently dropping an error.

## Mandatory Triggers

- missing, malformed, or unknown artifact type;
- missing or conflicting tenant, customer, case, evidence, target, or environment scope;
- missing, stale, expired, or unversioned policy;
- unavailable approval, identity, registry, or audit dependency when it is required;
- unsupported action or parameter;
- evidence hash or lineage failure;
- audit event write or chain-integrity failure;
- fleet eligibility, provenance, stage-gate, rollback, or recall ambiguity.

## Required Outcome

1. Do not execute or release the requested action.
2. Return a stable failure code and non-success process exit code.
3. Record the known request, scope, decision point, and reason without copying prohibited sensitive content.
4. Route to the accountable human role when escalation is possible.
5. Require a new decision after the missing state is corrected; do not resume from implied authorization.

`gaso` exits `1` for conformance failure and includes `external_action_executed: false`. Production enforcement must implement the same boundary externally.
