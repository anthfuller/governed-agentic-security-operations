# Ingestion Failure Handling

## Purpose

This file defines how ingestion failures are detected, classified, contained, routed, retried, escalated, audited, and replayed in governed agentic security operations.

Ingestion failure handling protects downstream MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows from incomplete, stale, misattributed, malformed, unauthorized, cross-tenant, or unauditable data.

Ingestion failure handling does not prove incident truth or evidence completeness. It preserves failure context so analysts, workflow owners, policy controls, and audit replay can determine whether downstream use is allowed, blocked, retried, quarantined, or escalated.

## Scope

This file applies to ingestion failures involving:

- source-system connectivity;
- connector registration and connector versioning;
- collection rules;
- parser execution;
- schema validation;
- timestamp handling;
- normalization;
- enrichment;
- deduplication;
- routing;
- indexing;
- evidence references;
- tenant, customer, case, workspace, subscription, account, or project attribution;
- data classification, sensitivity labels, allowed use, and retention metadata;
- ingestion audit and replay records;
- shared intelligence sanitization and release controls.

This file does not define production retry infrastructure, queue implementation, SIEM parser code, vendor-specific connector configuration, evidence repository design, legal sufficiency, or runtime incident-response procedures.

## Core Principles

- Ingestion failures MUST be visible, classified, scoped, and auditable.
- Missing or ambiguous tenant, customer, case, workspace, source, evidence, retention, or classification context MUST trigger fail-closed handling where downstream governed workflows depend on that context.
- Partial ingestion MUST NOT be treated as complete ingestion.
- Successful connector execution MUST NOT be treated as proof that all expected records were collected, parsed, enriched, normalized, routed, or indexed correctly.
- Failed, partial, stale, malformed, or quarantined data MUST NOT be used for customer-facing reports, approval packages, containment recommendations, shared intelligence, or DFIR conclusions unless the limitation is reviewed, recorded, and approved where required.
- Agents MAY summarize failure context, identify affected workflows, and prepare review packages.
- Agents MUST NOT suppress ingestion failures, relabel failed data as valid, retry prohibited operations, override policy, or release failure-affected outputs without governed review and approval.
- Failure correction MUST preserve the original failure record and append correction, replay, reprocessing, or disposition records.

## Failure Category Summary

| Failure Category | Description | Required Handling |
|---|---|---|
| `SOURCE_UNAVAILABLE` | Source system, API, stream, bucket, workspace, mailbox, repository, evidence store, or connector endpoint is unavailable. | Record outage context, affected scope, collection window, retry eligibility, and downstream impact. |
| `AUTHORIZATION_FAILURE` | Identity, credential, token, role, delegated grant, managed identity, service principal, or scoped permission is invalid, expired, revoked, or out of scope. | Block collection, preserve identity context, route to owner review, and audit denied access. |
| `SCOPE_MISMATCH` | Tenant, customer, case, workspace, subscription, account, project, region, or evidence scope does not match the expected workflow boundary. | Fail closed, quarantine affected records, and route to boundary review. |
| `SCHEMA_VALIDATION_FAILURE` | Raw, parsed, normalized, enriched, or routed records do not satisfy the expected schema or required fields. | Quarantine affected records, preserve parser and schema versions, and block downstream use until corrected. |
| `PARSER_FAILURE` | Parser error, unsupported format, field extraction failure, field collision, encoding issue, or parser-version mismatch. | Preserve raw reference, parser ID, parser version, error details, and correction path. |
| `NORMALIZATION_FAILURE` | Field mapping, semantic mapping, entity mapping, severity mapping, timestamp mapping, or provider-to-common-schema mapping fails. | Quarantine or mark records as limited-use, preserve mapping version, and block unsupported downstream assumptions. |
| `ENRICHMENT_FAILURE` | Threat intelligence, asset, identity, vulnerability, geo, ownership, business context, or cloud metadata enrichment fails or becomes stale. | Preserve base record, record enrichment limitation, block unsupported conclusions, and retry where allowed. |
| `TIMESTAMP_OR_ORDERING_FAILURE` | Source time, collection time, event time, processing time, ordering, deduplication, or replay sequence cannot be trusted. | Preserve time fields, record uncertainty, and block timeline-dependent conclusions until resolved. |
| `DUPLICATE_OR_GAP_DETECTED` | Duplicate records, missing intervals, dropped events, pagination gaps, stream offsets, or collection-window gaps are detected. | Record affected windows, estimate impact where possible, and route to review or replay. |
| `CLASSIFICATION_OR_RETENTION_FAILURE` | Data classification, sensitivity label, legal hold, retention policy, or allowed-use metadata is missing or inconsistent. | Fail closed for governed downstream use and route to data-handling review. |
| `EVIDENCE_REFERENCE_FAILURE` | Evidence object IDs, hashes, manifests, source attribution, or chain-of-custody references are missing or inconsistent. | Block evidence-derived conclusions and route to evidence review. |
| `AUDIT_FAILURE` | Required ingestion audit events, correlation IDs, replay records, or failure records cannot be produced or persisted. | Block sensitive downstream use and route to approved exception handling. |
| `DOWNSTREAM_ROUTING_FAILURE` | Case store, ticketing system, evidence store, data lake, vector index, knowledge store, report store, or workflow destination rejects or misroutes records. | Stop routing, preserve destination context, quarantine affected outputs, and audit impact. |
| `SANITIZATION_FAILURE` | Sanitization, de-identification, deduplication, customer-boundary validation, or release-scope validation fails before shared intelligence use. | Block release and route to governed review. |

## Failure Severity Model

| Severity | Condition | Handling |
|---|---|---|
| `LOW` | Failure affects non-sensitive, non-customer-facing, non-evidence, non-action-influencing internal data with no material downstream impact. | Log, monitor, and retry where allowed. |
| `MODERATE` | Failure affects ingestion completeness, enrichment quality, parser output, normalization quality, routing, or analyst context. | Record limitation, notify workflow owner, and prevent unsupported downstream conclusions. |
| `HIGH` | Failure affects customer-scoped records, evidence references, approval packages, detection logic, response recommendations, shared intelligence, or incident severity. | Quarantine or fail closed, route to analyst review, and require audit linkage before downstream use. |
| `CRITICAL` | Failure creates cross-tenant, cross-customer, evidence-integrity, unauthorized-access, policy-bypass, release, containment, or audit-path risk. | Fail closed, block downstream use, preserve all context, escalate, and require governed disposition. |

## Required Failure Record

Every governed ingestion failure MUST produce a structured failure record.

| Field | Requirement | Purpose |
|---|---|---|
| `ingestion_failure_id` | MUST | Unique identifier for the failure event. |
| `failure_category` | MUST | Classifies the failure type. |
| `failure_severity` | MUST | Defines handling priority and downstream restrictions. |
| `failure_time_utc` | MUST | Records when the failure was detected. |
| `detected_by` | MUST | Identifies connector, parser, workflow, monitor, analyst, agent, judge, policy control, or audit component that detected the issue. |
| `source_system_id` | MUST | Identifies the affected source system. |
| `connector_id` | MUST when connector-based collection is involved | Links the failure to the connector. |
| `connector_version` | MUST when version affects behavior | Supports replay and regression review. |
| `collection_rule_id` | MUST when collection rules selected records | Identifies collection scope. |
| `parser_id` | MUST when parsing was involved | Identifies the parser. |
| `parser_version` | MUST when parsing affects record meaning | Supports parser accountability and replay. |
| `schema_version` | MUST when structured records are affected | Identifies expected schema. |
| `normalization_mapping_id` | MUST when normalization is affected | Identifies the mapping used. |
| `enrichment_source_id` | MUST when enrichment is affected | Identifies the enrichment source. |
| `tenant_id` | MUST for tenant-scoped workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when case-bound | Links failure to investigation, incident, ticket, or DFIR matter. |
| `workflow_id` | MUST when a governed workflow is affected | Links failure to workflow context. |
| `workspace_id` | MUST when workspace scope affects ingestion | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects ingestion | Preserves cloud boundary context. |
| `evidence_object_ids` | MUST when evidence is involved | Preserves evidence traceability. |
| `affected_time_window` | MUST where measurable | Identifies affected collection or event interval. |
| `affected_record_count` | SHOULD where measurable | Supports impact assessment. |
| `data_classification` | MUST when classification affects handling | Preserves sensitivity context. |
| `sensitivity_label` | MUST when applicable | Preserves handling label context. |
| `allowed_use` | MUST when downstream use is constrained | Defines permitted use of affected records. |
| `retention_policy_id` | MUST when retention affects handling | Preserves retention boundary. |
| `policy_context_id` | MUST when policy affects failure handling | Links failure handling to policy context. |
| `approval_record_id` | MUST when approval affects retry, release, exception, or downstream use | Links handling to scoped approval. |
| `audit_reference_id` | MUST | Supports audit replay. |
| `correlation_ids` | MUST when available | Links related ingestion, workflow, case, evidence, policy, approval, and audit records. |
| `failure_detail` | MUST | Provides concise error and impact detail. |
| `handling_state` | MUST | Records blocked, quarantined, retrying, degraded, corrected, replayed, escalated, accepted-risk, or closed state. |
| `downstream_restrictions` | MUST when downstream use is affected | Defines what cannot consume the affected data. |
| `disposition_owner` | MUST for high or critical failures | Identifies accountable owner for disposition. |

## Detection Requirements

Ingestion controls MUST detect and record failures at each governed stage:

| Stage | Required Detection |
|---|---|
| Source connection | Availability, authentication, authorization, rate limit, source-side error, regional mismatch, and source contract changes. |
| Collection | Missing intervals, pagination errors, stream offsets, event gaps, duplicate collection, filter mismatch, and collection-rule drift. |
| Parsing | Unsupported format, malformed records, field extraction failure, parser version mismatch, and field collision. |
| Schema validation | Required field absence, invalid type, invalid enumeration, invalid timestamp, unexpected nesting, and schema version mismatch. |
| Normalization | Semantic mapping failure, provider-specific field ambiguity, entity mapping failure, and loss of source meaning. |
| Enrichment | Missing enrichment, stale enrichment, conflicting enrichment, unauthorized enrichment source, and enrichment scope mismatch. |
| Routing | Destination rejection, wrong destination, case mismatch, evidence-store mismatch, ticket mismatch, indexing failure, and output-destination mismatch. |
| Audit | Missing correlation ID, missing failure record, missing replay reference, failed persistence, and unauditable correction. |

## Handling States

| State | Meaning | Downstream Use |
|---|---|---|
| `DETECTED` | Failure has been observed but not yet classified. | Not allowed for sensitive downstream use. |
| `CLASSIFIED` | Failure category and severity are assigned. | Allowed only according to recorded restrictions. |
| `QUARANTINED` | Affected records are isolated from governed downstream consumption. | Not allowed until reviewed or corrected. |
| `RETRY_PENDING` | Retry is allowed and scheduled or queued. | Not allowed unless policy permits degraded use. |
| `REPLAY_PENDING` | Reprocessing or replay is required to reconstruct affected records. | Not allowed for final outputs until replay outcome is recorded. |
| `DEGRADED_USE_ALLOWED` | Limited use is permitted with recorded limitations. | Allowed only within defined scope and limitations. |
| `REVIEW_REQUIRED` | Human review is required before use, retry, exception, release, or closure. | Not allowed until review outcome is recorded. |
| `APPROVAL_REQUIRED` | Formal approval is required before exception, release, or sensitive downstream use. | Not allowed until approval is granted and scoped. |
| `CORRECTED` | Correction has been applied and linked to the original failure. | Allowed according to correction scope and validation result. |
| `CLOSED` | Failure has a final disposition. | Allowed only according to final disposition. |

## Fail-Closed Conditions

The ingestion workflow MUST fail closed, quarantine affected records, or route to controlled review when:

- source, connector, collection rule, parser, schema, normalization, enrichment, routing, or audit metadata is missing, ambiguous, stale, inconsistent, unauthorized, or unauditable;
- tenant identity, customer identity, case scope, workspace scope, subscription/account/project scope, evidence scope, or output destination is missing, ambiguous, mismatched, or out of scope;
- evidence object identifiers, source attribution, hashes, manifests, chain-of-custody references, or evidence tenant/customer attribution are missing or inconsistent where evidence is used;
- data classification, sensitivity label, allowed use, retention policy, legal hold, or release constraint cannot be resolved where downstream handling depends on it;
- parser, schema, normalization, enrichment, or routing changes field meaning without preserving versioned transformation context;
- ingestion failure affects customer-facing reports, approval packages, containment recommendations, case closure, shared intelligence, or DFIR conclusions;
- retry would cross tenant, customer, case, evidence, workspace, subscription, account, project, retention, or output-destination boundaries;
- audit logging, correlation, failure record creation, or replay linkage fails where audit is mandatory;
- an agent, tool, connector, parser, enrichment source, or downstream workflow attempts to suppress, relabel, overwrite, or bypass the failure state.

## Quarantine Requirements

Quarantine MUST be used when affected data cannot be safely consumed by governed workflows.

Quarantine records MUST preserve:

- failure record identifier;
- raw record reference where available;
- parsed or transformed record reference where available;
- source system and connector context;
- parser, schema, normalization, and enrichment context;
- tenant, customer, case, workspace, subscription/account/project, and evidence scope;
- data classification, sensitivity label, allowed use, and retention context;
- reason for quarantine;
- owner and review route;
- permitted remediation or replay path;
- audit reference.

Quarantined records MUST NOT be silently reintroduced into normal workflow output, shared intelligence, customer-facing reports, approval packages, or DFIR conclusions.

## Retry and Reprocessing Requirements

Retry and reprocessing MUST be governed by scope, policy, auditability, and downstream risk.

Retries MAY occur automatically only when all of the following are true:

- the requested retry operation is registered and allowed;
- tenant, customer, case, workspace, source, destination, retention, and evidence boundaries remain unchanged and authorized;
- retry does not require formal approval;
- retry does not create duplicate, conflicting, or misordered records without deduplication and replay controls;
- retry preserves the original failure record and creates a retry audit record.

Retries MUST route to review or approval when they involve:

- high or critical severity failures;
- evidence-affecting workflows;
- customer-facing reports or approval packages;
- shared intelligence release;
- cross-tenant or multi-customer scope;
- privileged credentials or new authorization grants;
- retention or legal-hold ambiguity;
- ingestion windows that could materially change incident severity, timeline, impact, containment recommendations, or closure.

Reprocessed records MUST preserve references to the original failure, the correction or replay operation, the versioned parser or transformation used, and the downstream records affected by the correction.

## Degraded Mode

Degraded mode MAY be used only when policy permits limited use of incomplete, delayed, or partially enriched data.

Degraded mode MUST define:

- affected source systems;
- affected tenants, customers, cases, workspaces, subscriptions, accounts, projects, and evidence sets;
- affected time windows;
- unavailable fields or enrichment sources;
- unsupported conclusions;
- permitted downstream uses;
- prohibited downstream uses;
- review or approval requirements;
- expiration or re-evaluation point;
- audit reference.

Degraded mode MUST NOT be used to bypass fail-closed requirements for evidence-impacting workflows, customer-facing release, containment recommendations, cross-tenant sanitization, or formal approval paths.

## Tenant, Customer, Case, and Evidence Boundaries

Failure handling MUST preserve tenant, customer, case, workspace, subscription/account/project, and evidence boundaries.

When attribution cannot be validated, affected records MUST be quarantined or failed closed.

Cross-tenant, cross-customer, cross-case, cross-workspace, cross-account, cross-project, or cross-evidence ambiguity MUST NOT be resolved by model inference, analyst assumption, or connector convenience.

Evidence-derived records MUST retain evidence object identifiers and evidence tenant/customer attribution. Evidence summaries, extracted fields, normalized events, and enriched records MUST remain distinguishable from original evidence.

## Agent Use of Failure Context

Agents MAY:

- summarize ingestion failure records;
- identify affected sources, time windows, cases, workflows, and downstream outputs;
- suggest retry, replay, quarantine, or escalation paths;
- draft review packages for analysts;
- identify likely downstream limitations;
- compare failure records against policy and audit requirements.

Agents MUST NOT:

- suppress ingestion failures;
- mark failed records as valid without governed correction;
- infer missing tenant, customer, case, evidence, or retention scope as fact;
- retry prohibited or approval-required ingestion operations;
- release failure-affected findings, reports, or shared intelligence without required review and approval;
- treat partial, stale, malformed, or unauditable data as complete;
- replace analyst review, formal approval, or evidence validation.

## Human Review and Approval

Human review is required when ingestion failure affects:

- incident severity, scope, timeline, containment recommendation, or closure;
- customer-scoped reporting;
- DFIR evidence handling;
- shared intelligence sanitization or release;
- high or critical severity classification;
- cross-tenant, cross-customer, cross-case, workspace, subscription, account, or project ambiguity;
- degraded-mode use for governed workflows.

Formal approval is required when policy requires approval for exception handling, release, retry, replay, evidence-affecting use, or customer-impacting downstream action.

Human review and formal approval MUST remain separate records.

## Audit and Replay Requirements

Ingestion failure handling MUST support replay of:

- the original source and collection context;
- connector, collection rule, parser, schema, normalization, enrichment, and routing versions;
- failure category and severity;
- affected tenant, customer, case, workspace, subscription/account/project, evidence, source, destination, and time window;
- failure detection source;
- quarantine, retry, replay, degraded-mode, review, approval, exception, or closure path;
- downstream records, workflows, reports, cases, indexes, or approval packages affected;
- correction records and reprocessing outcomes;
- final disposition and owner.

Audit records MUST prove the handling path without relying on model memory, narrative summaries, or mutable dashboards as the source of truth.

## Relationship to Other Data-Ingestion Files

| File | Relationship |
|---|---|
| [`data-ingestion-model.md`](data-ingestion-model.md) | Defines the baseline ingestion model and control expectations. |
| [`source-system-metadata.md`](source-system-metadata.md) | Defines source identity, ownership, scope, classification, and retention metadata required for failure handling. |
| [`normalization-and-enrichment.md`](normalization-and-enrichment.md) | Defines transformation and enrichment expectations that failures must preserve and replay. |
| [`ingestion-audit-replay.md`](ingestion-audit-replay.md) | Defines audit and replay requirements for ingestion decisions, transformations, failures, corrections, and downstream use. |
| [`shared-intelligence-sanitization-and-release-controls.md`](shared-intelligence-sanitization-and-release-controls.md) | Defines sanitization and release controls that must block failure-affected shared intelligence. |

## Operational Anti-Patterns

The following patterns violate governed ingestion failure handling:

- treating connector success as ingestion completeness;
- using partial records without recording limitations;
- allowing agents to suppress failure states;
- silently rewriting failed records instead of appending correction records;
- retrying denied, unauthorized, approval-required, or out-of-scope ingestion operations automatically;
- routing quarantined records to cases, reports, indexes, approval packages, or shared intelligence outputs;
- allowing malformed records to influence severity, containment, closure, or DFIR conclusions;
- inferring missing tenant, customer, case, evidence, retention, or classification metadata;
- copying raw evidence, secrets, tokens, credentials, or unnecessary customer data into failure records;
- failing open when audit, correlation, evidence attribution, policy context, or approval context is missing.

## Acceptance Criteria

This file is acceptable when:

- ingestion failure categories are defined and tied to governed handling requirements;
- failure severity determines downstream restrictions, review, escalation, quarantine, retry, replay, or fail-closed behavior;
- required failure records preserve source, connector, parser, schema, transformation, enrichment, routing, tenant, customer, case, workspace, evidence, classification, retention, policy, approval, and audit context where applicable;
- partial, stale, malformed, unauthorized, cross-scope, or unauditable data cannot silently influence governed workflows;
- quarantined data is isolated from normal downstream use until corrected, reviewed, or dispositioned;
- retry and reprocessing preserve original failure records and append replay or correction records;
- degraded mode has explicit limits, expiration, and audit records;
- agents may assist with failure analysis but cannot override policy, approval, evidence validation, or fail-closed controls;
- human review and formal approval remain separate controls;
- audit replay can reconstruct what failed, why it failed, what was affected, how it was handled, and what final disposition was reached.
