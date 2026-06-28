# Output Quality Judge

## Reference Architecture Disclaimer

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

## Purpose

The Output Quality Judge is an AI assurance component used to evaluate whether agent-generated outputs are suitable for governed Agentic SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR workflows.

It assesses whether an output is clear, evidence-grounded, appropriately scoped, tenant-safe, operationally safe, and ready for the next governed workflow step.

The Output Quality Judge does not approve actions, authorize tool execution, enforce policy, validate incident truth, certify forensic conclusions, or replace human analysts, incident responders, forensic examiners, policy engines, customer approvers, or formal approval workflows.

## Scope

This file applies to generated outputs that may influence:

- Investigation summaries
- DFIR analysis notes
- Customer-facing reports
- Escalation recommendations
- Containment, eradication, recovery, or remediation recommendations
- Analyst handoff summaries
- Governance evidence
- Approval-routing packages
- Executive or operational summaries
- Legal-sensitive or regulatory-supporting narratives
- Identity or access recommendations
- Tool-use recommendations before enforcement
- Private/local LLM-assisted DFIR report drafts

This file belongs in `ai-assurance/` because it defines an assurance review pattern for output quality. Detailed approval workflows belong in `human-oversight/`. Policy decision contracts, PEP/PDP behavior, action risk classification, and fail-closed enforcement belong in `policy-enforcement/`.

## Non-Goals

The Output Quality Judge MUST NOT:

- Act as a PDP.
- Produce `ALLOW`, `DENY`, or `REQUIRE_APPROVAL` decisions.
- Act as a human approver.
- Approve customer-facing release.
- Execute or authorize tool actions.
- Determine final incident severity, containment status, root cause, attribution, legal status, or compliance status.
- Certify forensic validity, evidence admissibility, or chain-of-custody sufficiency.
- Replace analyst, incident commander, forensic examiner, customer, legal, compliance, governance, or executive accountability.
- Treat local/private model execution as proof of accuracy, safety, or forensic validity.

## Assurance Role

The Output Quality Judge supports the governed Agentic MSSP / MDR / DFIR architecture by evaluating whether generated outputs meet quality and control expectations before they are routed to analysts, approvers, customer-facing workflows, policy-enforcement handoffs, or audit systems.

It evaluates output quality. It does not enforce output handling.

Agent Judges MUST NOT make enforcement decisions. If a separate component is implemented as an authorized PDP function, it MUST be governed, registered, evaluated, and audited as a PDP, not as an Agent Judge.

## When This Judge Is Required

The Output Quality Judge MUST be applied when agent-generated output affects governed decisions, customer-facing reporting, DFIR conclusions, containment, eradication, recovery, escalation, closure, legal-sensitive findings, governance evidence, approval workflows, tenant or customer boundaries, identity/access recommendations, tool requests, or high-impact operational recommendations.

At minimum, Output Quality Judge evaluation MUST be applied under the following conditions:

| Workflow Condition | Minimum Handling |
|---|---|
| Customer-facing output | MUST evaluate evidence grounding, scope, uncertainty, unsupported claims, audience appropriateness, and release readiness. |
| DFIR conclusion, timeline, or report draft | MUST evaluate evidence traceability, forensic caution, claim specificity, uncertainty, and reviewer requirements. |
| Containment, eradication, recovery, or remediation recommendation | MUST evaluate evidence support, operational impact, tenant/customer scope, approval context, and action-safety wording. |
| Escalation, severity, closure, or incident-status output | MUST evaluate evidence support, certainty language, scope, and review requirements before operational reliance. |
| Governance evidence or executive summary | MUST evaluate supportability, limitations, scope, audience appropriateness, and non-overclaiming. |
| Legal-sensitive or regulatory-supporting output | MUST evaluate evidence references, uncertainty, required review context, and prohibited legal/compliance overstatement. |
| Tenant, customer, workspace, subscription, account, or case boundary concern | MUST evaluate boundary consistency and route boundary ambiguity to fail-closed or review handling. |
| Identity or access recommendation | MUST evaluate evidence support, scope, operational impact, and required human review context. |
| Tool request or tool-influencing recommendation | MUST evaluate whether the output implies authorization, execution, or approval outside the governed PEP/PDP and tool-execution path. |
| Exploratory internal analysis without governed impact | SHOULD evaluate output quality when the output may later be reused, cited, summarized, or promoted into a governed workflow. |

## Control Boundary Addressed

The control boundary addressed by this judge is output quality assurance.

The judge evaluates whether generated content is:

- Evidence-grounded
- Tenant-scoped and customer-scoped
- Clear enough for operational use
- Free from unsupported conclusions
- Appropriate for the intended workflow stage
- Safe to route to the next governed workflow step
- Explicit about uncertainty, assumptions, limitations, and missing evidence
- Consistent with the requested output destination and audience
- Separate from authorization, approval, and tool-execution outcomes

The judge MUST NOT:

- Produce `ALLOW`, `DENY`, or `REQUIRE_APPROVAL` policy decisions
- Approve containment, remediation, isolation, deletion, access change, or customer notification
- Execute tools or initiate workflow actions
- Convert a low-quality output into an approved output
- Treat polished language as proof of correctness
- Treat local/private model execution as proof of accuracy or forensic validity
- Suppress uncertainty or evidence gaps to make the output appear complete
- Treat quality status as customer-release approval

## Required Inputs

The following inputs MUST be available where applicable when output quality findings influence governed workflow routing, human review, fail-closed handling, customer-facing output, DFIR conclusions, governance evidence, approval routing, or policy-enforcement handoff.

| Input | Requirement | Purpose |
|---|---|---|
| `judge_request_id` | MUST | Unique identifier for the output-quality evaluation request. |
| `judge_contract_id` | MUST for governed workflows | Identifies the governed judge contract. |
| `judge_contract_version` | MUST for governed workflows | Supports replay, audit review, and contract-version traceability. |
| `judge_id` | MUST | Identifies the Output Quality Judge. |
| `judge_version` | MUST for governed workflows | Supports repeatability, regression review, audit replay, and dispute review. |
| `timestamp_utc` | MUST | Records when the judge request was created. |
| `agent_id` | MUST when an agent produced or influenced the output | Identifies the agent associated with the output. |
| `agent_version` | MUST when applicable | Identifies the agent version used. |
| `agent_session_id` or `run_id` | MUST when an agent produced or influenced the output | Supports replay, traceability, and investigation of the specific agent execution. |
| `workflow_id` | MUST for governed workflows | Links the evaluation to the governed workflow. |
| `workflow_stage` | MUST when routing, review, or output handling depends on workflow stage | Supports stage-appropriate evaluation and review routing. |
| `case_id` | MUST for case-bound workflows | Links the review to the investigation or incident record. |
| `tenant_id` | MUST for tenant-scoped workflows | Preserves tenant boundary validation. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary validation. |
| `workspace_id` | MUST when workspace scope affects the output | Links the output to the SIEM, XDR, cloud, or logging workspace boundary. |
| `subscription_id` or `account_id` | MUST when cloud account scope affects the output | Links the output to the authorized cloud boundary. |
| `output_object_id` | MUST | Identifies the specific output being evaluated. |
| `agent_output_reference` | MUST | References the output body or stored artifact without requiring uncontrolled free-form reuse. |
| `output_type` | MUST | Identifies whether the output is an investigation summary, DFIR note, customer report, escalation recommendation, containment recommendation, governance artifact, or other governed output. |
| `evaluation_scope` | MUST | Identifies whether the evaluation applies to draft review, customer release readiness, DFIR review, approval package readiness, escalation, closure, or tool-influencing output. |
| `intended_use` | MUST | Analyst-only, customer-facing, containment, forensic, detection engineering, legal-sensitive, executive communication, or approval routing. |
| `intended_audience` | MUST when audience affects quality or release readiness | Identifies internal analyst, customer, executive, legal/regulatory, governance, or approval workflow audience. |
| `output_destination` | MUST where routing, release, or approval depends on destination | Supports destination-specific quality and review requirements. |
| `risk_level` | MUST where quality findings affect routing or review requirements | Supports escalation and review decisions. |
| `evidence_object_ids` | MUST when the output makes factual, investigative, DFIR, customer-facing, escalation, or governance claims | Supports evidence-to-output validation. |
| `evidence_references` | MUST when the output makes factual, investigative, DFIR, customer-facing, escalation, or governance claims | Enables evidence-to-output validation. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences the output, evidence interpretation, claim wording, routing recommendation, customer-facing wording, approval package, or downstream use | Defines approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, and retention boundary. |
| `claim_reference_ids` | MUST when claim-level review was performed for customer-facing reporting, DFIR conclusions, escalation, closure, containment, governance evidence, approval routing, tenant/customer boundaries, legal-sensitive findings, or high-impact operational decisions; SHOULD for lower-risk exploratory internal review | Supports traceability between claims, evidence, and findings. |
| `approved_data_sources` | MUST when the output relies on external enrichment, threat intelligence, customer evidence, or forensic artifacts | Supports source-appropriateness review. |
| `policy_context_id` | MUST when policy affects routing, release readiness, approval requirements, PDP context, tenant handling, evidence handling, or fail-closed behavior | Preserves policy context for downstream routing and audit. |
| `policy_obligation_ids` | MUST when policy obligations are evaluated or referenced | Links the finding to required obligations. |
| `approval_context` | MUST when the output references or depends on human approval | Provides approval state, scope, reviewer, and timestamp context. |
| `data_classification` | MUST when classification affects handling | Supports data-handling and release controls. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity or handling label context. |
| `model_id` | SHOULD | Supports repeatability and model-level traceability. |
| `prompt_template_id` | SHOULD where templated generation is used | Supports review of prompt-driven output patterns. |
| `known_limitations` | SHOULD when relevant | Documents known telemetry, evidence, model, or workflow limitations. |

Free-form output evaluation requests MUST NOT be used for governed workflows unless wrapped in a structured request object with required metadata.

## Evaluation Criteria

The judge MUST evaluate applicable agent output against the following criteria when the output influences investigation, DFIR conclusions, escalation, containment recommendations, approval decisions, governance evidence, or customer-facing reporting.

| Criterion | Requirement | Evaluation Intent |
|---|---|---|
| Evidence grounding | MUST | Claims that affect governed decisions MUST be supported by referenced evidence. |
| Claim specificity | MUST | The output MUST distinguish observed facts, inferred conclusions, assumptions, hypotheses, recommendations, and unknowns. |
| Tenant and customer scoping | MUST | The output MUST NOT mix tenants, customers, cases, evidence sets, workspaces, subscriptions, accounts, or environments. |
| Knowledge and memory scope | MUST when retrieval or memory is used | The output MUST NOT rely on stale, unauthorized, cross-customer, cross-tenant, cross-case, or retention-inconsistent retrieved context, RAG, vector search, shared memory, customer context, case memory, or evidence retrieval. |
| Operational clarity | MUST | The output MUST be understandable by the intended analyst, reviewer, approver, customer, or operational recipient. |
| Action safety | MUST | The output MUST NOT imply that sensitive actions are approved, executed, complete, or authorized unless that status is provided by the governed workflow. |
| Uncertainty handling | MUST | Unknowns, evidence gaps, assumptions, confidence limitations, and unresolved questions MUST be stated where material. |
| Audience appropriateness | MUST when audience affects handling | Wording MUST match the intended audience and output destination. |
| Forensic caution | MUST for DFIR outputs | DFIR outputs MUST avoid unsupported certainty, unsupported attribution, or conclusions not tied to evidence and chain-of-custody context where applicable. |
| Customer-facing readiness | MUST for customer-facing outputs | Customer-facing outputs MUST be reviewed for supportability, evidence grounding, scope, limitations, and release risk. |
| Legal/regulatory sensitivity | MUST where applicable | Outputs used for legal, regulatory, contractual, or governance support MUST preserve uncertainty and evidence references and MUST NOT make legal conclusions without required review. |
| Approval-status accuracy | MUST when approval is referenced | The output MUST NOT state or imply approval unless approval context is present, valid, scoped, and timely. |
| Non-overclaiming | MUST | The output MUST NOT claim production maturity, compliance status, forensic proof, attribution, containment success, or control effectiveness without evidence and required review context. |
| No autonomous SOC framing | MUST | The output MUST NOT imply that agents replace analysts, incident responders, forensic examiners, human approvers, policy engines, or incident command. |

## Output Requirements

The judge MUST produce structured findings for governed workflows so the result can be consumed by assurance dashboards, workflow routing, audit systems, human review queues, or policy-enforcement handoffs.

| Field | Requirement | Purpose |
|---|---|---|
| `judge_result_id` | MUST | Unique identifier for the judge result. |
| `judge_request_id` | MUST | Correlates the result to the request. |
| `judge_contract_id` | MUST for governed workflows | Identifies the governed judge contract. |
| `judge_contract_version` | MUST for governed workflows | Supports replay and contract-version traceability. |
| `judge_id` | MUST | Identifies the assurance judge. |
| `judge_version` | MUST for governed workflows | Supports repeatability, regression review, audit replay, and dispute review. |
| `timestamp_utc` | MUST | Records evaluation time. |
| `agent_id` | MUST when an agent produced or influenced the output | Identifies the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent produced or influenced the output | Preserves run-level traceability. |
| `workflow_id` | MUST for governed workflows | Links result to the governed workflow. |
| `workflow_stage` | MUST when routing, review, or output handling depends on workflow stage | Preserves workflow-stage context for routing and audit. |
| `case_id` | MUST for case-bound workflows | Links findings to the case or incident. |
| `tenant_id` | MUST for tenant-scoped workflows | Supports tenant-scoped audit and routing. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Supports customer-scoped audit, routing, and dispute review. |
| `output_object_id` | MUST | Identifies the reviewed output. |
| `output_type` | MUST | Identifies the output category reviewed. |
| `evaluation_scope` | MUST | Identifies the quality review scope. |
| `intended_use` | MUST when applicable | Preserves intended-use context for downstream handling. |
| `output_destination` | MUST when applicable | Preserves destination context for release-readiness and routing. |
| `finding` | MUST | Standard Agent Judge finding: `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE`. |
| `output_quality_status` | MUST | Output-quality-specific assurance status. |
| `severity` | MUST when applicable | Severity of the quality or assurance finding. |
| `confidence` | MUST when produced | Confidence score or rating for the judge result. |
| `quality_findings` | MUST | Lists quality issues, gaps, or pass conditions. |
| `failed_checks` | MUST when applicable | Specific output-quality checks that failed. |
| `passed_checks` | SHOULD when useful | Checks that passed and support replay or review. |
| `evidence_gaps` | MUST when evidence gaps are identified | Identifies unsupported or insufficiently supported claims. |
| `unsupported_claims` | MUST when unsupported claims are identified | Links or summarizes unsupported claims. |
| `claim_reference_ids` | MUST when claim-level findings are produced for governed output | Links findings to specific claims. |
| `tenant_boundary_result` | MUST when evaluated | Records tenant or customer boundary evaluation result. |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, and retention scope remained within approved boundaries. |
| `evidence_validation_result` | MUST when evaluated | Records evidence-support evaluation result. |
| `required_human_review` | MUST | Indicates whether human review is required before downstream use. |
| `review_required_reason` | MUST when `required_human_review` is true | Explains why human review is required. |
| `routing_recommendation` | SHOULD | Recommends routing such as correction, analyst review, customer release review, exception review, block, or fail-closed handling. |
| `policy_context_id` | MUST when policy affects handling | Preserves policy context used for routing or handoff. |
| `policy_obligation_ids` | MUST when policy obligations are evaluated or referenced | Links findings to obligations. |
| `correlation_ids` | MUST when applicable | Links related workflow, audit, PDP, PEP, tool execution, or approval references. |
| `audit_reference_id` | MUST when consumed by workflow routing, human review, fail-closed handling, customer-facing reporting, or governance workflows | Supports traceability and audit review. |
| `limitations` | MUST where material | Documents judge limitations, uncertainty, or scope boundaries. |
| `rationale_summary` | MUST | Concise rationale without unsupported claims. |

Judge outputs MUST be auditable, replayable, and consistently consumable by downstream workflows.

## Standard Agent Judge Findings

The top-level `finding` field MUST use the governed Agent Judge finding vocabulary unless the contract is explicitly versioned and approved.

| Finding | Meaning |
|---|---|
| `PASS` | The evaluated output met the applicable Output Quality Judge criteria for the evaluation scope. |
| `FAIL` | The evaluated output violated one or more required quality, scope, safety, evidence, or non-overclaiming criteria. |
| `NEEDS_REVIEW` | The evaluated output requires human review before downstream use. |
| `INSUFFICIENT_EVIDENCE` | The judge could not verify the output with available evidence or context. |
| `NOT_APPLICABLE` | The Output Quality Judge criteria do not apply to the evaluated item. |

`PASS` does not authorize release, containment, escalation, closure, tool execution, or customer communication. It means only that the output passed this specific assurance check for the stated scope.

## Output Quality Status Values

`output_quality_status` values are quality assurance statuses, not PDP decisions.

| Status | Meaning |
|---|---|
| `QUALITY_PASS` | Output meets applicable quality criteria for the current workflow stage. |
| `QUALITY_PASS_WITH_LIMITATIONS` | Output may continue only with documented limitations, scope constraints, or qualified wording. |
| `QUALITY_NEEDS_REVISION` | Output requires correction before downstream use. |
| `QUALITY_NEEDS_HUMAN_REVIEW` | Output requires analyst, reviewer, approver, customer release, legal, or governance review before downstream use. |
| `QUALITY_INSUFFICIENT_EVIDENCE` | Output includes claims, conclusions, or recommendations that are not adequately supported by referenced evidence. |
| `QUALITY_OUT_OF_SCOPE` | Output includes content outside the agent role, case scope, tenant boundary, customer boundary, or requested workflow task. |
| `QUALITY_FAIL` | Output fails required quality criteria and must not proceed without correction or governed review. |

`QUALITY_NEEDS_HUMAN_REVIEW` is an assurance status. It is not a PDP `REQUIRE_APPROVAL` decision.

## Recommended Routing Values

When `routing_recommendation` is produced, routing values MUST be selected from the governed route vocabulary unless the contract is explicitly versioned and approved.

| Route | Meaning |
|---|---|
| `CONTINUE` | Continue only to the next required control, review, or workflow step. |
| `CORRECT_OUTPUT` | Correct quality issues before use. |
| `REQUEST_MORE_EVIDENCE` | Obtain required evidence before use. |
| `REQUIRE_HUMAN_REVIEW` | Human review is required before downstream use. |
| `REQUIRE_CUSTOMER_RELEASE_REVIEW` | Customer-facing release review is required. |
| `REQUIRE_FORENSIC_REVIEW` | Forensic review is required. |
| `REQUIRE_LEGAL_REVIEW` | Legal-sensitive review is required. |
| `RESTRICT_INTERNAL_HANDLING` | Restrict output to internal, qualified, or exploratory use under policy. |
| `BLOCK` | Block the output, claim, recommendation, or downstream use. |
| `FAIL_CLOSED` | Fail closed before governed processing continues. |
| `ESCALATE` | Escalation is required under policy. |

Routing values are handling signals. They MAY become policy-relevant inputs to the PDP, but only the PDP produces governed authorization decisions.

## Human Review Requirements

Human reviewers MUST validate output quality when the output influences DFIR conclusions, customer-facing reporting, escalation, containment recommendations, legal/regulatory support, governance evidence, approval routing, incident closure, identity/access recommendations, or high-impact operational decisions.

Human reviewers MUST verify:

- Whether claims are supported by evidence references
- Whether the output separates fact, inference, assumption, hypothesis, and recommendation
- Whether material uncertainty is disclosed
- Whether tenant, customer, case, workspace, subscription, account, and evidence boundaries are preserved
- Whether knowledge store or memory scope is preserved when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced the output, evidence interpretation, claim wording, routing recommendation, customer-facing wording, approval package, or downstream use
- Whether the output is appropriate for the intended audience and output destination
- Whether the output implies unauthorized approval, enforcement, containment, closure, or customer release
- Whether the output requires correction, escalation, exception handling, or formal approval workflow routing
- Whether evidence gaps prevent the output from being used as a validated finding

Where individual claims are evaluated for high-impact governed outputs, the reviewer MUST verify claim-to-evidence linkage.

Human review MAY authorize correction, additional evidence collection, limited hypothesis labeling, documented exception handling, restricted internal handling, or formal approval routing under policy, but MUST NOT convert unsupported claims into validated findings.

## Policy Integration Requirements

Output Quality Judge findings MAY be used as PDP input when policy requires output-quality context.

The following requirements apply:

- A `FAIL`, `NEEDS_REVIEW`, or `INSUFFICIENT_EVIDENCE` finding for customer-facing, DFIR-impacting, legal-sensitive, containment, escalation, closure, governance, or high-impact output MUST prevent downstream reliance until correction, evidence collection, review, or approved routing occurs under policy.
- Output quality findings MUST NOT become PDP decisions unless consumed by the PDP under the governed policy decision contract.
- The PDP decision contract MUST remain separate from the Output Quality Judge finding contract.
- The PEP MUST enforce PDP obligations. The Output Quality Judge MUST NOT enforce those obligations directly.
- Unsupported customer-facing claims MUST be corrected, removed, qualified as hypothesis-only where appropriate, or blocked from release. Customer-release review MAY approve corrected or properly qualified language, but MUST NOT approve unsupported claims as validated facts.
- Output that implies containment, eradication, recovery, closure, or approval without governed evidence and review context MUST be corrected or blocked from downstream use.

## Fail-Closed Conditions

The workflow MUST fail closed or route to governed human review when:

- Required evidence references are missing.
- Tenant, customer, case, workspace, subscription, account, or output identity is missing or inconsistent for scoped workflows.
- The output contains unsupported DFIR conclusions.
- The output contains customer-facing claims without evidence support.
- The output recommends containment, eradication, recovery, remediation, access change, or escalation without required review context.
- The output implies approval, execution, containment success, closure, or release not present in the governed workflow record.
- The output contains high-impact uncertainty without disclosure.
- The output mixes evidence across tenants, customers, cases, workspaces, subscriptions, accounts, or environments.
- Knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influenced the output, evidence interpretation, claim wording, routing recommendation, customer-facing wording, approval package, or downstream use.
- The judge cannot evaluate the output due to missing required context.
- The output destination requires approval but approval status is absent, expired, revoked, incomplete, or out of scope.
- The judge result is unavailable where output-quality evaluation is mandatory.
- Audit logging fails where audit is mandatory.

Fail-closed handling MUST preserve the original output, judge result, evidence references, claim references where applicable, routing reason, and workflow context for audit review in governed workflows.

## Audit Requirements

Governed workflows MUST audit:

- Judge request and result identifiers.
- Judge contract identifier and version.
- Judge identity and version.
- Agent identity and agent session or run identifier where applicable.
- Original agent output reference.
- Output type, intended use, audience, and destination.
- Case, tenant, customer, workflow, and workflow-stage identifiers.
- Workspace, subscription, account, or environment identifiers where applicable.
- Evidence references used for the output.
- Knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced the output, evidence interpretation, claim wording, routing recommendation, customer-facing wording, approval package, or downstream use.
- Claim-level references where applicable.
- Standard judge finding and output-quality status.
- Quality findings, failed checks, evidence gaps, unsupported claims, and limitations.
- Human review requirement and review-required reason.
- Human reviewer identity when review occurs.
- Routing recommendation and final workflow disposition of the output.
- Related PDP, PEP, approval, tool execution, or audit references where applicable.
- Fail-closed events and reasons.
- Exceptions, overrides, or break-glass handling where applicable.
- Timestamp and audit integrity reference where implemented.

Audit records MUST support reconstruction of why an output was accepted for routing, rejected, corrected, escalated, blocked, failed closed, or sent to human review.

## Private/Local LLM-Assisted DFIR Considerations

For private/local LLM-assisted DFIR workflows, the Output Quality Judge MUST treat local model execution as an execution and evidence-handling context, not as proof of correctness.

Local execution may reduce exposure risk, but it does not prove:

- The output is accurate
- The output is evidence-supported
- The output is forensically valid
- The output is approved for customer release
- The output is appropriate for legal, regulatory, or governance use
- The output is safe for containment or remediation decisions
- The output satisfies chain-of-custody, examiner review, or customer authorization requirements

Private/local DFIR outputs MUST remain subject to evidence validation, human review, auditability, and workflow-specific approval requirements.

## PEP/PDP Handoff Boundary

Output Quality Judge findings MAY be consumed by policy-enforcement workflows as context.

The judge itself MUST NOT produce policy decisions.

| Component | Responsibility |
|---|---|
| Output Quality Judge | Evaluates output quality and produces assurance findings. |
| PDP | Produces governed policy decisions according to the policy contract. |
| PEP | Enforces PDP decisions and obligations within the governed workflow or tool boundary. |
| Human Reviewer | Reviews quality, evidence support, operational impact, and release readiness where required. |
| Tool Execution Layer | Executes only mediated, authorized actions according to governed workflow controls. |
| Audit System | Preserves judge findings, routing decisions, approvals, enforcement results, and workflow outcomes. |

## Relationship to Other AI Assurance Files

| File | Purpose |
|---|---|
| `agent-judges-overview.md` | Defines the role and boundaries of Agent Judges. |
| `judge-evaluation-contract.md` | Defines the governed judge input and output contract. |
| `evidence-support-judge.md` | Defines evidence-grounding requirements. |
| `hallucination-unsupported-claim-judge.md` | Defines unsupported-claim and hallucination checks. |
| `tenant-boundary-judge.md` | Defines tenant and customer boundary validation. |
| `hitl-compliance-judge.md` | Defines human review and approval validation. |
| `judge-human-review-model.md` | Defines human review of Agent Judge findings. |
| `judge-limitations.md` | Defines limitations on Agent Judge use. |

## Acceptance Criteria

This file is acceptable when:

- The Output Quality Judge is clearly defined as an assurance component.
- The judge does not approve actions, release outputs, execute tools, or enforce policy.
- Standard Agent Judge findings remain separate from output-quality-specific status values.
- Output quality expectations are tied to governed MSSP / MDR / DFIR workflows.
- Evidence grounding is mandatory for high-impact outputs.
- Tenant, customer, case, workspace, subscription, account, and evidence boundaries are treated as control boundaries.
- Knowledge store or memory scope is captured and evaluated when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences governed outputs or downstream use.
- Human review requirements are clear for high-impact outputs.
- Review or approval does not convert unsupported claims into validated facts.
- Fail-closed conditions are explicit.
- Audit requirements support replay and traceability.
- Private/local LLM-assisted DFIR limitations are clearly stated.
- PEP/PDP responsibilities remain separate.

## Anti-Patterns

The following are anti-patterns:

- Treating fluent language as proof of correctness.
- Treating the judge as a human approver.
- Treating the judge as a PDP or enforcement component.
- Treating a `PASS` or `QUALITY_PASS` as approval to release, execute, close, or notify.
- Allowing unsupported conclusions into customer-facing reports.
- Allowing DFIR outputs without evidence references.
- Mixing tenants, customers, cases, workspaces, subscriptions, accounts, or evidence sets.
- Using RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context outside approved knowledge store or memory scope.
- Allowing outputs to imply containment, remediation, eradication, recovery, access change, closure, or approval.
- Suppressing uncertainty to make output appear complete.
- Treating local/private LLM execution as proof of forensic validity.
- Using generic quality scoring without evidence, tenant, workflow, or audit context.
- Turning output quality assurance into a generic writing-style review.
- Claiming autonomous SOC capability from judged outputs.

