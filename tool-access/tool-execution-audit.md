# Tool Call Logging

## Purpose

This file defines the tool-call logging model for the `data-ingestion/` layer of the Governed Agentic MSSP / MDR / DFIR Security Operations Architecture repo.

Tool-call logging records how ingestion, retrieval, parsing, normalization, enrichment, routing, indexing, publication, evidence handling, and downstream data-use tools are invoked, scoped, mediated, evaluated, and consumed.

Tool-call logs provide replay, audit, troubleshooting, dispute review, policy handoff, evidence traceability, and downstream reconstruction. They do not authorize tool execution, approve customer release, replace human review, make PDP decisions, enforce PEP obligations, or certify forensic validity.

## Scope

This file applies to tool-call logging for:

- Data-ingestion connectors and collection tools.
- MCP servers, MCP clients, and MCP-exposed tools.
- Parser, schema-validation, normalization, transformation, summarization, enrichment, indexing, and routing tools.
- Evidence-store, case-store, ticketing, workflow-update, and report-store tools.
- Knowledge-store, vector-index, RAG, shared-memory, customer-context, case-memory, evidence-retrieval, and retrieved-context tools.
- Private/local LLM-assisted DFIR tooling that parses, extracts, summarizes, retrieves, or routes evidence.
- Tool calls whose outputs influence agent workflows, judge findings, human review, policy-enforcement handoffs, customer-facing wording, approval packages, governance evidence, or downstream operational use.

This file does not define the full PDP contract, PEP implementation, tool registry, evidence repository, approval workflow, or Agent Judge evaluation contract. Those controls belong in the appropriate repo areas.

## Non-Goals

Tool-call logging MUST NOT be used to:

- Treat a logged tool call as authorization to execute.
- Treat a successful tool call as approval, evidence completeness, incident truth, or forensic validation.
- Treat tool-call logs as a substitute for PDP decisions, PEP enforcement, human review, customer approval, or evidence authority.
- Use logs as the only source of tenant, customer, case, evidence, or retrieval scope.
- Store secrets, credentials, bearer tokens, private keys, managed identity tokens, or customer-sensitive payloads without approved redaction and protection.
- Treat private/local execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## Logging Principles

| Principle | Requirement |
|---|---|
| Complete reconstruction | Tool-call logs MUST support reconstruction of who or what invoked the tool, under which scope, against which source, producing which result, and how the result was consumed downstream. |
| Tenant and customer separation | Tool-call logs MUST preserve `tenant_id` and `customer_id` separately for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows. |
| Scope preservation | Tool-call logs MUST preserve case, workflow, workspace, subscription/account, evidence, source system, destination system, output destination, retention, and retrieval boundaries where applicable. |
| Policy and mediation traceability | Tool-call logs MUST record policy context, PEP/PDP handoff references, mediation path, approval context, and routing outcome where applicable. |
| Evidence traceability | Tool-call logs MUST preserve evidence object identifiers and evidence tenant/customer attribution when evidence is collected, retrieved, parsed, transformed, summarized, or referenced. |
| Retrieval boundary traceability | Tool-call logs MUST preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` when retrieval or memory affects tool output or downstream use. |
| Replayability | Tool-call logs MUST record schema, parser, transformation, normalization, enrichment, summarization, retrieval, and connector metadata needed for replay and dispute review. |
| Fail-closed support | Tool-call logging failure MUST fail closed or route to controlled review when logging is mandatory for governed workflow use. |

## Required Tool Call Log Record

Governed data-ingestion tool calls MUST produce a structured log record.

| Field | Requirement | Purpose |
|---|---|---|
| `tool_call_log_id` | MUST | Unique identifier for the tool-call log record. |
| `tool_call_id` | MUST | Unique identifier for the tool invocation. |
| `tool_request_id` | MUST | Links the log to the tool request. |
| `tool_response_id` | MUST when a response is produced | Links the log to the tool response. |
| `timestamp_utc` | MUST | Records when the tool call occurred. |
| `tool_id` | MUST | Identifies the tool invoked. |
| `tool_name` | MUST | Human-readable tool name. |
| `tool_version` | MUST for governed workflows | Supports replay, regression review, and audit reconstruction. |
| `tool_owner` | MUST for governed workflows | Identifies the accountable owner for tool operation, review, and remediation. |
| `tool_category` | MUST | Identifies connector, parser, enrichment, retrieval, evidence-store, case-store, workflow, or routing tool type. |
| `requested_operation` | MUST | Identifies the operation requested. |
| `authorized_operations` | MUST when policy, registry, or mediation controls define allowed operations | Records the allowed operation boundary used for evaluation. |
| `prohibited_operations` | MUST where sensitive misuse is possible | Records operations the tool MUST NOT perform. |
| `agent_id` | MUST when an agent requested or consumed the result | Identifies the agent associated with the tool call. |
| `agent_session_id` or `run_id` | MUST when an agent requested or consumed the result | Supports replay and run-level traceability. |
| `workflow_id` | MUST for governed workflows | Links the tool call to the governed workflow. |
| `workflow_stage` | MUST when routing, review, approval, or downstream handling depends on workflow stage | Preserves workflow-stage context. |
| `source_system_id` | MUST when the tool reads, collects, retrieves, parses, transforms, enriches, summarizes, indexes, or routes data from a source system | Identifies the source system, connector, evidence store, case store, knowledge store, API, or repository used by the tool. |
| `destination_system_id` | MUST when the tool writes, routes, exports, updates, publishes, indexes, releases, or sends data to another system | Identifies the destination system, case store, ticketing system, evidence store, knowledge store, vector index, report store, workflow, API, customer portal, or downstream service. |
| `output_destination` | MUST when tool output is routed, released, displayed, exported, used for customer-facing reporting, indexed, or consumed by downstream workflows | Preserves destination context for routing, release-readiness, customer boundary validation, and audit. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when tool use is tied to an investigation, incident, escalation, closure, customer-facing report, or DFIR workflow | Links tool use to the governed case. |
| `workspace_id` | MUST when workspace scope affects telemetry, evidence, access, or routing | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects tool use | Preserves cloud account, subscription, or project boundary. |
| `evidence_object_ids` | MUST when evidence or forensic artifacts are collected, retrieved, parsed, transformed, summarized, indexed, or referenced | Supports evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences tool output, evidence interpretation, routing, customer-facing wording, approval packages, or downstream use | Defines approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, freshness, and reuse scope remained within approved boundaries. |
| `connector_id` | MUST when connector-based ingestion or retrieval is used | Identifies the connector, agent, API integration, or collection mechanism. |
| `connector_version` | MUST when connector version affects parsing, field mapping, replay, or downstream interpretation | Supports troubleshooting, regression review, and audit replay. |
| `collection_rule_id` | MUST when collection rules select records, fields, sources, evidence, or events | Identifies the collection rule used to collect, filter, or route data. |
| `parser_id` | MUST when parsing is applied | Identifies the parser used to transform records. |
| `parser_version` | MUST when parsing affects field meaning, evidence interpretation, schema replay, or downstream use | Supports parser accountability and dispute review. |
| `schema_version` | MUST when normalized or structured records are produced | Identifies the output schema version used by downstream workflows. |
| `parser_or_transformation_version` | MUST when parsing, normalization, enrichment, summarization, extraction, transformation, field mapping, routing, indexing, publication, or retrieval changes field meaning or downstream interpretation | Supports transformation traceability, replay, regression review, and dispute analysis. |
| `normalization_metadata` | MUST when normalization is performed | Records normalization rules, mappings, derived fields, and preserved source references. |
| `enrichment_metadata` | MUST when enrichment is performed | Records enrichment source, freshness, confidence, and provenance. |
| `summarization_metadata` | MUST when summarization is performed | Records summary source references, generation context, and limitations. |
| `retrieval_metadata` | MUST when retrieval is performed | Records index/store identifier, retrieval timestamp, query reference, source references, and scope metadata where available. |
| `data_classification` | MUST when tool input, output, evidence, retrieved context, or transformed data has sensitivity, legal, customer, privacy, forensic, or regulated handling requirements | Preserves data-handling and release-control context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity or handling label context for tool input, output, evidence, or retrieved context. |
| `allowed_use` | MUST when tool output is constrained to specific workflow, case, customer, legal, governance, evidence-handling, or reporting purposes | Defines permitted downstream use of the tool result. |
| `retention_policy_id` | MUST when retention affects accessed data, tool output, evidence, or retrieved context | Preserves retention and disposal boundary. |
| `policy_context_id` | MUST when policy affects tool access, routing, release readiness, evidence handling, approval, retention, or fail-closed behavior | Links tool use to applicable policy context. |
| `policy_decision_reference` | MUST when a PDP decision governed access or downstream handling | Links the tool call to the policy decision without replacing it. |
| `pep_enforcement_reference` | MUST when PEP enforcement occurred | Links the tool call to enforcement outcome and obligations. |
| `approval_record_id` | MUST when tool use depends on formal approval | Links the tool call to a scoped approval record. |
| `audit_reference_id` | MUST when tool output is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, case, policy, approval, audit, evidence, and judge records. |
| `tool_status` | MUST | Records success, failure, partial, blocked, failed closed, quarantine, or review-required status. |
| `error_code` | MUST when the tool call fails, is blocked, or fails closed | Supports troubleshooting and controlled recovery. |
| `error_reason` | MUST when the tool call fails, is blocked, or fails closed | Records the controlled failure or routing reason. |
| `downstream_consumption` | MUST when the tool result is consumed by downstream workflows | Identifies downstream workflow, judge, report, case, policy handoff, approval package, or customer-facing use. |

## Request Logging Requirements

Tool request logs MUST capture the context needed to evaluate whether the tool call was allowed, scoped, mediated, and auditable.

| Field | Requirement | Purpose |
|---|---|---|
| `tool_request_id` | MUST | Unique identifier for the request. |
| `requested_operation` | MUST | Identifies the requested operation. |
| `requesting_identity` | MUST | Identifies the authenticated workload, user, service, agent, or workflow identity. |
| `agent_id` | MUST when an agent requested or influenced the request | Links request to the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent requested or influenced the request | Supports replay and run-level traceability. |
| `workflow_id` | MUST for governed workflows | Links request to the governed workflow. |
| `input_scope` | MUST | Defines source, destination, tenant, customer, case, evidence, retrieval, or operation scope. |
| `policy_context_id` | MUST when policy affects access or downstream handling | Preserves policy context. |
| `approval_record_id` | MUST when approval is required before tool use | Links request to scoped approval. |
| `correlation_ids` | MUST when available | Links request to related workflow, policy, approval, evidence, audit, and judge records. |

Free-form tool requests MUST NOT be used for governed workflows unless wrapped in structured context with required metadata.

## Response Logging Requirements

Tool response logs MUST capture enough metadata to determine what the tool returned, what scope was used, and whether the response is safe for downstream use.

| Field | Requirement | Purpose |
|---|---|---|
| `tool_response_id` | MUST | Unique identifier for the response. |
| `tool_request_id` | MUST | Links response to request. |
| `tool_id` | MUST | Identifies the responding tool. |
| `tool_version` | MUST for governed workflows | Supports replay and compatibility review. |
| `timestamp_utc` | MUST | Records response time. |
| `status` | MUST | Records success, failure, partial, blocked, failed closed, quarantine, or review-required status. |
| `result_reference` | MUST when result is stored or passed downstream | References result without uncontrolled reuse. |
| `schema_version` | MUST when response is structured | Supports validation and replay. |
| `evidence_object_ids` | MUST when evidence was accessed, retrieved, transformed, summarized, or referenced | Preserves evidence traceability. |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, freshness, and reuse scope remained within approved boundaries. |
| `scope_validation_result` | MUST when scope was evaluated | Records tenant, customer, case, workspace, evidence, output, and retrieval scope result. |
| `policy_decision_reference` | MUST when a PDP decision governed access | Links tool response to the policy decision without replacing it. |
| `audit_reference_id` | MUST when consumed by downstream governed workflows | Supports audit reconstruction. |
| `limitations` | MUST where material | Records partial results, stale data risk, retrieval limitations, missing evidence, or unresolved uncertainty. |

Tool responses MUST NOT be treated as approved, complete, or safe for downstream use merely because the tool returned successfully.

## Mediation and Policy Logging

Tool-call logs MUST preserve whether the tool call was mediated and which control path handled it.

| Field | Requirement | Purpose |
|---|---|---|
| `mediation_path` | MUST when the tool call is governed | Identifies workflow mediation, PEP/PDP path, MCP gateway, connector gateway, orchestration, service control, or manual review path. |
| `pdp_decision_id` | MUST when a PDP decision exists | Links the tool call to the governed policy decision. |
| `pdp_decision` | MUST when a PDP decision exists | Records the PDP decision without allowing the tool to replace the PDP. |
| `pep_enforcement_result` | MUST when PEP enforcement occurs | Records enforcement outcome and obligations. |
| `policy_obligation_ids` | MUST when obligations apply | Links applicable obligations to the tool call. |
| `approval_record_id` | MUST when formal approval is required | Links to approval state, scope, approver, timestamp, and expiration where applicable. |
| `human_review_record_id` | MUST when human review is required or completed | Links to human validation, correction, escalation, or review outcome. |
| `customer_approval_record_id` | MUST when customer-side approval is required | Links to customer authorization for release, access, remediation, containment, reporting, or evidence handling. |

Tool-call logs MAY include policy-relevant context. They MUST NOT represent tool output, tool success, or a log record as a PDP decision.

## Evidence and Retrieval Logging

When tool calls affect evidence, retrieval, memory, or knowledge-store context, logs MUST preserve the boundary and source metadata needed for downstream review.

Tool-call logs MUST record, where applicable:

- Evidence object identifiers.
- Evidence tenant and customer attribution.
- Evidence source system and collection metadata.
- Chain-of-custody references where applicable.
- Parser, schema, transformation, extraction, summarization, and normalization metadata.
- Knowledge store or memory scope.
- Retrieval source, retrieval timestamp, query reference, retrieved context reference, index identifier, vector index identifier, or store identifier.
- Knowledge memory scope result.
- Retention policy and allowed-use constraints.
- Downstream workflow, report, case, judge, or approval package that consumed the result.

Tool-call logs MUST NOT substitute for the evidence repository, chain-of-custody record, examiner validation, or original evidence object.

## Fail-Closed Conditions

The governed workflow, PEP, orchestration layer, MCP gateway, connector gateway, or tool mediation layer MUST fail closed, quarantine, or route to controlled review when:

- Tool-call logging is unavailable where logging is mandatory.
- Tool request, response, result, scope, identity, policy, approval, or audit identifiers cannot be recorded.
- Required tenant, customer, case, workflow, workspace, subscription/account, source, evidence, destination, or approval context is missing or ambiguous.
- Evidence tenant or customer attribution is missing or inconsistent for evidence used in governed workflows.
- `knowledge_store_or_memory_scope` is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influences tool output, agent output, evidence interpretation, routing, customer-facing wording, approval packages, or downstream use.
- `knowledge_memory_scope_result` indicates retrieval or memory scope did not remain within approved boundaries.
- Required source system, destination system, output destination, connector, collection rule, parser, schema, parser/transformation version, data classification, sensitivity label, allowed use, retention, or policy-context metadata is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where governed tool use, parsing, normalization, enrichment, retrieval, routing, indexing, publication, reporting, approval routing, or downstream use depends on it.
- Tool request or response schema validation fails.
- Tool identity, credential, token audience, managed identity, service principal, delegated permission, scoped grant, or role assignment is out of scope.
- Tool output attempts to modify case, evidence, workflow, approval, routing, or customer-facing records outside approved scope.
- Tool output attempts to imply approval, execution, containment success, closure, legal determination, forensic proof, or customer notification without governed workflow context.
- Human review or approval is required but missing, expired, revoked, incomplete, or out of scope.
- Audit logging fails where audit is mandatory.
- Tool result is required for a governed workflow but is unavailable, partial, stale, or inconsistent.

Fail-closed handling MUST preserve the original request, response where available, error details, scope context, evidence references, policy context, approval context, routing reason, and audit references.

## Audit Requirements

Governed tool-call logging MUST support audit reconstruction of:

- Tool request and result identifiers.
- Tool identity, version, owner, category, and requested operation.
- Source system, destination system, output destination, connector ID, connector version, collection rule, parser ID, parser version, schema version, parser_or_transformation_version, data classification, sensitivity label, allowed use, retention policy, policy context, routing, and downstream consumption where governed tool use, parsing, normalization, enrichment, retrieval, routing, indexing, publication, reporting, approval routing, or downstream use occurs.
- Requesting identity, agent identity, and session or run identifier where applicable.
- Tenant, customer, case, workflow, workspace, subscription/account, source, and destination context.
- Evidence object identifiers and evidence tenant/customer attribution where evidence is collected, retrieved, transformed, summarized, or referenced.
- `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced tool output, agent output, routing, reporting, approval packages, or downstream use.
- Schema validation, parser/transformation handling, normalization, enrichment, summarization, retrieval, indexing, publication, and routing metadata.
- Policy context, PDP decision reference, PEP enforcement reference, approval record, audit reference, and correlation identifiers where applicable.
- Human review routing, customer approval routing, correction, quarantine, retry, exception, or break-glass events.
- Downstream workflow, judge, report, case, or customer-facing use of tool output where applicable.

Audit records MUST support reconstruction of which tool was used, under which identity and scope, against which source and destination, producing which result, and how that result was consumed downstream.

## Privacy, Redaction, and Secret Handling

Tool-call logs MUST protect sensitive values.

Tool-call logs MUST NOT store:

- Raw bearer tokens.
- API keys.
- Private keys.
- Passwords.
- Session cookies.
- Managed identity tokens.
- Unredacted secrets.
- Customer data beyond what is required for governed audit reconstruction.
- Evidence payloads where evidence references are sufficient and policy requires reference-only logging.

Tool-call logs SHOULD store references, hashes, identifiers, redacted values, or scoped metadata rather than raw sensitive payloads where possible.

Redaction MUST NOT remove required tenant, customer, case, evidence, source, destination, retrieval, policy, approval, or audit context needed for governed review.

## Operational Anti-Patterns

The following patterns violate this tool-call logging model:

- Executing governed tool calls without a structured log record.
- Treating a tool-call log as authorization to execute.
- Treating tool success as human review, customer approval, incident truth, forensic proof, or customer-release readiness.
- Logging only free-text descriptions without tenant, customer, case, source, destination, evidence, retrieval, policy, or audit identifiers.
- Logging raw secrets, tokens, credentials, or uncontrolled customer payloads.
- Dropping source, destination, parser, schema, transformation, retrieval, or policy metadata needed for replay.
- Allowing tool-call logs to omit `knowledge_store_or_memory_scope` when retrieval or memory influenced tool output or downstream use.
- Allowing downstream systems to consume tool output when mandatory logging failed.
- Using local/private execution as proof that tool output is correct, tenant-safe, customer-safe, or forensically valid.
- Allowing Entra Agent ID, agent registry, identity governance, or lifecycle controls to be treated as operational SOC agents.

## Acceptance Criteria

This file is acceptable when:

- Tool-call logs record request, response, identity, scope, source, destination, policy, approval, evidence, retrieval, and downstream consumption context where applicable.
- Tool-call logs preserve tenant identity and customer identity separately for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows.
- Tool-call logs preserve evidence object identifiers and evidence tenant/customer attribution when evidence is involved.
- Tool-call logs preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` when retrieval or memory affects tool output or downstream use.
- Tool-call logs preserve connector, collection-rule, parser, schema, parser_or_transformation_version, normalization, enrichment, summarization, retrieval, indexing, publication, classification, sensitivity label, allowed use, retention, and policy context where required for audit replay.
- Tool-call logs remain separate from PDP authorization, PEP enforcement, Agent Judge assurance, human review, customer approval, tool execution, evidence authority, and forensic certification.
- Fail-closed handling exists when mandatory logging, identity, scope, source, destination, evidence, retrieval, policy, approval, or audit metadata is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope.
- Audit replay can reconstruct source system, destination system, output destination, connector, collection rule, parser, schema version, parser_or_transformation_version, classification, sensitivity label, allowed use, retention, policy context, routing, and downstream consumption.
