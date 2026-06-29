# AI Assurance

## Purpose

This directory defines the **AI Assurance & Analytics Layer** for the **Governed Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The purpose of this layer is to evaluate whether agent-assisted security operations are evidence-grounded, tenant-safe, auditable, policy-aware, and suitable for human-supervised operational use. It supports managed SOC, MSSP, MDR, cloud incident response, detection engineering, threat hunting, and private/local LLM-assisted DFIR workflows.

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

AI assurance is **not** an enforcement layer. It does not replace the PEP, PDP, human approval workflow, customer authorization process, incident commander, forensic examiner, or analyst accountable for final operational judgment.

---

## Scope

This directory covers assurance patterns for evaluating agentic security operations, including:

- Agent Judge operating boundaries
- Structured judge evaluation contracts
- Evidence support and grounding validation
- Hallucination and unsupported-claim detection
- Tenant, customer, workspace, subscription, account, and case-boundary checks
- Human-in-the-loop and human-on-the-loop compliance checks
- ATT&CK / ATLAS mapping validation
- Output quality scoring and release-readiness checks
- Sensitive-data leakage and data-isolation review patterns
- Model, prompt, and agent-behavior analytics
- Anomaly detection, clustering, and prioritization as decision-support analytics
- Private/local LLM forensic assurance
- Assurance telemetry for audit, replay, escalation review, and continuous improvement

These patterns apply to workflows involving SIEM, XDR, EDR, cloud telemetry, SaaS telemetry, identity telemetry, case data, evidence stores, vector indexes, knowledge stores, forensic artifacts, and analyst-facing recommendations.

---

## Out of Scope

This directory does not define:

- PEP/PDP authorization or enforcement logic
- Agent registration, lifecycle, ownership, or identity governance
- Product-specific deployment instructions
- Compliance certification or maturity scoring
- A replacement for analyst judgment, incident command, customer approval, or forensic review
- Autonomous SOC operation without human accountability
- A bypass path around governed approval or customer authorization

Where those topics are required, this directory should reference the appropriate governance, policy-enforcement, identity, human-oversight, or forensic workflow file instead of duplicating deep controls.

---

## Architectural Position

The AI Assurance & Analytics Layer evaluates operational agent activity before agent outputs, recommendations, mappings, or action requests are trusted for governed use.

Conceptually, this layer sits between:

- The **Agentic SOC / Orchestration Layer**, where operational agents reason, retrieve, correlate, recommend, and request action.
- The **Governance / Control Plane**, where policy enforcement, approval gates, audit logging, replay, and fail-closed behavior are governed.
- The **Agent Governance & Identity Control Plane**, where agent registry, lifecycle, ownership, authentication, authorization, and trust are managed.

AI assurance may consume identity, registration, ownership, policy, tenant, and case metadata, but it does not own those control planes.

Agent registry and agent identity capabilities belong in the **Agent Governance & Identity Control Plane**, not in the operational SOC agent layer. AI assurance may evaluate signals associated with registered or identity-governed agents, but it must not treat identity registration as proof that an output is correct, safe, evidence-supported, or approved for release. AI assurance may evaluate signals associated with registered agents or identity-governed agents, but it MUST NOT treat identity registration as proof that an output is correct, safe, evidence-supported, or approved for release.

---

## Core Boundary

AI assurance evaluates. It does not authorize or execute.

| Function | Responsible Layer or Component |
|---|---|
| Evaluate grounding, evidence support, tenant safety, HITL compliance, output quality, or mapping validity | AI Assurance & Analytics Layer |
| Make governed authorization decisions | PDP |
| Enforce authorization decisions and obligations | PEP |
| Approve sensitive action, containment, reporting, or customer-facing release | Human approval workflow |
| Execute governed tool actions | Tool gateway or controlled execution layer |
| Manage agent identity, registration, lifecycle, and ownership | Agent Governance & Identity Control Plane |
| Preserve audit, replay, and traceability records | Audit, logging, evidence, and governance stores |

Agent Judges MUST NOT make enforcement decisions. If a component is implemented as an authorized PDP function, it MUST be governed, registered, evaluated, and audited as a PDP, not as an Agent Judge.

---

## Decision and Event Separation

Governed workflows MUST preserve separation between assurance findings, policy decisions, enforcement results, human approvals, tool execution, and audit records.

| Item | Meaning | Owner |
|---|---|---|
| Assurance finding | Evaluation result about evidence support, tenant safety, grounding, output quality, HITL status, or mapping validity | AI assurance component |
| PDP decision | Governed authorization outcome such as `ALLOW`, `DENY`, or `REQUIRE_APPROVAL` | PDP |
| PEP enforcement result | Record of whether the PDP decision and obligations were enforced, denied, or failed closed | PEP |
| Human approval status | Record of whether required review was approved, denied, expired, revoked, pending, or required more evidence | Human approval workflow |
| Tool execution result | Result of a governed action after policy and approval controls were satisfied | Tool gateway or controlled execution layer |
| Audit event | Immutable or tamper-evident record of the request, evaluation, decision, approval, enforcement, or execution | Audit / logging layer |

Assurance findings may inform PDP context, approval routing, analyst review, escalation, or release readiness. They MUST NOT be treated as standalone permission to execute, release, suppress, delete, contain, isolate, notify, or close.

---

## Assurance Inputs and Outputs

AI assurance components should operate on structured context rather than unbounded free-text wherever possible.

### Baseline Inputs

| Input | Requirement | Purpose |
|---|---|---|
| `agent_id` | MUST | Identifies the agent being evaluated |
| `agent_session_id` or `run_id` | MUST | Supports replay and investigation |
| `tenant_id` / `customer_id` | MUST where tenant- or customer-scoped | Prevents cross-tenant or cross-customer contamination |
| `case_id` / `incident_id` | MUST when case- or incident-bound | Links findings to the operational record |
| `workflow_id` | SHOULD | Identifies the governed workflow or playbook |
| `input_reference_ids` | MUST when available | References prompts, requests, evidence, artifacts, queries, or context objects |
| `output_reference_id` | MUST when evaluating an output | Identifies the evaluated output |
| `evidence_object_ids` | MUST when claims depend on evidence | Supports evidence validation and traceability |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, or knowledge retrieval is used | Supports validation of retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, and retention boundaries |
| `policy_context_id` | SHOULD when policy affects handling | Links assurance findings to applicable baseline or policy context |
| `approval_workflow_id` | MUST when approval is required | Supports HITL/HOTL validation |
| `target_audience` | SHOULD | Distinguishes analyst-only, customer-facing, executive, legal-sensitive, or operational output |
| `intended_action` | MUST when action is requested | Allows action-risk and approval checks |

### Baseline Outputs

| Output | Requirement | Purpose |
|---|---|---|
| `assurance_event_id` | MUST | Unique assurance event identifier |
| `finding` | MUST | `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE` |
| `severity` | MUST when applicable | Indicates operational impact |
| `confidence` | SHOULD when produced | Indicates evaluation confidence |
| `evidence_validation_result` | MUST when evidence is evaluated | Shows whether claims are supported |
| `tenant_boundary_result` | MUST when tenant scope is evaluated | Shows whether scope remained valid |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Shows whether RAG, vector search, shared memory, customer context, case memory, or knowledge retrieval remained within approved scope |
| `hitl_result` | MUST when approval is required | Shows whether human review requirements were met |
| `unsupported_claims` | SHOULD when detected | Identifies claims requiring removal, evidence, or review |
| `recommended_route` | MUST when follow-up is required | Routes to analyst review, approval, escalation, rejection, or more evidence |
| `audit_reference_id` | MUST | Links the finding to audit records |
| `decision_reference_id` | MUST when consumed by PDP | Links assurance context to authorization decision |

---

## Core Assurance Capabilities

### Agent Judges

Agent Judges evaluate agent outputs against defined criteria such as evidence support, grounding, tenant safety, policy alignment, HITL compliance, output quality, and release readiness.

Agent Judge outputs MUST be structured, auditable, and replayable when used in governed workflows. Judge outputs may influence routing or PDP context, but MUST NOT independently authorize an action.

---

### Evidence Validation

Evidence validation checks whether agent claims are supported by approved evidence objects, case records, telemetry references, or forensic artifacts.

Evidence validation should verify evidence identity, source, tenant or customer scope, case association, timestamp relevance, chain-of-custody metadata where applicable, and whether the cited evidence actually supports the claim being made.

Unsupported operational claims MUST be routed for review, rejected, or blocked from customer-facing release according to policy.

---

### Hallucination and Unsupported-Claim Checks

Unsupported-claim checks evaluate whether an agent introduced facts, entities, timelines, root-cause statements, remediation claims, incident conclusions, attribution statements, or forensic findings that are not supported by approved evidence.

These checks are required for high-risk outputs such as customer reports, DFIR findings, containment recommendations, legal-sensitive matters, executive summaries, detection conclusions, and threat attribution statements.

---

### Tenant Boundary Checks

Tenant boundary checks verify that inputs, outputs, queries, evidence, recommendations, and tool requests remain within the authorized customer, tenant, workspace, subscription, account, or case boundary.

Tenant boundary failures MUST be treated as high-severity assurance failures. Cross-tenant data exposure, cross-customer evidence mixing, or ambiguous tenant attribution MUST be blocked, denied, or failed closed where the workflow could release, execute, or persist governed output.

### Knowledge and Memory Scope Checks

Knowledge and memory scope checks verify that RAG, vector search, shared memory, customer context, case memory, and knowledge retrieval remain within approved tenant, customer, case, workspace, evidence, and retention boundaries.

AI assurance MUST flag missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent knowledge store or memory scope when retrieved context influences agent output, recommendations, assurance findings, customer-facing reporting, DFIR conclusions, or policy-gated requests.

Knowledge and memory scope findings may inform analyst review, quarantine, PDP context, approval routing, or fail-closed handling. They MUST NOT be treated as standalone authorization to retrieve, persist, release, or reuse context.

---

### HITL / HOTL Compliance Checks

Human oversight checks verify that required review occurred before sensitive actions, customer-facing output, containment recommendations, forensic conclusions, or policy-enforced tool execution.

Where approval is required, the assurance check MUST validate reviewer role, reviewer identity, approval status, timestamp, approval scope, expiration or revocation state, and whether the approved action matches the requested or executed action.

A generic approval flag is not sufficient for actions requiring named accountability.

---

### ATT&CK / ATLAS Mapping Validation

Mapping validation checks whether detections, investigation findings, agent outputs, and AI-specific risks are mapped appropriately to supported frameworks.

Mappings are analytical context. They are not proof of compliance, production readiness, detection coverage, or operational correctness.

Mapping validation should verify that the mapping is evidence-supported, confidence is stated where appropriate, unsupported mappings are flagged, and AI-specific risks are not forced into unrelated cybersecurity categories.

---

### Output Quality and Release Readiness

Output quality checks evaluate whether an agent response is accurate, complete, relevant, concise, appropriately scoped, evidence-grounded, and suitable for the intended audience.

Release-readiness checks are especially important for customer-facing reporting, DFIR summaries, executive updates, legal-sensitive findings, and operational recommendations.

Output quality scores MUST NOT replace authorization, evidence validation, customer approval, or reviewer accountability.

---

### Analytics and Model Behavior Monitoring

AI assurance may include analytics such as anomaly detection, clustering, prioritization, model behavior monitoring, prompt-pattern analysis, and agent-output trend analysis.

These analytics provide decision support and continuous-improvement signals. They MUST NOT be treated as autonomous enforcement, containment, legal, or customer-release decisions unless routed through governed PDP/PEP and approval processes.

---

### Private / Local LLM Forensic Assurance

Private or local LLM-assisted DFIR workflows require additional assurance because they may involve disk artifacts, memory artifacts, malware outputs, packet captures, chain-of-custody evidence, legal-sensitive records, regulated customer data, or sovereignty-sensitive material.

Forensic assurance MUST preserve evidence traceability, tenant scope, chain-of-custody expectations where applicable, reviewer accountability, and auditability.

Where offline or no-egress forensic processing is required, assurance checks MUST validate that the workflow did not rely on unauthorized external data movement or unapproved model/tool access.

---

## Minimum Assurance Requirements

AI assurance implementations in this architecture MUST satisfy the following minimum expectations:

| Control Area | Minimum Requirement |
|---|---|
| Grounding | Operational claims that influence investigation, escalation, containment, reporting, customer-facing output, or DFIR conclusions MUST include evidence references |
| Tenant safety | Cross-tenant or cross-customer data mixing MUST be blocked, denied, or failed closed before exposure, release, or execution |
| Knowledge and memory scope | RAG, vector search, shared memory, customer context, case memory, and knowledge retrieval MUST remain within approved tenant, customer, case, evidence, and retention boundaries where used |
| Human oversight | Sensitive, containment, customer-facing, forensic, legal-sensitive, or high-impact outcomes MUST require appropriate human review |
| Evidence integrity | Evidence references MUST be traceable to the applicable case, tenant, customer, workspace, artifact, or source system |
| Tool use | AI assurance components MUST NOT bypass PEP/PDP-controlled tool access |
| Output handling | Customer-facing outputs MUST be reviewed where policy, customer obligation, case sensitivity, or risk classification requires review |
| Forensics | Forensic outputs MUST preserve chain-of-custody expectations, evidence traceability, and reviewer accountability |
| Audit | Assurance inputs, findings, scores, exceptions, reviewer actions, and downstream routing MUST be logged |
| Replay | Material evaluations MUST be reconstructable from logs, referenced evidence, and stored outputs where required |
| Exceptions | Exceptions MUST be explicit, justified, time-bound where applicable, approved where required, and auditable |

---

## Failure Handling

Assurance failures MUST be handled according to the risk of the workflow and the downstream impact.

| Failure Condition | Required Handling |
|---|---|
| Missing tenant or customer context for a governed workflow | Fail closed or route to authorized review before action or release |
| Evidence reference missing for an operational claim | Require evidence, revise output, or route to analyst review |
| Evidence does not support the claim | Block customer-facing release or require correction and review |
| Cross-tenant or cross-customer mismatch | Deny, quarantine, or fail closed according to policy |
| Knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent | Deny, quarantine, fail closed, or route to authorized review according to workflow risk and policy |
| Required human approval missing, expired, revoked, or out of scope | Do not execute or release; route to approval workflow |
| Agent Judge unavailable for a required check | Fail closed or require manual review according to workflow risk |
| Mapping unsupported or low confidence | Flag for analyst review; do not present as validated finding |
| Forensic evidence lineage incomplete | Require forensic reviewer validation before release or action |

Escalation alone is not sufficient when an unsafe output, cross-tenant exposure, unauthorized action, or customer-facing release could occur.

---

## Directory Contents

| File | Purpose |
|---|---|
| `agent-judges-overview.md` | Defines the role, limits, and operating model for Agent Judges |
| `judge-evaluation-contract.md` | Defines structured judge inputs, outputs, findings, evidence references, and routing signals |
| `evidence-support-judge.md` | Defines how operational claims are checked against approved evidence |
| `unsupported-claim-judge.md` | Defines checks for unsupported conclusions, fabricated details, overclaims, unsupported impact statements, and evidence gaps |
| `tenant-boundary-judge.md` | Defines checks for tenant, customer, workspace, subscription, account, and case boundaries |
| `hitl-requirement-check.md` | Defines checks for required human review, approval scope, reviewer identity, approval evidence, and escalation routing |
| `output-quality-judge.md` | Defines output-quality and release-readiness checks |
| `attack-atlas-mapping-judge.md` | Defines ATT&CK / ATLAS mapping validation boundaries |
| `judge-human-review-model.md` | Defines when assurance findings require human review or escalation |
| `judge-limitations.md` | Defines known limitations, non-goals, and prohibited uses of Agent Judges |
| `fleet-update-evaluation-and-safety-validation.md` | Defines safety validation for fleet updates before rollout, rollback, recall, or broad release |

Additional files may define sensitive-data leakage checks, model evaluation telemetry, forensic assurance, analytics monitoring, and assurance-event schemas where needed.

---

## Recommended Reading Path

1. Start with this README to understand the AI Assurance & Analytics Layer.
2. Read `agent-judges-overview.md` to understand the assurance-versus-enforcement boundary.
3. Read `judge-evaluation-contract.md` before implementing or evaluating any judge output.
4. Read the specific judge file for the risk being evaluated, such as evidence support, unsupported claims, tenant boundary, HITL compliance, output quality, or mapping validation.
5. Use governance, policy-enforcement, human-oversight, and agent-governance files for enforcement, approval, identity, lifecycle, and ownership details.

---

## Acceptance Criteria

This directory is aligned to the governed Agentic MSSP / MDR / DFIR architecture when:

- AI assurance evaluates agent activity without becoming an enforcement bypass.
- Agent Judge findings are structured, auditable, and separated from PDP decisions.
- Evidence, tenant, case, policy, approval, and output references are preserved where applicable.
- Knowledge store or memory scope is captured and evaluated when RAG, vector search, shared memory, customer context, case memory, or knowledge retrieval influences governed outputs, recommendations, assurance findings, or policy-gated requests.
- Customer-facing, forensic, containment, legal-sensitive, and high-impact outputs require appropriate review.
- Assurance failures route to denial, fail-closed handling, correction, escalation, or review based on policy and risk.
- F7-LAS is used only as a supporting control lens.
- No file claims autonomous SOC replacement, compliance certification, product implementation maturity, or unsupported production readiness.

---

## Operational Anti-Patterns

Avoid the following patterns:

- Treating an Agent Judge `PASS` as authorization to execute or release output
- Allowing assurance components to call governed tools directly
- Using output quality scores as a substitute for evidence validation
- Reducing human approval to a generic Boolean flag for sensitive actions
- Treating framework mappings as proof of detection coverage or compliance
- Allowing customer-facing DFIR reports to include unsupported conclusions
- Treating agent identity registration as proof of output correctness
- Escalating cross-tenant contamination after exposure instead of blocking or failing closed before exposure
- Duplicating PEP/PDP, agent lifecycle, identity, or approval controls inside AI assurance files

---
