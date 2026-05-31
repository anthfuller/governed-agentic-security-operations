# MSSP Operating Model

## Purpose

This file defines the **Managed Security Service Provider (MSSP) operating model** for the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The MSSP operating model describes how agentic assistance can support multi-customer managed security operations without weakening tenant separation, customer boundaries, service accountability, policy enforcement, human oversight, or auditability.

This file is an operating model, not a vendor-specific engineering design.

## Service Scope

The MSSP service model supports managed security operations across multiple customers and tenants.

| Area | In Scope |
|---|---|
| Alert handling | Customer-scoped alert triage, enrichment, classification, routing, and recommendation drafting. |
| Service operations | Queue management, prioritization, escalation support, SLA tracking, and analyst workflow support. |
| Customer reporting | Internal report drafting, customer summary preparation, and recommendation support before release review. |
| Tool-assisted investigation | Read-only enrichment, customer-scoped lookup, ticket preparation, and workflow routing through policy-enforced tool access. |
| Handoff | Escalation to MDR, SOC / IR, Cloud IR, or DFIR when the event exceeds MSSP operating authority. |

## Out of Scope

| Area | Out-of-Scope Boundary |
|---|---|
| Autonomous response | Agents must not execute containment, isolation, blocking, deletion, quarantine, credential reset, or customer notification without approved authority. |
| Unscoped customer access | Agents must not retrieve or use data outside the authorized tenant, customer, case, incident, or workflow scope. |
| Final customer-facing release | Agents may draft summaries, but final customer-facing release requires defined review and approval. |
| DFIR conclusions | MSSP workflows must not produce final forensic conclusions unless formally escalated into DFIR with evidence handling controls. |
| Customer authorization substitution | Internal MSSP approval does not replace customer authorization where customer authority is required. |

## Operating Principles

| Principle | Required Behavior |
|---|---|
| Customer isolation | Every workflow must remain bound to the correct tenant and customer. |
| No implicit agent trust | Agent output is recommendation or draft support, not execution authority. |
| Policy before action | Tool use, ticket updates, report release, or escalation state changes must pass policy evaluation where required. |
| PEP enforcement | Enforcement must occur at the real boundary: tool wrapper, workflow orchestrator, retrieval layer, ticket connector, or output path. |
| Human accountability | Humans remain accountable for service decisions, customer-impacting actions, and final release. |
| Auditability | Requests, context, recommendations, decisions, approvals, and outputs must be reconstructable. |
| Fail closed | Missing scope, missing policy, missing approval, or ambiguous customer context must stop or route the workflow. |

## MSSP Workflow Classes

| Workflow Class | Agentic Assistance Allowed | Approval Required? | Notes |
|---|---|---|---|
| Read-only alert triage | Yes | Usually no, if policy allows | Must remain customer scoped and auditable. |
| Alert enrichment | Yes | Usually no, if read-only and scoped | Retrieval must not cross customer or case boundaries. |
| Internal recommendation drafting | Yes | No for internal-only output; yes before sensitive action | Recommendation must not become execution authority. |
| Ticket or case update | Conditional | Depends on customer impact and workflow rules | PEP must control write access. |
| Customer-facing summary draft | Yes | Yes before release | Drafting is allowed; release is controlled. |
| Containment recommendation | Yes | Yes before execution | Human approval and possibly customer authorization required. |
| Customer notification | Draft only | Yes | Customer authorization may be required. |
| DFIR escalation | Yes | Yes if evidence handling begins | Hand off to DFIR operating model. |

## Roles and Responsibilities

| Role | Responsibility | Must Not Do |
|---|---|---|
| MSSP Analyst | Review alerts, validate agent recommendations, approve routine service actions within authority, escalate when needed. | Treat agent output as final decision without review. |
| MSSP Service Lead | Own service workflow, customer operating rules, escalation criteria, and SLA expectations. | Override customer or policy boundaries without authorization. |
| Agentic Workflow | Triage, enrich, summarize, draft recommendations, identify uncertainty, and prepare escalation context. | Execute sensitive actions, approve itself, notify customers, or access unrelated customer data. |
| PDP | Decide whether the workflow is allowed, denied, restricted, requires approval, or requires escalation. | Enforce execution directly without a PEP. |
| PEP | Enforce policy at workflow, tool, retrieval, ticket, reporting, and output boundaries. | Allow execution when policy, scope, or approval is missing. |
| Customer Approver | Authorize customer-impacting actions where required by contract or engagement rules. | Be bypassed by internal approval when customer authorization is required. |
| Audit / Assurance | Record workflow activity, evaluate controls, and support replay. | Depend only on narrative summaries without structured traceability. |

## Agentic Assistance Boundaries

| Agent May | Agent Must Not |
|---|---|
| Summarize customer-scoped alert context. | Access another customer’s data. |
| Recommend triage priority. | Close alerts without policy and human-controlled workflow rules. |
| Draft internal analyst notes. | Publish customer-facing communication. |
| Identify uncertainty and missing context. | Convert uncertainty into unsupported conclusions. |
| Suggest escalation to MDR, Cloud IR, or DFIR. | Initiate evidence handling without DFIR controls. |
| Prepare approval context for sensitive actions. | Approve or execute sensitive actions. |

## Policy and Enforcement Points

| Boundary | PDP Decision Required When | PEP Enforcement Location |
|---|---|---|
| Retrieval | Context is retrieved from customer, case, incident, memory, or knowledge stores. | Retrieval layer or RAG gateway. |
| Tool use | Agent or workflow requests a tool, API, connector, script, or automation action. | Tool wrapper, API gateway, or workflow orchestrator. |
| Ticket update | Workflow writes to ticket, case, or service record. | Ticket connector or case management connector. |
| Customer-facing output | Summary, report, notification, or recommendation may be sent externally. | Output publishing layer. |
| Escalation | Workflow moves from MSSP triage into MDR, Cloud IR, or DFIR. | Workflow orchestrator. |
| Memory write | Workflow attempts to persist customer, case, or service memory. | Memory PEP or knowledge-store gateway. |

## Human Approval Gates

| If This Occurs | Then Require |
|---|---|
| Recommendation includes containment, isolation, blocking, quarantine, deletion, credential reset, or account disablement. | Human approval before execution; customer authorization where required. |
| Recommendation affects production systems or customer operations. | Human approval and customer authorization assessment. |
| Output is customer-facing. | Review and release approval before publication. |
| Recommendation is low-confidence but high-impact. | Human analyst review before action. |
| Scope is ambiguous across customer, tenant, case, or incident. | Return for clarification or fail closed. |
| Workflow requires evidence preservation or forensic conclusion. | Escalation to DFIR operating model. |
| Agent proposes persistent memory write. | Policy decision and approval based on memory governance rules. |
| Customer contract requires authorization. | Customer authorization before action or release. |

## Customer Authorization Gates

| Customer Authorization Required When | Enforcement Requirement |
|---|---|
| Customer notification is sent. | Output PEP must block release without authorization reference. |
| Customer environment is changed. | Tool PEP must verify authorization and approved scope. |
| Response action may disrupt users, systems, identities, or business process. | Workflow PEP must require approval and authorization check. |
| Evidence, logs, or customer data are exported or transferred. | Evidence or data movement PEP must verify authorization. |
| Customer-facing report is released. | Release workflow must include reviewer and authorization references where required. |

## Data Boundary Enforcement

| Data Boundary | Required Control |
|---|---|
| Tenant | Requests must carry `tenant_id`; missing or mismatched tenant fails closed. |
| Customer | Requests must carry `customer_id`; cross-customer retrieval is denied. |
| Case / Incident | Case and incident context must be scoped when the workflow is tied to a specific event. |
| Knowledge / Memory | Retrieval must include `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where used. |
| Evidence | Evidence references are required only when MSSP workflow escalates into DFIR or evidence-sensitive review. |
| Output Destination | Output must declare destination before release or write action. |
| Classification | Data classification and sensitivity label must be preserved through workflow state. |

## Retrieval and Memory Rules

| If | Then |
|---|---|
| RAG is used for enrichment. | Restrict retrieval to customer, tenant, and incident scope. |
| Case memory is used. | Validate case and customer scope before prompt assembly. |
| Persistent memory write is requested. | Deny by default unless approved by policy and retention rules. |
| Retrieved context is stale. | Mark as stale or return for clarification before using it in a recommendation. |
| Retrieved context crosses customer or tenant boundary. | Deny and emit audit event. |
| Retrieval affects a customer-facing output. | Preserve source references and require review before release. |

## Sensitive Action Handling

MSSP workflows may recommend sensitive actions, but they must not execute them without approval and enforcement.

| Sensitive Action | MSSP Agent Output Allowed | Execution Allowed? |
|---|---:|---:|
| Endpoint isolation | Recommendation only | Only after approval and authorized response path. |
| Indicator blocking | Recommendation only | Only after approval and authorized response path. |
| Credential reset | Recommendation only | Only after approval and customer authorization where required. |
| Account disablement | Recommendation only | Only after approval and customer authorization where required. |
| Customer notification | Draft only | Only after release approval and customer authorization where required. |
| Evidence export | Not routine MSSP action | Requires DFIR / data handling authorization. |
| Incident closure | Draft recommendation only | Human-controlled workflow decision required. |

## Escalation Paths

| Condition | Escalate To | Reason |
|---|---|---|
| Confirmed or suspected active compromise requiring response | MDR | Investigation and response support. |
| Cloud IAM compromise or cloud resource compromise | Cloud IR | Cloud-specific containment and evidence handling. |
| Evidence preservation, forensic timeline, malware analysis, or chain-of-custody required | DFIR | Formal forensic workflow required. |
| Local or isolated AI-assisted evidence analysis required | Private / Local LLM-assisted DFIR | Evidence cannot be processed through shared/cloud AI services. |
| Customer-impacting action required | Service lead / customer approver | Customer authority or contractual approval may be required. |
| Policy exception required | Service owner / governance approver | Exception must be explicitly approved and logged. |

## Audit and Replay Requirements

MSSP workflows should emit or preserve:

- request identifier;
- correlation identifier;
- audit reference identifier;
- tenant and customer identifiers;
- case or incident identifier where applicable;
- workflow identifier;
- agent identifier;
- requester identity;
- retrieved context references where used;
- policy decision;
- approval record where required;
- customer authorization reference where required;
- tool invocation record where applicable;
- output destination;
- final workflow state;
- deny, clarification, or escalation reason where applicable.

## Fail-Closed Rules

| Failure Condition | Required Behavior |
|---|---|
| Missing `tenant_id` or `customer_id` | Fail closed. |
| Customer context mismatch | Deny and audit. |
| Retrieval returns cross-customer context | Deny, quarantine result, and audit. |
| Policy unavailable | Fail closed. |
| Approval required but missing | Block action and route for approval. |
| Customer authorization required but missing | Block customer-impacting action. |
| Output destination missing or unauthorized | Block write or release. |
| Agent requests prohibited tool use | Deny and audit. |
| Evidence handling begins without DFIR scope | Escalate to DFIR or fail closed. |

## Relationship to Examples

| Example | MSSP Relevance |
|---|---|
| [`alert-triage-to-recommendation`](../examples/alert-triage-to-recommendation/) | Primary MSSP example for scoped triage and recommendation-only output. |
| [`cloud-iam-compromise`](../examples/cloud-iam-compromise/) | Applies when MSSP escalates cloud IAM compromise to MDR or Cloud IR with approval-controlled response. |
| [`local-llm-forensic-timeline`](../examples/local-llm-forensic-timeline/) | Applies only if MSSP hands off or supports DFIR timeline work. |

## Relationship to Patterns

| Pattern | MSSP Usage |
|---|---|
| [`governed-agentic-security-operations-pattern.md`](../patterns/governed-agentic-security-operations-pattern.md) | Baseline for scoped, policy-gated, auditable MSSP workflows. |
| [`policy-enforced-tool-use-pattern.md`](../patterns/policy-enforced-tool-use-pattern.md) | Applies to tool, API, connector, ticket, and output write actions. |
| [`human-approved-sensitive-action-pattern.md`](../patterns/human-approved-sensitive-action-pattern.md) | Applies to sensitive, customer-impacting, privileged, or externally visible actions. |
| [`tenant-safe-rag-memory-pattern.md`](../patterns/tenant-safe-rag-memory-pattern.md) | Applies to RAG, customer knowledge, service memory, and case memory. |
| [`private-local-llm-dfir-pattern.md`](../patterns/private-local-llm-dfir-pattern.md) | Applies only when MSSP workflows hand off to or support local/private DFIR. |

## Acceptance Criteria

An MSSP agentic operating workflow is acceptable when:

- every workflow is bound to tenant and customer scope;
- case or incident scope is present where applicable;
- agent output is treated as recommendation or draft support, not execution authority;
- policy is evaluated before tool use, ticket write, escalation state change, or output release where required;
- PEP enforcement exists at the actual boundary;
- sensitive actions require human approval;
- customer-impacting actions require customer authorization where applicable;
- retrieval and memory are scoped and auditable where used;
- evidence handling escalates to DFIR when required;
- customer-facing outputs are reviewed before release;
- denied or uncertain workflows fail closed or return for clarification;
- audit records support reconstruction.

## Non-Goals

This operating model does not:

- define a specific MSSP product, SIEM, XDR, SOAR, or ticketing platform;
- require all MSSP workflows to be agentic;
- allow agents to perform autonomous response;
- replace human analysts or service owners;
- replace customer contracts or authorization requirements;
- replace MDR, Cloud IR, or DFIR operating models;
- claim that AI recommendations are authoritative without review.

## Summary

The MSSP operating model defines how agentic assistance can improve managed security operations while preserving customer separation, service accountability, policy enforcement, human oversight, and auditability.

The core principle is:

> MSSP agents may triage, enrich, summarize, recommend, and prepare work, but they must not cross customer boundaries, execute sensitive actions, release customer-facing outputs, or handle evidence outside governed scope.
