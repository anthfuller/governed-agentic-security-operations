# Action Risk Classification

Action classification determines the minimum policy, approval, enforcement, and audit handling. Classify the effective operation, not the agent's description of it.

| Class | Definition | Examples | Minimum handling |
|---|---|---|---|
| `read_only` | Retrieves non-sensitive data without changing external state. | Read synthetic case status. | Registered tool, valid scope, current decision, audit. |
| `sensitive_read` | Retrieves evidence, personal data, secrets-adjacent data, or restricted context. | Read a case evidence reference. | Least privilege, explicit case/evidence scope, human review where policy requires, audit. |
| `state_change` | Changes an identity, host, policy, configuration, case, or customer environment. | Isolate an endpoint; disable an account. | Scope-bound policy decision, required human/customer approvals, PEP enforcement, external receipt, audit. |
| `destructive` | Deletes, destroys, irreversibly alters, or makes recovery materially difficult. | Delete evidence; purge tenant data. | Deny by default; require separately approved policy and recovery controls if an organization elects to support it. |

## Rules

1. Unknown operations are denied.
2. Ambiguous operations use the higher plausible class and escalate.
3. Parameter changes that increase impact require reclassification and a new decision.
4. A read-only interface does not make sensitive data low risk.
5. A recommendation does not lower the risk class of the recommended action.

Record the class in the tool contract and reference policy. Validate negative fixtures for unknown actions, unregistered parameters, and prohibited destructive operations.
