# Tool Access

## Purpose

This directory defines the governance model for tool access in governed agentic security operations.

It covers how agents, orchestrators, MCP clients, workflows, and human-reviewed processes request, mediate, approve, execute, deny, and audit tool use across Managed SOC / MSSP, MDR, SOC, cloud incident response, detection engineering, threat hunting, and private/local LLM-assisted DFIR workflows.

Tools include connectors, APIs, SIEM and XDR queries, SOAR actions, cloud APIs, SaaS APIs, ticketing systems, case stores, evidence stores, knowledge stores, vector indexes, local forensic utilities, workflow-update mechanisms, report stores, MCP servers, and MCP-exposed tools.

Tool access is a controlled execution boundary. Tool registration, tool availability, MCP exposure, successful execution, or low-risk classification does not authorize tool use.

## Scope

This directory applies to tool access used by governed workflows, including:

- read-only telemetry, case, ticket, asset, identity, cloud, SaaS, and evidence retrieval;
- enrichment, parsing, normalization, summarization, indexing, routing, and report-drafting tools;
- case, ticket, queue, workflow, report, and notification update tools;
- evidence-aware DFIR parsing, extraction, timeline, memory, and local analysis tools;
- containment, isolation, account, permission, firewall, cloud-control, and other tenant-impacting tools;
- knowledge-store, vector-search, RAG, shared-memory, customer-context, case-memory, and retrieved-context tools;
- MCP servers, MCP clients, and MCP-exposed tool interfaces;
- tools whose output may influence investigation, triage, severity, escalation, approval, containment, remediation, customer communication, or audit records.

This directory does not define production adapter code, vendor configuration, runtime credentials, infrastructure deployment, customer-specific authority, legal sufficiency, evidence repository design, or the complete PDP contract. Those responsibilities belong in implementation systems and the appropriate governance directories.

## Core Principles

- Agents may request tool use only through governed workflow mediation.
- Tool availability is not authorization.
- Tool registration is not authorization.
- Tool risk classification is not authorization.
- MCP exposure is not authorization.
- Successful tool execution does not prove that the output is correct, complete, approved, or safe for downstream use.
- Policy Decision Point (PDP), Policy Enforcement Point (PEP), human review, formal approval, Agent Judge assurance, and tool execution remain separate responsibilities.
- Tools must run with least privilege and explicit operation scope.
- Tool access must preserve tenant, customer, case, workflow, evidence, source, destination, data-classification, retention, and output-destination context where applicable.
- Credentials, tokens, keys, service principals, managed identities, delegated grants, and scoped secrets must not be exposed to prompts, agent memory, uncontrolled logs, or uncontrolled tool output.
- Tool results must be treated as untrusted input until schema, scope, policy, evidence, retrieval, and output-destination checks are satisfied.
- Sensitive actions, evidence-affecting workflows, customer-facing releases, and tenant-impacting operations must fail closed when required context, approval, policy, or audit coverage is missing.

## Directory Contents

| File | Purpose |
|---|---|
| [`tool-registry.md`](tool-registry.md) | Defines required registration metadata for governed tools, including owner, version, allowed operations, prohibited operations, data sources, destinations, scope, and audit expectations. |
| [`tool-permissioning.md`](tool-permissioning.md) | Defines how tool requests are evaluated against identity, tenant, customer, case, workflow, evidence, policy, approval, and least-privilege constraints. |
| [`tool-risk-categories.md`](tool-risk-categories.md) | Defines tool risk categories and required handling for read, ingestion, evidence, retrieval, customer-scoped, privileged, external-sharing, and private/local DFIR tool use. |
| [`approved-tool-patterns.md`](approved-tool-patterns.md) | Defines approved patterns for scoped read, retrieval, enrichment, summarization, case update, report drafting, and policy-mediated execution. |
| [`restricted-tool-patterns.md`](restricted-tool-patterns.md) | Defines restricted or prohibited tool-use patterns that require denial, escalation, approval, quarantine, or fail-closed handling. |
| [`tool-call-logging.md`](tool-call-logging.md) | Defines logging requirements for tool requests, permission checks, policy decisions, approvals, execution results, errors, outputs, and downstream consumption. |
| [`security-model.md`](security-model.md) | Defines the MCP and tool-access security model for mediated tool exposure, request validation, response validation, auditability, and fail-closed behavior. |

## Tool Access Model

Governed tool access follows this model:

1. A workflow or agent requests a tool operation.
2. The request is bound to identity, tenant, customer, case, workflow, source, destination, evidence, and output context.
3. The tool registry confirms the tool identity, owner, version, allowed operations, prohibited operations, and approved scope.
4. The tool risk category determines required handling, review, approval, policy checks, and audit expectations.
5. The PDP evaluates whether the requested operation is allowed, denied, requires approval, or must fail closed.
6. The PEP enforces the PDP decision and obligations before the tool runs or output is released.
7. Required human review, formal approval, or customer approval occurs through separate approval paths.
8. The tool executes only within the approved operation and scope.
9. Tool output is validated before downstream use.
10. Audit records preserve the request, decision, approval, execution result, output reference, exception, and final state.

## Required Tool Access Context

A governed tool request should preserve enough context for authorization, enforcement, review, replay, and dispute handling.

| Context | Required Purpose |
|---|---|
| Tool identity | Identifies the registered tool, version, owner, category, and allowed operations. |
| Requesting identity | Identifies the user, service, workflow, agent, MCP client, or workload requesting access. |
| Agent/run context | Links the request to the agent, session, run, prompt package, model route, or workflow stage where applicable. |
| Tenant and customer context | Preserves tenant and customer boundaries separately for MSSP, MDR, DFIR, and multi-customer workflows. |
| Case and workflow context | Links the request to an incident, investigation, ticket, approval package, report, or DFIR matter. |
| Source and destination context | Identifies where data is read from, written to, routed, indexed, published, or consumed. |
| Evidence context | Preserves evidence object identifiers, evidence attribution, provenance, and chain-of-custody references where applicable. |
| Retrieval and memory context | Defines approved knowledge store, vector index, case memory, shared memory, customer context, retention, freshness, and reuse boundaries. |
| Policy and approval context | Links the request to policy context, PDP decision, PEP enforcement, approval record, and validity window. |
| Data-handling context | Preserves classification, sensitivity label, allowed use, retention, legal/privacy constraints, and release boundaries. |
| Audit context | Preserves event, correlation, tool execution, exception, output, and replay references. |

## Tool Risk Handling

Tool risk must be evaluated by operation and context, not only by tool name.

| Risk Area | Handling Requirement |
|---|---|
| Read-only internal access | Log identity, operation, source, scope, and audit reference. |
| Ingestion and enrichment | Preserve connector, parser, schema, transformation, source, destination, classification, and replay metadata. |
| Evidence-affecting access | Preserve evidence references, attribution, provenance, review routing, and chain-of-custody context where applicable. |
| Customer-scoped access | Preserve separate tenant and customer identity, case/workflow context, and output-destination controls. |
| Cross-tenant or multi-customer access | Require explicit authorization, policy gating, boundary validation, audit, and fail-closed behavior. |
| Retrieval or memory access | Validate knowledge-store, vector-index, memory, freshness, retention, tenant, customer, case, evidence, and reuse boundaries. |
| Customer-facing output or release | Require output-destination validation, evidence support, review or approval path, and audit. |
| Action-influencing output | Preserve policy context, review routing, downstream consumption, and PEP/PDP handoff where applicable. |
| Privileged access | Validate identity, token audience, role scope, least privilege, secret isolation, and audit coverage. |
| External sharing | Validate destination authorization, data classification, sensitivity label, allowed use, retention, and customer/legal/privacy constraints. |
| Private/local DFIR tooling | Preserve evidence links, examiner review context, local execution limits, and release controls. |

## Approved Tool Access Patterns

Approved patterns are scoped, mediated, and auditable. Examples include:

- retrieving telemetry within an approved tenant, customer, workspace, and case scope;
- enriching an alert with approved asset, identity, threat-intelligence, or cloud-context data;
- querying an evidence store by evidence reference without copying raw evidence into uncontrolled output;
- drafting a case summary that remains subject to evidence validation and analyst review;
- updating case metadata only after policy and workflow controls confirm the allowed operation;
- preparing a containment recommendation without executing containment;
- executing a sensitive action only after PDP authorization, PEP enforcement, required approval, scoped credentials, and audit readiness are confirmed;
- using private/local DFIR tools within approved case, evidence, customer, and examiner workflow boundaries.

## Restricted Tool Access Patterns

Restricted patterns must be denied, escalated, routed for approval, quarantined, or failed closed according to policy.

Restricted patterns include:

- agents directly selecting and executing tools outside governed workflow mediation;
- treating tool registration, tool availability, MCP exposure, or low-risk classification as authorization;
- using tools across tenants, customers, cases, workspaces, subscriptions, accounts, evidence sets, or memory scopes without explicit authorization;
- exposing credentials, tokens, service principals, managed identities, delegated grants, or scoped secrets to prompts or uncontrolled agent context;
- allowing tool output to imply approval, containment success, remediation completion, legal conclusion, forensic proof, customer notification, or case closure;
- modifying cases, evidence, workflow state, approvals, routing, reports, or customer communications outside approved scope;
- using retrieval, vector search, shared memory, customer context, case memory, or prior-case context outside approved boundaries;
- releasing customer-facing output without evidence support, review, approval, and release records where required;
- allowing tools to retry denied, approval-required, or failed-closed actions automatically;
- failing open when policy, approval, identity, scope, evidence, retrieval, schema, credential, destination, or audit context is missing.

## MCP-Mediated Tool Access

MCP servers, MCP clients, and MCP-exposed tools are mediated access surfaces.

MCP may expose tools, resources, prompts, and context interfaces, but MCP does not replace policy enforcement, identity governance, human review, customer approval, evidence validation, or audit accountability.

Governed MCP use must preserve:

- MCP server identity, version, owner, and environment;
- MCP client identity and authenticated caller context;
- MCP tool identity, version, category, allowed operations, and prohibited operations;
- tenant, customer, case, workflow, workspace, subscription, account, evidence, retrieval, source, and destination scope;
- request and response identifiers;
- schema, parser, transformation, enrichment, and retrieval metadata where applicable;
- policy decision, PEP enforcement, approval, audit, and correlation references;
- output destination, downstream use, limitations, and fail-closed state where applicable.

MCP responses must be treated as untrusted input until schema, scope, retrieval, evidence, policy, and output-destination checks are satisfied.

## Policy, Approval, and Enforcement Boundary

Tool access must preserve separation of responsibilities.

| Component | Responsibility |
|---|---|
| Agent | May request tool use and consume governed tool output through approved workflow mediation. |
| Tool Registry | Identifies registered tools, owners, versions, operations, prohibited operations, and scope. |
| Risk Classification | Determines required handling and review expectations; it does not authorize execution. |
| PDP | Produces governed authorization decisions according to the policy contract. |
| PEP | Enforces PDP decisions and obligations before tool execution or output release. |
| Agent Judge | Evaluates output quality, evidence support, retrieval scope, or boundary handling as assurance only. |
| Human Reviewer | Reviews high-impact output, scope, evidence support, and unresolved risk. |
| Formal Approval Path | Authorizes sensitive action, release, evidence handling, access change, or customer communication where required. |
| Tool Execution Layer | Executes only approved operations within scoped credentials and approved boundaries. |
| Audit System | Records request, policy, approval, enforcement, execution, output, exception, and downstream use. |

## Logging and Replay Requirements

Governed tool access must be replayable.

Tool-access audit records should capture:

- tool request, permission, policy decision, approval, execution, response, and downstream-use identifiers;
- tool identity, version, owner, category, risk category, and requested operation;
- requesting identity, agent identity, workflow, session, run, and correlation identifiers where applicable;
- tenant, customer, case, workspace, subscription, account, source, destination, and output-destination context;
- evidence object identifiers and evidence tenant/customer attribution where evidence is accessed or referenced;
- retrieval and memory scope where RAG, vector search, shared memory, customer context, case memory, evidence retrieval, or retrieved context is used;
- data classification, sensitivity label, allowed use, retention policy, and policy context;
- PDP decision, PEP enforcement, approval record, failure state, exception routing, and final outcome;
- tool output reference, limitations, validation result, and downstream workflow or report consumption.

Audit records should support reconstruction of which tool was requested, why it was allowed or denied, which scope applied, what executed, what result was produced, who or what consumed the result, and which final state was reached.

## Fail-Closed Conditions

Tool access must fail closed, quarantine, deny, or route to controlled review when:

- the tool is unregistered, expired, revoked, misconfigured, or inconsistent with the requested operation;
- the requested operation is not authorized or is listed as prohibited;
- identity, tenant, customer, case, workflow, source, destination, evidence, retrieval, memory, classification, retention, policy, approval, or audit context is missing or ambiguous;
- the request crosses tenant, customer, case, workspace, account, subscription, evidence, memory, retention, or reuse boundaries without explicit authorization;
- evidence attribution is missing, inconsistent, or outside the approved scope;
- retrieval or memory scope is missing, stale, unauthorized, cross-tenant, cross-customer, cross-case, or retention-inconsistent;
- tool request or response schema validation fails;
- credentials, token audience, role scope, delegated grants, service principals, managed identities, or scoped secrets are out of scope;
- tool output attempts to modify records outside approved scope;
- tool output attempts to imply approval, execution success, containment, remediation, legal conclusion, forensic proof, customer notification, or closure without governed workflow context;
- required human review, formal approval, or customer approval is missing, expired, revoked, incomplete, or out of scope;
- audit logging is unavailable where audit is mandatory;
- the tool result is unavailable, partial, stale, inconsistent, or unsafe for downstream use.

Fail-closed handling must preserve the original request, policy context, approval context, scope context, error details, output reference where available, routing reason, and audit reference.

## Relationship to Other Control Areas

Tool access depends on and produces records for other governance domains:

- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines PDP, PEP, decision, enforcement, approval-policy, and fail-closed expectations.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) defines human review, formal approval, customer approval, escalation, and review records.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, and cross-tenant boundary controls.
- [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) defines evidence references, evidence support, DFIR evidence handling, and evidence-aware audit replay.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines local/private LLM-assisted DFIR boundaries, evidence handling, review, and replay expectations.
- [`../data-ingestion/readme.md`](../data-ingestion/readme.md) defines source metadata, normalization, enrichment, ingestion failure handling, and ingestion replay.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines replayability, correlation, failure audit, and immutable audit expectations.
- [`../agent-governance/readme.md`](../agent-governance/readme.md) defines agent identity, lifecycle, ownership, monitoring, rollback, recall, and fleet governance.

## Acceptance Criteria

Tool access is acceptable when:

- all governed tools have registration records with owner, version, allowed operations, prohibited operations, scope, and audit expectations;
- tool access requests are mediated through governed workflows and do not rely on agent self-authorization;
- tool availability, MCP exposure, tool registration, successful execution, and low-risk classification are not treated as authorization;
- tenant, customer, case, workflow, evidence, source, destination, retrieval, memory, data-handling, and output-destination scope are preserved where applicable;
- risk classification remains separate from PDP authorization, PEP enforcement, Agent Judge assurance, human review, formal approval, customer approval, and tool execution;
- sensitive actions require PDP authorization, PEP enforcement, required approval, scoped credentials, and audit readiness before execution;
- MCP-mediated tool use is registered, scoped, validated, policy-mediated, and auditable;
- credentials and privileged identities are isolated from prompts, uncontrolled model context, and uncontrolled outputs;
- tool outputs are validated before they influence actions, approvals, reports, customer communications, or case closure;
- fail-closed handling exists for missing, ambiguous, unauthorized, stale, cross-tenant, cross-customer, cross-case, retention-inconsistent, unauditable, or out-of-scope context;
- audit replay can reconstruct tool request, risk category, policy decision, approval record, PEP enforcement, execution result, output reference, downstream use, exception path, and final state.
