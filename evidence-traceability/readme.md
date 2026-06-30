# Evidence Traceability

## Purpose

This directory defines evidence traceability expectations for governed agentic security operations across MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

Evidence traceability ensures that findings, recommendations, timelines, analyst notes, approval packages, reports, and agent-assisted outputs can be linked back to source evidence, evidence-derived artifacts, review records, and audit records.

This directory defines architecture and governance expectations. It does not define a production evidence repository, legal sufficiency, chain-of-custody implementation, forensic tool validation, customer-specific evidence procedures, or environment-specific operational runbooks.

## Scope

This directory applies to evidence handling and traceability for:

- security alerts, detections, incidents, investigations, tickets, and case records;
- telemetry-derived evidence from SIEM, XDR, EDR, NDR, cloud, SaaS, identity, email, firewall, endpoint, and business-application sources;
- forensic artifacts, disk images, memory captures, packet captures, logs, exports, screenshots, files, metadata, and derived artifacts;
- private/local LLM-assisted DFIR workflows that parse, extract, summarize, timeline, or draft reports from evidence;
- findings, recommendations, conclusions, severity changes, escalation decisions, closure recommendations, and customer-facing report content;
- evidence references used by agents, Agent Judges, human reviewers, approvers, policy decisions, and audit replay.

This directory does not replace `data-ingestion/`, `tool-access/`, `policy-enforcement/`, `human-oversight/`, `tenant-isolation/`, `local-llm-dfir/`, or `audit-replay/`. Evidence traceability supplies evidence context that those control areas consume.

## Core Principles

- Evidence-derived outputs are not original evidence.
- Agent-generated summaries, timelines, explanations, and reports must remain traceable to evidence references.
- Findings must identify supporting evidence, unsupported assumptions, uncertainty, and limitations.
- Original evidence must remain immutable or protected by the applicable evidence-handling process.
- Derived artifacts must be distinguishable from source evidence.
- Evidence references should be used instead of copying raw evidence into prompts, audit logs, reports, or approval records unless the evidence-handling model explicitly permits it.
- Tenant, customer, case, matter, workspace, source, retention, and access boundaries must be preserved.
- Evidence handling must not rely on model memory, unverified retrieval, or narrative explanation alone.
- Human review, examiner review, and formal approval remain separate from agent output and Agent Judge output.
- Customer-facing findings and DFIR conclusions require evidence support, review, approval where required, and audit replay.
- Missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, or unauditable evidence context must fail closed where governed workflow behavior depends on it.

## Directory Contents

| File | Purpose |
|---|---|
| [`evidence-traceability-model.md`](evidence-traceability-model.md) | Defines the evidence traceability model, evidence lifecycle, source-to-finding linkage, and control boundaries. |
| [`evidence-reference-requirements.md`](evidence-reference-requirements.md) | Defines required evidence reference fields, evidence identifiers, attribution metadata, and relationship records. |
| [`finding-support-requirements.md`](finding-support-requirements.md) | Defines evidence support requirements for findings, recommendations, reports, conclusions, and customer-facing outputs. |
| [`dfir-evidence-handling.md`](dfir-evidence-handling.md) | Defines DFIR evidence handling expectations for local/private analysis, derived artifacts, examiner review, and report drafting. |
| [`evidence-audit-replay.md`](evidence-audit-replay.md) | Defines audit and replay requirements for evidence access, evidence references, derived artifacts, finding support, and release decisions. |

## Governed Evidence Workflow

| Stage | Requirement |
|---|---|
| Evidence identification | The source, collection context, tenant, customer, case, and evidence type must be identified before evidence is used in governed workflows. |
| Evidence registration | Evidence objects or evidence references must receive stable identifiers and attribution metadata. |
| Scope validation | Tenant, customer, case, workspace, source, retention, legal hold, and allowed-use scope must be validated before access or downstream use. |
| Access mediation | Evidence access must occur through approved workflows, tools, repositories, or examiner processes with scoped identity and audit coverage. |
| Derived artifact creation | Parsed, extracted, normalized, summarized, timeline, or report-draft artifacts must preserve links to source evidence and transformation context. |
| Finding construction | Findings and recommendations must cite supporting evidence references and identify gaps, uncertainty, or assumptions. |
| Assurance checks | Agent Judges or AI assurance checks may evaluate evidence support, unsupported claims, tenant boundaries, and output quality as assurance only. |
| Human review | Analysts, investigators, or examiners must review high-impact findings, evidence interpretation, and unresolved uncertainty where required. |
| Approval and release | Customer-facing reports, evidence releases, sensitive findings, or DFIR conclusions must follow the required approval path. |
| Audit replay | Audit records must reconstruct evidence access, derived artifacts, findings, review, approval, release, correction, and final disposition. |

## Required Evidence Context

Governed evidence records should preserve the following fields where applicable.

| Field | Requirement | Purpose |
|---|---|---|
| `evidence_object_id` | MUST | Unique identifier for the evidence object or controlled evidence reference. |
| `evidence_reference_id` | MUST when evidence is cited or consumed downstream | Stable reference used by findings, reports, approvals, and audit replay. |
| `evidence_type` | MUST | Identifies log, alert, file, image, memory capture, packet capture, export, screenshot, artifact, timeline item, or derived artifact type. |
| `source_system_id` | MUST when evidence originates from a source system | Identifies the originating platform, tool, repository, or data source. |
| `source_record_id` | MUST when available | Preserves source-level traceability. |
| `source_timestamp` | MUST when available | Records when the source event or artifact was created. |
| `collection_timestamp` | MUST | Records when evidence was collected, received, acquired, exported, or registered. |
| `collector_identity` | MUST | Identifies the collector, examiner, connector, workflow, or service identity. |
| `collection_method` | SHOULD | Identifies API, export, forensic acquisition, connector, agent, manual upload, or other collection method. |
| `hash_or_manifest_reference` | MUST when integrity validation applies | References hash, manifest, or integrity record without duplicating evidence. |
| `chain_of_custody_record_id` | MUST when chain-of-custody applies | Links evidence use to the applicable custody record. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when evidence is tied to an investigation, incident, ticket, escalation, report, or DFIR matter | Links evidence to the governed case. |
| `workflow_id` | MUST for governed workflows | Links evidence use to workflow state. |
| `workspace_id` | MUST when workspace scope affects evidence access, interpretation, or routing | Preserves SIEM, XDR, cloud, logging, or case-workspace boundary. |
| `data_classification` | MUST when sensitivity affects access, handling, retention, approval, or release | Preserves handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, customer, or forensic handling label. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use for investigation, reporting, DFIR, approval, customer communication, or governance review. |
| `retention_policy_id` | MUST when retention affects evidence, derived artifacts, or references | Preserves retention and disposal boundary. |
| `legal_hold_id` | MUST when applicable | Links evidence handling to legal hold or preservation requirements. |
| `access_scope` | MUST when access is role-, case-, customer-, or workflow-bound | Defines who or what may access the evidence reference or derived artifact. |
| `derived_artifact_id` | MUST when evidence is transformed, extracted, summarized, or timelined | Identifies the derived artifact separately from original evidence. |
| `transformation_record_id` | MUST when transformation affects interpretation | Links derived artifacts to parsing, extraction, summarization, normalization, enrichment, or timeline logic. |
| `finding_id` | MUST when evidence supports a finding | Links evidence to the finding or recommendation it supports. |
| `report_section_id` | SHOULD when evidence supports report content | Links evidence to the specific report section, timeline entry, or conclusion. |
| `agent_id` | MUST when an agent accessed, summarized, cited, or used the evidence | Identifies agent participation. |
| `agent_session_id` or `run_id` | MUST when an agent accessed, summarized, cited, or used the evidence | Supports replay of agent-assisted evidence use. |
| `review_record_id` | MUST when human or examiner review is required | Links evidence interpretation to review. |
| `approval_record_id` | MUST when evidence release or customer-facing use requires approval | Links evidence use to formal approval. |
| `audit_reference_id` | MUST for governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links evidence, findings, cases, tools, policy decisions, approvals, reports, and audit records. |

## Evidence Support Levels

Findings, recommendations, and report statements should identify their evidence support level.

| Support Level | Description | Required Handling |
|---|---|---|
| `UNSUPPORTED` | Statement has no valid evidence reference or relies only on model output, memory, or assumption. | Must not be released as a finding. Route for correction or review. |
| `CONTEXTUAL` | Statement is supported by background context but not direct case evidence. | May be used as context if clearly labeled and not presented as a case finding. |
| `PARTIALLY_SUPPORTED` | Some evidence supports the statement, but gaps, conflicts, uncertainty, or missing sources remain. | Requires limitation notes and review before downstream use. |
| `EVIDENCE_SUPPORTED` | Statement is linked to relevant evidence references and derived artifacts. | May proceed to review and approval path where required. |
| `EXAMINER_VALIDATED` | Evidence interpretation has been reviewed by an accountable analyst, investigator, or examiner. | May support higher-impact conclusions subject to policy, approval, and release controls. |

Evidence support does not by itself authorize containment, remediation, evidence release, case closure, customer notification, or final DFIR conclusions.

## Agent Use of Evidence

Agents may assist with evidence-aware work when governed workflow controls permit it.

Agents may:

- retrieve scoped evidence references;
- summarize evidence-derived content;
- draft timelines from evidence references;
- identify missing evidence, conflicting evidence, or unsupported claims;
- prepare evidence support tables for analyst review;
- draft findings, recommendations, report sections, and approval packages with evidence references;
- route uncertainty, evidence gaps, and scope mismatches to review.

Agents must not:

- treat their own output as original evidence;
- modify, delete, overwrite, or silently replace evidence;
- fabricate evidence references or cite inaccessible evidence;
- access evidence outside approved tenant, customer, case, workspace, source, or retention scope;
- convert unsupported assumptions into findings;
- represent summaries as chain-of-custody records, examiner conclusions, legal determinations, or forensic proof;
- approve evidence release, customer-facing findings, containment, remediation, closure, or legal conclusions;
- bypass evidence validation, human review, approval, policy enforcement, or audit replay.

## Evidence Boundaries

| Boundary | Requirement |
|---|---|
| Source evidence boundary | Original evidence must remain distinguishable from parsed, summarized, enriched, or report-ready artifacts. |
| Derived artifact boundary | Derived artifacts must preserve source evidence references, transformation context, version, and limitations. |
| Tenant and customer boundary | Evidence must not be joined, reused, disclosed, or released across tenant or customer boundaries without explicit authorization. |
| Case boundary | Evidence must remain linked to the case, matter, investigation, ticket, or DFIR engagement for which it was collected or approved. |
| Chain-of-custody boundary | Chain-of-custody records must remain separate from agent summaries, audit records, and report drafts. |
| Retrieval boundary | RAG, vector search, case memory, customer context, and evidence retrieval must remain scoped to approved evidence and allowed use. |
| Output boundary | Findings, reports, timelines, and notifications must reference evidence support and follow review and approval requirements. |
| Retention boundary | Evidence and evidence references must follow retention, legal hold, customer, and case requirements. |

## DFIR Evidence Handling

Private/local LLM-assisted DFIR workflows must preserve evidence integrity and examiner accountability.

DFIR evidence handling must ensure that:

- forensic artifacts remain separate from extracted, parsed, summarized, or report-draft artifacts;
- local execution is treated as an execution and evidence-handling context, not proof of correctness;
- extracted indicators, timelines, file metadata, memory findings, packet observations, and artifact summaries preserve source evidence references;
- prompt packages, model routes, parsing tools, extraction tools, and transformation versions are recorded where they affect evidence interpretation;
- examiner review is required for forensic conclusions, customer-facing DFIR findings, and unresolved conflicts;
- evidence release follows the appropriate customer, legal, contractual, and approval path.

## Finding and Report Requirements

Findings, recommendations, timelines, and report sections must preserve enough evidence context for review and replay.

Each governed finding should identify:

- finding identifier;
- case identifier;
- tenant and customer scope;
- evidence references supporting the finding;
- derived artifacts used to interpret the evidence;
- evidence support level;
- uncertainty, limitations, or conflicting evidence;
- reviewer or examiner record where required;
- approval record where required;
- release scope and output destination where applicable;
- audit reference and correlation identifiers.

Customer-facing reports must not present unsupported, partially supported, or unreviewed statements as confirmed findings.

## Evidence Audit and Replay

Evidence audit replay should be able to reconstruct:

- which evidence objects or references were accessed;
- who or what accessed them;
- which tenant, customer, case, workspace, workflow, and evidence scope applied;
- which source systems, collection methods, timestamps, and integrity records were used;
- which derived artifacts were created;
- which agents, tools, prompts, model routes, or local analysis steps consumed evidence;
- which findings, recommendations, report sections, approval packages, or customer-facing outputs used the evidence;
- which unsupported claims, limitations, conflicts, or evidence gaps were identified;
- which human review, examiner review, approval, release, correction, or recall records applied;
- which final state was reached.

Audit replay does not prove that a finding was correct. It proves that evidence use, interpretation path, review, approval, release, and final disposition can be reconstructed and challenged.

## Fail-Closed Conditions

Governed workflows must fail closed, quarantine, or route to controlled review when:

- required evidence references are missing, ambiguous, stale, inaccessible, inconsistent, or unauditable;
- evidence tenant, customer, case, workspace, source, or retention scope is missing or mismatched;
- evidence integrity metadata, hash reference, manifest reference, or chain-of-custody reference is required but unavailable;
- an agent-generated output cites evidence that cannot be resolved;
- a finding is unsupported or only partially supported but is being prepared for release as a confirmed finding;
- retrieved context crosses tenant, customer, case, evidence, retention, or allowed-use boundaries;
- raw evidence is copied into prompts, logs, reports, audit records, or shared knowledge stores without authorization;
- evidence-derived output attempts to imply approval, legal conclusion, forensic proof, containment success, remediation success, closure, or customer notification without required controls;
- human review, examiner review, approval, or customer approval is required but missing, expired, revoked, incomplete, or out of scope;
- audit logging fails where evidence traceability is mandatory.

Fail-closed handling must preserve the original request, evidence references, missing or failed control, scope context, reviewer or approver requirement, routing reason, and audit reference.

## Operational Anti-Patterns

Avoid the following:

- treating model output, analyst narrative, or retrieved context as original evidence;
- releasing findings without evidence references;
- citing dashboards, summaries, or screenshots without preserving the underlying evidence reference where required;
- copying raw evidence into audit logs or prompts when references are sufficient;
- mixing evidence across tenants, customers, cases, matters, or retention scopes without explicit authorization;
- allowing agents to modify, delete, recategorize, or replace original evidence;
- allowing unsupported claims to become findings through repeated summarization;
- treating Agent Judge output as approval or examiner validation;
- treating local/private execution as proof of evidentiary validity;
- using evidence-derived summaries to replace chain-of-custody records;
- releasing customer-facing conclusions without review, approval, and evidence support;
- silently correcting findings instead of appending correction, supersession, or recall records.

## Relationship to Other Control Areas

Evidence traceability depends on records and controls from other governance domains:

- [`../data-ingestion/readme.md`](../data-ingestion/readme.md) defines source metadata, normalization, enrichment, failure handling, and ingestion replay.
- [`../tool-access/readme.md`](../tool-access/readme.md) defines tool registration, restricted tool use, scoped execution, and tool audit expectations.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines PDP, PEP, policy decision, approval policy, and fail-closed behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) defines review, formal approval, customer approval, escalation, and review record expectations.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, and cross-tenant boundary controls.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines private/local LLM-assisted DFIR boundaries, evidence handling, review workflow, and replay considerations.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines audit event, replayability, correlation, exception, failure, and immutable audit expectations.
- [`../governance-library/ai-assurance/readme.md`](../governance-library/ai-assurance/readme.md) defines Agent Judge contracts, unsupported-claim checks, evidence-support checks, output-quality checks, and limitations.

## Acceptance Criteria

Evidence traceability is acceptable when:

- evidence objects and evidence references have stable identifiers;
- source evidence remains distinguishable from derived artifacts, summaries, findings, timelines, and report drafts;
- tenant identity and customer identity are preserved separately for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- evidence use remains scoped to approved tenant, customer, case, workspace, source, retention, allowed-use, and access boundaries;
- findings, recommendations, timelines, and report statements identify supporting evidence references and limitations;
- unsupported claims cannot be released as findings;
- agent outputs, Agent Judge results, and analyst notes do not replace original evidence, chain-of-custody records, human review, examiner review, approval, or audit records;
- DFIR evidence handling preserves source evidence references, derived artifact lineage, examiner review, and release controls;
- customer-facing outputs link to evidence support, review, approval, release scope, and audit records where required;
- evidence audit replay can reconstruct evidence access, derived artifacts, findings, review, approval, release, correction, recall, and final disposition;
- fail-closed handling exists for missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, unsupported, or unauditable evidence context.
