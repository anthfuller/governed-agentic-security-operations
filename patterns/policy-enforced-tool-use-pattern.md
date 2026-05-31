# Policy-Enforced Tool Use Pattern

## Purpose

This pattern defines how tools, APIs, scripts, connectors, playbooks, and automation actions are safely used by agentic security workflows across the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

It supports **MSSP**, **MDR**, **SOC / Incident Response**, **DFIR**, and **Private / Local LLM-assisted DFIR** where applicable by requiring every tool action to be scoped, policy-evaluated, enforced, logged, and auditable before it can affect customer systems, tenant data, evidence, cases, or operational outcomes.

## Pattern Summary

Agentic systems must not receive broad or implicit tool access.

The core pattern is:

**Agent proposes tool use**  
→ **tool request is bound to tenant / customer / case / workflow context**  
→ **Policy Decision Point evaluates authorization and risk**  
→ **Policy Enforcement Point allows, denies, pauses, or routes for approval**  
→ **approved tool action executes with least privilege and scoped credentials**  
→ **result is validated, logged, and correlated to audit evidence**

This pattern makes tool use an explicitly governed action, not a default capability of the agent.

## Context

Agentic security operations may need tools to support:

- alert enrichment;
- asset lookup;
- identity lookup;
- threat intelligence queries;
- SIEM / XDR investigation;
- EDR containment recommendations;
- ticket updates;
- case management;
- evidence review;
- forensic artifact parsing;
- report generation;
- workflow routing;
- customer notification preparation.

In MSSP and MDR environments, the same operating platform may support many customers and tenants. In DFIR and Private / Local LLM-assisted DFIR, tools may interact with case evidence, forensic artifacts, local evidence repositories, timelines, reports, or isolated analysis environments.

Without a policy-enforced tool-use pattern, agents may call tools outside their mission, access the wrong tenant or case, use stale context, perform unauthorized actions, modify evidence, trigger customer-impacting operations, or produce results that cannot be reconstructed later.

## Problem

How can an agentic workflow use tools and APIs to support security operations while preventing unauthorized, unscoped, destructive, cross-tenant, cross-case, or non-auditable actions?

## Forces

This pattern balances the following forces:

- **Operational speed vs. authorization** — tools make investigations faster, but tool calls must be authorized before execution.
- **Agent autonomy vs. least privilege** — agents may propose actions, but tool access must be constrained to approved scope.
- **Shared platforms vs. customer isolation** — MSSP and MDR platforms may share infrastructure, but tool calls must remain tenant and customer scoped.
- **Investigation depth vs. evidence integrity** — DFIR workflows may require deep evidence access, but evidence must not be modified or contaminated.
- **Automation vs. human accountability** — sensitive or customer-impacting tool use must route to human review before execution.
- **Continuous operations vs. replayability** — tool actions must be logged so decisions and outcomes can be reconstructed.

## Applicability

Use this pattern when an agent, automation, workflow, or AI-assisted process can invoke or influence a tool action that affects:

- customer or tenant systems;
- case or incident records;
- SIEM, XDR, EDR, SOAR, cloud, identity, or ticketing platforms;
- evidence repositories or forensic artifacts;
- knowledge stores, memory, retrieval systems, or case context;
- reports or customer-facing outputs;
- containment, isolation, blocking, deletion, notification, or remediation workflows.

This pattern is applicable to:

- **MSSP** — customer-scoped alert enrichment, ticketing, reporting, and workflow routing.
- **MDR** — investigation, escalation, detection tuning, containment recommendation, and response support.
- **SOC / Incident Response** — triage, coordination, tool-assisted investigation, escalation, and approval routing.
- **DFIR** — evidence lookup, artifact parsing, timeline support, report preparation, and evidence-backed findings.
- **Private / Local LLM-assisted DFIR** — local or isolated tool use for forensic assistance where tool execution, inputs, outputs, and evidence references remain auditable.

Do not force this pattern onto manual work that does not involve agentic tool use, automation, or AI-assisted tool execution. The relevant controls for manual workflows remain human review, evidence integrity, chain of custody, and auditability.

## Solution

Place every tool call behind an explicit policy-enforced tool-use boundary.

The agent may propose a tool action, but the system must evaluate and enforce whether that action is allowed before execution. The enforcement boundary must sit close to the real execution point: the tool wrapper, API gateway, workflow orchestrator, sandbox, retrieval layer, evidence-access layer, or output publishing path.

The policy-enforced tool-use boundary should perform five functions:

1. **Bind context**  
   Attach tenant, customer, case, workflow, identity, requested action, tool, data scope, output destination, and evidence references where applicable.

2. **Evaluate policy**  
   Determine whether the requested tool action is allowed, denied, requires human approval, requires clarification, or must be escalated.

3. **Enforce decision**  
   Permit only approved tool calls and block or pause everything else.

4. **Constrain execution**  
   Use least privilege, scoped credentials, approved parameters, safe defaults, sandboxing, and output restrictions.

5. **Record and validate**  
   Log inputs, decisions, approvals, execution results, output destinations, and evidence references for audit and replay.

## Architecture Roles

### Agent

The agent may:

- reason over approved context;
- propose a tool action;
- explain why the tool is needed;
- provide intended inputs;
- receive approved tool results;
- summarize or recommend next steps.

The agent must not directly bypass policy enforcement or acquire unrestricted credentials.

### Tool Broker or Tool Wrapper

The tool broker or wrapper mediates tool access.

It should:

- receive tool requests from agents or workflows;
- normalize the request into a standard tool invocation contract;
- call the Policy Decision Point;
- enforce the Policy Enforcement Point decision;
- execute only approved actions;
- log tool inputs and outputs;
- return structured results to the workflow.

### Policy Decision Point

The PDP evaluates whether the tool request is allowed.

It should evaluate:

- requester identity;
- agent identity;
- tenant and customer scope;
- case or incident scope;
- tool authorization;
- data classification;
- sensitivity label;
- requested action;
- allowed parameters;
- approval requirements;
- evidence sensitivity;
- output destination;
- risk level;
- policy exceptions.

### Policy Enforcement Point

The PEP enforces the PDP decision at the real boundary.

It should:

- block denied tool calls;
- pause calls requiring approval;
- restrict parameters;
- inject scoped credentials only after approval;
- enforce output destination;
- prevent unapproved data access;
- fail closed when policy is unavailable or ambiguous;
- emit audit events for every decision and execution attempt.

### Human Approver

A human approver is required for sensitive tool actions.

Examples include:

- containment;
- isolation;
- deletion;
- blocking;
- credential reset;
- quarantine;
- evidence modification;
- customer notification;
- externally visible reporting;
- policy exceptions;
- actions with low confidence or unclear scope.

### Audit and Assurance Layer

The audit and assurance layer records, monitors, and validates tool use.

It should capture:

- request context;
- policy input;
- policy decision;
- approval record;
- tool call;
- execution result;
- evidence references;
- output destination;
- errors and denials;
- correlation identifiers;
- replay data.

## Reference Flow

A policy-enforced tool-use flow should operate as follows:

1. The agent receives a mission-scoped task.
2. The agent proposes a tool action and explains the intended purpose.
3. The workflow binds the request to tenant, customer, case, workflow, identity, data, evidence, and output context.
4. The tool broker normalizes the request into a tool invocation contract.
5. The PDP evaluates authorization, scope, risk, policy, and approval requirements.
6. The PDP returns one of the supported decision outcomes.
7. The PEP enforces the decision at the tool boundary.
8. If approved, the tool executes with scoped credentials and constrained parameters.
9. The tool result is returned to the workflow.
10. The result is validated for scope, evidence support, output safety, and policy alignment.
11. The request, decision, approval, execution result, and output are logged.
12. Monitoring and assurance findings feed governed improvements to policies, tests, prompts, tool wrappers, and procedures.

## Decision Outcomes

The pattern requires explicit tool-use decision outcomes:

- **Allow** — execute the tool action within approved scope.
- **Deny** — block the tool action and fail closed.
- **Require Human Approval** — pause until an authorized reviewer approves, rejects, or modifies the action.
- **Restrict** — allow the action only with reduced scope, safer parameters, or read-only mode.
- **Return for Clarification** — request more context when tenant, customer, case, authority, evidence basis, or output destination is unclear.
- **Escalate** — route to a human analyst, DFIR lead, incident commander, service owner, or customer approver.

## Tool Invocation Contract

A tool request should be converted into a standard contract before policy evaluation.

Minimum fields should include, where applicable:

- `tenant_id`;
- `customer_id`;
- `case_id`;
- `incident_id`;
- `workflow_id`;
- `agent_id`;
- `user_id` or service identity;
- `requested_action`;
- `tool_id`;
- `tool_owner`;
- `tool_purpose`;
- `source_system_id`;
- `destination_system_id`;
- `output_destination`;
- `data_classification`;
- `sensitivity_label`;
- `evidence_object_ids`;
- `knowledge_store_or_memory_scope`;
- `retrieved_context_scope`;
- `requested_parameters`;
- `risk_level`;
- `approval_required`;
- `approval_record_id`;
- `policy_decision`;
- `audit_reference_id`;
- `correlation_id`.

## Policy Input Requirements

The PDP should receive enough context to make a real decision.

Policy input should include:

- who or what is requesting the tool call;
- which agent or workflow is involved;
- which tenant and customer are in scope;
- which case, incident, or evidence set is in scope;
- what tool is being requested;
- what action and parameters are requested;
- what data classification and sensitivity apply;
- where the output will go;
- whether the action changes state;
- whether the action affects a customer, user, host, identity, or evidence object;
- whether human approval is required;
- whether the request depends on retrieved context or memory.

## Enforcement Requirements

The PEP must enforce the decision before tool execution.

A valid PEP implementation should:

- deny by default;
- fail closed if PDP is unavailable;
- block missing tenant, customer, case, or workflow context where required;
- block missing output destination where required;
- block missing evidence scope for evidence-sensitive workflows;
- restrict actions to approved tools and parameters;
- prevent direct agent access to secrets;
- inject scoped credentials only after authorization;
- enforce read-only mode where required;
- log all attempts, including denied attempts;
- prevent tools from writing outputs to unapproved destinations.

## Tool Risk Classes

Tool actions should be classified by risk.

### Low-Risk Tool Use

Examples:

- read-only lookup;
- metadata retrieval;
- non-sensitive enrichment;
- status checks;
- internal draft creation.

Controls:

- policy evaluation;
- scoped access;
- logging;
- output validation.

### Medium-Risk Tool Use

Examples:

- ticket updates;
- case note updates;
- detection rule draft generation;
- internal workflow routing;
- evidence metadata extraction;
- non-destructive query execution.

Controls:

- policy evaluation;
- scoped access;
- parameter validation;
- logging;
- output validation;
- human review where required by policy.

### High-Risk Tool Use

Examples:

- containment;
- isolation;
- blocking;
- quarantine;
- deletion;
- credential reset;
- customer notification;
- evidence modification;
- externally visible publishing;
- policy exception execution.

Controls:

- policy evaluation;
- mandatory human approval;
- scoped credentials;
- strong audit;
- replayability;
- explicit output destination;
- rollback or recovery plan where applicable.

## DFIR and Evidence-Sensitive Tool Use

For DFIR and Private / Local LLM-assisted DFIR, tool use must preserve forensic integrity.

Evidence-sensitive tool actions should:

- operate read-only unless explicitly approved;
- preserve original evidence;
- record evidence object identifiers;
- preserve provenance and chain of custody;
- distinguish extracted facts from model-generated interpretation;
- log parsing, transformation, enrichment, summarization, and report-generation steps;
- avoid overwriting source artifacts;
- ensure generated findings are traceable to evidence references;
- require human review before forensic conclusions are released.

Private or local execution does not remove the need for governance. Local tools should still log inputs, outputs, parameters, evidence references, and operator approvals.

## Retrieval, Memory, and Context Controls

Tool use may depend on retrieved context, memory, or knowledge stores.

When retrieval or memory influences a tool request, the workflow should validate:

- `knowledge_store_or_memory_scope`;
- `retrieved_context_scope`;
- tenant and customer boundaries;
- case and incident boundaries;
- freshness of retrieved context;
- authorization to use the retrieved context;
- whether retrieved context is evidence, reference material, prior finding, or model-generated text.

Tool execution should fail closed if retrieved context is cross-tenant, cross-customer, cross-case, stale, unauthorized, or insufficiently scoped.

## Output Destination Controls

The pattern requires explicit control over where tool results go.

Output destinations may include:

- internal analyst console;
- case record;
- ticketing system;
- evidence repository;
- audit log;
- customer report draft;
- customer-facing portal;
- detection engineering backlog;
- local DFIR workspace.

High-risk outputs, external outputs, customer-facing outputs, and evidence-related outputs should require validation and, where required, human approval before release.

## Logging and Audit Requirements

Every tool-use attempt should generate an audit event.

Audit events should record:

- request timestamp;
- requester identity;
- agent identity;
- tenant and customer context;
- case or incident context;
- tool and action requested;
- requested parameters;
- policy input;
- policy decision;
- approval status;
- execution result;
- output destination;
- evidence object references;
- error or denial reason;
- correlation identifiers.

Logs should support replay or reconstruction of the workflow.

## Human Oversight Triggers

Human review should be required when tool use is:

- destructive;
- privileged;
- customer-impacting;
- evidence-sensitive;
- externally visible;
- policy-exception based;
- low-confidence;
- ambiguous in tenant, customer, or case scope;
- dependent on stale or uncertain retrieved context;
- related to containment, isolation, blocking, deletion, quarantine, credential reset, customer notification, or evidence modification.

## Failure Modes

This pattern is intended to reduce the following failure modes:

- agent directly calls a tool without policy evaluation;
- tool call executes under the wrong tenant or customer;
- tool call uses the wrong case or evidence scope;
- agent uses broad credentials;
- tool writes to an unauthorized destination;
- high-risk action executes without approval;
- evidence is modified or contaminated;
- retrieved context causes cross-case or stale-context contamination;
- tool output cannot be reconstructed;
- policy is unavailable but execution proceeds anyway;
- tool logs do not include enough information for audit or replay.

## Anti-Patterns

Avoid the following anti-patterns:

- **Direct agent-to-tool access** — agents should not bypass policy and enforcement boundaries.
- **Prompt-only authorization** — prompts are not a substitute for PDP/PEP enforcement.
- **Shared credentials across tenants** — tool credentials must be scoped and controlled.
- **Tool access by default** — tools must be explicitly authorized.
- **Review after high-risk execution** — sensitive actions require review before execution.
- **Unscoped retrieval before tool use** — retrieved context must be tenant, customer, case, and authorization scoped.
- **Unlogged local DFIR tools** — local or offline tooling still requires auditability where AI assistance or agentic workflows are used.
- **Evidence-free output** — findings and reports must be tied to evidence references.
- **Uncontrolled output publishing** — tool results must not be written to customer-facing or external destinations without validation and approval where required.

## Service Model Mapping

| Service Model | Pattern Usage |
|---|---|
| MSSP | Governs multi-customer tool use for alert enrichment, ticketing, reporting, routing, and customer-specific workflows. |
| MDR | Governs investigation, escalation, containment recommendation, response support, and detection-related tool use. |
| SOC / Incident Response | Governs triage, coordination, tool-assisted investigation, incident updates, and approval-routed response actions. |
| DFIR | Governs evidence-sensitive tool use, artifact parsing, timeline support, case updates, and evidence-backed reporting. |
| Private / Local LLM-assisted DFIR | Applies when local or isolated AI-assisted tooling is used for forensic analysis, summarization, artifact review, or report preparation. |

## Implementation Guidance

A practical implementation should start with:

1. **Tool registry**
   - tool name;
   - tool owner;
   - approved use cases;
   - allowed actions;
   - risk class;
   - required metadata;
   - approval requirements;
   - allowed output destinations.

2. **Tool invocation contract**
   - normalized request schema;
   - required tenant, customer, case, workflow, and identity fields;
   - required evidence fields for DFIR;
   - required output destination;
   - correlation identifiers.

3. **Policy rules**
   - allowed tool/action combinations;
   - tenant and customer boundary checks;
   - role-based authorization;
   - case and evidence scope checks;
   - approval triggers;
   - deny conditions;
   - fail-closed behavior.

4. **PEP enforcement**
   - tool wrapper;
   - API gateway;
   - workflow orchestrator;
   - sandbox runtime;
   - retrieval layer;
   - evidence-access layer;
   - output publishing layer.

5. **Audit and validation**
   - log every tool-use attempt;
   - validate outputs before use;
   - correlate policy decisions with tool execution;
   - support replay and review.

## Minimum Metadata

Where applicable, every tool-use event should carry or reference:

- `tenant_id`;
- `customer_id`;
- `case_id`;
- `incident_id`;
- `workflow_id`;
- `agent_id`;
- `user_id` or service identity;
- `tool_id`;
- `tool_owner`;
- `requested_action`;
- `source_system_id`;
- `destination_system_id`;
- `output_destination`;
- `data_classification`;
- `sensitivity_label`;
- `evidence_object_ids`;
- `knowledge_store_or_memory_scope`;
- `retrieved_context_scope`;
- `policy_decision`;
- `approval_record_id`;
- `audit_reference_id`;
- `correlation_id`.

## Acceptance Criteria

A policy-enforced tool-use implementation is acceptable when:

- agents cannot call tools directly without passing through a PEP;
- every tool action is bound to tenant, customer, case, workflow, and identity context where applicable;
- policy is evaluated before execution;
- tools are denied by default and fail closed when policy cannot be evaluated;
- tool permissions are least-privilege and scoped;
- high-risk actions require human approval before execution;
- evidence-sensitive tool use preserves provenance and chain of custody;
- retrieval and memory scope are validated when they influence tool requests;
- output destinations are controlled and logged;
- all tool-use attempts are auditable and replayable;
- implementation includes tests for allow, deny, approval, clarification, escalation, and fail-closed paths.

## Non-Goals

This pattern does not:

- define a vendor-specific tool catalog;
- require every workflow to use tools;
- require every tool call to have human approval;
- replace human accountability;
- replace incident command or DFIR lead authority;
- make local or private LLM execution inherently trustworthy;
- remove the need for secure engineering, testing, monitoring, or operational runbooks.

## Related Architecture Views

This pattern complements:

- `governed-agentic-security-operations-pattern.md` — defines the broader governed agentic security operations pattern.
- `control-loop.md` — defines runtime action governance.
- `layered-architecture.md` — defines the operating layers.
- shared operating boundary visuals — define non-negotiable controls across service models.
- engineering architecture diagrams — define detailed components, integrations, and control planes.

## Summary

The Policy-Enforced Tool Use Pattern ensures that agentic systems do not receive uncontrolled access to operational tools, APIs, evidence stores, or customer-impacting actions.

The pattern supports MSSP, MDR, SOC / Incident Response, DFIR, and Private / Local LLM-assisted DFIR where applicable by requiring explicit context binding, PDP evaluation, PEP enforcement, scoped credentials, least privilege, human approval for sensitive actions, evidence-aware validation, and complete auditability.

The core principle is:

> Agents may propose tool use, but tools execute only through policy-enforced, scoped, auditable, and human-overseen control paths where risk requires it.
