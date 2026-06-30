# Tiered SOC Review Model

## Purpose

This file defines the tiered SOC review model for governed Agentic MSSP / MDR / DFIR security operations.

The tiered review model establishes how agent-assisted outputs, analyst findings, escalation recommendations, customer-facing summaries, DFIR conclusions, evidence-handling decisions, and sensitive operational recommendations move through appropriate human review levels before downstream use.

Tiered SOC review provides structured human validation and escalation. It does not replace PDP authorization, PEP enforcement, Agent Judge assurance, formal approval workflows, customer approval paths, tool execution controls, evidence authority, incident command authority, or forensic certification.

## Scope

This file applies to tiered SOC review for:

- Agent-generated triage, enrichment, investigation, and recommendation outputs.
- Analyst-reviewed alerts, incidents, evidence summaries, and escalation packages.
- MSSP and MDR service-desk, triage, investigation, and escalation workflows.
- DFIR draft findings, timelines, evidence summaries, and reportable conclusions.
- Customer-facing reports, executive summaries, governance evidence, legal-sensitive outputs, and approval packages.
- Containment, remediation, access-change, evidence-release, escalation, closure, or customer-notification recommendations.
- Tool requests, MCP-mediated access, data ingestion, retrieval, memory, and downstream use where tiered review is required.
- Private/local LLM-assisted DFIR workflows that affect evidence interpretation, reportable findings, or customer-facing outputs.

This file does not define PDP decision logic, PEP implementation behavior, Agent Judge scoring, customer approval workflow design, evidence repository internals, or incident command procedures.

## Non-Goals

Tiered SOC review MUST NOT be used to:

- Treat Tier 1, Tier 2, Tier 3, or service-tower review as PDP authorization.
- Treat analyst review as formal approval unless a formal approval workflow explicitly provides that authority.
- Treat escalation as approval.
- Treat Agent Judge findings as human validation.
- Treat customer-facing release readiness as customer approval.
- Allow agents, tools, workflows, or models to approve their own outputs or actions.
- Override a PDP `DENY` unless routed through a separately governed exception process explicitly permitted by policy.
- Treat private/local LLM execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## Tiered Review Principles

| Principle | Requirement |
|---|---|
| Explicit tier ownership | Each review tier MUST have defined authority, responsibility, and escalation boundaries. |
| Scope-bound decisions | Review outcomes MUST apply only to the reviewed tenant, customer, case, evidence set, output, action, destination, and time window. |
| Tenant and customer separation | `tenant_id` and `customer_id` MUST remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows. |
| Evidence-bound review | Tiered review involving findings, recommendations, DFIR conclusions, governance evidence, or customer-facing output MUST preserve evidence references. |
| Retrieval and memory boundary control | Tiered review involving RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context MUST preserve knowledge store or memory scope. |
| Review is not approval | Tiered review MAY validate, reject, correct, route, or escalate; it MUST NOT be treated as formal approval unless a formal approval workflow provides that authority. |
| Customer approval is explicit | Customer approval MUST remain separate from tiered review and MUST be captured when customer authorization is required. |
| Fail closed | Missing, ambiguous, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out-of-scope review context MUST block or route to controlled review. |
| Auditability | Tiered review decisions, rationale, escalation, approval handoffs, and downstream use MUST be auditable. |

## Review Tier Model

| Tier | Role | Review Boundary |
|---|---|---|
| Tier 1 / Initial Triage | Performs initial alert, enrichment, and routing review. | May validate basic scope, evidence presence, severity indicators, and routing readiness. MUST escalate uncertainty, unsupported claims, customer-facing output, DFIR materiality, or sensitive actions. |
| Tier 2 / Investigation Review | Performs deeper investigation, correlation, evidence review, and recommendation validation. | May validate investigation summaries, evidence support, tenant/customer scope, and operational recommendations within assigned authority. MUST escalate high-impact, customer-facing, legal-sensitive, or DFIR-conclusive items. |
| Tier 3 / Senior Review | Performs high-risk technical review, advanced investigation validation, and service-tower coordination. | May validate high-risk findings, complex evidence interpretation, and sensitive recommendations. MUST route formal approval, customer approval, DFIR lead, incident commander, legal, privacy, or governance items where required. |
| DFIR Lead / Examiner Review | Validates forensic conclusions, evidence interpretation, timelines, and reportable findings. | Required where outputs affect DFIR conclusions, evidence handling, forensic reporting, or customer-facing DFIR material. |
| Incident Commander / Service Owner Review | Validates operational impact, response strategy, service ownership, containment posture, and recovery coordination. | Required where actions materially affect customer operations, service availability, containment, recovery, closure, or communications. |
| Governance / Legal / Privacy / Compliance Review | Validates governance-sensitive, legal-sensitive, privacy-sensitive, regulatory, contractual, public, or audit-supporting material. | Required where outputs may affect legal, compliance, privacy, contractual, governance, or public/training use. |
| Customer Approval Path | Provides customer-side authorization where required. | Required for customer-facing release, customer evidence release, customer-impacting action, containment, remediation, reporting, or external disclosure where customer authorization applies. |

## Required Tiered Review Inputs

Tiered SOC review workflows MUST receive enough context to support accountable review, escalation, and downstream routing.

| Input | Requirement | Purpose |
|---|---|---|
| `tiered_review_request_id` | MUST | Unique identifier for the tiered review request. |
| `workflow_id` | MUST | Identifies the originating workflow, run, case, or process. |
| `workflow_stage` | MUST when routing or authority depends on stage | Identifies triage, investigation, DFIR, containment, reporting, closure, approval, exception, or customer-release stage. |
| `review_tier` | MUST | Identifies Tier 1, Tier 2, Tier 3, DFIR lead, incident commander, governance, legal, privacy, compliance, or customer approval path. |
| `review_reason` | MUST | Explains why review at this tier is required. |
| `requester_identity` | MUST | Identifies the human, agent, workflow, service, or process requesting review. |
| `requester_authority_context` | MUST when routing depends on requester authority | Identifies requester role, team, tenant authorization, and case relationship. |
| `reviewer_identity` | MUST when a reviewer is assigned or completes review | Identifies the reviewer. |
| `reviewer_authority_scope` | MUST when reviewer authority affects routing, approval, or downstream use | Preserves reviewer authority context. |
| `agent_id` | MUST when an agent generated, influenced, routed, or consumed the reviewed item | Identifies the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent generated, influenced, routed, or consumed the reviewed item | Supports replay and run-level traceability. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` or `incident_id` | MUST when review relates to an investigation, alert, incident, ticket, or DFIR matter | Links review to the governed operational record. |
| `workspace_id` | MUST when workspace scope affects telemetry, evidence, review, routing, or downstream use | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects the review | Preserves cloud account, subscription, or project boundary. |
| `evidence_object_ids` | MUST when review relies on evidence, investigation context, DFIR findings, governance evidence, or customer-facing content | Preserves evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context affects review | Defines approved retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| `data_classification` | MUST when classification affects review, routing, release, reuse, evidence handling, approval, or downstream use | Preserves data-handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when use is constrained to workflow, case, customer, legal, governance, evidence-handling, reporting, or DFIR purposes | Defines permitted downstream use. |
| `retention_policy_id` | MUST when retention affects evidence, retrieved context, output storage, release, reuse, or disposal | Preserves retention boundary. |
| `output_destination` | MUST when release, routing, disclosure, reporting, evidence handling, governance evidence, or downstream use depends on destination | Identifies where output is sent, stored, released, displayed, or consumed. |
| `policy_decision_reference` | MUST when review is triggered by PDP result or policy obligation | Links review to policy context. |
| `agent_judge_result_refs` | MUST when Agent Judge findings influenced review or routing | Links review to assurance findings considered. |
| `human_review_record_id` | MUST when human review is required or completed | Links review to the human review outcome. |
| `approval_record_id` | MUST when formal approval is required or completed | Links review to approval context. |
| `customer_approval_record_id` | MUST when customer-side approval is required or completed | Links review to customer authorization. |
| `audit_reference_id` | MUST when review is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, review, approval, customer approval, and audit records. |

## Tier Routing Requirements

| Condition | Required Routing |
|---|---|
| Basic alert enrichment with complete scope and no customer-facing use | Tier 1 review MAY be sufficient if policy permits and required audit context exists. |
| Evidence interpretation, unsupported-claim risk, customer-scoped output, or routing ambiguity | Route to Tier 2 review. |
| High-risk operational recommendation, cross-tenant ambiguity, sensitive data exposure, or policy exception | Route to Tier 3, governance, or formal approval path. |
| DFIR conclusion, timeline, root cause, scope, impact, attribution-sensitive statement, or final report content | Route to DFIR lead or examiner review. |
| Containment, remediation, access change, closure, recovery, or customer-impacting operational decision | Route to incident commander, service owner, or sensitive action approval path. |
| Customer-facing release, customer notification, evidence release, externally visible output, or customer-impacting action | Route to customer approval path where required. |
| Legal, privacy, regulatory, contractual, public, training, or audit-supporting use | Route to legal, privacy, compliance, governance, or executive review where required. |
| PDP `REQUIRE_APPROVAL` | Route to formal approval and remain blocked until valid approval exists. |
| PDP `DENY` | Fail closed; route only to separately governed exception review where explicitly permitted by policy. |
| Retrieval or memory scope uncertainty | Route to evidence, retrieval, governance, tenant-boundary, or senior review. |

## Tiered Review Outcomes

Tiered review workflows MUST define explicit outcomes.

| Outcome | Meaning |
|---|---|
| `TIER_REVIEW_VALIDATED` | Reviewer validated the item within tier authority and scope. This is not formal approval unless connected to an approval workflow. |
| `TIER_REVIEW_REJECTED` | Reviewer rejected the item. |
| `TIER_REVIEW_REQUEST_MORE_EVIDENCE` | Additional evidence or context is required. |
| `TIER_REVIEW_ESCALATED` | Item must be routed to a higher tier, different service tower, DFIR lead, incident commander, legal/compliance/privacy function, governance owner, or customer approver. |
| `TIER_REVIEW_ROUTE_TO_APPROVAL` | Item must enter the formal approval workflow. |
| `TIER_REVIEW_ROUTE_TO_CUSTOMER_APPROVAL` | Item must enter the customer approval path. |
| `TIER_REVIEW_CORRECT_AND_RESUBMIT` | Item must be corrected before further use. |
| `TIER_REVIEW_BLOCKED_FAIL_CLOSED` | Workflow cannot proceed because required context, evidence, approval, review, authority, policy, or auditability is missing or invalid. |

Tiered review outcomes are review and routing states unless produced by a formal approval workflow or governed PDP. They MUST NOT be represented as PDP authorization decisions by themselves.

## Relationship to PEP/PDP

Tiered SOC review does not replace policy enforcement.

| PDP Result | Tiered Review Handling |
|---|---|
| `ALLOW` | Workflow MAY proceed only if no separate tiered review, HITL, approval, customer approval, evidence, or destination requirement applies. |
| `REQUIRE_APPROVAL` | Tiered review may route to approval, but the workflow MUST remain blocked until valid approval exists. |
| `DENY` | The workflow MUST fail closed. Escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default. |

The PEP MUST enforce the PDP decision and returned obligations. If tiered review context, approval context, reviewer authority, or audit logging cannot be verified where required, the workflow MUST fail closed.

## Human Review and Approval Boundaries

Tiered review, formal approval, customer approval, escalation, and incident command authority MUST remain separate.

Tiered review MAY validate, reject, correct, route, or escalate outputs.

Formal approval MAY authorize sensitive release, containment, remediation, access change, evidence release, or customer-facing communication when required by policy.

Customer approval MAY authorize customer-facing release, evidence handling, customer-impacting actions, reporting, or external disclosure when required.

Tiered review records MUST NOT convert unsupported claims, missing evidence, unresolved Agent Judge findings, policy denial, or tool success into approved operational facts.

## Tiered Review for Customer-Facing Outputs

Customer-facing output requires the appropriate review tier before release or customer approval routing.

The reviewer MUST verify, where applicable:

- The output belongs to the correct tenant, customer, case, and destination.
- Evidence references support the material claims.
- Customer identity remains separate from tenant identity.
- Limitations, assumptions, and uncertainty are disclosed where material.
- Data classification, sensitivity label, allowed use, and retention policy support the intended release.
- Retrieval or memory scope is valid when retrieved context influenced the output.
- Required customer approval exists before release where required.
- The output does not claim legal, compliance, regulatory, forensic, or production-readiness authority without the required review path.

## Tiered Review for DFIR Conclusions

DFIR conclusions require review by an authorized DFIR lead, examiner, or assigned authority before reportable use.

The reviewer MUST verify, where applicable:

- Findings distinguish observed facts, inferences, assumptions, hypotheses, and conclusions.
- Evidence object identifiers support the conclusion.
- Evidence tenant and customer attribution are preserved.
- Timeline statements are traceable to evidence timestamps.
- Chain-of-custody or evidence-handling expectations are preserved where applicable.
- Private/local LLM-assisted output remains subject to examiner review and evidence validation.
- Model output is not treated as forensic proof.
- Customer-facing DFIR conclusions follow required review and approval paths.

## Private / Local LLM-Assisted DFIR Tiered Review

For private/local LLM-assisted DFIR workflows, tiered review is required when:

- Model output affects reportable DFIR conclusions.
- Evidence references are missing, ambiguous, or inconsistent.
- Timeline reconstruction cannot be validated from evidence.
- Extracted artifacts are not traceable to source evidence.
- The output introduces unreferenced artifacts, entities, timestamps, or conclusions.
- Knowledge store or memory scope is missing, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent.
- Customer-facing release, legal-sensitive output, governance evidence, or evidence export is involved.

Private/local execution does not make model output authoritative. It only changes where processing occurs. Examiner validation, evidence review, and required approval paths still apply.

## Fail-Closed Conditions

Tiered review workflows MUST fail closed, remain blocked, or route to controlled review when:

- Required tiered review is missing for a tier-review-gated workflow.
- Required reviewer identity, role, authority scope, review rationale, or review outcome is missing, ambiguous, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required tenant, customer, workspace, case, evidence, destination, review, approval, customer approval, or policy context is missing, conflicting, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, or retention policy is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where tiered review, customer-facing release, DFIR conclusions, governance evidence, approval routing, or downstream use depends on it.
- Evidence references are missing for material investigative, DFIR, governance, approval, or customer-facing output.
- Material claims are unsupported or contradicted by evidence.
- Agent Judge findings identify unresolved unsupported claims, tenant-boundary risk, evidence insufficiency, output-quality risk, or HITL non-compliance.
- PDP returns `DENY`; escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default.
- PDP returns `REQUIRE_APPROVAL` and valid approval is not present.
- The reviewer lacks authority for the tenant, customer, case, action type, risk level, evidence sensitivity, or destination.
- Customer approval is required but missing, expired, revoked, incomplete, ambiguous, unauditable, or out of scope.
- Audit logging or context preservation fails.
- The review package cannot distinguish facts from model-generated inference.

Fail-closed handling MUST preserve the request context, evidence references, review reason, routing reason, reviewer authority context, approval context where applicable, customer approval context where applicable, and audit reference.

## Audit Requirements

Tiered review workflows MUST audit:

- Tiered review record identifier.
- Review tier, status, outcome, and rationale.
- Requester identity and authority context.
- Reviewer identity, role, and authority context.
- Tenant, customer, workspace, case, incident, alert, and service-tower context.
- Agent identity, session identity, workflow identity, and initiating user or system.
- Evidence references and evidence tenant/customer attribution metadata.
- `knowledge_store_or_memory_scope` where retrieval or memory influenced review, evidence interpretation, routing, customer-facing wording, governance evidence, approval package, DFIR conclusions, or downstream use.
- `knowledge_memory_scope_result` where retrieval or memory scope was evaluated.
- `data_classification`, `sensitivity_label`, `allowed_use`, and `retention_policy_id` where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- Agent Judge findings considered during review.
- PEP/PDP decision and obligations, where applicable.
- `human_review_record_id`, `approval_record_id`, and `customer_approval_record_id` where review, formal approval, or customer approval is required or completed.
- Output destination and approved audience.
- Review timestamp, correlation identifier, and workflow step.
- Escalation reason, rejection reason, request-more-evidence reason, or fail-closed reason.
- Known limitations or unresolved uncertainty.

If the workflow cannot create the required audit record, the tiered review workflow MUST remain blocked until the issue is reviewed or remediated.

## Operational Anti-Patterns

Avoid the following:

- Treating Tier 1 review as approval for customer-facing release.
- Treating Tier 2 or Tier 3 validation as formal approval without an approval workflow.
- Treating tiered review as a PDP decision.
- Treating escalation from a review tier as approval.
- Allowing an agent to review or approve its own request.
- Allowing lower-tier review to authorize privileged, irreversible, customer-impacting, or externally visible action.
- Releasing customer-facing content without required approval.
- Approving DFIR conclusions based only on model output.
- Using local/private LLM execution as a reason to skip DFIR validation.
- Treating Agent Judge findings as optional when they identify material risk.
- Reusing tiered review outcomes across tenants, customers, cases, evidence sets, destinations, or time windows.
- Allowing missing audit records to default to approval or release.
- Treating Entra Agent ID, agent registry, identity governance, or lifecycle controls as operational SOC agents.

## Acceptance Criteria

This file is acceptable when:

- Tiered SOC review defines reviewer authority by tier and workflow risk.
- Tiered SOC review preserves tenant, customer, case, evidence, destination, review, approval, and customer approval boundaries.
- Tiered SOC review preserves `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where retrieval or memory affects review or downstream use.
- Tiered SOC review preserves data classification, sensitivity label, allowed use, and retention policy where sensitive data handling, release, reuse, customer-facing output, governance evidence, approval routing, or DFIR conclusions are involved.
- Tiered SOC review remains separate from Agent Judge assurance, PEP/PDP enforcement, formal approval, customer approval, tool execution, evidence authority, incident command authority, and forensic certification.
- Higher-tier or specialized review is required before customer-facing release, DFIR conclusions, sensitive action recommendations, evidence release, or externally visible output where required.
- Fail-closed handling exists for missing context, unsupported claims, invalid approvals, unauthorized reviewers, unresolved retrieval/memory scope, improper tier routing, and audit failures.
- Audit replay can reconstruct requester identity, reviewer identity, reviewer authority scope, review tier, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, human review record, approval record, customer approval record, rationale, outcome, routing, and downstream use.
