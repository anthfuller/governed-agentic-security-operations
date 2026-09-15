# Policy Decision Record Template

The policy decision records one of four outcomes: `ALLOW`, `DENY`, `REQUIRE_APPROVAL`, or `FAIL_CLOSED`.

It must bind the request, policy and version, scope, reason codes, required approvals, obligations, evaluation time, and expiration. `executed_action` is always `false` because a policy decision does not perform an action.

Validate [`policy-decision-record.yaml`](policy-decision-record.yaml) with `gaso validate`. Production decisions require an external PDP and must be revalidated by a PEP at the action boundary.
