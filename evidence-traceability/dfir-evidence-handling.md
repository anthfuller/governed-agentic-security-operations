# DFIR Evidence Handling

## Purpose

This file defines DFIR evidence-handling expectations for governed agentic security operations across MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted forensic workflows.

The model keeps source evidence, working copies, derived artifacts, agent-assisted outputs, examiner notes, findings, approval packages, released reports, and audit records clearly separated and traceable.

This file defines architecture and governance expectations. It does not define a production evidence repository, legally sufficient chain-of-custody implementation, forensic tool validation program, customer-specific evidence procedure, legal advice, or environment-specific operational runbook.

## Scope

This file applies to DFIR evidence handling for:

- disk images, file-system images, volume snapshots, file collections, and exported artifacts;
- memory captures, process listings, module lists, handles, network connections, and volatile data;
- packet captures, network flow exports, DNS records, proxy logs, firewall logs, and NDR records;
- endpoint telemetry, EDR exports, device timelines, process trees, command-line records, registry artifacts, persistence artifacts, and malware-related artifacts;
- cloud, identity, SaaS, email, ticketing, SIEM, XDR, and case-system exports used as DFIR evidence;
- screenshots, analyst notes, examiner notes, interview notes, case notes, and timeline entries when they support a governed finding;
- derived artifacts created through parsing, extraction, normalization, enrichment, timeline reconstruction, summarization, report drafting, or local/private LLM-assisted analysis;
- evidence references used in findings, recommendations, report sections, approval records, customer communications, and audit replay.

This file does not replace `data-ingestion/`, `tool-access/`, `tenant-isolation/`, `human-oversight/`, `policy-enforcement/`, `local-llm-dfir/`, or `audit-replay/`. It defines DFIR evidence-handling boundaries consumed by those control areas.

## Non-Goals

DFIR evidence handling MUST NOT be used to:

- treat agent output, retrieved context, parser output, or model-generated summaries as original evidence;
- replace examiner judgment, forensic methodology, legal review, or customer-specific evidence procedures;
- treat local/private execution as proof of correctness, evidentiary validity, or forensic completeness;
- treat chain-of-custody references as interchangeable with audit logs, analyst notes, or model output;
- bypass tenant, customer, case, workspace, evidence, retention, legal hold, access, review, approval, or audit boundaries;
- release evidence, derived artifacts, findings, or DFIR conclusions without required evidence support, review, and approval.

## Core Principles

- Source evidence remains immutable or protected by the applicable evidence-handling process.
- Working copies, derived artifacts, summaries, timelines, and report drafts remain separate from source evidence.
- Every derived artifact must be traceable to source evidence references and transformation context.
- Evidence references should be used instead of copying raw evidence into prompts, audit records, reports, approval records, or shared knowledge stores unless the evidence-handling model explicitly permits it.
- Chain-of-custody records remain separate from model output, audit logs, analyst notes, and report drafts.
- Examiner review is required for forensic conclusions, high-impact interpretations, disputed evidence, and customer-facing DFIR findings.
- Agent assistance may accelerate extraction, summarization, timeline drafting, and evidence support mapping, but it does not establish forensic truth.
- Agent Judges and AI assurance checks may evaluate evidence support and unsupported claims as assurance only.
- Tenant identity and customer identity must remain separate for MSSP, MDR, DFIR, customer-scoped, and multi-customer workflows.
- Missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, integrity-failed, or unauditable evidence context must fail closed where governed workflow behavior depends on it.

## DFIR Evidence Object Types

| Evidence Object Type | Description | Handling Requirement |
|---|---|---|
| Source evidence | Original collected, acquired, exported, received, or registered evidence. | MUST remain protected, immutable where required, and traceable to source, collection, integrity, scope, and custody context. |
| Evidence copy | Controlled duplicate of source evidence. | MUST reference source evidence and preserve copy method, timestamp, hash or manifest reference, and custodian where applicable. |
| Working copy | Analysis copy used by an examiner, workflow, or tool. | MUST remain linked to source evidence and MUST NOT be treated as source evidence. |
| Derived artifact | Parsed, extracted, normalized, enriched, summarized, or transformed artifact. | MUST preserve source evidence references, transformation record, tool or model context, limitations, and audit reference. |
| Timeline item | Event or observation placed into a DFIR timeline. | MUST reference source evidence, timestamp basis, time-zone handling, transformation context, and confidence or limitation where applicable. |
| Finding support artifact | Evidence support table, claim map, or finding-to-evidence linkage. | MUST identify supporting evidence, gaps, conflicts, assumptions, reviewer context, and approval path where required. |
| Agent output | Agent-generated summary, extraction, timeline draft, hypothesis, recommendation, or report draft. | MUST be labeled as agent-assisted output and MUST NOT replace evidence, examiner review, or approval. |
| Examiner note | Human examiner observation, interpretation, or decision. | MUST reference evidence and distinguish observation from conclusion. |
| Report section | Draft or released DFIR report content. | MUST link to supporting evidence, review records, approval records, release scope, and audit references. |

## Governed DFIR Evidence Workflow

| Stage | Requirement |
|---|---|
| Case or matter setup | Establish tenant, customer, case, engagement, scope, authority, retention, legal hold, and allowed-use context before evidence is handled. |
| Evidence intake | Record source, collector, collection method, acquisition context, classification, sensitivity, and custody context where applicable. |
| Evidence registration | Assign stable evidence identifiers and evidence reference identifiers before downstream use. |
| Integrity preservation | Record hash, manifest, signature, or integrity reference where integrity validation applies. |
| Scope validation | Validate tenant, customer, case, workspace, subscription, account, host, user, source, retention, legal hold, and allowed-use scope. |
| Access mediation | Allow access only through approved examiner, workflow, repository, or tool paths with scoped identity and audit coverage. |
| Working-copy creation | Create controlled analysis copies when needed and link them to source evidence and custody records where applicable. |
| Analysis and extraction | Preserve tool identity, tool version, parser version, model route, prompt package, transformation parameters, timestamp handling, and limitations where they affect interpretation. |
| Derived artifact creation | Link extracted indicators, file metadata, memory observations, packet observations, timelines, and summaries to source evidence. |
| Agent-assisted processing | Permit agents to summarize, classify, correlate, and draft only within approved case, evidence, retrieval, and output scope. |
| Examiner review | Validate evidence sufficiency, interpretation, unsupported claims, conflicting evidence, and release readiness. |
| Finding and report drafting | Link each finding, timeline entry, recommendation, and conclusion to evidence references and limitations. |
| Approval and release | Route customer-facing findings, evidence exports, sensitive conclusions, and release packages through required approval paths. |
| Audit and replay | Preserve records needed to reconstruct evidence access, transformation, review, approval, release, correction, and final disposition. |

## Required DFIR Evidence Record

Governed DFIR evidence handling MUST preserve a structured evidence record where applicable.

| Field | Requirement | Purpose |
|---|---|---|
| `evidence_object_id` | MUST | Unique identifier for the evidence object. |
| `evidence_reference_id` | MUST when evidence is cited or consumed downstream | Stable reference used by findings, timelines, report sections, approvals, and audit replay. |
| `evidence_role` | MUST | Identifies source evidence, evidence copy, working copy, derived artifact, summary, timeline item, finding support artifact, or report reference. |
| `evidence_type` | MUST | Identifies disk image, memory capture, packet capture, log export, endpoint artifact, cloud export, email artifact, screenshot, note, derived artifact, or other evidence type. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST | Links evidence to the investigation, incident, ticket, case, matter, or DFIR engagement. |
| `engagement_id` or `matter_id` | SHOULD when used by the service model | Links evidence to customer engagement or legal matter context. |
| `source_system_id` | MUST when evidence originates from a system or repository | Identifies originating SIEM, XDR, EDR, cloud, SaaS, identity, email, firewall, evidence store, case store, endpoint, host, or repository. |
| `source_record_id` | MUST when available | Preserves source-level traceability. |
| `source_host_id`, `account_id`, `user_id`, or equivalent | SHOULD when applicable | Preserves entity-level evidence attribution. |
| `source_timestamp` | MUST when available | Records the source event, artifact, or record time. |
| `collection_timestamp` | MUST | Records when evidence was collected, acquired, exported, received, or registered. |
| `collector_identity` | MUST | Identifies examiner, analyst, connector, service identity, agent, or workflow that collected or registered the evidence. |
| `collection_method` | MUST | Identifies forensic acquisition, API export, connector collection, manual upload, customer transfer, screenshot, case note, or other method. |
| `acquisition_tool_id` | SHOULD when acquisition tooling is used | Identifies acquisition or export tool. |
| `acquisition_tool_version` | SHOULD when acquisition tooling affects interpretation or replay | Supports tool accountability, repeatability, and dispute review. |
| `storage_location_reference` | MUST when evidence is stored | References controlled storage location without exposing uncontrolled raw evidence paths. |
| `hash_or_manifest_reference` | MUST when integrity validation applies | Links to hash, manifest, signature, or integrity record. |
| `chain_of_custody_record_id` | MUST when chain-of-custody applies | Links evidence to custody records without treating summaries or audit logs as custody records. |
| `legal_hold_id` | MUST when legal hold applies | Links evidence to preservation requirements. |
| `data_classification` | MUST when sensitivity affects handling, access, retention, approval, or release | Preserves handling context. |
| `sensitivity_label` | MUST when applicable | Preserves customer, privacy, legal, forensic, or operational sensitivity context. |
| `allowed_use` | MUST when evidence use is constrained | Defines permitted investigation, reporting, approval, legal, customer communication, or governance use. |
| `retention_policy_id` | MUST when retention affects evidence or derived artifacts | Preserves retention and disposal boundary. |
| `access_scope` | MUST | Defines role, case, customer, tenant, examiner, workflow, and tool access limits. |
| `derived_from_evidence_object_ids` | MUST for derived artifacts | Links derived artifacts to source evidence. |
| `transformation_record_id` | MUST when evidence is parsed, extracted, summarized, normalized, enriched, timelined, or transformed | Links derived output to transformation details. |
| `parser_id` | MUST when parsing is applied | Identifies parser used to produce derived structure. |
| `parser_version` | MUST when parsing affects interpretation, replay, or report content | Supports parser accountability and regression review. |
| `analysis_tool_id` | SHOULD when analysis tooling affects interpretation | Identifies forensic, parsing, extraction, timeline, malware, memory, packet, or reporting tool. |
| `analysis_tool_version` | SHOULD when tool version affects interpretation or replay | Supports repeatability and dispute review. |
| `model_route_id` | MUST when model output affects interpretation, timeline drafting, report drafting, or finding support | Identifies model route used by agent-assisted analysis. |
| `prompt_package_id` | MUST when prompts affect evidence interpretation or report drafting | Supports replay of model-assisted evidence use. |
| `knowledge_store_or_memory_scope` | MUST when retrieval, RAG, vector search, case memory, customer context, or evidence retrieval is used | Defines approved retrieval and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval remained within approved evidence, tenant, customer, case, retention, and reuse boundaries. |
| `limitations` | MUST where material | Records missing evidence, partial collection, time gaps, tool limitations, parsing uncertainty, unsupported claims, or conflicting evidence. |
| `examiner_review_record_id` | MUST when examiner review is required | Links evidence interpretation to accountable review. |
| `approval_record_id` | MUST when release, evidence export, sensitive conclusion, or customer-facing use requires approval | Links evidence use to scoped approval. |
| `audit_reference_id` | MUST for governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links evidence, case, workflow, tool, agent, review, approval, release, and audit records. |

## Source Evidence Handling

Source evidence MUST remain distinguishable from copies, derived artifacts, summaries, timelines, and report drafts.

Source evidence handling MUST ensure that:

- source evidence is registered before being cited or consumed downstream;
- integrity references are recorded where integrity validation applies;
- custody records are linked where custody tracking is required;
- source evidence is not silently modified, overwritten, deleted, or reclassified by agents, tools, or workflows;
- source evidence remains within approved tenant, customer, case, matter, retention, legal hold, and access boundaries;
- access to source evidence is mediated, scoped, logged, and replayable.

When source evidence cannot be protected, identified, scoped, or replayed, downstream governed use MUST fail closed or route to controlled review.

## Working Copy Requirements

Working copies MAY be created for analysis, extraction, timeline reconstruction, malware triage, memory analysis, packet analysis, or local/private LLM-assisted workflows.

Working copies MUST:

- reference the source evidence object;
- preserve creation timestamp, creator identity, storage reference, and purpose;
- preserve hash or manifest reference where required;
- remain scoped to the approved case, customer, tenant, examiner workflow, and allowed use;
- be distinguishable from source evidence;
- be disposed, retained, or placed under hold according to retention, legal hold, customer, and case requirements.

Working-copy output MUST NOT be treated as original evidence unless the evidence-handling process explicitly registers and preserves it as a new evidence object.

## Derived Artifact Requirements

Derived artifacts include extracted indicators, file listings, registry keys, event timelines, memory observations, packet observations, malware triage notes, artifact summaries, normalized records, enrichment outputs, and report-ready support tables.

Derived artifacts MUST preserve:

- source evidence references;
- transformation record identifier;
- parser, tool, script, model, or workflow identity where applicable;
- parser or transformation version where interpretation depends on it;
- timestamp handling and time-zone assumptions where applicable;
- data classification, sensitivity label, retention, and allowed-use context;
- limitations, uncertainty, unsupported claims, and conflicting evidence where material;
- examiner review record where required;
- audit reference and correlation identifiers.

Derived artifacts MUST NOT replace source evidence, chain-of-custody records, examiner validation, or approval records.

## Transformation Record Requirements

A transformation record SHOULD be created when evidence is parsed, extracted, normalized, enriched, summarized, timelined, converted, redacted, translated, or report-drafted.

| Field | Requirement | Purpose |
|---|---|---|
| `transformation_record_id` | MUST | Unique transformation record identifier. |
| `source_evidence_object_ids` | MUST | Identifies source evidence used. |
| `derived_artifact_ids` | MUST when derived output is created | Identifies resulting artifacts. |
| `transformation_type` | MUST | Identifies parse, extract, normalize, enrich, summarize, timeline, redact, report-draft, or other transformation. |
| `tool_id` | MUST when a tool is used | Identifies tool that performed the transformation. |
| `tool_version` | MUST when tool version affects interpretation or replay | Supports repeatability and dispute review. |
| `parser_id` | MUST when parsing is used | Identifies parser logic. |
| `parser_version` | MUST when parsing affects downstream meaning | Supports replay and regression review. |
| `model_route_id` | MUST when model-assisted transformation is used | Identifies model route. |
| `prompt_package_id` | MUST when prompts affect transformation output | Links model-assisted output to prompt context. |
| `input_scope` | MUST | Defines evidence, tenant, customer, case, workspace, source, and allowed-use scope. |
| `output_destination` | MUST when output is stored, routed, released, indexed, or consumed downstream | Preserves destination context. |
| `limitations` | MUST where material | Records uncertainty, unsupported claims, missing evidence, or incomplete parsing. |
| `review_record_id` | MUST when review is required | Links transformation output to human or examiner review. |
| `audit_reference_id` | MUST for governed workflows | Supports audit replay. |

## Private/Local LLM-Assisted DFIR Requirements

Private/local LLM-assisted DFIR workflows MAY support extraction, summarization, triage, timeline drafting, report drafting, evidence support mapping, and uncertainty identification.

Private/local LLM-assisted DFIR workflows MUST satisfy these requirements:

- local execution is treated as an execution and evidence-handling context, not proof of correctness;
- source evidence remains separate from prompts, retrieved context, derived artifacts, summaries, and report drafts;
- agents and models access only approved tenant, customer, case, evidence, workspace, retention, and allowed-use scope;
- raw evidence is not copied into prompts, logs, audit records, model memory, shared memory, or vector stores unless explicitly authorized by the evidence-handling model;
- retrieval, RAG, vector search, shared memory, customer context, case memory, and evidence retrieval remain within approved `knowledge_store_or_memory_scope`;
- model route, prompt package, retrieval scope, retrieved context references, and limitations are recorded where output affects interpretation, report drafting, or downstream use;
- model-generated findings remain drafts until examiner review and required approval are complete;
- unsupported claims, uncertainty, conflicts, and missing evidence are preserved rather than smoothed into confident conclusions;
- customer-facing DFIR conclusions require evidence validation, examiner review, release scope, approval where required, and audit replay.

Agents and models MUST NOT:

- modify, delete, overwrite, silently replace, or reclassify source evidence;
- fabricate evidence references;
- cite evidence that is inaccessible, out of scope, stale, or unresolved;
- create or certify chain-of-custody records;
- represent summaries as original evidence, forensic proof, legal conclusions, or examiner determinations;
- approve evidence release, findings, customer communications, containment, remediation, closure, or policy exceptions;
- bypass evidence validation, human review, examiner review, approval, policy enforcement, or audit replay.

## Evidence Access and Retrieval Boundaries

Evidence access MUST be scoped by tenant, customer, case, matter, role, workflow, evidence type, storage location, legal hold, retention, allowed use, and output destination where applicable.

Retrieval from evidence stores, case stores, knowledge stores, vector indexes, shared memory, customer context, case memory, or prior-case context MUST:

- use approved retrieval scope;
- preserve source references and retrieval timestamp;
- preserve store, index, query, or retrieval reference where available;
- record `knowledge_memory_scope_result` where retrieval scope is evaluated;
- prevent cross-tenant, cross-customer, cross-case, retention-inconsistent, stale, or unauthorized reuse;
- treat retrieved context as evidence-derived context, not original evidence or final truth.

Retrieved context MUST NOT be reused in another case, customer, tenant, report, approval package, or shared intelligence package unless reuse is explicitly authorized, sanitized where required, and auditable.

## Examiner Review Requirements

Examiner review is required when DFIR evidence interpretation affects:

- customer-facing DFIR findings, timelines, report sections, or executive summaries;
- incident scope, root cause, impact, exposure, containment status, eradication status, recovery status, or closure recommendation;
- malware, memory, disk, packet, cloud, identity, or email evidence interpretation;
- evidence conflicts, missing evidence, partial acquisition, timestamp ambiguity, or chain-of-custody concern;
- legal hold, customer escalation, evidence release, or sensitive disclosure;
- policy-gated workflow steps, approval packages, or audit dispute resolution.

An examiner review record SHOULD include:

- examiner identity;
- review timestamp;
- case and evidence scope;
- evidence references reviewed;
- derived artifacts reviewed;
- findings or report sections reviewed;
- unsupported claims, limitations, and conflicting evidence;
- approved, rejected, revised, or escalated disposition;
- required approval path where applicable;
- audit reference and correlation identifiers.

Examiner review MUST remain separate from agent output, Agent Judge output, customer approval, and formal release approval.

## Finding and Report Support Requirements

DFIR findings, timelines, recommendations, and report sections MUST preserve evidence support.

Each governed finding SHOULD include:

- finding identifier;
- case identifier;
- tenant and customer scope;
- evidence references supporting the finding;
- derived artifacts used to interpret the evidence;
- source timestamps and timeline assumptions where applicable;
- evidence support level;
- unsupported assumptions, limitations, or conflicting evidence;
- examiner review record where required;
- approval record where required;
- release scope and output destination where applicable;
- audit reference and correlation identifiers.

A statement that no evidence was found MUST identify the evidence searched, search scope, data coverage, time window, tooling, limitations, and unresolved gaps.

Customer-facing findings MUST NOT present unsupported, partially supported, unreviewed, or out-of-scope statements as confirmed conclusions.

## Chain-of-Custody Boundary

Chain-of-custody records MUST remain separate from:

- model outputs;
- agent summaries;
- derived artifacts;
- analyst notes;
- examiner notes;
- audit logs;
- report drafts;
- approval records;
- customer communications.

Audit records MAY reference chain-of-custody records, but audit replay MUST NOT be treated as a chain-of-custody implementation unless the evidence-handling process explicitly defines it that way.

When chain-of-custody applies, custody events SHOULD identify custodian, transfer, access, storage, integrity, timestamp, reason, and evidence object reference.

## Evidence Release and Export Controls

Evidence release, derived artifact export, report release, or customer-facing DFIR conclusion MUST be controlled by scope, evidence support, review, approval, and audit requirements.

Release packages SHOULD preserve:

- release identifier;
- case and customer scope;
- evidence references included or cited;
- derived artifacts included or cited;
- redaction or sanitization record where applicable;
- classification and sensitivity label;
- allowed use and retention expectations;
- reviewer and approver records;
- output destination;
- release timestamp;
- audit reference and correlation identifiers.

Evidence or derived artifacts MUST NOT be released across tenant, customer, case, legal hold, retention, or allowed-use boundaries without explicit authorization and audit coverage.

## Correction, Supersession, and Recall

Corrections to DFIR evidence interpretation MUST be appended, not silently overwritten.

Correction, supersession, or recall records SHOULD be created when:

- evidence was misattributed;
- a derived artifact was generated from the wrong source evidence;
- an agent or tool cited unresolved or out-of-scope evidence;
- a finding was unsupported, partially supported, or contradicted by later evidence;
- a report section used stale, incomplete, or incorrect evidence interpretation;
- a release package included evidence, derived artifacts, or conclusions outside approved scope;
- an approval was revoked, expired, or found to be out of scope.

Correction records SHOULD identify the original record, corrected record, reason, reviewer, approver where required, customer notification path where applicable, and audit reference.

## Audit and Replay Requirements

DFIR evidence handling MUST produce audit records sufficient to reconstruct:

- which evidence was collected, received, registered, accessed, copied, transformed, reviewed, released, corrected, or recalled;
- who or what accessed the evidence;
- which tenant, customer, case, matter, workspace, source, retention, legal hold, and allowed-use scope applied;
- which tools, parsers, models, prompt packages, retrieval scopes, and transformations were used;
- which derived artifacts were created;
- which findings, recommendations, timelines, report sections, approval packages, or customer communications used the evidence;
- which unsupported claims, limitations, conflicts, or evidence gaps were identified;
- which examiner review, human review, approval, release, correction, supersession, or recall records applied;
- what final disposition was reached.

Audit replay does not prove that a DFIR conclusion was correct. It proves that evidence use, interpretation, review, approval, release, correction, and final disposition can be reconstructed and challenged.

## Fail-Closed Conditions

Governed DFIR evidence workflows MUST fail closed, quarantine, or route to controlled review when:

- required evidence identifiers, evidence references, source metadata, collection metadata, integrity references, custody references, retention records, legal hold records, or access scope are missing, ambiguous, stale, inconsistent, or unauditable;
- tenant, customer, case, matter, workspace, source, host, account, user, or evidence attribution is missing or mismatched;
- source evidence and derived artifacts cannot be distinguished;
- evidence hash, manifest, signature, or integrity validation fails where integrity validation applies;
- chain-of-custody is required but unavailable, broken, incomplete, or inconsistent;
- a working copy or derived artifact cannot be linked to source evidence;
- an agent, model, tool, or parser cites evidence that cannot be resolved or is outside approved scope;
- retrieved context crosses tenant, customer, case, evidence, workspace, retention, legal hold, freshness, or allowed-use boundaries;
- `knowledge_store_or_memory_scope` is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval affects evidence interpretation or downstream use;
- `knowledge_memory_scope_result` is required but missing, unavailable, inconsistent, or indicates retrieval exceeded approved boundaries;
- parser, tool, model route, prompt package, or transformation version cannot be determined where replay or interpretation depends on it;
- raw evidence is copied into prompts, audit logs, shared memory, vector stores, or reports without authorization;
- a finding is unsupported or only partially supported but is being prepared for release as confirmed;
- examiner review, human review, formal approval, customer approval, or release approval is required but missing, expired, revoked, incomplete, or out of scope;
- agent output attempts to imply forensic proof, legal conclusion, customer notification, containment success, remediation success, closure, or approval without governed workflow context;
- audit logging fails where DFIR evidence traceability is mandatory.

Fail-closed handling MUST preserve the original request, evidence references, missing or failed control, scope context, reviewer or approver requirement, routing reason, and audit reference.

## Operational Anti-Patterns

Avoid the following:

- treating agent output, retrieved context, analyst narrative, dashboards, or summaries as original evidence;
- allowing agents or tools to modify, delete, overwrite, silently replace, or reclassify source evidence;
- mixing evidence across tenants, customers, cases, matters, workspaces, retention scopes, or legal holds without explicit authorization;
- creating findings without evidence references;
- presenting model-generated report language as examiner-validated DFIR conclusions without review;
- copying raw evidence into prompts, audit logs, shared memory, vector stores, or reports when controlled references are sufficient;
- using unscoped retrieval from case memory, customer context, shared memory, or prior-case context;
- treating local/private execution as proof of evidentiary validity;
- treating MCP, tool, parser, or model success as evidence completeness or forensic proof;
- treating Agent Judge output as examiner review, human approval, or customer approval;
- treating audit replay as a chain-of-custody system unless explicitly designed that way;
- releasing evidence, derived artifacts, findings, timelines, or report sections without required review, approval, release scope, and audit records;
- silently correcting evidence interpretation instead of appending correction, supersession, or recall records.

## Relationship to Other Control Areas

DFIR evidence handling depends on records and controls from other governance domains:

- [`evidence-traceability-model.md`](evidence-traceability-model.md) defines the broader evidence traceability model.
- [`evidence-reference-requirements.md`](evidence-reference-requirements.md) defines required evidence reference fields and attribution metadata.
- [`finding-support-requirements.md`](finding-support-requirements.md) defines evidence support requirements for findings, recommendations, and report content.
- [`evidence-audit-replay.md`](evidence-audit-replay.md) defines audit and replay requirements for evidence access, derived artifacts, findings, review, approval, and release.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines local/private LLM-assisted DFIR boundaries and review workflow.
- [`../tool-access/readme.md`](../tool-access/readme.md) defines scoped tool execution, restricted tool patterns, and tool audit expectations.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines PDP, PEP, policy decision, approval policy, and fail-closed behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) defines review, formal approval, customer approval, escalation, and review record expectations.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, and cross-tenant boundary controls.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines audit event, replayability, correlation, exception, failure, and immutable audit expectations.

## Acceptance Criteria

DFIR evidence handling is acceptable when:

- source evidence, working copies, derived artifacts, summaries, timelines, findings, and report drafts remain clearly separated;
- evidence objects and evidence references have stable identifiers;
- tenant identity and customer identity are preserved separately for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- evidence use remains scoped to approved tenant, customer, case, matter, workspace, source, retention, legal hold, allowed-use, and access boundaries;
- integrity references and chain-of-custody references are preserved where applicable;
- derived artifacts preserve source evidence references, transformation records, tool or model context, limitations, and audit references;
- private/local LLM-assisted DFIR output remains draft and evidence-derived until examiner review and required approval are complete;
- retrieval, RAG, vector search, shared memory, customer context, case memory, and evidence retrieval remain within approved scope;
- findings, timelines, recommendations, and report sections identify supporting evidence, uncertainty, limitations, and conflicting evidence where applicable;
- customer-facing DFIR conclusions are linked to evidence support, examiner review, required approval, release scope, and audit records;
- evidence release, derived artifact export, and report release are governed by classification, sensitivity, allowed use, retention, review, approval, and audit requirements;
- corrections, supersessions, recalls, and reversals are appended as traceable records;
- audit replay can reconstruct evidence access, working-copy creation, transformation, derived artifacts, agent-assisted processing, examiner review, findings, approval, release, correction, recall, and final disposition;
- fail-closed handling exists for missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, integrity-failed, unsupported, or unauditable evidence context.
