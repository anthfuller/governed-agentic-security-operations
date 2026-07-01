# Compromised Agent Recall

This directory models a governed emergency recall for an agent package version that shows indicators of compromise, scope violation, or unauthorized behavior. The example separates the recall request, policy decision, human approval, enforcement action, and audit replay records so that emergency containment can occur without expanding tenant, customer, case, tool, evidence, or memory boundaries.

## Scenario

| Field | Value |
| --- | --- |
| Scenario | `compromised_agent_recall` |
| Severity | `critical` |
| Urgency | `immediate` |
| Affected agent | `soc-triage-agent` |
| Agent package | `pkg-soc-triage-agent:2.7.3` |
| Registry | `agent-registry-prod` |
| Model route | `model-route-security-ops-standard` |
| Prompt package | `prompt-package-soc-triage-2.7.3` |
| Policy bundle | `policy-bundle-agent-actions-2025-02` |
| Tool contract | `tool-contract-soc-triage-2.7.3` |

The trigger is a suspected compromise of the `SOC Triage Agent` package version. Fleet monitoring observed an out-of-scope tool request, a runtime policy bundle mismatch, and an unusual cross-case context request.

## Scope

The recall is limited to the affected production scope:

| Scope dimension | In scope |
| --- | --- |
| Environment | `production` |
| Tenants | `tenant-alpha-prod`, `tenant-bravo-prod` |
| Customers | `customer-alpha`, `customer-bravo` |
| Cases | `case-iam-0007`, `case-endpoint-0019` |
| Sessions | Active and scheduled sessions using the affected agent version |
| Tools | Tools registered to the affected agent version |
| Memory | Case memory and runtime context for affected sessions |
| Downstream outputs | Included in recall scope |

The recall must not modify unaffected tenants, unaffected customers, unrelated cases, unrelated tool contracts, or customer environments.

## Files

| File | Purpose |
| --- | --- |
| `example-agent-recall-request.json` | Submits the emergency recall request from fleet monitoring and defines the affected agent, trigger signals, evidence references, requested actions, and authorization boundary. |
| `example-recall-policy-decision.json` | Records the policy decision for the recall request, including validation results, allowed actions, required approvals, enforcement conditions, and fail-closed checks. |
| `example-recall-approval-record.json` | Records human approval for sensitive recall actions and binds the approval to the request, policy decision, affected scope, and required reviewer roles. |
| `example-recall-audit-event.json` | Records enforcement results, state transitions, boundary checks, evidence preservation, and replayable facts for the recall. |

## Governance model

A recall request is not an authorization to execute recall actions. The request must be evaluated by a policy decision point, released through a policy enforcement point, and approved by required human reviewers before sensitive actions are enforced.

Sensitive recall actions require human approval before enforcement:

| Action ID | Action | Human approval |
| --- | --- | --- |
| `recall-action-001` | Suspend `pkg-soc-triage-agent:2.7.3` | Required |
| `recall-action-002` | Stop active and scheduled sessions for the affected scope | Required |
| `recall-action-003` | Revoke credentials bound to the affected agent version | Required |
| `recall-action-004` | Block tools registered to the affected agent version | Required |
| `recall-action-005` | Quarantine affected case memory and runtime context | Required |
| `recall-action-006` | Preserve supporting evidence and related audit records | Not required |

Evidence preservation does not require separate human approval because it preserves recall evidence and audit records by reference and does not authorize evidence modification.

## Authorization boundaries

The recall artifacts do not authorize:

- Customer environment containment
- Customer environment remediation
- Customer notification release
- Case closure
- Evidence modification
- Agent redeployment
- Cross-customer data sharing
- Policy exceptions
- Scope expansion beyond affected tenants, customers, cases, sessions, tools, memory, and downstream outputs

Customer approval is not required for the agent recall itself. Customer notification release remains outside the recall authorization and requires separate review.

## Evidence handling

Supporting evidence is handled by reference only. Raw evidence is not embedded in the recall artifacts.

The request references:

| Evidence reference | Evidence type | Source system |
| --- | --- | --- |
| `evidence-ref-agent-runtime-log-0001` | `agent_runtime_log` | `agent-fleet-monitoring` |
| `evidence-ref-policy-eval-0002` | `policy_evaluation_record` | `policy-enforcement-service` |
| `evidence-ref-tool-request-0003` | `tool_request_audit_record` | `tool-access-audit` |

Each evidence reference includes a time range and hash reference so audit replay can confirm what was reviewed without copying raw evidence into the example artifact.

## Knowledge and memory controls

Memory access is allowed only for investigation of the affected sessions. Memory reuse is blocked, affected runtime context must be quarantined, and retrieved context must not be released. Quarantined context must not be used for training, downstream generalization, or cross-customer intelligence release.

## Fail-closed conditions

Recall enforcement must fail closed when any required control cannot be validated, including:

- Affected agent identity cannot be verified
- Agent package version cannot be verified
- Tenant or customer scope is missing or ambiguous
- Policy bundle reference is missing or mismatched
- Required policy decision is unavailable
- Required approval is missing or expired
- Evidence reference validation fails
- Audit logging is unavailable
- Requested action exceeds recall scope

When a fail-closed condition is triggered, unexecuted recall actions must be denied until the condition is resolved and the required authorization chain is restored.

## Enforcement sequence

The example audit event records enforcement in the following order:

1. Preserve recall evidence and related audit records.
2. Suspend the affected agent package version.
3. Stop active and scheduled sessions in scope.
4. Revoke credentials bound to the affected agent version.
5. Block registered tool access for the affected agent version.
6. Quarantine affected runtime context and case memory.

Each enforcement action must validate policy decision, approval where required, scope, boundary controls, and audit availability before execution.

## Audit replay

The audit trail must reconstruct:

- Why the recall was requested
- Which agent version was affected
- Which tenants, customers, and cases were in scope
- Which actions were requested
- Which evidence references supported the request
- Which policy decision and approval records authorized or denied recall actions
- Which enforcement actions were executed or blocked
- Whether tenant, customer, memory, evidence, and tool boundaries were maintained

Required correlation fields include `request_id`, `correlation_id`, `agent_id`, `agent_package_id`, `agent_package_version`, `tenant_ids`, `customer_ids`, `case_ids`, `policy_bundle_id`, `tool_contract_id`, and `evidence_refs`.

## Validation points

Use this example to validate that an agent recall implementation can:

- Separate recall request, policy decision, human approval, enforcement, and audit replay records.
- Bind all artifacts to the same request and correlation identifiers.
- Constrain emergency action to affected production scope.
- Require human approval for sensitive recall actions.
- Preserve evidence by immutable reference without modifying source evidence.
- Quarantine affected memory and block reuse.
- Deny actions that exceed recall scope or lack required authorization.
- Produce an audit record that supports deterministic replay of the recall decision and enforcement path.
