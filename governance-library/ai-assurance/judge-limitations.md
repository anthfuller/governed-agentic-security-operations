# Judge Limitations

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

## Purpose

Judge Limitations defines the boundaries of Agent Judge use in governed Agentic SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR workflows.

Agent Judges provide assurance signals about agent output quality, evidence support, workflow conformance, review readiness, and risk indicators. They do not provide final truth, legal authority, forensic certification, policy authorization, or human accountability.

This file exists to prevent Agent Judge outputs from being misused as enforcement decisions, incident conclusions, approval decisions, compliance determinations, or substitutes for qualified analyst, incident commander, DFIR, customer, legal, or governance review.

## Scope

This file applies to Agent Judges used in the AI Assurance & Analytics Layer of the governed Agentic MSSP / MDR / DFIR architecture.

It applies when judges evaluate:

- Investigation summaries.
- Alert triage or enrichment output.
- DFIR report drafts.
- Evidence support and evidence traceability.
- Knowledge store, vector search, shared memory, customer context, case memory, evidence retrieval, and retrieved-context limitations.
- Unsupported or hallucinated claims.
- ATT&CK, ATLAS, or threat-model mappings.
- HITL compliance evidence.
- Tenant-boundary handling.
- Customer-facing reporting readiness.
- Governance evidence readiness.
- Private/local LLM-assisted DFIR output.

This file does not define the full PEP/PDP policy contract, approval workflow, evidence repository, forensic workflow, audit schema, or threat model. Those details belong in `policy-enforcement/`, `human-oversight/`, `local-llm-dfir/`, `workflows/`, and `threat-model/`.

## When This Limitation Model Applies

This limitation model MUST be applied whenever Agent Judge findings are produced, stored, displayed, routed, relied upon, or passed to downstream governed workflows.

At minimum, this limitation model MUST be applied when Agent Judge findings influence:

- Governed workflow routing.
- Human review routing.
- Customer-facing reporting.
- DFIR conclusions.
- Legal-sensitive, regulatory, contractual, or governance-supporting output.
- Incident escalation, severity changes, closure, or material status updates.
- Containment, isolation, blocking, disabling, deletion, remediation, recovery, or eradication recommendations.
- Tenant, customer, workspace, subscription, account, or case-boundary handling.
- Evidence interpretation, evidence selection, evidence summarization, or evidence release.
- Knowledge store, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved-context use.
- ATT&CK, ATLAS, or threat-model mappings used in operational findings.
- Approval workflows, exception handling, or break-glass processing.
- PDP context, PEP obligations, fail-closed behavior, or audit replay.

Lower-risk exploratory internal use MAY apply a lighter review model, but the output MUST remain clearly marked as exploratory and MUST NOT be reused for governed decisions, customer-facing output, DFIR conclusions, escalation, closure, containment, or governance evidence without the governed limitation controls defined in this file.

## Core Limitation Statement

Agent Judges MUST be treated as assurance components.

Agent Judges MUST NOT be treated as:

- Policy decision points.
- Enforcement engines.
- Human approvers.
- Incident commanders.
- Forensic examiners.
- Legal or regulatory authorities.
- Source-of-truth evidence systems.
- Customer authorization systems.
- Autonomous release gates without governed workflow controls.

If a separate component is implemented as a governed PDP function, it MUST be registered, evaluated, governed, and audited as a PDP, not as an Agent Judge.

## Control Boundary Addressed

The control boundary addressed by this file is judge-use limitation.

The purpose of the boundary is to ensure that Agent Judge findings are used only as assurance signals and workflow inputs, not as final operational authority.

Agent Judge outputs MAY influence routing, review prioritization, confidence assessment, evidence-gap identification, and escalation recommendations. They MUST NOT independently authorize execution, containment, evidence release, customer communication, case closure, legal reporting, tenant access, or policy exceptions.

## What Agent Judges Can Evaluate

Agent Judges MAY evaluate whether agent-generated output appears to satisfy defined assurance criteria, including:

| Evaluation Area | What the Judge Can Assess |
| --- | --- |
| Evidence support | Whether claims reference approved evidence objects or data sources. |
| Knowledge and memory scope | Whether retrieved context, RAG, vector search, shared memory, customer context, case memory, or evidence retrieval appears scoped, authorized, traceable, and retention-appropriate. |
| Claim quality | Whether output includes unsupported, speculative, exaggerated, or overconfident statements. |
| Mapping quality | Whether ATT&CK, ATLAS, or threat-model mappings appear scoped and evidence-supported. |
| HITL compliance | Whether required review evidence appears to exist for the workflow stage. |
| Tenant-boundary handling | Whether output appears to respect tenant, customer, or case boundaries. |
| Output readiness | Whether output appears suitable for human review or requires correction before downstream use. |
| Local/private LLM handling | Whether local execution context was represented accurately and not overstated as proof of correctness. |
| Audit readiness | Whether expected judge metadata and evidence references are present. |

## What Agent Judges Cannot Prove

Agent Judges MUST NOT be used to prove:

| Limitation | Required Interpretation |
| --- | --- |
| Incident truth | A judge cannot prove that an incident is malicious, benign, contained, attributable, reportable, or resolved. |
| Forensic validity | A judge cannot certify forensic soundness, chain of custody, artifact authenticity, or evidentiary admissibility. |
| Evidence completeness | A judge cannot prove that all relevant logs, artifacts, telemetry, or customer context were collected. |
| Retrieval or memory correctness | A judge cannot prove that retrieved context, RAG results, vector search results, shared memory, customer context, case memory, or evidence retrieval is complete, current, authorized, or free from stale or cross-boundary context. |
| Legal or regulatory status | A judge cannot determine breach notification, regulatory reporting, contractual liability, or legal obligations. |
| Customer authorization | A judge cannot approve customer-facing release, containment, remediation, or access to customer environments. |
| Policy authorization | A judge cannot output or replace governed PDP decisions such as `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`. |
| Human accountability | A judge cannot replace analyst, incident commander, customer, legal, governance, or executive accountability. |
| Model correctness | A judge cannot prove the reviewed model or agent was correct merely because another model evaluated it. |
| Compliance achievement | A judge cannot claim that the organization, workflow, customer, or output is compliant with a framework or regulation. |

## Required Separation of Responsibilities

Agent Judge limitations depend on clear separation of responsibilities.

| Component | Responsibility | Limitation |
| --- | --- | --- |
| Agent | Produces or proposes investigation, triage, enrichment, or reporting output. | MUST NOT self-authorize sensitive actions or final conclusions. |
| Agent Judge | Evaluates defined assurance criteria against the output and available evidence. | MUST NOT enforce policy, approve actions, or replace human review. |
| Human Reviewer | Reviews judge findings and validates high-impact outputs. | MUST NOT treat judge output as final proof without evidence review. |
| PDP | Produces governed policy decisions according to the policy contract. | MUST NOT be confused with judge assurance scoring. |
| PEP | Enforces PDP decisions and obligations within the governed workflow or tool boundary. | MUST NOT be confused with judge assurance scoring. |
| Evidence System | Stores evidence references, artifacts, provenance, and audit context. | MUST remain the source for evidence traceability, not the judge narrative. |
| Audit System | Records decisions, findings, routing, approvals, denials, exceptions, and fail-closed events. | MUST preserve judge findings as workflow evidence, not as final authority. |

## Required Inputs for Limitation-Aware Judge Use

The following inputs MUST be available where applicable when Agent Judge findings influence governed workflow routing, human review, fail-closed handling, customer-facing output, DFIR conclusions, governance evidence, policy-enforcement handoff, or audit replay.

| Input | Requirement | Purpose |
| --- | --- | --- |
| `judge_request_id` | MUST for governed workflows | Correlates limitation handling to the judge invocation. |
| `judge_contract_id` | MUST when a governed judge contract is used | Identifies the governing judge contract. |
| `judge_contract_version` | MUST when a governed judge contract is used | Supports replay against the correct contract version. |
| `judge_id` | MUST | Identifies the assurance component. |
| `judge_purpose` | MUST | Defines what the judge is allowed to evaluate. |
| `judge_version` | MUST for governed workflows | Supports repeatability, regression review, audit replay, and dispute review. |
| `workflow_id` | MUST for governed workflows | Links limitation handling to the workflow that consumed or relied on the judge result. |
| `workflow_stage` | MUST when routing, review, or output handling depends on workflow stage | Prevents misuse of judge output outside the intended process. |
| `case_id` | MUST for case-bound investigation, MDR, incident-response, or DFIR workflows | Supports traceability to the governed case. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, or customer environment workflows | Supports tenant-boundary assurance. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves the customer boundary separately from the tenant boundary. |
| `agent_output_reference` | MUST | Identifies the output being judged. |
| `agent_id` | MUST when an agent produced or influenced the reviewed output | Identifies the agent associated with the output. |
| `evidence_object_ids` | MUST when the judge evaluates evidence support, DFIR conclusions, governance evidence, customer-facing output, escalation, closure, containment, or approval routing | Supports evidence traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences the judge finding, evaluated output, evidence interpretation, limitation flags, routing recommendation, customer-facing wording, or downstream use | Defines approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, and retention boundary. |
| `approved_data_sources` | MUST when the judge evaluates claims based on enrichment, threat intelligence, customer evidence, forensic artifacts, or external context | Constrains assurance to approved sources. |
| `intended_use` | MUST when the judge result may influence downstream handling | Identifies analyst-only, customer-facing, containment, forensic, detection engineering, legal-sensitive, governance, or executive use. |
| `output_destination` | MUST when destination affects routing, release readiness, review, or audit requirements | Identifies internal, customer-facing, governance, legal, ticketing, case-system, executive, or external output destination. |
| `risk_level` | MUST when handling depends on risk | Supports routing, review, and fail-closed handling. |
| `review_policy_reference` | MUST when policy affects review routing, release readiness, approval routing, PDP context, evidence handling, tenant handling, or fail-closed behavior | Identifies the applicable review requirement. |
| `limitation_notice` | MUST when judge output is displayed to reviewers, reused downstream, or included in governed workflow context | Records the applicable limitation statement presented to downstream consumers. |
| `correlation_ids` | MUST when available | Links related workflow, audit, PDP, PEP, approval, tool, or case records. |

Free-form limitation handling MUST NOT be used for governed workflows unless it is wrapped in a structured record with the required metadata.

## Judge Outputs

Agent Judges MUST produce structured findings for governed workflows so the result can be consumed by assurance dashboards, workflow routing, audit systems, human review queues, or policy-enforcement handoffs.

A limitation-aware judge output MUST include the required fields below where applicable to the governed workflow.

| Output Field | Requirement | Purpose |
| --- | --- | --- |
| `judge_result_id` | MUST | Unique identifier for the judge finding. |
| `judge_request_id` | MUST for governed workflows | Correlates the result to the judge invocation. |
| `judge_contract_id` | MUST when a governed judge contract is used | Identifies the governing judge contract. |
| `judge_contract_version` | MUST when a governed judge contract is used | Supports replay against the correct contract version. |
| `judge_id` | MUST | Identifies the judge. |
| `judge_version` | MUST for governed workflows | Supports repeatability, regression review, audit replay, and dispute review. |
| `timestamp_utc` | MUST | Records when the limitation-aware finding was produced. |
| `case_id` | MUST for case-bound investigation, MDR, incident-response, or DFIR workflows | Links the finding to the governed case. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, or customer environment workflows | Preserves tenant-boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves the customer boundary separately from the tenant boundary. |
| `workflow_id` | MUST for governed workflows | Links the finding to the workflow that consumed or relied on it. |
| `finding` | MUST | Standard Agent Judge finding: `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE`. |
| `assurance_status` | MUST | Limitation-specific assurance status such as `PASS_WITH_LIMITATIONS`, `NEEDS_HUMAN_REVIEW`, `INSUFFICIENT_EVIDENCE`, `UNSUPPORTED_AUTHORITY_CLAIM`, `OUT_OF_SCOPE`, or `FAIL_CLOSED_RECOMMENDED`. |
| `limitation_flags` | MUST when the judge detects unsupported authority, evidence gaps, out-of-scope requests, missing context, or high-impact uncertainty | Identifies limitation categories that apply. |
| `unsupported_authority_detected` | MUST when evaluated | Indicates whether output improperly claims authority the judge cannot provide. |
| `evidence_gap_detected` | MUST when evaluated | Indicates missing or insufficient evidence linkage. |
| `knowledge_memory_scope_limitation_detected` | MUST when retrieval or memory is evaluated | Indicates whether RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context introduces limitation risk. |
| `requires_human_review` | MUST when high-impact governed output is affected | Supports review routing without acting as approval. |
| `recommended_route` | MUST when routing guidance is produced | Identifies review, correction, evidence collection, restriction, or fail-closed path. |
| `claim_reference_ids` | MUST when claim-level review was performed and the finding affects DFIR conclusions, customer-facing reporting, escalation, closure, containment recommendations, governance evidence, approval routing, tenant or customer boundaries, legal-sensitive findings, or high-impact operational decisions; SHOULD for lower-risk exploratory internal review | Supports claim-level traceability. |
| `audit_reference_id` | MUST when the judge result is consumed by workflow routing, human review, fail-closed handling, or customer-facing/governance workflows | Links to audit records or workflow event IDs. |
| `correlation_ids` | MUST when available | Links related workflow, audit, PDP, PEP, approval, tool, or case records. |
| `limitations_summary` | MUST when the result is consumed by a human reviewer or downstream workflow | Explains what the judge did and did not determine. |
| `downstream_use_constraints` | MUST when the output is not safe for unrestricted use | Identifies restrictions such as draft-only, internal-only, human-review-required, evidence-required, or customer-release-blocked. |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, and retention scope remained within approved boundaries. |

## Standard Finding Values

For governed workflows, limitation-aware Agent Judge output MUST include the standard `finding` field.

| Finding | Meaning |
| --- | --- |
| `PASS` | The evaluated item met the limitation-aware judge criteria, subject to normal judge limitations. |
| `FAIL` | The evaluated item violated required limitation boundaries, such as unsupported authority, missing required scope, or improper downstream use. |
| `NEEDS_REVIEW` | The evaluated item requires human review before downstream use. |
| `INSUFFICIENT_EVIDENCE` | The judge could not verify required evidence, context, scope, or source support. |
| `NOT_APPLICABLE` | The limitation criteria do not apply to the evaluated item. |

A `PASS` finding does not authorize action, approve release, validate forensic truth, determine legal obligations, or prove incident correctness.

## Assurance Status Values

Limitation-specific `assurance_status` values MAY provide additional context, but they MUST NOT replace the standard Agent Judge `finding` field.

Agent Judge statuses MUST remain assurance statuses, not policy decisions.

Recommended assurance status values include:

| Status | Meaning |
| --- | --- |
| `PASS_WITH_LIMITATIONS` | The output appears to satisfy the judge criteria, but normal limitations still apply. |
| `NEEDS_HUMAN_REVIEW` | The output requires human review before downstream use. This is an assurance status, not a PDP `REQUIRE_APPROVAL` decision. |
| `INSUFFICIENT_EVIDENCE` | The judge could not verify required evidence support. |
| `UNSUPPORTED_AUTHORITY_CLAIM` | The output implies the judge, agent, or workflow has authority it does not have. |
| `OUT_OF_SCOPE` | The requested judgment exceeds the defined judge purpose. |
| `FAIL_CLOSED_RECOMMENDED` | The judge detected a limitation or evidence gap that should trigger governed fail-closed handling. This is not a PDP decision. |

The judge MUST NOT output `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`. Those are governed PDP decision outputs and belong in `policy-enforcement/`.

## Recommended Routing Values

When `recommended_route` is produced, routing values MUST be selected from the governed route vocabulary unless the contract is explicitly versioned and approved.

| Route | Meaning |
| --- | --- |
| `CONTINUE` | Continue only to the next required control, review, or workflow step. |
| `CORRECT_OUTPUT` | Correct unsupported authority claims, overstated conclusions, or unsafe wording before use. |
| `REQUEST_MORE_EVIDENCE` | Obtain required evidence before downstream reliance. |
| `REQUIRE_HUMAN_REVIEW` | Route to an accountable reviewer before downstream use. |
| `RESTRICT_INTERNAL_HANDLING` | Limit use to internal exploratory or draft handling under policy. |
| `BLOCK` | Block the output, finding, or downstream use. |
| `FAIL_CLOSED` | Fail closed before governed processing continues. |
| `ESCALATE` | Escalate to the required reviewer, approver, policy owner, incident commander, legal reviewer, customer contact, or governance process. |

Routing values are handling signals. They are not authorization decisions, approval decisions, or permission to execute governed actions.

## Human Review Requirements

Human reviewers MUST validate Agent Judge findings when the finding influences:

- DFIR conclusions.
- Incident severity or classification.
- Customer-facing reporting.
- Escalation or containment recommendations.
- Legal, regulatory, contractual, or governance evidence.
- Case closure or material status updates.
- Approval routing or exception handling.
- Cross-tenant, customer-specific, or sensitive evidence handling.

Human reviewers MUST treat judge findings as review inputs, not as final determinations.

Human review MAY authorize correction, removal, additional evidence collection, limited hypothesis labeling, documented exception handling, or restricted internal use under policy. Human review MUST NOT convert unsupported claims, missing evidence, unsupported authority, or limitation flags into validated findings, customer-ready conclusions, forensic proof, legal determinations, or authorization to execute governed actions.

Where individual claims are evaluated for high-impact governed outputs, the reviewer MUST verify claim-to-evidence linkage.

## Private/Local LLM Limitation

Private or local LLM execution MAY reduce exposure to external model services, but it does not prove correctness, approval, forensic validity, legal sufficiency, chain of custody, or evidence completeness.

An Agent Judge MUST treat local model execution as an execution and evidence-handling context, not as proof of correctness.

A judge finding MUST NOT claim that local execution alone makes an output safe, valid, reportable, customer-ready, or forensically sound.

## Evidence and Forensic Limitations

Agent Judges MUST NOT be used as the system of record for forensic evidence.

When judge findings are used in DFIR workflows:

- Evidence objects MUST remain traceable to governed evidence stores or approved case repositories.
- Judge narratives MUST NOT replace artifact metadata, collection records, chain-of-custody records, analyst notes, or forensic validation.
- Missing evidence MUST be surfaced as an assurance gap.
- Inconsistent evidence references MUST be routed for review or fail-closed handling.
- Customer-facing forensic conclusions MUST be validated by accountable human reviewers.

## Framework and Mapping Limitations

Agent Judges MAY evaluate whether a framework mapping is evidence-supported and scoped, but they MUST NOT claim that a mapping proves intent, attribution, regulatory impact, or incident classification.

For ATT&CK, ATLAS, or other framework references:

- The judge MAY identify unsupported or weakly supported mappings.
- The judge MAY identify overbroad, stale, or ambiguous mappings.
- The judge MUST reference framework version, reference date, or internal framework reference when framework mappings influence DFIR conclusions, customer-facing reports, escalation, containment recommendations, or governance evidence.
- Human reviewers MUST validate mappings when they influence DFIR conclusions, customer-facing reports, escalation, containment recommendations, or governance evidence.

## Fail-Closed Conditions

Governed workflows MUST fail closed or route to human review when judge limitations create unacceptable uncertainty for downstream use.

Fail-closed or review routing is required when:

- The judge is asked to decide something outside its defined purpose.
- The judge output implies enforcement, approval, or final authority.
- Evidence references are missing for high-impact claims.
- Tenant or customer context is missing in a multi-tenant workflow.
- Knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influenced the judge finding, evaluated output, limitation flags, routing recommendation, customer-facing wording, or downstream use.
- The judge cannot distinguish between speculation and supported findings.
- The judge cannot evaluate the output because required inputs are missing.
- The output is intended for customer-facing, DFIR-impacting, legal/regulatory, escalation, containment, or governance use and required review evidence is absent.
- The judge result conflicts with policy, human review, evidence metadata, or audit records.

Fail-closed handling MUST preserve the original output, judge result, evidence references, limitation flags, and routing reason for audit review in governed workflows.

## Audit Requirements

Governed workflows using Agent Judges MUST audit:

- Judge request identifier and judge result identifier.
- Judge identity and version for governed judge limitation workflows.
- Judge contract identifier and version where a governed judge contract is used.
- Standard `finding` and limitation-specific `assurance_status`.
- Limitation flags, unsupported-authority indicators, evidence-gap indicators, and downstream-use constraints.
- Agent output reference and agent identity where applicable.
- Case, tenant, customer, workflow, workflow stage, and output-destination context.
- Evidence references provided to the judge.
- Knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced the judge finding, evaluated output, limitation flags, routing recommendation, customer-facing wording, or downstream use.
- Approved data sources used for evaluation.
- Claim reference identifiers when claim-level review affects customer-facing reporting, DFIR conclusions, escalation, closure, containment recommendations, governance evidence, approval routing, tenant or customer boundaries, legal-sensitive findings, or high-impact operational decisions.
- Human review routing and reviewer identity where applicable.
- Fail-closed events and reasons.
- Overrides, exceptions, break-glass handling, or post-event reviews.
- Downstream use of judge findings in reports, routing, approval workflows, policy context, or governance evidence.
- Timestamp and audit integrity reference where implemented.

Audit records MUST make it clear that the judge produced assurance findings, not final approval, human accountability, incident truth, forensic proof, legal determination, or PDP authorization.

## Anti-Patterns

The following patterns violate the judge limitation model:

- Treating a judge score as approval to execute containment, remediation, or customer communication.
- Allowing an Agent Judge to output `ALLOW`, `DENY`, or `REQUIRE_APPROVAL` as if it were a PDP.
- Treating `NEEDS_HUMAN_REVIEW` as equivalent to a governed approval decision.
- Using a judge finding as proof that an incident is closed, benign, malicious, attributable, or reportable.
- Claiming that local/private LLM use proves correctness or forensic validity.
- Using judge output as the source of truth for evidence, chain of custody, or artifact authenticity.
- Treating RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context as complete, current, authorized, or reusable without approved knowledge store or memory scope validation.
- Allowing an agent to self-correct based only on judge feedback and then release output without required human review.
- Using framework mapping quality as proof of incident classification.
- Suppressing limitation flags from customer-facing or governance workflows.
- Failing open when judge inputs are missing or out of scope.

## Alignment with Governed Agentic MSSP / MDR / DFIR Architecture

Judge limitations support the architecture by preserving separation between assurance, policy enforcement, human accountability, evidence handling, and operational execution.

They help ensure that Agent Judges improve review quality without becoming hidden approvers, uncontrolled policy engines, or unaccountable decision authorities.

This supports governed SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR operations by requiring evidence traceability, human validation for high-impact outputs, fail-closed routing for uncertainty, and clear audit records for downstream use.

## Acceptance Criteria

This file is correctly implemented when:

- Agent Judges are clearly documented as assurance components.
- Judge outputs are not treated as PDP decisions, human approvals, or final incident determinations.
- High-impact judge findings route to accountable human review.
- Judge findings preserve evidence references and limitation flags.
- Judge findings preserve knowledge store or memory scope limitations when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context influences governed outputs or downstream use.
- Private/local LLM execution is not represented as proof of correctness or forensic validity.
- Framework mappings are treated as scoped assurance signals, not proof of incident truth.
- Governed workflows fail closed when judge limitations or missing inputs create unacceptable uncertainty.
- Audit records distinguish assurance findings from enforcement decisions and approvals.
- Downstream systems can consume judge findings without confusing them with authorization.

## Summary

Agent Judges are useful assurance components, but their value depends on clear limitation boundaries.

They can identify evidence gaps, unsupported claims, weak mappings, review readiness issues, and workflow assurance concerns. They cannot approve actions, enforce policy, certify forensic truth, determine legal obligations, replace human accountability, or prove incident correctness.

In governed Agentic MSSP / MDR / DFIR workflows, judge findings MUST remain traceable, reviewable, limited, and auditable.
