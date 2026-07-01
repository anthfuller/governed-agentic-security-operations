# Finding Support Requirements

## Purpose

This file defines evidence support requirements for findings, recommendations, conclusions, timelines, severity determinations, escalation notes, closure rationale, approval packages, reports, and customer-facing outputs in governed agentic security operations.

Finding support ensures that each material statement can be traced to source evidence, derived artifacts, interpretation context, limitations, review records, approval records where required, and audit records.

This file defines architecture and governance expectations. It does not define a production evidence repository, legal sufficiency, forensic certification, customer-specific reporting procedure, detection rule logic, scoring algorithm, or environment-specific operational runbook.

## Scope

This file applies to evidence support for:

- Managed SOC, MSSP, MDR, and cloud incident response findings;
- alert triage findings, incident summaries, case notes, escalation narratives, and closure recommendations;
- threat-hunting hypotheses that are promoted to findings or recommendations;
- private/local LLM-assisted DFIR observations, timelines, extracted artifacts, report sections, and conclusions;
- customer-facing reports, notifications, briefings, summaries, and approval packages;
- severity, impact, scope, confidence, containment, remediation, eradication, recovery, and monitoring recommendations;
- Agent Judge evidence-support checks, unsupported-claim checks, output-quality checks, and tenant-boundary checks;
- audit replay of how a finding was created, supported, reviewed, approved, released, corrected, superseded, or recalled.

This file does not replace `evidence-reference-requirements.md`, `dfir-evidence-handling.md`, `evidence-audit-replay.md`, `human-oversight/`, `policy-enforcement/`, `tenant-isolation/`, `local-llm-dfir/`, or `audit-replay/`. It defines how evidence is attached to findings and downstream outputs.

## Non-Goals

Finding support MUST NOT be used to:

- treat agent output, model confidence, retrieved context, or narrative fluency as evidence;
- treat evidence support as authorization to execute containment, remediation, access changes, evidence release, customer notification, or case closure;
- replace analyst review, examiner review, formal approval, customer approval, legal review, or customer-specific reporting procedures;
- convert assumptions, hypotheses, stale context, or unsupported statements into confirmed findings;
- bypass tenant, customer, case, evidence, retention, legal hold, review, approval, or audit boundaries;
- imply forensic proof, legal conclusion, root-cause certainty, attribution certainty, or incident closure without required evidence, review, and approval.

## Core Principles

- A finding is not release-ready unless its material statements are linked to evidence references and limitations.
- Evidence support is claim-specific; one supported claim does not make the entire finding supported.
- Evidence support, human review, formal approval, policy authorization, and tool execution are separate control steps.
- Agent-generated summaries, hypotheses, and drafts are working artifacts, not evidence support by themselves.
- Agent Judge output is an assurance signal, not approval authority or examiner validation.
- Confidence scores are not evidence. They may be recorded as model or analyst signals only when separated from evidence support level.
- Derived artifacts must remain traceable to source evidence and transformation context.
- Findings must identify unsupported assumptions, missing evidence, conflicting evidence, uncertainty, and scope limitations.
- Customer-facing outputs must not present unsupported, partially supported, or unreviewed statements as confirmed findings.
- Tenant identity and customer identity must remain separate for MSSP, MDR, DFIR, customer-scoped, and multi-customer workflows.
- Missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, or unauditable evidence support must fail closed where governed workflow behavior depends on it.

## Finding Object Types

| Object Type | Description | Support Requirement |
|---|---|---|
| Observation | A statement about something seen in telemetry, evidence, logs, artifacts, or records. | MUST cite evidence references or derived artifacts linked to source evidence. |
| Investigative hypothesis | A possible explanation requiring validation. | MUST be labeled as a hypothesis and MUST NOT be released as a confirmed finding without supporting evidence and review. |
| Confirmed finding | A supported statement about activity, impact, scope, or condition. | MUST have evidence references, support rationale, limitation handling, and review where required. |
| Timeline item | A time-bound event or sequence used to explain activity. | MUST cite timestamp source, time-zone handling, evidence reference, and transformation context where applicable. |
| Severity determination | A priority, severity, impact, or risk classification. | MUST cite evidence and policy or service criteria used to support the determination. |
| Recommendation | Proposed containment, remediation, recovery, monitoring, reporting, or follow-up action. | MUST cite the finding and evidence basis, and MUST route to policy and approval paths where required. |
| DFIR conclusion | Examiner-facing or customer-facing conclusion from forensic analysis. | MUST cite source evidence, derived artifacts, examiner review, limitations, and approval where required. |
| Closure rationale | Explanation for closing, downgrading, escalating, or deferring a case. | MUST cite evidence, review decision, unresolved limitations, and final disposition. |
| Report statement | Statement included in a report, briefing, notification, or approval package. | MUST cite finding support records and release approval where required. |

## Evidence Support Levels

Finding support levels describe how strongly a statement is supported by evidence. They do not authorize release or action by themselves.

| Support Level | Description | Required Handling |
|---|---|---|
| `UNSUPPORTED` | No valid evidence reference supports the statement, or the statement relies only on agent output, memory, assumption, or unsupported narrative. | MUST NOT be released as a finding. Route for correction, evidence collection, or removal. |
| `CONTEXTUAL` | Background material supports context but not a case-specific claim. | MAY be used as context if clearly labeled and separated from case findings. |
| `PARTIALLY_SUPPORTED` | Some evidence supports the statement, but gaps, conflicts, uncertainty, missing sources, or unresolved scope issues remain. | Requires limitations and review before downstream use. MUST NOT be presented as confirmed without qualification. |
| `EVIDENCE_SUPPORTED` | The statement is linked to relevant evidence references and derived artifacts sufficient for the stated scope. | May proceed to review and approval path where required. |
| `EXAMINER_VALIDATED` | An accountable analyst, investigator, or examiner has reviewed the evidence interpretation. | May support higher-impact conclusions, subject to policy, approval, and release controls. |

Evidence support level MUST remain separate from release status, policy decision status, approval status, and execution status.

## Release Readiness States

Release readiness describes whether a finding or output may move through review and release workflow. It is not the same as evidence support level.

| State | Description | Requirement |
|---|---|---|
| `DRAFT` | Working finding, note, hypothesis, or report content. | MUST remain internal to the governed workflow. |
| `REVIEW_REQUIRED` | Evidence support, scope, wording, or interpretation requires analyst or examiner review. | MUST be reviewed before release or sensitive downstream use. |
| `REVISION_REQUIRED` | Reviewer found unsupported claims, missing evidence, unclear scope, or wording risk. | MUST be corrected and re-reviewed before release. |
| `APPROVAL_REQUIRED` | Policy, customer authority, legal, contractual, or operational sensitivity requires approval. | MUST have scoped approval before release or action. |
| `APPROVED_FOR_SCOPED_RELEASE` | Required review and approval are complete for a defined output, audience, case, customer, and time window. | MUST be released only within approved scope. |
| `RELEASED` | Output has been released through the governed path. | MUST preserve release record, version, approval, evidence support, and audit reference. |
| `SUPERSEDED` | A later finding or output replaces the prior version. | MUST preserve prior version and supersession record. |
| `RECALLED` | Released output is withdrawn, corrected, or restricted. | MUST preserve recall reason, affected scope, notification path, and audit reference. |

## Required Finding Support Record

Governed findings, recommendations, report statements, and customer-facing outputs SHOULD have a structured finding support record. The record MUST be present where policy, evidence handling, review, approval, or audit replay depends on it.

| Field | Requirement | Purpose |
|---|---|---|
| `finding_support_record_id` | MUST | Unique identifier for the support record. |
| `finding_id` | MUST | Links support to the governed finding, recommendation, report statement, or conclusion. |
| `finding_statement_id` | MUST when a finding contains multiple material statements | Links support to a specific claim or statement. |
| `finding_type` | MUST | Identifies observation, hypothesis, confirmed finding, severity determination, recommendation, timeline item, DFIR conclusion, closure rationale, or report statement. |
| `statement_reference` | MUST | References the statement text, report section, timeline entry, note, or output version being supported. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST | Links the finding to the incident, investigation, ticket, case, matter, or DFIR engagement. |
| `workflow_id` | MUST for governed workflows | Links support to workflow state. |
| `workflow_stage` | SHOULD when handling depends on stage | Identifies triage, investigation, escalation, reporting, approval, release, closure, correction, supersession, or recall stage. |
| `evidence_reference_ids` | MUST for supported statements | Links the finding to stable evidence references. |
| `evidence_object_ids` | MUST when available and permitted | Links the support record to underlying evidence objects. |
| `derived_artifact_ids` | MUST when parsed, extracted, normalized, enriched, summarized, or timeline artifacts support the finding | Separates source evidence from derived artifacts. |
| `transformation_record_ids` | MUST when derived artifacts affect interpretation | Links the finding to parsing, extraction, normalization, enrichment, summarization, timeline, or model-assisted transformation context. |
| `source_system_ids` | MUST when source systems affect interpretation or replay | Identifies SIEM, XDR, EDR, NDR, cloud, identity, email, SaaS, firewall, evidence store, case store, or other source systems. |
| `source_record_ids` | SHOULD when source-level records are available | Preserves source-level traceability. |
| `timestamp_basis` | MUST when timing is material | Describes whether timing comes from source event time, collection time, normalized time, timeline reconstruction, or derived artifact time. |
| `data_classification` | MUST when sensitivity affects handling, approval, or release | Preserves handling requirements. |
| `sensitivity_label` | MUST when applicable | Preserves privacy, legal, customer, forensic, or service handling label. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use for investigation, escalation, reporting, approval, customer communication, or governance review. |
| `retention_policy_id` | MUST when retention affects evidence or output use | Preserves retention and disposal boundary. |
| `legal_hold_id` | MUST when applicable | Links finding support to preservation requirements. |
| `support_level` | MUST | Records unsupported, contextual, partially supported, evidence-supported, or examiner-validated state. |
| `support_rationale` | MUST | Explains how the cited evidence supports the statement. |
| `unsupported_assumptions` | MUST when assumptions remain | Identifies claims or inferences that are not directly supported. |
| `limitations` | MUST when material | Records missing data, stale data, partial coverage, collection gaps, tool limitations, interpretation uncertainty, or scope limits. |
| `conflicting_evidence_reference_ids` | MUST when material conflicts exist | Links conflicts to evidence references rather than suppressing them. |
| `confidence_signal` | MAY | Records model, analyst, or tool confidence only when separated from evidence support level. |
| `agent_id` | MUST when an agent created, drafted, modified, cited, or consumed the support mapping | Identifies agent participation. |
| `agent_session_id` or `run_id` | MUST when an agent participated | Supports replay of agent-assisted work. |
| `agent_output_reference_id` | MUST when agent output contributed to the finding draft | Links the support record to agent-generated draft output without treating it as evidence. |
| `agent_judge_result_id` | SHOULD when assurance checks evaluated the finding | Links unsupported-claim, evidence-support, tenant-boundary, or output-quality checks. |
| `review_record_id` | MUST when analyst, investigator, or examiner review is required | Links evidence interpretation to accountable review. |
| `approval_record_id` | MUST when release, action, evidence export, or customer communication requires approval | Links support to scoped approval without replacing it. |
| `policy_context_id` | MUST when policy affects release, routing, action, or fail-closed handling | Links support to applicable policy context. |
| `output_destination` | MUST when the finding is released, exported, routed, or used downstream | Identifies report, portal, ticket, case system, approval package, notification, or workflow destination. |
| `release_record_id` | MUST when output is released | Links finding support to release version and scope. |
| `audit_reference_id` | MUST for governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links finding, evidence, workflow, tool, policy, approval, release, correction, and audit records. |
| `support_status` | MUST | Records draft, review required, revision required, approval required, approved for scoped release, released, superseded, recalled, or closed state. |

## Material Statement Requirements

Findings and reports SHOULD be decomposed into material statements when release, review, approval, audit replay, or dispute handling depends on claim-level support.

A material statement is any claim that affects interpretation, severity, scope, customer action, case closure, DFIR conclusion, or downstream decision-making.

Material statements include:

- what happened;
- when it happened;
- which asset, identity, tenant, customer, workspace, subscription, account, case, or evidence set was affected;
- whether an alert is true positive, benign, false positive, suspicious, confirmed, unresolved, or inconclusive;
- whether activity indicates compromise, attempted compromise, policy violation, exposure, persistence, lateral movement, exfiltration, malware execution, privilege escalation, or recovery;
- severity, priority, impact, likelihood, confidence, or urgency claims;
- containment, remediation, eradication, recovery, monitoring, or escalation recommendations;
- root-cause, threat actor, campaign, malware family, technique, tactic, exploitability, and data-impact claims;
- closure, downgrade, deferral, or no-action rationale;
- statements intended for customer reports, briefings, approvals, or notifications.

Each material statement MUST have one of the following:

- valid evidence support;
- clear contextual labeling;
- documented limitation or uncertainty;
- reviewer decision to remove, revise, qualify, or escalate the statement.

## Claim-Type Support Requirements

| Claim Type | Minimum Support Requirement |
|---|---|
| Observed activity | Evidence reference showing the event, artifact, telemetry, or record. |
| Timeline sequence | Timestamp basis, source evidence, normalization context, and time-zone handling where applicable. |
| Affected asset or identity | Asset, user, account, host, workload, mailbox, device, subscription, tenant, or customer evidence reference. |
| Scope or blast radius | Evidence showing searched sources, included scope, excluded scope, and known gaps. |
| Severity or priority | Evidence plus service criteria, policy context, impact rationale, or risk classification basis. |
| Impact claim | Evidence supporting observed or reasonably inferred impact, with uncertainty stated when impact is not confirmed. |
| Root-cause claim | Evidence linking cause to observed effect; otherwise label as hypothesis or likely cause. |
| Technique or tactic mapping | Evidence supporting mapped behavior and mapping rationale; weak mappings must be qualified. |
| Malware or tool identification | Evidence from artifact analysis, telemetry, signatures, hash references, sandbox results, or examiner validation where required. |
| Exfiltration or data-access claim | Evidence of access, staging, transfer, exposure, or confirmed data movement; absence of proof must not be presented as proof of no impact. |
| Attribution claim | Strong evidence and review. Low-confidence attribution must be qualified or omitted. |
| Recommendation | Finding support plus rationale linking recommendation to risk, evidence, and allowed response scope. |
| Closure or false-positive rationale | Evidence supporting benign explanation, expected behavior, test activity, duplicate status, or lack of sufficient evidence, with limitations. |
| DFIR conclusion | Source evidence, derived artifacts, examiner review, limitations, and approval where required. |

## Finding Support Workflow

| Stage | Requirement |
|---|---|
| Draft finding | Create finding, statement, or hypothesis with tenant, customer, case, workflow, and source scope. |
| Claim decomposition | Split material statements so support can be evaluated claim by claim. |
| Evidence attachment | Link evidence references, source records, derived artifacts, and transformation records. |
| Scope validation | Validate tenant, customer, case, workspace, source, retention, legal hold, and allowed-use boundaries. |
| Support classification | Assign support level for each material statement. |
| Gap and conflict capture | Record missing evidence, conflicting evidence, stale data, collection gaps, and unresolved uncertainty. |
| Agent Judge assurance | Evaluate unsupported claims, evidence support, tenant boundaries, output quality, and release risks as assurance only. |
| Human or examiner review | Review high-impact, uncertain, DFIR, disputed, customer-facing, or approval-bound findings. |
| Policy and approval routing | Route release, action, evidence export, or sensitive communication through required policy and approval paths. |
| Release or closure | Release, close, defer, escalate, revise, supersede, or recall only within approved scope. |
| Audit replay | Preserve records needed to reconstruct support, review, approval, release, correction, and final disposition. |

## Evidence Reference Requirements

Finding support MUST rely on stable evidence references rather than unbounded copied evidence whenever references are sufficient.

Evidence references used for finding support MUST preserve, where applicable:

- evidence object identifier;
- evidence reference identifier;
- source system and source record identifier;
- tenant and customer attribution;
- case, matter, incident, ticket, or workflow association;
- source timestamp, collection timestamp, normalized timestamp, or timeline timestamp basis;
- source scope, workspace, subscription, account, host, identity, mailbox, or application context;
- data classification, sensitivity label, allowed use, retention, and legal hold context;
- hash, manifest, signature, chain-of-custody, or integrity reference where applicable;
- derived artifact and transformation record identifiers when evidence was parsed, extracted, normalized, enriched, summarized, or timelined;
- access scope and audit reference.

Evidence references MUST be resolvable by authorized reviewers and replay processes. A finding that cites an inaccessible, ambiguous, stale, mismatched, or unauthorized evidence reference MUST route to correction or review.

## Derived Artifact Support Requirements

Derived artifacts may support findings only when they remain traceable to source evidence.

Derived artifacts include:

- normalized event records;
- enriched alerts;
- parsed file metadata;
- memory analysis outputs;
- packet or flow summaries;
- extracted indicators;
- timeline entries;
- screenshots with linked source records;
- local/private LLM-generated summaries;
- agent-drafted report sections;
- evidence support tables.

Derived artifacts used for finding support MUST identify:

- source evidence references;
- transformation record;
- tool, parser, model, prompt package, enrichment source, or analysis method where it affects interpretation;
- transformation timestamp;
- version information for parser, model route, enrichment source, mapping logic, or timeline logic where applicable;
- limitations, excluded data, stale inputs, failed enrichment, partial extraction, or unsupported inference.

Derived artifacts MUST NOT replace source evidence, examiner review, or chain-of-custody records.

## Normalization and Enrichment Support Requirements

Normalized and enriched data may support findings when source traceability and transformation context are preserved.

Finding support that relies on normalization or enrichment MUST record:

- normalized schema version;
- parser or transformation version;
- enrichment source and retrieval timestamp;
- enrichment confidence or quality signal where available;
- source-to-normalized field mapping where interpretation depends on mapped fields;
- stale, partial, failed, unavailable, or conflicting enrichment results;
- whether enrichment is contextual or directly case-specific.

External enrichment, threat intelligence, reputation, geolocation, sandbox, or vendor classification output MUST NOT be treated as conclusive without evidence support, scope validation, and review where required.

## Retrieved Context and Memory Requirements

Finding support may use retrieved context, knowledge stores, vector search, case memory, customer context, or evidence retrieval only when retrieval scope is governed.

When retrieved context influences a finding, the support record MUST preserve:

- retrieval source or store identifier;
- retrieval timestamp;
- query or retrieval reference where retained;
- retrieved context reference;
- tenant, customer, case, evidence, workspace, retention, and allowed-use scope;
- `knowledge_store_or_memory_scope` where applicable;
- `knowledge_memory_scope_result` where retrieval scope was evaluated;
- limitations, freshness constraints, exclusions, and conflicts.

Retrieved context MUST NOT be treated as complete, current, authorized, or reusable without scope validation. Cross-tenant, cross-customer, cross-case, stale, unauthorized, or retention-inconsistent retrieval MUST fail closed or route to review.

## Agent-Assisted Finding Support

Agents may assist with finding support when governed workflow controls permit it.

Agents may:

- draft findings from scoped evidence references;
- identify material statements requiring evidence support;
- map claims to evidence references;
- summarize evidence-derived artifacts;
- flag unsupported claims, missing evidence, conflicting evidence, stale context, and scope mismatch;
- propose support levels for review;
- prepare evidence support tables, review packages, approval packages, and report drafts;
- route uncertainty, gaps, and release risk to review.

Agents must not:

- fabricate evidence references;
- cite evidence they cannot resolve within approved scope;
- treat model output, model memory, retrieved context, or tool success as original evidence;
- assign final support level for release without required review;
- suppress conflicting evidence, limitations, or unsupported assumptions;
- convert hypotheses into confirmed findings without evidence and review;
- approve findings, release reports, notify customers, close cases, or authorize sensitive actions;
- bypass policy enforcement, human review, customer approval, evidence validation, or audit replay.

## Agent Judge and AI Assurance Boundaries

Agent Judges and AI assurance checks may evaluate finding support, but they do not approve findings or authorize release.

Agent Judge checks MAY evaluate:

- unsupported claims;
- missing or unresolved evidence references;
- evidence-to-claim alignment;
- tenant, customer, case, evidence, and retrieval boundary handling;
- conflicting evidence and limitations;
- customer-facing wording risk;
- severity and recommendation consistency;
- output-quality issues, ambiguity, overstatement, and unsupported certainty.

Agent Judge output MUST be recorded as assurance context only. It MUST NOT be treated as evidence, examiner validation, human review, formal approval, policy decision, or release authorization.

## Human Review and Examiner Review Requirements

Human review validates whether evidence support is sufficient for the intended use.

Human or examiner review is required when:

- the finding is high impact, disputed, ambiguous, or materially uncertain;
- the finding affects severity, customer notification, escalation, closure, containment, remediation, access change, evidence release, or DFIR conclusion;
- the finding relies on derived artifacts, model-assisted interpretation, retrieval, external enrichment, or incomplete evidence;
- evidence conflicts, missing data, collection gaps, stale context, or scope mismatch are material;
- customer-facing output presents confirmed findings, recommendations, or conclusions;
- policy requires review before release, action, or approval.

Review records SHOULD identify:

- reviewer identity and role;
- review timestamp;
- evidence references reviewed;
- statements accepted, revised, qualified, rejected, or escalated;
- unresolved limitations or conflicts;
- required approval path;
- audit reference and correlation identifiers.

Examiner review is required for forensic conclusions, evidence interpretation disputes, high-impact DFIR findings, and customer-facing DFIR report content where applicable.

## Approval and Policy Boundaries

Evidence support and human review do not replace policy authorization or formal approval.

Policy enforcement and approval controls remain required when a finding or recommendation affects:

- containment, remediation, eradication, recovery, or access changes;
- customer notification, report release, evidence release, or sensitive communication;
- severity escalation, service-level commitments, legal escalation, or contractual handling;
- case closure or downgrade where policy requires approval;
- cross-tenant, cross-customer, cross-case, evidence, or data-sharing boundaries;
- local/private DFIR report release or evidence-derived conclusions.

The Policy Decision Point evaluates policy context. The Policy Enforcement Point enforces decisions and obligations before tools, release paths, tenant environments, evidence stores, customer systems, or production systems are affected.

A finding support record MUST NOT be treated as a policy decision, PEP enforcement result, formal approval, customer approval, or authority to execute.

## Customer-Facing Output Requirements

Customer-facing findings, reports, notifications, recommendations, and briefings MUST preserve evidence support and release scope.

Customer-facing output MUST:

- reference supported findings or approved report sections;
- avoid unsupported certainty, unsupported attribution, unsupported impact claims, and unqualified speculation;
- identify limitations, unknowns, excluded scope, and unresolved evidence gaps where material;
- distinguish observations, hypotheses, confirmed findings, recommendations, and conclusions;
- follow required review, approval, release, and retention handling;
- preserve release version, output destination, approval record, evidence support record, and audit reference.

Customer-facing output MUST NOT present agent-generated text, retrieved context, enrichment results, or draft report content as confirmed findings unless required evidence support, review, and approval controls are complete.

## Severity, Recommendation, and Action Support

Severity, recommendation, and action-oriented statements require evidence support and governance handling.

Severity determinations SHOULD cite:

- observed activity or artifact evidence;
- affected asset, identity, system, tenant, customer, or case scope;
- impact or risk rationale;
- policy, service, or severity criteria where applicable;
- uncertainty, missing evidence, and excluded scope.

Recommendations SHOULD cite:

- finding or evidence basis;
- intended objective;
- affected scope;
- known risk, limitation, or dependency;
- whether action requires policy decision, approval, customer authority, or tool execution.

A recommendation MUST NOT be treated as authorization to execute. Sensitive action requires the appropriate policy decision, enforcement step, human approval, customer approval where required, and audit path.

## Conflicting Evidence and Limitation Handling

Finding support MUST preserve material conflicts and limitations.

Conflicting evidence includes:

- telemetry disagreement;
- source timestamp mismatch;
- parser or normalization discrepancy;
- enrichment disagreement;
- incomplete collection;
- stale data;
- missing source records;
- evidence integrity failure;
- cross-source inconsistency;
- analyst or examiner disagreement.

When conflicts or limitations are material, the finding MUST be revised, qualified, escalated, or held from release until reviewed.

Limitations SHOULD be stated in a way that prevents unsupported certainty. Absence of evidence MUST NOT be presented as proof of absence unless collection scope, source coverage, and review support that statement.

## Correction, Supersession, and Recall

Finding support records MUST support correction, supersession, and recall when evidence or interpretation changes.

Corrections, supersessions, and recalls SHOULD preserve:

- original finding identifier;
- original support record;
- corrected or superseding finding identifier;
- reason for correction, supersession, or recall;
- evidence references that changed;
- reviewer and approver context where required;
- affected report, notification, case, approval, or release scope;
- customer notification path where required;
- audit reference and correlation identifiers.

Corrections MUST be appended as new records or controlled updates. Prior support records MUST NOT be silently rewritten or deleted when they are required for replay, dispute handling, or governance review.

## Audit and Replay Requirements

Audit replay should be able to reconstruct:

- which finding, statement, recommendation, timeline item, conclusion, or report section was created;
- who or what created, modified, reviewed, approved, released, corrected, superseded, or recalled it;
- which tenant, customer, case, workflow, evidence, and retrieval scope applied;
- which evidence references and derived artifacts supported each material statement;
- which claims were unsupported, contextual, partially supported, evidence-supported, or examiner-validated;
- which limitations, conflicts, assumptions, stale inputs, or missing evidence were known;
- which agent, model route, prompt package, tool, parser, enrichment source, or transformation process contributed to the draft or support mapping;
- which Agent Judge checks evaluated support and what they found;
- which human review, examiner review, approval, policy decision, enforcement, release, correction, supersession, or recall records applied;
- which final state was reached.

Audit replay does not prove that a finding was correct. It proves that evidence support, interpretation, review, approval, release, correction, and final disposition can be reconstructed, inspected, challenged, and correlated.

## Fail-Closed Conditions

Governed workflows MUST fail closed, quarantine, or route to controlled review when:

- a material statement lacks a valid support level;
- a finding marked as evidence-supported lacks resolvable evidence references;
- an evidence reference is missing, ambiguous, stale, inaccessible, unauthorized, inconsistent, or unauditable;
- tenant, customer, case, workspace, source, evidence, retention, legal hold, or allowed-use scope is missing or mismatched;
- retrieved context crosses tenant, customer, case, evidence, memory, retention, or allowed-use boundaries;
- a derived artifact lacks required source evidence, transformation, parser, enrichment, model, or version context;
- an agent-generated draft cites fabricated, inaccessible, unrelated, or out-of-scope evidence;
- unsupported, contextual, partially supported, disputed, or unreviewed statements are being prepared for release as confirmed findings;
- severity, impact, root cause, attribution, exfiltration, containment, remediation, closure, or DFIR conclusion claims lack required support or review;
- conflicting evidence or material limitations are suppressed or omitted;
- Agent Judge output is being treated as approval, evidence, or examiner validation;
- human review, examiner review, formal approval, or customer approval is required but missing, expired, revoked, incomplete, or out of scope;
- policy decision or PEP enforcement context is required but unavailable;
- audit logging fails where finding support traceability is mandatory.

Fail-closed handling MUST preserve the original request, finding draft, evidence references, missing or failed control, scope context, review or approval requirement, routing reason, and audit reference.

## Operational Anti-Patterns

Avoid the following:

- treating model confidence as evidence support;
- allowing fluent narratives to replace evidence references;
- presenting hypotheses as confirmed findings;
- citing screenshots, dashboards, summaries, or retrieved snippets without preserving underlying evidence references where required;
- reusing findings from another tenant, customer, case, workspace, or report without explicit authorization and support validation;
- using old evidence references after a case, retention, legal hold, or release scope changes;
- suppressing conflicting evidence or limitations to make a finding appear stronger;
- treating Agent Judge output as approval or examiner validation;
- treating human review as formal approval;
- treating evidence support as authorization for containment, remediation, notification, release, or closure;
- allowing agents to fabricate, repair, or infer missing citations;
- silently rewriting released findings rather than appending correction, supersession, or recall records;
- failing open when evidence support, review, approval, or audit context is missing.

## Relationship to Other Control Areas

Finding support depends on records and controls from other governance domains:

- [`evidence-traceability-model.md`](evidence-traceability-model.md) defines the evidence lifecycle, relationship model, source-to-finding traceability, and evidence boundaries.
- [`evidence-reference-requirements.md`](evidence-reference-requirements.md) defines evidence identifiers, evidence reference fields, attribution metadata, and reference validation.
- [`dfir-evidence-handling.md`](dfir-evidence-handling.md) defines DFIR evidence handling, derived artifact handling, examiner review, and report-drafting controls.
- [`evidence-audit-replay.md`](evidence-audit-replay.md) defines audit and replay requirements for evidence access, derived artifacts, finding support, review, approval, release, and recall.
- [`../data-ingestion/readme.md`](../data-ingestion/readme.md) defines source metadata, normalization, enrichment, failure handling, and ingestion replay.
- [`../tool-access/readme.md`](../tool-access/readme.md) defines tool registration, restricted tool use, scoped execution, and tool audit expectations.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines policy decision, enforcement, approval policy, and fail-closed behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) defines human review, formal approval, customer approval, escalation, and review record expectations.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, evidence, and cross-tenant boundary controls.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines private/local LLM-assisted DFIR evidence, review, and replay boundaries.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines audit event, replayability, correlation, failure audit, and immutable audit expectations.
- [`../governance-library/ai-assurance/readme.md`](../governance-library/ai-assurance/readme.md) defines Agent Judge contracts, unsupported-claim checks, evidence-support checks, output-quality checks, and limitations.

## Acceptance Criteria

Finding support is acceptable when:

- each material finding statement has evidence support, contextual labeling, limitation handling, or documented removal;
- evidence support levels remain separate from release status, approval status, policy decisions, and tool execution;
- tenant identity and customer identity remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- findings preserve case, workflow, source, evidence, derived artifact, transformation, retention, allowed-use, and audit context where applicable;
- evidence references are resolvable by authorized review and replay processes;
- source evidence remains distinguishable from derived artifacts, agent summaries, timelines, and report drafts;
- unsupported, contextual, partially supported, disputed, or unreviewed statements cannot be released as confirmed findings;
- severity, impact, root cause, attribution, exfiltration, containment, remediation, closure, and DFIR conclusion claims receive appropriate support and review;
- Agent Judge output is treated as assurance only;
- human review, examiner review, formal approval, customer approval, PDP decisions, and PEP enforcement remain separate control steps;
- customer-facing outputs are linked to evidence support, review, approval where required, release scope, and audit records;
- correction, supersession, and recall records preserve prior findings and changed evidence context;
- audit replay can reconstruct finding creation, evidence support, agent participation, assurance checks, review, approval, release, correction, and final disposition;
- governed workflows fail closed or route to controlled review when support, scope, review, approval, policy, or audit context is missing, ambiguous, unauthorized, stale, inconsistent, or unauditable.
