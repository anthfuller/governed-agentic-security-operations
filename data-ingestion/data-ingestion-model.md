# Data Ingestion Model

## Purpose

This file defines the governed data-ingestion model for agent-assisted security operations across Managed SOC / MSSP, MDR, cloud incident response, detection engineering, threat hunting, and private/local LLM-assisted DFIR workflows.

The model describes how telemetry, operational records, enrichment context, evidence references, and sanitized intelligence enter governed workflows while preserving source attribution, tenant and customer boundaries, schema meaning, retention context, downstream-use constraints, and audit replayability.

Data ingestion provides governed inputs for investigation, correlation, triage, enrichment, reporting, policy evaluation, and audit replay. It does not authorize response actions, replace evidence systems, certify forensic conclusions, or grant agents permission to use tools or cross boundaries.

## Scope

This model applies to ingestion of:

- SIEM, XDR, EDR, NDR, firewall, identity, email, cloud, SaaS, ticketing, case-management, vulnerability, asset, and business-application telemetry;
- cloud audit records, identity activity, security alerts, incident records, asset context, and control-plane events;
- normalized event records, enrichment records, correlation context, and workflow-ready context packages;
- evidence references and evidence-derived metadata used by DFIR or investigation workflows;
- threat intelligence, customer-approved intelligence, and sanitized intelligence intended for controlled downstream use;
- local/private LLM-assisted DFIR extraction, parsing, summarization, or retrieval metadata when outputs are consumed by governed workflows.

This file does not define production collector configuration, SIEM deployment, parser code, schema implementation, storage architecture, MCP security controls, tool registration, PDP policy contracts, evidence repository design, or operational runbooks.

## Core Principles

- Ingested data MUST retain source attribution.
- Normalized records MUST NOT erase the original source meaning.
- Enrichment MUST be attributable, versioned where material, and distinguishable from source data.
- `tenant_id` and `customer_id` MUST remain separate where MSSP, MDR, DFIR, customer-scoped, or multi-customer workflows apply.
- Case-bound data MUST remain tied to the approved `case_id`, workflow, and evidence scope.
- Evidence-derived records MUST reference evidence objects instead of replacing original evidence.
- Agent-consumable context MUST be scoped before use.
- Tool availability, connector success, parser success, enrichment success, or index availability MUST NOT be treated as authorization.
- Data-ingestion failures that affect governed decisions, customer-facing outputs, evidence interpretation, policy decisions, or sensitive actions MUST fail closed or route to governed review.
- Ingestion records MUST support audit replay without relying on model memory or analyst narrative alone.

## Ingestion Model Overview

Governed ingestion transforms source records into scoped, validated, and replayable records for downstream workflows.

| Stage | Purpose | Required Control Outcome |
|---|---|---|
| Source onboarding | Register source systems, owners, scope, classification, and retention expectations. | Source identity, owner, tenant/customer scope, and allowed use are known before ingestion. |
| Collection | Collect records from approved sources through approved connectors, agents, APIs, streams, exports, or local DFIR workflows. | Collection remains within approved source, identity, tenant, customer, case, and workflow scope. |
| Source validation | Validate source metadata, timestamps, identifiers, completeness, and integrity indicators where available. | Invalid, ambiguous, stale, or unauthorized records are blocked, quarantined, or routed for review. |
| Parsing | Convert source records into structured fields without losing original source references. | Parser identity and version are preserved where parsing affects field meaning. |
| Normalization | Map parsed records into governed schemas for correlation, triage, enrichment, policy evaluation, and replay. | Normalized records preserve source fields, schema version, transformation context, and limitations. |
| Enrichment | Add asset, identity, threat intelligence, vulnerability, cloud, case, customer, or evidence context. | Enrichment source, timestamp, freshness, version, and confidence or limitation signals are preserved. |
| Routing | Route records to case stores, SIEM/XDR workflows, evidence-aware workflows, knowledge stores, vector indexes, reports, or audit stores. | Destination, output use, retention, customer boundary, and approval requirements are enforced. |
| Downstream consumption | Provide scoped data for agents, analysts, Agent Judges, PDP evaluation, customer review, and audit replay. | Downstream users receive only authorized, scoped, replayable context. |

## Required Ingestion Record Fields

Governed ingestion records SHOULD preserve the fields needed to reconstruct source, transformation, scope, routing, and downstream use.

| Field | Requirement | Purpose |
|---|---|---|
| `ingestion_record_id` | MUST | Unique identifier for the governed ingestion record. |
| `source_event_id` | MUST when available | Preserves the source system's event or record identifier. |
| `source_system_id` | MUST | Identifies the source platform, system, repository, evidence store, or telemetry source. |
| `source_system_type` | MUST | Identifies SIEM, XDR, EDR, cloud, identity, email, SaaS, firewall, ticketing, case, evidence, asset, vulnerability, or local DFIR source type. |
| `source_owner` | MUST for governed sources | Identifies accountable owner for the source integration. |
| `connector_id` | MUST when connector-based ingestion is used | Identifies the connector, collector, API integration, agent, export process, or local import path. |
| `connector_version` | MUST when version affects parsing, replay, or interpretation | Supports troubleshooting, regression review, and audit replay. |
| `collection_rule_id` | MUST when rules select records, fields, sources, or destinations | Identifies what collection rule controlled ingestion. |
| `collector_identity` | MUST when available | Identifies the workload, service identity, account, or examiner workflow that collected the record. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when case-bound | Links ingestion to the investigation, incident, ticket, or DFIR matter. |
| `workflow_id` | MUST for governed workflows | Links ingestion to the governed workflow consuming the data. |
| `workspace_id` | MUST when workspace scope affects access or interpretation | Preserves SIEM, XDR, logging, or analytics workspace boundary. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud scope applies | Preserves cloud account, subscription, or project boundary. |
| `source_timestamp_utc` | MUST when available | Records when the event occurred or was generated by the source. |
| `collection_timestamp_utc` | MUST | Records when the record was collected. |
| `ingestion_timestamp_utc` | MUST | Records when the record entered the governed ingestion flow. |
| `parser_id` | MUST when parsing is applied | Identifies the parser used to transform source data. |
| `parser_version` | MUST when parsing affects field meaning | Supports schema replay, troubleshooting, and dispute review. |
| `normalization_schema` | MUST when normalized output is produced | Identifies the target schema family. |
| `schema_version` | MUST when normalized output is produced | Identifies the normalized schema version. |
| `parser_or_transformation_version` | MUST when transformation changes downstream interpretation | Supports replay and regression analysis. |
| `data_classification` | MUST when handling depends on sensitivity, privacy, customer, legal, or regulated context | Preserves handling requirements. |
| `sensitivity_label` | MUST when applicable | Preserves handling label context. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted workflow, case, reporting, evidence, governance, or customer use. |
| `retention_policy_id` | MUST when retention applies | Preserves retention and disposal boundary. |
| `destination_system_id` | MUST when records are routed, indexed, stored, exported, or consumed downstream | Identifies destination system or workflow. |
| `output_destination` | MUST when output destination affects handling | Identifies case store, ticketing system, report store, evidence-aware workflow, knowledge store, vector index, audit store, or customer channel. |
| `evidence_object_ids` | MUST when evidence is referenced or derived | Preserves evidence traceability. |
| `evidence_tenant_ids` | MUST when evidence is referenced in tenant-scoped workflows | Preserves evidence-to-tenant attribution. |
| `evidence_customer_ids` | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer attribution. |
| `enrichment_refs` | MUST when enrichment is applied | Identifies enrichment records, source, timestamp, and version where available. |
| `knowledge_store_or_memory_scope` | MUST when retrieved context, RAG, vector search, shared memory, customer context, case memory, or evidence retrieval influences downstream use | Defines approved retrieval and memory boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval remained within approved boundaries. |
| `policy_context_id` | MUST when policy affects access, routing, release, retention, or fail-closed behavior | Links ingestion to applicable policy context. |
| `approval_record_id` | MUST when downstream use depends on approval | Links ingestion use to scoped approval. |
| `audit_reference_id` | MUST for governed workflows | Supports replay and audit reconstruction. |
| `correlation_ids` | MUST when available | Links source, workflow, case, evidence, policy, approval, tool, enrichment, and audit records. |
| `limitations` | MUST where material | Records incomplete fields, stale context, partial collection, parser uncertainty, enrichment gaps, or unsupported assumptions. |

## Source System Requirements

Each governed source MUST have a source record that defines:

- source owner and accountable maintainer;
- source type and operational purpose;
- tenant, customer, workspace, account, subscription, project, case, or evidence scope;
- approved collection method;
- expected timestamp fields and clock assumptions;
- data classification and sensitivity handling;
- retention policy and legal hold handling where applicable;
- allowed use and prohibited downstream use;
- approved destination systems and output destinations;
- required parser, schema, and enrichment expectations;
- failure owner and escalation path;
- audit and replay requirements.

A source MUST NOT be ingested into governed workflows when ownership, scope, classification, retention, or allowed use cannot be resolved.

## Collection Requirements

Collection MUST be explicit and scoped.

| Requirement | Description |
|---|---|
| Approved source | Collection MUST occur only from registered sources or approved case/evidence import paths. |
| Approved identity | Collection MUST use approved workload, service, analyst, examiner, or integration identity. |
| Scoped operation | Collection MUST remain within approved tenant, customer, case, workspace, account, subscription, project, evidence, and workflow scope. |
| Field control | Collection rules SHOULD define required, optional, excluded, minimized, and sensitive fields. |
| Time control | Collection SHOULD preserve source time, collection time, ingestion time, and known clock limitations. |
| Destination control | Collection MUST define where records may be routed, stored, indexed, exported, or consumed. |
| Auditability | Collection MUST emit enough metadata for replay, failure review, and downstream validation. |

Collection success MUST NOT imply that the data is complete, accurate, authorized for all downstream use, or ready for customer-facing output.

## Parsing and Normalization Requirements

Parsing and normalization MUST preserve source meaning while making records usable by governed workflows.

| Control | Requirement |
|---|---|
| Source preservation | Original source references, source field names, source event identifiers, and source timestamps MUST be preserved or referenceable. |
| Parser accountability | Parser identity and parser version MUST be recorded when parsing affects interpretation. |
| Schema accountability | Normalized records MUST identify schema family and schema version. |
| Transformation traceability | Transformations that change field meaning, severity, identity, asset, event category, or evidence interpretation MUST be recorded. |
| Loss awareness | Dropped, minimized, redacted, or unavailable fields SHOULD be represented through limitations or transformation metadata. |
| Type validation | Normalized fields SHOULD be validated against expected type, format, range, and enum constraints. |
| Boundary preservation | Tenant, customer, case, workspace, subscription/account, evidence, and retention boundaries MUST survive normalization. |

Normalized records MUST NOT be treated as original evidence, final incident truth, or proof that a source event was complete.

## Enrichment Requirements

Enrichment adds context to ingested records. It MUST remain attributable and controlled.

Common enrichment sources include:

- asset inventory;
- identity and access context;
- cloud account, subscription, project, resource, and control-plane context;
- vulnerability and exposure context;
- threat intelligence and indicator context;
- detection, analytic, rule, and ATT&CK/ATLAS mapping context;
- case, ticket, timeline, and workflow context;
- evidence references and examiner-provided context;
- customer-approved sanitized intelligence.

Enrichment MUST preserve:

- enrichment source;
- enrichment timestamp;
- freshness or staleness indicators where available;
- enrichment version where material;
- confidence, limitation, or unresolved-state indicators where material;
- tenant, customer, case, evidence, and retention scope;
- downstream-use constraints.

Enrichment MUST NOT override source data silently. Conflicts between source data and enrichment MUST be preserved, resolved through governed logic, or routed to review.

## Routing and Destination Requirements

Ingested and enriched records MAY be routed to downstream systems only when destination controls allow it.

| Destination | Required Handling |
|---|---|
| SIEM or analytics store | Preserve source, schema, tenant/customer, classification, retention, and audit context. |
| Case or ticketing system | Preserve case scope, customer scope, workflow stage, evidence references, and release limitations. |
| Evidence-aware workflow | Preserve evidence object references, attribution, transformation history, and examiner review requirements. |
| Knowledge store or vector index | Preserve retrieval scope, retention, freshness, allowed use, source references, and exclusion rules. |
| Agent context package | Include only authorized, scoped, current-enough, and replayable context. |
| Agent Judge input | Preserve evidence support, tenant/customer scope, source references, and limitations. |
| Policy evaluation input | Preserve requested action context, source and destination scope, data classification, allowed use, and evidence references. |
| Customer-facing report workflow | Preserve evidence support, review record, approval record, release scope, classification, and limitations. |
| Audit store | Preserve identifiers and references needed for replay while minimizing unnecessary sensitive content. |

Routing MUST fail closed or route to review when the destination is missing, ambiguous, unauthorized, inconsistent with retention, inconsistent with allowed use, or outside tenant, customer, case, evidence, or workflow scope.

## Agent Use of Ingested Data

Agents MAY use ingested data to:

- summarize scoped telemetry;
- correlate related events;
- identify investigative pivots;
- draft incident timelines;
- propose triage or escalation rationale;
- prepare evidence-supported review packages;
- recommend policy-gated next steps;
- support detection engineering or threat hunting review;
- draft customer-facing material for review and approval.

Agents MUST NOT:

- treat ingested data as authorization to act;
- cross tenant, customer, case, evidence, workspace, account, subscription, project, retention, or retrieval boundaries;
- treat normalized or enriched records as original evidence;
- hide source limitations, parsing gaps, enrichment gaps, stale data, or unsupported assumptions;
- convert a partial ingestion result into a definitive incident conclusion;
- release customer-facing content without required review and approval;
- use retrieved context, vector results, shared memory, or case memory outside approved scope;
- retry denied or approval-required actions through alternate data paths.

## Evidence-Aware Ingestion

When ingestion touches evidence or evidence-derived data:

- original evidence MUST remain controlled by the evidence-handling model;
- ingestion records MUST reference evidence object identifiers rather than replacing evidence objects;
- evidence tenant and customer attribution MUST be preserved;
- source timestamps, collection timestamps, transformation history, and parser versions MUST be preserved where applicable;
- evidence-derived summaries MUST remain distinguishable from original evidence;
- examiner review MUST remain separate from parser, model, or enrichment success;
- customer-facing DFIR conclusions MUST require evidence validation, human review, auditability, and the appropriate approval path.

## Retrieval, Memory, and Indexing Boundaries

When ingested data is indexed, embedded, retrieved, or reused through knowledge stores, vector indexes, shared memory, customer context, case memory, RAG, or evidence retrieval:

- `knowledge_store_or_memory_scope` MUST be defined before use in governed workflows;
- retrieval MUST remain within approved tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundaries;
- retrieval results MUST preserve source references and retrieval metadata where available;
- `knowledge_memory_scope_result` MUST be recorded when retrieval or memory scope is evaluated;
- stale, cross-tenant, cross-customer, cross-case, unauthorized, or retention-inconsistent retrieval MUST fail closed or route to governed review;
- indexed data MUST not become a bypass around source access, evidence handling, approval, or retention controls.

## Shared Intelligence Handling

Shared intelligence derived from customer, tenant, case, or evidence material MUST NOT be distributed until sanitization, de-identification, approval, versioning, release scope, and audit requirements are satisfied.

Only sanitized and approved intelligence may be reused across tenants or customers. Raw customer data, raw evidence, tenant-specific identifiers, unapproved case details, and source records MUST NOT leave their approved boundary through the ingestion pipeline.

## Failure Handling

The ingestion flow MUST fail closed, quarantine, suppress downstream use, or route to review when:

- source registration is missing, stale, revoked, or inconsistent;
- required tenant, customer, case, workflow, workspace, account, subscription, source, evidence, destination, classification, retention, or allowed-use context is missing;
- collection identity or connector scope is unauthorized;
- source timestamps, record identifiers, or required fields are missing where downstream use depends on them;
- parser validation fails;
- schema validation fails;
- transformation changes cannot be reconstructed;
- enrichment source, freshness, or attribution is missing where downstream use depends on it;
- evidence attribution is missing or inconsistent;
- retrieval or memory scope is missing, stale, unauthorized, cross-tenant, cross-customer, cross-case, or retention-inconsistent;
- destination routing is unauthorized or ambiguous;
- audit logging fails where audit is mandatory;
- downstream workflow requires complete ingestion but receives partial, stale, inconsistent, or unsupported records.

Failure handling MUST preserve the original request or collection event, source context, error reason, affected scope, downstream systems blocked or quarantined, owner, routing result, and audit reference.

## Audit and Replay Requirements

Data ingestion MUST emit audit records sufficient to reconstruct:

- which source system produced the record;
- which connector, collection rule, parser, schema, and transformation versions were used;
- which tenant, customer, case, workflow, workspace, subscription/account, project, evidence, and destination scope applied;
- when the source event occurred, when it was collected, and when it was ingested;
- what normalization and enrichment occurred;
- which fields, records, or enrichment were excluded, minimized, redacted, blocked, stale, or unavailable;
- which downstream workflow, agent, judge, policy request, approval package, case, report, or audit record consumed the data;
- which failures, denials, quarantine events, retries, corrections, or release decisions occurred;
- which final state was reached.

Audit replay MUST be able to inspect and challenge the decision path without relying on model memory, undocumented assumptions, or unsupported narrative summaries.

## Relationship to Other Control Areas

| Control Area | Relationship |
|---|---|
| [`source-system-metadata.md`](source-system-metadata.md) | Defines source identity, ownership, scope, classification, retention, and source control expectations. |
| [`normalization-and-enrichment.md`](normalization-and-enrichment.md) | Defines detailed normalization, enrichment, schema, mapping, and attribution requirements. |
| [`ingestion-failure-handling.md`](ingestion-failure-handling.md) | Defines detailed failure, quarantine, retry, suppression, and review routing expectations. |
| [`ingestion-audit-replay.md`](ingestion-audit-replay.md) | Defines ingestion-specific audit and replay requirements. |
| [`shared-intelligence-sanitization-and-release-controls.md`](shared-intelligence-sanitization-and-release-controls.md) | Defines controls for sanitized intelligence release and cross-tenant-safe reuse. |
| [`../tool-access/readme.md`](../tool-access/readme.md) | Defines governed tool registration, scoped tool execution, restricted tool use, and tool execution audit. |
| [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) | Defines PDP, PEP, policy decision, approval policy, risk classification, and fail-closed behavior. |
| [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) | Defines tenant, customer, case, and cross-tenant boundary controls. |
| [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) | Defines evidence references, finding support, DFIR evidence handling, and evidence audit replay. |
| [`../audit-replay/readme.md`](../audit-replay/readme.md) | Defines audit event, replayability, correlation, exception, failure, and immutable audit expectations. |

## Operational Anti-Patterns

Avoid the following:

- ingesting sources without owner, scope, classification, retention, and allowed-use metadata;
- treating connector success as authorization;
- treating normalized records as original evidence;
- silently overwriting source fields with enrichment values;
- dropping source identifiers, parser versions, schema versions, or transformation history;
- merging tenant and customer identity into a single ambiguous field;
- routing records to cases, reports, knowledge stores, vector indexes, or customer channels without destination controls;
- allowing agents to consume unscoped, stale, cross-customer, cross-tenant, or cross-case context;
- using retrieved context without source references, retrieval scope, freshness, and retention validation;
- allowing shared intelligence release from raw customer or evidence data without sanitization and approval;
- allowing customer-facing output to rely on unsupported, partial, stale, or unauditable ingestion results;
- failing open when required ingestion, source, scope, schema, enrichment, evidence, retrieval, destination, approval, or audit metadata is missing.

## Acceptance Criteria

This file is acceptable when the data-ingestion model ensures that:

- source systems are identified, owned, scoped, classified, and governed before use;
- ingestion preserves tenant and customer identity separately where required;
- collection, parsing, normalization, enrichment, routing, indexing, and downstream use remain replayable;
- normalized and enriched records preserve source attribution and limitations;
- evidence-derived records reference original evidence without replacing it;
- retrieved context and memory use remain scoped by tenant, customer, case, evidence, retention, freshness, and allowed-use boundaries;
- agents consume only scoped and governed context;
- ingestion does not authorize tool execution, response actions, customer-facing release, evidence release, or policy exceptions;
- failure handling blocks, quarantines, suppresses, or routes unsafe ingestion states for review;
- audit replay can reconstruct source, collection, parser, schema, enrichment, destination, workflow, policy, approval, evidence, and final-state context.
