# Cloud IAM Compromise Example

## Purpose

This example demonstrates a governed agentic workflow for a suspected **cloud identity and access management (IAM) compromise**.

The example supports the **Agentic MSSP / MDR / DFIR Security Operations Architecture** by showing how an agentic workflow can assist with cloud IAM investigation and response recommendation while preserving policy enforcement, human approval, customer scope, auditability, and safe handling of privileged actions.

This example is intentionally stronger than simple alert triage because cloud IAM compromise may involve privileged accounts, access tokens, conditional access changes, session revocation, credential reset, account disablement, tenant-wide impact, and customer-facing response decisions.

## Scenario

A cloud security signal indicates suspicious IAM activity involving a customer identity. The signal may include impossible travel, anomalous sign-in, suspicious OAuth consent, privilege escalation, token abuse, or abnormal administrative activity.

An agentic workflow is asked to review scoped context, summarize likely risk, recommend next steps, and prepare an approval request for sensitive actions if needed.

The agent must not directly disable accounts, revoke sessions, reset credentials, remove OAuth grants, change IAM policy, notify the customer, or close the incident. Any sensitive or customer-impacting action must be policy-evaluated and routed through human approval before execution.

## Service Model Applicability

| Service Model | Applicability |
|---|---|
| MSSP | Applies to managed cloud security monitoring, customer-scoped IAM triage, escalation, reporting support, and response coordination. |
| MDR | Applies to cloud IAM investigation, compromise assessment, response recommendations, and containment approval workflows. |
| SOC / Incident Response | Applies to privileged identity investigation, incident coordination, escalation, and policy-gated response support. |
| DFIR | Applies when the IAM compromise requires evidence handling, forensic timeline development, log preservation, chain-of-custody tracking, or formal incident investigation. |
| Private / Local LLM-assisted DFIR | Applies only if IAM evidence or forensic artifacts are analyzed in a local, private, isolated, or customer-controlled LLM environment. It is not required for the basic cloud IAM response example. |

## Example Files

| File | Purpose |
|---|---|
| `README.md` | Explains the example scenario, workflow, controls, approval path, auditability, failure paths, and related patterns. |
| `example-request.json` | Shows the incoming cloud IAM compromise request with tenant, customer, identity, incident, workflow, tool, retrieval, and output scope. |
| `example-approval-record.json` | Shows the human approval record for a sensitive action, including scope, reviewer, conditions, expiration, and customer authorization handling. |
| `example-policy-decision.json` | Shows the PDP decision, restrictions, approval requirements, enforcement obligations, and fail-closed behavior. |
| `example-audit-event.json` | Shows the audit event correlating request, approval record, policy decision, enforcement results, and final workflow state. |

## Actors and Components

| Actor or Component | Role |
|---|---|
| Cloud security signal source | Produces the IAM compromise alert or incident signal. |
| Agentic IAM investigation workflow | Reviews scoped IAM context and proposes investigation or response recommendations. |
| Retrieval or enrichment layer | Retrieves approved customer, identity, asset, sign-in, audit, and incident context where allowed. |
| Policy Decision Point | Evaluates authorization, risk, approval requirements, output destination, tool permissions, and allowed response path. |
| Policy Enforcement Point | Enforces policy at the workflow, tool, API, retrieval, identity, and output boundaries. |
| Human approver | Reviews and approves, denies, modifies, escalates, or requests clarification for sensitive IAM actions. |
| Customer approver | Provides customer authorization where required by contract, engagement rules, or customer-impacting action. |
| Audit layer | Records request, approval, policy decision, enforcement result, output, and final workflow state. |

## Preconditions

Before this workflow runs, the system should have:

- a valid `tenant_id`;
- a valid `customer_id`;
- a valid `incident_id`;
- a valid `workflow_id`;
- an identified `agent_id`;
- a scoped cloud identity or principal under investigation;
- an approved set of cloud IAM context sources;
- authorized read-only access to relevant sign-in, audit, identity, and policy context;
- defined output destination;
- data classification and sensitivity label;
- policy rules for IAM-sensitive actions;
- approval workflow for privileged or customer-impacting response actions;
- audit and replay requirements.

## Example Flow

1. **Cloud IAM signal received**  
   A cloud IAM compromise signal is received from an approved security source.

2. **Request normalized**  
   The event is normalized into a governed workflow request with tenant, customer, incident, identity, workflow, data classification, output destination, and authorization scope.

3. **Context retrieved**  
   The workflow retrieves only approved customer-scoped and incident-scoped IAM context (e.g., sign-in activity, audit logs, role changes, OAuth consent).

4. **Agent investigation support**  
   The agent summarizes the suspected IAM compromise, identifies supporting signals, states uncertainty, and drafts a recommendation for containment.

5. **AI Assurance (Agent Judge) evaluation**  
   An independent Agent Judge evaluates the agent's draft. It verifies that the recommendation is supported by the retrieved evidence, respects tenant boundaries, and correctly flags the containment recommendation as a "sensitive action."

6. **Initial Policy decision evaluated**  
   The PDP evaluates the validated request and determines that the requested action (e.g., account disablement) triggers a `REQUIRE_APPROVAL` state.

7. **Approval request created & routed**  
   The workflow creates an approval request detailing the evidence summary, affected identity, proposed action, scope, and expiration, routing it to the authorized Incident Commander.

8. **Human approval recorded**  
   The human reviewer approves the action. A cryptographically signed human approval record is generated, binding the reviewer's identity to the specific target and time window.

9. **Final Policy Authorization & Token Minting**  
   The PDP consumes the human approval record, validates its cryptographic binding to the original request, and issues a final `ALLOW` decision alongside a time-bounded execution token.

10. **PEP enforcement applied**  
   The Tool Gateway (PEP) intercepts the execution request. It strictly validates the execution token's signature, target scope, and `expires_at` claim. If valid, the API call is executed; otherwise, it fails closed.

11. **Audit event emitted**  
   The workflow emits an immutable audit event correlating the request, judge output, approval record, policy decisions, executed tool action, and final workflow state.

## Policy and Enforcement Points

Policy evaluation should occur before:

- identity or account state is changed;
- sessions or tokens are revoked;
- credentials are reset;
- an account is disabled;
- OAuth grants or application permissions are removed;
- privileged role assignments are changed;
- IAM policies or conditional access policies are changed;
- a case record or customer-facing output is updated;
- a customer notification is sent;
- the incident is closed or downgraded.

Enforcement should occur at the real execution boundary, such as:

- workflow orchestrator;
- identity or IAM tool wrapper;
- cloud API gateway;
- retrieval layer;
- approval workflow boundary;
- output publishing path;
- audit event pipeline.

## Human Approval Triggers

Human approval should be required when a recommendation includes:

- account disablement;
- credential reset;
- session or token revocation;
- OAuth grant removal;
- privileged role removal;
- IAM policy change;
- conditional access change;
- production-impacting response;
- customer notification;
- customer-facing report release;
- incident closure;
- low-confidence but high-impact recommendation;
- ambiguous customer, tenant, identity, or incident scope.

Human approval should include enough context for the reviewer to understand why the action is recommended, what evidence supports it, what impact it may have, and what scope the approval covers.

## Customer Authorization Considerations

Some IAM actions may require customer authorization depending on service agreement, role delegation, operational impact, legal sensitivity, or customer policy.

Customer authorization may be required for:

- disabling a customer identity;
- resetting credentials;
- removing access from production systems;
- changing customer IAM or access policy;
- sending customer notification;
- releasing customer-facing incident summaries;
- exporting IAM evidence or logs;
- involving third parties.

Internal human approval should not be treated as a substitute for customer authorization when customer authorization is required.

## Evidence, Audit, and Traceability

This example may begin as cloud IAM triage, but it can escalate into incident response or DFIR if evidence preservation, timeline construction, or formal investigation is required.

Audit and traceability should include:

- request timestamp;
- tenant, customer, incident, and workflow scope;
- affected identity or principal;
- cloud source system;
- retrieved context references;
- proposed action;
- policy decision;
- approval request and approval record;
- approval conditions and expiration;
- PEP enforcement result;
- tool action attempted or blocked;
- output destination;
- customer authorization reference where required;
- audit and correlation identifiers.

For DFIR escalation, evidence references should be explicit and should include evidence object identifiers, provenance, timestamps, and chain-of-custody metadata where applicable.

## Failure and Deny Paths

The workflow should deny, fail closed, or return for clarification when:

- tenant or customer scope is missing;
- identity or principal scope is ambiguous;
- incident scope is missing;
- the agent requests cross-customer context;
- retrieved context is stale, unauthorized, or outside scope;
- the proposed action is not supported by available context;
- the action requires approval but no valid approval exists;
- approval exists but does not match action, identity, scope, or time window;
- customer authorization is required but absent;
- policy cannot be evaluated;
- output destination is missing or unauthorized;
- budget, model, or runtime constraints are exceeded.

## What This Example Should Not Do

This example should not:

- allow an agent to directly perform privileged IAM actions;
- treat recommendation as approval;
- allow approval reuse across customers, tenants, identities, incidents, or workflows;
- bypass PDP / PEP controls;
- notify the customer without required authorization;
- close the incident solely based on model output;
- retrieve unrelated customer or case context;
- treat local/private AI analysis as inherently trustworthy;
- force DFIR or Private / Local LLM-assisted DFIR controls unless the workflow escalates into evidence handling or local forensic analysis.

## Expected Control Outcome

A successful run should produce:

- a scoped cloud IAM compromise request;
- a recommendation or proposed sensitive action;
- a human approval record where sensitive action is proposed;
- a policy decision that binds the action to scope and conditions;
- PEP enforcement that allows only approved actions;
- an audit event that supports replay and accountability;
- a clear next-state outcome such as allow, deny, restrict, require approval, require customer authorization, return for clarification, or escalate.

## Acceptance Criteria

This example is acceptable when:

- the workflow is scoped to a specific tenant, customer, incident, workflow, and affected identity;
- the agent does not receive direct authority to execute privileged IAM actions;
- policy is evaluated before tool use, output write, notification, or incident state change;
- sensitive IAM actions require human approval before execution;
- customer authorization is represented where applicable;
- approval records are bounded to action, scope, identity, reviewer, conditions, and expiration;
- PEP enforcement blocks missing, invalid, expired, or mismatched approvals;
- retrieval remains customer, tenant, identity, and incident scoped;
- audit records allow the workflow to be reconstructed;
- DFIR and Private / Local LLM-assisted DFIR apply only when forensic evidence handling or local/private forensic analysis is introduced.

## Related Patterns

This example maps to:

- [`governed-agentic-security-operations-pattern.md`](../../patterns/governed-agentic-security-operations-pattern.md)
- [`policy-enforced-tool-use-pattern.md`](../../patterns/policy-enforced-tool-use-pattern.md)
- [`human-approved-sensitive-action-pattern.md`](../../patterns/human-approved-sensitive-action-pattern.md)
- [`tenant-safe-rag-memory-pattern.md`](../../patterns/tenant-safe-rag-memory-pattern.md)
- [`private-local-llm-dfir-pattern.md`](../../patterns/private-local-llm-dfir-pattern.md)
- [`control-loop.md`](../../control-loop.md)
- [`layered-architecture.md`](../../layered-architecture.md)

## Summary

This example shows how a cloud IAM compromise workflow can use agentic assistance without allowing the agent to perform privileged or customer-impacting actions directly.

The core principle is:

> Agents may investigate and recommend, but cloud IAM response actions execute only through scoped policy decisions, valid approval records, PEP enforcement, customer authorization where required, and complete auditability.
