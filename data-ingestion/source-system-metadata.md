# Source System Metadata

## Purpose

This file defines the required metadata for source systems, connectors, collection rules, source records, and provenance used by governed data-ingestion workflows.

Source-system metadata allows downstream workflows to understand where data came from, who owns it, which tenant, customer, case, workspace, account, or evidence scope applies, how it was collected, how it may be used, how long it may be retained, and whether it is fit for governed use.

Source metadata supports ingestion validation, normalization, enrichment, policy evaluation, tenant and customer boundary checks, evidence traceability, audit replay, and controlled downstream use. It does not authorize tool execution, response action, customer release, evidence release, case closure, or formal approval.

## Scope

This file applies to source metadata for:

- SIEM, XDR, EDR, NDR, firewall, identity, email, cloud, SaaS, vulnerability, asset, ticketing, case-management, and business-application sources;
- connectors, collectors, agents, APIs, exports, event streams, queues, message pipelines, batch files, local import paths, and private/local DFIR collection paths;
- source systems used for telemetry, alert, incident, asset, identity, control-plane, enrichment, evidence, case, report, workflow, knowledge, or audit context;
- source records collected, parsed, normalized, enriched, indexed, summarized, routed, or referenced by governed workflows;
- private/local LLM-assisted DFIR workflows that import, parse, extract, summarize, or route evidence-derived metadata;
- shared intelligence workflows that derive reusable security knowledge from scoped ingestion outputs.

This file does not define production connector configuration, vendor-specific API setup, SIEM schema implementation, evidence repository design, legal sufficiency, chain-of-custody procedure, tool registration, MCP security, PDP policy contracts, or operational runbooks.

## Core Principles

- Every governed source MUST have an accountable owner.
- Source identity MUST be stable enough to support audit replay.
- `tenant_id` and `customer_id` MUST remain separate where MSSP, MDR, DFIR, customer-scoped, or multi-customer workflows apply.
- Source metadata MUST preserve native source identifiers where available.
- Collection metadata MUST identify how, when, and by which identity a record was collected.
- Source timestamps, collection timestamps, and ingestion timestamps MUST remain distinguishable.
- Source records, parsed records, normalized records, enriched records, summarized outputs, and routed outputs MUST remain distinguishable.
- Source metadata MUST preserve data classification, sensitivity, retention, allowed use, and destination constraints where applicable.
- Source metadata MUST identify known limitations, trust assumptions, freshness expectations, and schema dependencies.
- Source metadata MUST NOT be invented, silently inferred, overwritten, or repaired by agents without governed review.
- Missing, ambiguous, stale, unauthorized, inconsistent, or unauditable source metadata MUST trigger quarantine, controlled review, degraded handling, or fail-closed behavior where governed workflow behavior depends on it.

## Source Metadata Model

Governed data ingestion depends on several related metadata records.

| Metadata Record | Purpose |
|---|---|
| Source-system registration record | Defines the source system, owner, environment, scope, classification, retention, allowed use, and approved destinations. |
| Connector record | Defines the connector, collector, API integration, agent, export process, or local import path used to collect records. |
| Collection-rule record | Defines which records, fields, time ranges, scopes, and destinations are included or excluded. |
| Source-record metadata | Preserves source-native identifiers, timestamps, format, integrity indicators, scope, and raw-record references. |
| Provenance record | Links source, connector, collection rule, parser, normalization, enrichment, routing, evidence, policy, approval, and audit context. |
| Source-quality record | Records completeness, freshness, schema compatibility, trust level, known limitations, and validation results. |

These records may be stored separately or embedded in a larger ingestion record. The architecture requirement is that the relationships remain reconstructable.

## Source-System Lifecycle States

Source systems SHOULD have explicit lifecycle state.

| State | Meaning | Allowed Handling |
|---|---|---|
| `CANDIDATE` | Source has been identified but not approved for governed ingestion. | Evaluation only. No governed downstream use. |
| `REGISTERED` | Required ownership, scope, classification, and collection metadata have been recorded. | Limited testing or controlled onboarding. |
| `ACTIVE` | Source is approved for governed ingestion within defined scope. | Governed collection and downstream routing may occur. |
| `REVIEW_REQUIRED` | Source metadata, scope, quality, ownership, retention, or authorization requires review. | Hold, quarantine, or restrict use until review completes. |
| `SUSPENDED` | Source is temporarily disabled because of failure, drift, policy issue, boundary risk, or audit concern. | Do not use for governed decisions unless an approved exception applies. |
| `DEPRECATED` | Source remains referenceable for replay but should not be used for new ingestion. | Preserve replay access. Restrict new use. |
| `RETIRED` | Source is no longer used. | Preserve historical references according to retention requirements. |
| `BLOCKED` | Source is prohibited for governed ingestion. | Do not collect or route. Preserve audit reason. |

A source moving from `CANDIDATE` or `REGISTERED` to `ACTIVE` SHOULD have an accountable approval or governance record where policy requires it.

## Required Source-System Registration Record

Every source system used by governed workflows MUST have a registration record.

| Field | Requirement | Purpose |
|---|---|---|
| `source_system_id` | MUST | Unique identifier for the source system. |
| `source_system_name` | MUST | Human-readable source name. |
| `source_system_type` | MUST | Identifies SIEM, XDR, EDR, NDR, firewall, identity, email, cloud, SaaS, ticketing, case, evidence, asset, vulnerability, enrichment, knowledge, report, workflow, audit, or local DFIR source type. |
| `source_system_owner` | MUST | Identifies accountable owner for the source. |
| `technical_owner` | MUST for governed sources | Identifies owner responsible for connector health, schema changes, and integration support. |
| `data_owner` | MUST when data-handling, privacy, legal, customer, or retention constraints apply | Identifies owner responsible for data-use expectations. |
| `service_owner` | SHOULD | Identifies MSSP, MDR, SOC, DFIR, cloud IR, detection engineering, or platform owner. |
| `source_environment` | MUST | Identifies production, staging, lab, local, private, customer-specific, or test environment. |
| `source_lifecycle_state` | MUST | Records candidate, registered, active, review-required, suspended, deprecated, retired, or blocked state. |
| `source_native_system_id` | SHOULD when available | Preserves source-native system identifier. |
| `source_native_tenant_id` | MUST when the source platform has native tenant scope | Preserves the source platform tenant identifier separately from governed `tenant_id`. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves governed tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `workspace_id` | MUST when workspace scope affects telemetry, access, routing, or downstream interpretation | Preserves SIEM, XDR, logging, analytics, or security workspace scope. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud scope applies | Preserves cloud account, subscription, project, or organization boundary. |
| `region` or `data_residency_scope` | MUST when residency, sovereignty, privacy, or customer agreement affects handling | Preserves regional and data-residency context. |
| `case_scope_supported` | MUST when records can be bound to incidents, investigations, tickets, or DFIR matters | Identifies whether and how records may be case-bound. |
| `evidence_source_indicator` | MUST when the source can provide evidence or evidence-derived metadata | Identifies whether the source may produce evidence references or forensic artifacts. |
| `authoritative_for` | SHOULD | Identifies fields, entities, or facts for which the source is considered authoritative. |
| `not_authoritative_for` | SHOULD | Identifies fields, entities, or facts the source must not be treated as authoritative for. |
| `source_trust_level` | SHOULD | Records trusted, partially trusted, untrusted, unknown, or review-required status. |
| `known_limitations` | MUST when limitations affect interpretation | Records gaps, delay, sampling, field loss, false-positive risk, partial collection, parser dependency, or source-quality limits. |
| `expected_latency` | SHOULD | Defines normal delay between source event creation and collection. |
| `freshness_requirement` | MUST when downstream use depends on current data | Defines maximum acceptable age for governed use. |
| `expected_volume_profile` | SHOULD | Supports anomaly detection for missing, duplicate, delayed, or excessive records. |
| `collection_methods` | MUST | Identifies approved API, stream, export, agent, file, local import, evidence import, or manual collection methods. |
| `approved_connector_ids` | MUST when connector-based collection is used | Identifies connectors authorized for this source. |
| `approved_collection_rule_ids` | MUST when collection rules govern selection or routing | Identifies rules authorized for this source. |
| `approved_operations` | MUST | Defines allowed operations such as collect, read, retrieve, parse, normalize, enrich, route, index, or reference. |
| `prohibited_operations` | MUST where misuse is possible | Defines operations the ingestion path must not perform. |
| `approved_destinations` | MUST when records are routed or consumed downstream | Defines approved case stores, ticketing systems, evidence-aware workflows, knowledge stores, vector indexes, report stores, audit stores, or internal workflows. |
| `prohibited_destinations` | MUST where destination misuse is possible | Defines destinations that must not receive records from this source. |
| `data_classification` | MUST when classification affects access, routing, retention, release, approval, evidence handling, or downstream use | Preserves handling expectations. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, customer, or regulated handling label. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use such as triage, investigation, enrichment, evidence support, reporting draft, audit replay, detection engineering, threat hunting, or shared-intelligence candidate. |
| `disallowed_use` | SHOULD | Defines prohibited downstream use. |
| `retention_policy_id` | MUST when retention affects source data, transformed data, indexed data, retrieved context, or audit replay | Preserves retention and disposal boundary. |
| `legal_hold_support` | MUST when legal hold may apply | Identifies whether and how records can be preserved. |
| `schema_family` | SHOULD | Identifies source schema family or event family. |
| `source_schema_version` | MUST when available and material to parsing or replay | Supports parser selection and interpretation. |
| `parser_dependencies` | MUST when parsing affects field meaning | Identifies parser IDs or parser families expected for the source. |
| `normalization_schema_targets` | SHOULD | Identifies approved normalized schema targets. |
| `enrichment_dependencies` | SHOULD | Identifies enrichment sources or enrichment classes normally applied. |
| `time_zone` | MUST when timestamps are not UTC or require conversion | Preserves source timestamp interpretation. |
| `clock_sync_expectation` | SHOULD | Records expected source clock behavior and known drift limitations. |
| `integrity_support` | SHOULD | Identifies source signatures, hashes, manifests, sequence numbers, immutable log capability, or tamper-evidence support where available. |
| `audit_logging_support` | MUST for governed sources | Identifies whether source access, collection, export, failure, and routing activity can be audited. |
| `audit_reference_id` | MUST when source registration is consumed by governed workflows | Supports replay and governance review. |
| `policy_context_id` | MUST when policy affects collection, routing, retention, release, or fail-closed handling | Links source registration to applicable policy context. |
| `approval_record_id` | MUST when source activation, sensitive collection, destination routing, evidence use, or shared intelligence use requires formal approval | Links the source to approval authority and scope. |
| `correlation_ids` | MUST when available | Links source registration to connector, collection rule, policy, approval, audit, evidence, and workflow records. |

## Connector Metadata Requirements

Connectors, collectors, API integrations, agents, export jobs, local import paths, or private/local DFIR import mechanisms MUST be identifiable separately from the source system.

| Field | Requirement | Purpose |
|---|---|---|
| `connector_id` | MUST | Unique identifier for the connector or collection mechanism. |
| `connector_name` | MUST | Human-readable connector name. |
| `connector_version` | MUST when version affects parsing, field mapping, failure handling, or replay | Supports troubleshooting and regression review. |
| `connector_owner` | MUST | Identifies accountable owner for connector configuration and lifecycle. |
| `connector_type` | MUST | Identifies API, stream, event hub, queue, file export, collector agent, endpoint agent, cloud connector, local import, manual import, or evidence import. |
| `connector_environment` | MUST | Identifies production, staging, lab, local, private, or customer-specific connector context. |
| `source_system_id` | MUST | Links connector to the source system. |
| `collector_identity` | MUST | Identifies service identity, managed identity, delegated account, workload identity, examiner workflow, or approved collection identity. |
| `credential_reference` | MUST when credentials are used | References credential material without exposing secrets. |
| `authorized_operations` | MUST | Defines operations permitted for the connector. |
| `prohibited_operations` | MUST where sensitive misuse is possible | Defines operations the connector must not perform. |
| `network_or_execution_boundary` | SHOULD | Identifies execution zone, local boundary, private boundary, cloud boundary, or customer-specific boundary. |
| `rate_limit_or_collection_limit` | SHOULD | Records limits that can affect completeness or timeliness. |
| `retry_behavior` | MUST when retry affects duplicates, ordering, or replay | Defines retry behavior and idempotency expectations. |
| `deduplication_strategy` | SHOULD | Defines duplicate detection or sequence handling. |
| `failure_routing` | MUST | Defines quarantine, review, retry, degraded mode, or fail-closed handling. |
| `schema_output_contract` | MUST when connector output is structured | Defines expected output format and schema. |
| `logging_requirements` | MUST | Defines required access, request, response, failure, and routing logs. |
| `approval_record_id` | MUST when connector use requires approval | Links connector use to approval authority and scope. |
| `audit_reference_id` | MUST for governed workflows | Supports audit replay. |

Connector success MUST NOT be treated as proof that the source record is complete, current, correctly scoped, authorized for downstream use, or approved for release.

## Collection Rule Metadata Requirements

Collection rules define what is collected, filtered, excluded, transformed, or routed from a source.

| Field | Requirement | Purpose |
|---|---|---|
| `collection_rule_id` | MUST | Unique identifier for the collection rule. |
| `collection_rule_name` | MUST | Human-readable rule name. |
| `collection_rule_version` | MUST | Supports replay and change review. |
| `rule_owner` | MUST | Identifies accountable owner. |
| `source_system_id` | MUST | Links the rule to the source. |
| `connector_id` | MUST when connector-based collection is used | Links rule to connector. |
| `selection_criteria` | MUST | Defines records, event types, tables, indexes, fields, queries, labels, evidence sets, or time ranges included. |
| `exclusion_criteria` | MUST when data is intentionally excluded | Defines excluded records, fields, labels, sources, evidence sets, tenants, customers, cases, or destinations. |
| `scope_filters` | MUST when tenant, customer, workspace, subscription/account, case, evidence, or region scope applies | Defines required boundary filters. |
| `field_allowlist` | SHOULD when data minimization applies | Defines fields allowed for collection. |
| `field_denylist` | SHOULD when sensitive fields must be excluded | Defines fields not allowed for collection. |
| `sampling_or_truncation_behavior` | MUST when applied | Records whether records are sampled, truncated, aggregated, or summarized. |
| `collection_window` | SHOULD | Defines scheduled, streaming, batch, historical, backfill, or case-specific collection window. |
| `backfill_authorization` | MUST when historical backfill is allowed | Defines approved scope and constraints for historical collection. |
| `destination_system_id` | MUST when rule routes records downstream | Identifies approved destination. |
| `output_destination` | MUST when destination affects handling | Defines case, ticketing, evidence, knowledge, vector index, report, workflow, audit, or shared intelligence destination. |
| `data_classification` | MUST when rule affects data classification or sensitivity handling | Preserves classification context. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use of collected output. |
| `retention_policy_id` | MUST when retention applies | Preserves retention and disposal boundary. |
| `policy_context_id` | MUST when policy affects collection or routing | Links rule to applicable policy. |
| `approval_record_id` | MUST when rule activation, sensitive collection, backfill, evidence access, shared intelligence routing, or cross-boundary handling requires approval | Links rule to scoped approval. |
| `audit_reference_id` | MUST | Supports replay. |

Collection rules MUST NOT silently broaden scope, add destinations, collect new sensitive fields, or alter evidence handling without governed change control.

## Source Record Metadata Requirements

Every source record consumed by governed workflows SHOULD preserve source-record metadata sufficient for review and replay.

| Field | Requirement | Purpose |
|---|---|---|
| `source_record_id` | MUST when available | Preserves source-native record traceability. |
| `source_event_id` | MUST when available | Preserves event-level traceability. |
| `source_system_id` | MUST | Identifies originating source. |
| `source_system_type` | MUST | Identifies source class. |
| `source_native_tenant_id` | MUST when available | Preserves native source tenant scope. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves governed tenant scope. |
| `customer_id` | MUST for customer-scoped workflows | Preserves customer boundary separately from tenant identity. |
| `workspace_id` | MUST when workspace scope applies | Preserves workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud scope applies | Preserves cloud account or project context. |
| `case_id` | MUST when source record is case-bound | Links the record to the governed matter. |
| `evidence_object_ids` | MUST when source record is evidence or evidence-derived | Links record to evidence objects. |
| `source_event_type` | MUST when available | Preserves event type. |
| `source_record_format` | SHOULD | Identifies JSON, XML, CSV, log line, binary metadata, export package, API response, archive manifest, or local import format. |
| `source_schema_version` | SHOULD when available | Supports parser selection and replay. |
| `source_timestamp_utc` | MUST when available | Records when the source event occurred. |
| `source_observed_timestamp_utc` | SHOULD when available | Records when the source observed the event. |
| `collection_timestamp_utc` | MUST | Records when the record was collected or received. |
| `ingestion_timestamp_utc` | MUST | Records when the record entered governed ingestion. |
| `collector_identity` | MUST | Identifies the collection identity. |
| `connector_id` | MUST when connector-based collection is used | Identifies the connector. |
| `connector_version` | MUST when material to replay | Supports compatibility review. |
| `collection_rule_id` | MUST when a collection rule selected the record | Identifies collection selection logic. |
| `raw_record_reference` | MUST when raw record is stored or referenceable | References the original or canonical source record without uncontrolled copying. |
| `source_hash` | SHOULD when available or required | Supports integrity validation. |
| `sequence_number` | SHOULD when available | Supports gap, duplicate, and ordering checks. |
| `ingestion_batch_id` | SHOULD for batch collection | Links records collected together. |
| `data_classification` | MUST when classification affects handling | Preserves handling requirements. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity context. |
| `allowed_use` | MUST when constrained | Defines permitted downstream use. |
| `retention_policy_id` | MUST when retention applies | Preserves retention boundary. |
| `quality_state` | MUST for governed records | Records valid, partial, stale, duplicate, malformed, unsupported, review-required, quarantined, or blocked state. |
| `validation_results` | SHOULD | Records timestamp, schema, scope, source, integrity, and completeness validation results. |
| `limitations` | SHOULD when material | Records missing fields, partial collection, stale source, sampling, truncation, parser mismatch, or unsupported event type. |
| `audit_reference_id` | MUST | Supports replay and governance review. |
| `correlation_ids` | MUST when available | Links source record to ingestion, parsing, normalization, enrichment, evidence, policy, workflow, and audit records. |

Raw source records SHOULD be referenced rather than duplicated into every downstream record. Where raw records are copied, classification, retention, access control, and evidence-handling requirements MUST apply.

## Provenance Requirements

Provenance records link the source-to-output path.

Governed ingestion MUST preserve, where applicable:

- source-system registration reference;
- connector identity and version;
- collection rule identity and version;
- collector identity;
- source-native record identifiers;
- source, collection, and ingestion timestamps;
- parser identity and version;
- normalization schema and mapping version;
- enrichment source, timestamp, freshness, and version;
- tenant, customer, workspace, subscription/account, case, and evidence scope;
- data classification, sensitivity, allowed use, and retention policy;
- destination system and output destination;
- policy context, approval record, audit reference, and correlation identifiers;
- validation, failure, quarantine, retry, correction, or replay records.

Provenance MUST remain available to downstream workflows that rely on ingested data for agent context, Agent Judge checks, analyst review, approval packages, reporting, policy decisions, evidence interpretation, or audit replay.

## Source Quality and Validation States

Source metadata SHOULD include a quality state before downstream use.

| Quality State | Meaning | Required Handling |
|---|---|---|
| `VALID` | Required metadata and validation checks passed. | May be consumed within approved scope. |
| `PARTIAL` | Record is usable only with limitations. | Preserve limitations and restrict use where needed. |
| `STALE` | Record or source is older than the freshness requirement. | Block, review, or use only where policy permits stale context. |
| `DUPLICATE` | Record appears to duplicate a previously collected record. | Deduplicate or preserve duplicate relationship for replay. |
| `MALFORMED` | Record does not match expected format or schema. | Quarantine or route to parser review. |
| `UNSUPPORTED` | Source type, event type, version, or format is unsupported. | Block or route to onboarding review. |
| `SCOPE_MISMATCH` | Tenant, customer, workspace, account, case, evidence, or destination scope does not match approved context. | Fail closed or route to controlled review. |
| `RETENTION_CONFLICT` | Retention or allowed-use constraints conflict with requested use. | Fail closed or route to policy review. |
| `REVIEW_REQUIRED` | Metadata is ambiguous or material uncertainty exists. | Hold until review completes. |
| `QUARANTINED` | Record is isolated from normal downstream use. | Preserve audit context and disposition. |
| `BLOCKED` | Record is prohibited for downstream use. | Do not route. Preserve reason. |

## Timestamp Requirements

Source, collection, ingestion, parsing, normalization, enrichment, and routing timestamps MUST remain distinguishable.

| Timestamp | Requirement |
|---|---|
| `source_timestamp_utc` | Records when the event occurred or was generated by the source, where available. |
| `source_observed_timestamp_utc` | Records when the source observed the event, where available. |
| `collection_timestamp_utc` | Records when the collector received or extracted the record. |
| `ingestion_timestamp_utc` | Records when the record entered governed ingestion. |
| `parsing_timestamp_utc` | Records when parsing occurred, where applicable. |
| `normalization_timestamp_utc` | Records when normalization occurred, where applicable. |
| `enrichment_timestamp_utc` | Records when enrichment occurred, where applicable. |
| `routing_timestamp_utc` | Records when output was routed downstream, where applicable. |

When source timestamps are unavailable, ambiguous, local-time-only, clock-skewed, or inconsistent, that limitation MUST be preserved and downstream use MUST be restricted where time accuracy affects investigation, detection, evidence interpretation, reporting, or policy evaluation.

## Classification, Retention, and Allowed Use

Source metadata MUST preserve handling constraints before records are routed downstream.

| Control Area | Requirement |
|---|---|
| Data classification | Source and record classification MUST be preserved where it affects access, routing, retention, release, evidence handling, reporting, or customer communication. |
| Sensitivity labels | Labels MUST remain attached to records, derived outputs, and indexed content where applicable. |
| Allowed use | Source metadata MUST define permitted downstream use where use is constrained. |
| Disallowed use | Prohibited uses SHOULD be recorded where misuse is likely. |
| Retention | Retention policy MUST apply to source records, transformed records, enriched records, indexed records, and retrieved context where applicable. |
| Legal hold | Legal hold context MUST be preserved where applicable. |
| Data minimization | Collection rules SHOULD collect only fields required for approved workflows. |
| Destination limits | Source output MUST be routed only to approved destinations. |

A record approved for internal triage MUST NOT automatically be approved for customer communication, shared intelligence release, evidence release, model memory, vector indexing, report publication, or response action.

## Tenant, Customer, Case, Workspace, Account, and Evidence Boundaries

Source metadata MUST preserve boundary context before downstream use.

| Boundary | Requirement |
|---|---|
| Tenant boundary | `tenant_id` or equivalent governed tenant scope MUST be preserved where applicable. |
| Customer boundary | `customer_id` MUST remain separate from `tenant_id` for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows. |
| Native source boundary | Source-native tenant, workspace, subscription, account, organization, or project identifiers SHOULD be preserved. |
| Workspace boundary | Workspace identifiers MUST be preserved when they affect source access, routing, or interpretation. |
| Cloud account boundary | Subscription, account, project, organization, and region scope MUST be preserved when cloud telemetry or control-plane events are collected. |
| Case boundary | Case-bound records MUST remain tied to the approved case or incident unless policy authorizes correlation. |
| Evidence boundary | Evidence-derived records MUST reference evidence objects and must not replace original evidence. |
| Retrieval boundary | Records routed to knowledge stores, vector indexes, shared memory, customer context, case memory, or evidence retrieval MUST preserve approved retrieval and reuse scope. |
| Destination boundary | Output destination MUST be validated before routing, indexing, release, or downstream consumption. |

Boundary metadata MUST be validated before records are used by agents, Agent Judges, analysts, policy workflows, approval packages, reports, shared intelligence releases, or evidence-aware workflows.

## Evidence and Private/Local DFIR Source Metadata

When a source is evidence, evidence-derived, or part of a private/local LLM-assisted DFIR workflow, additional metadata is required.

| Field | Requirement | Purpose |
|---|---|---|
| `evidence_object_ids` | MUST | Links source records or derived metadata to evidence objects. |
| `evidence_tenant_ids` | MUST when tenant scope applies | Preserves evidence-to-tenant attribution. |
| `evidence_customer_ids` | MUST when customer scope applies | Preserves evidence-to-customer attribution. |
| `evidence_collection_context` | MUST when available | References collection source, examiner workflow, acquisition method, and collection conditions. |
| `chain_of_custody_reference` | MUST when chain-of-custody applies | Links to chain-of-custody records without replacing them. |
| `examiner_identity` | MUST when local DFIR import or review is performed by an examiner | Preserves accountability. |
| `local_execution_context` | MUST for private/local LLM-assisted DFIR ingestion | Identifies local, private, lab, isolated, or customer-specific execution context. |
| `derived_output_indicator` | MUST when source output is extracted, summarized, transformed, or model-assisted | Distinguishes derived metadata from original evidence. |
| `evidence_handling_limitations` | SHOULD | Records constraints, incomplete extraction, unsupported artifacts, tool limitations, or review requirements. |

Local execution MUST be treated as an execution and evidence-handling context, not proof of correctness, evidentiary validity, or forensic completeness.

## Source Metadata for Knowledge Stores and Memory

When ingestion output is routed to knowledge stores, vector indexes, shared memory, customer context, case memory, evidence retrieval, or retrieved context, source metadata MUST preserve retrieval and reuse boundaries.

| Field | Requirement | Purpose |
|---|---|---|
| `knowledge_store_or_memory_scope` | MUST | Defines approved tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundary. |
| `source_support_refs` | MUST when indexed or retrieved content supports downstream output | Preserves source references for review and replay. |
| `index_id` or `store_id` | MUST when records are indexed | Identifies destination knowledge store, vector index, or memory store. |
| `index_version` | SHOULD when version affects retrieval or replay | Supports retrieval reconstruction. |
| `retrieval_allowed_use` | MUST | Defines whether content may be used for triage, investigation, report drafting, detection engineering, threat hunting, assurance checks, or shared intelligence. |
| `retrieval_disallowed_use` | SHOULD | Defines prohibited uses. |
| `expiration_time_utc` | SHOULD when freshness matters | Prevents stale reuse. |
| `recall_reference_id` | MUST when indexed content is recalled | Supports removal and downstream impact review. |

Raw tenant, customer, case, or evidence data MUST NOT be routed into shared knowledge stores, vector indexes, or shared memory unless sanitization, scope, retention, approval, destination, and audit controls allow it.

## Agent Use of Source Metadata

Agents MAY:

- use source metadata to identify source, scope, freshness, limitations, and provenance;
- flag missing, stale, inconsistent, or ambiguous source metadata;
- draft questions, review packets, and approval packages that cite source references;
- summarize records with source references and limitations;
- compare source scope against workflow, tenant, customer, case, evidence, retention, and allowed-use requirements;
- recommend quarantine, retry, parser review, enrichment review, or escalation when metadata is insufficient.

Agents MUST NOT:

- fabricate source-system metadata, timestamps, owners, tenants, customers, cases, evidence references, or approvals;
- treat metadata presence as authorization to execute tools or actions;
- treat connector success as proof of completeness, correctness, or approval;
- broaden collection scope, destination scope, retention scope, or allowed use;
- modify source records, evidence objects, collection rules, parser logic, or source registration outside governed change paths;
- route records to customer-facing, external, report, approval, evidence, knowledge, memory, or shared intelligence destinations without required controls;
- treat source metadata as original evidence, forensic proof, policy decision, human review, or formal approval.

## Review and Approval Requirements

Human review or formal approval MUST be triggered when source metadata affects sensitive downstream use.

| Condition | Required Handling |
|---|---|
| New governed source activation | Review source owner, scope, classification, retention, collection method, and destinations. |
| Sensitive source onboarding | Require approval where policy requires approval for evidence, privileged, legal, regulated, customer, or cross-boundary sources. |
| Collection scope expansion | Review and approve added tenants, customers, cases, workspaces, accounts, fields, event types, or destinations where required. |
| Historical backfill | Require scoped authorization when backfill can change investigation, reporting, retention, or evidence interpretation. |
| Evidence-derived ingestion | Require evidence-aware handling and review where evidence interpretation or customer-facing output may be affected. |
| Shared intelligence candidate use | Require sanitization, review, release control, and approval where applicable. |
| Metadata ambiguity | Route to controlled review before governed decisions depend on the data. |
| Source suspension or retirement | Preserve replayability and downstream impact context. |

Human review may validate source quality and scope. Formal approval may authorize source activation, collection expansion, sensitive routing, or release where policy requires it. Neither review nor approval authorizes unrelated tool execution, response action, case closure, evidence release, or customer communication.

## Fail-Closed Conditions

The ingestion workflow MUST fail closed, quarantine, restrict downstream use, or route to controlled review when:

- source-system registration is missing, expired, revoked, blocked, or inconsistent with the requested use;
- source owner, technical owner, data owner, or approval context is missing where required;
- source lifecycle state is candidate, review-required, suspended, deprecated, retired, or blocked and the requested use requires active status;
- required tenant, customer, workspace, subscription/account, region, case, evidence, destination, retention, or allowed-use metadata is missing, ambiguous, unauthorized, stale, inconsistent, or out of scope;
- source-native identifiers cannot be mapped to governed tenant, customer, workspace, subscription/account, case, or evidence scope where mapping is required;
- source timestamp, collection timestamp, ingestion timestamp, collector identity, connector identity, or collection rule identity is missing where replay depends on it;
- connector version, collection rule version, source schema version, parser dependency, or normalization target cannot be determined where field meaning or replay depends on it;
- data classification, sensitivity label, allowed use, retention, legal hold, or destination constraint conflicts with requested downstream use;
- source record integrity checks fail or source sequence gaps materially affect downstream use;
- collection scope is broader than approved scope;
- destination system or output destination is unauthorized, ambiguous, or inconsistent with allowed use;
- evidence attribution is missing where evidence or evidence-derived records are consumed;
- knowledge-store, vector-index, shared-memory, customer-context, case-memory, evidence-retrieval, or retrieved-context routing lacks approved retrieval and reuse scope;
- audit logging fails where audit is required;
- an agent, workflow, connector, parser, or enrichment step attempts to infer, overwrite, suppress, or repair required source metadata without governed review.

Fail-closed handling MUST preserve the source reference, request context, failure reason, affected records, scope metadata, policy context where available, quarantine or retry status, reviewer or owner routing, and audit references.

## Audit and Replay Requirements

Audit replay MUST be able to reconstruct:

- which source system produced or supplied a record;
- which owner, lifecycle state, classification, allowed use, and retention policy applied at the time of ingestion;
- which tenant, customer, workspace, subscription/account, case, evidence, region, and native source scope applied;
- which connector, collector identity, collection rule, and collection method were used;
- which source identifiers, timestamps, sequence numbers, raw-record references, integrity indicators, and limitations were preserved;
- which parser, schema, normalization target, enrichment source, destination, and downstream workflow consumed the record;
- which source metadata was missing, stale, ambiguous, inconsistent, quarantined, reviewed, corrected, or blocked;
- which policy context, approval record, review record, audit record, and correlation identifiers governed collection or routing;
- whether a record was used by an agent, Agent Judge, analyst, approval package, report workflow, policy workflow, evidence-aware workflow, knowledge store, vector index, shared memory, shared intelligence package, or audit replay process.

Audit records SHOULD reference source records and evidence objects rather than copying raw sensitive source material into audit logs unless the evidence-handling and retention model explicitly permits it.

## Relationship to Other Data-Ingestion Files

- [`data-ingestion-model.md`](data-ingestion-model.md) defines the full governed ingestion lifecycle and control boundaries.
- [`normalization-and-enrichment.md`](normalization-and-enrichment.md) defines parser, schema, mapping, enrichment, conflict, freshness, and downstream interpretation requirements.
- [`ingestion-failure-handling.md`](ingestion-failure-handling.md) defines quarantine, retry, degraded-mode, and fail-closed handling.
- [`ingestion-audit-replay.md`](ingestion-audit-replay.md) defines replay requirements for ingestion events, transformations, enrichment, routing, and downstream consumption.
- [`shared-intelligence-sanitization-and-release-controls.md`](shared-intelligence-sanitization-and-release-controls.md) defines sanitization, approval, release, rollback, and recall controls for reusable security knowledge derived from ingestion.

## Operational Anti-Patterns

Avoid the following:

- collecting from unregistered or ownerless sources;
- treating source-system availability as authorization to collect or route data;
- treating connector success as evidence completeness or source correctness;
- storing tenant and customer identity as a single ambiguous field;
- dropping source-native identifiers during parsing or normalization;
- overwriting source timestamps with collection or ingestion timestamps;
- routing records with unknown classification, retention, allowed use, or destination constraints;
- indexing raw customer, tenant, case, or evidence content into shared memory or knowledge stores without sanitization and approval;
- silently broadening collection rules during parser or connector changes;
- using stale or partial sources for severity, routing, approval packages, reports, evidence interpretation, or policy decisions without limitations and review;
- relying on model-generated summaries as source metadata;
- allowing agents to invent, repair, or approve missing source metadata;
- using unauditable source records for governed decisions;
- deleting source metadata corrections instead of appending correction or reversal records.

## Acceptance Criteria

This file is acceptable when:

- source systems have accountable ownership, lifecycle state, approved scope, classification, retention, allowed use, and approved destinations;
- connector and collection-rule metadata are preserved separately from source-system metadata;
- source records preserve source-native identifiers, timestamps, collector identity, raw-record references, scope, quality state, and limitations where applicable;
- tenant identity and customer identity remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- workspace, subscription/account, project, region, case, evidence, destination, retention, and allowed-use boundaries are preserved where applicable;
- source timestamps, collection timestamps, ingestion timestamps, and transformation timestamps remain distinguishable;
- source metadata preserves data classification, sensitivity label, retention policy, legal hold, allowed use, and disallowed use where applicable;
- evidence-derived records preserve evidence references and do not replace original evidence;
- source metadata for knowledge stores, vector indexes, shared memory, customer context, case memory, and evidence retrieval preserves approved retrieval and reuse scope;
- missing, ambiguous, stale, unauthorized, inconsistent, out-of-scope, or unauditable source metadata triggers quarantine, review, degraded handling, or fail-closed behavior;
- audit replay can reconstruct source registration, connector, collection rule, source record, provenance, validation, routing, and downstream use;
- source metadata does not authorize tool execution, customer release, evidence release, response action, case closure, or formal approval.
