# Agent Judges Overview

## Purpose

This document defines the role, boundaries, and operating model for **Agent Judges** in the AI Assurance & Analytics Layer of the **Governed Agentic MSSP / MDR / DFIR Security Operations Architecture**.

Agent Judges evaluate agent outputs, evidence support, tenant scope, human-review requirements, unsupported claims, and operational quality. They provide assurance signals that help determine whether an agent output should proceed, require correction, require review, be escalated, be blocked, or be routed into a governed approval or policy workflow.

Agent Judges are **assurance components**, not autonomous decision-makers, enforcement engines, human approvers, incident commanders, or forensic examiners.

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

---

## Architectural Placement

Agent Judges belong in the **AI Assurance & Analytics Layer**.

They evaluate operational agent behavior and outputs before those outputs are relied upon by analysts, customers, approval workflows, case systems, or governed execution paths.

Agent Judges may provide structured assurance signals to:

- Agent orchestrators
- PEP/PDP workflows
- HITL and HOTL approval workflows
- Audit logging systems
- Case management systems
- Evidence validation workflows
- Model and prompt governance processes
- Detection engineering review workflows
- Customer release review workflows

Agent Judges MUST NOT directly bypass governance controls, directly execute governed tools, or independently authorize operational action.

Microsoft Agent 365 and Microsoft Entra Agent ID belong in the **Agent Governance & Identity Control Plane**, not in the operational SOC agent layer and not inside the Agent Judge function. Agent Judges may evaluate identity, registration, lifecycle, ownership, or policy context produced by that control plane, but they do not replace identity governance, access control, registration, lifecycle management, or authorization.

---

## Scope

Agent Judges may evaluate:

- Agent-generated investigation summaries
- Detection and triage recommendations
- Threat hunting conclusions
- Incident enrichment outputs
- Customer-facing draft reports
- Containment or response recommendations
- Evidence references and case notes
- DFIR timelines and forensic summaries
- ATT&CK / ATLAS mappings
- Tool-use requests or proposed actions before enforcement
- Human approval evidence and review status
- Tenant, customer, workspace, subscription, account, and case boundaries
- Knowledge store, vector search, shared memory, customer context, case memory, and retrieval boundaries where used
- Output risk classification and intended-use alignment
- Sensitive-data, legal-sensitive, or customer-release readiness where policy requires evaluation

Agent Judges apply across MSSP, MDR, cloud incident response, detection engineering, threat hunting, and private/local LLM-assisted DFIR workflows.

---

## Non-Goals

Agent Judges do not:

- Replace the PEP or PDP
- Authorize governed tool execution
- Enforce policy decisions
- Approve containment or response actions
- Replace analyst judgment
- Replace incident command
- Replace customer authorization
- Replace forensic examiner review
- Replace legal, regulatory, or customer-release review
- Certify compliance
- Prove detection correctness
- Prove forensic conclusions
- Operate as autonomous SOC decision-makers

---

## Assurance vs. Enforcement Boundary

The following boundary MUST be preserved:

| Function | Responsible Component |
|---|---|
| Evaluate output quality, grounding, evidence support, tenant boundary, or HITL compliance | Agent Judge |
| Produce assurance finding | Agent Judge |
| Make authorization decision | PDP |
| Enforce authorization decision | PEP |
| Approve sensitive or customer-facing action | Human approval workflow |
| Execute governed tool action | Tool gateway or controlled execution layer |
| Manage agent identity, lifecycle, registration, ownership, and authorization context | Agent Governance & Identity Control Plane |
| Preserve audit record | Audit / logging layer |

Agent Judge findings are signals. They become policy-relevant only when consumed by the PDP, PEP, approval workflow, orchestrator, case workflow, or another governed control under an explicit contract.

Agent Judges MUST NOT be treated as enforcement shortcuts.

---

## Required Separation of Outcomes

Governed workflows MUST preserve separation between judge findings, policy decisions, enforcement results, approvals, tool execution, and audit events.

| Item | Example Values | Meaning |
|---|---|---|
| Agent Judge finding | `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, `NOT_APPLICABLE` | Assurance evaluation result |
| PDP decision | `ALLOW`, `DENY`, `REQUIRE_APPROVAL` | Authorization outcome |
| PEP enforcement result | `ENFORCED`, `DENIED`, `FAILED_CLOSED`, `NOT_EXECUTED` | Enforcement status |
| Human approval status | `APPROVED`, `DENIED`, `PENDING`, `EXPIRED`, `REVOKED`, `REQUIRES_MORE_EVIDENCE` | Human review state |
| Tool execution result | `EXECUTED`, `FAILED`, `BLOCKED`, `NOT_REQUESTED` | Tool action outcome |
| Audit event | `RECORDED`, `FAILED`, `INTEGRITY_VERIFIED` | Audit/logging status |

Agent Judge findings MUST NOT be overloaded as PDP decisions, approval outcomes, enforcement results, or tool execution outcomes.

---

## When Agent Judges Are Required

Agent Judge evaluation MUST be required when policy, workflow design, customer obligation, or risk classification requires assurance before output use, release, escalation, or action.

At minimum, Agent Judge evaluation MUST be applied when the workflow condition affects governed decisions, customer-facing output, containment or response recommendations, DFIR conclusions, tenant or customer boundaries, identity-impacting recommendations, incident escalation or closure, tool requests, or framework mappings used in operational findings.

| Workflow Condition | Minimum Handling |
|---|---|
| Customer-facing output | MUST evaluate grounding, unsupported claims, evidence support, output quality, and release readiness |
| Containment or response recommendation | MUST evaluate evidence support, tenant scope, approval context, and operational impact |
| DFIR timeline, forensic summary, or report draft | MUST evaluate evidence traceability, chain-of-custody context, unsupported conclusions, and reviewer requirements |
| Cross-tenant or multi-customer workflow | MUST evaluate tenant, customer, workspace, subscription, account, environment, and case boundaries |
| Identity, access, or privilege-related recommendation | MUST evaluate evidence support, risk level, approval requirements, identity impact, and intended-use constraints |
| Incident closure, escalation, or material status change | MUST evaluate evidence sufficiency, unsupported claims, operational impact, and required review state |
| ATT&CK / ATLAS mapping used in operational findings | MUST evaluate mapping support and avoid treating mapping as proof of correctness, compliance, or detection effectiveness |
| Tool request before enforcement | MUST evaluate risk context, evidence support, tenant scope, and policy context before PDP/PEP handling |

Agent Judge evaluation MAY be optional for low-risk exploratory analytics only when outputs are not customer-facing, do not influence governed decisions, do not trigger tool execution, and are not relied upon for incident conclusions, operational findings, or operational actions.

---

## Core Judge Categories

### Evidence Support Judge

Evaluates whether operational claims are supported by approved evidence.

For governed workflows, the judge MUST validate applicable evidence fields, including:

- Evidence object identity
- Evidence source
- Case association
- Tenant or customer scope
- Timestamp relevance
- Whether evidence supports the specific claim
- Whether evidence is sufficient for the conclusion or recommendation
- Chain-of-custody metadata where forensic evidence is used

Unsupported claims MUST be marked as `FAIL` or `INSUFFICIENT_EVIDENCE` depending on the evaluation contract.

---

### Hallucination / Unsupported Claim Judge

Evaluates whether the agent introduced facts, entities, conclusions, incident details, root cause statements, attribution claims, or remediation claims that are not grounded in approved evidence.

This judge is required for:

- Customer-facing reports
- Executive summaries
- DFIR findings
- Containment recommendations
- Threat attribution statements
- Legal-sensitive outputs
- High-impact incident conclusions
- Incident closure recommendations

---

### Tenant Boundary Judge

Evaluates whether inputs, outputs, evidence references, queries, case objects, recommendations, and tool-use requests remain within the authorized tenant, customer, workspace, subscription, account, environment, or case boundary.

Cross-tenant data mixing MUST result in `FAIL` and MUST be blocked or fail closed by the governed workflow. Escalation alone is insufficient if data has already been exposed, executed, released, or used in a governed decision.

Tenant boundary evaluation MUST distinguish tenant identity, customer identity, workspace identity, subscription or account identity, case identity, and destination context where those fields are available or required by policy.

---

### Knowledge and Memory Scope Judge

Evaluates whether RAG, vector search, shared memory, customer context, case memory, and knowledge retrieval remain within approved tenant, customer, case, workspace, evidence, and retention boundaries.

Knowledge and memory scope failures MUST be marked as `FAIL` or `NEEDS_REVIEW` according to the judge contract when retrieved context is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or inconsistent with retention requirements.

Knowledge and memory scope findings may inform analyst review, quarantine, PDP context, approval routing, or fail-closed handling. They MUST NOT be treated as standalone authorization to retrieve, persist, release, or reuse context.

---

### HITL / HOTL Compliance Judge

Evaluates whether required human review occurred before sensitive, customer-facing, containment, legal-sensitive, forensic, or high-impact outcomes.

For required approvals, the judge MUST validate where applicable:

- Required reviewer role
- Reviewer identity
- Approval status
- Approval timestamp
- Approval scope
- Expiration or revocation state
- Case or incident association
- Customer approval context where required
- Whether the approved action matches the requested or executed action

A generic approval flag is insufficient where named accountability is required.

---

### Output Quality Judge

Evaluates whether an output is complete, relevant, concise, evidence-grounded, scoped, and appropriate for the intended recipient.

Output quality scoring MAY be used for review routing, but MUST NOT replace authorization, evidence validation, required human approval, tenant-boundary validation, or customer-release review.

---

### ATT&CK / ATLAS Mapping Judge

Evaluates whether ATT&CK or ATLAS mappings are supported by evidence and appropriate to the finding.

Mappings are analytical context. They MUST NOT be treated as compliance proof, control attestation, evidence that an incident conclusion is correct, or proof that a detection is effective.

---

### Forensic Assurance Judge

Evaluates private/local LLM-assisted DFIR outputs, including timeline reconstruction, artifact parsing, evidence summaries, and forensic report drafts.

For forensic workflows, the judge MUST validate where applicable:

- Evidence object references
- Chain-of-custody metadata
- Case association
- Tenant or customer scope
- No unauthorized external data egress where offline or private operation is required
- Analyst review before release
- Whether conclusions are traceable to evidence
- Whether legal, sovereignty, or customer-release constraints require additional review

Forensic Agent Judge findings MUST NOT replace examiner review, legal review, incident command, or customer release approval.

---

## Judge Input Requirements

For governed workflows, Agent Judges MUST receive structured inputs.

At minimum, judge input MUST include applicable fields.

| Field | Requirement | Description |
|---|---|---|
| `judge_id` | MUST | Identifier for the judge being invoked |
| `judge_version` | MUST | Version of the judge logic, prompt, model, rule set, or evaluator |
| `judge_contract_id` | MUST | Identifier for the governed judge input/output contract being enforced |
| `agent_id` | MUST | Agent being evaluated |
| `agent_session_id` | MUST | Agent session or run identifier |
| `workflow_id` | MUST for governed workflows; SHOULD for exploratory or non-governed analytics | Workflow or orchestration identifier supporting replay and traceability |
| `case_id` | MUST when applicable | Case or incident identifier |
| `tenant_id` | MUST when applicable | Tenant boundary identifier |
| `customer_id` | MUST for MSSP, MDR, DFIR, or customer-scoped workflows | Customer boundary identifier |
| `evaluation_scope` | MUST | Scope of the evaluation, such as output, evidence, tool request, customer release, forensic report, or approval check |
| `tenant_scope` | MUST when applicable | Structured tenant, customer, workspace, subscription, account, environment, and case boundary context |
| `input_object_ids` | MUST when applicable | Prompts, requests, artifacts, records, or objects under evaluation |
| `output_object_id` | MUST when applicable | Agent output under evaluation |
| `evidence_object_ids` | MUST when applicable | Evidence used to validate claims |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, or knowledge retrieval is used | Approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, and retention boundary |
| `policy_context_id` | MUST when policy affects routing, release readiness, approval requirements, PDP context, tenant handling, evidence handling, output handling, or fail-closed behavior | Relevant policy, baseline, obligation, or approval context |
| `evaluation_type` | MUST | Type of evaluation being performed |
| `intended_use` | MUST | Analyst-only, customer-facing, containment, forensic, detection engineering, executive reporting, escalation, closure, or other intended use |
| `intended_recipient` | MUST when applicable | Analyst, customer, incident commander, detection engineer, executive, legal reviewer, or automated workflow |
| `risk_level` | MUST when applicable | Risk classification for the output or action |
| `requested_action` | MUST when applicable | Action being evaluated before enforcement |
| `human_approval_context` | MUST when applicable | Approval state and reviewer metadata |
| `customer_release_context` | MUST for customer-facing output | Release readiness, required reviewer, approval state, and customer-facing destination context |

Free-form inputs SHOULD NOT be used for governed workflows unless they are wrapped in a structured request object with auditable metadata.

---

## Judge Output Requirements

For governed workflows, Agent Judges MUST produce structured outputs.

At minimum, judge output MUST include applicable fields.

| Field | Requirement | Description |
|---|---|---|
| `judge_result_id` | MUST | Unique judge result identifier |
| `judge_id` | MUST | Judge identifier |
| `judge_version` | MUST | Judge version |
| `judge_contract_id` | MUST | Identifier for the governed judge input/output contract enforced |
| `timestamp_utc` | MUST | Evaluation timestamp |
| `workflow_id` | MUST for governed workflows; SHOULD for exploratory or non-governed analytics | Workflow or orchestration identifier supporting replay and traceability |
| `finding` | MUST | `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE` |
| `severity` | MUST when applicable | Severity of the finding |
| `confidence` | MUST when produced | Confidence value or rating |
| `rationale_summary` | MUST | Concise rationale without unsupported claims |
| `failed_checks` | MUST when applicable | Specific failed checks |
| `required_controls_evaluated` | MUST when applicable | Required assurance controls evaluated by the judge |
| `policy_obligation_ids` | MUST when applicable | Policy obligations evaluated or referenced by the judge |
| `evidence_object_ids` | MUST when applicable | Evidence considered during evaluation |
| `unsupported_claims` | MUST when applicable | Claims that lack evidence support |
| `tenant_boundary_result` | MUST when evaluated | Tenant boundary evaluation result |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Result of RAG, vector search, shared memory, customer context, case memory, or knowledge retrieval scope validation |
| `evidence_validation_result` | MUST when evaluated | Evidence validation result |
| `hitl_validation_result` | MUST when evaluated | Human approval validation result |
| `customer_release_review_status` | MUST for customer-facing output | Customer release review state |
| `recommended_route` | MUST when applicable | Review, escalation, correction, block, fail-closed, approval, or release route |
| `audit_reference_id` | MUST when applicable | Related audit event or record |

Judge outputs MUST be auditable, replayable, and consistently consumable by downstream workflows.

---

## Standard Finding Values

For governed workflows, Agent Judges MUST use the governed finding vocabulary unless the contract is explicitly versioned and approved.

| Finding | Meaning |
|---|---|
| `PASS` | The evaluated item met the judge criteria |
| `FAIL` | The evaluated item violated one or more required criteria |
| `NEEDS_REVIEW` | The evaluated item requires human review before use |
| `INSUFFICIENT_EVIDENCE` | The judge could not verify the claim, action, or output with available evidence |
| `NOT_APPLICABLE` | The judge criteria do not apply to the evaluated item |

`PASS` does not mean an action is authorized. It means the item passed that specific assurance check.

---

## Recommended Handling by Finding

| Finding | Recommended Handling |
|---|---|
| `PASS` | Continue to the next required control, approval, or workflow step |
| `FAIL` | Block, fail closed, correct, or escalate based on policy |
| `NEEDS_REVIEW` | Route to required reviewer before release, reliance, escalation, closure, or action |
| `INSUFFICIENT_EVIDENCE` | Require more evidence or prevent unsupported use |
| `NOT_APPLICABLE` | Continue only if no policy requires the judge result |

Handling MUST be performed by the governed workflow, not by the Agent Judge acting independently.

---

## Policy Integration

Agent Judge findings MAY be used as PDP input when policy requires assurance context.

Examples:

- A containment recommendation with `INSUFFICIENT_EVIDENCE` MUST NOT proceed to execution unless policy permits the required review path, the required approval is captured, the PDP authorizes the action, and the PEP enforces the decision and obligations.
- A customer-facing report with unsupported claims MUST be corrected, blocked from release, or routed through required customer-release review according to policy.
- A tenant boundary failure MUST cause deny or fail-closed handling where tenant context affects authorization, release, evidence handling, tool access, or governed decision-making.
- A forensic report without required chain-of-custody metadata MUST be blocked from release or operational reliance unless routed through required forensic, legal, or customer review under policy.
- A HITL check failure MUST prevent sensitive action execution where approval is required.
- A read-only investigation output that influences escalation, closure, reporting, containment recommendations, or customer communication MUST still be evaluated and audited where required by policy.

The PDP decision contract MUST remain separate from the judge finding contract.

---

## Human Oversight Requirements

Human review MUST be required when judge findings affect:

- Containment actions
- Customer-facing reports
- Legal-sensitive findings
- Forensic conclusions
- Cross-tenant or tenant-boundary concerns
- High-impact operational recommendations
- Identity or access changes
- Incident closure
- Material escalation decisions
- Public or executive communication

Human review records MUST include named accountability where required by policy.

Customer approval MUST be preserved where the workflow requires customer authorization, customer release approval, customer-side acceptance, or customer-directed response decisions.

---

## Audit Requirements

Agent Judge activity MUST be logged for governed workflows.

Read-only governed actions, investigations, judge evaluations, and evidence lookups MUST produce audit records when used in governed workflows.

Audit records MUST capture applicable fields, including:

- Judge identifier and version
- Judge contract identifier
- Agent identifier and session identifier
- Workflow identifier for governed workflows
- Case, customer, and tenant context where applicable
- Evaluation scope and tenant scope where applicable
- Input and output object references
- Evidence object references
- Knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, or knowledge retrieval is used
- Finding and severity
- Failed checks
- Required controls evaluated
- Policy obligation identifiers where applicable
- Unsupported claims
- Tenant boundary result where evaluated
- Evidence validation result where evaluated
- HITL validation result where evaluated
- Customer release review status where applicable
- Recommended handling route
- Human reviewer identity where applicable
- Related PDP decision reference where applicable
- Related PEP enforcement result where applicable
- Timestamp and audit integrity reference where implemented

Audit records MUST support replay, investigation, review, and continuous improvement.

---

## Model and Prompt Governance

Agent Judges may be implemented using rules, deterministic checks, model-based evaluators, LLM-as-judge patterns, or hybrid approaches.

For governed workflows:

- Judge prompts MUST be versioned.
- Judge criteria MUST be documented.
- Judge outputs MUST be structured.
- Judge changes MUST be reviewable.
- Judge performance SHOULD be periodically evaluated.
- Judge failures and false positives SHOULD be tracked.
- Judge behavior SHOULD be tested against known good, known bad, and ambiguous examples.
- Judge model or provider changes MUST trigger regression testing where model output affects governed assurance findings, approval routing, PDP context, release readiness, tenant handling, evidence validation, or fail-closed behavior.
- Known judge limitations SHOULD be documented and reviewed.

Model-based judges MUST NOT be assumed reliable solely because they produce confident output.

---

## Failure Handling

Agent Judge failures MUST be handled explicitly.

| Failure Condition | Required Handling |
|---|---|
| Judge unavailable for a required control | Fail closed or route to required manual review |
| Judge returns malformed output | Retry only within configured limits, then fail closed or route to required manual review |
| Judge cannot access required evidence | Return `INSUFFICIENT_EVIDENCE` or fail closed based on policy |
| Tenant context missing | Fail closed for tenant-scoped workflows |
| Customer context missing in customer-scoped workflow | Fail closed or route to required manual review before reliance, release, or action |
| Knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent | Fail closed or route to required review according to workflow risk and policy |
| Approval context missing for required approval | Fail closed or route to required approval workflow |
| Policy context missing where policy affects handling | Fail closed or route to required policy review |
| Conflicting judge results | Route to human review or higher-priority policy handling |
| Audit logging failure | Fail closed where audit is mandatory |

Retry behavior MUST be bounded by policy or workflow configuration. Retries MUST NOT become an uncontrolled loop, bypass audit logging, or delay fail-closed handling where required.

A governed workflow MUST NOT silently ignore a required judge failure.

---

## Acceptance Criteria

An Agent Judge implementation is acceptable for governed workflows only when:

- The judge has a documented purpose, evaluation scope, owner, version, and contract.
- Required inputs are structured and include workflow, agent, case, tenant, customer, evidence, policy, and approval context where applicable.
- Outputs use the governed finding vocabulary or an explicitly versioned and approved contract.
- Judge findings are separated from PDP decisions, PEP enforcement results, approval outcomes, and tool execution results.
- Required judge failures cause fail-closed handling, required review, or policy-governed routing.
- Judge activity is logged with sufficient context to support replay, review, investigation, and continuous improvement.
- Customer-facing, forensic, containment, cross-tenant, identity-impacting, or high-impact outputs receive required assurance and human review.
- The implementation does not allow Agent Judges to directly authorize, approve, or execute governed actions.
- Known limitations, false positives, and false negatives are tracked where the judge influences governed workflow handling.
- The implementation preserves customer, tenant, evidence, and case boundaries.
- The implementation captures and evaluates knowledge store or memory scope when RAG, vector search, shared memory, customer context, case memory, or knowledge retrieval influences governed outputs, recommendations, assurance findings, or policy-gated requests.

---

## Anti-Patterns

The following patterns are not acceptable for governed agentic security operations:

- Using Agent Judges as authorization engines
- Allowing judges to directly execute tools
- Treating a judge `PASS` as approval to act
- Treating unsupported claims as low-risk because they sound plausible
- Using free-form judge output where structured output is required
- Allowing tenant-boundary failures to proceed with escalation only after exposure
- Using quality scores as substitutes for evidence validation
- Releasing customer-facing findings without required review
- Treating ATT&CK or ATLAS mapping as proof of correctness
- Treating local/private LLM output as forensic evidence without chain-of-custody support
- Skipping audit records because the action was read-only
- Treating Microsoft Agent 365 or Microsoft Entra Agent ID as operational SOC agents instead of governance and identity control-plane components
- Treating model confidence as evidence support
- Ignoring knowledge store, vector search, shared memory, customer context, case memory, or retrieval scope when judging outputs influenced by retrieved context

---

## Example Agent Judge Flow

1. Operational agent produces an investigation summary, recommendation, report draft, or proposed tool request.
2. Evidence Support Judge validates claims against approved evidence.
3. Tenant Boundary Judge checks tenant, customer, workspace, subscription, account, environment, and case scope.
4. Knowledge and Memory Scope Judge checks RAG, vector search, shared memory, customer context, case memory, or retrieval scope where used.
5. Hallucination / Unsupported Claim Judge identifies unsupported conclusions.
6. HITL / HOTL Compliance Judge checks whether required review or approval occurred.
7. Agent Judge findings are logged.
8. Findings are passed as context to the governed workflow.
9. PDP makes an authorization decision when authorization is required.
10. PEP enforces the PDP decision and obligations.
11. Human approval workflow handles required review where policy requires it.
12. Tool gateway executes only authorized actions.
13. Audit records preserve the full chain of request, finding, decision, approval, enforcement, and execution.

---

## Relationship to Other AI Assurance Files

This file provides the overview for Agent Judges. More detailed contracts are defined in related files:

| File | Purpose |
|---|---|
| `judge-evaluation-contract.md` | Structured judge input and output contract |
| `evidence-support-judge.md` | Evidence-grounding judge requirements |
| `hallucination-unsupported-claim-judge.md` | Unsupported-claim and hallucination checks |
| `tenant-boundary-judge.md` | Tenant and customer boundary validation |
| `hitl-compliance-judge.md` | Human review and approval validation |
| `output-quality-judge.md` | Output quality and customer-readiness scoring |
| `attack-atlas-mapping-judge.md` | ATT&CK and ATLAS mapping validation |
| `judge-human-review-model.md` | Human review routing and accountability model |
| `judge-limitations.md` | Known limitations and non-authoritative boundaries for Agent Judges |

---

## Reference Architecture Disclaimer

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.
