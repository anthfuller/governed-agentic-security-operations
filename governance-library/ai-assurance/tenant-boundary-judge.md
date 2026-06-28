# Tenant Boundary Judge

## Purpose

The Tenant Boundary Judge evaluates whether agent-generated outputs, evidence references, workflow context, tool requests, routing recommendations, or output destinations preserve tenant and customer isolation in governed Agentic SOC, MSSP, MDR, Cloud Incident Response, and private/local LLM-assisted DFIR workflows.

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

This judge is an assurance component. It does not make policy decisions, approve actions, authorize tool execution, release customer-facing output, or replace human review.

## Scope

This file defines the assurance role of a Tenant Boundary Judge in the `ai-assurance/` layer.

It evaluates whether an agent output or workflow artifact:

- references the correct tenant and customer;
- uses tenant-authorized and customer-authorized evidence;
- uses tenant-authorized and customer-authorized knowledge stores, vector indexes, shared memory, customer context, case memory, evidence retrieval, and retrieved context;
- avoids cross-tenant or cross-customer data leakage;
- preserves customer isolation in MSSP, MDR, and DFIR workflows;
- identifies ambiguous tenant or customer context;
- detects mismatched case, workspace, subscription, account, evidence, or customer identifiers;
- identifies tenant-boundary risk in tool requests before policy-enforcement handoff;
- produces structured findings for audit, workflow routing, human review, and policy-enforcement handoff.

Detailed tenant access control, identity design, registration, lifecycle, runtime authorization, and tool enforcement belong in `agent-governance/` and `policy-enforcement/`. This file addresses the assurance evaluation boundary only.

## Control Boundary Addressed

The control boundary addressed by this judge is tenant-boundary assurance.

The judge evaluates whether the artifact under review appears consistent with the expected tenant and customer context and whether any referenced evidence, case metadata, tool context, or output destination may violate tenant or customer isolation.

The Tenant Boundary Judge MUST NOT:

- authorize cross-tenant access;
- approve data release;
- override PDP policy decisions;
- execute tools;
- modify evidence;
- determine final incident ownership;
- resolve tenant conflicts without human or policy-controlled workflow handling;
- output `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`.

Agent Judges MUST NOT make enforcement decisions. If a separate component is implemented as an authorized PDP function, it MUST be governed, registered, evaluated, and audited as a PDP, not as an Agent Judge.

## Why This Judge Exists

Agentic SOC and MSSP workflows may handle many customers, tenants, workspaces, subscriptions, accounts, cases, evidence stores, and incident queues. A tenant-boundary failure can expose sensitive data, route findings to the wrong customer, contaminate DFIR evidence, or cause incorrect operational action.

The Tenant Boundary Judge exists to provide a structured assurance check before outputs, evidence references, tool requests, or workflow transitions are consumed by downstream systems or reviewers.

## When This Judge Is Required

The Tenant Boundary Judge MUST be applied when agent-generated output, evidence references, workflow context, tool requests, routing recommendations, or output destinations affect governed decisions, customer-facing reporting, DFIR conclusions, containment recommendations, escalation, closure, governance evidence, approval workflows, tenant or customer boundaries, identity/access recommendations, policy-enforcement handoff, or high-impact operational recommendations.

At minimum, Tenant Boundary Judge evaluation MUST be applied to the following workflow conditions when tenant or customer scope affects handling:

| Workflow Condition | Minimum Handling |
|---|---|
| Customer-facing output | MUST evaluate tenant, customer, case, evidence, workspace, and destination alignment before release routing |
| DFIR timeline, forensic summary, or report draft | MUST evaluate evidence ownership, case association, customer scope, and cross-case or cross-tenant contamination risk |
| Cross-tenant or multi-customer workflow | MUST evaluate tenant, customer, workspace, subscription, account, evidence, case, and destination boundaries |
| Tool request before enforcement | MUST evaluate tenant scope, customer scope, tool context, requested action, and policy context before PDP/PEP handling |
| Evidence selection or evidence summarization | MUST evaluate evidence attribution, evidence source scope, permitted use, and case/customer association |
| Knowledge store, vector search, shared memory, customer context, case memory, evidence retrieval, or retrieved-context use | MUST evaluate tenant, customer, case, evidence, workspace, retention, and reuse boundaries before downstream handling |
| Escalation, closure, or governance evidence | MUST evaluate whether the routed output and referenced evidence belong to the correct tenant, customer, case, and workflow |
| Private/local LLM-assisted DFIR | MUST evaluate whether local evidence stores, retrieved artifacts, generated summaries, and report drafts preserve tenant and customer boundaries |

Exploratory internal analysis SHOULD use this judge when tenant ambiguity, shared context, or multi-customer evidence could affect downstream interpretation.

## Required Inputs

The following inputs MUST be available where applicable when tenant-boundary findings influence governed workflow routing, human review, fail-closed handling, customer-facing output, DFIR conclusions, governance evidence, or policy-enforcement handoff.

| Input | Requirement | Purpose |
|---|---:|---|
| `judge_request_id` | MUST | Unique identifier for the tenant-boundary judge request. |
| `judge_contract_id` | MUST for governed workflows | Identifies the governed judge contract used for evaluation. |
| `judge_contract_version` | MUST for governed workflows | Identifies the governed judge contract version used for replay and audit. |
| `judge_id` | MUST | Identifies the judge component. |
| `judge_version` | MUST for governed workflows | Supports repeatability, regression review, audit replay, and dispute review. |
| `timestamp_utc` | MUST | Records when the request was created. |
| `tenant_id` | MUST | Identifies the tenant context expected for the workflow. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Identifies the customer associated with the workflow. |
| `case_id` | MUST for case-bound investigation, MDR, incident-response, or DFIR workflows | Links the review to a governed investigation or incident case. |
| `workflow_id` | MUST for governed workflows; SHOULD for exploratory internal review | Identifies the governed workflow being evaluated. |
| `workflow_stage` | MUST where review path, routing, release readiness, or output handling depends on workflow stage | Distinguishes triage, investigation, DFIR, escalation, reporting, closure, or customer-release contexts. |
| `workspace_id` | MUST where workspace-scoped evidence or telemetry is used | Verifies the operational workspace context. |
| `subscription_id` or `account_id` | MUST where cloud subscription, account, or project scope affects the workflow | Supports cloud and multi-account boundary validation. |
| `agent_id` | MUST | Identifies the agent whose output or action request is being reviewed. |
| `agent_session_id` or `run_id` | MUST when an agent produced or influenced the reviewed output | Supports replay, traceability, and investigation of the specific agent execution. |
| `agent_owner` | MUST where escalation, accountability, or remediation routing depends on agent ownership | Supports accountability and escalation. |
| `agent_output_reference` | MUST when an agent output is reviewed | Identifies the output being judged. |
| `evidence_object_ids` | MUST where evidence is referenced | Supports traceability between output claims and tenant-bound evidence. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in a multi-tenant or customer-scoped workflow | Allows comparison between referenced evidence and expected tenant context. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in a customer-scoped workflow | Allows comparison between referenced evidence and expected customer context. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences the output, evidence interpretation, routing recommendation, tool request, customer-facing wording, or downstream use | Defines approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, workspace, retention, and reuse boundary. |
| `output_destination` | MUST where output is routed, released, or used for customer-facing, governance, legal, or operational handling | Identifies whether tenant-boundary risk affects routing or disclosure. |
| `tool_name` | MUST where tool context is reviewed | Identifies tenant-scoped tool or data-access context. |
| `tool_contract_id` | MUST where tool contracts are used | Supports validation of expected tenant-scoped tool behavior. |
| `requested_action` | MUST when tool context, containment, remediation, escalation, closure, or customer-impacting routing is reviewed | Provides context for downstream routing and human review. |
| `policy_context_id` | MUST when policy affects routing, release readiness, approval requirements, PDP context, tenant handling, evidence handling, or fail-closed behavior | Preserves policy context for downstream handling and audit. |
| `prior_judge_results` | MAY | Supports correlation with unsupported-claim, HITL, evidence-support, or output-quality findings. |

Free-form tenant labels MUST NOT be used as the only boundary identifier for governed workflows.

## Evaluation Criteria

The Tenant Boundary Judge MUST evaluate applicable artifacts against the following criteria when the output, evidence, routing, or tool context affects investigation, DFIR conclusions, escalation, containment recommendations, approval decisions, governance evidence, policy-enforcement handoff, or customer-facing reporting.

| Criterion | Required Evaluation |
|---|---|
| Tenant identity consistency | Confirm that referenced tenant identifiers match the expected workflow tenant context. |
| Customer identity consistency | Confirm that customer identifiers, case metadata, and output destination align. |
| Evidence tenant alignment | Confirm that referenced evidence belongs to the expected tenant or is explicitly marked as approved shared context. |
| Evidence customer alignment | Confirm that referenced evidence belongs to the expected customer or is explicitly authorized for shared or aggregated use. |
| Knowledge and memory scope alignment | Confirm that RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, and retrieved context remain within authorized tenant, customer, case, evidence, workspace, retention, and reuse boundaries. |
| Workspace alignment | Confirm that workspace, subscription, environment, account, project, or data-source identifiers are consistent with the expected tenant boundary. |
| Case alignment | Confirm that output, evidence, and routing references align to the correct case or incident record. |
| Cross-tenant exposure risk | Identify output text, evidence references, metadata, prompts, tool outputs, or routing details that may disclose another tenant’s data. |
| Cross-customer contamination risk | Identify whether evidence, summaries, or recommendations mix customers without explicit governed authorization. |
| Ambiguous tenant context | Identify missing, conflicting, or unclear tenant/customer identifiers. |
| Tool-context alignment | Identify tool requests or tool outputs that appear inconsistent with the tenant-scoped workflow. |
| Output-destination alignment | Identify whether the destination could expose tenant-specific content to the wrong customer, analyst queue, case, report, or approval path. |
| Evidence contamination risk | Identify whether evidence from another tenant, customer, case, or workspace appears to have been mixed into the current workflow. |
| Reviewer escalation need | Identify whether the finding requires human review, workflow quarantine, correction, or policy-enforcement handoff. |

The judge MUST distinguish tenant-boundary assurance from authorization. A clean tenant-boundary result does not authorize tool execution, release, containment, escalation, or case closure.

## Standard Finding Values

For governed workflows, the Tenant Boundary Judge MUST produce a standard Agent Judge finding in addition to any tenant-specific status.

| Finding | Meaning |
|---|---|
| `PASS` | Tenant and customer boundary checks passed for the evaluated scope. |
| `FAIL` | A tenant, customer, case, workspace, evidence, tool, or destination boundary violation was detected. |
| `NEEDS_REVIEW` | Tenant or customer context requires human review before downstream use. |
| `INSUFFICIENT_EVIDENCE` | Required tenant, customer, evidence, case, workspace, tool, or destination context is missing or insufficient. |
| `NOT_APPLICABLE` | Tenant-boundary evaluation does not apply to the evaluated item. |

`PASS` is an assurance finding only. It MUST NOT be treated as approval, release authorization, PDP authorization, or permission to execute an action.

## Tenant Boundary Status Values

The judge MAY also produce a tenant-specific `tenant_boundary_status` to support routing and dashboards.

| Status | Meaning |
|---|---|
| `TENANT_BOUNDARY_PASS` | No tenant-boundary issue was detected based on the available inputs. |
| `TENANT_CONTEXT_INCOMPLETE` | Required tenant, customer, case, workspace, evidence, or destination context is missing or insufficient. |
| `TENANT_CONTEXT_AMBIGUOUS` | Tenant or customer context is unclear, conflicting, or not reliably attributable. |
| `TENANT_MISMATCH_DETECTED` | One or more identifiers do not match the expected tenant, customer, case, workspace, evidence, or output context. |
| `CUSTOMER_MISMATCH_DETECTED` | One or more identifiers do not match the expected customer, case, evidence, or output context. |
| `CROSS_TENANT_RISK_DETECTED` | The artifact may expose, route, mix, or depend on information from another tenant. |
| `CROSS_CUSTOMER_RISK_DETECTED` | The artifact may expose, route, mix, or depend on information from another customer. |
| `EVIDENCE_BOUNDARY_RISK` | Evidence references may be missing attribution, incorrectly scoped, contaminated, or cross-boundary. |
| `NEEDS_HUMAN_REVIEW` | Human review is required to resolve tenant-boundary uncertainty or high-impact routing/release risk. This is an assurance status, not a PDP `REQUIRE_APPROVAL` decision. |
| `FAIL_CLOSED_RECOMMENDED` | The judge identified missing, conflicting, or risky tenant-boundary context that should prevent further automated routing until resolved by the governed workflow. |

## Structured Output Fields

For governed workflows, the judge MUST produce structured output.

| Field | Requirement | Purpose |
|---|---:|---|
| `judge_result_id` | MUST | Unique identifier for the judge result. |
| `judge_request_id` | MUST | Links result to the judge request. |
| `judge_contract_id` | MUST for governed workflows | Identifies the governed judge contract used for evaluation. |
| `judge_contract_version` | MUST for governed workflows | Identifies the governed judge contract version used for replay and audit. |
| `judge_id` | MUST | Identifies the judge component. |
| `judge_version` | MUST for governed workflows | Supports repeatability, regression review, audit replay, and dispute review. |
| `timestamp_utc` | MUST | Records when the evaluation occurred. |
| `finding` | MUST | Standard Agent Judge finding: `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE`. |
| `tenant_boundary_status` | MUST | Provides the tenant-specific assurance status. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Captures the expected tenant context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Captures customer context. |
| `case_id` | MUST for case-bound investigation, MDR, incident-response, escalation, closure, customer-facing, or DFIR workflows | Links the finding to the investigation or incident workflow. |
| `workflow_id` | MUST for governed workflows | Links the finding to the governed workflow. |
| `workflow_stage` | MUST when routing, review, release, escalation, or output handling depends on workflow stage | Preserves workflow-stage context for downstream handling. |
| `workspace_id` | MUST when workspace, subscription, account, project, cloud, telemetry, evidence, tool, or destination scope affects the workflow | Captures workspace context. |
| `subscription_id` or `account_id` | MUST when workspace, subscription, account, project, cloud, telemetry, evidence, tool, or destination scope affects the workflow | Captures cloud account, project, or subscription context. |
| `agent_id` | MUST | Identifies the agent associated with the output or request. |
| `agent_session_id` or `run_id` | MUST when an agent produced or influenced the reviewed output | Supports run-level traceability. |
| `evidence_object_ids` | MUST where evidence was reviewed | Supports traceability to evidence references. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence was reviewed in a multi-tenant or customer-scoped workflow | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence was reviewed in a customer-scoped workflow | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when retrieval or memory influenced the reviewed output, evidence interpretation, routing recommendation, tool request, customer-facing wording, or downstream use | Preserves retrieval, memory, customer, tenant, case, evidence, workspace, retention, and reuse boundaries. |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| `output_destination` | MUST when destination was evaluated, routed, released, or used for customer-facing, governance, legal, or operational handling | Preserves destination context for audit, routing, release-readiness, and boundary review. |
| `mismatched_identifiers` | MUST when mismatches are detected | Identifies tenant, customer, case, workspace, evidence, tool, or destination mismatches. |
| `cross_tenant_indicators` | MUST when cross-tenant risk is detected | Lists the observed indicators of possible boundary violation. |
| `cross_customer_indicators` | MUST when cross-customer risk is detected | Lists the observed indicators of possible customer-boundary violation. |
| `missing_context_fields` | MUST when context is incomplete | Identifies required fields that were unavailable. |
| `risk_rationale` | MUST | Explains why the judge produced the finding and status. |
| `recommended_routing` | MUST when the finding is `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, `TENANT_CONTEXT_INCOMPLETE`, `TENANT_CONTEXT_AMBIGUOUS`, `TENANT_MISMATCH_DETECTED`, `CUSTOMER_MISMATCH_DETECTED`, `CROSS_TENANT_RISK_DETECTED`, `CROSS_CUSTOMER_RISK_DETECTED`, `EVIDENCE_BOUNDARY_RISK`, `NEEDS_HUMAN_REVIEW`, `FAIL_CLOSED_RECOMMENDED`, or when downstream handling is required | Suggests human review, quarantine, correction, block, fail-closed handling, or policy-enforcement handoff. |
| `reviewer_required` | MUST when tenant context is incomplete, ambiguous, mismatched, cross-tenant risk is detected, cross-customer risk is detected, or the output affects customer-facing reporting, DFIR conclusions, escalation, containment recommendations, governance evidence, approval routing, or policy-enforcement handoff | Identifies whether human review is needed. |
| `review_required_reason` | MUST when `reviewer_required` is true | Explains why human review is required. |
| `audit_references` | MUST when consumed by workflow routing, human review, fail-closed handling, customer-facing output, or governance workflows | Supports reconstruction of the assurance decision. |
| `prior_judge_result_refs` | MAY | Links to related judge findings. |

Judge outputs MUST be auditable, replayable, and consistently consumable by downstream workflows.

## Required `tenant_boundary_result`

The Tenant Boundary Judge MUST produce a structured `tenant_boundary_result`.

| Field | Requirement | Purpose |
|---|---:|---|
| `status` | MUST | `PASS`, `FAIL`, `NEEDS_REVIEW`, `INSUFFICIENT_EVIDENCE`, or `NOT_APPLICABLE`. |
| `tenant_boundary_status` | MUST | Tenant-specific status such as `TENANT_BOUNDARY_PASS`, `TENANT_CONTEXT_INCOMPLETE`, or `CROSS_TENANT_RISK_DETECTED`. |
| `authorized_scope` | MUST when applicable | Authorized tenant, customer, workspace, subscription, account, case, and output-destination scope. |
| `observed_scope` | MUST when applicable | Scope observed in the evaluated input, output, evidence, tool request, or routing context. |
| `boundary_violation_detected` | MUST | Boolean boundary violation indicator. |
| `cross_tenant_data_detected` | MUST | Boolean cross-tenant indicator. |
| `cross_customer_data_detected` | MUST when customer scope applies | Boolean cross-customer indicator. |
| `evidence_scope_valid` | MUST when evidence is reviewed | Whether evidence is scoped to the correct tenant, customer, case, workspace, subscription, or account. |
| `knowledge_memory_scope_valid` | MUST when knowledge store or memory scope is evaluated | Whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved tenant, customer, case, evidence, and workspace boundaries. |
| `destination_scope_valid` | MUST when output destination is reviewed | Whether the destination aligns to the expected tenant, customer, case, and workflow. |
| `tool_scope_valid` | MUST when tool context is reviewed | Whether tool context aligns to the expected tenant and customer scope. |
| `handling_requirement` | MUST when violation, ambiguity, missing context, or downstream handling is detected | Human review, correction, quarantine, block, fail closed, or policy-enforcement handoff. |
| `rationale_summary` | MUST | Concise boundary evaluation rationale. |

Cross-tenant or cross-customer data mixing MUST be blocked or fail closed. Escalation alone is insufficient unless data has not been exposed, executed, released, or used in a governed decision.

## Recommended Routing Values

For governed workflows, when `recommended_routing` is produced, routing values MUST be selected from the governed route vocabulary unless the contract is explicitly versioned and approved.

| Route | Meaning |
|---|---|
| `CONTINUE` | Continue only to the next required workflow step. |
| `CORRECT_CONTEXT` | Correct tenant, customer, case, workspace, evidence, or destination context before use. |
| `REQUEST_MORE_CONTEXT` | Obtain required tenant, customer, evidence, case, workspace, tool, or destination context before use. |
| `REQUIRE_HUMAN_REVIEW` | Human review is required before downstream use. |
| `QUARANTINE_OUTPUT` | Hold output or artifact to prevent exposure or downstream use. |
| `BLOCK_RELEASE` | Block customer-facing or external release. |
| `BLOCK_TOOL_REQUEST` | Block tool request before policy-enforcement or execution handoff. |
| `FAIL_CLOSED` | Fail closed before governed processing continues. |
| `ESCALATE` | Escalate under the governed process without treating escalation as authorization. |

`ESCALATE` is not authorization, release approval, tenant-boundary exception, or permission to execute a governed action.

Routing values are handling signals. They MAY become policy-relevant inputs to the PDP, but only the PDP produces governed authorization decisions.

## Human Review Requirements

Human review MUST verify applicable tenant, customer, case, workspace, evidence, destination, and shared-context boundaries when the finding affects DFIR conclusions, customer-facing reporting, escalation, containment recommendations, governance evidence, approval routing, or policy-enforcement handoff.

Human review MUST verify, where applicable:

- expected tenant and customer context;
- case and workspace association;
- evidence object ownership;
- output destination;
- whether any cross-tenant or cross-customer reference is authorized shared context;
- whether aggregation or shared context is permitted for the intended use;
- whether knowledge store or memory scope is authorized, current, tenant-scoped, customer-scoped, case-scoped, retention-consistent, and permitted for the intended use;
- whether the artifact should be corrected, quarantined, escalated, blocked, or rejected.

Human review MUST NOT be bypassed where tenant or customer context is ambiguous and the output may affect another customer, tenant, case, evidence set, tool request, or destination.

Human review MUST NOT convert unauthorized cross-tenant or cross-customer exposure into approved evidence. Review may authorize correction, quarantine, additional evidence collection, documented exception handling, or restricted internal handling under policy.

## Fail-Closed Conditions

The governed workflow MUST fail closed or route to the appropriate controlled review path when:

- tenant or customer identity is missing for a tenant-scoped or customer-scoped workflow;
- tenant identifiers conflict across input, evidence, tool output, or destination;
- customer identifiers conflict across input, evidence, case, tool output, or destination;
- evidence references do not match the expected tenant, customer, workspace, subscription, account, or case;
- knowledge store or memory scope is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influenced the output, evidence interpretation, routing recommendation, tool request, customer-facing wording, or downstream use;
- output text contains another tenant’s or customer’s protected data;
- destination metadata does not match the expected tenant, customer, case, or workflow;
- workspace, subscription, environment, account, project, or case context is inconsistent;
- the judge cannot determine whether the content is tenant-safe or customer-safe;
- the judge result cannot be persisted for audit in a governed workflow.

Fail-closed handling MUST preserve the original artifact, judge result, evidence references, tenant context, customer context, routing reason, workflow state, and reviewer disposition for audit review in governed workflows.

## Audit Requirements

Governed workflows using the Tenant Boundary Judge MUST audit:

- judge request and result identifiers;
- judge contract identifier and version for governed workflows;
- judge identity and version for governed workflows;
- agent identity and agent session or run identifier where an agent produced or influenced the reviewed output;
- the agent output or artifact reviewed;
- the tenant, customer, case, workspace, subscription, account, workflow, and workflow-stage context;
- evidence references and evidence attribution metadata provided to the judge;
- knowledge store or memory scope where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced the reviewed output, evidence interpretation, routing recommendation, tool request, customer-facing wording, or downstream use;
- output destination and tool context where applicable;
- judge finding, tenant-boundary status, and rationale;
- detected mismatches or cross-tenant/cross-customer indicators;
- missing or ambiguous context fields;
- human review requirement and reason where applicable;
- human review outcome, where applicable;
- downstream routing, quarantine, correction, escalation, block, or fail-closed handling;
- policy-enforcement handoff, where applicable.

Audit records MUST support reconstruction of the reviewed artifact, context, finding, routing, and downstream handling.

Audit records MUST NOT expose another tenant’s or customer’s protected content beyond what is required for authorized investigation, review, legal hold, or governance handling.

## Private/Local LLM-Assisted DFIR Considerations

Private or local model execution reduces some exposure pathways, but it does not prove tenant correctness, customer correctness, evidence validity, or authorization.

The Tenant Boundary Judge MUST treat local model execution as an execution and evidence-handling context, not as proof that the output is tenant-safe or customer-safe.

For private/local LLM-assisted DFIR, the judge MUST evaluate whether:

- local evidence stores are tenant-scoped and customer-scoped;
- retrieved forensic artifacts belong to the expected tenant, customer, or case;
- RAG, vector search, shared memory, customer context, case memory, evidence retrieval, and retrieved context remain within approved tenant, customer, case, evidence, workspace, retention, and reuse boundaries;
- generated summaries avoid cross-case, cross-customer, or cross-tenant contamination;
- report drafts preserve customer boundaries;
- analyst validation is required before customer-facing or legally sensitive use.

## Relationship to PEP/PDP

The Tenant Boundary Judge provides assurance findings only.

The PDP produces governed policy decisions according to the policy contract.

The PEP enforces PDP decisions and obligations within the governed workflow or tool boundary.

Tenant-boundary findings MAY be provided to policy-enforcement components as context, but the judge MUST NOT replace PDP decision-making or PEP enforcement.

## Relationship to Other AI Assurance Judges

The Tenant Boundary Judge may operate alongside:

- unsupported-claim judges;
- output-quality judges;
- HITL compliance judges;
- ATT&CK / ATLAS mapping judges;
- evidence-support judges.

Each judge MUST produce structured findings within its own assurance scope for governed workflows. Tenant-boundary results MUST NOT be treated as proof that the output is factually correct, complete, legally sufficient, approved for release, or authorized for execution.

## Acceptance Criteria

This file is implemented correctly when:

- the judge is clearly defined as an assurance component;
- tenant and customer isolation are treated as mandatory control boundaries;
- standard Agent Judge findings remain separate from tenant-specific assurance statuses;
- output statuses are assurance statuses only;
- PDP and PEP responsibilities remain separate;
- required input and output fields support tenant-boundary, customer-boundary, workflow, and run-level traceability;
- knowledge store or memory scope is captured and evaluated when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences governed outputs, tool requests, routing, or downstream use;
- high-impact tenant or customer uncertainty routes to human review or fail-closed handling;
- audit records can reconstruct the reviewed artifact, context, finding, routing, and downstream handling;
- private/local LLM-assisted DFIR is treated as an evidence-handling context, not proof of correctness;
- no section implies that an Agent Judge can approve release, authorize tool execution, or enforce policy.

## Anti-Patterns

Avoid the following:

- treating `TENANT_BOUNDARY_PASS` or `PASS` as approval or authorization;
- allowing an Agent Judge to override PDP or human approval decisions;
- routing customer-facing output when tenant or customer context is incomplete;
- mixing customer evidence in shared prompts without tenant and customer attribution;
- using local/private model execution as proof of tenant safety or customer safety;
- storing audit records that expose another tenant’s or customer’s protected content unnecessarily;
- relying on filename, analyst notes, or free-text labels as the only tenant or customer identifier;
- permitting cross-tenant or cross-customer retrieval without explicit governed authorization;
- using RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context outside approved knowledge store or memory scope;
- allowing downstream workflows to ignore tenant-boundary judge failures;
- collapsing Agent Judge, PDP, PEP, human reviewer, and tool executor roles into one component.
