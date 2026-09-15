# Policy Decision Flow

Evaluate a governed action in this order:

1. Parse and schema-validate the request and policy.
2. Verify the policy profile applies to the request.
3. Verify explicit customer, tenant, case, target, evidence, and environment scope.
4. Find the registered action; deny unknown or explicitly prohibited actions.
5. Match the required tool contract and version.
6. Reject undeclared parameters or a target outside `scope.target_ids`.
7. Determine required approval types from the action rule.
8. Validate each approval's human identity, request, action, target, scope, conditions, and validity period.
9. Emit one bounded decision with reason codes, obligations, and expiration.
10. Preserve the decision for audit; do not execute the action.

Malformed or ambiguous inputs produce `FAIL_CLOSED`. Missing valid approvals produce `REQUIRE_APPROVAL`. Explicitly unsupported behavior produces `DENY`. `ALLOW` means the reference policy requirements were satisfied; only an external PEP may act on a real system.
