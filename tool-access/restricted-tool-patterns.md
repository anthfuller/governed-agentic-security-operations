# MCP Security Model

## Purpose

This file defines the security model for Model Context Protocol (MCP) servers, MCP clients, MCP tools, and MCP-mediated data-ingestion access in the Governed Agentic MSSP / MDR / DFIR Security Operations Architecture repo.

The MCP security model exists to ensure that agents, workflows, and downstream assurance components can use MCP-connected tools without bypassing tenant, customer, case, evidence, policy, approval, retrieval, or audit boundaries.

MCP provides a tool and context interface. It does not replace policy enforcement, identity governance, human review, customer approval, evidence validation, or forensic accountability.

## Scope

This file applies to MCP use in the `data-ingestion/` layer when MCP servers or MCP-exposed tools are used to:

- Access SIEM, XDR, EDR, NDR, cloud, SaaS, identity, email, firewall, ticketing, or business-application telemetry.
- Retrieve or enrich data from case stores, evidence stores, knowledge stores, vector indexes, shared memory, customer context, or case memory.
- Support ingestion, parsing, normalization, enrichment, summarization, retrieval, or evidence-reference workflows.
- Provide tools to agentic SOC, MSSP, MDR, Cloud Incident Response, or private/local LLM-assisted DFIR workflows.
- Influence investigation summaries, routing recommendations, escalation, containment recommendations, customer-facing wording, governance evidence, or approval packages.

This file does not define the full agent lifecycle model, tool registry model, approval workflow, evidence repository model, or PDP contract. Those controls belong in the appropriate governance, human-oversight, evidence, and policy-enforcement files.

## Non-Goals

The MCP security model MUST NOT be used to:

- Treat an MCP server as a PDP.
- Treat an MCP server as a human approver.
- Treat MCP tool availability as authorization to execute a tool.
- Treat MCP tool output as final incident truth, forensic proof, legal conclusion, or compliance determination.
- Treat retrieved context, vector-search output, shared memory, or case memory as complete, current, authorized, or reusable without scope validation.
- Bypass PEP/PDP, approval, review, audit, tenant, customer, case, evidence, retention, or output-destination controls.
- Treat private/local MCP deployment as proof of correctness or forensic validity.

## MCP Security Boundary

The MCP security boundary is the controlled interface between agents or workflows and external tools, data sources, retrieval systems, or context providers.

MCP servers and MCP tools MUST be treated as mediated access surfaces.

An MCP server may expose capabilities, but it MUST NOT independently authorize sensitive actions, customer-facing release, evidence release, containment, remediation, case closure, or policy exceptions.

Sensitive MCP tool use MUST be governed by explicit identity, scope, policy, approval, and audit controls before tool output is consumed by downstream workflows.

## Required Separation of Responsibilities

| Component | Responsibility | Limitation |
|---|---|---|
| Agent | Requests data, context, or tool use through governed workflows. | MUST NOT self-authorize MCP tool access or execute outside approved scope. |
| MCP Client | Connects the agent or workflow to approved MCP servers. | MUST NOT bypass workflow, identity, policy, or audit controls. |
| MCP Server | Exposes approved tools, resources, prompts, or context interfaces. | MUST NOT act as PDP, human approver, evidence authority, or customer-release authority. |
| MCP Tool | Performs a scoped operation such as read, retrieve, parse, enrich, store, or update. | MUST NOT exceed registered operation, identity, tenant, customer, case, evidence, or retention scope. |
| PEP | Enforces PDP decisions and obligations at the workflow, tool, or execution boundary. | MUST remain separate from MCP tool logic unless explicitly implemented as a governed enforcement component. |
| PDP | Produces governed authorization decisions according to the policy contract. | MUST remain the source of authorization decisions where policy gating is required. |
| Agent Judge | Evaluates MCP-related output, evidence support, boundary handling, or quality as assurance only. | MUST NOT authorize MCP execution or override PEP/PDP decisions. |
| Human Reviewer | Reviews high-impact outputs, evidence support, scope, and unresolved risk. | MUST NOT be replaced by MCP tool success or judge output. |
| Customer Approval Path | Handles customer-side approval where required for release, containment, remediation, access, or reporting. | MUST remain separate from MCP tool invocation. |
| Audit System | Records MCP requests, responses, scope, identity, policy context, and downstream use. | MUST support replay and reconstruction. |

Entra Agent ID, agent registry, identity governance, lifecycle management, ownership, and authorization controls belong in the Agent Governance and Identity Control Plane. They MUST NOT be treated as operational SOC agents.

## MCP Trust Assumptions

MCP servers and tools MUST be treated as untrusted or partially trusted components unless explicitly governed.

The architecture MUST assume that MCP tool descriptions, resource metadata, retrieved context, prompts, and responses can be incomplete, stale, maliciously influenced, misconfigured, overbroad, or scoped incorrectly.

MCP security controls MUST validate:

- Who or what is requesting tool access.
- Which agent, workflow, case, tenant, and customer are in scope.
- Which MCP server and tool are being invoked.
- Which operation is requested.
- Which data source, evidence store, knowledge store, vector index, or memory scope is accessed.
- Which output destination or downstream workflow will consume the result.
- Whether policy, approval, or human review is required before use.

## Required MCP Registration Fields

Every MCP server and MCP-exposed tool used in governed workflows MUST have a registration record.

| Field | Requirement | Purpose |
|---|---|---|
| `mcp_server_id` | MUST | Unique identifier for the MCP server. |
| `mcp_server_name` | MUST | Human-readable MCP server name. |
| `mcp_server_version` | MUST for governed workflows | Supports replay, compatibility checks, regression review, and audit reconstruction. |
| `mcp_server_owner` | MUST | Identifies accountable owner. |
| `mcp_server_environment` | MUST | Identifies production, staging, lab, local, private, or customer-specific environment. |
| `tool_id` | MUST | Unique identifier for the MCP tool. |
| `tool_name` | MUST | Human-readable MCP tool name. |
| `tool_version` | MUST for governed workflows | Supports replay, audit, and change control. |
| `tool_category` | MUST | Identifies connector, parser, enrichment, retrieval, evidence-store, case-store, or workflow tool type. |
| `source_system_id` | MUST when MCP-mediated tool use collects, retrieves, parses, enriches, transforms, routes, indexes, publishes, or stores data from a source system | Identifies the source system or platform used for ingestion replay and audit reconstruction. |
| `destination_system_id` | MUST when MCP tool output is routed, written, exported, published, indexed, released, or consumed by another system | Identifies the destination system, case store, ticketing system, evidence store, knowledge store, vector index, report store, workflow, API, customer portal, or downstream service. |
| `output_destination` | MUST when MCP tool output affects routing, reporting, approval, disclosure, evidence handling, or downstream consumption | Identifies where MCP tool output is sent, stored, indexed, published, released, or consumed. |
| `data_classification` | MUST when classification affects access, routing, retention, release, approval, or customer-facing use | Preserves classification context for handling and downstream use. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, handling, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when MCP tool output is constrained to specific workflow, case, customer, legal, governance, evidence-handling, or reporting purposes | Defines permitted downstream use of the MCP tool result. |
| `connector_id` | MUST when connector-based ingestion or retrieval is used | Identifies the connector, agent, API integration, or collection mechanism. |
| `connector_version` | MUST when connector version affects parsing, field mapping, replay, or downstream interpretation | Supports troubleshooting, regression review, and audit replay. |
| `collection_rule_id` | MUST when collection rules select records, fields, sources, evidence, or events | Identifies the collection rule used to collect, filter, or route data. |
| `parser_id` | MUST when parsing is applied | Identifies the parser used to transform records. |
| `parser_version` | MUST when parsing affects field meaning, evidence interpretation, schema replay, or downstream use | Supports parser accountability and dispute review. |
| `schema_version` | MUST when normalized or structured records are produced | Identifies the output schema version used by downstream workflows. |
| `parser_or_transformation_version` | MUST when parsing, normalization, enrichment, summarization, extraction, transformation, field mapping, routing, indexing, publication, or retrieval changes field meaning or downstream interpretation | Supports transformation traceability, replay, regression review, and dispute analysis. |
| `authorized_operations` | MUST | Defines allowed operations such as read, retrieve, parse, enrich, normalize, store, or update case metadata. |
| `prohibited_operations` | MUST where sensitive misuse is possible | Defines operations the MCP tool MUST NOT perform. |
| `approved_data_sources` | MUST when tool access touches telemetry, evidence, enrichment, knowledge, memory, or customer data | Defines data sources the tool may access. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when tool use is case-bound | Links MCP tool use to an investigation, incident, or DFIR case. |
| `workflow_id` | MUST for governed workflows | Links MCP use to the governed workflow. |
| `workspace_id` | MUST when workspace scope affects MCP access or downstream use | Preserves SIEM, XDR, cloud, or logging workspace boundary. |
| `subscription_id` or `account_id` | MUST when cloud account scope affects MCP access or downstream use | Preserves cloud account, project, or subscription boundary. |
| `evidence_object_ids` | MUST when MCP access collects, retrieves, transforms, summarizes, or references evidence | Preserves evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in a multi-tenant or customer-scoped workflow | Preserves evidence-to-tenant attribution. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in a customer-scoped workflow | Preserves evidence-to-customer attribution. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context is exposed or consumed through MCP | Defines approved retrieval, memory, vector-store, customer-context, case-memory, tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundary. |
| `policy_context_id` | MUST when policy affects MCP access, routing, release readiness, approval, evidence handling, or fail-closed behavior | Links MCP use to applicable policy context. |
| `approval_record_id` | MUST when MCP use depends on formal approval | Links the MCP operation to a scoped approval record. |
| `audit_reference_id` | MUST when MCP output is consumed by governed workflow routing, assurance, reporting, or policy handoff | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, MCP, tool, case, policy, approval, audit, evidence, and judge records. |
| `retention_policy_id` | MUST when retention affects MCP-accessed data or retrieved context | Preserves retention and disposal boundary. |

## MCP Access Control Requirements

MCP server and tool access MUST enforce least privilege.

| Control | Requirement |
|---|---|
| Client identity | MCP clients MUST authenticate using approved identity mechanisms for the deployment context. |
| Server authorization | MCP servers MUST allow only approved clients, workflows, agents, or service identities. |
| Tool authorization | MCP tools MUST validate that the requested operation is allowed for the requesting identity and workflow context. |
| Tenant and customer scope | MCP access MUST remain within approved tenant and customer boundaries. |
| Case scope | MCP access MUST remain within approved case or incident boundaries where case-bound workflows apply. |
| Evidence scope | MCP access MUST preserve evidence object identifiers and attribution metadata when evidence is accessed. |
| Knowledge and memory scope | MCP retrieval MUST remain within approved `knowledge_store_or_memory_scope` where retrieval or memory is used. |
| Destination scope | MCP results MUST NOT be routed to customer-facing, external, legal, governance, or operational destinations without required review and approval paths. |
| Credential handling | Tokens, keys, managed identities, service principals, delegated credentials, and scoped grants MUST NOT be exposed to agents or uncontrolled prompts. |
| Tool output handling | MCP responses MUST be treated as untrusted input until schema, scope, evidence, and policy checks are satisfied. |

## MCP Request Requirements

MCP tool requests used in governed workflows MUST include structured context sufficient for authorization, mediation, audit, and downstream use.

| Field | Requirement | Purpose |
|---|---|---|
| `mcp_request_id` | MUST | Unique MCP request identifier. |
| `mcp_server_id` | MUST | Identifies the MCP server receiving the request. |
| `tool_id` | MUST | Identifies the MCP tool requested. |
| `requested_operation` | MUST | Identifies the operation being requested. |
| `agent_id` | MUST when an agent requested or influenced the request | Identifies the agent associated with MCP use. |
| `agent_session_id` or `run_id` | MUST when an agent requested or influenced the request | Supports replay and run-level traceability. |
| `workflow_id` | MUST for governed workflows | Links request to governed workflow. |
| `workflow_stage` | MUST when routing, review, or authorization depends on workflow stage | Preserves stage-specific handling. |
| `tenant_id` | MUST for tenant-scoped or multi-tenant workflows | Preserves tenant boundary. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` | MUST when case-bound | Links request to the governed case. |
| `input_scope` | MUST | Defines data, source, evidence, retrieval, or operation scope. |
| `source_system_id` | MUST when MCP-mediated ingestion, retrieval, parsing, enrichment, transformation, routing, indexing, publication, or downstream use depends on a source system | Identifies the source system or platform used for replay and audit reconstruction. |
| `destination_system_id` | MUST when MCP tool output is routed, written, exported, published, indexed, released, or consumed by another system | Identifies the destination system, case store, ticketing system, evidence store, knowledge store, vector index, report store, workflow, API, customer portal, or downstream service. |
| `data_classification` | MUST when classification affects access, routing, retention, release, approval, or customer-facing use | Preserves classification context for handling and downstream use. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, handling, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when MCP tool output is constrained to specific workflow, case, customer, legal, governance, evidence-handling, or reporting purposes | Defines permitted downstream use of the MCP tool result. |
| `connector_id` | MUST when connector-based ingestion or retrieval is used | Identifies the connector, agent, API integration, or collection mechanism. |
| `collection_rule_id` | MUST when collection rules select records, fields, sources, evidence, or events | Identifies the collection rule used to collect, filter, or route data. |
| `parser_id` | MUST when parsing is applied | Identifies the parser used to transform records. |
| `schema_version` | MUST when normalized or structured records are produced | Identifies the output schema version used by downstream workflows. |
| `parser_or_transformation_version` | MUST when parsing, normalization, enrichment, summarization, extraction, transformation, field mapping, routing, indexing, publication, or retrieval changes field meaning or downstream interpretation | Supports transformation traceability, replay, regression review, and dispute analysis. |
| `output_destination` | MUST when downstream handling depends on destination | Identifies internal, customer-facing, governance, legal, case-system, ticketing, or workflow destination. |
| `knowledge_store_or_memory_scope` | MUST when retrieval or memory is used | Defines approved retrieval and memory boundary. |
| `policy_context_id` | MUST when policy affects access or handling | Preserves policy context. |
| `approval_record_id` | MUST when approval is required before MCP use | Links the request to scoped approval. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, approval, and audit records. |

Free-form MCP requests MUST NOT be used for governed workflows unless wrapped in structured context with required metadata.

## MCP Response Requirements

MCP responses consumed by governed workflows MUST preserve enough context for validation, replay, review, and audit.

| Field | Requirement | Purpose |
|---|---|---|
| `mcp_response_id` | MUST | Unique MCP response identifier. |
| `mcp_request_id` | MUST | Links response to request. |
| `mcp_server_id` | MUST | Identifies responding MCP server. |
| `tool_id` | MUST | Identifies responding MCP tool. |
| `tool_version` | MUST for governed workflows | Supports replay and compatibility review. |
| `timestamp_utc` | MUST | Records response time. |
| `status` | MUST | Records success, failure, partial, blocked, failed closed, or review-required status. |
| `result_reference` | MUST when result is stored or passed downstream | References result without uncontrolled reuse. |
| `source_system_id` | MUST when MCP-mediated ingestion, retrieval, parsing, enrichment, transformation, routing, indexing, publication, or downstream use depends on a source system | Identifies the source system or platform used for replay and audit reconstruction. |
| `destination_system_id` | MUST when MCP tool output is routed, written, exported, published, indexed, released, or consumed by another system | Identifies the destination system, case store, ticketing system, evidence store, knowledge store, vector index, report store, workflow, API, customer portal, or downstream service. |
| `output_destination` | MUST when MCP tool output affects routing, reporting, approval, disclosure, evidence handling, or downstream consumption | Identifies where MCP tool output is sent, stored, indexed, published, released, or consumed. |
| `data_classification` | MUST when classification affects access, routing, retention, release, approval, or customer-facing use | Preserves classification context for handling and downstream use. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, handling, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when MCP tool output is constrained to specific workflow, case, customer, legal, governance, evidence-handling, or reporting purposes | Defines permitted downstream use of the MCP tool result. |
| `connector_id` | MUST when connector-based ingestion or retrieval is used | Identifies the connector, agent, API integration, or collection mechanism. |
| `connector_version` | MUST when connector version affects parsing, field mapping, replay, or downstream interpretation | Supports troubleshooting, regression review, and audit replay. |
| `collection_rule_id` | MUST when collection rules select records, fields, sources, evidence, or events | Identifies the collection rule used to collect, filter, or route data. |
| `parser_id` | MUST when parsing is applied | Identifies the parser used to transform records. |
| `parser_version` | MUST when parsing affects field meaning, evidence interpretation, schema replay, or downstream use | Supports parser accountability and dispute review. |
| `schema_version` | MUST when response is structured | Supports validation and replay. |
| `parser_or_transformation_version` | MUST when parsing, normalization, enrichment, summarization, extraction, transformation, field mapping, routing, indexing, publication, or retrieval changes field meaning or downstream interpretation | Supports transformation traceability, replay, regression review, and dispute analysis. |
| `evidence_object_ids` | MUST when evidence was accessed, retrieved, transformed, summarized, or referenced | Preserves evidence traceability. |
| `knowledge_memory_scope_result` | MUST when knowledge store or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, freshness, and reuse scope remained within approved boundaries. |
| `scope_validation_result` | MUST when scope was evaluated | Records tenant, customer, case, workspace, evidence, output, and retrieval scope result. |
| `policy_decision_reference` | MUST when a PDP decision governed access | Links MCP response to the policy decision without replacing it. |
| `audit_reference_id` | MUST when consumed by downstream governed workflows | Supports audit reconstruction. |
| `limitations` | MUST where material | Records partial results, stale data risk, retrieval limitations, missing evidence, or unresolved uncertainty. |

MCP responses MUST NOT be treated as approved, complete, or safe for downstream use merely because the tool returned successfully.

## MCP Mediation Requirements

MCP tool use MUST be mediated when it:

- Accesses tenant-scoped, customer-scoped, case-scoped, workspace-scoped, subscription/account-scoped, evidence-scoped, or memory-scoped data.
- Retrieves from knowledge stores, vector indexes, shared memory, customer context, case memory, evidence stores, or prior-case context.
- Influences agent output, judge findings, routing recommendations, escalation, containment, closure, governance evidence, customer-facing reports, approval packages, or policy context.
- Modifies cases, tickets, queues, workflow records, evidence metadata, or routing state.
- Uses privileged credentials, managed identities, service principals, scoped tokens, delegated credentials, or customer-specific access grants.
- Crosses tenant, customer, environment, workspace, subscription, account, case, evidence, memory, retention, or reuse boundaries.

Mediation MAY be implemented through workflow controls, a PEP/PDP path, MCP gateway controls, approved orchestration, connector policy, or service control.

## Policy Enforcement Boundary

MCP tools MAY provide policy-relevant context to the PDP.

MCP tools MUST NOT produce governed authorization decisions unless the tool itself is explicitly implemented, registered, governed, tested, and audited as a PDP.

The PDP remains responsible for producing governed authorization decisions such as `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`.

The PEP remains responsible for enforcing PDP decisions and obligations at the workflow, tool, or execution boundary.

Agents, MCP clients, MCP servers, MCP tools, and Agent Judges MUST NOT bypass the PEP/PDP path where policy-gated access, release, execution, or routing is required.

## Human Review and Approval Boundaries

Human review and formal approval MUST remain separate from MCP tool success.

Human review may validate MCP-related evidence support, scope, quality, and downstream readiness.

Formal approval may authorize customer-facing release, containment, remediation, access change, evidence release, or other sensitive workflow steps where policy requires approval.

MCP tool invocation MUST NOT be treated as human review, customer approval, release approval, or authorization to execute sensitive actions.

## Evidence Handling Requirements

When MCP tools access or process evidence:

- Evidence object identifiers MUST be preserved.
- Evidence tenant and customer attribution MUST be preserved.
- Evidence transformation MUST be distinguishable from original evidence.
- Source timestamps, collection timestamps, collector identity, source system, parser version, and transformation history MUST be preserved where applicable.
- MCP-generated summaries MUST NOT replace original evidence, chain-of-custody records, analyst notes, or examiner validation.
- Customer-facing DFIR conclusions MUST require the appropriate evidence validation, human review, and approval path.

## Knowledge Store, Vector Search, and Memory Requirements

When MCP exposes or consumes RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context:

- `knowledge_store_or_memory_scope` MUST be defined before retrieval is used in governed outputs or downstream workflows.
- Retrieval MUST be scoped to approved tenant, customer, case, evidence, workspace, retention, freshness, and reuse boundaries.
- `knowledge_memory_scope_result` MUST be recorded when retrieval or memory scope is evaluated.
- Retrieved context MUST preserve source references, retrieval timestamp, index or store identifier, and scope metadata where available.
- Retrieved context MUST NOT be treated as complete, current, authorized, or reusable without scope validation.
- Cross-customer, cross-tenant, cross-case, stale, unauthorized, or retention-inconsistent retrieval MUST fail closed or route to governed review.

## Private/Local LLM-Assisted DFIR Considerations

Private or local MCP deployment may reduce exposure to external services, but it does not prove correctness, tenant safety, customer safety, forensic validity, legal sufficiency, or evidence completeness.

For private/local LLM-assisted DFIR workflows:

- MCP servers and tools MUST remain bound to approved local evidence stores, case scope, customer scope, and examiner workflow.
- Local retrieval, vector search, shared memory, and case memory MUST remain within approved `knowledge_store_or_memory_scope`.
- MCP-generated extraction, parsing, or summarization output MUST preserve evidence references.
- Local execution MUST be treated as an execution and evidence-handling context, not proof of correctness.
- Customer-facing DFIR conclusions MUST require evidence validation, examiner review, auditability, and the appropriate approval path.

## Fail-Closed Conditions

The governed workflow, MCP gateway, PEP, orchestration layer, or tool mediation layer MUST fail closed, quarantine, or route to controlled review when:

- MCP server registration is missing, expired, revoked, or inconsistent with the requested operation.
- MCP tool registration is missing, expired, revoked, or inconsistent with the requested operation.
- Required tenant, customer, case, workspace, subscription/account, source, evidence, destination, or workflow context is missing or ambiguous.
- Evidence tenant or customer attribution is missing or inconsistent for evidence used in governed workflows.
- `knowledge_store_or_memory_scope` is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influences MCP tool output, agent output, evidence interpretation, routing, customer-facing wording, approval packages, or downstream use.
- MCP request or response schema validation fails.
- Required source system, destination system, output destination, connector, collection rule, parser, schema, parser/transformation version, data classification, sensitivity label, allowed use, retention, or policy-context metadata is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where MCP-mediated ingestion, parsing, normalization, enrichment, retrieval, routing, indexing, publication, reporting, approval routing, or downstream use depends on it.
- MCP server, tool, parser, enrichment, or retrieval version cannot be determined where replay or audit is required.
- MCP client identity, server identity, tool identity, credential, token audience, managed identity, service principal, delegated permission, or role assignment is out of scope.
- MCP output attempts to modify case, evidence, workflow, approval, routing, or customer-facing records outside approved scope.
- MCP output attempts to imply approval, execution, containment success, closure, legal determination, forensic proof, or customer notification without governed workflow context.
- Audit logging fails where audit is mandatory.
- MCP result is required for a governed workflow but is unavailable, partial, stale, or inconsistent.

Fail-closed handling MUST preserve the original request, response where available, error details, scope context, evidence references, policy context, routing reason, and audit references.

## Audit Requirements

Governed MCP use MUST audit:

- MCP request and response identifiers.
- MCP server identity, version, owner, and environment.
- MCP tool identity, version, category, and authorized operation.
- Source system, destination system, output destination, connector ID, connector version, collection rule, parser ID, parser version, schema version, parser_or_transformation_version, data classification, sensitivity label, allowed use, retention policy, policy context, routing, and downstream consumption where MCP-mediated tool use, parsing, normalization, enrichment, retrieval, indexing, publication, reporting, approval routing, or downstream use occurs.
- MCP client identity and authenticated caller context.
- Agent identity and agent session or run identifier where an agent requested or consumed the result.
- Tenant, customer, case, workflow, workspace, subscription/account, source, and destination context.
- Evidence object identifiers and evidence tenant/customer attribution where evidence is collected, retrieved, transformed, summarized, or referenced.
- `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced MCP output, agent output, routing, reporting, approval packages, or downstream use.
- Schema version, parser version, normalization mapping, enrichment source, retrieval source, and freshness where applicable.
- Policy context, PDP decision reference, PEP enforcement reference, approval record, audit reference, and correlation identifiers where applicable.
- Human review routing, customer approval routing, correction, quarantine, retry, exception, or break-glass events.
- Downstream workflow, judge, report, case, or customer-facing use of MCP output where applicable.

Audit records MUST support reconstruction of which MCP server and tool were used, under which identity and scope, against which data source, producing which result, and how that result was consumed downstream.

## Operational Anti-Patterns

The following patterns violate this MCP security model:

- Treating MCP tool availability as authorization to use the tool.
- Allowing agents to directly select and execute MCP tools without governed workflow mediation.
- Allowing MCP tools to bypass PEP/PDP where policy-gated access, release, execution, or routing is required.
- Treating MCP tool success as evidence completeness, incident truth, approval, or forensic validation.
- Exposing unmanaged credentials, delegated tokens, service principals, managed identities, or scoped grants to prompts or uncontrolled agent context.
- Using MCP tools across tenants, customers, cases, workspaces, subscriptions/accounts, evidence sets, or memory scopes without explicit authorization.
- Using RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context outside approved `knowledge_store_or_memory_scope`.
- Reusing retrieved context without validating freshness, retention, tenant, customer, case, evidence, workspace, and reuse boundaries.
- Allowing MCP output to imply containment, remediation, eradication, recovery, access change, closure, customer notification, legal determination, or approval.
- Allowing Entra Agent ID, agent registry, identity governance, or lifecycle controls to be treated as operational SOC agents.
- Failing open when MCP registration, schema, identity, policy, evidence attribution, retrieval boundary, or audit context is missing.

## Acceptance Criteria

This file is acceptable when:

- MCP servers, MCP clients, and MCP tools are treated as mediated access surfaces.
- MCP responsibilities remain separate from PDP, PEP, Agent Judge, human review, customer approval, evidence authority, and forensic authority responsibilities.
- MCP tools do not produce `ALLOW`, `DENY`, or `REQUIRE_APPROVAL` decisions unless explicitly implemented and governed as PDP functions.
- Tenant identity, customer identity, case scope, workspace scope, subscription/account scope, evidence attribution, retrieval scope, and output destination are preserved where applicable.
- `knowledge_store_or_memory_scope` is required when RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context is exposed or consumed through MCP.
- `knowledge_memory_scope_result` is recorded where retrieval or memory scope is evaluated.
- MCP outputs preserve evidence traceability and do not become final truth sources.
- Private/local MCP use remains subject to evidence validation, human review, auditability, and workflow-specific approval requirements.
- Fail-closed handling exists for missing, ambiguous, unauthorized, stale, cross-tenant, cross-customer, cross-case, retention-inconsistent, unauditable, or out-of-scope MCP context.
- Audit records can reconstruct MCP identity, tool use, input scope, output references, policy context, routing, and downstream use.
- MCP audit replay can reconstruct source system, destination system, output destination, connector, collection rule, parser, schema version, parser_or_transformation_version, classification, sensitivity label, allowed use, retention, policy context, routing, and downstream consumption.
