# Walkthrough: MSSP Endpoint Isolation Recommendation

## Scenario

An MDR analyst receives an alert indicating suspicious endpoint behavior in a customer tenant. An agent assists by summarizing scoped evidence and recommending endpoint isolation.

## Governance Objective

Show how an agent-assisted recommendation moves through evidence support, policy decision, approval, scoped execution, and audit replay without allowing the agent to authorize itself.

## Flow

1. Alert is received.
2. Agent retrieves scoped evidence.
3. Agent drafts an endpoint isolation recommendation.
4. Agent judge checks evidence support, tenant scope, and unsupported claims.
5. Policy Decision Point evaluates whether the action is allowed, denied, escalated, or failed closed.
6. Human approver reviews the recommendation and decision record.
7. Customer approval is required if the action affects the customer environment and the service model requires customer authorization.
8. Policy Enforcement Point enforces the approved action through a scoped tool.
9. Audit event records the decision path, approval path, scope, tool request, and execution result.
10. Audit replay reconstructs what was known, what was recommended, what was approved, what was executed, and why.

## Control Points

| Step | Control |
|---|---|
| Evidence retrieval | Tenant, customer, case, and evidence-scope validation |
| Agent recommendation | Unsupported-claim and evidence-support checks |
| Policy decision | PDP risk classification and approval policy |
| Human approval | Formal approval record |
| Customer approval | Separate customer authorization where required |
| Tool execution | PEP-enforced scoped action |
| Audit replay | Replayable decision and execution trail |

## Failure Modes

| Failure | Expected Behavior |
|---|---|
| Evidence is missing | Fail closed or escalate for human review |
| Tenant scope is ambiguous | Fail closed |
| Agent recommendation lacks evidence support | Deny or escalate |
| Customer approval is required but missing | Deny execution |
| Tool request exceeds approved scope | Block at PEP |
| Audit event cannot be written | Fail closed for governed execution |

## Representative Artifacts

- Agent recommendation record
- Agent judge output
- Policy decision record
- Human approval record
- Customer approval record, where required
- Tool execution request
- Tool execution result
- Audit event
- Replay summary

## Architecture References

- [`../architecture/control-loop.md`](../architecture/control-loop.md)
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md)
- [`../human-oversight/readme.md`](../human-oversight/readme.md)
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md)
- [`../tool-access/readme.md`](../tool-access/readme.md)
- [`../audit-replay/readme.md`](../audit-replay/readme.md)
