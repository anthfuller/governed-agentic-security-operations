# HITL Compliance Judge

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

## Purpose

The HITL Compliance Judge is an AI assurance component that evaluates whether required human-in-the-loop review, approval, escalation, or customer authorization requirements were satisfied for governed Agentic SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR workflows.

It supports the governed Agentic MSSP / MDR / DFIR architecture by evaluating whether agent outputs, proposed actions, investigation conclusions, containment recommendations, evidence handling steps, and customer-facing deliverables include the required human review evidence before they are relied upon, routed, executed, or released.

The judge evaluates compliance with HITL expectations. It does not approve actions, authorize execution, override policy, or replace human accountability.

## Scope

This judge applies to workflows where agentic systems participate in:

- Investigation summarization.
- DFIR report drafting.
- Alert enrichment and triage.
- Escalation recommendations.
- Containment recommendations.
- Customer-facing security reporting.
- Evidence review, evidence selection, or evidence interpretation.
- Governance evidence preparation.
- High-impact operational recommendations.
- Actions that require analyst, incident commander, customer, legal, compliance, governance, or executive review.

This file defines the assurance boundary for HITL compliance evaluation only. Detailed approval workflow design belongs in `human-oversight/`. PDP decision contracts, risk classification, fail-closed behavior, and audit schemas belong in `policy-enforcement/`.

## Non-Goals

The HITL Compliance Judge MUST NOT:

- Act as a human approver.
- Act as a PDP.
- Output policy authorization decisions.
- Execute response actions.
- Modify evidence.
- Determine final incident severity.
- Certify legal, regulatory, or contractual compliance.
- Replace analyst, incident commander, forensic examiner, customer, legal, or governance accountability.

## When This Judge Is Required

The HITL Compliance Judge MUST be applied when agent-generated output, proposed action, evidence interpretation, or workflow state affects governed decisions, customer-facing reporting, DFIR conclusions, containment, isolation, blocking, deletion, eradication, recovery, escalation, closure, legal-sensitive findings, governance evidence, approval workflows, tenant or customer boundaries, identity/access recommendations, or high-impact operational recommendations.

At minimum, HITL compliance evaluation MUST be applied to the following workflow conditions when they are part of a governed workflow:

| Workflow Condition | Minimum Handling |
| --- | --- |
| Customer-facing report, executive summary, or customer deliverable | MUST validate approval requirement, reviewer identity, approval status, approved scope, evidence linkage, and release readiness. |
| DFIR conclusion, forensic timeline, or final incident narrative | MUST validate examiner or authorized reviewer involvement, evidence linkage, approval timing, scope alignment, and customer-release requirements where applicable. |
| Containment, isolation, blocking, deletion, eradication, recovery, or remediation recommendation | MUST validate required approval, reviewer authority, action scope, tenant/customer boundary, operational impact, and approval timing before the recommendation is relied upon or executed. |
| Escalation, severity change, incident closure, or material case disposition | MUST validate required reviewer role, case linkage, evidence support, workflow stage, and approval status before the disposition is treated as governed output. |
| Legal-sensitive, regulatory-sensitive, insurance-sensitive, contractual, or governance evidence output | MUST validate required legal, compliance, governance, customer, or authorized reviewer involvement before the output is used as decision support or released. |
| Cross-tenant, multi-customer, or customer-impacting workflow | MUST validate tenant ID, customer ID, approval scope, reviewer authority, and customer authorization where required. |
| Identity/access-impacting recommendation | MUST validate human approval requirements, reviewer authority, separation of duties, target scope, and policy context before downstream use. |
| Tool request or action proposal that requires human approval | MUST validate approval status, approved scope, action identity, workflow stage, and policy handoff before PEP/PDP or execution handling. |
| Exception, emergency, or break-glass handling | MUST validate justification, reviewer, scope, timing, expiration, and post-event review requirement. |

Exploratory, analyst-only, low-risk internal review MAY use lighter HITL assurance only where policy permits and where the output does not influence governed decisions, customer-facing output, DFIR conclusions, containment, escalation, closure, identity/access changes, tenant/customer boundaries, or high-impact operational recommendations.

## Assurance Boundary

The control boundary addressed by this judge is HITL compliance assurance.

The judge evaluates whether the workflow contains sufficient evidence that required human review or approval occurred before the governed output or action was used in a high-impact path.

Agent Judges MUST NOT make enforcement decisions. The HITL Compliance Judge does not enforce approval. Enforcement remains the responsibility of the governed workflow, PEP/PDP, approval system, or orchestration control. If a separate component is implemented as an authorized PDP function, it MUST be governed, registered, evaluated, and audited as a PDP, not as an Agent Judge.

## Required Inputs

The judge requires enough context to evaluate whether HITL requirements were met for the specific workflow stage and output destination.

| Input | Requirement | Purpose |
| --- | --- | --- |
| `judge_request_id` | MUST | Unique identifier for the assurance evaluation. |
| `judge_contract_id` | MUST for governed workflows | Identifies the judge contract used to evaluate the request. |
| `judge_contract_version` | MUST for governed workflows | Supports replay, regression analysis, and dispute review. |
| `tenant_id` | MUST for tenant-scoped, MSSP, MDR, DFIR, or multi-tenant workflows | Identifies the tenant boundary for the case, workflow, and approval context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-facing, customer-scoped, or multi-customer workflows | Identifies the customer boundary separately from the tenant boundary. |
| `case_id` | MUST when tied to an investigation, incident, DFIR case, customer case, escalation, or closure | Connects the review to the governed case record. |
| `workflow_id` | MUST for governed workflows | Identifies the governed workflow being evaluated. |
| `workflow_stage` | MUST when approval requirements vary by stage | Identifies whether the output is draft, investigation, escalation, containment, reporting, or closure. |
| `agent_id` | MUST | Identifies the agent that produced or influenced the output. |
| `agent_role` | SHOULD | Describes the agent function being evaluated. |
| `output_id` | MUST when evaluating an agent output | Links the evaluation to the specific output. |
| `action_id` | MUST when evaluating a proposed or completed action | Links the evaluation to the proposed or completed action. |
| `risk_level` | MUST when approval requirements depend on risk | Indicates the risk tier used by the workflow or policy. |
| `policy_context_id` | MUST when policy affects approval, routing, release readiness, tenant handling, evidence handling, or fail-closed behavior | Identifies the applicable policy or baseline context. |
| `required_approval_policy_id` | MUST when a policy defines review requirements | Identifies the policy source that requires HITL review. |
| `approval_workflow_id` | MUST when approval was required or triggered | Links the evaluation to the approval workflow. |
| `approval_record_id` | MUST when approval occurred | Links the evaluation to the specific approval record used for audit replay and dispute review. |
| `approval_status` | MUST when approval was required or triggered | Indicates whether approval is pending, approved, denied, expired, revoked, incomplete, or not required. |
| `reviewer_identity` | MUST when human review occurred | Identifies the reviewer or approver. |
| `reviewer_role` | MUST when reviewer authorization depends on role | Supports validation of authority and separation of duties. |
| `approval_timestamp_utc` | MUST when approval occurred | Supports timeliness and audit validation. |
| `approval_expiration_utc` | MUST when approvals are time-bound | Supports stale approval detection. |
| `approved_scope` | MUST when approval is scope-limited | Defines what was reviewed and approved. |
| `evidence_object_ids` | MUST when the output influences investigation, DFIR, decision, approval, or customer-facing reporting | Links the output and approval to referenced evidence. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences the output, approval scope, evidence interpretation, customer-facing wording, DFIR conclusion, or proposed action | Defines approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, and retention boundary. |
| `output_destination` | MUST when review requirements depend on destination | Identifies internal, customer-facing, governance, legal, executive, or operational use. |
| `customer_approval_reference` | MUST when customer approval is required | Links to customer authorization or review record. |
| `customer_approval_status` | MUST when customer approval is required | Indicates whether customer approval is pending, approved, denied, expired, revoked, incomplete, or outside scope. |
| `customer_approval_scope` | MUST when customer approval is required | Defines the customer-approved output, action, tenant, customer, case, destination, evidence, and workflow scope. |
| `customer_approver_identity` | MUST when customer approval occurred | Identifies the authorized customer-side approver or approval authority. |
| `exception_reference_id` | MUST when exception or break-glass handling is invoked | Links the review to exception governance. |

Free-form approval assertions MUST NOT be used for governed workflows unless they are wrapped in structured approval records with auditable metadata.

## Evaluation Criteria

The judge MUST evaluate applicable workflow records, approval metadata, and output context against the following criteria when the output or action influences investigation, DFIR conclusions, escalation, containment recommendations, approval decisions, governance evidence, customer-facing reporting, legal/regulatory support, or operational response decisions.

| Criterion | Requirement |
| --- | --- |
| Approval requirement identification | The judge MUST determine whether HITL review was required for the workflow stage, risk level, output destination, action type, tenant boundary, customer obligation, or policy context. |
| Approval status | Required approval MUST be completed before the output or action is treated as approved for governed use. |
| Reviewer authorization | The reviewer identity and role MUST be appropriate for the action, tenant, customer, workflow stage, and risk level. |
| Separation of duties | The approving human MUST NOT be the same actor or agent identity that generated the output where separation of duties is required. |
| Evidence linkage | Approval MUST be traceable to the evidence, output, recommendation, or action that was reviewed. |
| Knowledge and memory scope linkage | Approval MUST be traceable to the knowledge store or memory scope when retrieved context, RAG, vector search, shared memory, customer context, case memory, or evidence retrieval influenced the reviewed output, evidence interpretation, recommendation, or action. |
| Scope alignment | Approval scope MUST match the actual output, action, tenant, customer, case, destination, and workflow stage. |
| Timeliness | Approval MUST occur before the governed output is released or the governed action is executed. |
| Expiration handling | Expired, revoked, or stale approvals MUST NOT be treated as valid. |
| Customer approval | Customer authorization MUST be present, valid, attributable, timely, and scoped where customer-facing, tenant-impacting, customer-controlled, evidence-transfer, customer-notification, risk-acceptance, or provider-operated actions require it. |
| Exception handling | Break-glass or exception workflows MUST include documented reason, reviewer, scope, timing, expiration where applicable, and post-event review requirement. |
| Output routing | Outputs requiring review MUST remain in draft, review, restricted, or blocked state until the required approval evidence is present. |
| Policy handoff | The judge result MUST be available to the governed workflow, PEP/PDP, or orchestration layer for routing, audit, or fail-closed handling. |

## Human Approval Conditions

Human review or approval MUST be validated when the workflow involves:

- Customer-facing investigation reports.
- DFIR conclusions or final incident narratives.
- Containment, isolation, blocking, disabling, deletion, eradication, recovery, or remediation recommendations.
- Escalation or severity changes that affect operational response.
- Incident closure or material case disposition.
- Legal, regulatory, governance, insurance, contractual, or customer obligation evidence.
- Evidence interpretation that materially affects incident conclusions.
- Use of private/local LLM-assisted DFIR output in a reportable decision.
- Identity or access-impacting recommendations.
- Exception, break-glass, or emergency handling.
- Cross-tenant impact, customer-visible changes, or service-provider action on behalf of a customer.

The judge evaluates whether the approval requirement was satisfied. It does not grant approval.

## Judge Outputs

For governed workflows, the judge MUST produce structured findings that can be consumed by assurance dashboards, workflow routing, audit systems, or policy enforcement handoffs.

The judge MUST NOT output `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`. Those are PDP decision outputs. If a separate component is implemented as an authorized PDP function, it MUST be governed, registered, evaluated, and audited as a PDP, not as an Agent Judge.

The judge output MUST include a standard Agent Judge `finding` field and a separate HITL-specific validation field such as `hitl_validation_result` or `evaluation_result`.

Standard Agent Judge finding values:

| Finding | Meaning |
| --- | --- |
| `PASS` | HITL compliance criteria passed for the evaluated scope. |
| `FAIL` | Required HITL compliance criteria failed. |
| `NEEDS_REVIEW` | Human review is required before the output or action may be relied upon. |
| `INSUFFICIENT_EVIDENCE` | Required HITL context or approval evidence is missing or cannot be validated. |
| `NOT_APPLICABLE` | HITL compliance evaluation does not apply to the evaluated item. |

HITL-specific compliance status values:

| HITL Status | Meaning |
| --- | --- |
| `HITL_COMPLIANT` | Required human review evidence is present, scoped, timely, and traceable. |
| `HITL_NON_COMPLIANT` | Required human review evidence is missing, invalid, stale, out of scope, unauthorized, or not traceable. |
| `INSUFFICIENT_EVIDENCE` | The judge cannot determine compliance because required context or records are missing. |
| `NEEDS_HUMAN_REVIEW` | The workflow requires human review before the output can be relied upon. |
| `OUT_OF_SCOPE` | The evaluated item is outside this judge's HITL assurance boundary. |

A `PASS` finding with `HITL_COMPLIANT` status means the HITL compliance check passed for the evaluated scope. It does not authorize execution, release, containment, escalation, closure, or customer communication.

## Recommended Finding Schema

| Field | Requirement | Purpose |
| --- | --- | --- |
| `judge_result_id` | MUST | Unique identifier for the judge result. |
| `judge_request_id` | MUST | Correlates the judge result to the evaluation request. |
| `judge_contract_id` | MUST for governed workflows | Identifies the judge contract applied. |
| `judge_contract_version` | MUST for governed workflows | Supports replay and regression analysis. |
| `judge_id` | MUST | Identifies the judge that produced the result. |
| `judge_version` | MUST | Supports repeatability, change tracking, and dispute review. |
| `timestamp_utc` | MUST | Records evaluation time in UTC. |
| `tenant_id` | MUST for tenant-scoped workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-facing, customer-scoped, or multi-customer workflows | Preserves customer boundary context. |
| `case_id` | MUST when tied to a case, incident, DFIR matter, escalation, or closure | Links result to the case record. |
| `workflow_id` | MUST for governed workflows | Links result to the governed workflow. |
| `workflow_stage` | MUST when applicable | Shows where the compliance check occurred. |
| `agent_id` | MUST | Identifies the agent that produced or influenced the output or action. |
| `output_id` | MUST when output-based | Identifies the evaluated output. |
| `action_id` | MUST when action-based | Identifies the evaluated action. |
| `approval_workflow_id` | MUST when approval was required or triggered | Links to approval workflow. |
| `approval_record_id` | MUST when approval occurred | Links to the specific approval record used for replay and dispute review. |
| `approval_status` | MUST when approval was required or triggered | Shows approval state. |
| `customer_approval_status` | MUST when customer approval is required | Shows customer approval state. |
| `customer_approval_scope` | MUST when customer approval is required | Shows what the customer approved. |
| `customer_approver_identity` | MUST when customer approval occurred | Supports customer-side accountability. |
| `reviewer_identity` | MUST when review occurred | Supports accountability. |
| `reviewer_role` | MUST when review occurred | Supports role validation. |
| `approved_scope` | MUST when approval occurred | Shows what was approved. |
| `finding` | MUST | Standard Agent Judge finding: `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE`. |
| `evaluation_result` | MUST | HITL-specific compliance result such as `HITL_COMPLIANT`, `HITL_NON_COMPLIANT`, `INSUFFICIENT_EVIDENCE`, `NEEDS_HUMAN_REVIEW`, or `OUT_OF_SCOPE`. |
| `finding_summary` | MUST | Summarizes the compliance finding. |
| `missing_requirements` | MUST when applicable | Lists absent or invalid HITL evidence. |
| `evidence_object_ids` | MUST when evidence was part of the reviewed output | Links to reviewed evidence. |
| `knowledge_store_or_memory_scope` | MUST when retrieval or memory influenced the reviewed output, approval scope, evidence interpretation, recommendation, or action | Links HITL validation to approved retrieval, memory, customer, tenant, case, evidence, and retention boundaries. |
| `policy_context_id` | MUST when policy affects handling | Links the result to applicable policy context. |
| `routing_recommendation` | MUST when applicable | Indicates review, remediation, escalation, restriction, block, or policy handoff without acting as PDP authorization. |
| `audit_reference_id` | MUST when applicable | Links the judge result to the audit record. |

## Recommended Routing Values

When `routing_recommendation` is produced, the value MUST be selected from the governed route vocabulary unless the judge contract is explicitly versioned and approved.

| Route | Meaning |
| --- | --- |
| `CONTINUE` | Continue to the next required workflow step. |
| `REQUIRE_HUMAN_REVIEW` | Required human review has not been completed or must be repeated. |
| `REQUIRE_CUSTOMER_APPROVAL` | Customer authorization is required before the output or action can proceed. |
| `RESTRICT_INTERNAL_HANDLING` | Keep the output internal, draft-only, or limited-use until approval evidence is complete. |
| `REVIEW_APPROVAL_SCOPE` | Approval exists but scope alignment must be validated or corrected. |
| `REVIEWER_AUTHORITY_REVIEW` | Reviewer identity, role, or authority must be validated. |
| `REQUEST_MORE_EVIDENCE` | Additional approval, evidence, or workflow context is required. |
| `BLOCK` | Block the output, release, recommendation, or action from governed use. |
| `FAIL_CLOSED` | Fail closed before governed processing continues. |
| `ESCALATE` | Escalation is required under policy or operational procedure. |

Routing values are handling signals. They MAY become policy-relevant inputs to the PDP, but only the PDP produces governed authorization decisions.

## Audit Requirements

Governed workflows using this judge MUST audit:

- Judge request and result.
- Judge identity and version.
- Judge contract identifier and version where applicable.
- Tenant, customer, case, workflow, and workflow stage.
- Agent identity and output or action identifier.
- Approval policy or requirement source.
- Approval workflow identifier and approval record identifier when approval occurred.
- Approval status.
- Reviewer identity and role.
- Approval timestamp and expiration, where applicable.
- Approved scope.
- Evidence object identifiers.
- Knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced the reviewed output, approval scope, evidence interpretation, recommendation, or action.
- Customer approval status, customer approval scope, and customer approver identity where customer approval is required or occurred.
- Judge findings and missing requirements.
- Routing decision made by the workflow, PEP/PDP, or human oversight process.
- Exception or break-glass reference, where applicable.
- Timestamp and audit integrity reference where implemented.

Audit records MUST preserve the original output, judge result, approval metadata, evidence references, and routing reason for governed workflows.

## Fail-Closed Conditions

The HITL Compliance Judge does not enforce fail-closed behavior directly. The governed workflow, orchestration layer, or PEP/PDP MUST fail closed, pause, block release, or route to human review when:

- Required approval evidence or approval record identifier is missing.
- Approval status is denied, expired, revoked, incomplete, or pending.
- Reviewer identity or role cannot be validated.
- Approval scope does not match the output, action, tenant, customer, case, destination, or workflow stage.
- Required customer approval is missing, denied, expired, revoked, incomplete, outside customer authority, outside approved scope, not attributable, or cannot be validated.
- Customer ID is missing for customer-scoped, MSSP, MDR, DFIR, customer-facing, or multi-customer workflows.
- Evidence references required for review are missing or inconsistent.
- Knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influenced the reviewed output, approval scope, evidence interpretation, recommendation, or action.
- The output was changed after approval without re-review.
- A break-glass path lacks required justification, reviewer, scope, expiration where applicable, or post-event review requirement.
- The judge result is `HITL_NON_COMPLIANT` or `INSUFFICIENT_EVIDENCE` for a governed high-impact output.
- The judge is unavailable where HITL compliance evaluation is mandatory.

Fail-closed handling MUST preserve the original output, approval metadata, judge result, evidence references, and routing reason for audit review in governed workflows.

## What Agents Must Not Do

Agents MUST NOT:

- Self-approve their own outputs or actions.
- Mark HITL requirements as satisfied without approval evidence.
- Modify approval records.
- Bypass human review because an output appears low risk without policy evaluation.
- Convert draft DFIR or investigation output into customer-facing reporting without required review.
- Treat absence of a judge finding as approval.
- Execute containment, remediation, deletion, identity/access changes, or customer-impacting actions without required authorization.
- Override a human reviewer, PDP, approval workflow, or customer approval requirement.
- Use synthetic, missing, unrelated, or cross-tenant evidence to claim approval compliance.
- Use RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context outside approved knowledge store or memory scope to claim HITL or customer-approval compliance.

## Failure Modes

Common failure modes include:

- Missing approval workflow linkage.
- Approval recorded against the wrong case, tenant, customer, output, or action.
- Reviewer lacks authority for the risk level or customer context.
- Approval granted before final output changes.
- Approval reused beyond its scope or expiration.
- Approval granted without validating knowledge store or memory scope where retrieved context influenced the output, evidence interpretation, recommendation, or action.
- Customer approval is missing, denied, expired, revoked, incomplete, outside customer authority, outside approved scope, not attributable, or cannot be validated.
- Customer-facing report released from a draft or unreviewed state.
- Break-glass flow used without post-event review.
- Human reviewer validates text quality but not evidence traceability.
- Agent-generated summary implies approval when no approval record exists.
- Judge result is logged but not consumed by the governed workflow.

## Private/Local LLM-Assisted DFIR Considerations

For private/local LLM-assisted DFIR, the judge MUST evaluate whether reportable conclusions, forensic narratives, or customer-facing summaries were reviewed by an authorized human before use.

The judge SHOULD treat local model execution as an evidence handling context, not as proof of correctness. Private execution may reduce data exposure, but it does not remove the need for human validation, evidence traceability, approval records, or auditability.

## Acceptance Criteria

This file is acceptable when the implemented or documented HITL Compliance Judge:

- Clearly remains an assurance component.
- Does not act as a PDP or human approver.
- Defines when HITL compliance evaluation MUST run.
- Evaluates required human review evidence for high-impact outputs and actions.
- Requires tenant, customer, workflow, approval, reviewer, evidence, and output context where applicable.
- Requires knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences reviewed outputs, evidence interpretation, recommendations, approvals, or actions.
- Validates customer approval status, scope, authority, attribution, and expiration where customer approval is required.
- Produces structured findings rather than authorization decisions.
- Supports fail-closed routing without enforcing authorization directly.
- Preserves auditability and traceability.
- Supports customer-facing, DFIR, governance, and operational review boundaries.
- Avoids compliance certification claims.
- Avoids claims that agents replace human accountability.

## Anti-Patterns

Avoid these patterns:

- Treating an Agent Judge result as approval.
- Allowing an agent to self-certify HITL compliance.
- Using the judge as an implicit PDP.
- Reusing approvals across tenants, customers, cases, outputs, or actions without scope validation.
- Allowing customer-facing reports to bypass review because they are AI-generated drafts.
- Treating local/private LLM execution as sufficient assurance.
- Logging approval status without reviewer identity or scope.
- Treating expired or revoked approvals as valid.
- Failing open when approval evidence is missing.
- Duplicating full human approval workflow design inside the AI assurance layer.
