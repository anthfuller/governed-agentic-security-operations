# Approval Policy Requirements

Approval is required only from an authorized human or customer role defined by policy. Analyst review, agent output, assurance results, and tool registration are not approvals.

## Required Binding

An approval record must bind:

- approver identity and role;
- request and policy-decision identifiers;
- approved action and target;
- customer, tenant, case, evidence, and environment scope as applicable;
- conditions, validity start, and expiration;
- decision: approved or denied.

## Minimum Rules

| Condition | Required result |
|---|---|
| Approval type is missing | `REQUIRE_APPROVAL` or `DENY` according to policy. |
| Approver is an agent or judge | `DENY`. |
| Request, action, target, or scope differs | `DENY`. |
| Approval is expired or not yet valid | `DENY`. |
| Customer authorization is contractually required and absent | `DENY`. |
| Approval conditions cannot be enforced | `FAIL_CLOSED`. |

Controls: `GASO-APR-001`, `GASO-APR-002`, and `GASO-APR-003`. Validate records against [`../schemas/approval-record.schema.json`](../schemas/approval-record.schema.json).
