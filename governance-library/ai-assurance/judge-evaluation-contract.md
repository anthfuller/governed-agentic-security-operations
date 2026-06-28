# Judge Evaluation Contract

## Purpose

This document defines the governed input, output, and audit contract for **Agent Judge** evaluations in the AI assurance layer of the **Governed Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The contract ensures that Agent Judge evaluations are structured, auditable, replayable, tenant-scoped, evidence-grounded, and consistently consumable by downstream workflows.

Agent Judge findings are assurance signals, not authorization decisions. They MAY become policy-relevant inputs to the PDP, but only the PDP produces governed authorization decisions.

---

## Scope

This contract applies to Agent Judge evaluations for:

- Evidence support validation
- Hallucination and unsupported-claim detection
- Tenant and customer boundary validation
- Knowledge store, vector search, shared memory, customer context, case memory, evidence retrieval, and retrieved-context scope validation
- HITL approval validation
- Customer-facing output review
- Forensic output assurance
- ATT&CK / ATLAS mapping validation
- Tool-use request evaluation before enforcement
- Detection engineering review support
- Incident summary and escalation quality checks

This contract applies to governed MSSP, MDR, DFIR, cloud security, SIEM, XDR, and private/local LLM forensic workflows.

---

## When This Contract Is Required

This contract MUST be used for Agent Judge evaluations when the evaluation affects governed decisions, customer-facing output, DFIR conclusions, containment or response recommendations, escalation, closure, governance evidence, legal-sensitive findings, approval workflows, tenant or customer boundaries, identity or access recommendations, tool requests before enforcement, or high-impact operational recommendations.

Exploratory internal analysis MAY use a lighter evaluation format only when the output does not affect governed workflow routing, approval requirements, PDP context, tenant handling, evidence handling, release readiness, or fail-closed behavior.

## Non-Goals

This contract does not define:

- PDP authorization decisions
- PEP enforcement results
- Human approval workflow implementation
- Tool execution logic
- Compliance certification
- A maturity model
- A product-specific implementation guarantee
- An autonomous SOC replacement model

---

## Contract Boundary

Agent Judge evaluations MUST remain separate from policy decisions, enforcement actions, human approvals, tool execution, and audit events.

| Item | Contract Owner | Example Values |
|---|---|---|
| Agent Judge finding | Agent Judge | `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, `NOT_APPLICABLE` |
| PDP decision | PDP | `ALLOW`, `DENY`, `REQUIRE_APPROVAL` |
| PEP enforcement result | PEP | `ENFORCED`, `DENIED`, `FAILED_CLOSED`, `NOT_EXECUTED` |
| Human approval status | Approval workflow | `APPROVED`, `DENIED`, `PENDING`, `EXPIRED`, `REVOKED`, `REQUIRES_MORE_EVIDENCE` |
| Tool execution result | Tool gateway or controlled execution layer | `EXECUTED`, `FAILED`, `BLOCKED`, `NOT_REQUESTED` |
| Audit event | Audit / logging layer | `RECORDED`, `FAILED`, `INTEGRITY_VERIFIED` |

Agent Judge findings MUST NOT be overloaded as PDP decisions, PEP enforcement outcomes, approval states, or tool execution results.

---

## Contract Versioning

Every governed judge evaluation MUST identify the contract used to evaluate and structure the result.

Required identifiers:

| Field | Requirement | Description |
|---|---|---|
| `judge_contract_id` | MUST | Stable identifier for the governed judge contract |
| `judge_contract_version` | MUST | Version of the judge contract |
| `judge_id` | MUST | Identifier for the judge implementation |
| `judge_version` | MUST | Version of the judge logic, prompt, rules, model, or evaluator |
| `evaluation_type` | MUST | Type of evaluation performed |
| `evaluation_scope` | MUST | Scope of the object being evaluated |

Contract changes that alter required fields, finding values, routing semantics, severity handling, evidence requirements, tenant-boundary handling, or audit requirements MUST be versioned and approved.

---

## Governed Finding Vocabulary

For governed workflows, Agent Judges MUST use the governed finding vocabulary unless the contract is explicitly versioned and approved.

| Finding | Meaning |
|---|---|
| `PASS` | The evaluated item met the judge criteria |
| `FAIL` | The evaluated item violated one or more required criteria |
| `NEEDS_REVIEW` | The evaluated item requires human review before use |
| `INSUFFICIENT_EVIDENCE` | The judge could not verify the claim, action, or output with available evidence |
| `NOT_APPLICABLE` | The judge criteria do not apply to the evaluated item |

`PASS` means only that the evaluated item passed that specific assurance check. It does not authorize action, approve release, or execute a tool.

---

## Input Contract Requirements

For governed workflows, Agent Judges MUST receive structured inputs.

At minimum, judge input MUST include applicable fields.

| Field | Requirement | Description |
|---|---|---|
| `judge_request_id` | MUST | Unique identifier for the judge request |
| `judge_contract_id` | MUST | Identifier for the governed judge contract |
| `judge_contract_version` | MUST | Version of the governed judge contract |
| `judge_id` | MUST | Identifier for the judge being invoked |
| `judge_version` | MUST | Version of the judge logic, prompt, rules, model, or evaluator |
| `timestamp_utc` | MUST | Time the judge request was created |
| `agent_id` | MUST | Agent being evaluated |
| `agent_version` | MUST when applicable | Version of the agent being evaluated |
| `agent_session_id` | MUST | Agent session or run identifier |
| `workflow_id` | MUST for governed workflows; SHOULD for exploratory or non-governed analytics | Governed workflow, orchestration, or review flow associated with the evaluation |
| `case_id` | MUST when applicable | Case or incident identifier |
| `tenant_id` | MUST when applicable | Authorized tenant boundary identifier |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Authorized customer boundary identifier |
| `workspace_id` | MUST when applicable | SIEM, XDR, cloud, or logging workspace identifier |
| `subscription_id` | MUST when applicable | Cloud subscription, account, or project identifier |
| `evaluation_type` | MUST | Evidence support, tenant boundary, HITL, hallucination, forensic, output quality, mapping, or tool-use evaluation |
| `evaluation_scope` | MUST | Output, evidence, tool request, customer release, forensic report, approval check, or mapping |
| `tenant_scope` | MUST when applicable | Structured tenant, customer, workspace, subscription, account, and case boundary context |
| `intended_use` | MUST | Analyst-only, customer-facing, containment, forensic, detection engineering, legal-sensitive, or executive communication |
| `risk_level` | MUST when applicable | Risk classification for the evaluated output or action |
| `action_risk_classification_id` | MUST when applicable | Identifier for the action-risk classification applied to the output or requested action |
| `risk_taxonomy_version` | MUST when applicable | Version of the risk taxonomy used for R1-R5 or equivalent risk levels |
| `input_object_ids` | MUST when applicable | Prompt, request, artifact, record, query, or source objects under evaluation |
| `output_object_id` | MUST when applicable | Agent output being evaluated |
| `evidence_object_ids` | MUST when applicable | Evidence objects available to support the evaluation |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences the evaluated output, evidence interpretation, recommendation, mapping, approval context, customer-facing wording, or proposed action | Approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, and retention boundary |
| `policy_context_id` | MUST when policy affects routing, release readiness, approval requirements, PDP context, tenant handling, evidence handling, exception handling, or fail-closed behavior | Relevant policy, baseline, or approval context |
| `policy_obligation_ids` | MUST when applicable | Policy obligations that the evaluation is expected to test |
| `output_destination` | MUST when applicable | Destination for customer-facing, executive, legal-sensitive, ticketing, case-system, or external outputs |
| `data_classification` | MUST when applicable | Sensitivity, legal, customer-regulated, or forensic data classification |
| `sensitivity_label` | MUST when applicable | Sensitivity label or handling label applied to the evaluated input, output, or evidence |
| `exception_id` | MUST when applicable | Approved exception reference when policy permits an exception |
| `exception_expiration_utc` | MUST when an exception is used | Expiration time for the approved exception |
| `requested_action` | MUST when applicable | Proposed action being evaluated before enforcement |
| `tool_contract_id` | MUST when applicable | Governed tool contract associated with a proposed tool request |
| `human_approval_context` | MUST when applicable | Human approval state, reviewer identity, scope, and timestamp metadata |
| `customer_release_context` | MUST when applicable | Customer-facing release review state and required reviewer context |
| `forensic_context` | MUST when applicable | Chain-of-custody, evidence handling, and examiner review context |
| `correlation_ids` | MUST when applicable | Related workflow, audit, PDP, PEP, or tool execution references |

Free-form inputs MUST NOT be used for governed workflows unless wrapped in a structured request object with required metadata.

---

## Required Tenant Scope Object

Where tenant or customer boundaries apply, the input MUST include a structured `tenant_scope` object.

| Field | Requirement | Description |
|---|---|---|
| `tenant_id` | MUST when applicable | Authorized tenant boundary |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Authorized customer boundary |
| `workspace_id` | MUST when applicable | Authorized SIEM, XDR, or logging workspace |
| `subscription_id` | MUST when applicable | Authorized cloud subscription, account, or project |
| `case_id` | MUST when applicable | Authorized case or incident boundary |
| `data_residency_boundary` | MUST when applicable | Data residency, sovereignty, or regulatory boundary |
| `authorized_evidence_sources` | MUST when applicable | Evidence sources allowed for the evaluation |
| `authorized_output_destinations` | MUST when applicable | Allowed output destinations |
| `cross_tenant_access_allowed` | MUST | Boolean indicating whether cross-tenant access is permitted under policy |
| `cross_tenant_justification_id` | MUST when cross-tenant access is allowed | Approved exception, policy, or authorization reference |

If tenant scope is required for a tenant-scoped workflow and is missing, the workflow MUST fail closed. Manual review MAY occur only as a separate remediation or reclassification step before any governed processing, release, or tool execution continues.

---

## Required Evidence Reference Object

Where evidence validation applies, evidence references MUST be structured.

| Field | Requirement | Description |
|---|---|---|
| `evidence_object_id` | MUST | Unique evidence object identifier |
| `evidence_type` | MUST when applicable | Log, alert, artifact, note, report, timeline, query result, packet capture, or other evidence type |
| `evidence_source` | MUST | Source system, evidence store, log source, forensic artifact, or case system |
| `tenant_id` | MUST when applicable | Tenant boundary for the evidence |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Customer boundary for the evidence |
| `case_id` | MUST when applicable | Case or incident association |
| `workspace_id` | MUST when applicable | Workspace, account, project, or subscription boundary for the evidence |
| `collection_time_utc` | MUST when applicable | Evidence collection timestamp |
| `observation_time_utc` | MUST when applicable | Time the observed event occurred |
| `integrity_reference` | MUST when implemented | Hash, signature, immutable log reference, or storage integrity marker |
| `chain_of_custody_id` | MUST for forensic evidence | Chain-of-custody reference |
| `classification` | MUST when applicable | Sensitivity, legal, customer, or data-handling classification |
| `permitted_use` | MUST when applicable | Intended and authorized use of the evidence |

For forensic workflows, chain-of-custody and evidence traceability MUST be preserved.

---

## Required Knowledge Store or Memory Scope Object

Where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences a governed evaluation, the input MUST include a structured `knowledge_store_or_memory_scope` object.

| Field | Requirement | Description |
|---|---|---|
| `scope_id` | MUST | Unique knowledge or memory scope identifier |
| `approved_sources` | MUST | Approved knowledge stores, vector indexes, case memory, customer context stores, evidence retrieval sources, or memory sources |
| `tenant_id` | MUST when tenant-scoped | Authorized tenant boundary for retrieval or memory use |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Authorized customer boundary for retrieval or memory use |
| `case_id` | MUST when case-bound | Authorized case or incident boundary |
| `workspace_id` | MUST when workspace-scoped | Authorized workspace boundary where applicable |
| `evidence_scope` | MUST when evidence retrieval is used | Evidence boundary associated with retrieved context |
| `retention_policy_id` | MUST when retention affects use | Retention boundary governing retrieved or remembered context |
| `cross_customer_reuse_allowed` | MUST | Boolean indicating whether cross-customer reuse is permitted under policy |
| `cross_tenant_reuse_allowed` | MUST | Boolean indicating whether cross-tenant reuse is permitted under policy |
| `cross_case_reuse_allowed` | MUST | Boolean indicating whether cross-case reuse is permitted under policy |
| `authorization_reference` | MUST when reuse or exception is allowed | Approved policy, exception, customer authorization, or governance reference |

If knowledge store or memory scope is required and missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent, the workflow MUST fail closed or route to required review according to workflow risk and policy.

---

## Output Contract Requirements

For governed workflows, Agent Judges MUST produce structured outputs.

At minimum, judge output MUST include applicable fields.

| Field | Requirement | Description |
|---|---|---|
| `judge_result_id` | MUST | Unique judge result identifier |
| `judge_request_id` | MUST | Related judge request identifier |
| `judge_contract_id` | MUST | Identifier for the governed judge contract |
| `judge_contract_version` | MUST | Version of the governed judge contract |
| `judge_id` | MUST | Judge identifier |
| `judge_version` | MUST | Judge implementation version |
| `timestamp_utc` | MUST | Evaluation timestamp |
| `agent_id` | MUST | Agent evaluated |
| `agent_session_id` | MUST | Agent session or run identifier |
| `workflow_id` | MUST for governed workflows; SHOULD for exploratory or non-governed analytics | Governed workflow, orchestration, or review flow associated with the evaluation |
| `case_id` | MUST when applicable | Case or incident identifier |
| `tenant_id` | MUST when applicable | Tenant boundary identifier |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Customer boundary identifier |
| `evaluation_type` | MUST | Type of evaluation performed |
| `evaluation_scope` | MUST | Scope evaluated |
| `intended_use` | MUST when applicable | Analyst-only, customer-facing, containment, forensic, detection engineering, legal-sensitive, or executive communication |
| `output_destination` | MUST when applicable | Destination for customer-facing, executive, legal-sensitive, ticketing, case-system, or external outputs |
| `finding` | MUST | Governed finding value |
| `severity` | MUST when applicable | Severity of the finding |
| `confidence` | MUST when produced | Confidence value or rating |
| `rationale_summary` | MUST | Concise rationale without unsupported claims |
| `failed_checks` | MUST when applicable | Specific checks that failed |
| `passed_checks` | SHOULD when useful | Checks that passed and support replay or review |
| `required_controls_evaluated` | MUST when applicable | Required assurance controls evaluated by the judge |
| `policy_obligation_ids` | MUST when applicable | Policy obligations evaluated or referenced |
| `evidence_object_ids` | MUST when applicable | Evidence objects considered during evaluation |
| `unsupported_claims` | MUST when applicable | Claims not supported by approved evidence |
| `tenant_boundary_result` | MUST when evaluated | Tenant boundary evaluation result |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Result of RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved-context scope validation |
| `evidence_validation_result` | MUST when evaluated | Evidence validation result |
| `hitl_validation_result` | MUST when evaluated | Human approval validation result |
| `approval_record_id` | MUST when approval exists | Specific approval record identifier for audit replay and dispute review |
| `customer_release_review_status` | MUST for customer-facing output | Customer release review state |
| `forensic_validation_result` | MUST for forensic workflows | Forensic evidence and chain-of-custody evaluation result |
| `recommended_route` | MUST when applicable | Review, correction, escalation, block, fail closed, or continue route |
| `correlation_ids` | MUST when applicable | Related workflow, audit, PDP, PEP, or tool execution references |
| `audit_reference_id` | MUST when applicable | Related audit event or record |

Judge outputs MUST be auditable, replayable, and consistently consumable by downstream workflows.

---

## Standard Result Sub-Objects

### `tenant_boundary_result`

When tenant-boundary evaluation is performed, the result MUST be structured.

| Field | Requirement | Description |
|---|---|---|
| `status` | MUST | `PASS`, `FAIL`, `NEEDS_REVIEW`, or `NOT_APPLICABLE` |
| `authorized_scope` | MUST when applicable | Authorized tenant, customer, workspace, subscription, account, or case scope |
| `observed_scope` | MUST when applicable | Scope observed in the evaluated input or output |
| `boundary_violation_detected` | MUST | Boolean boundary violation indicator |
| `cross_tenant_data_detected` | MUST | Boolean cross-tenant indicator |
| `handling_requirement` | MUST when violation is detected | Block, fail closed, or required review route |
| `rationale_summary` | MUST | Concise boundary evaluation rationale |

Cross-tenant data mixing MUST be blocked or fail closed. Escalation alone is insufficient unless data has not been exposed, executed, released, or used in a governed decision.

---

### `knowledge_memory_scope_result`

When knowledge store or memory scope evaluation is performed, the result MUST be structured.

| Field | Requirement | Description |
|---|---|---|
| `status` | MUST | `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE` |
| `scope_id` | MUST when applicable | Knowledge or memory scope identifier evaluated |
| `approved_sources_valid` | MUST when applicable | Whether approved retrieval or memory sources were used |
| `tenant_scope_valid` | MUST when applicable | Whether retrieval or memory remained within tenant scope |
| `customer_scope_valid` | MUST for customer-scoped workflows | Whether retrieval or memory remained within customer scope |
| `case_scope_valid` | MUST when case-bound | Whether retrieval or memory remained within case scope |
| `evidence_scope_valid` | MUST when evidence retrieval is used | Whether retrieved evidence context remained within approved evidence scope |
| `retention_boundary_valid` | MUST when retention affects use | Whether retrieval or memory use complied with retention boundaries |
| `cross_boundary_reuse_detected` | MUST | Whether unauthorized cross-customer, cross-tenant, or cross-case reuse was detected |
| `handling_requirement` | MUST when violation is detected | Block, fail closed, quarantine, or required review route |
| `rationale_summary` | MUST | Concise knowledge and memory scope evaluation rationale |

---

### `evidence_validation_result`

When evidence validation is performed, the result MUST be structured.

| Field | Requirement | Description |
|---|---|---|
| `status` | MUST | `PASS`, `FAIL`, `INSUFFICIENT_EVIDENCE`, `NEEDS_REVIEW`, or `NOT_APPLICABLE` |
| `claims_evaluated` | MUST when applicable | Claims evaluated against evidence |
| `claims_supported` | MUST when applicable | Claims supported by approved evidence |
| `claims_unsupported` | MUST when applicable | Claims not supported by approved evidence |
| `missing_evidence` | MUST when applicable | Required evidence not available |
| `evidence_scope_valid` | MUST when applicable | Whether evidence is scoped to the correct tenant, customer, case, or workspace |
| `evidence_sufficiency` | MUST when applicable | Whether evidence is sufficient for the conclusion or recommendation |
| `rationale_summary` | MUST | Concise evidence evaluation rationale |

Unsupported operational claims MUST prevent execution or release when they affect containment, customer-facing output, forensic conclusions, legal-sensitive output, escalation, closure, or high-impact recommendations unless routed through required approval or review under policy.

---

### `hitl_validation_result`

When human approval is required, the result MUST be structured.

| Field | Requirement | Description |
|---|---|---|
| `status` | MUST | `PASS`, `FAIL`, `NEEDS_REVIEW`, or `NOT_APPLICABLE` |
| `approval_required` | MUST | Whether human approval was required |
| `approval_status` | MUST when approval is required | Approved, denied, pending, expired, revoked, or requires more evidence |
| `reviewer_role` | MUST when approval is required | Required reviewer role |
| `reviewer_identity` | MUST when approval is required | Named reviewer identity |
| `approval_timestamp_utc` | MUST when approval exists | Approval timestamp |
| `approval_scope` | MUST when approval is required | Scope of approval |
| `approval_expiration_utc` | MUST when applicable | Approval expiration timestamp |
| `approval_workflow_id` | MUST when approval is required | Approval workflow reference |
| `approval_record_id` | MUST when approval exists | Specific approval record identifier for replay, audit, and dispute review |
| `action_matches_approval` | MUST when action is evaluated | Whether requested or executed action matches approval scope |
| `rationale_summary` | MUST | Concise HITL validation rationale |

A generic approval flag is insufficient when named accountability is required.

---

### `forensic_validation_result`

When forensic workflows are evaluated, the result MUST be structured.

| Field | Requirement | Description |
|---|---|---|
| `status` | MUST | `PASS`, `FAIL`, `INSUFFICIENT_EVIDENCE`, `NEEDS_REVIEW`, or `NOT_APPLICABLE` |
| `chain_of_custody_valid` | MUST when forensic evidence is used | Whether chain-of-custody metadata is valid |
| `evidence_traceability_valid` | MUST when forensic evidence is used | Whether findings trace to evidence |
| `authorized_evidence_only` | MUST | Whether only approved evidence was used |
| `external_egress_detected` | MUST where offline/private operation is required | Whether unauthorized external egress occurred |
| `examiner_review_status` | MUST when applicable | Examiner review status |
| `legal_review_status` | MUST when applicable | Legal review status |
| `customer_release_review_status` | MUST when applicable | Customer release review status |
| `rationale_summary` | MUST | Concise forensic validation rationale |

Forensic judge findings MUST NOT replace examiner review, legal review, or customer release approval.

---

## Recommended Routing Values

Agent Judge output MAY include `recommended_route`.

For governed workflows, when `recommended_route` is produced, routing values MUST be selected from the governed route vocabulary unless the contract is explicitly versioned and approved.

| Route | Meaning |
|---|---|
| `CONTINUE` | Continue to the next required workflow step |
| `CORRECT_OUTPUT` | Output must be corrected before use |
| `REQUEST_MORE_EVIDENCE` | More evidence is required before use |
| `REQUIRE_HUMAN_REVIEW` | Human review is required |
| `REQUIRE_CUSTOMER_RELEASE_REVIEW` | Customer-facing release review is required |
| `REQUIRE_FORENSIC_REVIEW` | Forensic review is required |
| `REQUIRE_LEGAL_REVIEW` | Legal-sensitive review is required |
| `BLOCK` | Output or action must be blocked |
| `FAIL_CLOSED` | Workflow must fail closed |
| `ESCALATE` | Escalation is required under policy |

`ESCALATE` is not authorization, release approval, tenant-boundary exception, or permission to execute a governed action.

Routing values are handling signals. They are not authorization decisions. They MAY become policy-relevant inputs to the PDP, but only the PDP produces governed authorization decisions.

---

## Finding-to-Handling Requirements

| Finding | Minimum Governed Handling |
|---|---|
| `PASS` | Continue only to the next required control, approval, or workflow step |
| `FAIL` | Block, fail closed, correct, or route to required review based on policy |
| `NEEDS_REVIEW` | Route to required human review before release or action |
| `INSUFFICIENT_EVIDENCE` | Require more evidence or prevent unsupported use |
| `NOT_APPLICABLE` | Continue only if no policy requires that judge result |

A `PASS` finding MUST NOT be interpreted as authorization to execute a governed action.

---

## Policy Integration Requirements

Agent Judge findings MAY be used as PDP input when policy requires assurance context.

The following requirements apply:

- Tenant boundary `FAIL` MUST result in deny, block, or fail-closed handling.
- Knowledge or memory scope `FAIL` MUST result in deny, block, quarantine, fail-closed handling, or required review where retrieved context, RAG, vector search, shared memory, customer context, case memory, evidence retrieval, or knowledge retrieval affects governed output, evidence interpretation, recommendation, approval context, customer-facing wording, or proposed action.
- Cross-tenant data mixing MUST be blocked or fail closed unless a valid pre-approved exception exists and no unauthorized exposure, release, execution, or governed decision use occurred.
- Unsupported containment recommendations MUST NOT execute as validated recommendations. Required review or approval MAY authorize correction, additional evidence collection, limited hypothesis labeling, emergency exception handling, or restricted internal handling under policy, but MUST NOT convert unsupported recommendations into evidence-supported findings.
- Unsupported customer-facing claims MUST be corrected, removed, qualified as hypothesis-only where appropriate, or blocked from release. Customer-release review MAY approve corrected or properly qualified language, but MUST NOT approve unsupported claims as validated facts.
- Forensic conclusions without required evidence traceability or chain-of-custody metadata MUST be blocked from release or operational reliance as validated findings. Forensic, legal, or customer review MAY authorize correction, additional evidence collection, limited hypothesis labeling, documented exception handling, or restricted internal handling under policy, but MUST NOT convert unsupported forensic conclusions into forensic proof.
- HITL validation failure MUST prevent sensitive action execution where approval is required.
- Read-only governed actions, investigations, judge evaluations, and evidence lookups MUST still produce audit records when used in governed workflows.

The PDP decision contract MUST remain separate from the judge evaluation contract.

---

## Audit Requirements

Judge evaluations MUST produce audit records for governed workflows.

Audit records MUST capture applicable fields, including:

- Judge request identifier
- Judge result identifier
- Judge contract identifier and version
- Judge identifier and version
- Agent identifier and session identifier
- Workflow identifier for governed workflows
- Case, tenant, customer, workspace, and subscription context where applicable
- Evaluation type and scope
- Intended use and risk level where applicable
- Input, output, and evidence object references
- Knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences the evaluated output, evidence interpretation, recommendation, mapping, approval context, customer-facing wording, or proposed action
- Policy context and policy obligation identifiers where applicable
- Finding, severity, confidence, and rationale summary
- Failed checks and unsupported claims where applicable
- Tenant boundary result where evaluated
- Evidence validation result where evaluated
- HITL validation result where evaluated
- Forensic validation result where evaluated
- Customer release review status where applicable
- Recommended route
- Related PDP decision reference where applicable
- Related PEP enforcement result where applicable
- Related tool execution result where applicable
- Human reviewer identity where applicable
- Timestamp and audit integrity reference where implemented

Audit records MUST support replay, investigation, escalation review, and continuous improvement.

---

## Failure Handling Requirements

Judge evaluation failures MUST be handled explicitly.

| Failure Condition | Required Handling |
|---|---|
| Required judge unavailable | Fail closed or route to required manual review |
| Required input field missing | Fail closed or route to required manual review |
| Tenant scope missing for tenant-scoped workflow | Fail closed; manual review MAY occur only as a separate remediation or reclassification step before governed processing, release, or tool execution continues |
| Knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influences governed evaluation | Fail closed or route to required review according to workflow risk and policy |
| Evidence unavailable for required evidence validation | Return `INSUFFICIENT_EVIDENCE`, fail closed, or route to required review under policy |
| Judge output malformed | Retry only within configured limits, then fail closed or route to required manual review |
| Judge contract version unsupported | Fail closed or route to required manual review |
| Conflicting judge findings | Route to required human review or higher-priority policy handling |
| Audit logging failure | Fail closed where audit is mandatory |

Retries MUST be bounded by policy or workflow configuration. Retries MUST NOT become uncontrolled loops, bypass audit logging, or delay fail-closed handling where required.

A governed workflow MUST NOT silently ignore a required judge failure.

---

## Example Judge Request

```json
{
  "judge_request_id": "jr-2026-000123",
  "judge_contract_id": "ai-assurance.judge-evaluation-contract",
  "judge_contract_version": "1.0",
  "judge_id": "evidence-support-judge",
  "judge_version": "1.0",
  "timestamp_utc": "2026-05-24T15:20:00Z",
  "agent_id": "soc-investigation-agent",
  "agent_session_id": "session-789",
  "workflow_id": "workflow-customer-report-review-001",
  "case_id": "case-456",
  "tenant_id": "tenant-123",
  "customer_id": "customer-abc",
  "workspace_id": "workspace-def",
  "evaluation_type": "evidence_support",
  "evaluation_scope": "customer_facing_output",
  "intended_use": "customer-facing",
  "risk_level": "R3",
  "output_object_id": "output-111",
  "evidence_object_ids": [
    "evidence-001",
    "evidence-002"
  ],
  "knowledge_store_or_memory_scope": {
    "scope_id": "kscope-customer-abc-case-456",
    "approved_sources": [
      "case-memory-456",
      "customer-abc-knowledge-store"
    ],
    "tenant_id": "tenant-123",
    "customer_id": "customer-abc",
    "case_id": "case-456",
    "retention_policy_id": "retention-policy-001",
    "cross_customer_reuse_allowed": false,
    "cross_tenant_reuse_allowed": false,
    "cross_case_reuse_allowed": false
  },
  "policy_context_id": "policy-context-222",
  "policy_obligation_ids": [
    "obligation-evidence-required",
    "obligation-customer-release-review"
  ],
  "tenant_scope": {
    "tenant_id": "tenant-123",
    "customer_id": "customer-abc",
    "workspace_id": "workspace-def",
    "case_id": "case-456",
    "cross_tenant_access_allowed": false
  }
}
```

---

## Example Judge Result

```json
{
  "judge_result_id": "jres-2026-000123",
  "judge_request_id": "jr-2026-000123",
  "judge_contract_id": "ai-assurance.judge-evaluation-contract",
  "judge_contract_version": "1.0",
  "judge_id": "evidence-support-judge",
  "judge_version": "1.0",
  "timestamp_utc": "2026-05-24T15:20:08Z",
  "agent_id": "soc-investigation-agent",
  "agent_session_id": "session-789",
  "workflow_id": "workflow-customer-report-review-001",
  "case_id": "case-456",
  "tenant_id": "tenant-123",
  "customer_id": "customer-abc",
  "evaluation_type": "evidence_support",
  "evaluation_scope": "customer_facing_output",
  "intended_use": "customer-facing",
  "output_destination": "customer_report_draft",
  "finding": "INSUFFICIENT_EVIDENCE",
  "severity": "HIGH",
  "confidence": 0.91,
  "rationale_summary": "One customer-facing claim was not supported by the approved evidence objects.",
  "failed_checks": [
    "claim_support"
  ],
  "required_controls_evaluated": [
    "evidence_identity",
    "evidence_scope",
    "claim_support",
    "customer_release_review"
  ],
  "policy_obligation_ids": [
    "obligation-evidence-required",
    "obligation-customer-release-review"
  ],
  "evidence_object_ids": [
    "evidence-001",
    "evidence-002"
  ],
  "unsupported_claims": [
    {
      "claim_id": "claim-003",
      "claim_summary": "Unsupported lateral movement conclusion",
      "required_handling": "CORRECT_OUTPUT_OR_REQUEST_MORE_EVIDENCE"
    }
  ],
  "knowledge_memory_scope_result": {
    "status": "PASS",
    "scope_id": "kscope-customer-abc-case-456",
    "approved_sources_valid": true,
    "tenant_scope_valid": true,
    "customer_scope_valid": true,
    "case_scope_valid": true,
    "retention_boundary_valid": true,
    "cross_boundary_reuse_detected": false
  },
  "evidence_validation_result": {
    "status": "INSUFFICIENT_EVIDENCE",
    "claims_evaluated": 7,
    "claims_supported": 6,
    "claims_unsupported": 1,
    "evidence_scope_valid": true,
    "evidence_sufficiency": "insufficient_for_claim_003",
    "rationale_summary": "Approved evidence supports six claims but does not support the lateral movement conclusion."
  },
  "customer_release_review_status": "REQUIRED",
  "recommended_route": "REQUEST_MORE_EVIDENCE",
  "audit_reference_id": "audit-999"
}
```

---

## Anti-Patterns

The following patterns are not acceptable for governed workflows:

- Using free-form judge results where structured output is required
- Treating judge `PASS` as authorization to execute a governed tool
- Treating judge findings as PDP decisions
- Treating unsupported claims as acceptable because the output sounds plausible
- Allowing tenant-boundary failures to proceed after exposure with escalation only
- Ignoring RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved-context scope in governed judge evaluations
- Releasing customer-facing output without required review
- Executing containment actions with unsupported evidence
- Treating local/private LLM forensic summaries as forensic proof without chain-of-custody support
- Skipping audit records for read-only investigations or evidence lookups
- Retrying malformed judge output without bounded retry limits
- Changing judge contract semantics without versioning and approval

---

## Relationship to Other AI Assurance Files

| File | Purpose |
|---|---|
| `agent-judges-overview.md` | Defines the role and boundaries of Agent Judges |
| `evidence-support-judge.md` | Defines evidence-grounding requirements |
| `hallucination-unsupported-claim-judge.md` | Defines unsupported-claim and hallucination checks |
| `tenant-boundary-judge.md` | Defines tenant and customer boundary validation |
| `hitl-compliance-judge.md` | Defines human review and approval validation |

---

## Reference Architecture Disclaimer

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.
