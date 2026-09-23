# Approval Workflows

## Purpose

This file defines baseline approval workflow requirements for governed Agentic MSSP / MDR / DFIR security operations.

Approval workflows provide the human accountability path for sensitive, high-impact, customer-facing, tenant-scoped, or evidence-dependent decisions. They are used when an agentic workflow, analyst workflow, policy decision, or operational process requires explicit human authorization before the action, recommendation, report, escalation, or handoff can proceed.

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

## Scope

Approval workflows apply to human-oversight decisions across:

- Managed SOC / MSSP triage and reporting
- MDR investigation and containment guidance
- Cloud incident response coordination
- Private/local LLM-assisted DFIR workflows
- Customer-facing outputs
- Escalation decisions
- Governance evidence review
- Sensitive operational recommendations
- Approval gates returned by policy-enforcement workflows

This file does not define the full PDP decision contract, PEP enforcement contract, Agent Judge evaluation model, evidence validation model, or tenant-isolation model. Those controls belong in their respective architecture areas. This file defines how human approval is requested, evaluated, recorded, constrained, expired, and audited.

## Architecture Alignment

Approval workflows sit in the Human Oversight layer and interact with the Agentic SOC / Orchestration Layer, AI Assurance & Analytics Layer, Governance / Control Plane, Agent Governance & Identity Control Plane, service towers, and customer-facing operational outcomes.

Approval workflows are not autonomous agents. They are accountability and decision-control mechanisms for governed operations.

Microsoft Entra Agent ID and Microsoft Agent 365 belong in the Agent Governance & Identity Control Plane. They should be treated as identity, lifecycle, trust, and governance services in this reference architecture, not as operational SOC agents.

## Control Boundary

Approval workflows enforce the boundary between:

- agent-generated recommendations and authorized operational action
- analyst review and privileged execution
- internal analysis and customer-facing reporting
- policy evaluation and human accountability
- evidence-supported findings and unsupported conclusions
- routine investigation and high-impact operational decisions
- tenant-scoped workflows and cross-tenant risk

An approval workflow MUST NOT allow an agent, model, tool, or automation path to bypass required human authorization.

## Approval Workflow Principles

Approval workflows MUST be:

| Principle | Requirement |
|---|---|
| Explicit | Approval requirements MUST be represented as explicit workflow state, not implied by comments or informal communication. |
| Scoped | Approval MUST apply only to the specified tenant, customer, case, action type, evidence set, risk level, and time window. |
| Attributable | The approver identity, authority, decision, timestamp, and decision rationale MUST be recorded. |
| Evidence-bound | Approval for DFIR conclusions, operational recommendations, containment guidance, governance evidence, or customer-facing output MUST reference supporting evidence. |
| Policy-constrained | Human approval MUST NOT override a PDP DENY decision unless the request is routed through a separately governed exception process explicitly permitted by policy. |
| Expiring | Scoped approval MUST include an expiration or validity boundary. |
| Auditable | Approval decisions, rejections, escalations, expirations, revocations, and exception reviews MUST be audit logged. |
| Fail-closed | Missing, expired, ambiguous, unauthorized, or unverifiable approval MUST block the workflow. |

## When Approval Is Required

Human approval MUST be required when a proposed action, output, or decision affects any of the following:

| Area | Approval Requirement |
|---|---|
| Containment | Isolation, blocking, disabling, quarantine, credential reset, access revocation, or equivalent containment recommendation or action. |
| Escalation | Escalation to customer leadership, DFIR leadership, legal, compliance, executive stakeholders, or external parties. |
| Customer-facing reporting | Reports, summaries, recommendations, attestations, incident updates, post-incident material, or governance evidence sent outside the operating team. |
| DFIR conclusions | Root cause, scope, impact, timeline, attribution-sensitive statements, exfiltration assessment, malware findings, chain-of-custody implications, or final incident conclusions. |
| Evidence handling | Evidence collection, retention, export, transformation, release, deletion, chain-of-custody claims, or sensitive evidence disclosure. |
| Tenant-boundary decisions | Cross-tenant ambiguity, mismatched tenant context, shared service context, customer ownership uncertainty, or data-source ownership ambiguity. |
| Privileged action | Actions requiring elevated permissions, scoped credentials, administrative access, break-glass access, or policy exception. |
| Governance evidence | Artifacts used for audit, assurance, executive review, control validation, or contractual/customer obligations. |
| Approval routing | Changes to approval path, approver authority, customer approval requirement, escalation path, or exception process. |
| High-impact internal decisions | Operational response decisions that may materially affect customer operations, investigation direction, service delivery, containment posture, or evidence integrity. |

Human review MUST be required when model output is materially uncertain, evidence is incomplete, the proposed action is irreversible, or operational risk is not clearly classified and the output affects DFIR conclusions, customer-facing reporting, containment recommendations, escalation, governance evidence, approval routing, or operational response decisions.

## Approval Workflow Triggers

Approval workflows MUST define explicit trigger conditions instead of relying on subjective judgment alone. Baseline triggers SHOULD include:

| Trigger | Description |
|---|---|
| PDP `REQUIRE_APPROVAL` | Policy permits the request only after approved human authorization. |
| High action risk | The proposed action exceeds the threshold for automated or analyst-only handling. |
| Customer-facing output | The output will be shared with a customer, external party, executive stakeholder, or governance audience. |
| DFIR materiality | The output affects findings, scope, impact, timeline, evidence interpretation, or report conclusions. |
| Evidence sensitivity | The workflow uses privileged, sensitive, regulated, customer-owned, forensic, or chain-of-custody evidence. |
| Tenant uncertainty | Tenant, customer, workspace, case, evidence, identity, or destination context is incomplete, ambiguous, mismatched, or cross-tenant. |
| Operational impact | The action may affect service availability, identity posture, endpoint state, workload state, incident response posture, or customer trust. |
| Exception request | A request requires deviation from standard policy, process, scope, timing, authority, or approval path. |

## Required Inputs

Approval workflows MUST receive enough context to support an accountable decision.

| Input | Requirement |
|---|---|
| approval_request_id | MUST uniquely identify the approval request. |
| workflow_id | MUST identify the originating workflow, run, case, or process. |
| approval_status | MUST represent the current workflow state where approval is being requested, evaluated, revalidated, expired, revoked, escalated, or blocked. |
| tenant_id / customer_id | MUST be included when the workflow is tenant-scoped, customer-scoped, or multi-tenant. |
| case_id / incident_id | MUST be included when the decision relates to an investigation, alert, incident, ticket, or DFIR matter. |
| requested_action | MUST describe the proposed action, output, recommendation, release, escalation, or exception. |
| action_risk_level | MUST classify the operational risk of the requested action where risk classification is used. |
| approval_reason | MUST explain why approval is required. |
| evidence_references | MUST be included when the decision relies on evidence, investigation context, DFIR findings, governance evidence, or customer-facing content. |
| knowledge_store_or_memory_scope | MUST be included where retrieval, memory, customer-facing output, governance evidence, evidence handling, approval routing, reuse, release, or DFIR conclusions affect the approval decision. |
| knowledge_memory_scope_result | MUST be included where retrieval or memory scope was evaluated and affects the approval decision, customer-facing output, governance evidence, evidence handling, approval routing, reuse, release, or DFIR conclusions. |
| data_classification | MUST be included where sensitive data handling, release, reuse, customer-facing output, governance evidence, evidence handling, approval routing, or DFIR conclusions affect the approval decision. |
| sensitivity_label | MUST be included where sensitivity, privacy, legal, customer-specific handling, release, reuse, customer-facing output, governance evidence, evidence handling, approval routing, or DFIR conclusions affect the approval decision. |
| allowed_use | MUST be included where use is constrained by workflow, case, customer, legal, governance, evidence-handling, reporting, reuse, customer-facing output, or DFIR purpose. |
| retention_policy_id | MUST be included where retention, reuse, evidence handling, customer-facing output, governance evidence, approval routing, or DFIR conclusions affect the approval decision. |
| output_destination | MUST be included when the approved item may be sent, published, executed, exported, or released. |
| requester_identity | MUST identify the human, agent, workflow, service, or process requesting approval. |
| requester_authority_context | SHOULD identify the requester role, team, tenant authorization, and case relationship. |
| reviewer_authority_scope | MUST identify or validate that the approver is authorized for the tenant, customer, case, action type, evidence sensitivity, and risk level. |
| policy_decision_reference | MUST be included when approval is triggered by PDP `REQUIRE_APPROVAL` or related policy evaluation. |
| agent_or_tool_context | MUST be included when the request was generated, enriched, recommended, or routed by an agent, model, tool, or automation. |
| approval_expiration / approval_valid_until | MUST be included where scoped approval is used. |
| rollback_or_recovery_context | SHOULD be included when the action has operational impact and reversal or mitigation may be required. |

Substantive approval review MUST NOT proceed unless the review package includes enough context to support an accountable decision. If required inputs are missing, inconsistent, expired, unauthorized, or unverifiable, the workflow MUST remain blocked until corrected, rejected, escalated, or routed to a governed exception process.

## Approval Decision Outcomes

Human approval workflows MUST define explicit allowed approval outcomes.

Baseline outcomes SHOULD include:

| Outcome | Meaning |
|---|---|
| APPROVED | The request is approved within the defined scope, conditions, and expiration boundary. |
| REJECTED | The request is not approved and MUST NOT proceed under the current approval request. |
| REQUEST_MORE_EVIDENCE | The request lacks sufficient evidence, context, or validation for approval. |
| ESCALATE | The request requires review by a higher authority, different team, customer authority, DFIR lead, legal/compliance function, or exception process. |
| APPROVED_WITH_CONDITIONS | The request is approved only if specified conditions, scope limits, or compensating controls are satisfied. |
| EXPIRED | The approval request or prior approval is no longer valid. |
| REVOKED | A previously granted approval is withdrawn before execution or continued use. |
| BLOCKED_FAIL_CLOSED | The workflow is blocked because required approval, context, authority, evidence, or auditability is missing or invalid. |

Approval outcomes MUST be represented as structured workflow state. Free-text comments alone MUST NOT be treated as approval.

## Approval Attributes

Every approval decision MUST include:

| Attribute | Requirement |
|---|---|
| approval_request_id | Links the decision to the request. |
| decision_outcome | Records the explicit approval outcome. |
| approval_status | Records the current workflow state, such as pending, approved, rejected, expired, revoked, escalated, or blocked_fail_closed. |
| approver_identity | Identifies the approving or rejecting human authority. |
| approver_role | Identifies the approver function or responsibility. |
| reviewer_authority_scope | Records or references the approver’s authority scope. |
| decision_timestamp | Records when the decision occurred. |
| decision_rationale | Explains the basis for the decision. |
| approved_scope | Defines tenant, customer, case, action, evidence, tool, output, and destination boundaries. |
| approval_valid_until | Defines expiration where scoped approval is used. |
| conditions | Records required conditions or limits when approval is conditional. |
| evidence_references_reviewed | Records the evidence references considered by the approver. |
| knowledge_store_or_memory_scope | Records approved retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse scope where retrieval or memory affects approval. |
| knowledge_memory_scope_result | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| data_classification | Records classification context for the approved item. |
| sensitivity_label | Records sensitivity, handling, privacy, legal, or customer-specific label context. |
| allowed_use | Records permitted downstream use of the approved item. |
| retention_policy_id | Records retention and disposal boundary for the approved item. |
| human_review_record_id | Links approval to the human review record where human review is required or completed. |
| customer_approval_record_id | Links approval to customer authorization where customer approval is required. |
| policy_decision_reference | Links to PDP decision context when applicable. |
| audit_event_id | Links the decision to the audit trail. |

## Approval Scope

Approval MUST be narrowly scoped. An approval for one action, tenant, customer, case, evidence set, destination, or time window MUST NOT be reused for a different action or context unless policy explicitly permits reuse and the reuse is audit logged.

Approval scope MUST include the applicable attributes needed to bind the approval to the specific tenant, customer, case, action, evidence set, destination, approver authority, and validity window. Baseline scope attributes SHOULD include:

- tenant or customer boundary
- case, incident, or ticket boundary
- requested action
- action risk level
- evidence references
- output destination
- tool or workflow boundary
- approver authority scope
- expiration time
- required conditions
- rollback or review requirements where applicable

## Relationship to PDP Decisioning and PEP Enforcement

Approval workflows do not replace policy enforcement.

| PDP Result | Approval Workflow Behavior |
|---|---|
| ALLOW | The workflow MAY proceed if no separate approval requirement applies. |
| REQUIRE_APPROVAL | The workflow MUST remain blocked until valid approval becomes bound evidence and the request returns to the PDP for reevaluation. |
| DENY | The workflow MUST fail closed. Escalation MAY occur only for separately governed exception review where explicitly permitted by policy, and MUST NOT permit execution by default. |

Human approval is bound evidence that returns to the PDP for reevaluation; it does not directly authorize execution. Only the resulting PDP permit reaches the PEP.

The PEP MUST enforce the resulting PDP decision and obligations before authorizing access. If the PEP cannot verify valid approval, approval scope, approval expiration, approver authority, or required audit logging, the workflow MUST fail closed.

The PEP or workflow gate MUST revalidate approval status, scope, expiration, approver authority, and required conditions before execution or release.

Human approval MUST NOT be used to soften or bypass policy denial. Exception handling, if permitted, MUST be separately governed, explicitly authorized by policy, and independently audited.

## Human-in-the-Loop and Human-on-the-Loop

Approval workflows may support both HITL and HOTL operating models.

| Model | Use |
|---|---|
| HITL | Required before an action, output, escalation, report, or handoff can proceed. |
| HOTL | Used for monitoring, review, tuning, retrospective assessment, quality assurance, and escalation readiness. |

HITL MUST be used where approval is a required control boundary. HOTL MUST NOT be substituted for HITL when pre-action approval is required.

## Customer Approval

Customer approval MUST be required when the workflow affects customer-facing reporting, customer-authorized containment, customer evidence release, externally visible recommendations, contractual escalation, or customer-owned operational risk.

Customer approval workflows MUST define the required approval attributes. Baseline attributes SHOULD include:

- authorized customer approver
- customer tenant or business context
- case or incident scope
- approved action or release
- evidence references
- reporting destination
- expiration or validity window
- constraints or conditions
- audit record

Customer approval MUST NOT be assumed from general engagement participation, prior discussion, ticket comments, or informal communication unless the operating model explicitly permits that form of approval and captures it in the audit trail.

## Escalation and Exception Review

Escalation is required when the approval requester, analyst, or approver cannot make an accountable decision within their authority scope.

Escalation SHOULD occur for:

- uncertain tenant or customer ownership
- high-impact containment or recovery decisions
- legal, regulatory, privacy, contractual, or executive sensitivity
- material DFIR uncertainty
- disputed evidence interpretation
- policy exception requests
- customer disagreement or unclear authorization
- urgent break-glass scenarios
- unresolved model uncertainty affecting operational decisions

Exception review MUST be separate from normal approval. It MAY document risk acceptance, emergency handling, or reclassification review only where explicitly permitted by policy. It MUST NOT automatically permit execution.

## Break-Glass Approval

Break-glass approval is an emergency path for time-sensitive, high-impact situations where normal approval routing is unavailable or insufficient.

Break-glass approval MUST include:

- emergency justification
- requester identity
- approver identity
- action scope
- tenant or customer scope
- case or incident scope
- time-bound validity
- evidence or operational basis
- compensating controls where available
- post-event review requirement
- audit record

Break-glass approval MUST NOT become a routine path for avoiding normal approval gates. Post-event review MUST be performed.

## Fail-Closed Conditions

Approval workflows MUST fail closed when:

- required approval is missing
- approval is expired
- approval scope does not match the requested action
- approver authority cannot be validated
- tenant, customer, case, evidence, or destination context is missing, ambiguous, or mismatched
- PDP returns `DENY`
- PDP returns `REQUIRE_APPROVAL` and no valid approval exists
- required evidence references are missing or unverifiable
- customer approval is required but missing
- audit logging fails
- required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, retention policy, human review record, approval record, or customer approval record is missing, expired, revoked, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where approval, customer-facing release, DFIR conclusions, governance evidence, approval routing, or downstream use depends on it
- approval status cannot be determined
- approval state is inconsistent across systems
- approval conditions are not satisfied
- requester identity or workflow identity cannot be validated
- the workflow attempts to reuse approval outside approved scope

Fail-closed handling MUST preserve the request context, denial or escalation reason, approver context, approval status, and evidence references needed for review where technically available. If audit logging or context preservation fails, the workflow MUST remain blocked until reviewed or remediated.

## Audit Requirements

Approval workflows MUST audit:

- approval request creation
- requester identity
- approver identity
- reviewer authority scope
- tenant, customer, case, and evidence context
- knowledge_store_or_memory_scope where retrieval or memory affects approval, customer-facing release, DFIR conclusions, governance evidence, approval routing, or downstream use
- knowledge_memory_scope_result where retrieval or memory scope was evaluated
- data_classification, sensitivity_label, allowed_use, and retention_policy_id where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved
- human_review_record_id, approval_record_id, and customer_approval_record_id where review, formal approval, or customer approval is required or completed
- requested action
- action risk level
- policy decision reference
- approval outcome
- decision rationale
- approval conditions
- approval expiration
- approval revocation
- escalation path
- exception review path
- break-glass use
- customer approval where applicable
- failed, blocked, or expired approval attempts
- execution attempt following approval
- mismatch between approval scope and requested execution
- audit or context preservation failure

Audit records MUST be tamper-resistant according to organizational logging and retention requirements. They SHOULD be searchable and linked to the case, incident, workflow, policy decision, and evidence references where applicable.

## What Humans Approve

Humans may approve:

- proceeding with scoped containment recommendation or action
- releasing customer-facing content
- accepting DFIR conclusions for reporting
- escalating to another team or authority
- approving conditional workflow continuation
- authorizing scoped evidence handling
- approving time-bound privileged action
- accepting risk within their authority
- routing to exception review
- requesting more evidence before decision

Humans MUST approve within their assigned authority scope. Approval outside the approver’s authority MUST be blocked or escalated.

## What Humans Must Not Approve

Humans MUST NOT approve:

- actions outside policy-permitted scope
- execution after PDP `DENY` outside a separately governed exception process
- tenant-ambiguous or cross-tenant actions without verified authorization
- customer-facing claims unsupported by evidence
- DFIR conclusions based only on model output
- evidence release without verified authority
- privileged action without scoped authorization
- approval reuse outside the approved tenant, customer, case, action, evidence, destination, or time window
- bypass of audit logging
- informal approval paths that cannot be reconstructed
- agent-generated approval of its own request

## F7-LAS Alignment

F7-LAS may be used as a supporting control lens for approval workflows.

Approval workflows primarily align with:

- L4 Tool Layer, where mediated tool execution requires gated authorization for sensitive actions.
- L5 Policy Engine Layer, where PDP decisions may require human approval and the PEP enforces the resulting decision and obligations before authorizing access.
- L6 Sandbox / Blast-Radius Layer, where approval constrains operational scope and impact.
- L7 Monitoring & Evaluation, where approval decisions, escalations, exceptions, and audit events remain observable and auditable.

F7-LAS should support the architecture’s accountability model. It should not replace the MSSP / MDR / DFIR operating model or become the primary subject of this file.

## Acceptance Criteria

An approval workflow is acceptable when:

- approval requirements are explicit and policy-aligned
- required approval inputs are defined and validated
- approver identity and authority are verified
- approval outcomes are structured and auditable
- scoped approvals include expiration or validity boundaries
- PDP `REQUIRE_APPROVAL` cannot proceed without valid approval
- PDP `DENY` fails closed unless routed to separately governed exception review explicitly permitted by policy
- customer approval is required for customer-facing or customer-authorized decisions
- DFIR conclusions and reporting approvals are evidence-bound
- missing, expired, ambiguous, or unauthorized approval blocks the workflow
- approval decisions are traceable to tenant, customer, case, action, evidence, policy, and audit context
- approval records support audit replay across requester identity, approver identity, approver authority, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, approval record, customer approval record, decision rationale, approval outcome, routing, and downstream use
- humans cannot approve outside their authority scope
- approval state cannot be forged, implied, or inferred from unstructured comments alone
- fail-closed behavior preserves review context where technically available

## Anti-Patterns

Avoid the following:

- treating analyst comments as approval without structured workflow state
- allowing agents to approve their own requests
- allowing approval to override PDP `DENY` without governed exception review
- using broad standing approvals for unrelated actions
- reusing approval across tenants, customers, cases, destinations, or time windows
- approving customer-facing content without evidence references
- approving DFIR conclusions based only on model output
- allowing HOTL review where HITL approval is required
- using break-glass as a routine approval path
- permitting approval without approver authority validation
- omitting approval expiration for scoped approval
- failing open when approval state is missing or unverifiable
- bypassing audit logging for urgent or internal workflows
- treating Agent Judge output as approval
- treating policy evaluation as human authorization
- placing identity governance services in the operational SOC agent layer
