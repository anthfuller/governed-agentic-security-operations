# HITL / HOTL Model

## Purpose

This file defines the Human-in-the-Loop (HITL) and Human-on-the-Loop (HOTL) model for governed Agentic MSSP / MDR / DFIR security operations.

The model establishes when human participation is required before a workflow proceeds, when human monitoring is sufficient, and when escalation, formal approval, customer approval, or fail-closed handling is required.

HITL and HOTL controls provide human oversight. They do not replace PDP authorization, PEP enforcement, Agent Judge assurance, formal approval workflows, customer approval paths, evidence authority, incident command authority, or forensic certification.

## Scope

This file applies to human oversight for:

- Agent-generated triage, enrichment, investigation, and recommendation outputs.
- Analyst review of investigation summaries, DFIR findings, customer-facing reports, governance evidence, and escalation recommendations.
- Approval workflow routing for sensitive, high-impact, customer-facing, evidence-dependent, or policy-gated decisions.
- Agent Judge findings that identify unsupported claims, tenant-boundary risk, evidence gaps, output-quality issues, or HITL non-compliance.
- Tool requests, tool outputs, MCP-mediated access, data ingestion, retrieval, memory, and downstream use where human oversight is required.
- Private/local LLM-assisted DFIR workflows that affect evidence interpretation, reportable findings, or customer-facing outputs.

This file does not define PDP decision logic, PEP enforcement behavior, Agent Judge scoring, evidence collection procedures, or customer approval workflow design.

## Non-Goals

The HITL / HOTL model MUST NOT be used to:

- Treat human oversight as PDP authorization.
- Treat HOTL monitoring as pre-action approval.
- Treat analyst review as formal approval unless a formal approval workflow explicitly provides that authority.
- Treat escalation as approval.
- Treat Agent Judge findings as human validation.
- Allow agents to self-approve, self-authorize, or bypass required oversight.
- Allow customer-facing release without required review or approval paths.
- Treat private/local LLM execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## HITL and HOTL Definitions

| Oversight Mode | Definition | Required Boundary |
|---|---|---|
| HITL | A human decision, review, or approval is required before the workflow, output, action, release, escalation, or downstream use can proceed. | The workflow MUST remain blocked until the required human step is completed and recorded. |
| HOTL | A human monitors, reviews, tunes, investigates, or retrospectively assesses workflow behavior without blocking each action by default. | HOTL MUST NOT be substituted where HITL is required by policy, risk, evidence, customer impact, or output destination. |

## Oversight Principles

| Principle | Requirement |
|---|---|
| Explicit mode | Workflows MUST explicitly identify whether HITL or HOTL applies. |
| Risk-based oversight | Human oversight mode MUST be based on risk, evidence sensitivity, customer impact, policy obligations, output destination, and downstream use. |
| Review is not approval | Human review MAY validate, reject, correct, route, or escalate; it MUST NOT be treated as formal approval unless a formal approval workflow provides that authority. |
| Customer approval is separate | Customer approval MUST remain separate from analyst review, Agent Judge findings, escalation, and HOTL monitoring. |
| Policy remains authoritative | PDP decisions and PEP enforcement MUST remain separate from HITL and HOTL records. |
| Evidence traceability | HITL/HOTL records MUST preserve evidence references and evidence tenant/customer attribution where evidence influences the output. |
| Retrieval and memory control | HITL/HOTL records MUST preserve retrieval and memory scope when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context influences the output. |
| Auditability | Oversight decisions, review records, approval handoffs, escalation paths, and downstream use MUST be auditable. |
| Fail closed | Missing, ambiguous, expired, revoked, unauthorized, stale, inconsistent, unauditable, or out-of-scope oversight context MUST fail closed where governed workflows depend on it. |

## When HITL Is Required

HITL MUST be used when the workflow affects:

| Condition | HITL Requirement |
|---|---|
| Customer-facing output | Human review or approval is required before release or customer-facing routing. |
| DFIR conclusions | Human validation is required before conclusions are used in reportable findings, timelines, impact statements, or final reports. |
| Containment or remediation | Human approval or policy-gated approval is required where actions are privileged, destructive, irreversible, customer-impacting, or externally visible. |
| Evidence handling | Human validation or approval is required for evidence release, evidence export, evidence deletion, chain-of-custody-sensitive handling, or forensic conclusions. |
| Governance evidence | Human review is required before outputs are used for audit, assurance, executive reporting, control evidence, or contractual support. |
| Legal, privacy, regulatory, or contractual sensitivity | Human review and applicable approval routing are required before downstream use. |
| Tenant or customer ambiguity | Human review is required when tenant, customer, case, evidence, workspace, destination, or ownership context is ambiguous or mismatched. |
| Retrieval or memory uncertainty | Human review is required when retrieval/memory scope is missing, stale, cross-customer, cross-tenant, cross-case, unauthorized, or retention-inconsistent. |
| PDP `REQUIRE_APPROVAL` | Formal approval is required before proceeding. |
| PDP `DENY` | The workflow MUST fail closed; escalation may occur only through a separately governed exception path where policy permits. |
| Agent Judge material risk | HITL is required when Agent Judge findings identify unresolved evidence, tenant-boundary, unsupported-claim, HITL, or output-quality risk for high-impact outputs. |

## When HOTL May Be Used

HOTL MAY be used when:

- The workflow is low-risk, internal-only, non-customer-facing, and non-DFIR-conclusive.
- The action is read-only and does not affect customer operations, evidence handling, approval routing, release, or downstream execution.
- Agent output is exploratory and clearly marked as not approved for governed decisions.
- Monitoring, tuning, retrospective analysis, model quality review, or dashboard oversight is sufficient.
- Policy does not require pre-action review or approval.
- Missing or uncertain context cannot cause customer-facing release, evidence alteration, privileged action, or governed downstream reliance.

HOTL MUST escalate to HITL when risk, uncertainty, customer impact, policy obligations, evidence sensitivity, or output destination exceeds the HOTL boundary.

## Required HITL / HOTL Record

Governed workflows using HITL or HOTL MUST preserve a structured oversight record.

| Field | Requirement | Purpose |
|---|---|---|
| `oversight_record_id` | MUST | Unique identifier for the HITL/HOTL record. |
| `oversight_mode` | MUST | Identifies `HITL` or `HOTL`. |
| `oversight_status` | MUST | Identifies pending, completed, rejected, escalated, blocked, failed-closed, expired, or not-applicable state. |
| `reviewer_identity` | MUST when human review or monitoring occurs | Identifies the accountable human reviewer or monitor. |
| `reviewer_authority_scope` | MUST when review authority affects routing, approval, or downstream use | Preserves reviewer authority context. |
| `requester_identity` | MUST when a human, agent, workflow, service, or process requested oversight | Identifies who or what requested oversight. |
| `agent_id` | MUST when an agent generated, influenced, routed, or consumed the reviewed item | Identifies the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent generated, influenced, routed, or consumed the reviewed item | Supports replay and run-level traceability. |
| `workflow_id` | MUST for governed workflows | Links oversight to the originating workflow. |
| `workflow_stage` | MUST when oversight depends on workflow stage | Identifies triage, investigation, DFIR, containment, reporting, closure, approval, exception, or customer-release stage. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` or `incident_id` | MUST when oversight relates to an investigation, alert, incident, ticket, or DFIR matter | Links oversight to the governed operational record. |
| `evidence_object_ids` | MUST when oversight relies on evidence, investigation context, DFIR findings, governance evidence, or customer-facing content | Preserves evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context affects oversight | Defines approved retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| `data_classification` | MUST when classification affects oversight, routing, release, reuse, evidence handling, approval, or downstream use | Preserves data-handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when use is constrained to workflow, case, customer, legal, governance, evidence-handling, reporting, or DFIR purposes | Defines permitted downstream use. |
| `retention_policy_id` | MUST when retention affects evidence, retrieved context, output storage, release, reuse, or disposal | Preserves retention boundary. |
| `output_destination` | MUST when release, routing, disclosure, reporting, evidence handling, governance evidence, or downstream use depends on destination | Identifies where output is sent, stored, released, displayed, or consumed. |
| `policy_decision_reference` | MUST when oversight is triggered by PDP result or policy obligation | Links oversight to policy context. |
| `human_review_record_id` | MUST when HITL review is required or completed | Links oversight to the human review outcome. |
| `approval_record_id` | MUST when formal approval is required or completed | Links oversight to approval context. |
| `customer_approval_record_id` | MUST when customer-side approval is required or completed | Links oversight to customer authorization. |
| `audit_reference_id` | MUST when oversight is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, review, approval, customer approval, and audit records. |

## HITL Decision Outcomes

HITL workflows MUST define explicit outcomes.

| Outcome | Meaning |
|---|---|
| `HITL_VALIDATED` | Human reviewer validated the item within scope. This is not formal approval unless connected to an approval workflow. |
| `HITL_REJECTED` | Human reviewer rejected the item. |
| `HITL_REQUEST_MORE_EVIDENCE` | Additional evidence or context is required. |
| `HITL_ESCALATE` | Item must be routed to another reviewer, approver, customer approver, DFIR lead, incident commander, legal/compliance/privacy function, or governance owner. |
| `HITL_ROUTE_TO_APPROVAL` | Item must enter the formal approval workflow. |
| `HITL_ROUTE_TO_CUSTOMER_APPROVAL` | Item must enter the customer approval path. |
| `HITL_CORRECT_AND_RESUBMIT` | Item must be corrected before further use. |
| `HITL_BLOCKED_FAIL_CLOSED` | Workflow cannot proceed because required context, evidence, approval, review, policy, or auditability is missing or invalid. |

HITL outcomes are review and routing states unless produced by a formal approval workflow or governed PDP. They MUST NOT be represented as PDP authorization decisions by themselves.

## HOTL Monitoring Outcomes

HOTL workflows SHOULD define structured monitoring outcomes.

| Outcome | Meaning |
|---|---|
| `HOTL_NO_ACTION_REQUIRED` | Monitoring did not identify a material issue within the reviewed scope. |
| `HOTL_FLAG_FOR_REVIEW` | Item should be reviewed by a human but is not automatically approved or blocked. |
| `HOTL_ESCALATE_TO_HITL` | Risk, uncertainty, policy, evidence, customer impact, or destination requires pre-action human review. |
| `HOTL_ROUTE_TO_ASSURANCE` | Item should be evaluated by Agent Judge or assurance workflow. |
| `HOTL_ROUTE_TO_GOVERNANCE` | Item should be routed to governance, policy, compliance, or risk review. |
| `HOTL_BLOCKED_FAIL_CLOSED` | Monitoring identified missing or invalid context that requires fail-closed handling. |

HOTL outcomes MUST NOT authorize release, execution, approval, containment, customer notification, or DFIR conclusions.

## Relationship to PEP/PDP

HITL and HOTL do not replace policy enforcement.

| PDP Result | HITL/HOTL Handling |
|---|---|
| `ALLOW` | Workflow MAY proceed only if no separate HITL, approval, customer approval, evidence, or destination requirement applies. |
| `REQUIRE_APPROVAL` | HITL may route to approval, but the workflow MUST remain blocked until valid approval exists. |
| `DENY` | The workflow MUST fail closed. Escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default. |

The PEP MUST enforce the PDP decision and returned obligations. If HITL/HOTL context, approval context, authority, or audit logging cannot be verified where required, the workflow MUST fail closed.

## Human Review and Approval Boundaries

HITL review, HOTL monitoring, formal approval, and customer approval MUST remain separate.

HITL MAY validate, reject, correct, route, or escalate outputs.

HOTL MAY monitor, flag, tune, assess, or recommend escalation.

Formal approval MAY authorize sensitive release, containment, remediation, access change, evidence release, or customer-facing communication when required by policy.

Customer approval MAY authorize customer-facing release, evidence handling, customer-impacting actions, reporting, or external disclosure when required.

HITL and HOTL MUST NOT convert unsupported claims, missing evidence, unresolved Agent Judge findings, or policy denial into approved operational facts.

## Private / Local LLM-Assisted DFIR Oversight

For private/local LLM-assisted DFIR workflows, HITL is required when:

- Model output affects reportable DFIR conclusions.
- Evidence references are missing, ambiguous, or inconsistent.
- Timeline reconstruction cannot be validated from evidence.
- Extracted artifacts are not traceable to source evidence.
- The output introduces unreferenced artifacts, entities, timestamps, or conclusions.
- Knowledge store or memory scope is missing, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent.
- Customer-facing release, legal-sensitive output, governance evidence, or evidence export is involved.

Private/local execution does not make model output authoritative. It only changes where processing occurs. Examiner validation, evidence review, and required approval paths still apply.

## Fail-Closed Conditions

HITL/HOTL workflows MUST fail closed, remain blocked, or route to controlled review when:

- Required HITL review is missing for a HITL-gated workflow.
- HOTL monitoring is substituted for HITL where pre-action review is required.
- Required tenant, customer, workspace, case, evidence, destination, review, approval, customer approval, or policy context is missing, conflicting, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, or retention policy is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where oversight, customer-facing release, DFIR conclusions, governance evidence, approval routing, or downstream use depends on it.
- Evidence references are missing for material investigative, DFIR, governance, approval, or customer-facing output.
- Material claims are unsupported or contradicted by evidence.
- Agent Judge findings identify unresolved unsupported claims, tenant-boundary risk, evidence insufficiency, output-quality risk, or HITL non-compliance.
- PDP returns `DENY`; escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default.
- PDP returns `REQUIRE_APPROVAL` and valid approval is not present.
- The reviewer or monitor lacks authority for the tenant, customer, case, action type, risk level, evidence sensitivity, or destination.
- Customer approval is required but missing, expired, revoked, incomplete, ambiguous, unauditable, or out of scope.
- Audit logging or context preservation fails.
- The oversight package cannot distinguish facts from model-generated inference.

Fail-closed handling MUST preserve the request context, evidence references, oversight reason, routing reason, approval context where applicable, customer approval context where applicable, and audit reference.

## Audit Requirements

HITL/HOTL workflows MUST audit:

- Oversight record identifier.
- Oversight mode, status, outcome, and rationale.
- Requester identity and authority context.
- Reviewer or monitor identity and authority context.
- Tenant, customer, workspace, case, incident, alert, and service-tower context.
- Agent identity, session identity, workflow identity, and initiating user or system.
- Evidence references and evidence tenant/customer attribution metadata.
- `knowledge_store_or_memory_scope` where retrieval or memory influenced oversight, evidence interpretation, routing, customer-facing wording, governance evidence, approval package, DFIR conclusions, or downstream use.
- `knowledge_memory_scope_result` where retrieval or memory scope was evaluated.
- `data_classification`, `sensitivity_label`, `allowed_use`, and `retention_policy_id` where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- Agent Judge findings considered during oversight.
- PEP/PDP decision and obligations, where applicable.
- `human_review_record_id`, `approval_record_id`, and `customer_approval_record_id` where review, formal approval, or customer approval is required or completed.
- Output destination and approved audience.
- Review or monitoring timestamp, correlation identifier, and workflow step.
- Escalation reason, rejection reason, request-more-evidence reason, or fail-closed reason.
- Known limitations or unresolved uncertainty.

If the workflow cannot create the required audit record, the HITL/HOTL workflow MUST remain blocked until the issue is reviewed or remediated.

## Operational Anti-Patterns

Avoid the following:

- Treating HOTL monitoring as HITL approval.
- Treating HITL validation as formal approval without an approval workflow.
- Treating HITL or HOTL as a PDP decision.
- Treating escalation from HITL or HOTL as approval.
- Allowing an agent to approve its own request.
- Allowing HOTL monitoring to authorize customer-facing release.
- Releasing customer-facing content without required approval.
- Using local/private LLM execution as a reason to skip DFIR validation.
- Treating Agent Judge findings as optional when they identify material risk.
- Reusing HITL or HOTL outcomes across tenants, customers, cases, evidence sets, destinations, or time windows.
- Allowing missing audit records to default to approval or release.
- Treating Entra Agent ID, agent registry, identity governance, or lifecycle controls as operational SOC agents.

## Acceptance Criteria

This file is acceptable when:

- HITL and HOTL are explicitly defined as separate oversight modes.
- HITL is required before high-impact, customer-facing, DFIR-conclusive, evidence-sensitive, policy-gated, or approval-gated downstream use.
- HOTL is limited to monitoring, retrospective review, quality review, tuning, and escalation readiness unless policy explicitly allows otherwise.
- HITL/HOTL records preserve tenant, customer, case, evidence, destination, review, approval, and customer approval boundaries.
- HITL/HOTL records preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where retrieval or memory affects oversight or downstream use.
- HITL/HOTL records preserve data classification, sensitivity label, allowed use, and retention policy where sensitive data handling, release, reuse, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- HITL/HOTL remains separate from Agent Judge assurance, PEP/PDP enforcement, formal approval, customer approval, tool execution, evidence authority, and forensic certification.
- Valid approval or customer approval is required before customer-facing release, customer-impacting action, evidence release, or externally visible output where required.
- Fail-closed handling exists for missing context, unsupported claims, invalid approvals, unauthorized reviewers, unresolved retrieval/memory scope, improper HOTL substitution, and audit failures.
- Audit replay can reconstruct requester identity, reviewer/monitor identity, authority scope, oversight mode, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, human review record, approval record, customer approval record, rationale, outcome, routing, and downstream use.
