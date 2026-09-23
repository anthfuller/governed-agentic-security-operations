# Analyst Review Checkpoints

## Reference Architecture Disclaimer

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

## Purpose

The `human-oversight/analyst-review-checkpoints.md` file defines baseline checkpoints analysts should apply when reviewing agent-assisted security operations output in governed Agentic SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR workflows.

These checkpoints exist to ensure that analyst review is evidence-based, tenant-aware, auditable, and aligned to the sensitivity of the proposed output or action. They are not a replacement for PEP/PDP enforcement, Agent Judge evaluation, incident command authority, customer approval, legal review, or formal DFIR leadership approval where those controls are required.

## Scope

This file covers analyst review checkpoints for:

- Agent-generated triage summaries.
- Investigation summaries and recommended next steps.
- Alert enrichment and correlation narratives.
- Threat-hunting findings.
- DFIR draft findings and timelines.
- Containment or response recommendations.
- Escalation recommendations.
- Customer-facing draft reports or summaries.
- Governance evidence summaries.
- Private/local LLM-assisted evidence analysis outputs.

This file does not define:

- PDP authorization logic.
- PEP implementation behavior.
- Agent Judge scoring contracts.
- Evidence ingestion or forensic parsing procedures.
- Customer approval workflow design.
- Break-glass exception governance.
- Product-specific SOC tooling configuration.

Those details belong in the appropriate `policy-enforcement/`, `ai-assurance/`, `local-llm-dfir/`, `workflows/`, `templates/`, or related human-oversight files.

## Control Intent

Analyst review checkpoints enforce the boundary between agent-assisted output and human-validated operational use.

The control intent is to ensure that analysts verify:

- The output belongs to the correct tenant, customer, case, workspace, and service tower.
- The output is supported by referenced evidence.
- Material claims, conclusions, and recommendations are not based only on model assertion.
- Risk level and operational impact are properly classified.
- Sensitive actions are routed to the correct approval path.
- Customer-facing content is reviewed before release.
- DFIR conclusions remain analyst-validated and evidence-supported.
- Missing, ambiguous, or conflicting context blocks the workflow or triggers escalation.

## Analyst Review Is Not Policy Override

Analyst review provides human validation and accountability. It does not override policy enforcement.

An analyst MUST NOT approve execution of an action that a PDP has denied unless the request is routed through a separately governed exception process explicitly permitted by policy. Analyst review also MUST NOT convert an Agent Judge warning into an approved state without resolving or documenting the underlying issue.

## Review Entry Criteria

Substantive analyst approval review MUST NOT proceed unless the review package includes enough context to support an accountable decision.

Required review inputs include, where applicable:

| Input | Review purpose |
|---|---|
| `tenant_id`, `customer_id`, `workspace_id`, or equivalent tenant context | Confirms the output belongs to the expected customer and environment. |
| `case_id`, `incident_id`, `alert_id`, or investigation reference | Anchors the review to the correct operational record. |
| Agent identity and session or workflow identifier | Identifies which agent or workflow produced the output. |
| Proposed output, action, recommendation, or escalation | Defines what the analyst is being asked to validate. |
| Evidence references and evidence tenant-attribution metadata | Allows claims and findings to be checked against source evidence. |
| `knowledge_store_or_memory_scope` | Required where RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, retrieved context, customer-facing output, governance evidence, or DFIR conclusions affect the analyst-reviewed output. |
| `knowledge_memory_scope_result` | Required where retrieval or memory scope was evaluated and affects the analyst-reviewed output, release, reuse, governance evidence, DFIR conclusions, or downstream use. |
| `data_classification` | Required where sensitive data handling, release, reuse, customer-facing output, governance evidence, or DFIR conclusions affect the analyst-reviewed output. |
| `sensitivity_label` | Required where sensitivity, privacy, legal, customer-specific handling, release, reuse, customer-facing output, governance evidence, or DFIR conclusions affect the analyst-reviewed output. |
| `allowed_use` | Required where output use is constrained by workflow, case, customer, legal, governance, evidence-handling, reporting, reuse, customer-facing output, or DFIR purpose. |
| `retention_policy_id` | Required where retention, reuse, evidence handling, customer-facing output, governance evidence, or DFIR conclusions affect the analyst-reviewed output. |
| Risk classification and operational impact | Determines whether review, escalation, or formal approval is required. |
| PEP/PDP decision and obligations, where applicable | Confirms authorization state and required approval handling. |
| Agent Judge findings, where applicable | Identifies unsupported-claim, evidence-support, tenant-boundary, HITL, or quality concerns. |
| Output destination and audience | Determines whether customer-facing, privileged, external, or cross-tenant release controls apply. |
| Known limitations, uncertainty, missing evidence, or conflicting context | Ensures uncertainty is not hidden from the reviewer. |

If required review inputs are missing, inconsistent, or unverifiable, the analyst MUST select a blocked, rejected, request-more-evidence, or escalation outcome rather than approving the output.

## Core Analyst Review Checkpoints

Analysts MUST apply the applicable checkpoints before allowing agent-assisted output to influence DFIR conclusions, customer-facing reporting, containment recommendations, escalation, governance evidence, approval routing, or operational response decisions.

### 1. Tenant, Customer, and Case Boundary Check

The analyst MUST verify that the output is bound to the correct tenant, customer, workspace, case, evidence set, and output destination.

Review questions:

- Does the output reference the expected tenant, customer, case, workspace, and service tower?
- Do evidence references belong to the same tenant or approved shared context?
- Is there any cross-tenant data, customer mixing, or ambiguous attribution?
- Is the destination authorized for this tenant and case?

Fail-closed conditions:

- Tenant, customer, workspace, case, evidence, or destination context is missing.
- Evidence appears to come from a different tenant or unapproved shared context.
- The output combines customer data without explicit authorization.
- The analyst cannot verify the tenant boundary.

### 2. Evidence Support Check

The analyst MUST verify that material claims are supported by referenced evidence.

Review questions:

- Are all material claims linked to evidence references?
- Does the cited evidence actually support the claim?
- Are timestamps, entities, indicators, users, hosts, cloud resources, and actions accurately represented?
- Are confidence levels, uncertainty, and limitations stated where evidence is incomplete?

Fail-closed conditions:

- Material claims lack evidence references.
- The evidence does not support the claim.
- The output overstates certainty.
- Evidence is incomplete but the output presents a final conclusion.

### 3. Unsupported Claim and Hallucination Check

The analyst MUST review agent-generated claims for unsupported reasoning, invented facts, missing context, or unsupported causal conclusions.

Review questions:

- Does the model assert facts not present in the evidence package?
- Does the output infer attacker intent, root cause, impact, or containment effectiveness without support?
- Are external threat intelligence or framework references used only where supported?
- Did an Agent Judge flag unsupported claims or hallucination risk?

Fail-closed conditions:

- The output contains unsupported root-cause, attribution, impact, or containment claims.
- The analyst cannot trace a material claim to evidence.
- Agent Judge warnings are unresolved for material output.

### 4. DFIR Conclusion Check

The analyst MUST validate DFIR conclusions before they are treated as findings, incident conclusions, timeline statements, or formal report content.

Review questions:

- Does the conclusion distinguish observation, inference, and confirmed fact?
- Are alternative explanations or limitations documented where relevant?
- Is the timeline supported by evidence timestamps and source context?
- Are chain-of-custody or evidence-handling expectations preserved where applicable?

Fail-closed conditions:

- The output presents draft analysis as a final DFIR conclusion.
- Timeline sequence cannot be validated from evidence.
- Evidence handling, scope, or source integrity is unclear.
- The analyst cannot distinguish confirmed facts from model inference.

### 5. Containment and Response Recommendation Check

The analyst MUST validate operational impact before any containment or response recommendation is approved, escalated, or used for decision-making.

Review questions:

- What system, identity, network segment, workload, tenant, or customer would be affected?
- Is the action reversible or irreversible?
- What is the expected blast radius?
- Does the recommendation require customer approval, incident commander approval, or policy exception review?
- Has PEP/PDP authorization and required approval routing been satisfied?

Fail-closed conditions:

- Blast radius is unclear.
- Reversibility is unknown.
- The action is privileged, destructive, or customer-impacting and approval is missing.
- The recommendation bypasses PEP/PDP or approval workflow requirements.

### 6. Escalation and Routing Check

The analyst MUST verify that escalation recommendations are routed to the correct service tower, authority level, customer contact, or governance function.

Review questions:

- Is the severity or priority supported by evidence?
- Is the escalation recipient authorized for the tenant and case?
- Does the escalation disclose only information appropriate for the recipient?
- Does the escalation trigger customer, legal, DFIR lead, or incident commander involvement?

Fail-closed conditions:

- Escalation routing is ambiguous.
- Severity is unsupported or overstated.
- Recipient scope is incorrect or not authorized.
- The escalation would disclose customer or tenant information to the wrong audience.

### 7. Customer-Facing Output Check

The analyst MUST review customer-facing content before release or routing for customer approval.

Review questions:

- Are findings evidence-supported and scoped to the correct customer?
- Are limitations, uncertainty, and assumptions clearly stated?
- Is the language operationally precise and not speculative?
- Does the output avoid unsupported product, compliance, legal, or attribution claims?
- Is customer approval required before release?

Fail-closed conditions:

- Customer-facing content contains unsupported claims.
- Evidence or tenant attribution is incomplete.
- Required customer approval is missing.
- The release destination is not verified.

### 8. Governance Evidence Check

The analyst MUST validate governance evidence summaries before they are used for control reporting, policy evidence, or assurance workflows.

Review questions:

- Is the evidence source clearly identified?
- Does the summary avoid claiming compliance or certification outcomes?
- Are control interpretations labeled as analysis, not proof of compliance?
- Are limitations and scope boundaries documented?

Fail-closed conditions:

- The output makes compliance overclaims.
- Evidence is missing, stale, or outside scope.
- The output implies formal assurance beyond the available evidence.

### 9. Sensitive Data and Disclosure Check

The analyst MUST verify that the output does not expose sensitive, privileged, cross-tenant, or unnecessary data.

Review questions:

- Does the output include secrets, tokens, credentials, personal data, customer-sensitive information, or privileged operational details?
- Is the data necessary for the review or destination audience?
- Is redaction, minimization, or restricted routing required?
- Does private/local LLM processing preserve required evidence-handling boundaries?

Fail-closed conditions:

- Sensitive data appears in an unauthorized destination.
- Redaction or minimization requirements are unresolved.
- Cross-tenant or privileged data exposure risk is present.

### 10. Approval Requirement Check

The analyst MUST verify whether the output or action requires additional approval before it proceeds.

Review questions:

- Does policy require approval for this action, destination, risk level, or customer impact?
- Has the PEP/PDP returned `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`?
- Is approval valid, scoped, unexpired, and issued by an authorized approver?
- Does approval apply only to the specific tenant, customer, case, action, evidence set, destination, and time window?

Fail-closed conditions:

- Required approval is missing, expired, revoked, invalid, or out of scope.
- The approver authority scope does not match the tenant, customer, case, action type, or risk level.
- The workflow treats silence, timeout, or missing response as approval.

## Review Outcome Requirements

Analyst review workflows MUST define explicit allowed review outcomes.

Baseline analyst outcomes SHOULD include:

| Outcome | When to use |
|---|---|
| `APPROVED_FOR_INTERNAL_USE` | The output is suitable for internal operational use within the reviewed scope. |
| `APPROVED_FOR_ESCALATION` | The output may be escalated to the approved recipient or service tower. |
| `APPROVED_FOR_CUSTOMER_REVIEW` | The output may be routed for customer-facing review or approval, but is not automatically released. |
| `REJECTED` | The output or recommendation is inaccurate, unsupported, unsafe, unauthorized, or out of scope. |
| `REQUEST_MORE_EVIDENCE` | The analyst cannot validate the output without additional evidence or context. |
| `ESCALATE_TO_DFIR_LEAD` | The decision requires DFIR lead or incident commander review. |
| `ESCALATE_TO_GOVERNANCE` | The decision requires governance, risk, exception, or policy review. |
| `ESCALATE_TO_CUSTOMER_APPROVER` | Customer authorization is required before action or release. |
| `BLOCKED_FAIL_CLOSED` | The workflow cannot proceed because a required control, context, approval, or audit condition is missing. |

Approval outcomes MUST be scoped. An analyst approval for one tenant, customer, case, action, evidence set, destination, or time window MUST NOT be reused for another scope unless policy explicitly permits reuse and the reuse is audited.

## Audit Requirements

Analyst review decisions MUST be auditable.

Audit records MUST include, where applicable:

- Analyst identity and role.
- Reviewer authority scope or equivalent authorization context.
- Tenant, customer, workspace, case, alert, incident, and service-tower context.
- Agent identity, session identity, workflow identity, and initiating user or system.
- Reviewed output, proposed action, recommendation, or release artifact.
- Evidence references and evidence tenant-attribution metadata.
- `knowledge_store_or_memory_scope` where retrieval or memory influenced the reviewed output, evidence interpretation, routing, customer-facing wording, governance evidence, approval package, DFIR conclusions, or downstream use.
- `knowledge_memory_scope_result` where retrieval or memory scope was evaluated.
- `data_classification`, `sensitivity_label`, `allowed_use`, and `retention_policy_id` where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- `human_review_record_id`, `approval_record_id`, and `customer_approval_record_id` where review, formal approval, or customer approval is required or completed.
- Agent Judge findings considered during review.
- PEP/PDP decision and obligations, where applicable.
- Review outcome and rationale.
- Required approval status and approval reference, where applicable.
- Output destination and approved audience.
- Review timestamp, correlation identifier, and workflow step.
- Escalation reason, rejection reason, or request-more-evidence reason.
- Known limitations or unresolved uncertainty.

If the workflow cannot create the required audit record, the review MUST remain blocked until the issue is reviewed or remediated.

## Analyst Review Fail-Closed Conditions

Analyst review MUST fail closed or escalate when:

- Required tenant, customer, workspace, case, evidence, or destination context is missing or conflicting.
- Evidence references are missing for material investigative, DFIR, governance, approval, or customer-facing output.
- Material claims are unsupported or contradicted by evidence.
- Agent Judge findings identify unresolved unsupported claims, tenant-boundary risk, evidence insufficiency, or HITL non-compliance.
- PEP/PDP returns `DENY`. Analyst review MUST fail closed. Escalation MAY occur only for separately governed exception review where explicitly permitted by policy, and must not permit execution by default.
- PEP/PDP returns `REQUIRE_APPROVAL` and valid approval is not present.
- The analyst lacks authority for the tenant, customer, case, action type, risk level, or destination.
- The proposed action is irreversible, destructive, privileged, customer-impacting, or externally visible and required approval is missing.
- Audit logging or context preservation fails.
- Required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, retention policy, human review record, approval record, or customer approval record is missing, expired, revoked, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where analyst review, customer-facing release, DFIR conclusions, governance evidence, approval routing, or downstream use depends on it.
- The review package cannot distinguish facts from model-generated inference.

Fail-closed handling MUST preserve the request context, evidence references, review reason, and escalation path where technically available.

## Private / Local LLM-Assisted DFIR Checkpoints

For private/local LLM-assisted DFIR workflows, analysts MUST apply additional validation before using model output as investigative support.

The analyst MUST verify:

- The local or private model output is tied to the correct evidence set.
- The model did not introduce unreferenced artifacts, entities, timestamps, or conclusions.
- Timeline reconstruction is supported by evidence timestamps.
- Extracted artifacts are traceable to source evidence.
- Report drafts distinguish evidence-backed facts from analyst interpretation.
- Sensitive evidence handling, chain-of-custody expectations, and customer scope are preserved where applicable.

Private or local execution does not make model output authoritative. It only changes where processing occurs. Analyst validation remains required for material DFIR conclusions and customer-facing use.

## Handoff Boundaries

Analyst review checkpoints depend on controlled handoffs with other architecture areas:

| Related area | Handoff boundary |
|---|---|
| `ai-assurance/` | Provides Agent Judge findings, evidence-support checks, tenant-boundary checks, and unsupported-claim review signals. |
| `policy-enforcement/` | Provides PDP decisions, PEP obligations, risk classifications, and approval requirements. |
| `agent-governance/` | Provides agent identity, ownership, lifecycle, and authority metadata. |
| `local-llm-dfir/` | Provides private/local evidence processing context and DFIR validation requirements. |
| `workflows/` | Defines how review packages move between agents, humans, tools, evidence stores, approval gates, and audit systems. |
| `templates/` | Provides reusable analyst review, escalation, approval, and customer-release checklists. |

This file defines analyst checkpoints only. It MUST NOT become the full implementation contract for those related areas.

## F7-LAS Alignment

F7-LAS may be used as a supporting control lens for analyst review checkpoints.

Relevant alignment includes:

- L2 Grounding / RAG: evidence references and source context must support claims.
- L4 Tools: tool actions must remain mediated and policy-gated.
- L5 Policy: approval and authorization requirements must not be bypassed by analyst review.
- L6 Sandbox / Blast Radius: containment and response recommendations must account for operational impact.
- L7 Monitoring & Evaluation: analyst decisions, evidence references, outcomes, and escalations must remain observable and auditable.

F7-LAS supports the checkpoint model but does not replace the MSSP / MDR / DFIR operating model.

## Acceptance Criteria

This file is acceptable when analyst review checkpoints:

- Require tenant, customer, case, evidence, and destination validation.
- Require evidence support for material claims.
- Require human validation of DFIR conclusions and customer-facing outputs.
- Require additional approval for containment, escalation, privileged, irreversible, external, or customer-impacting actions.
- Separate analyst review from Agent Judge assurance and PEP/PDP enforcement.
- Define explicit review outcomes.
- Define fail-closed handling for missing context, unsupported claims, invalid approvals, unauthorized reviewers, and audit failures.
- Preserve auditability across reviewer identity, authority scope, evidence references, rationale, outcome, and routing.
- Support audit replay across reviewer identity, reviewer authority, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, approval record, customer approval record, rationale, outcome, routing, and downstream use.
- Avoid product-specific implementation claims, compliance overclaims, and autonomous SOC language.

## Anti-Patterns

Avoid the following:

- Treating agent output as validated because it appears complete.
- Treating model confidence as evidence.
- Approving outputs without checking tenant and customer boundaries.
- Accepting citations or evidence references without verifying that they support the claim.
- Allowing an analyst to override a PDP `DENY` decision outside a governed exception process.
- Releasing customer-facing content without approval where required.
- Using local/private LLM execution as a reason to skip DFIR validation.
- Treating Agent Judge findings as optional when they identify material risk.
- Approving irreversible or privileged actions without blast-radius review.
- Reusing approval outside the approved scope.
- Allowing missing audit records to default to approval.
- Turning analyst review into a rubber-stamp process.

## Summary

Analyst review checkpoints ensure that agent-assisted security operations remain evidence-based, tenant-aware, policy-aligned, and auditable. Analysts validate what agents produce, resolve ambiguity, escalate material risk, and prevent unsupported outputs from becoming operational decisions, DFIR conclusions, customer-facing reports, or sensitive response actions.
