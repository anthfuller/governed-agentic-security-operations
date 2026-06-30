# Evidence Audit Replay

## Purpose

This document defines audit and replay requirements for evidence access, evidence references, derived artifacts, finding support, review, approval, release, correction, and final disposition in governed agentic security operations.

Evidence audit replay ensures that evidence use can be reconstructed across Managed SOC / MSSP, MDR, cloud incident response, and private/local LLM-assisted DFIR workflows without relying on model memory, informal notes, or unverifiable narrative summaries.

Evidence audit replay does not prove that a finding, recommendation, or DFIR conclusion was correct. It proves that evidence use, interpretation path, review, approval, release, correction, and final disposition can be inspected, correlated, challenged, and reconstructed.

This document defines architecture and governance expectations. It does not define a production evidence repository, legally sufficient chain-of-custody implementation, forensic tool validation program, customer-specific evidence procedure, or operational runbook.

## Scope

This document applies to audit and replay requirements for:

- evidence registration, access, retrieval, and reference use;
- source evidence, evidence copies, working copies, derived artifacts, timelines, summaries, and report drafts;
- evidence transformation, including parsing, extraction, normalization, enrichment, summarization, timeline generation, redaction, and report drafting;
- evidence support for findings, recommendations, severity changes, escalation decisions, closure recommendations, and report sections;
- agent-assisted evidence use, Agent Judge evidence-support checks, unsupported-claim checks, and boundary checks;
- human review, examiner review, approval, release, correction, supersession, recall, and closure records;
- private/local LLM-assisted DFIR workflows that use evidence references, retrieved context, case memory, vector search, or local analysis tools;
- audit records that link evidence use to tenant, customer, case, workflow, policy, approval, tool, model, retrieval, and release context.

This document does not replace the evidence repository, chain-of-custody process, legal review, customer authority model, policy decision contract, tool-access model, or general audit-replay model.

## Core Principles

- Evidence audit replay records how evidence was used. It does not make an unsupported finding correct.
- Evidence-derived outputs are not original evidence.
- Audit records should reference evidence rather than copy raw evidence content unless the evidence-handling model explicitly permits copying.
- Source evidence, working copies, derived artifacts, summaries, timelines, findings, and report drafts must remain distinguishable.
- Tenant, customer, case, matter, workspace, source, retention, legal hold, and access boundaries must be preserved during replay.
- Chain-of-custody records remain separate from audit records, agent summaries, review notes, and report drafts.
- Agent output, retrieved context, and Agent Judge output are not evidence authority, examiner review, formal approval, customer approval, or release approval.
- Findings and report statements must be traceable to supporting evidence references, derived artifacts, reviewer records, approval records where required, and audit records.
- Corrections, supersessions, recalls, and reversals should be appended as new records rather than silently rewriting prior records.
- Missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, integrity-failed, unsupported, or unauditable evidence context must fail closed where governed workflow behavior depends on it.

## Evidence Replay Objectives

Evidence audit replay should be able to answer the following questions.

| Objective | Replay Question |
|---|---|
| Evidence origin | What evidence object, source system, collection method, timestamp, collector, and integrity reference were involved? |
| Evidence scope | Which tenant, customer, case, matter, workspace, source, retention, legal hold, access, and allowed-use boundaries applied? |
| Evidence access | Who or what accessed the evidence, through which workflow, tool, identity, policy decision, and approval path where required? |
| Evidence transformation | Which parser, tool, model route, prompt package, transformation record, schema version, or enrichment source produced a derived artifact? |
| Evidence support | Which evidence references and derived artifacts supported each finding, recommendation, timeline entry, or report section? |
| Evidence gaps | Which limitations, missing evidence, conflicts, unsupported claims, or unresolved uncertainty were identified? |
| Review and approval | Which analyst, investigator, examiner, reviewer, approver, or customer approval path reviewed or approved evidence use where required? |
| Release and downstream use | Which evidence, derived artifacts, report sections, approval packages, notifications, or release records consumed the evidence context? |
| Correction and recall | Which finding, artifact, report section, release, or evidence interpretation was corrected, superseded, recalled, or reversed? |
| Final disposition | What final state was reached and which records prove the path without relying on model memory? |

## Evidence Audit Event Types

Evidence audit replay should preserve structured events for the evidence lifecycle.

| Event Type | Purpose |
|---|---|
| `EVIDENCE_REGISTERED` | Records evidence object or evidence reference creation. |
| `EVIDENCE_ACCESS_REQUESTED` | Records a request to access, retrieve, view, parse, copy, export, summarize, or transform evidence. |
| `EVIDENCE_ACCESS_ALLOWED` | Records policy, scope, identity, approval, or workflow context that permitted access. |
| `EVIDENCE_ACCESS_DENIED` | Records denied, blocked, expired, out-of-scope, or failed-closed access. |
| `EVIDENCE_REFERENCE_USED` | Records evidence reference use in a finding, timeline, summary, report draft, review, approval package, or audit record. |
| `WORKING_COPY_CREATED` | Records creation of a controlled working copy for analysis or DFIR workflow use. |
| `EVIDENCE_TRANSFORMED` | Records parsing, extraction, normalization, enrichment, summarization, timeline creation, redaction, or report-draft transformation. |
| `DERIVED_ARTIFACT_CREATED` | Records creation of an artifact derived from source evidence or working copies. |
| `RETRIEVED_CONTEXT_USED` | Records evidence retrieval, RAG, vector search, case memory, customer context, or shared memory use. |
| `FINDING_SUPPORT_EVALUATED` | Records evidence-support assessment for findings, recommendations, report sections, or conclusions. |
| `UNSUPPORTED_CLAIM_DETECTED` | Records unsupported, weakly supported, conflicting, or out-of-scope statements requiring correction or review. |
| `EVIDENCE_GAP_IDENTIFIED` | Records missing source evidence, incomplete collection, unavailable artifacts, time gaps, or interpretation limitations. |
| `EVIDENCE_REVIEW_COMPLETED` | Records analyst, investigator, examiner, or human review of evidence use or interpretation. |
| `EVIDENCE_APPROVAL_RECORDED` | Records formal approval related to evidence release, customer-facing use, sensitive conclusion, or downstream action. |
| `EVIDENCE_RELEASED` | Records release, export, report inclusion, customer communication, or approved downstream consumption. |
| `EVIDENCE_CORRECTION_APPENDED` | Records correction to evidence interpretation, attribution, support level, report wording, or derived artifact handling. |
| `EVIDENCE_SUPERSEDED` | Records that a derived artifact, finding, report section, or interpretation has been replaced by a later controlled record. |
| `EVIDENCE_RECALLED` | Records recall or withdrawal of released evidence-derived content, finding support, report section, or package. |
| `EVIDENCE_REPLAY_REQUESTED` | Records a replay request and the scope of reconstruction. |
| `EVIDENCE_REPLAY_COMPLETED` | Records completed replay, reconstructed chain, limitations, and unresolved gaps. |
| `EVIDENCE_REPLAY_FAILED` | Records replay failure, missing records, broken linkage, access denial, or retention/legal-hold conflict. |

## Required Evidence Audit Record

Evidence audit events should preserve enough structured context for correlation, review, and replay.

| Field | Requirement | Purpose |
|---|---|---|
| `evidence_audit_event_id` | MUST | Unique identifier for the evidence audit event. |
| `event_type` | MUST | Identifies the evidence audit event type. |
| `event_time_utc` | MUST | Records the trusted event timestamp. |
| `correlation_id` | MUST | Links the event to the end-to-end workflow or case path. |
| `parent_event_id` | SHOULD when available | Links the event to the prior event in the evidence chain. |
| `causation_id` | SHOULD when available | Identifies the event, request, decision, approval, or failure that caused this event. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when evidence is tied to an investigation, incident, ticket, escalation, report, or DFIR matter | Links evidence use to the governed case. |
| `matter_id` | SHOULD when legal, DFIR, or customer procedure uses a separate matter identifier | Preserves matter-specific evidence context. |
| `workflow_id` | MUST for governed workflows | Links evidence use to workflow state. |
| `workflow_stage` | MUST when access, review, approval, routing, or release depends on workflow stage | Preserves stage-specific replay context. |
| `workspace_id` | MUST when workspace scope affects evidence access, interpretation, or routing | Preserves SIEM, XDR, cloud, logging, or case-workspace boundary. |
| `source_system_id` | MUST when evidence originates from a source system | Identifies the source platform, repository, tool, connector, or evidence store. |
| `source_record_id` | MUST when available | Preserves source-level traceability. |
| `source_timestamp` | MUST when available | Records when the source event or artifact was created. |
| `collection_timestamp` | MUST when evidence was collected, received, exported, acquired, or registered | Records evidence collection or registration time. |
| `collector_identity` | MUST when evidence collection or registration occurred | Identifies the collector, examiner, connector, workflow, or service identity. |
| `evidence_object_ids` | MUST when evidence is accessed, referenced, transformed, reviewed, approved, released, or corrected | Identifies controlled evidence objects. |
| `evidence_reference_ids` | MUST when evidence is cited or consumed downstream | Identifies stable evidence references used by findings, approvals, reports, and replay. |
| `evidence_type` | MUST when applicable | Identifies log, alert, file, image, memory capture, packet capture, export, screenshot, artifact, timeline item, or derived artifact type. |
| `hash_or_manifest_reference` | MUST when integrity validation applies | Links to hash, manifest, signature, or integrity record without duplicating raw evidence. |
| `chain_of_custody_record_id` | MUST when chain-of-custody applies | Links evidence use to custody tracking without treating audit replay as custody. |
| `data_classification` | MUST when sensitivity affects access, handling, retention, approval, or release | Preserves handling context. |
| `sensitivity_label` | MUST when applicable | Preserves customer, privacy, legal, forensic, or operational sensitivity context. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted investigation, reporting, approval, customer communication, governance, or legal use. |
| `retention_policy_id` | MUST when retention affects evidence, derived artifacts, or references | Preserves retention and disposal boundary. |
| `legal_hold_id` | MUST when applicable | Links evidence handling to legal hold or preservation requirements. |
| `access_scope` | MUST when access is role-, case-, customer-, tenant-, examiner-, or workflow-bound | Defines who or what may access evidence references or derived artifacts. |
| `requesting_identity` | MUST when access, retrieval, transformation, release, or replay is requested | Identifies authenticated user, service, workflow, tool, or agent identity. |
| `actor_role` | SHOULD when available | Identifies analyst, investigator, examiner, approver, service, workflow, or agent role. |
| `agent_id` | MUST when an agent accessed, summarized, cited, transformed, evaluated, or used evidence | Identifies agent participation. |
| `agent_session_id` or `run_id` | MUST when an agent accessed, summarized, cited, transformed, evaluated, or used evidence | Supports run-level replay. |
| `tool_id` | MUST when a tool accessed, retrieved, copied, transformed, exported, or released evidence | Identifies the tool involved. |
| `tool_version` | MUST when tool version affects evidence handling, interpretation, or replay | Supports repeatability and dispute review. |
| `parser_id` | MUST when parsing is applied | Identifies parser logic. |
| `parser_version` | MUST when parsing affects interpretation, replay, or report content | Supports parser accountability and regression review. |
| `schema_version` | MUST when normalized or structured evidence-derived records are produced | Identifies output schema used downstream. |
| `transformation_record_id` | MUST when evidence is parsed, extracted, normalized, enriched, summarized, timelined, redacted, or report-drafted | Links evidence use to transformation details. |
| `parser_or_transformation_version` | MUST when transformation affects field meaning, interpretation, replay, or downstream use | Supports transformation traceability. |
| `derived_artifact_ids` | MUST when derived artifacts are created or consumed | Identifies artifacts derived from source evidence or working copies. |
| `model_route_id` | MUST when model output affects interpretation, support assessment, timeline drafting, report drafting, or downstream use | Identifies the model route used. |
| `prompt_package_id` | MUST when prompts affect evidence interpretation or report drafting | Supports replay of model-assisted evidence use. |
| `knowledge_store_or_memory_scope` | MUST when retrieval, RAG, vector search, shared memory, case memory, customer context, or evidence retrieval is used | Defines approved retrieval and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval remained within approved evidence, tenant, customer, case, retention, freshness, and reuse boundaries. |
| `retrieved_context_reference_ids` | MUST when retrieved context influences evidence interpretation or downstream use | Identifies retrieved context without uncontrolled reuse. |
| `finding_id` | MUST when evidence supports or refutes a finding | Links evidence to the finding or recommendation. |
| `report_section_id` | SHOULD when evidence supports report content | Links evidence to a timeline entry, report section, or conclusion. |
| `evidence_support_level` | MUST when finding support is evaluated | Records unsupported, contextual, partially supported, evidence-supported, or examiner-validated status. |
| `limitations` | MUST where material | Records missing evidence, partial collection, time gaps, stale data, conflicting evidence, unsupported claims, or tool limitations. |
| `review_record_id` | MUST when human review is required | Links evidence interpretation to accountable review. |
| `examiner_review_record_id` | MUST when examiner review is required | Links DFIR evidence interpretation to examiner validation. |
| `approval_record_id` | MUST when evidence release, customer-facing use, sensitive finding, or downstream action requires approval | Links evidence use to scoped approval. |
| `policy_decision_id` | MUST when policy governed evidence access, release, routing, or downstream use | Links evidence use to the Policy Decision Point decision. |
| `pep_enforcement_id` | MUST when a Policy Enforcement Point enforced access, release, routing, or downstream use | Links the event to enforcement. |
| `release_record_id` | MUST when evidence-derived content is released or exported | Links release to evidence, review, approval, and scope. |
| `output_destination` | MUST when evidence-derived content is routed, exported, published, released, indexed, or consumed downstream | Identifies the destination and release boundary. |
| `status` | MUST | Records allowed, denied, blocked, quarantined, failed closed, released, corrected, superseded, recalled, completed, or failed state. |
| `audit_reference_id` | MUST for governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links evidence, workflow, case, tool, model, review, approval, policy, release, correction, and audit records. |

## Evidence Replay Chain

A replayable evidence chain should preserve the following sequence where applicable.

| Stage | Replay Requirement |
|---|---|
| Evidence identification | Reconstruct how the evidence object or evidence reference was identified and why it was in scope. |
| Evidence registration | Reconstruct evidence identifiers, source metadata, collection metadata, attribution, classification, integrity, retention, and legal hold context. |
| Scope validation | Reconstruct tenant, customer, case, matter, workspace, source, access, retention, legal hold, and allowed-use validation. |
| Access decision | Reconstruct the identity, policy decision, enforcement result, approval dependency, and access outcome. |
| Tool or workflow use | Reconstruct which tool, workflow, model, prompt package, parser, or local analysis step consumed evidence. |
| Transformation | Reconstruct source evidence, working copies, transformation records, parser/tool/model versions, and derived artifacts. |
| Finding support | Reconstruct how evidence references supported, partially supported, contradicted, or failed to support each finding or report statement. |
| Assurance checks | Reconstruct Agent Judge or AI assurance checks for evidence support, unsupported claims, tenant boundary, retrieval boundary, and output quality. |
| Human or examiner review | Reconstruct reviewer identity, review scope, unresolved issues, corrections, and examiner validation where required. |
| Approval and release | Reconstruct approval authority, approval scope, release scope, output destination, customer-facing use, and expiration or revocation state. |
| Correction, supersession, or recall | Reconstruct why a record changed, which prior record was affected, who reviewed it, what was released or withdrawn, and what final state remains. |

## Evidence Access Replay Requirements

Evidence access replay MUST preserve:

- access request identifier;
- requesting identity, role, workflow, and agent session where applicable;
- evidence object and evidence reference identifiers;
- tenant, customer, case, matter, workspace, source, retention, legal hold, and allowed-use scope;
- requested operation, such as view, retrieve, copy, parse, summarize, transform, export, release, or replay;
- policy decision and enforcement result where policy governs access;
- approval record where approval is required before access or release;
- result status, including allowed, denied, blocked, quarantined, failed closed, or review-required;
- output destination or downstream consumer where access results are routed or consumed;
- audit reference and correlation identifiers.

Evidence access MUST NOT be replayed from model memory, informal notes, or unsupported narrative summaries alone.

## Derived Artifact Replay Requirements

Derived artifacts MUST remain traceable to source evidence and transformation context.

Replay records for derived artifacts MUST preserve:

- source evidence object identifiers;
- working copy identifiers where used;
- derived artifact identifiers;
- transformation record identifier;
- parser, tool, workflow, script, model route, and prompt package identifiers where applicable;
- parser, tool, schema, or transformation version where interpretation or replay depends on it;
- time-zone assumptions, timestamp handling, field mappings, and normalization assumptions where material;
- enrichment source and freshness where enrichment affects interpretation;
- limitations, uncertainty, missing evidence, conflicts, or unsupported claims where material;
- reviewer or examiner record where required;
- approval and release record where the derived artifact is used in customer-facing outputs or sensitive downstream action.

A derived artifact MUST NOT replace source evidence, custody records, examiner validation, or approval records.

## Finding Support Replay Requirements

Findings, recommendations, severity changes, timeline entries, report sections, and conclusions must preserve evidence support context.

Each replayable finding should identify:

- finding identifier;
- case identifier;
- tenant and customer scope;
- supporting evidence reference identifiers;
- derived artifact identifiers used for interpretation;
- evidence support level;
- unsupported assumptions, uncertainty, limitations, and conflicting evidence where applicable;
- Agent Judge or AI assurance result where evidence support was evaluated;
- reviewer or examiner record where required;
- approval record and release record where required;
- audit reference and correlation identifiers.

Unsupported or partially supported statements MUST NOT be released as confirmed findings. They MUST be corrected, labeled, routed to review, or excluded from release according to the governed workflow.

## Private/Local LLM-Assisted DFIR Replay Requirements

Private/local LLM-assisted DFIR workflows MUST preserve replay records for model-assisted evidence use.

Replay MUST capture where applicable:

- evidence references used by the local workflow;
- model route identifier;
- prompt package identifier;
- local tool, parser, extractor, or timeline builder identity and version;
- retrieval scope and retrieved context references;
- `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` when retrieval, RAG, vector search, shared memory, case memory, customer context, or evidence retrieval is used;
- generated summary, timeline, extraction, support table, report draft, or limitation note reference;
- unsupported-claim, evidence-support, tenant-boundary, retrieval-boundary, and output-quality assurance results where performed;
- examiner review record;
- approval and release records where conclusions, evidence-derived artifacts, or report sections are released.

Private or local execution does not prove correctness, evidentiary validity, legal sufficiency, or forensic completeness. Model-assisted outputs remain evidence-derived drafts until examiner review and required approval are complete.

## Review, Approval, and Release Replay

Human review, examiner review, formal approval, customer approval, and release records MUST remain separate.

Replay MUST be able to reconstruct:

- who reviewed evidence use or interpretation;
- what evidence references and derived artifacts were reviewed;
- which limitations, conflicts, or unsupported claims were accepted, corrected, escalated, or excluded;
- whether examiner review was required and completed;
- whether formal approval was required, granted, denied, expired, revoked, or out of scope;
- whether customer approval was required before release or action;
- which evidence-derived content was released, to which destination, under which scope, and under which retention or sensitivity constraints;
- whether a release was later corrected, superseded, recalled, or withdrawn.

A review record MUST NOT be treated as approval unless the approval record explicitly grants scoped approval for the action or release.

## Correction, Supersession, and Recall Replay

Corrections, supersessions, recalls, and reversals MUST preserve prior records and append new records.

A correction, supersession, or recall record SHOULD identify:

- original evidence audit event identifier;
- affected evidence object, evidence reference, derived artifact, finding, report section, release, or approval package;
- reason for correction, supersession, recall, or reversal;
- corrected evidence references or corrected interpretation;
- reviewer or examiner identity;
- approval record where approval is required;
- release or customer notification path where applicable;
- final disposition;
- audit reference and correlation identifiers.

Prior records SHOULD NOT be deleted or silently rewritten to hide errors, unsupported claims, scope mismatches, or release defects.

## Fail-Closed Conditions

Governed evidence workflows MUST fail closed, quarantine, or route to controlled review when:

- required evidence identifiers, evidence references, source metadata, collection metadata, integrity references, custody references, retention records, legal hold records, or access scope are missing, ambiguous, stale, inconsistent, unauthorized, or unauditable;
- tenant, customer, case, matter, workspace, source, host, account, user, evidence, retention, legal hold, or allowed-use attribution is missing or mismatched;
- source evidence, working copies, derived artifacts, summaries, timelines, findings, and report drafts cannot be distinguished;
- evidence hash, manifest, signature, or integrity validation fails where integrity validation applies;
- chain-of-custody is required but unavailable, broken, incomplete, inconsistent, or out of scope;
- a working copy or derived artifact cannot be linked to source evidence;
- an agent, model, tool, parser, or workflow cites evidence that cannot be resolved or is outside approved scope;
- retrieval, RAG, vector search, shared memory, customer context, case memory, or evidence retrieval crosses tenant, customer, case, matter, evidence, workspace, retention, legal hold, freshness, or allowed-use boundaries;
- `knowledge_store_or_memory_scope` is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval affects evidence interpretation or downstream use;
- `knowledge_memory_scope_result` is required but missing, unavailable, inconsistent, stale, or indicates retrieval exceeded approved boundaries;
- parser, tool, schema, model route, prompt package, or transformation version cannot be determined where replay or interpretation depends on it;
- raw evidence is copied into prompts, audit logs, shared memory, vector stores, reports, or approval packages without authorization;
- a finding is unsupported or only partially supported but is being prepared for release as confirmed;
- human review, examiner review, formal approval, customer approval, or release approval is required but missing, expired, revoked, incomplete, or out of scope;
- evidence-derived output attempts to imply forensic proof, legal conclusion, customer notification, containment success, remediation success, closure, or approval without governed workflow context;
- audit logging or audit persistence fails where evidence traceability is mandatory.

Fail-closed handling MUST preserve the original request, evidence references, missing or failed control, scope context, reviewer or approver requirement, routing reason, final disposition, and audit reference.

## Replay Boundaries

Evidence audit replay must preserve governance boundaries while supporting reconstruction.

| Boundary | Requirement |
|---|---|
| Evidence boundary | Audit records should reference evidence without turning audit storage into an unrestricted evidence repository. |
| Custody boundary | Chain-of-custody records should be linked where applicable, but audit replay must not be treated as custody unless explicitly designed for that purpose. |
| Tenant and customer boundary | Replay access must remain scoped to authorized tenants, customers, service roles, and customer authority. |
| Case and matter boundary | Evidence must not be joined, reused, replayed, or released across cases or matters without authorization. |
| Source and workspace boundary | Evidence source, workspace, cloud account, subscription, project, host, user, and system attribution must be preserved where applicable. |
| Retrieval and memory boundary | Retrieved context, vector search, shared memory, case memory, customer context, and evidence retrieval must remain within approved scope. |
| Model boundary | Model output is replay input, not evidence authority or proof of correctness. |
| Review and approval boundary | Review records, examiner records, formal approval, customer approval, and release records must remain distinct. |
| Retention and legal hold boundary | Replay must respect retention, disposal, preservation, legal hold, access-control, and redaction requirements. |

## Audit Storage and Integrity Expectations

Evidence audit records should be structured, protected, access-controlled, and replayable.

Evidence audit storage SHOULD support:

- append-only or tamper-evident records where required;
- stable event identifiers and correlation identifiers;
- canonical event structure for replay;
- access controls aligned to tenant, customer, case, matter, role, and allowed-use scope;
- retention and legal hold handling;
- minimized raw evidence content in audit records;
- protected references to evidence, derived artifacts, review records, approval records, release records, and correction records;
- reconstruction of event order, causation, and final state;
- detection of missing, altered, out-of-order, or inconsistent records.

Sensitive evidence content, credentials, secrets, private keys, tokens, and unnecessary customer data MUST NOT be copied into audit records.

## Operational Anti-Patterns

Avoid the following:

- treating audit replay as proof that a finding, recommendation, or DFIR conclusion is correct;
- treating agent output, retrieved context, dashboards, analyst narrative, summaries, or report language as original evidence;
- copying raw evidence into prompts, audit logs, shared memory, vector stores, reports, or approval packages when controlled references are sufficient;
- allowing agents or tools to modify, delete, overwrite, silently replace, or reclassify source evidence;
- fabricating evidence references or citing inaccessible evidence;
- releasing findings without evidence references, support level, review, approval where required, and release records;
- treating Agent Judge output as examiner review, human approval, customer approval, or release approval;
- treating human review as formal approval without a scoped approval record;
- treating local/private LLM execution as proof of evidentiary validity or forensic completeness;
- mixing evidence across tenants, customers, cases, matters, workspaces, retention scopes, or legal holds without authorization;
- using retrieval, RAG, vector search, shared memory, case memory, customer context, or evidence retrieval outside approved scope;
- silently correcting evidence interpretation instead of appending correction, supersession, or recall records;
- failing open when evidence references, scope, integrity, custody, retrieval, review, approval, or audit context is missing.

## Relationship to Other Control Areas

Evidence audit replay depends on records and controls from other governance domains:

- [`readme.md`](readme.md) defines the evidence traceability directory purpose, core principles, evidence support levels, and evidence workflow.
- [`evidence-traceability-model.md`](evidence-traceability-model.md) defines the broader evidence traceability model.
- [`evidence-reference-requirements.md`](evidence-reference-requirements.md) defines required evidence reference fields and attribution metadata.
- [`finding-support-requirements.md`](finding-support-requirements.md) defines evidence support requirements for findings, recommendations, and report content.
- [`dfir-evidence-handling.md`](dfir-evidence-handling.md) defines DFIR evidence handling, derived artifact, examiner review, correction, and release expectations.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines general audit event, replayability, correlation, exception, failure, and immutable audit expectations.
- [`../data-ingestion/readme.md`](../data-ingestion/readme.md) defines source metadata, normalization, enrichment, ingestion failure handling, and ingestion replay.
- [`../tool-access/readme.md`](../tool-access/readme.md) defines scoped tool execution, restricted tool patterns, MCP-mediated access, and tool audit expectations.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines PDP, PEP, policy decision, approval policy, and fail-closed behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) defines review, formal approval, customer approval, escalation, and review record expectations.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, and cross-tenant boundary controls.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines local/private LLM-assisted DFIR boundaries, evidence handling, review workflow, and replay considerations.

## Acceptance Criteria

Evidence audit replay is acceptable when:

- evidence access, retrieval, transformation, reference use, review, approval, release, correction, supersession, recall, and final disposition emit structured audit records where required;
- source evidence, working copies, derived artifacts, summaries, timelines, findings, and report drafts remain distinguishable during replay;
- evidence object identifiers, evidence reference identifiers, source metadata, collection metadata, integrity references, custody references where applicable, and attribution metadata are preserved;
- tenant identity and customer identity remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- evidence use remains scoped to approved tenant, customer, case, matter, workspace, source, retention, legal hold, allowed-use, and access boundaries;
- derived artifacts preserve source evidence references, transformation records, parser/tool/model context, limitations, and audit references;
- findings, recommendations, timelines, report sections, and conclusions identify evidence support level, supporting evidence, uncertainty, limitations, and conflicting evidence where applicable;
- Agent Judge and AI assurance outputs are recorded as assurance signals, not evidence authority or approval authority;
- private/local LLM-assisted DFIR output remains evidence-derived and draft until examiner review and required approval are complete;
- retrieval, RAG, vector search, shared memory, customer context, case memory, and evidence retrieval preserve approved scope and record retrieval-boundary results where required;
- customer-facing evidence-derived outputs link to evidence support, review, approval where required, release scope, output destination, and audit records;
- corrections, supersessions, recalls, and reversals are appended as traceable records;
- replay can reconstruct evidence origin, access, scope validation, transformation, derived artifacts, finding support, review, approval, release, correction, recall, and final disposition;
- fail-closed handling exists for missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, integrity-failed, unsupported, or unauditable evidence context.
