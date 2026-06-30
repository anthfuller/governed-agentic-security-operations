# Escalation Paths

## Purpose

This file defines baseline escalation path requirements for governed Agentic MSSP / MDR / DFIR security operations.

Escalation paths provide controlled routing when an analyst, agentic workflow, approval workflow, Agent Judge finding, policy decision, evidence issue, tenant/customer boundary issue, or operational risk cannot be resolved within the current workflow authority.

Escalation paths do not authorize tool execution, approve customer-facing release, replace PDP decisions, replace PEP enforcement, replace human review, replace customer approval, or certify forensic validity.

## Scope

This file applies to escalation paths for:

- Agent-generated triage, enrichment, investigation, and recommendation outputs.
- Analyst review outcomes requiring higher authority.
- Approval workflows requiring different approver authority.
- PDP `REQUIRE_APPROVAL`, PDP `DENY`, or policy exception routing.
- Agent Judge findings that identify unresolved evidence, tenant-boundary, unsupported-claim, output-quality, or HITL risks.
- Customer-facing reports, executive summaries, governance evidence, legal-sensitive outputs, and DFIR conclusions.
- Containment, remediation, access-change, evidence-release, escalation, closure, or customer-notification recommendations.
- Private/local LLM-assisted DFIR evidence analysis and report drafts.
- Cross-tenant, cross-customer, cross-case, retrieval/memory, evidence, retention, or output-destination ambiguity.

This file does not define PDP decision logic, PEP enforcement behavior, Agent Judge scoring, evidence collection procedures, customer approval workflow design, or incident command procedures.

## Non-Goals

Escalation paths MUST NOT be used to:

- Treat escalation as approval.
- Treat escalation as PDP authorization.
- Treat escalation as permission to execute a tool or action.
- Treat escalation as customer-facing release approval.
- Treat escalation as legal, compliance, regulatory, or forensic certification.
- Allow agents to self-escalate into approval, self-approve, or bypass governed workflows.
- Override a PDP `DENY` unless routed through a separately governed exception process explicitly permitted by policy.
- Treat private/local LLM execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## Escalation Principles

| Principle | Requirement |
|---|---|
| Explicit routing | Escalation MUST be represented as structured workflow state, not implied by comments or informal communication. |
| Scoped authority | Escalation MUST route to an authority valid for the tenant, customer, case, evidence, action type, risk level, and output destination. |
| Tenant and customer separation | `tenant_id` and `customer_id` MUST remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows. |
| Evidence-bound escalation | Escalation involving findings, recommendations, DFIR conclusions, governance evidence, or customer-facing output MUST preserve evidence references. |
| Retrieval and memory boundary control | Escalation involving RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context MUST preserve knowledge store or memory scope. |
| Review is not approval | Escalation for review MUST NOT be treated as formal approval unless a formal approval workflow explicitly provides that authority. |
| Customer approval is explicit | Escalation to customer approval MUST preserve customer approver, scope, evidence, action, destination, and expiration context. |
| Fail closed | Missing, ambiguous, unauthorized, stale, expired, revoked, inconsistent, unauditable, or out-of-scope escalation context MUST block or route to controlled review. |
| Auditability | Escalation decisions, routing, rationale, outcomes, and downstream use MUST be auditable. |

## Escalation Triggers

Escalation MUST occur when the current workflow, analyst, approver, agentic process, or service tower cannot make an accountable decision within scope.

| Trigger | Escalation Requirement |
|---|---|
| Tenant or customer ambiguity | Escalate to tenant-boundary, customer-boundary, governance, or service-owner review. |
| Cross-tenant or cross-customer risk | Escalate to governance and fail closed unless explicit authorization exists. |
| Evidence insufficiency | Escalate to evidence owner, DFIR lead, or request-more-evidence path. |
| Unsupported claim risk | Escalate to analyst review, output correction, or assurance review. |
| DFIR materiality | Escalate to DFIR lead, incident commander, legal, or customer approval path where applicable. |
| Customer-facing release | Escalate to customer-facing review or customer approval before release. |
| Legal, regulatory, privacy, or contractual sensitivity | Escalate to legal, compliance, privacy, governance, or customer authority. |
| Containment or remediation impact | Escalate to incident commander, service owner, customer approver, or formal approval workflow. |
| PDP `REQUIRE_APPROVAL` | Escalate to the approval workflow and remain blocked until valid approval exists. |
| PDP `DENY` | Fail closed; escalate only to separately governed exception review where policy explicitly permits. |
| Retrieval or memory scope uncertainty | Escalate to retrieval, knowledge-store, evidence, tenant-boundary, or governance review. |
| Private/local DFIR uncertainty | Escalate to examiner, DFIR lead, or evidence owner before reportable use. |

## Required Escalation Inputs

Escalation workflows MUST receive enough context to support accountable routing and decision-making.

| Input | Requirement | Purpose |
|---|---|---|
| `escalation_request_id` | MUST | Unique identifier for the escalation request. |
| `workflow_id` | MUST | Identifies the originating workflow, run, case, or process. |
| `workflow_stage` | MUST when routing or authority depends on stage | Identifies triage, investigation, DFIR, containment, reporting, closure, approval, exception, or customer-release stage. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` or `incident_id` | MUST when escalation relates to an investigation, alert, incident, ticket, or DFIR matter | Links escalation to the governed operational record. |
| `requester_identity` | MUST | Identifies the human, agent, workflow, service, or process requesting escalation. |
| `requester_authority_context` | MUST when routing depends on requester authority | Identifies requester role, team, tenant authorization, and case relationship. |
| `agent_id` | MUST when an agent generated, influenced, or routed the escalated item | Identifies the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent generated, influenced, or routed the escalated item | Supports replay and run-level traceability. |
| `escalation_reason` | MUST | Explains why escalation is required. |
| `requested_escalation_path` | MUST | Identifies target reviewer, approver, service tower, DFIR lead, legal/compliance function, governance function, or customer authority. |
| `escalation_risk_level` | MUST when risk affects routing or urgency | Classifies the operational, customer, evidence, legal, or governance risk. |
| `evidence_object_ids` | MUST when escalation relies on evidence, investigation context, DFIR findings, governance evidence, or customer-facing content | Preserves evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context affects the escalation | Defines approved retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| `data_classification` | MUST when classification affects routing, release, reuse, evidence handling, approval, or downstream use | Preserves data-handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when use is constrained to workflow, case, customer, legal, governance, evidence-handling, reporting, or DFIR purposes | Defines permitted downstream use. |
| `retention_policy_id` | MUST when retention affects evidence, retrieved context, output storage, release, reuse, or disposal | Preserves retention boundary. |
| `output_destination` | MUST when release, routing, disclosure, reporting, evidence handling, governance evidence, or downstream use depends on destination | Identifies where output is sent, stored, released, displayed, or consumed. |
| `policy_decision_reference` | MUST when escalation is triggered by PDP result or policy obligation | Links escalation to policy context. |
| `human_review_record_id` | MUST when escalation follows human review | Links escalation to the review outcome. |
| `approval_record_id` | MUST when escalation depends on formal approval state | Links escalation to approval context. |
| `customer_approval_record_id` | MUST when customer-side approval is required or completed | Links escalation to customer authorization. |
| `audit_reference_id` | MUST when escalation is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, review, approval, customer approval, and audit records. |

## Escalation Path Types

| Escalation Path | Required Use |
|---|---|
| Analyst escalation | Use when the current analyst lacks authority, evidence, context, or confidence to validate the output. |
| Service tower escalation | Use when the issue belongs to another SOC, MDR, cloud, identity, endpoint, network, or platform team. |
| DFIR lead escalation | Use when findings affect DFIR conclusions, timelines, evidence interpretation, reportable findings, or forensic handling. |
| Incident commander escalation | Use when decisions materially affect response strategy, containment posture, recovery, communications, or closure. |
| Governance escalation | Use when policy exceptions, control gaps, tenant/customer ambiguity, or compliance-sensitive handling is involved. |
| Legal/privacy/compliance escalation | Use when legal-sensitive, privacy-sensitive, regulatory, contractual, or breach-notification issues may be involved. |
| Customer approver escalation | Use when customer authorization is required for release, evidence handling, containment, remediation, reporting, or external disclosure. |
| Exception review escalation | Use only when policy permits a separately governed exception path. |
| Break-glass escalation | Use only for emergency time-sensitive scenarios with scoped authority, audit, and post-event review. |

## Escalation Outcomes

Escalation workflows MUST define explicit outcomes.

| Outcome | Meaning |
|---|---|
| `ESCALATED_FOR_REVIEW` | The item has been routed to an authorized reviewer or team for evaluation. |
| `ESCALATED_FOR_APPROVAL` | The item has been routed to a formal approval workflow. |
| `ESCALATED_TO_CUSTOMER_APPROVER` | The item has been routed for customer-side authorization. |
| `ESCALATED_TO_DFIR_LEAD` | The item has been routed to DFIR leadership or examiner authority. |
| `ESCALATED_TO_GOVERNANCE` | The item has been routed for governance, policy, risk, or exception review. |
| `REQUEST_MORE_EVIDENCE` | Additional evidence or context is required before downstream use. |
| `CORRECT_AND_RESUBMIT` | The output or request must be corrected before further review. |
| `BLOCKED_FAIL_CLOSED` | The workflow cannot proceed because required context, approval, review, policy, evidence, or auditability is missing or invalid. |
| `OUT_OF_SCOPE` | The escalation path is not valid for the requested item. |

Escalation outcomes are routing states. They MUST NOT be represented as authorization decisions unless produced by the governed PDP or formal approval workflow.

## Relationship to PEP/PDP

Escalation paths do not replace policy enforcement.

| PDP Result | Escalation Handling |
|---|---|
| `ALLOW` | Escalation MAY occur for quality, review, evidence, customer, governance, or operational reasons, but is not required by the PDP result alone. |
| `REQUIRE_APPROVAL` | Escalation MUST route to the appropriate approval path and the workflow MUST remain blocked until valid approval exists. |
| `DENY` | The workflow MUST fail closed. Escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default. |

The PEP MUST enforce the PDP decision and returned obligations. If escalation context, approval context, authority, or audit logging cannot be verified where required, the workflow MUST fail closed.

## Human Review and Approval Boundaries

Human review and escalation MUST remain separate from formal approval unless a formal approval workflow explicitly provides that authority.

Escalation MAY route to:

- human review,
- formal approval,
- customer approval,
- DFIR lead review,
- incident commander review,
- legal/compliance/privacy review,
- governance review,
- exception review,
- correction,
- request-more-evidence handling.

Escalation MUST NOT convert unsupported claims, missing evidence, unresolved Agent Judge findings, or policy denial into approved operational facts.

## Customer Escalation Requirements

Customer escalation MUST be used when customer authorization, customer notification, customer-facing release, customer-owned evidence handling, customer-impacting containment, contractual escalation, or external disclosure is required.

Customer escalation MUST preserve:

- customer identity,
- tenant context,
- case or incident scope,
- evidence references,
- data classification,
- sensitivity label,
- allowed use,
- retention policy,
- output destination,
- requested action or release,
- customer approver identity where applicable,
- approval or customer approval record where applicable,
- expiration or validity boundary where applicable,
- audit reference.

Customer escalation MUST NOT be assumed from ticket comments, informal communication, prior engagement participation, or general awareness unless the operating model explicitly permits that form of authorization and captures it in the audit trail.

## Private / Local LLM-Assisted DFIR Escalation

For private/local LLM-assisted DFIR workflows, escalation MUST occur when:

- The model output affects reportable DFIR conclusions.
- Evidence references are missing, ambiguous, or inconsistent.
- Timeline reconstruction cannot be validated from evidence.
- Extracted artifacts are not traceable to source evidence.
- The output introduces unreferenced artifacts, entities, timestamps, or conclusions.
- Knowledge store or memory scope is missing, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent.
- Customer-facing release, legal-sensitive output, governance evidence, or evidence export is involved.

Private/local execution does not make model output authoritative. It only changes where processing occurs. Examiner validation, evidence review, and required approval paths still apply.

## Fail-Closed Conditions

Escalation workflows MUST fail closed, remain blocked, or route to controlled review when:

- Required tenant, customer, workspace, case, evidence, destination, review, approval, customer approval, or policy context is missing, conflicting, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, or retention policy is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where escalation, customer-facing release, DFIR conclusions, governance evidence, approval routing, or downstream use depends on it.
- Evidence references are missing for material investigative, DFIR, governance, approval, or customer-facing output.
- Material claims are unsupported or contradicted by evidence.
- Agent Judge findings identify unresolved unsupported claims, tenant-boundary risk, evidence insufficiency, or HITL non-compliance.
- PDP returns `DENY`; escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default.
- PDP returns `REQUIRE_APPROVAL` and valid approval is not present.
- The escalation target lacks authority for the tenant, customer, case, action type, risk level, evidence sensitivity, or destination.
- Customer approval is required but missing, expired, revoked, incomplete, ambiguous, unauditable, or out of scope.
- Audit logging or context preservation fails.
- The escalation package cannot distinguish facts from model-generated inference.

Fail-closed handling MUST preserve the request context, evidence references, escalation reason, routing reason, approval context where applicable, customer approval context where applicable, and audit reference.

## Audit Requirements

Escalation workflows MUST audit:

- Escalation request identifier.
- Requester identity and authority context.
- Escalation target, target authority, service tower, role, or approval path.
- Escalation reason, risk level, outcome, and rationale.
- Tenant, customer, workspace, case, incident, alert, and service-tower context.
- Agent identity, session identity, workflow identity, and initiating user or system.
- Evidence references and evidence tenant/customer attribution metadata.
- `knowledge_store_or_memory_scope` where retrieval or memory influenced escalation, evidence interpretation, routing, customer-facing wording, governance evidence, approval package, DFIR conclusions, or downstream use.
- `knowledge_memory_scope_result` where retrieval or memory scope was evaluated.
- `data_classification`, `sensitivity_label`, `allowed_use`, and `retention_policy_id` where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- Agent Judge findings considered during escalation.
- PEP/PDP decision and obligations, where applicable.
- `human_review_record_id`, `approval_record_id`, and `customer_approval_record_id` where review, formal approval, or customer approval is required or completed.
- Output destination and approved audience.
- Review timestamp, correlation identifier, and workflow step.
- Escalation reason, rejection reason, request-more-evidence reason, or fail-closed reason.
- Known limitations or unresolved uncertainty.

If the workflow cannot create the required audit record, the escalation MUST remain blocked until the issue is reviewed or remediated.

## Operational Anti-Patterns

Avoid the following:

- Treating escalation as approval.
- Treating escalation as permission to execute.
- Treating escalation as a PDP decision.
- Treating escalation to a customer as customer approval without a customer approval record.
- Treating escalation to an analyst as formal approval.
- Allowing an agent to escalate its own request into approval without governed workflow control.
- Escalating unsupported customer-facing findings without evidence references.
- Escalating cross-tenant or cross-customer data without explicit authorization.
- Reusing escalation outcomes across tenants, customers, cases, evidence sets, destinations, or time windows.
- Allowing PDP `DENY` to proceed through informal escalation.
- Using break-glass escalation as a routine path.
- Releasing customer-facing content after escalation without required approval.
- Using local/private LLM execution as a reason to skip DFIR validation.
- Treating Agent Judge findings as optional when they identify material risk.
- Allowing missing audit records to default to approval or release.

## Acceptance Criteria

This file is acceptable when escalation paths:

- Define explicit escalation triggers, inputs, paths, outcomes, fail-closed conditions, and audit requirements.
- Preserve tenant, customer, case, evidence, destination, review, approval, and customer approval boundaries.
- Preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where retrieval or memory affects escalation or downstream use.
- Preserve data classification, sensitivity label, allowed use, and retention policy where sensitive data handling, release, reuse, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- Separate escalation from Agent Judge assurance, PEP/PDP enforcement, human review, formal approval, customer approval, tool execution, evidence authority, and forensic certification.
- Require valid approval or customer approval before customer-facing release, customer-impacting action, evidence release, or externally visible output where required.
- Define fail-closed handling for missing context, unsupported claims, invalid approvals, unauthorized escalation targets, unresolved retrieval/memory scope, and audit failures.
- Support audit replay across requester identity, escalation target, target authority, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, human review record, approval record, customer approval record, rationale, outcome, routing, and downstream use.
- Avoid product-specific implementation claims, compliance overclaims, and autonomous SOC language.

## Summary

Escalation paths ensure that unresolved risk, missing context, unclear authority, evidence gaps, customer-facing impact, DFIR uncertainty, and policy-gated decisions are routed to the correct accountable function without being mistaken for authorization, approval, or execution.
