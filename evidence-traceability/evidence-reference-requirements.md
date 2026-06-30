# Evidence Reference Requirements

## Purpose

This file defines evidence reference requirements for governed agentic security operations across MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

Evidence references provide stable, scoped, auditable links between evidence objects, derived artifacts, findings, timelines, recommendations, reports, approvals, and audit records.

This file defines reference architecture and governance expectations. It does not define a production evidence repository, legally sufficient chain-of-custody implementation, forensic tool validation program, customer-specific evidence procedure, or operational runbook.

## Scope

This file applies to evidence references used by:

- security alerts, detections, incidents, investigations, tickets, and case records;
- SIEM, XDR, EDR, NDR, cloud, SaaS, identity, email, firewall, endpoint, packet, memory, disk, file, and business-application evidence;
- normalized, enriched, parsed, extracted, summarized, or transformed evidence-derived records;
- private/local LLM-assisted DFIR workflows that parse, extract, summarize, timeline, or draft reports from evidence;
- agent-generated summaries, recommendations, timelines, report sections, and approval packages;
- Agent Judge or AI assurance checks that evaluate evidence support or unsupported claims;
- human review, examiner review, formal approval, customer approval, release, correction, supersession, recall, and audit replay workflows.

This file does not replace evidence handling, finding support, data ingestion, tool access, policy enforcement, human oversight, tenant isolation, local/private LLM DFIR, or audit replay controls. Evidence references supply structured linkage that those controls consume.

## Non-Goals

Evidence references must not be used to:

- replace original evidence;
- replace chain-of-custody records;
- prove that a finding or conclusion is correct;
- prove legal sufficiency or forensic validity;
- authorize evidence access, release, containment, remediation, closure, or customer notification;
- allow agents to fabricate support for findings;
- bypass review, approval, policy enforcement, tenant isolation, evidence handling, or audit replay.

## Core Principles

- Evidence references are controlled pointers to evidence, not evidence authority by themselves.
- Evidence references must be stable enough to support review, dispute handling, correction, and replay.
- Source evidence must remain distinguishable from derived artifacts, summaries, timelines, findings, and report drafts.
- References should identify the smallest practical evidence unit that supports a statement.
- References must preserve tenant, customer, case, workspace, source, retention, and allowed-use boundaries.
- References must preserve enough source, collection, integrity, and transformation context to support replay.
- Agent output must cite evidence references where evidence support is claimed.
- Agent-generated references must be validated before they support findings, reports, approval packages, or release decisions.
- Unsupported, stale, inaccessible, unauthorized, ambiguous, or mismatched references must not be used as confirmed evidence support.
- Missing or invalid evidence references must fail closed where governed workflow behavior depends on evidence support.

## Evidence Reference Model

An evidence reference links a downstream statement or artifact to a controlled evidence source.

| Object | Description | Requirement |
|---|---|---|
| Evidence object | Source evidence, controlled evidence copy, or registered evidence artifact. | Must have a stable `evidence_object_id` where governed workflows depend on it. |
| Evidence reference | Scoped pointer to an evidence object, segment, field, timestamp range, file location, extracted artifact, or derived artifact. | Must have a stable `evidence_reference_id` when cited downstream. |
| Derived artifact | Parsed, extracted, normalized, enriched, summarized, timelined, or report-ready output produced from evidence. | Must remain linked to source evidence and transformation context. |
| Finding support record | Relationship between a finding, recommendation, report statement, or approval package and the evidence references supporting it. | Must identify support level, limitations, review status, and unresolved gaps where applicable. |
| Review record | Human, examiner, or analyst review of evidence interpretation or finding support. | Must remain separate from the evidence reference itself. |
| Approval record | Formal authorization for release, action, or customer communication where required. | Must remain separate from evidence reference, review, and agent output. |
| Audit record | Replayable record of evidence access, citation, transformation, review, approval, release, correction, or recall. | Must link evidence reference activity to workflow and correlation identifiers. |

An evidence reference must not imply that the evidence was reviewed, approved, sufficient, current, complete, legally valid, or forensically conclusive unless separate review, approval, validation, or custody records support that status.

## Identifier Hierarchy

Evidence reference records should preserve the following identifier relationships.

| Identifier | Purpose |
|---|---|
| `evidence_object_id` | Identifies the registered source evidence object or controlled evidence artifact. |
| `evidence_reference_id` | Identifies the specific reference used by a finding, report, review, approval, or audit record. |
| `source_system_id` | Identifies the originating system, repository, tool, platform, or evidence store. |
| `source_record_id` | Identifies the original source event, alert, log record, file, export row, object, message, or artifact where available. |
| `derived_artifact_id` | Identifies a parsed, extracted, normalized, enriched, summarized, timelined, or report-draft artifact. |
| `transformation_record_id` | Links a derived artifact to parser, extractor, enrichment, summarization, normalization, model, tool, or workflow context. |
| `finding_id` | Links evidence support to a finding, recommendation, severity decision, timeline entry, or conclusion. |
| `report_section_id` | Links evidence support to a specific report section, timeline entry, table, appendix, or statement. |
| `review_record_id` | Links evidence interpretation to analyst, investigator, or examiner review where required. |
| `approval_record_id` | Links evidence use, release, or customer communication to formal approval where required. |
| `audit_reference_id` | Links evidence reference use to audit and replay records. |
| `correlation_ids` | Links evidence reference activity to workflow, case, policy, approval, tool, release, correction, or recall records. |

References should remain resolvable after re-indexing, storage migration, report redrafting, tool change, or model change. If a reference is superseded, corrected, recalled, or retired, the prior reference must remain replayable through appended status records.

## Evidence Reference Types

| Reference Type | Description | Required Precision |
|---|---|---|
| `SOURCE_OBJECT` | Reference to a registered evidence object such as a file, image, export, log bundle, packet capture, memory image, disk image, alert, or case record. | Evidence object identifier, source system, collection context, tenant, customer, case, and integrity reference where applicable. |
| `SOURCE_RECORD` | Reference to a specific log record, alert, event, message, ticket entry, file metadata record, or telemetry record. | Source record identifier, source timestamp, collection timestamp, source system, and schema or parser context where applicable. |
| `FIELD_OR_VALUE` | Reference to a specific field, value, attribute, indicator, detection field, extracted property, or metadata item. | Field path, source record, value context, parser or schema version, and transformation context where applicable. |
| `TIME_RANGE` | Reference to events or artifacts within a bounded time range. | Start time, end time, time zone or UTC normalization, source clock context where known, and query or filter reference where applicable. |
| `FILE_OR_PATH` | Reference to a file, path, registry key, process path, container path, mailbox item, cloud object, or storage object. | Path or object identifier, source system, hash or manifest reference where applicable, and acquisition or collection context. |
| `OFFSET_OR_RANGE` | Reference to byte offsets, line ranges, row ranges, packet ranges, memory regions, page ranges, or artifact segments. | Offset, range, unit, artifact identifier, hash or manifest reference, and tool version where applicable. |
| `DERIVED_ARTIFACT` | Reference to a parsed, extracted, normalized, enriched, summarized, or timelined artifact. | Derived artifact identifier, source evidence references, transformation record, tool or model version, and limitations. |
| `TIMELINE_ITEM` | Reference to a timeline entry derived from one or more evidence sources. | Timeline item identifier, source evidence references, time source, confidence or limitation notes, and review status where required. |
| `SCREENSHOT_OR_EXPORT` | Reference to a screenshot, exported report, query result, or manually captured evidence artifact. | Capture context, source system, collector identity, timestamp, integrity record where applicable, and underlying source reference when available. |
| `RETRIEVED_CONTEXT` | Reference to retrieved context from a knowledge store, vector index, evidence store, case memory, customer context, or RAG workflow. | Retrieval event, store or index identifier, query reference, scope result, timestamp, source references, retention, and allowed-use context. |

A single finding may require multiple evidence references when the support depends on correlation across different sources, timestamps, tenants, customers, cases, or derived artifacts.

## Required Evidence Reference Record

Governed evidence references must preserve a structured reference record.

| Field | Requirement | Purpose |
|---|---|---|
| `evidence_reference_id` | MUST | Unique identifier for the evidence reference. |
| `evidence_object_id` | MUST when referencing registered evidence | Links the reference to the controlled evidence object. |
| `evidence_reference_type` | MUST | Identifies source object, source record, field, time range, file path, derived artifact, timeline item, screenshot, export, or retrieved context. |
| `reference_status` | MUST | Records active, superseded, corrected, recalled, retired, unavailable, or disputed status. |
| `reference_target` | MUST | Identifies the referenced object, record, segment, field, path, offset, range, or derived artifact. |
| `reference_granularity` | MUST | Identifies object-level, record-level, field-level, segment-level, time-range, artifact-level, or derived-artifact-level precision. |
| `source_system_id` | MUST when evidence originates from a source system | Identifies the originating platform, repository, case system, evidence store, or data source. |
| `source_record_id` | MUST when available | Preserves traceability to the original source event, alert, log record, file, message, object, or artifact. |
| `source_timestamp` | MUST when available | Records the time associated with the source event or artifact. |
| `collection_timestamp` | MUST | Records when the evidence was collected, received, acquired, exported, registered, or referenced. |
| `collector_identity` | MUST | Identifies the collector, examiner, connector, workflow, service identity, or analyst that collected or registered the evidence. |
| `collection_method` | SHOULD | Identifies API, export, forensic acquisition, connector, agent, manual upload, screenshot, query, or local analysis method. |
| `collection_rule_id` | SHOULD when collection rules selected records | Links the reference to a collection rule, query, detection, filter, or acquisition scope. |
| `query_or_filter_reference` | SHOULD when query results are cited | Preserves the query, filter, search job, saved search, or retrieval event reference without requiring raw query content in every record. |
| `parser_id` | MUST when parsing affects the reference | Identifies the parser or extractor that produced the referenced structure. |
| `parser_version` | MUST when parsing affects interpretation | Supports replay, dispute review, and regression analysis. |
| `schema_version` | MUST when normalized records are referenced | Identifies the normalized schema used by downstream workflows. |
| `parser_or_transformation_version` | MUST when transformation changes field meaning or interpretation | Preserves parsing, extraction, normalization, enrichment, summarization, or timeline context. |
| `hash_or_manifest_reference` | MUST when integrity validation applies | References hash, manifest, verification, or integrity record without duplicating evidence. |
| `chain_of_custody_record_id` | MUST when chain-of-custody applies | Links reference use to the applicable custody record. |
| `tenant_id` | MUST for tenant-scoped, workspace-scoped, cloud-account-scoped, customer-scoped, or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when evidence is tied to an investigation, incident, ticket, escalation, report, or DFIR matter | Links evidence reference use to the governed case. |
| `workflow_id` | MUST for governed workflows | Links the evidence reference to workflow state. |
| `workflow_stage` | SHOULD when interpretation depends on stage | Identifies intake, triage, investigation, enrichment, review, approval, release, correction, recall, closure, or replay context. |
| `workspace_id` | MUST when workspace scope affects evidence access, interpretation, or routing | Preserves SIEM, XDR, cloud, logging, case-workspace, or evidence-workspace boundary. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects the evidence reference | Preserves cloud subscription, account, or project boundary. |
| `data_classification` | MUST when sensitivity affects access, handling, retention, approval, release, or customer communication | Preserves handling context. |
| `sensitivity_label` | MUST when applicable | Preserves privacy, legal, customer, forensic, regulated, or restricted handling label. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use for investigation, DFIR analysis, reporting, approval, governance review, customer communication, or legal handling. |
| `retention_policy_id` | MUST when retention affects evidence, derived artifacts, references, reports, or audit records | Preserves retention and disposal boundary. |
| `legal_hold_id` | MUST when applicable | Links evidence reference handling to preservation or legal hold requirements. |
| `access_scope` | MUST when access is role-, case-, customer-, tenant-, workflow-, evidence-, or repository-bound | Defines who or what may resolve, view, cite, transform, release, or replay the reference. |
| `derived_artifact_id` | MUST when reference points to or depends on derived evidence | Identifies the derived artifact separately from source evidence. |
| `source_evidence_reference_ids` | MUST when reference points to a derived artifact | Lists source evidence references used to create the derived artifact. |
| `transformation_record_id` | MUST when derived artifact or interpretation depends on transformation | Links parsing, extraction, normalization, enrichment, summarization, timeline, or report-drafting logic. |
| `finding_id` | MUST when the reference supports a finding | Links reference to the finding, recommendation, timeline entry, severity decision, or conclusion. |
| `finding_support_level` | MUST when used for finding support | Records whether support is direct, indirect, corroborating, partial, conflicting, unsupported, or reviewed. |
| `report_section_id` | SHOULD when used in report content | Links reference to the report section, table, timeline entry, appendix, or statement. |
| `agent_id` | MUST when an agent accessed, cited, summarized, or used the reference | Identifies agent participation. |
| `agent_session_id` or `run_id` | MUST when an agent accessed, cited, summarized, or used the reference | Supports replay of agent-assisted evidence use. |
| `model_route_id` | SHOULD when model-assisted processing affects derived output | Identifies the model route or local/private model context used for derived output. |
| `prompt_package_id` | SHOULD when prompt design affects derived output | Links evidence interpretation to prompt package or analysis template where applicable. |
| `tool_execution_id` | MUST when a tool accessed, parsed, transformed, retrieved, or summarized the reference | Links evidence reference activity to mediated tool execution. |
| `review_record_id` | MUST when analyst, investigator, or examiner review is required | Links interpretation to accountable human review. |
| `approval_record_id` | MUST when release, action, or customer communication requires approval | Links evidence use to scoped formal approval. |
| `release_record_id` | MUST when reference supports released report content, customer notification, evidence export, or shared intelligence | Links evidence support to release scope and version. |
| `limitations` | SHOULD where material | Records uncertainty, missing context, partial data, clock skew, tool limitation, parser limitation, redaction, or access limitation. |
| `audit_reference_id` | MUST when the reference is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links evidence reference activity to workflow, tool, policy, approval, review, release, correction, recall, and audit records. |

## Reference Granularity Requirements

Evidence references should be as precise as practical for the claim they support.

| Evidence Form | Minimum Reference Precision |
|---|---|
| SIEM or log event | Source system, source record ID, timestamp, normalized schema version where applicable, and query or collection reference. |
| Alert or detection | Alert ID, detection ID or rule reference, source system, related event references, severity context, and timestamp. |
| Endpoint artifact | Host or asset reference, artifact path or identifier, timestamp, collection method, hash or manifest reference where applicable. |
| Cloud record | Cloud provider account, subscription, project, region where applicable, resource identifier, event ID, source timestamp, and collection context. |
| SaaS or identity record | Tenant, user or service identity reference, source record ID, event timestamp, source system, and collection context. |
| Email evidence | Mailbox or message reference, message ID, header or attachment reference where applicable, tenant and customer scope, and collection context. |
| Packet capture | Capture identifier, packet range or time range, hash or manifest reference, collection interface where applicable, and analysis tool context. |
| Memory artifact | Memory image identifier, process or region reference, offset or artifact path, hash or manifest reference, and extraction tool context. |
| Disk or file-system artifact | Image or acquisition identifier, file path, offset or metadata reference, hash or manifest reference, and extraction tool context. |
| Screenshot or manual export | Capture identifier, collector identity, capture timestamp, source system, underlying source reference when available, and integrity reference where applicable. |
| Derived timeline entry | Timeline item ID, source evidence references, time source, normalization context, and review status where required. |
| Report statement | Statement or section ID, supporting evidence references, support level, limitations, review, approval, and release reference where required. |

Broad references may be used for initial triage, but findings, customer-facing report content, evidence releases, sensitive actions, closure recommendations, and DFIR conclusions require precise and reviewable references.

## Source and Attribution Requirements

Evidence references must preserve source and attribution context.

Required attribution includes, where applicable:

- tenant identifier;
- customer identifier;
- case, incident, ticket, matter, or workflow identifier;
- source system or evidence repository identifier;
- source record or object identifier;
- source timestamp and collection timestamp;
- collector, examiner, connector, tool, workflow, or service identity;
- collection method and collection rule;
- workspace, subscription, account, project, region, asset, mailbox, identity, or resource scope;
- data classification, sensitivity label, retention policy, legal hold, and allowed-use context;
- evidence status and reference status.

Tenant identity and customer identity must remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows.

When source attribution is missing, ambiguous, stale, inconsistent, or unauditable, the reference must not be used for confirmed findings unless an approved review path explicitly accepts the limitation.

## Integrity and Custody Reference Requirements

Evidence references do not replace integrity records or chain-of-custody records.

Where integrity validation applies, evidence references must link to:

- hash record, manifest, verification record, or acquisition manifest;
- evidence object status;
- collection or acquisition method;
- collector or examiner identity;
- storage or evidence repository reference;
- chain-of-custody record where applicable;
- verification status and timestamp where available.

When chain-of-custody applies, the evidence reference must identify the applicable custody record, but the reference itself must not be treated as the custody record.

If integrity or custody status is disputed, missing, expired, inconsistent, or unavailable, the reference must be marked with the appropriate limitation and routed to review where the workflow depends on that evidence.

## Derived Artifact Reference Requirements

Derived artifacts must remain traceable to source evidence.

A derived artifact reference must identify:

- derived artifact identifier;
- source evidence reference identifiers;
- transformation record identifier;
- parser, extractor, enrichment, summarization, timeline, or model route used;
- tool version, parser version, schema version, or transformation version where applicable;
- timestamp of transformation;
- identity of the tool, workflow, analyst, examiner, or agent that created it;
- limitations, confidence, partial-data status, or known transformation constraints where applicable;
- review status where the derived artifact supports higher-impact findings or release decisions.

Derived artifacts must not be presented as original evidence. Summaries, extracted indicators, timelines, normalized records, enriched records, and report drafts must preserve links to the source evidence that supports them.

## Normalization and Enrichment Reference Requirements

When normalized or enriched records are used as evidence support, references must preserve the link back to source evidence and transformation context.

Normalized or enriched references should include:

- source evidence reference ID;
- normalized record ID where applicable;
- parser ID and parser version;
- schema version;
- normalization mapping or transformation record;
- enrichment source, enrichment timestamp, enrichment version, and freshness context;
- confidence or limitation statements where enrichment is probabilistic, external, stale, partial, or unsupported;
- data classification, retention, allowed-use, and destination restrictions.

Enrichment does not convert weak evidence into confirmed evidence. Enriched context may support triage, prioritization, or analyst review, but must not be used as confirmed finding support unless the source evidence and enrichment limitations are reviewable.

## Retrieved Context and Memory Reference Requirements

RAG, vector search, knowledge-store retrieval, shared memory, case memory, customer context, and evidence retrieval must preserve reference boundaries.

Retrieved context references must include, where applicable:

- retrieval event identifier;
- knowledge store, memory store, evidence store, vector index, or case context identifier;
- query or retrieval reference;
- retrieval timestamp;
- retrieved source reference identifiers;
- tenant, customer, case, evidence, workspace, retention, and allowed-use scope;
- `knowledge_store_or_memory_scope`;
- `knowledge_memory_scope_result` where evaluated;
- freshness, staleness, redaction, or partial-result limitations;
- downstream workflow or output that consumed the retrieved context.

Retrieved context must not be treated as complete, current, authorized, or reusable without scope validation. Cross-tenant, cross-customer, cross-case, stale, unauthorized, retention-inconsistent, or unauditable retrieval must fail closed or route to governed review.

## Agent Use of Evidence References

Agents may use evidence references only within governed workflow boundaries.

Agents may:

- request scoped evidence references through approved tools or workflows;
- summarize evidence-derived content with citations to evidence references;
- draft timelines, findings, report sections, and approval packages using evidence references;
- identify missing references, inaccessible references, conflicting references, unsupported claims, and evidence gaps;
- propose support levels for human review;
- prepare reference tables for analyst, investigator, examiner, or approver review.

Agents must not:

- fabricate evidence references;
- cite evidence they cannot resolve or were not authorized to access;
- treat retrieved context or model memory as evidence without a controlled evidence reference;
- modify, delete, overwrite, reclassify, or silently replace evidence references;
- convert unsupported or partially supported statements into confirmed findings;
- use evidence references across tenant, customer, case, workspace, retention, or allowed-use boundaries without authorization;
- imply review, approval, chain-of-custody, legal conclusion, forensic proof, customer notification, containment success, remediation success, or closure from the existence of a reference;
- bypass evidence validation, human review, examiner review, formal approval, policy enforcement, or audit replay.

## Evidence Reference Validation

Evidence references must be validated before they support findings, approval packages, customer-facing reports, evidence release, or sensitive actions.

Validation should confirm:

- the reference resolves to the intended evidence object, record, segment, derived artifact, or retrieved context;
- the reference belongs to the correct tenant, customer, case, workspace, source, retention scope, and allowed use;
- the requesting identity, agent, tool, workflow, reviewer, or approver is authorized for the reference;
- required integrity, hash, manifest, custody, or acquisition records are available where applicable;
- parser, schema, normalization, enrichment, retrieval, model, or transformation context is available where interpretation depends on it;
- source timestamps, collection timestamps, time ranges, offsets, field paths, or artifact paths are precise enough for the claim;
- evidence status and reference status allow downstream use;
- limitations, conflicts, uncertainty, and partial support are preserved;
- required human review, examiner review, approval, and audit records are linked where applicable.

Validation failure must not be hidden by model summaries, report wording, analyst notes, dashboard views, or repeated agent reasoning.

## Finding and Report Reference Requirements

Findings, recommendations, timelines, severity decisions, closure recommendations, and report statements must identify supporting evidence references.

Each governed finding or report statement should preserve:

- finding or statement identifier;
- tenant, customer, case, workflow, and report scope;
- evidence reference identifiers;
- derived artifact identifiers where used;
- support level;
- unsupported assumptions, gaps, conflicts, uncertainty, and limitations;
- review record where review is required;
- approval record where release or customer communication requires approval;
- released version, destination, and release record where applicable;
- audit reference and correlation identifiers.

Customer-facing content must not present unsupported, partially supported, unresolved, unreviewed, or disputed statements as confirmed findings.

## Evidence Reference Status

Evidence references must have explicit status when used in governed workflows.

| Status | Meaning | Handling |
|---|---|---|
| `ACTIVE` | Reference is valid for its approved scope. | May be used according to access, retention, allowed-use, review, and approval controls. |
| `LIMITED` | Reference is usable only with stated limitations. | Must preserve limitation text and route to review where required. |
| `DISPUTED` | Reference, interpretation, integrity, attribution, or support is challenged. | Must not support confirmed findings without review and documented resolution. |
| `SUPERSEDED` | A newer reference, corrected reference, or derived artifact replaces the reference for future use. | Prior reference must remain replayable; downstream records should point to the superseding reference where appropriate. |
| `CORRECTED` | Reference metadata or interpretation has been corrected. | Correction must be appended and linked to prior reference. |
| `RECALLED` | Reference or downstream use has been recalled due to error, boundary issue, release issue, or evidence issue. | Must trigger affected-output review and audit replay. |
| `RETIRED` | Reference is no longer approved for new use due to retention, case closure, policy, or repository change. | Must remain available for replay where retention and legal hold permit. |
| `UNAVAILABLE` | Reference cannot currently be resolved. | Must not support confirmed findings or release decisions until resolved or reviewed. |

Reference status changes must be appended and auditable. Prior reference states must not be silently overwritten.

## Release and Approval Reference Requirements

Evidence references used for customer-facing reports, evidence release, shared intelligence release, notifications, or approval packages must link to the required review and approval records.

Before release, governed workflows must confirm:

- evidence references resolve within approved tenant, customer, case, workspace, retention, and allowed-use scope;
- unsupported or partially supported claims are not presented as confirmed findings;
- derived artifacts preserve source evidence links and transformation records;
- sensitive content, raw evidence, restricted data, legal hold material, and customer-specific data are handled according to release scope;
- reviewer or examiner records are complete where required;
- approval record is valid, scoped, unexpired, and linked to the release;
- release version, destination, and audit reference are recorded.

Approval of a report, release, or customer communication must not be inferred from evidence reference existence, agent output, tool success, or Agent Judge output.

## Correction, Supersession, and Recall

Evidence reference errors must be corrected through append-only records.

Correction, supersession, or recall may be required when:

- reference points to the wrong evidence object, record, field, artifact, or time range;
- tenant, customer, case, workspace, retention, allowed-use, or access scope was wrong;
- source attribution, timestamp, collector identity, parser version, schema version, transformation record, or integrity context was wrong;
- derived artifact relationship was incomplete or incorrect;
- reference was fabricated, inaccessible, stale, disputed, or unauthorized;
- reference was used in a released report, customer notification, approval package, shared intelligence package, or action decision with incorrect support;
- reference crossed tenant, customer, case, evidence, memory, or retention boundaries.

Corrections must preserve the original reference, corrected reference, reason, reviewer or approver where required, affected downstream records, final disposition, and audit references.

## Fail-Closed Conditions

Governed workflows must fail closed, quarantine, or route to controlled review when:

- required evidence reference is missing, ambiguous, stale, inaccessible, unauthorized, inconsistent, disputed, unavailable, or unauditable;
- evidence reference cannot be resolved to the intended evidence object, record, field, artifact, segment, time range, or derived artifact;
- evidence reference crosses tenant, customer, case, workspace, source, evidence, memory, retention, legal hold, or allowed-use boundaries;
- source system, source record, source timestamp, collection timestamp, collector identity, parser version, schema version, transformation record, integrity record, or custody reference is required but unavailable;
- reference status is disputed, recalled, retired, unavailable, or out of scope for the requested use;
- an agent cites evidence it was not authorized to access or cannot resolve;
- retrieved context lacks required source references, retrieval scope, freshness context, or `knowledge_memory_scope_result` where required;
- evidence-derived output attempts to imply approval, customer notification, legal determination, forensic proof, containment success, remediation success, closure, or release authorization without required controls;
- review, examiner review, approval, customer approval, or policy decision is required but missing, expired, revoked, incomplete, or out of scope;
- audit logging fails where evidence reference traceability is mandatory.

Fail-closed handling must preserve the original request, failed reference, missing control, scope context, affected workflow, routing reason, reviewer or approver requirement, and audit reference.

## Audit and Replay Requirements

Evidence reference activity must be auditable and replayable.

Audit replay should reconstruct:

- which evidence reference was created, resolved, cited, transformed, reviewed, approved, released, corrected, superseded, recalled, or retired;
- which evidence object, source record, field, segment, time range, file path, derived artifact, timeline item, report statement, or retrieved context was referenced;
- who or what created, accessed, modified, cited, reviewed, approved, released, corrected, or recalled the reference;
- which tenant, customer, case, workspace, source, evidence, retention, legal hold, allowed-use, and access scope applied;
- which tools, parsers, transformations, retrieval events, model routes, prompts, or local/private DFIR steps affected interpretation;
- which findings, recommendations, timelines, reports, approvals, releases, shared intelligence packages, actions, or customer communications consumed the reference;
- which limitations, conflicts, uncertainty, unsupported claims, or review findings applied;
- which final state was reached.

Audit replay does not prove the finding was correct. It proves that evidence reference use, support, review, approval, release, correction, recall, and final disposition can be reconstructed and challenged.

## Operational Anti-Patterns

Avoid the following:

- citing evidence without a stable evidence reference;
- treating model output, retrieved context, analyst narrative, dashboard views, or screenshots as original evidence without controlled references;
- using broad references when a precise source record, field, time range, or artifact segment is required;
- fabricating evidence references or citing evidence the workflow cannot resolve;
- copying raw evidence into prompts, logs, reports, or approval records when controlled references are sufficient;
- joining evidence across tenants, customers, cases, workspaces, memory scopes, or retention scopes without explicit authorization;
- treating reference existence as review, approval, legal determination, forensic proof, release authorization, containment success, remediation success, or closure;
- using stale, inaccessible, disputed, recalled, or unavailable references to support confirmed findings;
- allowing agents to modify, suppress, delete, reclassify, or silently replace evidence references;
- allowing derived artifacts, summaries, timelines, or enriched records to obscure source evidence;
- releasing customer-facing conclusions without evidence references, review, approval, and audit records where required;
- correcting reference errors by overwriting prior records instead of appending correction, supersession, or recall records.

## Relationship to Other Control Areas

Evidence reference requirements depend on records and controls from other governance domains:

- [`evidence-traceability-model.md`](evidence-traceability-model.md) defines the overall evidence traceability model, lifecycle, and source-to-finding linkage.
- [`finding-support-requirements.md`](finding-support-requirements.md) defines evidence support requirements for findings, recommendations, conclusions, report sections, and customer communications.
- [`dfir-evidence-handling.md`](dfir-evidence-handling.md) defines DFIR evidence handling expectations for source evidence, working copies, derived artifacts, examiner review, and release controls.
- [`evidence-audit-replay.md`](evidence-audit-replay.md) defines audit and replay requirements for evidence access, evidence references, derived artifacts, finding support, review, approval, release, correction, and recall.
- [`../data-ingestion/readme.md`](../data-ingestion/readme.md) defines source metadata, normalization, enrichment, failure handling, and ingestion replay.
- [`../tool-access/readme.md`](../tool-access/readme.md) defines tool registration, restricted tool use, scoped execution, and tool audit expectations.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines PDP, PEP, policy decision, approval policy, and fail-closed behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) defines review, formal approval, customer approval, escalation, and review record expectations.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, and cross-tenant boundary controls.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines private/local LLM-assisted DFIR boundaries, evidence handling, review workflow, and replay considerations.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines audit event, replayability, correlation, exception, failure, and immutable audit expectations.

## Acceptance Criteria

Evidence reference requirements are acceptable when:

- evidence references have stable identifiers and resolvable targets;
- source evidence remains distinguishable from references, derived artifacts, summaries, timelines, findings, and report drafts;
- references preserve tenant identity and customer identity separately for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- references preserve source system, source record, collection, timestamp, collector, integrity, custody, parser, schema, transformation, retention, legal hold, allowed-use, and access context where applicable;
- derived artifact references preserve source evidence links and transformation records;
- normalized, enriched, retrieved, and model-assisted outputs preserve source references and limitations;
- findings, recommendations, timelines, report sections, approval packages, and customer communications identify supporting evidence references and support levels;
- unsupported, partially supported, disputed, stale, inaccessible, recalled, or unavailable references cannot be presented as confirmed evidence support without review and documented limitation;
- agent outputs cannot fabricate references or convert unresolved references into findings;
- review, approval, release, correction, supersession, and recall records link back to the evidence references they affect;
- audit replay can reconstruct evidence reference creation, resolution, access, use, review, approval, release, correction, recall, and final disposition;
- fail-closed handling exists for missing, ambiguous, unauthorized, stale, cross-tenant, cross-customer, cross-case, retention-inconsistent, unsupported, or unauditable evidence references.
