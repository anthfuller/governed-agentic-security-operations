# Human Accountability

## Purpose

This file defines human accountability requirements for governed Agentic MSSP / MDR / DFIR security operations.

Human accountability ensures that human reviewers, approvers, customer approvers, incident commanders, DFIR leads, governance owners, and authorized operational roles remain accountable for decisions that affect customer-facing outputs, DFIR conclusions, evidence handling, escalation, containment, remediation, approval routing, or downstream operational use.

Human accountability does not replace PDP authorization, PEP enforcement, Agent Judge assurance, formal approval workflows, customer approval paths, tool execution controls, evidence authority, or forensic certification.

## Scope

This file applies to human accountability for:

- Analyst review of agent-generated triage, enrichment, investigation, and recommendation outputs.
- Approval workflows for customer-facing, privileged, irreversible, evidence-sensitive, legal-sensitive, or high-impact decisions.
- Escalation paths involving service towers, DFIR leads, incident commanders, governance, legal, compliance, privacy, or customer approvers.
- HITL and HOTL oversight of governed agentic workflows.
- Agent Judge findings that require human validation, rejection, correction, escalation, or routing.
- Customer-facing reports, executive summaries, governance evidence, legal-sensitive outputs, and DFIR conclusions.
- Tool use, MCP-mediated access, data ingestion, retrieval, memory, evidence handling, and downstream consumption where human accountability is required.
- Private/local LLM-assisted DFIR workflows where model output may influence evidence interpretation, reportable findings, or customer-facing outputs.

This file does not define PDP decision logic, PEP enforcement behavior, Agent Judge scoring, evidence collection procedures, customer approval workflow design, or incident command procedures.

## Non-Goals

Human accountability MUST NOT be used to:

- Treat human review as PDP authorization.
- Treat human review as formal approval unless a formal approval workflow explicitly provides that authority.
- Treat customer-facing release readiness as customer approval.
- Treat escalation as approval.
- Treat Agent Judge findings as human validation.
- Allow humans to approve outside their authority scope.
- Allow agents, tools, or workflows to self-authorize, self-approve, or bypass required accountability paths.
- Override a PDP `DENY` unless routed through a separately governed exception process explicitly permitted by policy.
- Treat private/local LLM execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## Accountability Principles

| Principle | Requirement |
|---|---|
| Named accountability | Human-accountable decisions MUST identify the responsible person, role, authority scope, and decision context. |
| Authority-scoped decisions | Humans MUST act only within assigned tenant, customer, case, evidence, action, risk, approval, and destination authority. |
| Review is not approval | Human review MAY validate, reject, correct, route, or escalate; it MUST NOT be treated as formal approval unless a formal approval workflow provides that authority. |
| Customer approval is separate | Customer approval MUST remain separate from analyst review, Agent Judge findings, escalation, and HOTL monitoring. |
| Policy remains authoritative | PDP decisions and PEP enforcement MUST remain separate from human review and accountability records. |
| Evidence-bound accountability | Human accountability for findings, recommendations, reports, DFIR conclusions, or governance evidence MUST preserve evidence references. |
| Retrieval and memory boundary control | Human accountability records MUST preserve retrieval and memory scope when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context influences the decision. |
| Auditability | Human decisions, rationale, authority, review records, approval records, escalation paths, and downstream use MUST be auditable. |
| Fail closed | Missing, ambiguous, expired, revoked, unauthorized, stale, inconsistent, unauditable, or out-of-scope accountability context MUST fail closed where governed workflows depend on it. |

## Human Accountability Roles

| Role | Accountability Boundary |
|---|---|
| Analyst | Validates evidence support, tenant/customer scope, uncertainty, and operational readiness within assigned authority. |
| Senior analyst or escalation reviewer | Reviews higher-risk or ambiguous findings, escalations, and unresolved review issues. |
| DFIR lead or examiner | Validates DFIR conclusions, timelines, evidence interpretation, and reportable findings. |
| Incident commander | Owns response strategy, major operational decisions, containment posture, recovery coordination, and closure authority where assigned. |
| Formal approver | Approves scoped actions, releases, exceptions, evidence handling, or workflow continuation within assigned approval authority. |
| Customer approver | Provides customer-side authorization where required for release, evidence handling, containment, remediation, reporting, or external disclosure. |
| Governance owner | Reviews policy exceptions, control gaps, compliance-sensitive handling, and governance evidence. |
| Legal, privacy, or compliance reviewer | Reviews legal-sensitive, privacy-sensitive, regulatory, contractual, or public/audit-supporting material within assigned authority. |

## Required Human Accountability Record

Governed workflows requiring human accountability MUST preserve a structured accountability record.

| Field | Requirement | Purpose |
|---|---|---|
| `human_accountability_record_id` | MUST | Unique identifier for the accountability record. |
| `accountability_type` | MUST | Identifies analyst review, HITL review, HOTL monitoring, formal approval, customer approval, escalation, DFIR validation, governance review, legal review, privacy review, compliance review, or incident command decision. |
| `accountability_status` | MUST | Identifies pending, completed, rejected, escalated, blocked, failed-closed, expired, revoked, or not-applicable state. |
| `accountable_human_identity` | MUST | Identifies the accountable person. |
| `accountable_human_role` | MUST | Identifies the accountable function or responsibility. |
| `accountable_authority_scope` | MUST | Preserves authority context for tenant, customer, case, evidence, action type, risk level, destination, and approval scope. |
| `requester_identity` | MUST when a human, agent, workflow, service, or process requested the accountable decision | Identifies who or what requested the decision. |
| `agent_id` | MUST when an agent generated, influenced, routed, or consumed the reviewed item | Identifies the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent generated, influenced, routed, or consumed the reviewed item | Supports replay and run-level traceability. |
| `workflow_id` | MUST for governed workflows | Links accountability to the originating workflow. |
| `workflow_stage` | MUST when authority, routing, approval, or downstream handling depends on workflow stage | Identifies triage, investigation, DFIR, containment, reporting, closure, approval, exception, or customer-release stage. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` or `incident_id` | MUST when accountability relates to an investigation, alert, incident, ticket, or DFIR matter | Links accountability to the governed operational record. |
| `evidence_object_ids` | MUST when accountability relies on evidence, investigation context, DFIR findings, governance evidence, or customer-facing content | Preserves evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context affects accountability | Defines approved retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| `data_classification` | MUST when classification affects accountability, routing, release, reuse, evidence handling, approval, or downstream use | Preserves data-handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when use is constrained to workflow, case, customer, legal, governance, evidence-handling, reporting, or DFIR purposes | Defines permitted downstream use. |
| `retention_policy_id` | MUST when retention affects evidence, retrieved context, output storage, release, reuse, or disposal | Preserves retention boundary. |
| `output_destination` | MUST when release, routing, disclosure, reporting, evidence handling, governance evidence, or downstream use depends on destination | Identifies where output is sent, stored, released, displayed, or consumed. |
| `decision_rationale` | MUST when an accountable human decision is made | Records why the decision was made. |
| `decision_outcome` | MUST when an accountable human decision is made | Records the accountable result, rejection, escalation, approval, customer approval, or fail-closed outcome. |
| `policy_decision_reference` | MUST when accountability is triggered by PDP result or policy obligation | Links accountability to policy context. |
| `human_review_record_id` | MUST when human review is required or completed | Links accountability to the human review outcome. |
| `approval_record_id` | MUST when formal approval is required or completed | Links accountability to approval context. |
| `customer_approval_record_id` | MUST when customer-side approval is required or completed | Links accountability to customer authorization. |
| `audit_reference_id` | MUST when accountability is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, review, approval, customer approval, and audit records. |

## Accountability Decision Outcomes

Human accountability workflows MUST define explicit outcomes.

| Outcome | Meaning |
|---|---|
| `ACCOUNTABILITY_VALIDATED` | Accountable human validated the item within scope. This is not formal approval unless connected to an approval workflow. |
| `ACCOUNTABILITY_REJECTED` | Accountable human rejected the item. |
| `ACCOUNTABILITY_REQUEST_MORE_EVIDENCE` | Additional evidence or context is required. |
| `ACCOUNTABILITY_ESCALATED` | Item must be routed to another reviewer, approver, customer approver, DFIR lead, incident commander, legal/compliance/privacy function, or governance owner. |
| `ACCOUNTABILITY_ROUTE_TO_APPROVAL` | Item must enter the formal approval workflow. |
| `ACCOUNTABILITY_ROUTE_TO_CUSTOMER_APPROVAL` | Item must enter the customer approval path. |
| `ACCOUNTABILITY_CORRECT_AND_RESUBMIT` | Item must be corrected before further use. |
| `ACCOUNTABILITY_BLOCKED_FAIL_CLOSED` | Workflow cannot proceed because required context, evidence, approval, review, authority, policy, or auditability is missing or invalid. |

Accountability outcomes are review, validation, approval, or routing states according to the workflow that produced them. They MUST NOT be represented as PDP authorization decisions by themselves.

## Relationship to PEP/PDP

Human accountability does not replace policy enforcement.

| PDP Result | Human Accountability Handling |
|---|---|
| `ALLOW` | Workflow MAY proceed only if no separate human review, approval, customer approval, evidence, or destination requirement applies. |
| `REQUIRE_APPROVAL` | Accountability may route to approval, but the workflow MUST remain blocked until valid approval exists. |
| `DENY` | The workflow MUST fail closed. Escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default. |

The PEP MUST enforce the PDP decision and returned obligations. If accountability context, approval context, authority, or audit logging cannot be verified where required, the workflow MUST fail closed.

## Human Review and Approval Boundaries

Human review, formal approval, customer approval, escalation, and incident command accountability MUST remain separate.

Human review MAY validate, reject, correct, route, or escalate outputs.

Formal approval MAY authorize sensitive release, containment, remediation, access change, evidence release, or customer-facing communication when required by policy.

Customer approval MAY authorize customer-facing release, evidence handling, customer-impacting actions, reporting, or external disclosure when required.

Human accountability records MUST NOT convert unsupported claims, missing evidence, unresolved Agent Judge findings, policy denial, or tool success into approved operational facts.

## Accountability for Customer-Facing Outputs

Customer-facing output requires named accountability before release or customer approval routing.

The accountable human MUST verify, where applicable:

- The output belongs to the correct tenant, customer, case, and destination.
- Evidence references support the material claims.
- Customer identity remains separate from tenant identity.
- Limitations, assumptions, and uncertainty are disclosed where material.
- Data classification, sensitivity label, allowed use, and retention policy support the intended release.
- Retrieval or memory scope is valid when retrieved context influenced the output.
- Required customer approval exists before release where required.
- The output does not claim legal, compliance, regulatory, forensic, or production-readiness authority without the required review path.

## Accountability for DFIR Conclusions

DFIR conclusions require named human accountability before reportable use.

The accountable human MUST verify, where applicable:

- Findings distinguish observed facts, inferences, assumptions, hypotheses, and conclusions.
- Evidence object identifiers support the conclusion.
- Evidence tenant and customer attribution are preserved.
- Timeline statements are traceable to evidence timestamps.
- Chain-of-custody or evidence-handling expectations are preserved where applicable.
- Private/local LLM-assisted output remains subject to examiner review and evidence validation.
- Model output is not treated as forensic proof.
- Customer-facing DFIR conclusions follow required review and approval paths.

## Private / Local LLM-Assisted DFIR Accountability

For private/local LLM-assisted DFIR workflows, human accountability is required when:

- Model output affects reportable DFIR conclusions.
- Evidence references are missing, ambiguous, or inconsistent.
- Timeline reconstruction cannot be validated from evidence.
- Extracted artifacts are not traceable to source evidence.
- The output introduces unreferenced artifacts, entities, timestamps, or conclusions.
- Knowledge store or memory scope is missing, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent.
- Customer-facing release, legal-sensitive output, governance evidence, or evidence export is involved.

Private/local execution does not make model output authoritative. It only changes where processing occurs. Examiner validation, evidence review, and required approval paths still apply.

## Fail-Closed Conditions

Human accountability workflows MUST fail closed, remain blocked, or route to controlled review when:

- Required human accountability is missing for a human-accountability-gated workflow.
- Required accountable human identity, role, authority scope, decision rationale, or decision outcome is missing, ambiguous, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required tenant, customer, workspace, case, evidence, destination, review, approval, customer approval, or policy context is missing, conflicting, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, or retention policy is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where accountability, customer-facing release, DFIR conclusions, governance evidence, approval routing, or downstream use depends on it.
- Evidence references are missing for material investigative, DFIR, governance, approval, or customer-facing output.
- Material claims are unsupported or contradicted by evidence.
- Agent Judge findings identify unresolved unsupported claims, tenant-boundary risk, evidence insufficiency, output-quality risk, or HITL non-compliance.
- PDP returns `DENY`; escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default.
- PDP returns `REQUIRE_APPROVAL` and valid approval is not present.
- The accountable human lacks authority for the tenant, customer, case, action type, risk level, evidence sensitivity, or destination.
- Customer approval is required but missing, expired, revoked, incomplete, ambiguous, unauditable, or out of scope.
- Audit logging or context preservation fails.
- The accountability package cannot distinguish facts from model-generated inference.

Fail-closed handling MUST preserve the request context, evidence references, accountability reason, routing reason, authority context, approval context where applicable, customer approval context where applicable, and audit reference.

## Audit Requirements

Human accountability workflows MUST audit:

- Human accountability record identifier.
- Accountability type, status, outcome, and rationale.
- Requester identity and authority context.
- Accountable human identity, role, and authority context.
- Tenant, customer, workspace, case, incident, alert, and service-tower context.
- Agent identity, session identity, workflow identity, and initiating user or system.
- Evidence references and evidence tenant/customer attribution metadata.
- `knowledge_store_or_memory_scope` where retrieval or memory influenced accountability, evidence interpretation, routing, customer-facing wording, governance evidence, approval package, DFIR conclusions, or downstream use.
- `knowledge_memory_scope_result` where retrieval or memory scope was evaluated.
- `data_classification`, `sensitivity_label`, `allowed_use`, and `retention_policy_id` where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- Agent Judge findings considered during accountability review.
- PEP/PDP decision and obligations, where applicable.
- `human_review_record_id`, `approval_record_id`, and `customer_approval_record_id` where review, formal approval, or customer approval is required or completed.
- Output destination and approved audience.
- Review, accountability, or approval timestamp, correlation identifier, and workflow step.
- Escalation reason, rejection reason, request-more-evidence reason, or fail-closed reason.
- Known limitations or unresolved uncertainty.

If the workflow cannot create the required audit record, the human accountability workflow MUST remain blocked until the issue is reviewed or remediated.

## Operational Anti-Patterns

Avoid the following:

- Treating human accountability as a PDP decision.
- Treating human review as formal approval without an approval workflow.
- Treating escalation as approval.
- Allowing an agent to provide accountability for its own request.
- Allowing an accountable human to approve outside their authority scope.
- Releasing customer-facing content without required approval.
- Using local/private LLM execution as a reason to skip DFIR validation.
- Treating Agent Judge findings as optional when they identify material risk.
- Reusing accountability outcomes across tenants, customers, cases, evidence sets, destinations, or time windows.
- Allowing missing audit records to default to approval or release.
- Treating Entra Agent ID, agent registry, identity governance, or lifecycle controls as operational SOC agents.

## Acceptance Criteria

This file is acceptable when:

- Human accountability is explicitly tied to named identity, role, authority scope, rationale, and outcome.
- Human accountability remains separate from Agent Judge assurance, PEP/PDP enforcement, formal approval, customer approval, tool execution, evidence authority, and forensic certification.
- Human accountability records preserve tenant, customer, case, evidence, destination, review, approval, and customer approval boundaries.
- Human accountability records preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where retrieval or memory affects accountability or downstream use.
- Human accountability records preserve data classification, sensitivity label, allowed use, and retention policy where sensitive data handling, release, reuse, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- Accountable humans cannot approve outside assigned authority scope.
- Valid approval or customer approval is required before customer-facing release, customer-impacting action, evidence release, or externally visible output where required.
- Fail-closed handling exists for missing context, unsupported claims, invalid approvals, unauthorized accountable humans, unresolved retrieval/memory scope, and audit failures.
- Audit replay can reconstruct requester identity, accountable human identity, authority scope, accountability type, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, human review record, approval record, customer approval record, rationale, outcome, routing, and downstream use.
