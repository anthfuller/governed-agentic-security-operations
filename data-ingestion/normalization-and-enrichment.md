# Normalization and Enrichment

## Purpose

This file defines governance expectations for parsing, normalization, enrichment, entity resolution, schema versioning, mapping traceability, freshness handling, and downstream interpretation of ingested security data.

Normalization and enrichment allow data from different telemetry, cloud, SaaS, identity, endpoint, network, ticketing, case, evidence, and DFIR sources to be used consistently by governed workflows. They must preserve source meaning, tenant and customer boundaries, evidence references, and audit replay context.

This file defines architecture and control expectations. It does not define production parsers, vendor-specific schemas, detection content, enrichment provider configuration, SIEM deployment, data warehouse design, or customer-specific operating procedures.

## Scope

This file applies to normalization and enrichment for:

- source records collected through connectors, APIs, agents, exports, streams, event hubs, or files;
- parsed records produced from raw telemetry or evidence-derived data;
- normalized records used by detection, triage, investigation, reporting, policy, approval, and audit workflows;
- enrichment from threat intelligence, identity, asset inventory, cloud context, vulnerability context, geolocation, reputation, case context, evidence context, or knowledge stores;
- entity resolution for users, devices, workloads, IP addresses, cloud resources, SaaS objects, identities, mailboxes, cases, evidence objects, and customer assets;
- private/local LLM-assisted DFIR workflows that extract, summarize, classify, or structure evidence-derived data;
- downstream use by agents, Agent Judges, analysts, policy decision logic, ticketing systems, case systems, reports, and shared intelligence pipelines.

This file does not replace source-system metadata, ingestion failure handling, evidence traceability, tenant isolation, tool access, policy enforcement, human approval, or audit replay controls.

## Core Principles

- Normalized data is derived data. It must not replace the original source record or evidence object.
- Enrichment adds context. It must not be treated as incident truth, evidence completeness, customer approval, or authorization for action.
- Source values, mapped values, derived values, and enriched values must remain distinguishable.
- Parser, schema, mapping, transformation, enrichment source, and enrichment version must be traceable where they affect downstream interpretation.
- Field-level uncertainty, lossy transformation, unmapped fields, conflicting values, stale context, and partial enrichment must be preserved where material.
- Tenant identity and customer identity must remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows.
- Case, evidence, workspace, subscription, account, project, retention, and allowed-use boundaries must be preserved where applicable.
- Normalization and enrichment must not silently widen data access, reuse, routing, or release scope.
- Agent-generated summaries must not be stored or treated as normalized source records unless they are explicitly labeled as derived outputs with source references and review status.
- Missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, or unauditable normalization or enrichment context must fail closed where governed workflow behavior depends on it.

## Normalization Lifecycle

| Stage | Requirement | Output |
|---|---|---|
| Source reference | Preserve source system, source record reference, source timestamp, collection timestamp, and collector identity. | Source-linked parsed record. |
| Parsing | Apply an identified parser with parser version and parsing status. | Parsed fields with extraction status. |
| Schema validation | Validate required fields, data types, enumerations, timestamp formats, and schema version. | Validated or rejected structured record. |
| Field mapping | Map source fields to normalized fields using a versioned mapping. | Normalized fields with source references. |
| Type conversion | Convert timestamps, numeric fields, identifiers, severities, and enumerations without hiding conversion limitations. | Typed normalized fields. |
| Entity resolution | Resolve identities, assets, cloud resources, mailboxes, applications, network entities, and evidence objects using approved sources. | Resolved entities with match confidence and authority source. |
| Derived field creation | Create derived fields only when source inputs, derivation logic, and limitations are recorded. | Derived fields with transformation references. |
| Scope validation | Validate tenant, customer, case, workspace, account, evidence, and destination scope before downstream use. | Scope validation result. |
| Downstream routing | Route normalized records only to approved destinations and workflows. | Routed record with destination context. |
| Audit linkage | Record parser, schema, mapping, transformation, scope, routing, and correlation context. | Replayable normalization event. |

## Required Normalization Record

Governed normalization should produce a structured record with the following fields where applicable.

| Field | Requirement | Purpose |
|---|---|---|
| `normalization_event_id` | MUST | Unique identifier for the normalization event. |
| `source_system_id` | MUST | Identifies the originating system or platform. |
| `source_record_id` | MUST when available | Preserves source-level traceability. |
| `source_record_reference` | MUST | References the raw or collected source record. |
| `parsed_record_id` | MUST when parsing is applied | Links normalization to the parsed record. |
| `normalized_record_id` | MUST | Identifies the normalized output record. |
| `source_record_type` | MUST when known | Identifies log, event, alert, artifact, ticket, case, finding, or evidence-derived record type. |
| `source_timestamp` | MUST when available | Preserves when the source event occurred. |
| `collection_timestamp` | MUST | Preserves when the source record was collected or received. |
| `normalization_timestamp` | MUST | Records when normalization occurred. |
| `collector_identity` | MUST | Identifies connector, agent, service identity, or collection mechanism. |
| `connector_id` | MUST when connector-based ingestion is used | Identifies the connector or integration. |
| `connector_version` | MUST when version affects parsing, mapping, or replay | Supports troubleshooting and regression review. |
| `collection_rule_id` | MUST when collection rules select records, fields, sources, or events | Identifies collection scope. |
| `parser_id` | MUST when parsing is applied | Identifies parser logic. |
| `parser_version` | MUST when parsing affects field meaning or replay | Supports parser accountability and dispute review. |
| `schema_version` | MUST | Identifies the normalized output schema. |
| `normalization_mapping_id` | MUST | Identifies field mapping logic. |
| `normalization_mapping_version` | MUST | Supports replay and mapping regression review. |
| `parser_or_transformation_version` | MUST when transformation changes field meaning or downstream interpretation | Supports transformation traceability and audit replay. |
| `field_mapping_status` | MUST | Records complete, partial, failed, lossy, conflicting, or review-required mapping status. |
| `unmapped_fields_reference` | SHOULD when unmapped fields exist | Preserves fields that were not mapped. |
| `lossy_transformation_indicator` | MUST when transformation loses precision or source meaning | Prevents silent loss of context. |
| `derived_field_references` | MUST when derived fields are created | Links derived values to source fields and transformation logic. |
| `entity_resolution_result` | MUST when entity resolution is applied | Records match source, confidence, and limitations. |
| `data_classification` | MUST when sensitivity affects access, routing, retention, release, or downstream use | Preserves data-handling context. |
| `sensitivity_label` | MUST when applicable | Preserves handling label context. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use of normalized data. |
| `retention_policy_id` | MUST when retention affects source data, transformed data, indexed data, or retrieved context | Preserves retention and disposal boundary. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `workspace_id` | MUST when workspace scope affects telemetry, access, routing, or downstream use | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects the record | Preserves cloud boundary context. |
| `case_id` | MUST when normalization output is tied to an investigation, incident, ticket, report, or DFIR workflow | Links normalized data to the governed case. |
| `workflow_id` | MUST for governed workflows | Links normalization to workflow state. |
| `evidence_object_ids` | MUST when evidence or forensic artifacts are parsed, normalized, summarized, indexed, or referenced | Supports evidence traceability. |
| `destination_system_id` | MUST when normalized records are routed, written, indexed, published, or consumed by another system | Identifies downstream destination. |
| `output_destination` | MUST when output is displayed, routed, exported, released, indexed, or consumed downstream | Preserves release and routing context. |
| `scope_validation_result` | MUST when scope is evaluated | Records tenant, customer, case, workspace, account, evidence, retention, and destination validation result. |
| `policy_context_id` | MUST when policy affects normalization, routing, release readiness, retention, evidence handling, or fail-closed behavior | Links normalization to applicable policy context. |
| `audit_reference_id` | MUST for governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related source, ingestion, case, evidence, policy, approval, tool, and audit records. |

## Field Mapping Requirements

| Field Type | Requirement |
|---|---|
| Direct mappings | Preserve source field name, source value reference, normalized field name, mapping rule, and mapping version. |
| Derived fields | Preserve derivation rule, source field references, transformation version, and limitations. |
| Timestamps | Preserve source timestamp, collection timestamp, normalization timestamp, timezone handling, precision, and clock-skew indicators where applicable. |
| Severity and priority | Preserve source severity, source scale, normalized severity, mapping rule, and any loss of granularity. |
| Identity fields | Preserve source identity, normalized principal, tenant or directory scope, authority source, and match confidence. |
| Asset fields | Preserve source asset identifier, hostname, IP address, cloud resource identifier, observed interval, authority source, and match confidence. |
| Network fields | Preserve source and destination addresses, ports, protocol, direction, NAT, proxy, VPN, and sensor context where available. |
| Cloud fields | Preserve subscription, account, project, tenant, resource identifier, region, service, workload, and control-plane context. |
| SaaS and email fields | Preserve application, workspace, mailbox, message, user, object, and tenant-specific identifiers where available. |
| Evidence fields | Preserve evidence object identifiers and attribution metadata. Normalization must not overwrite original evidence. |
| Customer and tenant fields | Preserve tenant identity and customer identity separately. Derived customer scope must not overwrite tenant identifiers. |
| Case fields | Preserve case, incident, ticket, workflow, and routing context without joining unrelated matters. |
| Classification fields | Preserve data classification, sensitivity label, allowed use, retention policy, and release constraints. |

## Enrichment Lifecycle

| Stage | Requirement | Output |
|---|---|---|
| Enrichment request | Define lookup key, source record, normalized record, workflow, tenant, customer, and allowed-use scope. | Scoped enrichment request. |
| Source authorization | Use only approved enrichment sources for the requested tenant, customer, case, evidence, or workflow scope. | Authorized or denied enrichment path. |
| Lookup and retrieval | Preserve enrichment source, source version, lookup timestamp, query reference, and returned result reference. | Traceable enrichment result. |
| Freshness evaluation | Evaluate timestamp, time-to-live, source update time, and staleness risk. | Freshness status. |
| Confidence and limitations | Preserve provider confidence, match confidence, uncertainty, partial results, and conflicts. | Interpretable enrichment context. |
| Scope validation | Validate that enrichment does not cross tenant, customer, case, evidence, retention, or reuse boundaries. | Scope validation result. |
| Record attachment | Attach enrichment as derived context without overwriting source or normalized truth. | Enriched record. |
| Downstream gating | Apply review, approval, policy, or fail-closed handling when enrichment affects sensitive action, release, escalation, or closure. | Governed downstream use. |
| Audit linkage | Record request, result, scope, freshness, confidence, routing, and downstream consumption. | Replayable enrichment event. |

## Required Enrichment Record

Governed enrichment should produce a structured record with the following fields where applicable.

| Field | Requirement | Purpose |
|---|---|---|
| `enrichment_event_id` | MUST | Unique identifier for the enrichment event. |
| `normalized_record_id` | MUST when enrichment attaches to a normalized record | Links enrichment to normalized data. |
| `source_record_reference` | MUST when enrichment traces back to source data | Preserves source linkage. |
| `enrichment_type` | MUST | Identifies threat intelligence, identity, asset, cloud, vulnerability, geolocation, reputation, case, evidence, or knowledge enrichment. |
| `enrichment_source_id` | MUST | Identifies the enrichment source. |
| `enrichment_source_version` | MUST when source version affects interpretation or replay | Supports regression and dispute review. |
| `enrichment_provider_owner` | SHOULD for governed sources | Identifies accountable owner. |
| `lookup_key_reference` | MUST | References the indicator, identity, asset, resource, case, or evidence key used for lookup. |
| `lookup_timestamp` | MUST | Records when lookup occurred. |
| `enrichment_timestamp` | MUST | Records when the enrichment result was produced or attached. |
| `source_update_timestamp` | SHOULD when available | Records when the enrichment source was last updated. |
| `freshness_status` | MUST | Records fresh, stale, unknown, expired, partial, or review-required status. |
| `ttl_or_expiration` | SHOULD when enrichment has time-limited validity | Supports stale-result handling. |
| `confidence_score` | SHOULD when provided | Captures confidence without treating it as approval. |
| `match_confidence` | MUST when entity resolution or fuzzy matching is used | Indicates match quality. |
| `limitations` | MUST where material | Records uncertainty, partial result, stale data, conflict, or scope limitation. |
| `conflict_indicator` | MUST when enrichment conflicts with source or other enrichment | Prevents silent conflict resolution. |
| `data_classification` | MUST when sensitivity affects access, routing, retention, release, or downstream use | Preserves handling context. |
| `sensitivity_label` | MUST when applicable | Preserves handling label context. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use of enriched data. |
| `retention_policy_id` | MUST when retention affects enrichment or retrieved context | Preserves retention and disposal boundary. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when enrichment is case-bound | Links enrichment to investigation, incident, ticket, or DFIR matter. |
| `workflow_id` | MUST for governed workflows | Links enrichment to workflow state. |
| `workspace_id` | MUST when workspace scope affects enrichment or downstream use | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects enrichment | Preserves cloud boundary context. |
| `evidence_object_ids` | MUST when evidence or forensic artifacts are enriched, summarized, indexed, or referenced | Supports evidence traceability. |
| `knowledge_store_or_memory_scope` | MUST when retrieval, vector search, shared memory, customer context, case memory, or evidence retrieval is used | Defines approved retrieval and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval remained within approved boundaries. |
| `destination_system_id` | MUST when enriched records are routed, written, indexed, published, or consumed by another system | Identifies downstream destination. |
| `output_destination` | MUST when output is displayed, routed, exported, released, indexed, or consumed downstream | Preserves release and routing context. |
| `scope_validation_result` | MUST when scope is evaluated | Records tenant, customer, case, workspace, account, evidence, retention, retrieval, and destination validation result. |
| `policy_context_id` | MUST when policy affects enrichment, routing, release readiness, retention, evidence handling, or fail-closed behavior | Links enrichment to applicable policy context. |
| `audit_reference_id` | MUST for governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related source, ingestion, case, evidence, policy, approval, tool, and audit records. |

## Enrichment Source Requirements

| Enrichment Type | Requirement |
|---|---|
| Threat intelligence | Preserve source, indicator type, confidence, first seen, last seen, expiration or TTL, collection restrictions, and allowed use. |
| Identity context | Preserve directory, tenant, user, group, role, service principal, workload identity, and authority source. |
| Asset context | Preserve inventory source, asset identifier, owner, exposure state, observed interval, and match confidence. |
| Cloud context | Preserve provider, tenant, subscription, account, project, resource identifier, region, service, and control-plane scope. |
| Vulnerability context | Preserve scanner or exposure source, scan timestamp, asset match confidence, vulnerability identifier, and remediation-state timestamp. |
| Geolocation and reputation | Preserve provider, lookup time, confidence, uncertainty, and warning that results may be approximate or stale. |
| Detection and ATT&CK context | Preserve rule, analytic, technique mapping, mapping version, and whether mapping is direct, inferred, or analyst-reviewed. |
| Case context | Preserve case identifier, workflow stage, allowed-use scope, and review status before reuse. |
| Evidence context | Preserve evidence object identifiers, evidence attribution, source references, and chain-of-custody references where applicable. |
| Knowledge or memory context | Preserve store identifier, retrieval scope, retrieval timestamp, source references, retention, freshness, and reuse constraints. |

## Freshness and Expiration

Normalization and enrichment workflows must preserve freshness context when downstream interpretation depends on it.

| Condition | Required Handling |
|---|---|
| Fresh context | Record source update time, lookup time, and applicable TTL. |
| Stale context | Mark stale status, preserve original result, restrict downstream use, and route to refresh or review where required. |
| Unknown freshness | Treat as higher risk and restrict use where freshness affects severity, containment, release, closure, or customer communication. |
| Expired enrichment | Prevent sensitive downstream use unless policy permits exception handling with review or approval. |
| Conflicting freshness | Preserve both results, identify sources, and avoid silent preference without recorded rationale. |
| Refreshed enrichment | Preserve link to prior enrichment result and record whether downstream outputs were affected. |

## Conflict and Uncertainty Handling

Normalization and enrichment must preserve uncertainty rather than hide it.

Conflicts must be recorded when:

- two sources produce different values for the same entity, asset, identity, indicator, severity, owner, or status;
- normalized values conflict with source fields;
- enrichment contradicts source telemetry or evidence-derived data;
- identity, asset, or cloud-resource matching is ambiguous;
- confidence is low, unknown, stale, or source-dependent;
- field mapping loses source precision or changes meaning;
- downstream use could materially affect severity, containment guidance, customer communication, shared intelligence, or DFIR conclusions.

Conflicting or uncertain values must not be silently overwritten. High-impact conflicts must route to review, fail closed, or remain excluded from sensitive downstream use until resolved.

## Tenant, Customer, Case, and Evidence Boundaries

Normalization and enrichment must preserve boundary context before records are routed, indexed, retrieved, summarized, or used downstream.

| Boundary | Requirement |
|---|---|
| Tenant boundary | Records must remain linked to the correct tenant, workspace, directory, subscription, account, project, or environment. |
| Customer boundary | Customer identity must remain separate from tenant identity and must control customer-scoped handling. |
| Case boundary | Case-bound data must not be joined with unrelated matters unless policy authorizes correlation. |
| Evidence boundary | Evidence-derived data must preserve evidence object references and must not replace original evidence. |
| Retention boundary | Normalized and enriched outputs must preserve retention policy and legal-hold context where applicable. |
| Output boundary | Records must only be routed, released, indexed, or consumed by approved destinations and workflows. |
| Retrieval boundary | RAG, vector search, shared memory, customer context, case memory, and evidence retrieval must remain within approved scope. |

## Private/Local LLM-Assisted DFIR Requirements

Private/local LLM-assisted DFIR workflows may parse, extract, classify, summarize, or structure evidence-derived data, but those outputs remain derived records.

For DFIR workflows:

- original evidence must remain immutable and separately referenced;
- extracted artifacts must preserve evidence object identifiers and source offsets, paths, hashes, timestamps, or artifact references where available;
- summaries must preserve source evidence references and limitation notes;
- normalization must identify parser, extraction, model, prompt package, and transformation version where they affect interpretation;
- enrichment must remain within approved local evidence stores, case scope, customer scope, and examiner workflow;
- examiner review is required before evidence-derived conclusions are used in customer-facing reports or final DFIR findings;
- local execution must not be treated as proof of correctness, forensic validity, or evidence completeness.

## Agent Use of Normalized and Enriched Data

Agents may use normalized and enriched data to:

- retrieve scoped context;
- correlate related events;
- summarize relevant facts;
- identify missing data or uncertainty;
- draft investigation notes;
- prepare review or approval packages;
- suggest follow-up questions or evidence collection;
- support Agent Judge checks for evidence support, boundary handling, unsupported claims, and output quality.

Agents must not:

- treat normalized or enriched data as original evidence;
- treat enrichment as proof of incident truth, legal conclusion, or forensic certification;
- suppress source references, uncertainty, stale status, conflicts, or limitations;
- widen tenant, customer, case, evidence, retention, or retrieval scope;
- route records to unapproved destinations;
- approve customer-facing release, containment, remediation, closure, or evidence release;
- change source records, evidence records, policy decisions, approval records, or audit records outside governed workflow controls.

## Downstream Use Requirements

| Downstream Use | Requirement |
|---|---|
| Detection and triage | Preserve source references, schema version, field mappings, enrichment freshness, and uncertainty. |
| Investigation and case work | Preserve tenant, customer, case, evidence, workflow, and analyst-review context. |
| Policy decision context | Provide structured scope, classification, allowed use, evidence references, and limitations. |
| Agent Judge checks | Provide source references, evidence support, retrieved context boundaries, and unsupported-claim indicators. |
| Customer-facing reports | Require evidence support, review status, approval path where required, and clear separation of source, derived, and enriched values. |
| Shared intelligence | Use only sanitized, approved, versioned security knowledge and preserve release, rollback, and recall context. |
| Audit replay | Preserve enough metadata to reconstruct source, parser, schema, mapping, enrichment, routing, and downstream consumption. |

## Fail-Closed Conditions

The ingestion workflow must fail closed, quarantine affected records, or route to controlled review when:

- parser, schema, normalization mapping, transformation version, or enrichment source is missing, ambiguous, stale, unauthorized, inconsistent, or unauditable;
- required source, tenant, customer, case, workspace, account, evidence, destination, classification, allowed-use, or retention context is missing or mismatched;
- source values, normalized values, derived values, or enriched values cannot be distinguished;
- field mapping loses material source meaning without recording lossy transformation context;
- enrichment is stale, expired, conflicting, unsupported, or outside approved scope;
- identity, asset, cloud-resource, indicator, or evidence matching is ambiguous and affects downstream action, release, escalation, or closure;
- RAG, vector search, shared memory, customer context, case memory, or evidence retrieval occurs without approved retrieval scope and scope result;
- normalized or enriched output would cross tenant, customer, case, evidence, retention, output-destination, or reuse boundaries;
- normalized or enriched output affects customer-facing reports, approval packages, containment recommendations, shared intelligence, or DFIR conclusions without required review or approval path;
- audit logging, correlation, or replay linkage fails where governed workflow behavior depends on it;
- an agent, tool, parser, enrichment source, or downstream workflow attempts to overwrite source truth, suppress limitations, bypass failure handling, or relabel derived data as original evidence.

## Audit and Replay Requirements

Normalization and enrichment events must support reconstruction of:

- source system, source record, source timestamp, collection timestamp, and collector identity;
- connector, collection rule, parser, parser version, schema version, normalization mapping, and transformation version;
- source fields, normalized fields, derived fields, unmapped fields, lossy transformations, and limitations;
- enrichment source, enrichment type, lookup key, lookup time, freshness status, confidence, conflicts, and expiration;
- tenant, customer, case, workspace, subscription, account, project, evidence, classification, allowed-use, retention, and destination scope;
- scope validation result and fail-closed or review routing outcome;
- downstream systems, workflows, cases, reports, policy decisions, approvals, Agent Judge checks, or shared intelligence packages that consumed the output;
- correction, refresh, quarantine, retry, replay, rollback, recall, or closure events related to normalization or enrichment.

Audit records should reference source records and evidence objects rather than copying raw evidence or unnecessary sensitive content into audit logs.

## Operational Anti-Patterns

Avoid the following:

- overwriting source fields with normalized or enriched values;
- storing normalized data without source record references;
- storing enrichment without source, lookup time, freshness, confidence, limitations, or allowed-use context;
- using a generic schema or mapping version that cannot support replay;
- suppressing unmapped fields, lossy transformations, stale enrichment, or conflicting values;
- resolving identities, assets, cloud resources, or evidence objects across tenants, customers, or cases without explicit policy authority;
- treating threat intelligence, reputation, geolocation, or vulnerability enrichment as proof of compromise without supporting evidence;
- allowing agent-generated summaries to become normalized source records without derived-output labeling, source references, and review status;
- using private/local DFIR extraction output as final evidence or examiner-approved findings without review;
- routing normalized or enriched records to customer-facing reports, shared intelligence, or approval packages without required evidence support and review path;
- failing open when parser, schema, mapping, enrichment, scope, retention, or audit context is missing.

## Relationship to Other Data-Ingestion Files

- [`data-ingestion-model.md`](data-ingestion-model.md) defines the broader governed ingestion lifecycle and source-to-destination flow.
- [`source-system-metadata.md`](source-system-metadata.md) defines source, connector, collection rule, and source-record metadata expectations.
- [`ingestion-failure-handling.md`](ingestion-failure-handling.md) defines quarantine, retry, degraded-mode, and fail-closed behavior.
- [`ingestion-audit-replay.md`](ingestion-audit-replay.md) defines replay requirements for ingestion, normalization, enrichment, routing, and downstream consumption.
- [`shared-intelligence-sanitization-and-release-controls.md`](shared-intelligence-sanitization-and-release-controls.md) defines controls for sanitized, approved, versioned security knowledge derived from ingestion.

## Acceptance Criteria

This file is acceptable when:

- source records, parsed records, normalized records, derived fields, and enriched records remain distinguishable;
- normalization preserves source references, parser version, schema version, mapping version, transformation version, and field-level limitations where applicable;
- enrichment preserves source, lookup key, lookup time, freshness, confidence, limitations, conflicts, and allowed-use context;
- tenant identity and customer identity remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- case, workspace, subscription, account, project, evidence, retention, retrieval, and output-destination boundaries are preserved where applicable;
- evidence-derived normalized and enriched outputs reference original evidence without replacing it;
- agents can consume normalized and enriched data only within governed workflow, policy, approval, evidence, and audit boundaries;
- stale, conflicting, missing, ambiguous, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, or unauditable context fails closed or routes to controlled review where downstream behavior depends on it;
- customer-facing reports, approval packages, shared intelligence, and DFIR conclusions are supported by source references, evidence references, review status, and approval path where required;
- audit replay can reconstruct source, parser, schema, mapping, enrichment, freshness, scope validation, routing, downstream consumption, corrections, and final disposition.
