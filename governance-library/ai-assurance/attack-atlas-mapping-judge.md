# ATT&CK / ATLAS Mapping Judge

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

## Purpose

The ATT&CK / ATLAS Mapping Judge is an AI assurance control used to review whether agent-generated mappings to MITRE ATT&CK, MITRE ATLAS, or related threat-model context are evidence-supported, correctly scoped, and clearly qualified.

This judge exists to reduce unsupported technique mapping, threat overstatement, framework misuse, and customer-facing claims that are not backed by investigation evidence.

The ATT&CK / ATLAS Mapping Judge is an assurance component. It is not a policy decision point, enforcement engine, approval authority, or incident commander.

## Scope

This file applies to AI-assisted SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR workflows where an agent, analyst assistant, report drafting assistant, or investigation workflow proposes mappings such as:

- ATT&CK tactic, technique, or procedure references.
- ATLAS tactic, technique, or AI-specific adversary behavior references.
- Attack-path or kill-chain style summaries.
- Threat-model annotations used in analyst notes, incident summaries, customer-facing outputs, or governance reporting.
- AI-system abuse mappings involving prompt injection, tool misuse, data exfiltration, unsafe delegation, model manipulation, or agentic workflow abuse.

This file does not define the full threat model, residual-risk register, PEP/PDP policy contract, approval workflow, or incident-response playbook. Those details belong in the appropriate `threat-model/`, `policy-enforcement/`, `human-oversight/`, and `workflows/` files.

## Role in the Governed Architecture

The ATT&CK / ATLAS Mapping Judge operates in the AI Assurance & Analytics Layer. It reviews mapping quality before mapped findings are used in investigation conclusions, escalation narratives, customer-facing reports, governance evidence, or operational decision support.

It supports the governed Agentic MSSP / MDR / DFIR architecture by enforcing the following assurance expectations:

- Agent-generated mappings MUST be tied to evidence references.
- Framework mappings MUST remain scoped to the observed behavior or documented hypothesis.
- Mapping confidence MUST be represented accurately.
- Unsupported mappings MUST be flagged before they influence operational or customer-facing decisions.
- Agent Judges MUST remain separate from Agents, PEP/PDP, Human Approval, Tool Execution, Evidence, and Audit components.


## When This Judge Is Required

At minimum, the ATT&CK / ATLAS Mapping Judge MUST be applied when a framework mapping affects governed decisions, customer-facing output, DFIR conclusions, containment or response recommendations, incident escalation or closure, threat attribution statements, governance evidence, tenant or customer boundaries, or operational findings used by analysts or customers.

| Workflow Condition | Minimum Handling |
|---|---|
| Customer-facing output includes ATT&CK, ATLAS, attack-path, kill-chain, or AI-abuse mapping | MUST evaluate evidence support, scope, confidence language, unsupported claims, output wording, and release readiness |
| DFIR timeline, forensic summary, or report draft includes framework mapping | MUST evaluate evidence traceability, chain-of-custody context where applicable, unsupported conclusions, and reviewer requirements |
| Containment, eradication, recovery, or response recommendation references a mapping | MUST evaluate evidence support, tenant scope, operational impact, approval context, and confidence level |
| Threat actor attribution, campaign association, or adversary-behavior claim references a mapping | MUST evaluate evidence support, confidence, analyst validation requirements, and overstatement risk |
| Cross-tenant, multi-customer, or aggregated security finding includes mapping | MUST evaluate tenant, customer, workspace, subscription, account, case, and aggregation-governance boundaries |
| Tool request, escalation, closure, or governed workflow step depends on mapping context | MUST evaluate risk context, evidence support, tenant scope, policy context, and downstream handling before PDP/PEP use |
| ATT&CK or ATLAS mapping is used in governance evidence, reporting, or assurance analytics | MUST evaluate framework fit, evidence support, scope limits, confidence, and whether the mapping is being misused as compliance proof |

Exploratory internal notes MAY use preliminary mapping language, but the output MUST be labeled as exploratory and MUST NOT influence governed decisions, customer-facing content, DFIR conclusions, escalation, closure, or response recommendations until required mapping assurance is completed.

## Control Boundary

The control boundary enforced by this judge is mapping assurance.

The judge evaluates whether a proposed ATT&CK or ATLAS mapping is sufficiently supported for its intended use. It does not authorize tool execution, approve containment, declare attribution, assign incident severity, or release content to a customer.

Mandatory control boundaries:

- The judge MUST NOT make enforcement decisions.
- The judge MUST NOT approve or execute response actions.
- The judge MUST NOT replace analyst validation.
- The judge MUST NOT treat framework alignment as proof of compromise, attribution, regulatory compliance, or production maturity.
- The judge MUST distinguish observed evidence from inferred behavior.
- The judge MUST identify unsupported, overbroad, stale, ambiguous, or misapplied mappings.
- The judge MUST route sensitive or customer-facing mapping disputes to human review.

## Required Inputs

A mapping review request MUST include enough context for the judge to evaluate evidence support and scope.

Required inputs where applicable:

| Input | Requirement |
|---|---|
| `case_id` | MUST be included when the mapping is tied to an investigation, incident, DFIR matter, or customer deliverable. |
| `tenant_id` or tenant boundary reference | MUST be included for MSSP, MDR, or multi-tenant workflows. |
| `customer_id` or equivalent customer boundary reference | MUST be included for MSSP, MDR, DFIR, customer-facing, or customer-scoped workflows. |
| `agent_id` | MUST identify the agent or workflow that proposed the mapping. |
| `mapping_request_id` | MUST uniquely identify the mapping review request. |
| `framework_name` | MUST identify the framework being used, such as ATT&CK or ATLAS. |
| `framework_version` or reference date | MUST be included when the implementation maintains versioned framework references or when the mapping affects customer-facing reporting, DFIR conclusions, governance evidence, escalation, closure, or response recommendations. |
| `proposed_tactic` | MUST be included when the mapping uses a tactic-level claim that affects operational findings, escalation, closure, DFIR conclusions, governance evidence, or customer-facing output. |
| `proposed_technique` | MUST be included when the mapping uses a technique-level claim that affects operational findings, escalation, closure, DFIR conclusions, governance evidence, or customer-facing output. |
| `mapping_rationale` | MUST explain why the mapping was proposed. |
| `evidence_object_ids` | MUST reference the evidence used to support the mapping. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST be included when evidence is used in a multi-tenant, multi-customer, MSSP, MDR, DFIR, or customer-scoped workflow. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, mapping catalog retrieval, or retrieved framework context is used to support the mapping. |
| `evidence_summary` | SHOULD summarize the relevant evidence without replacing the evidence reference; it MUST NOT be treated as a substitute for evidence object references. |
| `confidence_level` | MUST describe the proposed confidence level when the output may influence investigation, escalation, or customer-facing reporting. |
| `intended_output_destination` | MUST identify whether the mapping is for analyst notes, internal triage, escalation, customer-facing report, governance evidence, or response planning. |

The judge MUST fail the review when the request does not include enough evidence context to evaluate the mapping safely.

## Evaluation Requirements

### Evidence Support

The judge MUST verify that each proposed mapping is supported by cited evidence.

The judge MUST flag a mapping when:

- The evidence does not show the behavior claimed by the mapping.
- The mapping relies only on model inference without evidence.
- The mapping uses general security language instead of observed behavior.
- The evidence references are missing, inaccessible, unrelated, or tenant-mismatched.
- The mapping depends on assumptions that are not labeled as hypotheses.

Evidence support MAY be partial, but partial support MUST be labeled clearly and MUST NOT be presented as confirmed behavior.

### Framework Boundary

The judge MUST verify that the proposed mapping uses the correct framework boundary.

Examples:

- ATT&CK SHOULD be used for adversary behavior, enterprise intrusion activity, cloud techniques, endpoint activity, identity abuse, persistence, lateral movement, exfiltration, and related operational threat activity.
- ATLAS SHOULD be used when the mapped behavior involves AI-system attack patterns, ML/LLM abuse, model manipulation, prompt injection, malicious tool use, data poisoning, unsafe agent delegation, or AI-specific adversarial behavior.
- A mapping MUST NOT be forced into ATT&CK or ATLAS when the evidence only supports a general control weakness, governance gap, or architectural risk.

The judge MUST flag mappings that confuse AI governance risks with confirmed adversary behavior.

### Specificity and Precision

The judge SHOULD prefer the narrowest defensible mapping supported by the evidence.

The judge MUST flag mappings that are:

- Too broad for the evidence.
- More specific than the evidence supports.
- Based only on keyword similarity.
- Duplicative across multiple techniques without clear behavioral distinction.
- Used to imply a full attack chain when only a single behavior was observed.

When the evidence only supports a tactic-level observation, the judge MUST NOT allow the output to present a technique-level mapping as confirmed.

### Confidence Handling

The judge MUST require confidence to match the strength of the evidence.

Suggested confidence handling:

| Confidence | Use |
|---|---|
| `confirmed` | Evidence directly supports the mapped behavior. |
| `probable` | Multiple evidence points support the mapping, but some uncertainty remains. |
| `possible` | Evidence suggests the mapping, but additional validation is required. |
| `unsupported` | Evidence does not support the mapping. |
| `not_applicable` | The framework does not fit the observed behavior or use case. |

The judge MUST flag any output that presents a possible or unsupported mapping as confirmed.

### Tenant and Evidence Boundary

The judge MUST validate that mappings are constrained to the correct customer, tenant, environment, case, or evidence boundary.

The judge MUST fail the review when:

- Evidence from one tenant is used to support a mapping for another tenant.
- Evidence from a lab, sample, synthetic dataset, or unrelated environment is presented as customer evidence.
- A mapping is generalized across customers without explicit aggregation governance.
- Evidence cannot be traced back to the investigation context.

### Knowledge and Memory Scope Boundary

The judge MUST validate knowledge store or memory scope when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, mapping catalog retrieval, or retrieved framework context influences the proposed mapping, mapping rationale, evidence summary, confidence level, or customer-facing wording.

The judge MUST flag missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent knowledge store or memory scope.

Knowledge and memory scope findings may inform analyst review, quarantine, PDP context, approval routing, or fail-closed handling. They MUST NOT be treated as standalone authorization to retrieve, persist, release, or reuse context.

### Output Destination Risk

The judge MUST apply stricter review for outputs that influence customer-facing reports, escalation, containment recommendations, executive summaries, insurance/legal support, or DFIR conclusions.

Customer-facing or DFIR-impacting mappings MUST be evidence-supported, qualified, and human-reviewed when they influence conclusions, recommendations, or response decisions.

## Judge Outputs

The judge MUST produce an assurance result, not an enforcement decision.

Agent Judge findings MUST remain separate from PDP decisions, PEP enforcement results, approval states, and tool execution results.

The governed judge finding MUST use the standard Agent Judge finding vocabulary:

| Finding | Meaning |
|---|---|
| `PASS` | Mapping is adequately supported for the stated destination and confidence level. |
| `FAIL` | Mapping violates required evidence, scope, tenant, framework, confidence, or review criteria. |
| `NEEDS_REVIEW` | Human validation is required before the mapping may influence operational, DFIR, customer-facing, governance, escalation, closure, or response output. |
| `INSUFFICIENT_EVIDENCE` | Evidence does not sufficiently support the proposed mapping or confidence level. |
| `NOT_APPLICABLE` | ATT&CK, ATLAS, or the stated framework does not apply to the observed behavior or use case. |

Specialized mapping review details MAY be recorded in a separate `mapping_review_status` field. These statuses are handling details, not PDP decisions.

| Mapping Review Status | Meaning |
|---|---|
| `SUPPORTED` | Mapping is supported for the stated scope, destination, and confidence level. |
| `SUPPORTED_WITH_LIMITATIONS` | Mapping may be used only with stated qualifications, scope limits, or confidence language. |
| `NEEDS_REVISION` | Mapping may be reasonable but requires narrower scope, better evidence references, corrected wording, or clearer confidence language. |
| `UNSUPPORTED_MAPPING` | Mapping is not supported by the provided evidence. |
| `OUT_OF_SCOPE` | Mapping does not belong in ATT&CK, ATLAS, or the stated framework context. |
| `REQUIRES_HUMAN_REVIEW` | Human validation is required before operational or customer-facing use. |

The judge output MUST include:

- `mapping_request_id`
- `finding`
- `mapping_review_status`
- `review_summary`
- `supported_mappings`
- `unsupported_mappings`
- `required_revisions`
- `evidence_gaps`
- `confidence_assessment`
- `tenant_boundary_result`
- `evidence_validation_result`
- `knowledge_memory_scope_result` when knowledge store or memory scope is evaluated
- `human_review_required`
- `policy_context_id` when policy affects routing, release readiness, approval requirements, PDP context, tenant handling, evidence handling, or fail-closed behavior
- `audit_event_id` or audit correlation reference

The judge MUST NOT output `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`. If a component is implemented as an authorized PDP function, it MUST be governed, registered, evaluated, and audited as a PDP, not as this Agent Judge.

## Human Review Requirements

Human review MUST be required when the proposed mapping:

- Influences customer-facing reporting.
- Influences DFIR conclusions.
- Influences containment, eradication, recovery, or escalation recommendations.
- Supports suspected threat actor attribution.
- Supports legal, regulatory, insurance, or contractual reporting.
- Conflicts with analyst findings or prior validated evidence.
- Uses low-confidence or incomplete evidence for a high-impact conclusion.
- Involves cross-tenant, multi-customer, or aggregated findings.
- Identifies AI-system compromise, agent misuse, unsafe tool execution, or model manipulation as a confirmed event.

When human review is required, human reviewers MUST validate both the mapping and the wording used to describe it before the mapping influences operational, DFIR, customer-facing, governance, escalation, closure, or response output.

## Audit Requirements

Every mapping review MUST be auditable.

The audit record MUST include:

- Mapping review request identifier.
- Agent or workflow that proposed the mapping.
- Judge component identity and version where available.
- Case, tenant, customer, environment, or evidence boundary.
- Proposed framework, tactic, technique, and rationale.
- Evidence object references used by the judge.
- Evidence tenant attribution or equivalent tenant-boundary metadata where applicable.
- Knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, mapping catalog retrieval, or retrieved framework context is used.
- Judge status and confidence assessment.
- Required revisions or evidence gaps.
- Human review requirement and reviewer outcome where applicable.
- Timestamp and correlation identifier.
- Downstream destination of the reviewed mapping.

Audit logs MUST preserve the difference between proposed mappings, judge findings, analyst decisions, and final published content.

## Framework Reference Management

Framework references can change over time. For governed workflows, the mapping review process MUST preserve the framework reference set, version, retrieval date, or approved internal catalog reference used during the evaluation when that context affects customer-facing output, DFIR conclusions, governance evidence, escalation, closure, response recommendations, or audit replay.

If the judge uses a model, prompt, retrieval index, or mapping catalog to evaluate ATT&CK / ATLAS mappings:

- Judge prompts MUST be versioned.
- Mapping catalogs or framework reference sources MUST be traceable where used.
- Model, provider, prompt, or retrieval-index changes MUST trigger regression testing where the change can affect governed assurance findings, approval routing, PDP context, release readiness, tenant handling, evidence validation, or fail-closed behavior.
- Test examples SHOULD include supported mappings, unsupported mappings, ambiguous mappings, tenant-mismatched evidence, synthetic evidence misuse, and customer-facing wording risks.

## Failure Conditions

The judge can fail because of missing context, poor evidence quality, mapping ambiguity, framework drift, prompt injection, retrieval errors, or workflow misuse.

The judge MUST fail closed for mapping assurance when:

- Required evidence references are missing.
- Evidence cannot be accessed or validated.
- Evidence appears tenant-mismatched.
- Customer context is missing, ambiguous, or mismatched for customer-scoped workflows.
- Knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory is used.
- Framework references are unavailable where required by the implementation.
- The proposed mapping is unsupported but presented as confirmed.
- The mapping would influence a customer-facing or DFIR-impacting output without human review.
- The request attempts to bypass the judge, PEP/PDP, audit logging, or approval workflow.
- The request asks the judge to approve enforcement, containment, or customer release directly.

Fail-closed behavior for this judge means the mapping MUST NOT be treated as approved assurance output. The workflow MUST route the item to revision, evidence collection, or human review according to the governing process.

## Agent Restrictions

Agents MUST NOT:

- Invent ATT&CK or ATLAS mappings.
- Treat framework mapping as proof of compromise.
- Use mappings to imply threat actor attribution without evidence and human validation.
- Present hypotheses as confirmed findings.
- Use synthetic evidence as customer evidence.
- Reuse mappings across tenants without tenant-specific evidence validation.
- Bypass the judge when mappings influence high-impact outputs.
- Convert judge feedback into enforcement decisions.
- Claim compliance, certification, or production assurance based on framework alignment.
- Publish customer-facing mappings without required review.

## Relationship to Policy Enforcement

This judge reviews mapping quality. It does not replace PEP/PDP enforcement.

Policy enforcement files define whether a workflow action is allowed, denied, or requires approval. This judge may provide assurance signals that a PEP/PDP can consider, but it MUST NOT directly execute or authorize actions.

If policy requires a valid mapping review before report generation, escalation, or case closure, the PEP/PDP MUST evaluate that requirement through the policy-enforcement model.

## Relationship to Threat Modeling

This file does not define the full threat model. It only defines how an AI assurance judge reviews ATT&CK / ATLAS mapping quality.

Threat modeling files should define abuse cases, attack paths, mitigations, and residual risks. The mapping judge MAY review whether mapped threat-model statements are evidence-supported and correctly scoped.

## Acceptance Criteria

This file is acceptable when the ATT&CK / ATLAS Mapping Judge:

- Is clearly defined as an AI assurance component.
- Does not make enforcement, approval, containment, or customer-release decisions.
- Requires evidence references for mappings that influence investigation, DFIR, escalation, or customer-facing outputs.
- Separates ATT&CK, ATLAS, general governance risks, and architectural risks.
- Flags unsupported, overbroad, forced, or misapplied mappings.
- Requires human review for high-impact mapping use.
- Preserves tenant isolation and evidence boundaries.
- Preserves customer identity and evidence tenant attribution where mappings affect MSSP, MDR, DFIR, customer-facing, or customer-scoped workflows.
- Captures and validates knowledge store or memory scope when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, mapping catalog retrieval, or retrieved framework context influences mapping output.
- Produces standardized Agent Judge findings with mapping-specific review details kept separate from PDP decisions, approval states, and tool execution results.
- Produces auditable assurance outputs.
- Fails closed when evidence, scope, tenant, or review context is insufficient.
- Aligns with the governed Agentic MSSP / MDR / DFIR architecture without turning the file into a generic framework-mapping guide.

## Anti-Patterns

Avoid these anti-patterns:

- Using ATT&CK or ATLAS mappings as decorative labels.
- Mapping every finding to a framework even when the evidence does not support it.
- Treating model-generated mapping as analyst validation.
- Presenting low-confidence hypotheses as confirmed adversary behavior.
- Mixing customer evidence with lab, synthetic, or unrelated tenant evidence.
- Using ATT&CK or ATLAS mapping as a compliance claim.
- Letting an Agent Judge approve operational action.
- Allowing framework mapping to bypass PEP/PDP enforcement.
- Allowing mapping output to bypass human review when it affects DFIR conclusions or customer-facing reports.
- Creating broad AI governance commentary instead of focused mapping assurance.
- Duplicating threat-model, policy-enforcement, or human-oversight controls inside this file.
