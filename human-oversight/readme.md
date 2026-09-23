# Human Oversight

## Reference Architecture Disclaimer

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

## Purpose

The `human-oversight/` directory defines how accountable humans remain part of governed Agentic SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR workflows.

Human oversight exists to prevent agentic systems from independently making sensitive operational, investigative, customer-facing, containment, escalation, or governance decisions without authorized review. Agents may assist with triage, summarization, evidence organization, drafting, routing, and recommendation generation, but accountable humans remain responsible for approving sensitive actions and validating conclusions.

## Scope

This directory covers:

- Human accountability for agent-assisted security operations.
- HITL and HOTL decision boundaries.
- Approval workflows for sensitive actions.
- Customer approval and customer-facing release controls.
- Escalation, exception, and break-glass oversight.
- Human review of DFIR conclusions, containment recommendations, governance evidence, and operational response decisions.
- Oversight handoffs between agents, Agent Judges, PDP decisioning, PEP enforcement, evidence handling, audit logging, and service tower operations.

This directory does not define:

- PDP decision logic or PEP enforcement behavior.
- Agent Judge evaluation contracts.
- Agent identity lifecycle controls.
- Tenant-isolation implementation details.
- Forensic evidence processing procedures.
- Product-specific configuration instructions.
- Compliance certification mappings.

Those controls belong in the appropriate `policy-enforcement/`, `ai-assurance/`, `agent-governance/`, `local-llm-dfir/`, `workflows/`, or `threat-model/` directories.

## Control Intent

Human oversight enforces the accountability boundary between agent-assisted analysis and authorized operational decision-making.

The control intent is to ensure that:

- Sensitive agent-generated recommendations are reviewed before execution or release.
- Human approvers have sufficient evidence, context, and tenant attribution to make a decision.
- Customer-impacting outputs are not released without appropriate review.
- Containment, escalation, DFIR, governance, and reporting actions remain accountable.
- Missing, ambiguous, or conflicting context causes escalation or fail-closed handling.
- Audit records preserve who reviewed, what was reviewed, what was approved, what was rejected, and why.

## Architecture Alignment

Within the governed Agentic MSSP / MDR / DFIR architecture, human oversight acts as an accountability layer across the operating model.

Agents may propose actions or draft outputs. Agent Judges may assess quality, policy alignment, unsupported claims, evidence support, tenant-boundary risk, and HITL compliance. The PDP makes policy decisions and determines whether approval is required. Human approval becomes bound evidence that returns to the PDP for reevaluation; it does not directly authorize execution. Only the resulting PDP permit reaches the PEP, which enforces the decision and obligations before authorizing access. Human approvers validate sensitive decisions, approve or reject actions, resolve ambiguity, and accept accountability for operational outcomes.

Human oversight is not a substitute for policy decisioning or enforcement. PDP decisioning and PEP enforcement remain separate responsibilities. Human approval MUST NOT override a PDP `DENY` decision unless the request is routed through a separately governed exception process explicitly permitted by policy. Human oversight is also not an Agent Judge function. Agent Judges provide assurance signals, not final accountability.

Microsoft Entra Agent ID and Microsoft Agent 365 belong in the Agent Governance & Identity Control Plane. They should not be treated as operational SOC agents or human-oversight decision makers.

## HITL and HOTL Model

| Oversight mode | Meaning | Appropriate use |
|---|---|---|
| Human-in-the-loop (HITL) | A human decision is required before the workflow may proceed. | Sensitive actions, customer-facing outputs, containment recommendations, DFIR conclusions, escalation decisions, governance evidence, exception handling, or ambiguous tenant context. |
| Human-on-the-loop (HOTL) | Humans supervise, monitor, and can intervene, but routine low-risk workflow steps may proceed under policy. | Low-risk enrichment, non-destructive summarization, queue organization, internal draft preparation, or telemetry review where policy permits. |

HITL MUST be used when the workflow affects customer-facing reporting, DFIR conclusions, containment recommendations, escalation, policy exceptions, governance evidence, approval routing, or cross-tenant risk.

HOTL MAY be used only where the action is low risk, reversible, internally scoped, policy-permitted, and fully audited.

## Human Oversight Roles

Organizations may adapt role names, but governed workflows SHOULD distinguish the following accountability functions:

| Role | Primary responsibility |
|---|---|
| SOC Analyst | Reviews triage, validates evidence, confirms operational context, and escalates when needed. |
| MDR / MSSP Service Lead | Confirms service-tower ownership, customer obligations, routing, escalation, and reporting expectations. |
| Incident Commander / DFIR Lead | Approves or rejects incident conclusions, containment recommendations, evidence handling decisions, and investigative direction. |
| Customer Approver | Authorizes customer-impacting actions, external reporting, containment requests, or release of formal findings where required. |
| Governance / Risk Owner | Reviews exceptions, policy deviations, risk acceptance, and governance evidence. |
| Policy / Platform Owner | Confirms whether approval workflows, policy requirements, and technical enforcement boundaries are functioning as intended. |
| Audit Reviewer | Reviews accountability records, approval evidence, exception records, and post-event review artifacts. |

A single person may hold more than one role in smaller environments, but role accountability MUST remain clear in the audit trail.

## Required Human Review Triggers

Human review MUST be required when any of the following conditions apply:

| Trigger | Human review requirement |
|---|---|
| Tenant context is missing, ambiguous, mismatched, or cross-tenant risk is detected. | Validate tenant, customer, case, workspace, evidence, destination, and shared-context boundaries. |
| Output affects customer-facing reporting. | Validate claims, evidence support, tenant attribution, severity, scope, and release destination. |
| Output affects DFIR conclusions. | Validate evidence, chain of reasoning, source attribution, uncertainty, and alternative explanations. |
| Output recommends containment or operational response. | Validate blast radius, reversibility, customer approval requirements, and operational risk. |
| Output affects escalation. | Validate severity, service-tower ownership, routing, and recipient scope. |
| Output affects governance evidence. | Validate source evidence, limitations, control interpretation, and approval record. |
| Agent Judge flags unsupported claims, hallucination risk, tenant-boundary risk, or insufficient evidence. | Require analyst validation or escalation before use. |
| PDP returns `REQUIRE_APPROVAL`. | Route to the authorized approval workflow, bind valid approval evidence, and return the request to the PDP for reevaluation before execution. |
| Policy exception or break-glass handling is requested. | Require documented approval, risk acceptance, and post-event review. |
| The destination is external, customer-facing, privileged, or shared across tenants. | Validate release authorization and destination boundary. |

Human review MUST be required when model output is materially uncertain, evidence is incomplete, the proposed action is irreversible, or operational risk is not clearly classified and the output affects DFIR conclusions, customer-facing reporting, containment recommendations, escalation, governance evidence, approval routing, or operational response decisions.

## Required Inputs to Human Review

Human review MUST receive enough context to make an informed and auditable decision.

Required inputs include, where applicable:

- Tenant, customer, workspace, case, and service-tower context.
- Agent identity, session identity, request identity, and initiating user or workflow.
- Proposed action, output, recommendation, or release artifact.
- Risk classification and approval requirement.
- Evidence object references and evidence tenant-attribution metadata.
- Agent Judge findings, including unsupported-claim, evidence-support, tenant-boundary, and HITL compliance signals.
- PDP decision and approval requirements, plus PEP obligations and constraints.
- Tool name, tool contract, action type, and output destination.
- Known limitations, uncertainty, missing evidence, or conflicting context.
- Prior approvals, exception records, or customer authorization requirements.
- Reviewer authority scope, or equivalent metadata, so the workflow can validate that the approver is authorized for the tenant, customer, case, action type, and risk level.
- Time, source system, workflow step, and routing path.

If required review context is missing or cannot be verified, the workflow MUST fail closed or route for escalation.

## Human Review Outputs

Human review decisions MUST be explicit and auditable.

Human review workflows MUST define explicit allowed review outcomes. Baseline outcomes SHOULD include:

| Outcome | Meaning |
|---|---|
| Approved | The reviewed action or output may proceed within the approved scope. |
| Rejected | The reviewed action or output may not proceed. |
| Request More Evidence | The workflow cannot proceed until additional evidence or context is provided. |
| Escalated | The decision requires a different approver, service tower, customer representative, DFIR lead, or governance owner. |
| Reclassified | The risk level, severity, scope, or routing has been changed by an authorized reviewer. |
| Exception Review | The request requires policy exception handling, risk acceptance, or emergency governance review. |
| Break-Glass Approved | Emergency handling is approved under defined constraints and mandatory post-event review. |

Approval MUST be scoped. A human approval for one tenant, customer, case, action, destination, time window, or evidence set MUST NOT be reused for a different scope unless policy explicitly permits it and the reuse is audited. Where scoped approval is used, the approval record MUST include `approval_valid_until`, `approval_expiration`, or equivalent expiration metadata.

## What Humans Must Approve

Human approval MUST be required before:

- Releasing customer-facing findings, reports, summaries, or recommendations.
- Making or endorsing DFIR conclusions.
- Recommending or initiating containment actions where customer or operational impact exists.
- Escalating incidents to customers, executives, regulators, legal teams, or external parties where policy requires review.
- Accepting policy exceptions, break-glass actions, or risk acceptance decisions.
- Using incomplete, ambiguous, or conflicting evidence in a material conclusion.
- Proceeding when tenant or customer boundaries cannot be confidently validated.
- Handing off actions to privileged tools, downstream workflows, or external destinations when approval is required by policy.

Human approval MUST be required for high-impact internal decisions that affect containment, escalation, privileged action, DFIR conclusions, evidence handling, tenant-boundary decisions, governance evidence, or operational response.

## What Agents Must Not Do

Agents MUST NOT:

- Self-approve actions, reports, conclusions, exceptions, or escalations.
- Override human approval requirements.
- Change `reviewer_required`, risk classification, tenant attribution, or approval routing to avoid review.
- Release customer-facing content without authorized approval.
- Declare DFIR conclusions as final without human validation.
- Initiate containment actions unless explicitly authorized through policy and approval workflows.
- Bypass PDP decisioning, required approval reevaluation, or PEP enforcement.
- Suppress Agent Judge findings or audit events.
- Alter, delete, or fabricate evidence references.
- Reuse approvals outside the approved scope.
- Treat human silence, timeout, or non-response as approval.
- Present confidence scores as a substitute for accountable human review.

## Audit Requirements

Human-oversight workflows MUST generate audit records for governed decisions.

Audit records MUST include, where applicable:

- Reviewer identity and role.
- Tenant, customer, workspace, case, and service-tower context.
- Requested action, output, recommendation, or artifact.
- Evidence object references and tenant-attribution metadata.
- Agent identity, session identity, workflow identity, and initiating user or system.
- Agent Judge findings used during review.
- PDP decision and PEP obligations.
- Approval outcome, rejection reason, escalation reason, or request for more evidence.
- Approval scope, expiration, constraints, and destination.
- Timestamp, source system, workflow step, and correlation identifier.
- Exception or break-glass justification.
- Post-event review record for emergency handling.

Audit records MUST be tamper-resistant according to the organization’s logging and retention requirements.

## Fail-Closed Conditions

The workflow MUST fail closed or route to escalation when:

- Required human approval is missing, expired, invalid, revoked, or out of scope.
- The reviewer is not authorized for the tenant, customer, case, service tower, action type, or risk level.
- Tenant, customer, workspace, case, evidence, or destination context is incomplete or mismatched.
- Evidence references are missing for investigative, DFIR, approval, governance, or customer-facing output.
- Agent Judge findings indicate unsupported claims, tenant-boundary risk, insufficient evidence, or HITL non-compliance and the issue is unresolved.
- PDP returns `REQUIRE_APPROVAL` and no valid approval is present as bound evidence for PDP reevaluation.
- The approval workflow is unavailable or cannot produce an auditable decision.
- The output destination is external, shared, privileged, or customer-facing and release authorization is not verified.
- Break-glass handling is requested without required authorization and post-event review requirements.
- Audit logging fails for a governed workflow.

Fail-closed handling MUST preserve the request context, denial or escalation reason, and evidence references needed for review where technically available. If audit logging or context preservation fails, the workflow MUST remain blocked until reviewed or remediated.

## Human Oversight Failure Modes

Human oversight can fail when:

- Approvers lack sufficient evidence or tenant context.
- Approval routing is unclear or too broad.
- Human review becomes a rubber-stamp process.
- Agent-generated summaries omit limitations, uncertainty, or conflicting evidence.
- Customer approval requirements are not represented in workflow logic.
- Emergency approvals are not followed by post-event review.
- Approval records do not capture scope, constraints, or decision rationale.
- Reviewers approve outputs outside their authority.
- Teams rely on model confidence rather than evidence validation.

These failures SHOULD be treated as architecture and process risks, not merely user-training issues.

## Handoff Boundaries

Human oversight depends on controlled handoffs with other architecture areas:

| Related area | Handoff boundary |
|---|---|
| `agent-governance/` | Provides agent identity, ownership, lifecycle, access context, and accountability metadata. |
| `ai-assurance/` | Provides Agent Judge findings and evaluation signals for human review. |
| `policy-enforcement/` | Provides PDP decisions, PEP obligations, risk classifications, and approval requirements. |
| `local-llm-dfir/` | Provides private/local evidence handling context, draft findings, and analyst validation requirements. |
| `workflows/` | Defines end-to-end routing between agents, judges, the PDP, the PEP, humans, tools, evidence stores, and audit systems. |
| `threat-model/` | Defines abuse cases, bypass paths, reviewer manipulation risks, and residual risks. |
| `templates/` | Provides reusable approval, escalation, exception, and review templates. |

Human oversight files SHOULD reference these areas when needed, but MUST NOT duplicate their detailed controls.

## Private / Local LLM-Assisted DFIR Considerations

For private/local LLM-assisted DFIR workflows, human oversight is especially important because the model may assist with evidence summarization, timeline drafting, artifact interpretation, and report preparation.

Human reviewers MUST validate:

- Evidence source and scope.
- Tenant and customer attribution.
- Chain-of-custody expectations where applicable.
- Whether the model output is supported by referenced evidence.
- Whether the output overstates certainty.
- Whether alternative explanations or limitations are documented.
- Whether the finding is suitable for customer-facing release.

Local model execution does not remove the need for human review. Private processing may reduce certain data-exposure risks, but it does not make model output authoritative.

## F7-LAS Alignment

F7-LAS may be used as a supporting control lens for human oversight.

Human oversight primarily aligns with:

- L4 Tool Layer, where mediated tool execution prevents direct uncontrolled action.
- L5 Policy Engine Layer, where PDP decisions may require approval and the PEP enforces the resulting decision and obligations before authorizing access.
- L6 Sandbox / Blast-Radius Layer, where human approval helps constrain operational impact.
- L7 Monitoring & Evaluation, where review decisions, audit events, and escalation outcomes must remain observable and auditable.

F7-LAS should support the architecture’s accountability model. It should not replace the MSSP / MDR / DFIR operating model or become the primary subject of this directory.

## Recommended Directory Content

This directory contains human-oversight artifacts such as:

| File | Purpose |
|---|---|
| `human-review-model.md` | Defines human review requirements and review boundaries. |
| `hitl-hotl-model.md` | Defines human-in-the-loop and human-on-the-loop operating models. |
| `analyst-review-checkpoints.md` | Defines analyst validation checkpoints for agent-assisted workflows. |
| `tiered-soc-review-model.md` | Defines review escalation across SOC, MDR, MSSP, DFIR, and service-owner roles. |
| `human-accountability.md` | Defines accountable roles, ownership, and decision responsibility. |
| `approval-boundaries.md` | Defines where review ends and formal approval begins. |
| `approval-workflows.md` | Defines approval routing, approval outcomes, expiration, and scope. |
| `sensitive-action-approval.md` | Defines approval requirements for containment, privileged, customer-impacting, and evidence-sensitive actions. |
| `customer-approval-model.md` | Defines when customer approval is required before release or action. |
| `escalation-paths.md` | Defines escalation, exception, and break-glass oversight paths. |
| `fleet-change-approval-and-emergency-override.md` | Defines approval and emergency override controls for fleet-level changes. |
| `review-record-requirements.md` | Defines required fields for review, approval, escalation, and exception records. |

Files in this directory SHOULD remain focused on human accountability and approval workflow boundaries. Detailed PDP logic, Agent Judge evaluation design, evidence processing, or agent lifecycle controls belong in their respective directories.

## Acceptance Criteria

Human-oversight content is acceptable when it:

- Clearly defines when human review is required.
- Separates human approval from Agent Judge assurance, PDP decisioning, and PEP enforcement.
- Identifies reviewer roles and accountable decision owners.
- Requires human approval for sensitive, customer-facing, DFIR, containment, escalation, governance, exception, and cross-tenant-risk workflows.
- Requires evidence references and tenant-attribution metadata for review decisions where applicable.
- Defines explicit review outcomes and scoped approvals.
- Defines fail-closed behavior for missing, invalid, expired, unauthorized, or unauditable approvals.
- Preserves auditability across reviewer identity, decision rationale, evidence references, approval scope, and routing.
- Avoids unsupported product claims, compliance claims, and autonomous SOC language.
- Aligns with governed Agentic MSSP / MDR / DFIR operations.

## Anti-Patterns

Avoid the following:

- Treating agent recommendations as approved decisions.
- Allowing agents to self-approve or suppress review requirements.
- Using Agent Judges as enforcement authorities.
- Treating PDP approval requirements or PEP obligations as optional.
- Releasing customer-facing reports without review.
- Making DFIR conclusions without validated evidence.
- Reusing approvals outside their original scope.
- Approving cross-tenant outputs without tenant-boundary validation.
- Treating confidence scores as evidence.
- Letting reviewer timeout, silence, or workflow failure default to approval.
- Creating broad “human reviewed” statements without reviewer identity, scope, evidence, rationale, and timestamp.
- Using local/private LLM execution as a reason to skip analyst validation.
- Converting this directory into generic AI governance, product documentation, or compliance mapping content.

## Summary

Human oversight is the accountability boundary for governed Agentic MSSP / MDR / DFIR operations. It ensures that agent-assisted analysis, recommendations, reports, escalations, and sensitive actions remain subject to authorized human judgment, evidence validation, tenant-boundary review, and auditable approval.

Agents can assist. Agent Judges can evaluate. The PDP can decide, and the PEP can enforce the resulting permit and obligations. Humans remain accountable for sensitive operational, investigative, customer-facing, exception, and governance decisions.
