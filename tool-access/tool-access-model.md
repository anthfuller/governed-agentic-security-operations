# Tool Permissioning

## Purpose

This file defines tool permissioning requirements for the `data-ingestion/` layer of the Governed Agentic MSSP / MDR / DFIR Security Operations Architecture repo.

Tool permissioning controls which data-ingestion tools, connectors, MCP-exposed tools, parsers, enrichment services, retrieval interfaces, evidence-store tools, case-store tools, and routing tools may be used, under which identity, against which source and destination, for which tenant, customer, case, evidence, workflow, and downstream purpose.

Tool permissioning does not authorize itself. It defines the permission context and required boundaries that must be evaluated by the governed workflow, PEP/PDP path, tool gateway, MCP gateway, connector gateway, or other approved mediation layer.

## Scope

This file applies to permissioning for:

- Data-ingestion connectors and collection tools.
- MCP servers, MCP clients, and MCP-exposed tools used for ingestion or retrieval.
- Parser, schema-validation, normalization, enrichment, transformation, summarization, indexing, publication, and routing tools.
- Evidence-store, case-store, ticketing, workflow-update, and report-store tools.
- Knowledge-store, vector-index, RAG, shared-memory, customer-context, case-memory, evidence-retrieval, and retrieved-context tools.
- Private/local LLM-assisted DFIR tools that parse, extract, summarize, retrieve, or route evidence.
- Tool use that influences agent workflows, Agent Judge findings, human review, customer-facing wording, approval packages, governance evidence, policy-enforcement context, or downstream operational use.

This file does not define the full PDP contract, PEP implementation, tool registry lifecycle, evidence repository, approval workflow, or Agent Judge evaluation contract. Those controls belong in the appropriate repo areas.

## Non-Goals

Tool permissioning MUST NOT be used to:

- Treat a tool registration record as authorization to execute any exposed operation.
- Treat a tool permission record as a PDP decision unless it is produced by a governed PDP.
- Treat a successful permission check as customer release approval, human approval, incident truth, evidence completeness, or forensic validation.
- Allow agents to self-authorize tool access.
- Allow tools to bypass PEP/PDP, workflow mediation, human review, customer approval, evidence handling, or audit controls.
- Treat retrieved context, vector search results, RAG grounding, shared memory, or case memory as complete, current, authorized, or reusable without scope validation.
- Treat private/local execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## Permissioning Principles

| Principle | Requirement |
|---|---|
| Default deny | Tool use MUST be denied unless tool identity, operation, scope, policy context, and audit requirements are satisfied. |
| Least privilege | Tool permissions MUST grant only the minimum source, destination, operation, tenant, customer, case, evidence, workspace, and retention scope required. |
| Operation-specific access | Read, collect, retrieve, parse, enrich, normalize, summarize, index, publish, route, export, update, and release operations MUST be permissioned separately where risk differs. |
| Tenant and customer separation | `tenant_id` and `customer_id` MUST remain separate for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows. |
| Source and destination control | Permissioning MUST preserve both source system and destination system context where tool output is routed, written, exported, indexed, published, released, or downstream-consumed. |
| Evidence boundary control | Tool permissions MUST preserve evidence object identifiers and evidence tenant/customer attribution when evidence is collected, retrieved, parsed, transformed, summarized, or referenced. |
| Retrieval boundary control | Tool permissions MUST preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where retrieval or memory affects tool output or downstream use. |
| Auditable authorization path | Permission checks, policy references, approval references, mediation paths, and downstream consumption MUST be auditable. |

## Permission Boundary Model

Tool permissioning MUST evaluate at least these boundaries when applicable:

| Boundary | Required Handling |
|---|---|
| Tool identity | Tool ID, version, owner, category, allowed operations, and prohibited operations MUST be known before governed use. |
| Requesting identity | User, workload, managed identity, service principal, agent, workflow, or MCP client identity MUST be authenticated and authorized for the requested scope. |
| Source system | Source system, connector, API, evidence store, case store, knowledge store, vector index, or repository MUST be authorized for the workflow and customer context. |
| Destination system | Destination system, case store, ticketing system, evidence store, knowledge store, vector index, report store, workflow, API, customer portal, or downstream service MUST be authorized before routing or publication. |
| Tenant and customer | Tool use MUST remain within approved tenant and customer scope. |
| Case and workflow | Tool use MUST remain bound to approved case, incident, workflow, and workflow-stage context where applicable. |
| Evidence | Tool use MUST preserve evidence object identifiers, tenant/customer attribution, provenance, and transformation history. |
| Retrieval and memory | Tool use MUST remain within approved knowledge store, vector index, customer context, case memory, evidence retrieval, retention, freshness, and reuse boundaries. |
| Classification and sensitivity | Data classification, sensitivity label, allowed use, retention, legal hold, and customer handling requirements MUST be preserved. |
| Policy and approval | Policy context and approval context MUST be available where access, release, evidence handling, or downstream use depends on them. |

## Required Tool Permission Record

Governed data-ingestion tool use MUST have a structured permission record before the result is consumed downstream.

| Field | Requirement | Purpose |
|---|---|---|
| `tool_permission_id` | MUST | Unique identifier for the tool permission record. |
| `tool_id` | MUST | Identifies the tool being permissioned. |
| `tool_name` | MUST | Human-readable tool name. |
| `tool_version` | MUST for governed workflows | Supports replay, regression review, and audit reconstruction. |
| `tool_owner` | MUST for governed workflows | Identifies accountable owner for tool operation, review, and remediation. |
| `tool_category` | MUST | Identifies connector, parser, enrichment, retrieval, evidence-store, case-store, workflow, or routing tool type. |
| `requested_operation` | MUST | Identifies the requested tool operation. |
| `authorized_operations` | MUST | Defines operations allowed for the current identity, workflow, and scope. |
| `prohibited_operations` | MUST where sensitive misuse is possible | Defines operations the tool MUST NOT perform. |
| `requesting_identity` | MUST | Identifies the authenticated workload, user, service, agent, MCP client, or workflow identity. |
| `agent_id` | MUST when an agent requested or influenced tool use | Identifies the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent requested or influenced tool use | Supports replay and run-level traceability. |
| `workflow_id` | MUST for governed workflows | Links permissioning to the governed workflow. |
| `workflow_stage` | MUST when routing, review, approval, or downstream handling depends on workflow stage | Preserves stage-specific permission context. |
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
| `data_classification` | MUST when tool input, output, evidence, retrieved context, or transformed data has sensitivity, legal, customer, privacy, forensic, or regulated handling requirements | Preserves data-handling and release-control context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity or handling label context for tool input, output, evidence, or retrieved context. |
| `allowed_use` | MUST when tool output is constrained to specific workflow, case, customer, legal, governance, evidence-handling, or reporting purposes | Defines permitted downstream use of the tool result. |
| `retention_policy_id` | MUST when retention affects accessed data, tool output, evidence, or retrieved context | Preserves retention and disposal boundary. |
| `policy_context_id` | MUST when policy affects tool access, routing, release readiness, evidence handling, approval, retention, or fail-closed behavior | Links tool use to applicable policy context. |
| `approval_record_id` | MUST when tool use depends on formal approval | Links the tool call to a scoped approval record. |
| `audit_reference_id` | MUST when tool output is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, case, policy, approval, audit, evidence, and judge records. |

## Permission Evaluation Outcomes

Permission evaluation outcomes MUST be structured when tool permissioning is evaluated.

| Outcome | Meaning |
|---|---|
| `TOOL_PERMISSION_ALLOWED_BY_POLICY` | Tool use may proceed only within the scoped policy, workflow, identity, operation, destination, and audit context. |
| `TOOL_PERMISSION_REQUIRES_APPROVAL` | Tool use requires formal approval before proceeding. This is not a PDP `REQUIRE_APPROVAL` decision unless produced by the PDP. |
| `TOOL_PERMISSION_REQUIRES_HUMAN_REVIEW` | Tool use requires human review before downstream reliance. |
| `TOOL_PERMISSION_DENIED` | Tool use must not proceed. |
| `TOOL_PERMISSION_FAIL_CLOSED` | Missing, ambiguous, unauthorized, stale, cross-boundary, retention-inconsistent, or unauditable context requires fail-closed handling. |
| `TOOL_PERMISSION_OUT_OF_SCOPE` | The requested operation is outside registered or authorized tool scope. |

Permission outcomes are handling signals unless produced by a governed PDP. They MUST NOT be represented as authorization decisions outside the PDP decision contract.

## Permissioning by Operation Type

| Operation Type | Permission Requirement |
|---|---|
| Read or collect | MUST validate source system, connector identity, tenant, customer, workspace, account, case, data classification, allowed use, and retention scope. |
| Retrieve from knowledge or memory | MUST validate `knowledge_store_or_memory_scope`, freshness, retention, reuse, tenant, customer, case, evidence, and workspace scope. |
| Parse, transform, normalize, summarize, or enrich | MUST validate parser, schema, transformation, enrichment, source, evidence, classification, and downstream-use context. |
| Index or publish | MUST validate destination system, output destination, knowledge-store/vector-index scope, retention, customer boundary, and allowed use. |
| Write or update | MUST validate destination system, case/workflow scope, approval context where required, and audit context. |
| Export or release | MUST validate destination, data classification, sensitivity label, customer release path, approval context, and evidence handling. |
| Case or ticket update | MUST validate case, workflow, customer, tenant, severity/closure/escalation authority, and downstream consumption. |
| Evidence handling | MUST validate evidence object identifiers, attribution metadata, provenance, chain-of-custody context, allowed use, and retention scope. |

## PEP/PDP Handoff Boundary

Tool permissioning MUST preserve separation between tools, PEP, PDP, Agent Judges, human review, and customer approval.

| Component | Responsibility |
|---|---|
| Tool permissioning record | Captures requested operation, identity, source, destination, scope, policy context, approval context, and audit context. |
| Data-ingestion tool | Performs a scoped operation only when permitted by workflow, identity, policy, and scope controls. |
| Agent | May request or consume tool output only through governed workflow mediation. |
| Agent Judge | May evaluate output quality, evidence support, tenant boundary, HITL compliance, or retrieval risk as assurance only. |
| PDP | Produces governed authorization decisions according to the policy contract. |
| PEP | Enforces PDP decisions and obligations at the workflow, tool, or execution boundary. |
| Human Reviewer | Validates high-impact output, scope, evidence support, and unresolved risk. |
| Customer Approval Path | Handles customer-side approval where required for release, containment, remediation, access, or reporting. |
| Audit System | Records permission checks, tool requests, decision context, result, routing, and downstream use. |

A tool permissioning record MUST NOT be treated as the PDP or PEP unless explicitly produced and enforced through those governed components.

## Human Review and Approval Boundaries

Human review and approval MUST remain separate from tool permissioning.

Human review MAY validate scope, evidence support, output quality, retrieval boundaries, or risk before downstream use.

Formal approval MAY authorize sensitive release, containment, remediation, access change, evidence release, or customer-facing communication when required by policy.

A tool permission check MUST NOT be treated as human review, formal approval, customer approval, or authorization to execute a sensitive action unless the required governed path provides that authorization separately.

## Evidence and Retrieval Permissioning

Tool permissioning MUST validate evidence and retrieval boundaries before the result is consumed downstream.

Permissioning MUST verify, where applicable:

- Evidence object identifiers.
- Evidence tenant and customer attribution.
- Evidence source system and collection metadata.
- Case and workflow association.
- Chain-of-custody references where applicable.
- Knowledge store or memory scope.
- Retrieval source, retrieval timestamp, query reference, retrieved context reference, index identifier, vector index identifier, or store identifier.
- Knowledge memory scope result where evaluated.
- Retention policy and allowed-use constraints.
- Downstream workflow, report, case, judge, or approval package consuming the result.

Tool permissioning MUST NOT substitute for the evidence repository, chain-of-custody record, examiner validation, or original evidence object.

## Private/Local LLM-Assisted DFIR Permissioning

Private/local LLM-assisted DFIR tool use MUST satisfy these permissioning requirements:

- Local execution MUST be treated as an execution and evidence-handling context, not proof of correctness.
- Local tools MUST remain bound to approved evidence stores, case scope, tenant scope, customer scope, and examiner workflow.
- RAG, vector search, shared memory, customer context, case memory, evidence retrieval, and retrieved context MUST remain within approved `knowledge_store_or_memory_scope`.
- Extracted artifacts, parsed outputs, summaries, and report drafts MUST preserve evidence references.
- Customer-facing DFIR conclusions MUST require evidence validation, examiner review, auditability, and the appropriate approval path.

## Fail-Closed Conditions

The governed workflow, PEP, orchestration layer, MCP gateway, connector gateway, or tool mediation layer MUST fail closed, quarantine, or route to controlled review when:

- Tool permissioning is missing, expired, revoked, inconsistent, or out of scope for the requested operation.
- Requested operation is not listed in authorized operations or is listed in prohibited operations.
- Required tenant, customer, case, workflow, workspace, subscription/account, source, evidence, destination, or approval context is missing or ambiguous.
- Evidence tenant or customer attribution is missing or inconsistent for evidence used in governed workflows.
- `knowledge_store_or_memory_scope` is missing, ambiguous, unauthorized, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent where retrieval or memory influences tool output, agent output, evidence interpretation, routing, customer-facing wording, approval packages, or downstream use.
- `knowledge_memory_scope_result` indicates retrieval or memory scope did not remain within approved boundaries.
- Required source system, destination system, output destination, connector, collection rule, parser, schema, parser/transformation version, data classification, sensitivity label, allowed use, retention, or policy-context metadata is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where governed tool use, parsing, normalization, enrichment, retrieval, routing, indexing, publication, reporting, approval routing, or downstream use depends on it.
- Tool request or response schema validation fails.
- Tool identity, requesting identity, credential, token audience, managed identity, service principal, delegated permission, scoped grant, or role assignment is out of scope.
- Tool output attempts to modify case, evidence, workflow, approval, routing, or customer-facing records outside approved scope.
- Tool output attempts to imply approval, execution, containment success, closure, legal determination, forensic proof, or customer notification without governed workflow context.
- Human review or approval is required but missing, expired, revoked, incomplete, or out of scope.
- Audit logging fails where audit is mandatory.
- Tool result is required for a governed workflow but is unavailable, partial, stale, or inconsistent.

Fail-closed handling MUST preserve the original request, permission result, response where available, error details, scope context, evidence references, policy context, approval context, routing reason, and audit references.

## Audit Requirements

Governed tool permissioning MUST audit:

- Tool permission, request, and result identifiers.
- Tool identity, version, owner, category, and requested operation.
- Source system, destination system, output destination, connector ID, connector version, collection rule, parser ID, parser version, schema version, parser_or_transformation_version, data classification, sensitivity label, allowed use, retention policy, policy context, routing, and downstream consumption where governed tool use, parsing, normalization, enrichment, retrieval, routing, indexing, publication, reporting, approval routing, or downstream use occurs.
- Requesting identity, agent identity, and session or run identifier where applicable.
- Tenant, customer, case, workflow, workspace, subscription/account, source, and destination context.
- Evidence object identifiers and evidence tenant/customer attribution where evidence is collected, retrieved, transformed, summarized, or referenced.
- `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context influenced tool output, agent output, routing, reporting, approval packages, or downstream use.
- Policy context, PDP decision reference, PEP enforcement reference, approval record, audit reference, and correlation identifiers where applicable.
- Human review routing, customer approval routing, correction, quarantine, retry, exception, or break-glass events.
- Downstream workflow, judge, report, case, or customer-facing use of tool output where applicable.

Audit records MUST support reconstruction of which tool was permissioned, under which identity and scope, against which source and destination, with which policy context, producing which result, and how that result was consumed downstream.

## Operational Anti-Patterns

The following patterns violate this tool permissioning model:

- Treating tool registration as permission to execute every exposed operation.
- Treating a permission record as a PDP decision outside the governed PDP decision contract.
- Allowing an agent to self-authorize data-ingestion tool use.
- Allowing tools to access tenants, customers, cases, workspaces, subscriptions/accounts, evidence sets, destinations, or memory scopes without explicit permission.
- Using RAG, vector search, shared memory, customer context, case memory, knowledge retrieval, evidence retrieval, or retrieved context outside approved `knowledge_store_or_memory_scope`.
- Reusing retrieved context without validating freshness, retention, tenant, customer, case, evidence, workspace, and reuse boundaries.
- Allowing tool permissioning to imply containment, remediation, eradication, recovery, access change, closure, customer notification, legal determination, or approval.
- Allowing tool-generated evidence summaries to replace original evidence, examiner validation, or chain-of-custody records.
- Allowing Entra Agent ID, agent registry, identity governance, or lifecycle controls to be treated as operational SOC agents.
- Failing open when permission, schema, identity, policy, evidence attribution, retrieval boundary, approval context, or audit context is missing.

## Acceptance Criteria

This file is acceptable when:

- Tool permissioning uses explicit requested operation, identity, source, destination, tenant, customer, case, evidence, retention, policy, approval, and audit context.
- Tool permissioning remains separate from PDP authorization, PEP enforcement, Agent Judge assurance, human review, customer approval, tool execution, evidence authority, and forensic certification.
- Tool permissioning preserves tenant identity and customer identity separately for MSSP, MDR, DFIR, customer-scoped, customer-facing, and multi-customer workflows.
- Tool permissioning preserves source system, destination system, output destination, connector, collection rule, parser, schema version, parser_or_transformation_version, classification, sensitivity label, allowed use, retention, policy context, routing, and downstream consumption where required for replay and audit.
- Tool permissioning preserves evidence object identifiers and evidence tenant/customer attribution when evidence is involved.
- Tool permissioning preserves `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` when retrieval or memory affects tool output or downstream use.
- Tool permissioning does not allow agents or tools to self-authorize governed access.
- Fail-closed handling exists when permissioning, identity, scope, source, destination, evidence, retrieval, policy, approval, or audit metadata is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope.
- Audit replay can reconstruct the permissioned tool, requested operation, requesting identity, source system, destination system, output destination, connector, collection rule, parser, schema version, parser_or_transformation_version, classification, sensitivity label, allowed use, retention, policy context, routing, and downstream consumption.
