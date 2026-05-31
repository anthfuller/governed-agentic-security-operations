# MDR Operating Model

## Purpose

This file defines the **Managed Detection and Response (MDR) operating model** for the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The MDR operating model describes how agentic assistance can support investigation, escalation, response recommendation, containment preparation, detection tuning support, and analyst workflow acceleration without granting agents autonomous response authority.

This file is an operating model, not a vendor-specific engineering design.

## Service Scope

The MDR service model supports detection, investigation, response support, and escalation for customer security operations.

| Area | In Scope |
|---|---|
| Investigation | Customer-scoped alert and incident investigation using approved telemetry, enrichment, identity, asset, and threat context. |
| Response recommendation | Drafting response options, containment recommendations, escalation rationale, and analyst decision support. |
| Containment preparation | Preparing approval packages for actions such as endpoint isolation, identity containment, indicator blocking, or cloud IAM containment. |
| Detection feedback | Recommending detection tuning, suppression review, enrichment improvements, and coverage gaps for analyst review. |
| Escalation | Routing to SOC / IR, Cloud IR, DFIR, or Private / Local LLM-assisted DFIR when the incident requires deeper response or evidence handling. |
| Reporting support | Drafting internal incident summaries and customer-facing report sections before review and release approval. |

## Out of Scope

| Area | Out-of-Scope Boundary |
|---|---|
| Autonomous containment | Agents must not directly isolate hosts, block indicators, disable accounts, reset credentials, quarantine files, or change policy without approved authority. |
| Unscoped investigation | Agents must not retrieve or correlate data outside authorized tenant, customer, case, incident, workflow, or evidence scope. |
| Final incident determination | Agent output must not be treated as a final incident conclusion without analyst review. |
| Customer notification | Agents may draft customer communications, but release requires approval and customer authorization where required. |
| DFIR findings | MDR workflows must not issue forensic findings unless escalated into DFIR with evidence and chain-of-custody controls. |
| Local LLM forensic analysis | Private / Local LLM-assisted DFIR applies only when evidence is analyzed in a local, isolated, or customer-controlled AI environment. |

## Operating Principles

| Principle | Required Behavior |
|---|---|
| Investigation scope | Every MDR workflow must be bound to tenant, customer, incident, workflow, and identity or asset scope where applicable. |
| Agent as assistant | Agents may investigate, summarize, recommend, and draft, but must not become the decision authority. |
| Policy before response | Response, containment, tool execution, output release, and workflow state changes must pass policy evaluation where required. |
| PEP at execution boundary | Enforcement must occur at the tool wrapper, workflow orchestrator, API gateway, retrieval layer, ticket connector, or output path. |
| Human approval for sensitive action | Sensitive, destructive, privileged, customer-impacting, or externally visible actions require approval before execution. |
| Customer authorization where required | Customer-impacting response actions must follow the customer’s authorization rules and service agreement. |
| Evidence-aware escalation | If evidence preservation, timeline reconstruction, or forensic conclusion is required, escalate to DFIR. |
| Audit and replay | MDR recommendations, decisions, approvals, tool calls, and outputs must be reconstructable. |
| Fail closed | Missing scope, missing policy, missing approval, or ambiguous context must stop, deny, or route for clarification. |

## MDR Workflow Classes

| Workflow Class | Agentic Assistance Allowed | Approval Required? | Notes |
|---|---|---|---|
| Alert investigation | Yes | Usually no for read-only investigation | Must remain customer and incident scoped. |
| Entity enrichment | Yes | Usually no if read-only and scoped | Retrieval and memory boundaries must be enforced. |
| Response recommendation | Yes | Yes before execution | Recommendation is not execution authority. |
| Endpoint isolation preparation | Yes | Yes | Requires approval and authorized response path. |
| Identity containment preparation | Yes | Yes | May require customer authorization. |
| Indicator blocking recommendation | Yes | Yes before enforcement | Blocking can disrupt business or create false positives. |
| Detection tuning draft | Yes | Review required before deployment | Drafting is allowed; deployment is controlled. |
| Customer summary draft | Yes | Yes before release | Customer-facing output requires review. |
| DFIR escalation | Yes | Yes when evidence handling begins | Hand off to DFIR operating model. |

## Roles and Responsibilities

| Role | Responsibility | Must Not Do |
|---|---|---|
| MDR Analyst | Validate agent recommendations, investigate scoped incidents, approve routine analyst actions within authority, and escalate high-risk workflows. | Execute sensitive response based only on agent output. |
| MDR Incident Lead | Own incident coordination, containment approval routing, customer escalation, and service-level decisioning. | Bypass customer authorization or policy requirements. |
| Agentic Workflow | Triage, enrich, correlate, summarize, draft recommendations, identify uncertainty, and prepare approval packages. | Execute containment, approve itself, publish externally, or access unrelated customer data. |
| PDP | Decide whether action is allowed, denied, restricted, approval-required, clarification-required, or escalation-required. | Act as the enforcement point. |
| PEP | Enforce decisions at tool, API, workflow, retrieval, memory, ticketing, and output boundaries. | Permit execution when policy, scope, approval, or authorization is missing. |
| Customer Approver | Authorize customer-impacting response actions where required. | Be bypassed when customer authority is required. |
| DFIR Lead | Own forensic evidence handling when the MDR case escalates into DFIR. | Treat MDR triage output as final forensic evidence without validation. |
| Audit / Assurance | Preserve traceability, evaluate decision quality, monitor enforcement, and support replay. | Depend on unstructured narrative without structured identifiers. |

## Agentic Assistance Boundaries

| Agent May | Agent Must Not |
|---|---|
| Review customer-scoped incident context. | Retrieve another customer’s data. |
| Correlate alerts, entities, identities, assets, and threat context. | Correlate across tenants unless explicitly authorized. |
| Draft risk and response recommendations. | Execute containment or remediation. |
| Prepare approval packages for sensitive actions. | Approve or reuse approvals. |
| Identify uncertainty and missing evidence. | Convert uncertainty into confirmed findings. |
| Suggest escalation to Cloud IR or DFIR. | Initiate evidence handling without DFIR scope. |
| Draft customer summaries. | Release customer-facing communications. |

## Policy and Enforcement Points

Service owners must map the PDP / PEP boundaries defined in this operating model to specific infrastructure components in their deployment guide, such as workflow orchestrators, tool wrappers, API gateways, retrieval gateways, ticket connectors, memory gateways, and output publishing controls.

| Boundary | PDP Decision Required When | PEP Enforcement Location |
|---|---|---|
| Retrieval | Context is retrieved from SIEM, XDR, EDR, cloud, identity, ticketing, RAG, memory, or case stores. | Retrieval layer, RAG gateway, or memory gateway. |
| Tool use | Agent or workflow requests a tool, API, connector, script, or automation action. | Tool wrapper, API gateway, or workflow orchestrator. |
| Response action | Workflow proposes containment, isolation, blocking, quarantine, credential reset, or policy change. | Response automation connector or tool PEP. |
| Detection tuning | Workflow proposes rule changes, suppression, allow-list, or detection deployment. | Detection engineering workflow or CI/CD gate. |
| Ticket or case update | Workflow writes to customer ticket, case record, or incident state. | Ticket connector or case management connector. |
| Customer-facing output | Summary, report, notification, or recommendation is released externally. | Output publishing layer. |
| Escalation | Workflow moves from MDR into Cloud IR, SOC / IR, DFIR, or Private / Local LLM-assisted DFIR. | Workflow orchestrator. |

## Human Approval Gates

| If This Occurs | Then Require |
|---|---|
| Recommendation includes endpoint isolation, blocking, quarantine, deletion, credential reset, account disablement, or policy change. | Human approval before execution; customer authorization where required. |
| Response action may disrupt customer operations. | Human approval and customer authorization assessment. |
| Agent proposes containment with medium or low confidence. | Human analyst review before action. |
| Customer-facing communication is drafted. | Review and release approval before publication. |
| Detection change affects production detections. | Detection owner or service lead approval before deployment. |
| Incident closure is proposed. | Human-controlled closure decision with audit-linked rationale. |
| Workflow requires evidence preservation or forensic conclusion. | Escalation to DFIR operating model. |
| Local/private forensic AI analysis is required. | Escalation to Private / Local LLM-assisted DFIR operating model. |
| Scope is ambiguous across customer, tenant, incident, identity, asset, or case. | Return for clarification or fail closed. |

## Customer Authorization Gates

| Customer Authorization Required When | Enforcement Requirement |
|---|---|
| Response action changes customer environment state. | Tool PEP must verify authorization and approved scope. |
| Action may disrupt endpoint, identity, cloud, network, SaaS, or business operations. | Workflow PEP must require authorization check before execution. |
| Customer notification is sent. | Output PEP must block release without authorization reference where required. |
| Customer-facing report is released. | Release workflow must include reviewer and authorization references where required. |
| Evidence, logs, or customer data are exported or transferred. | Data movement or evidence PEP must verify authorization. |
| Customer contract defines specific response authority. | Workflow must enforce contract-specific approval path. |

## Data Boundary Enforcement

| Data Boundary | Required Control |
|---|---|
| Tenant | Requests must carry `tenant_id`; missing or mismatched tenant fails closed. |
| Customer | Requests must carry `customer_id`; cross-customer retrieval is denied and audited. |
| Incident / Case | Incident and case identifiers must be present for incident-scoped workflows. |
| Asset / Identity | Response recommendations must identify affected asset or identity scope. |
| Knowledge / Memory | Retrieval must include `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where used. |
| Evidence | Evidence references are required when MDR escalates into evidence-sensitive DFIR work. |
| Output Destination | Output destination must be declared before write, release, ticket update, or report generation. |
| Classification | Data classification and sensitivity label must persist through workflow state. |

## Retrieval and Memory Rules

| If | Then |
|---|---|
| RAG is used for investigation. | Restrict retrieval to customer, incident, case, asset, and identity scope. |
| Case memory influences recommendation. | Validate memory scope and freshness before prompt assembly. |
| Shared knowledge is retrieved. | Confirm it is approved reference context and not another customer’s data. |
| Persistent memory write is requested. | Deny by default unless policy, owner, retention, and approval are present. |
| Retrieved context is stale or conflicting. | Flag uncertainty and route for analyst review. |
| Retrieved context crosses customer, tenant, or case boundary. | Deny, quarantine result, and emit audit event. |
| Retrieval supports customer-facing output. | Preserve source references and require release review. |

## Sensitive Action Handling

MDR workflows may recommend sensitive response actions, but they must not execute them without approval and enforcement.

An **authorized response path** means the response action is executed only through a documented, approved, and replayable workflow. For enterprise use, the response path should be represented as an **idempotent workflow** or **signed playbook** that defines the allowed action, required approvals, customer authorization requirements, PEP enforcement point, rollback or recovery expectation where applicable, and audit fields.

| Sensitive Action | MDR Agent Output Allowed | Execution Allowed? |
|---|---:|---:|
| Endpoint isolation | Recommendation and approval package | Only after approval and authorized response path. |
| Indicator blocking | Recommendation and approval package | Only after approval and authorized response path. |
| File quarantine | Recommendation and approval package | Only after approval and authorized response path. |
| Credential reset | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| Account disablement | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| OAuth grant removal | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| Detection rule deployment | Draft change only | Only through detection owner review and deployment gate. |
| Customer notification | Draft only | Only after release approval and customer authorization where required. |
| Evidence export | Not routine MDR action | Requires DFIR / data handling authorization. |
| Incident closure | Draft recommendation only | Human-controlled workflow decision required with audit-linked closure rationale. |

## Detection Tuning and Content Changes

| If This Occurs | Then Require |
|---|---|
| Agent proposes detection rule change. | Detection owner review before deployment. |
| Agent proposes suppression or allow-list. | Risk review and customer scope validation. |
| Change affects multiple customers. | Service lead approval and tenant impact review. |
| Change is based on uncertain context. | Require analyst validation and test evidence. |
| Change deploys through pipeline. | CI/CD gate, approval record, rollback path, and audit event. |
| Change affects customer-specific detection. | Customer scope and authorization check where required. |

## Escalation Paths

| Condition | Escalate To | Reason |
|---|---|---|
| Incident requires active response or containment coordination beyond MDR authority. | SOC / Incident Response or service lead | Incident command or operational authority required. |
| Cloud IAM compromise, OAuth abuse, cloud policy change, or cloud resource compromise. | Cloud IR | Cloud-specific investigation and response controls required. |
| Evidence preservation, timeline reconstruction, malware analysis, disk/memory analysis, or chain-of-custody required. | DFIR | Formal forensic workflow required. |
| Evidence cannot leave customer-controlled or isolated environment. | Private / Local LLM-assisted DFIR | Local/private forensic AI workflow required. |
| Customer-impacting action required. | Customer approver / service lead | Customer authorization or contractual approval may be required. |
| Policy exception required. | Governance approver / service owner | Exception must be explicitly approved and logged. |

## Audit and Replay Requirements

MDR workflows should emit or preserve:

- request identifier;
- correlation identifier;
- audit reference identifier — this **MUST** match the audit reference identifier used in the related `example-audit-event.json` structure so the request, decision, approval, enforcement, execution result, and final workflow state remain linked;
- tenant and customer identifiers;
- incident and case identifiers where applicable;
- asset, identity, or cloud resource identifiers where applicable;
- workflow identifier;
- agent identifier;
- requester identity;
- retrieved context references where used;
- recommendation or proposed action;
- policy decision;
- approval record where required;
- customer authorization reference where required;
- tool invocation record where applicable;
- execution result where action is authorized;
- output destination;
- final workflow state;
- deny, clarification, or escalation reason where applicable.

## Fail-Closed Rules

| Failure Condition | Required Behavior |
|---|---|
| Missing `tenant_id` or `customer_id` | Fail closed. |
| Incident scope missing for incident workflow | Return for clarification or fail closed. |
| Affected asset or identity scope missing for response recommendation | Return for clarification before action. |
| Customer context mismatch | Deny and audit. |
| Retrieval returns cross-customer context | Deny, quarantine result, and audit. |
| Policy unavailable | Fail closed. |
| Approval required but missing | Block action and route for approval. |
| Customer authorization required but missing | Block customer-impacting action. |
| Output destination missing or unauthorized | Block write or release. |
| Agent requests prohibited tool use | Deny and audit. |
| Evidence handling begins without DFIR scope | Escalate to DFIR or fail closed. |
| Detection change lacks owner approval | Block deployment. |

## Relationship to Examples

| Example | MDR Relevance |
|---|---|
| [`alert-triage-to-recommendation`](../examples/alert-triage-to-recommendation/) | Applies to MDR triage and recommendation-only workflow before response action. |
| [`cloud-iam-compromise`](../examples/cloud-iam-compromise/) | Primary MDR example for sensitive response requiring approval and customer authorization. |
| [`local-llm-forensic-timeline`](../examples/local-llm-forensic-timeline/) | Applies when MDR escalates into DFIR timeline work or local/private forensic analysis. |

## Relationship to Patterns

| Pattern | MDR Usage |
|---|---|
| [`governed-agentic-security-operations-pattern.md`](../patterns/governed-agentic-security-operations-pattern.md) | Baseline for scoped, policy-gated, auditable MDR workflows. |
| [`policy-enforced-tool-use-pattern.md`](../patterns/policy-enforced-tool-use-pattern.md) | Applies to tool, API, connector, response, ticket, and output write actions. |
| [`human-approved-sensitive-action-pattern.md`](../patterns/human-approved-sensitive-action-pattern.md) | Applies to containment, response actions, detection changes, customer-facing outputs, and incident closure. |
| [`tenant-safe-rag-memory-pattern.md`](../patterns/tenant-safe-rag-memory-pattern.md) | Applies to investigation context, RAG, case memory, customer memory, and retrieved evidence support. |
| [`private-local-llm-dfir-pattern.md`](../patterns/private-local-llm-dfir-pattern.md) | Applies only when MDR escalates into local/private forensic analysis. |

Service owners must map these pattern requirements to deployment-specific infrastructure controls, policies, tests, and runbooks before implementation.

## Acceptance Criteria

An MDR agentic operating workflow is acceptable when:

- every workflow is bound to tenant, customer, incident, and workflow scope;
- asset, identity, cloud resource, or evidence scope is present where applicable;
- agent output is treated as recommendation or draft support, not execution authority;
- policy is evaluated before tool use, response action, ticket write, detection deployment, escalation state change, or output release where required;
- PEP enforcement exists at the actual boundary;
- sensitive actions require human approval;
- customer-impacting actions require customer authorization where applicable;
- retrieval and memory are scoped and auditable where used;
- response actions execute only through authorized response paths;
- detection changes require owner review and deployment controls;
- evidence handling escalates to DFIR when required;
- customer-facing outputs are reviewed before release;
- denied or uncertain workflows fail closed or return for clarification;
- audit records support reconstruction.

## Non-Goals

This operating model does not:

- define a specific MDR product, SIEM, XDR, EDR, SOAR, cloud, or ticketing implementation;
- require every MDR workflow to be agentic;
- allow agents to perform autonomous containment or remediation;
- replace human analysts, incident leads, service owners, or customer authority;
- replace customer contracts or authorization requirements;
- replace Cloud IR or DFIR operating models;
- claim that AI recommendations are authoritative without review;
- permit final forensic conclusions without DFIR controls.

## Summary

The MDR operating model defines how agentic assistance can accelerate investigation, recommendation drafting, response preparation, and escalation while preserving customer boundaries, policy enforcement, human approval, customer authorization, and auditability.

The core principle is:

> MDR agents may investigate, correlate, summarize, recommend, and prepare approval packages, but they must not execute sensitive response actions, release customer-facing outputs, alter detections, or handle evidence outside governed scope.
