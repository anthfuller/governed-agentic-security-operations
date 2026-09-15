# Tenant Scope Validation

Scope validation compares the same dimensions across correlated artifacts before an action, release, or evidentiary use.

## Validation Procedure

1. Identify the authoritative request and applicable dimensions.
2. Require each downstream artifact to carry those dimensions.
3. Normalize only according to a documented, deterministic rule.
4. Compare values exactly across evidence, decision, approval, tool, and audit records.
5. Reject missing or conflicting values and record a denial reason.
6. Re-run validation after any request or context change.

The offline command is:

```bash
gaso verify-tenant-scope request.yaml decision.yaml approval.yaml tool-request.yaml
```

A passing result means the supplied files agree on their declared scope. It does not prove that a caller was authorized for the scope or that production systems enforced it.

## Negative Tests

At minimum test a different tenant, customer, case, target, evidence object, and output destination; a missing identifier; and an approval copied from another request. Each must block progression.

Related controls: `GASO-TEN-001`, `GASO-TEN-002`, `GASO-TEN-003`, `GASO-APR-002`, `GASO-TOL-003`.
