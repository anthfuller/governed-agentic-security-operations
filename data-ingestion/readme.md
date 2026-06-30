# Data Ingestion

## Purpose

This directory defines the governed data-ingestion model for agentic security operations across Managed SOC / MSSP, MDR, cloud incident response, and private/local LLM-assisted DFIR workflows.

Data ingestion includes source-system metadata, collection context, parsing, normalization, enrichment, routing, failure handling, audit replay, and shared intelligence release controls.

This directory defines architecture and governance expectations. It does not define production pipelines, vendor connector configuration, executable workflows, data warehouse design, SIEM deployment, evidence repository implementation, or customer-specific operating procedures.

## Scope

This directory applies to ingestion and integration of security-relevant data from:

- SIEM, XDR, EDR, NDR, cloud, SaaS, identity, email, firewall, ticketing, and business-application sources;
- connectors, agents, APIs, event hubs, message pipelines, files, exports, and streaming sources;
- source records, parsed records, normalized records, enriched records, derived context, and routed outputs;
- case stores, evidence stores, knowledge stores, vector indexes, report stores, ticketing systems, and workflow systems where ingestion output is consumed;
- private/local LLM-assisted DFIR workflows that parse, extract, summarize, or route evidence-derived data;
- shared security intelligence pipelines that sanitize, approve, version, and release reusable security knowledge.

This directory does not replace `tool-access/`, `policy-enforcement/`, `tenant-isolation/`, `evidence-traceability/`, `local-llm-dfir/`, or `audit-replay/`. Data ingestion supplies governed source and transformation context that those control areas consume.

## Core Principles

- Ingestion is a governance boundary, not only a data movement function.
- Source identity, tenant scope, customer scope, case scope, data classification, retention, and allowed use must be preserved where applicable.
- Raw source records and evidence objects must remain distinguishable from parsed, normalized, enriched, summarized, or routed outputs.
- Normalization and enrichment must not overwrite source truth or hide uncertainty.
- Agent-generated summaries are not source records, evidence records, policy decisions, or approvals.
- Successful ingestion does not authorize downstream tool execution, customer release, containment, remediation, closure, or evidence handling.
- Missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, or unauditable ingestion context must fail closed where governed workflow behavior depends on it.
- Shared intelligence distribution must use sanitized, approved, versioned security knowledge. Raw tenant data and raw customer data must not be redistributed across boundaries.
- Audit replay must be able to reconstruct which source, connector, rule, parser, schema, transformation, enrichment, identity, tenant, customer, case, destination, and downstream workflow participated in an ingestion path.

## Directory Contents

| File | Purpose |
|---|---|
| [`data-ingestion-model.md`](data-ingestion-model.md) | Defines the governed ingestion model, ingestion lifecycle, source-to-destination flow, and control boundaries. |
| [`source-system-metadata.md`](source-system-metadata.md) | Defines required metadata for source systems, connectors, collection rules, source records, and provenance. |
| [`normalization-and-enrichment.md`](normalization-and-enrichment.md) | Defines expectations for parsing, normalization, enrichment, schema versions, mapping versions, freshness, and downstream interpretation. |
| [`ingestion-failure-handling.md`](ingestion-failure-handling.md) | Defines failure, quarantine, retry, degraded-mode, and fail-closed handling for ingestion workflows. |
| [`ingestion-audit-replay.md`](ingestion-audit-replay.md) | Defines audit and replay requirements for ingestion events, transformations, enrichment, routing, and downstream consumption. |
| [`shared-intelligence-sanitization-and-release-controls.md`](shared-intelligence-sanitization-and-release-controls.md) | Defines sanitization, approval, versioning, release, rollback, and recall controls for reusable security knowledge derived from ingestion. |

## Governed Ingestion Workflow

| Stage | Requirement |
|---|---|
| Source registration | The source system, owner, data classification, tenant/customer scope, retention, allowed use, and collection method must be defined before governed ingestion. |
| Collection authorization | Collection must occur through approved connectors, agents, APIs, exports, or pipelines with scoped identity and permitted operation context. |
| Source capture | Source identifiers, source timestamps, collection timestamps, collector identity, and source record references must be preserved. |
| Parsing | Parsers must be identified, versioned, and tied to source type, connector version, schema version, and failure behavior. |
| Schema validation | Records must be validated before downstream use where schema quality affects routing, detection, investigation, evidence interpretation, reporting, or policy context. |
| Normalization | Normalized fields must preserve source references, mapping versions, and any field-level limitations or lossy transformations. |
| Enrichment | Enrichment must identify enrichment source, version, timestamp, confidence, freshness, and scope. Enrichment must not silently replace original source values. |
| Scope validation | Tenant, customer, workspace, subscription/account, case, evidence, and destination scope must be validated before routing or downstream consumption. |
| Routing | Outputs must be routed only to approved destinations, case records, evidence stores, knowledge stores, queues, reports, or workflows. |
| Audit and replay | Each governed ingestion path must produce enough structured context to reconstruct source, transformation, enrichment, routing, failure, and downstream use. |

## Required Ingestion Context

Governed ingestion records should preserve the following fields where applicable.

| Field | Requirement | Purpose |
|---|---|---|
| `ingestion_event_id` | MUST | Unique ingestion event identifier. |
| `source_system_id` | MUST | Identifies the originating system or platform. |
| `source_record_id` | MUST when available | Preserves source-level traceability. |
| `source_timestamp` | MUST when available | Records when the source event occurred. |
| `collection_timestamp` | MUST | Records when the event was collected or received. |
| `collector_identity` | MUST | Identifies the connector, agent, service identity, or collection mechanism. |
| `connector_id` | MUST when connector-based ingestion is used | Identifies the connector or integration. |
| `connector_version` | MUST when version affects parsing, field mapping, or replay | Supports troubleshooting and regression review. |
| `collection_rule_id` | MUST when collection rules select records, fields, sources, or events | Identifies the collection rule used. |
| `parser_id` | MUST when parsing is applied | Identifies the parser used. |
| `parser_version` | MUST when parsing affects field meaning or replay | Supports parser accountability and dispute review. |
| `schema_version` | MUST when normalized or structured records are produced | Identifies the output schema version. |
| `normalization_mapping_id` | SHOULD when normalization is applied | Identifies field mapping logic. |
| `parser_or_transformation_version` | MUST when transformation changes field meaning or downstream interpretation | Supports replay, review, and dispute analysis. |
| `enrichment_source_id` | MUST when enrichment is applied | Identifies enrichment source. |
| `enrichment_timestamp` | MUST when enrichment is applied | Records enrichment freshness. |
| `data_classification` | MUST when sensitivity affects access, routing, retention, release, or downstream use | Preserves handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity or handling label context. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use of ingested or derived data. |
| `retention_policy_id` | MUST when retention affects source data, transformed data, indexed data, or retrieved context | Preserves retention and disposal boundary. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `workspace_id` | MUST when workspace scope affects telemetry, access, routing, or downstream use | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud scope affects ingestion or downstream use | Preserves cloud boundary context. |
| `case_id` | MUST when ingestion output is tied to an investigation, incident, escalation, report, or DFIR workflow | Links ingested data to the governed case. |
| `workflow_id` | MUST for governed workflows | Links ingestion to workflow state. |
| `evidence_object_ids` | MUST when evidence or forensic artifacts are collected, parsed, transformed, summarized, indexed, or referenced | Supports evidence traceability. |
| `destination_system_id` | MUST when records are routed, written, indexed, published, or consumed by another system | Identifies downstream destination. |
| `output_destination` | MUST when output is displayed, routed, exported, released, indexed, or consumed downstream | Preserves release and routing context. |
| `policy_context_id` | MUST when policy affects ingestion, routing, release readiness, retention, evidence handling, or fail-closed behavior | Links ingestion to applicable policy context. |
| `audit_reference_id` | MUST for governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links ingestion to related case, policy, approval, tool, evidence, workflow, and audit records. |

## Source-System Requirements

Source systems used in governed workflows must have enough metadata to support trust, replay, and boundary validation.

At minimum, source-system records should define:

- accountable owner;
- source type and source environment;
- tenant, customer, workspace, subscription/account, and region scope where applicable;
- data classification and sensitivity label expectations;
- retention and legal-hold considerations where applicable;
- collection mechanism and allowed operations;
- expected latency and freshness range;
- known field limitations, parser dependencies, and schema assumptions;
- approved destinations and prohibited destinations;
- audit requirements for collection, parsing, transformation, enrichment, routing, retry, and failure.

A source system with missing ownership, ambiguous tenant/customer scope, unknown retention handling, or unauditable collection behavior must not feed sensitive governed workflows without controlled review.

## Normalization and Enrichment Requirements

Normalization and enrichment must be traceable, versioned, and bounded.

| Area | Requirement |
|---|---|
| Field mapping | Normalized fields must be linked to mapping logic, schema version, parser version, and source field references where available. |
| Source preservation | Original source records or source references must remain available according to evidence, audit, and retention requirements. |
| Lossy transformation | Dropped, truncated, inferred, merged, or reformatted fields must be identifiable during replay. |
| Enrichment provenance | Enrichment source, version, timestamp, freshness, confidence, and limitations must be preserved where material. |
| Boundary validation | Enrichment must not cross tenant, customer, case, workspace, evidence, retention, or allowed-use boundaries without authorization. |
| Conflict handling | Conflicting source and enrichment values must be preserved or routed for review. Enrichment must not silently overwrite source truth. |
| Downstream use | Outputs used for recommendations, routing, severity, reporting, approval packages, or evidence interpretation must carry sufficient provenance for review. |

## Tenant, Customer, Case, and Evidence Boundaries

Data ingestion must preserve separation between tenant identity, customer identity, case scope, and evidence attribution.

| Boundary | Requirement |
|---|---|
| Tenant boundary | Ingested records must preserve tenant or equivalent platform scope where applicable. |
| Customer boundary | MSSP, MDR, DFIR, customer-scoped, and multi-customer workflows must preserve `customer_id` separately from `tenant_id`. |
| Case boundary | Case-bound ingestion output must not be joined with unrelated matters unless policy authorizes the correlation. |
| Evidence boundary | Evidence-derived outputs must reference evidence objects and must not replace original evidence. |
| Retrieval boundary | RAG, vector search, shared memory, customer context, case memory, evidence retrieval, and retrieved context must remain within approved tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundaries. |
| Destination boundary | Records must not be routed to reporting, release, workflow, case, evidence, knowledge, or external destinations outside approved scope. |

## Agent Use of Ingested Data

Agents may use governed ingestion outputs to:

- retrieve scoped telemetry and context;
- summarize records with source references;
- identify missing metadata, parsing failures, schema mismatches, or enrichment limitations;
- correlate records within approved tenant, customer, case, evidence, and workflow boundaries;
- draft investigation notes, case context, report language, review packages, or approval packages;
- recommend next steps subject to policy, review, approval, and enforcement controls.

Agents must not:

- treat ingestion success as authorization for action;
- modify source records, evidence objects, collection rules, parser logic, normalized fields, or enrichment values outside governed change paths;
- invent source fields, evidence references, timestamps, tenant/customer identifiers, or confidence claims;
- bypass schema validation, scope checks, retention controls, review paths, approval paths, or audit logging;
- route ingestion outputs to customer-facing, external, legal, report, approval, or action workflows without required controls;
- treat model-generated summaries as original evidence, source truth, forensic proof, or policy decisions.

## Failure Handling

Ingestion workflows must fail closed, quarantine, or route to controlled review when:

- source-system metadata is missing, stale, ambiguous, unauthorized, or inconsistent;
- tenant, customer, workspace, subscription/account, case, evidence, destination, retention, or allowed-use scope is missing or mismatched;
- connector, collection rule, parser, schema, mapping, or transformation version cannot be determined where replay depends on it;
- parser or schema validation fails;
- enrichment is unavailable, stale, conflicting, untrusted, out of scope, or retention-inconsistent;
- source timestamps, collection timestamps, identity context, or provenance cannot be trusted;
- evidence attribution is missing where evidence-derived data is used;
- routing destination is unauthorized or ambiguous;
- audit logging fails where audit is required;
- downstream workflows depend on ingestion output that is partial, stale, contradictory, or unauditable.

Failure handling must preserve the original request, source reference, error details, scope context, affected records, policy context where available, routing decision, retry or quarantine status, and audit references.

## Ingestion Audit and Replay

Ingestion replay must be able to reconstruct:

- what source produced the record;
- when the source event occurred and when it was collected;
- which connector, collection rule, parser, schema, mapping, and transformation were used;
- what normalization and enrichment were applied;
- what fields were dropped, inferred, transformed, conflicted, or unavailable;
- which tenant, customer, workspace, subscription/account, case, evidence, and workflow scope applied;
- which destination or downstream workflow consumed the result;
- what failed, was quarantined, was retried, was excluded, or failed closed;
- which audit records and correlation identifiers link the ingestion path to later workflow activity.

Ingestion replay does not prove that a security finding, recommendation, or response decision was correct. It proves that the source-to-output path can be reconstructed, inspected, challenged, and correlated.

## Shared Intelligence Sanitization and Release

Reusable security knowledge derived from ingestion must be sanitized, approved, versioned, and scoped before distribution.

Shared intelligence release controls must ensure that:

- raw tenant data and raw customer data do not leave their approved boundary;
- customer identifiers, hostnames, user identities, secrets, evidence content, case details, and sensitive operational details are removed or transformed where required;
- sanitized intelligence is traceable to an approved release package without exposing raw source material;
- approval records define release scope, eligible tenants/customers, version, owner, and rollback or recall conditions;
- downstream consumers can determine whether intelligence is approved for detection, enrichment, reporting, triage, hunt, or agent context use;
- rollback, recall, correction, and exception paths are auditable.

## Relationship to Other Control Areas

- [`../tool-access/readme.md`](../tool-access/readme.md) defines governed tool registration, restricted tool patterns, scoped execution, and tool execution audit. Data ingestion depends on approved tools but does not authorize tool execution.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines PDP, PEP, approval policy, risk classification, and fail-closed behavior. Data ingestion provides source, scope, classification, and provenance context for policy decisions.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, and cross-tenant boundary controls. Data ingestion must preserve those identifiers before downstream use.
- [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) defines evidence references, finding support, and DFIR evidence handling. Data ingestion must not replace original evidence or chain-of-custody records.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines private/local LLM-assisted DFIR boundaries. Data ingestion supports local parsing, extraction, summarization, evidence references, and replay.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines audit event, correlation, replayability, failure audit, and immutable audit expectations. Data ingestion must emit records that can be replayed.
- [`../governance-library/ai-assurance/readme.md`](../governance-library/ai-assurance/readme.md) defines AI assurance and Agent Judge expectations. Ingested context used by assurance checks must preserve source, scope, and evidence references.

## Operational Anti-Patterns

Avoid the following:

- treating ingestion as trusted merely because the connector succeeded;
- allowing records with missing tenant, customer, case, source, parser, schema, classification, destination, retention, or audit metadata into governed workflows;
- overwriting source fields with enrichment values without preserving source and enrichment provenance;
- mixing tenants, customers, cases, workspaces, subscriptions/accounts, evidence sets, or memory scopes without authorization;
- routing raw customer or tenant data into shared intelligence packages;
- using agent-generated summaries as source records, original evidence, or approval evidence without source references;
- allowing downstream recommendations, reports, approvals, or actions to rely on unauditable ingestion paths;
- retrying failed ingestion in ways that duplicate, reorder, or silently mutate records without audit context;
- dropping parsing or normalization failures without review or audit;
- failing open when ingestion context is required for a governed workflow.

## Acceptance Criteria

This directory is acceptable when:

- source-system metadata requirements are clear;
- collection, parsing, normalization, enrichment, routing, failure, and replay expectations are separated;
- tenant identity and customer identity remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows;
- source records, normalized records, enriched records, summarized outputs, and evidence-derived outputs remain distinguishable;
- parser, schema, mapping, transformation, enrichment, connector, and collection-rule versions are preserved where they affect replay or downstream interpretation;
- ingestion outputs preserve data classification, sensitivity, allowed use, retention, destination, and downstream consumption context where required;
- evidence-derived ingestion output preserves evidence references and does not replace original evidence;
- retrieval and memory context remains within approved tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundaries;
- ingestion failures produce controlled quarantine, retry, exception, escalation, or fail-closed outcomes;
- shared intelligence release uses sanitized, approved, versioned, and recallable packages;
- audit replay can reconstruct the source-to-output path without relying on model memory or narrative explanations;
- ingestion success does not authorize tool execution, customer release, containment, remediation, closure, or formal approval.
