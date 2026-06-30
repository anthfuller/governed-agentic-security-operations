# Tool Registry

## Purpose

This file defines the tool registry model for the `data-ingestion/` layer of the Governed Agentic MSSP / MDR / DFIR Security Operations Architecture repo.

The tool registry records approved ingestion, retrieval, parsing, normalization, enrichment, evidence-store, case-store, routing, publication, indexing, MCP-exposed, and private/local DFIR tools before they are used by governed workflows.

The registry establishes tool identity, ownership, versioning, scope, source and destination boundaries, allowed operations, prohibited operations, required metadata, mediation requirements, audit requirements, and fail-closed expectations.

A tool registry record does not authorize execution by itself. Tool execution still requires governed workflow mediation, PEP/PDP handling where applicable, required approval paths, human review where required, and audit coverage.

## Scope

This file applies to registry records for:

- Data-ingestion connectors and collection tools.
- MCP servers, MCP clients, and MCP-exposed tools used for ingestion or retrieval.
- Parser, schema-validation, normalization, transformation, enrichment, summarization, indexing, publication, and routing tools.
- Evidence-store, case-store, ticketing, report-store, and workflow-update tools.
- Knowledge-store, vector-index, RAG, shared-memory, customer-context, case-memory, evidence-retrieval, and retrieved-context tools.
- Private/local LLM-assisted DFIR tools that parse, extract, summarize, retrieve, or route evidence.
- Tools whose outputs may influence agent workflows, Agent Judge findings, human review, customer-facing wording, approval packages, governance evidence, policy-enforcement context, or downstream operational use.

This file does not define the full PDP contract, PEP implementation, tool permission decision logic, evidence repository, approval workflow, or Agent Judge evaluation contract. Those controls belong in the appropriate repo areas.

## Non-Goals

The tool registry MUST NOT be used to:

- Treat tool registration as authorization to execute any exposed operation.
- Treat a registry record as a PDP decision.
- Treat registry approval as human approval, customer approval, release approval, evidence validation, incident truth, or forensic certification.
- Allow agents to self-register or self-authorize tools for governed use.
- Allow tools to bypass PEP/PDP, workflow mediation, human review, approval, evidence handling, or audit controls.
- Treat retrieved context, vector search results, RAG grounding, shared memory, or case memory as complete, current, authorized, or reusable without scope validation.
- Treat private/local execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## Registry Principles

| Principle | Requirement |
|---|---|
| Registered before governed use | Tools MUST be registered before they are used in governed data-ingestion workflows. |
| Explicit ownership | Every governed tool MUST have an accountable owner for registration, operation, review, remediation, and retirement. |
| Versioned operation | Tool versions, connector versions, parser versions, schema versions, and transformation versions MUST be recorded where downstream interpretation or replay depends on them. |
| Operation-specific control | Allowed and prohibited operations MUST be explicitly defined. |
| Tenant and customer separation | `tenant_id` and `customer_id` MUST remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows. |
| Source and destination traceability | Registry records MUST preserve source system, destination system, and output destination context where applicable. |
| Evidence boundary control | Registry records MUST preserve evidence object identifiers and evidence tenant/customer attribution requirements where evidence is accessed, transformed, retrieved, summarized, indexed, or referenced. |
| Retrieval boundary control | Registry records MUST preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` requirements where retrieval or memory affects tool output or downstream use. |
| Fail-closed by default | Missing, ambiguous, unauthorized, stale, inconsistent, unauditable, cross-boundary, or out-of-scope registry context MUST fail closed or route to controlled review when governed workflows depend on the tool. |

## Required Tool Registry Record

Governed data-ingestion tools MUST have a structured registry record.

| Field | Requirement | Purpose |
|---|---|---|
| `tool_registry_id` | MUST | Unique identifier for the registry record. |
| `tool_id` | MUST | Unique identifier for the tool. |
| `tool_name` | MUST | Human-readable tool name. |
| `tool_version` | MUST for governed workflows | Supports replay, regression review, compatibility review, and audit reconstruction. |
| `tool_owner` | MUST for governed workflows | Identifies the accountable owner for tool registration, operation, review, remediation, and retirement. |
| `tool_category` | MUST | Identifies connector, parser, enrichment, retrieval, evidence-store, case-store, workflow, routing, publication, indexing, or MCP-exposed tool type. |
| `tool_environment` | MUST | Identifies production, staging, lab, local, private, customer-specific, or development environment. |
| `tool_status` | MUST | Identifies draft, approved-for-governed-use, restricted, deprecated, revoked, suspended, or retired state. |
| `authorized_operations` | MUST | Defines operations allowed for the tool, such as read, collect, retrieve, parse, enrich, normalize, summarize, index, publish, route, export, store, or update. |
| `prohibited_operations` | MUST where sensitive misuse is possible | Defines operations the tool MUST NOT perform. |
| `restricted_operations` | MUST when the tool has elevated-risk operations | Identifies operations requiring policy gating, approval, human review, or additional mediation. |
| `source_system_id` | MUST when the tool collects, retrieves, parses, enriches, transforms, routes, indexes, publishes, or stores data from a source system | Identifies the source system, connector, evidence store, case store, knowledge store, API, repository, platform, or data source used by the tool. |
| `destination_system_id` | MUST when tool output is routed, written, exported, published, indexed, released, or consumed by another system | Identifies the destination system, case store, ticketing system, evidence store, knowledge store, vector index, report store, workflow, API, customer portal, or downstream service. |
| `output_destination` | MUST when tool output affects routing, reporting, approval, disclosure, evidence handling, indexing, publication, release, or downstream consumption | Identifies where tool output is sent, stored, indexed, published, released, displayed, or consumed. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when tool use is tied to an investigation, incident, escalation, closure, customer-facing report, or DFIR workflow | Links tool use to the governed case. |
| `workflow_id` | MUST for governed workflows | Links the tool to governed workflow usage. |
| `workspace_id` | MUST when workspace scope affects telemetry, evidence, access, retrieval, routing, or downstream use | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects tool use | Preserves cloud account, subscription, or project boundary. |
| `evidence_object_ids` | MUST when evidence or forensic artifacts are collected, retrieved, parsed, transformed, summarized, indexed, or referenced | Supports evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influences tool output, evidence interpretation, routing, customer-facing wording, approval packages, or downstream use | Defines approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result_required` | MUST when retrieval or memory scope must be evaluated before downstream use | Identifies whether `knowledge_memory_scope_result` must be produced before the tool result is consumed. |
| `connector_id` | MUST when connector-based ingestion or retrieval is used | Identifies the connector, agent, API integration, or collection mechanism. |
| `connector_version` | MUST when connector version affects parsing, field mapping, replay, or downstream interpretation | Supports troubleshooting, regression review, and audit replay. |
| `collection_rule_id` | MUST when collection rules select records, fields, sources, evidence, or events | Identifies the collection rule used to collect, filter, or route data. |
| `parser_id` | MUST when parsing is applied | Identifies the parser used to transform records. |
| `parser_version` | MUST when parsing affects field meaning, evidence interpretation, schema replay, or downstream use | Supports parser accountability and dispute review. |
| `schema_version` | MUST when normalized or structured records are produced | Identifies the output schema version used by downstream workflows. |
| `parser_or_transformation_version` | MUST when parsing, normalization, enrichment, summarization, extraction, transformation, field mapping, routing, indexing, publication, or retrieval changes field meaning or downstream interpretation | Supports transformation traceability, replay, regression review, and dispute analysis. |
| `data_classification` | MUST when tool input, output, evidence, retrieved context, or transformed data has sensitivity, legal, customer, privacy, forensic, or regulated handling requirements | Preserves data-handling and release-control context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity or handling label context for tool input, output, evidence, or retrieved context. |
| `allowed_use` | MUST when tool output is constrained to specific workflow, case, customer, legal, governance, evidence-handling, or reporting purposes | Defines permitted downstream use of the tool result. |
| `retention_policy_id` | MUST when retention affects accessed data, tool output, evidence, indexed data, or retrieved context | Preserves retention and disposal boundary. |
| `policy_context_id` | MUST when policy affects tool access, routing, release readiness, evidence handling, approval, retention, or fail-closed behavior | Links tool use to applicable policy context. |
| `approval_record_id` | MUST when tool registration or use depends on formal approval | Links the tool or operation to a scoped approval record. |
| `audit_reference_id` | MUST when the registry record is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, case, policy, approval, audit, evidence, and judge records. |

## Registry Lifecycle States

| State | Meaning |
|---|---|
| `DRAFT` | Tool record is incomplete and MUST NOT be used in governed workflows. |
| `APPROVED_FOR_GOVERNED_USE` | Tool may be used only within the registered scope, authorized operations, mediation path, policy context, and audit requirements. |
| `RESTRICTED` | Tool has elevated-risk operations and requires additional policy gating, approval, review, or controlled routing. |
| `SUSPENDED` | Tool use is temporarily blocked pending review, remediation, or investigation. |
| `REVOKED` | Tool use is blocked and MUST NOT proceed in governed workflows. |
| `DEPRECATED` | Tool is being phased out and MUST NOT be used for new governed workflows unless explicitly approved. |
| `RETIRED` | Tool is no longer available for governed use. |

Tool lifecycle state MUST NOT be treated as a PDP authorization decision. A registered and approved state means the tool may be considered by governed workflows within scope; it does not authorize a specific execution.

## Registration Review Requirements

Tool registration MUST be reviewed when:

- A new tool, MCP server, connector, parser, enrichment source, retrieval interface, evidence-store tool, or case-store tool is added.
- A tool changes owner, version, operation, source system, destination system, output destination, connector, parser, schema, transformation, retrieval source, or policy context.
- A tool begins handling customer-facing, DFIR-impacting, legal-sensitive, governance, approval-routing, or evidence-affecting outputs.
- A tool begins using RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context.
- A tool crosses tenant, customer, case, workspace, subscription/account, evidence, retention, reuse, or output-destination boundaries.
- A tool is suspended, revoked, deprecated, or retired.

Human review may validate registry completeness, ownership, scope, evidence support, and control readiness. Human review does not replace PDP authorization, PEP enforcement, customer approval, or formal approval where required.

## PEP/PDP Handoff Boundary

Tool registry records MUST preserve separation between registry, tool execution, PEP, PDP, Agent Judges, human review, and customer approval.

| Component | Responsibility |
|---|---|
| Tool registry | Records tool identity, owner, version, scope, allowed operations, prohibited operations, required metadata, lifecycle state, and audit context. |
| Data-ingestion tool | Performs a scoped operation only when permitted by workflow, identity, policy, and scope controls. |
| Agent | May request or consume tool output only through governed workflow mediation. |
| Agent Judge | May evaluate output quality, evidence support, tenant boundary, HITL compliance, or retrieval risk as assurance only. |
| PDP | Produces governed authorization decisions according to the policy contract. |
| PEP | Enforces PDP decisions and obligations at the workflow, tool, or execution boundary. |
| Human Reviewer | Validates high-impact output, scope, evidence support, and unresolved risk. |
| Customer Approval Path | Handles customer-side approval where required for release, containment, remediation, access, or reporting. |
| Audit System | Records registry use, permission checks, tool requests, decision context, result, routing, and downstream use. |

A registry record MUST NOT be treated as a PDP or PEP decision unless the governed PDP or PEP path explicitly evaluates and enforces it.

## Evidence and Retrieval Registry Requirements

Tool registry records MUST identify evidence and retrieval boundaries before the tool result is consumed downstream.

Registry records MUST preserve, where applicable:

- Evidence object identifiers.
- Evidence tenant and customer attribution.
- Evidence source system and collection metadata.
- Case and workflow association.
- Chain-of-custody requirements where applicable.
- Knowledge store or memory scope.
- Retrieval source, retrieval timestamp expectations, index identifier, vector index identifier, or store identifier.
- Requirement to produce `knowledge_memory_scope_result` where retrieval or memory scope is evaluated.
- Retention policy and allowed-use constraints.
- Downstream workflow, report, case, judge, approval package, or customer-facing use.

Tool registry records MUST NOT substitute for the evidence repository, chain-of-custody record, examiner validation, or original evidence object.

## Private/Local LLM-Assisted DFIR Registry Requirements

Private/local LLM-assisted DFIR tool registry records MUST satisfy these requirements:

- Local execution MUST be treated as an execution and evidence-handling context, not proof of correctness.
- Local tools MUST remain bound to approved evidence stores, case scope, tenant scope, customer scope, and examiner workflow.
- RAG, vector search, shared memory, customer context, case memory, evidence retrieval, and retrieved context MUST remain within approved `knowledge_store_or_memory_scope`.
- Extracted artifacts, parsed outputs, summaries, and report drafts MUST preserve evidence references.
- Customer-facing DFIR conclusions MUST require evidence validation, examiner review, auditability, and the appropriate approval path.

## Fail-Closed Conditions

The governed workflow, PEP, orchestration layer, MCP gateway, connector gateway, or tool mediation layer MUST fail closed, quarantine, or route to controlled review when:

- Tool registry record is missing, expired, revoked, suspended, deprecated, inconsistent, or out of scope for the requested operation.
- Requested operation is not listed in authorized operations or is listed in prohibited operations.
- Required tenant, customer, case, workflow, workspace, subscription/account, source, evidence, destination, or approval context is missing or ambiguous.
- Evidence tenant or customer attribution is missing or inconsistent for evidence used in governed workflows.
- `knowledge_store_or_memory_scope` is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influences tool output, agent output, evidence interpretation, routing, customer-facing wording, approval packages, or downstream use.
- `knowledge_memory_scope_result` is required but missing, unavailable, inconsistent, stale, or indicates retrieval or memory scope did not remain within approved boundaries.
- Required source system, destination system, output destination, connector, collection rule, parser, schema, parser/transformation version, data classification, sensitivity label, allowed use, retention, or policy-context metadata is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where governed tool use, parsing, normalization, enrichment, retrieval, routing, indexing, publication, reporting, approval routing, or downstream use depends on it.
- Tool request or response schema validation fails.
- Tool identity, requesting identity, credential, token audience, managed identity, service principal, delegated permission, scoped grant, or role assignment is out of scope.
- Tool output attempts to modify case, evidence, workflow, approval, routing, or customer-facing records outside approved scope.
- Tool output attempts to imply approval, execution, containment success, closure, legal determination, forensic proof, or customer notification without governed workflow context.
- Human review or approval is required but missing, expired, revoked, incomplete, or out of scope.
- Audit logging fails where audit is mandatory.
- Tool result is required for a governed workflow but is unavailable, partial, stale, or inconsistent.

Fail-closed handling MUST preserve the original request, registry record reference, permission result where available, response where available, error details, scope context, evidence references, policy context, approval context, routing reason, and audit references.

## Audit Requirements

Governed tool registry use MUST audit:

- Tool registry, permission, request, and result identifiers.
- Tool identity, version, owner, category, lifecycle state, and requested operation.
- Source system, destination system, output destination, connector ID, connector version, collection rule, parser ID, parser version, schema version, parser_or_transformation_version, data classification, sensitivity label, allowed use, retention policy, policy context, routing, and downstream consumption where governed tool use, parsing, normalization, enrichment, retrieval, routing, indexing, publication, reporting, approval routing, or downstream use occurs.
- Requesting identity, agent identity, and session or run identifier where applicable.
- Tenant, customer, case, workflow, workspace, subscription/account, source, and destination context.
- Evidence object identifiers and evidence tenant/customer attribution where evidence is collected, retrieved, transformed, summarized, or referenced.
- `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced tool output, agent output, routing, reporting, approval packages, or downstream use.
- Policy context, PDP decision reference, PEP enforcement reference, approval record, audit reference, and correlation identifiers where applicable.
- Human review routing, customer approval routing, correction, quarantine, retry, exception, or break-glass events.
- Downstream workflow, judge, report, case, or customer-facing use of tool output where applicable.

Audit records MUST support reconstruction of which tool was registered, under which owner and lifecycle state, with which allowed and prohibited operations, against which source and destination, under which identity and scope, and how the result was consumed downstream.

## Operational Anti-Patterns

The following patterns violate this tool registry model:

- Using an unregistered tool in governed ingestion, retrieval, parsing, enrichment, evidence, case, routing, or publication workflows.
- Treating tool registration as permission to execute every exposed operation.
- Treating a registry record as a PDP decision outside the governed PDP decision contract.
- Allowing an agent to self-register, self-authorize, or self-approve data-ingestion tool use.
- Allowing tools to access tenants, customers, cases, workspaces, subscriptions/accounts, evidence sets, destinations, or memory scopes without explicit registry and permission context.
- Using RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context outside approved `knowledge_store_or_memory_scope`.
- Reusing retrieved context without validating freshness, retention, tenant, customer, case, evidence, workspace, and reuse boundaries.
- Allowing tool registration to imply containment, remediation, eradication, recovery, access change, closure, customer notification, legal determination, or approval.
- Allowing tool-generated evidence summaries to replace original evidence, examiner validation, or chain-of-custody records.
- Allowing Entra Agent ID, agent registry, identity governance, or lifecycle controls to be treated as operational SOC agents.
- Failing open when registry, permission, schema, identity, policy, evidence attribution, retrieval boundary, approval context, or audit context is missing.

## Acceptance Criteria

This file is acceptable when:

- Tool registry records use explicit tool identity, owner, version, lifecycle state, requested operation, authorized operations, prohibited operations, source, destination, tenant, customer, case, evidence, retention, policy, approval, and audit context.
- Tool registry remains separate from PDP authorization, PEP enforcement, Agent Judge assurance, human review, customer approval, tool execution, evidence authority, and forensic certification.
- Tool registry preserves tenant identity and customer identity separately for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows.
- Tool registry preserves source system, destination system, output destination, connector, collection rule, parser, schema version, parser_or_transformation_version, classification, sensitivity label, allowed use, retention, policy context, routing, and downstream consumption where required for replay and audit.
- Tool registry preserves evidence object identifiers and evidence tenant/customer attribution when evidence is involved.
- Tool registry preserves `knowledge_store_or_memory_scope` and requires `knowledge_memory_scope_result` when retrieval or memory affects tool output or downstream use.
- Tool registry does not allow agents or tools to self-register or self-authorize governed access.
- Fail-closed handling exists when registry, permissioning, identity, scope, source, destination, evidence, retrieval, policy, approval, or audit metadata is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope.
- Audit replay can reconstruct the registered tool, owner, lifecycle state, requested operation, requesting identity, source system, destination system, output destination, connector, collection rule, parser, schema version, parser_or_transformation_version, classification, sensitivity label, allowed use, retention, policy context, routing, and downstream consumption.
