# Alert Triage to Recommendation Example

## Purpose

This example demonstrates a governed agentic workflow that receives a security alert, enriches the alert with approved context, produces a response recommendation, evaluates the recommendation, records a policy decision, and emits an audit event.

The example supports the **Agentic MSSP / MDR / DFIR Security Operations Architecture** by showing how alert triage can remain scoped, policy-gated, evidence-aware, and auditable before any operational action is taken.

## Scenario

A security alert is received for a customer environment. An agentic workflow is asked to review the alert, summarize the likely issue, identify supporting context, and recommend the next operational step.

The agent does **not** directly execute containment, block indicators, modify detections, notify the customer, or close the case. It produces a recommendation that must be evaluated by assurance checks and policy controls before it can be acted on.

## Service Model Applicability

| Service Model | Applicability |
|---|---|
| MSSP | Applies to multi-customer alert triage, enrichment, recommendation drafting, ticket updates, and customer reporting support. |
| MDR | Applies to investigation support, escalation, response recommendation, and containment recommendation workflows. |
| SOC / Incident Response | Applies to alert review, incident coordination, escalation, and policy-gated investigation support. |
| DFIR | Applies only if the alert escalates into evidence handling, forensic investigation, timeline development, or case-level incident analysis. |
| Private / Local LLM-assisted DFIR | Not the primary use case for this example. It may apply only if the alert is escalated into local or isolated forensic analysis using private/local AI assistance. |

## Example Files

| File | Purpose |
|---|---|
| `README.md` | Explains the example scenario, workflow, controls, failure paths, and related patterns. |
| `example-request.json` | Shows the incoming alert triage request with tenant, customer, incident, workflow, and scope metadata. |
| `example-judge-output.json` | Shows assurance output evaluating evidence support, output quality, boundary alignment, and escalation concerns. |
| `example-policy-decision.json` | Shows the policy decision for the proposed recommendation or action. |
| `example-audit-event.json` | Shows the audit record that correlates the request, agent output, judge output, policy decision, and workflow context. |

## Actors and Components

| Actor or Component | Role |
|---|---|
| Alert source | Produces the security alert or incident signal. |
| Agentic triage workflow | Reviews scoped alert context and proposes a recommendation. |
| Retrieval or enrichment layer | Provides approved tenant/customer/incident context where allowed. |
| Judge or assurance check | Evaluates output quality, evidence support, boundary alignment, and risk. |
| Policy Decision Point | Determines whether the recommendation is allowed, denied, restricted, requires approval, or requires clarification. |
| Policy Enforcement Point | Enforces the policy decision before any tool use, output release, ticket update, or response action. |
| Human analyst | Reviews sensitive, uncertain, customer-impacting, or high-risk recommendations where required. |
| Audit layer | Records the request, context, judge output, policy decision, and workflow result. |

## Preconditions

Before this workflow runs, the system should have:

- a valid `tenant_id`;
- a valid `customer_id`;
- a valid `incident_id` or alert reference;
- a valid `workflow_id`;
- an identified `agent_id`;
- scoped authorization to access the alert;
- defined output destination;
- data classification and sensitivity label;
- approved enrichment or retrieval scope where retrieval is used;
- policy rules for recommendation, escalation, approval, and deny paths.

## Example Flow

1. **Alert received**  
   A scoped alert or incident is received from an approved source.

2. **Request normalized**  
   The request is normalized into a standard workflow input with tenant, customer, incident, workflow, identity, classification, and output metadata.

3. **Context retrieved or enriched**  
   Approved context is retrieved only within the authorized customer, tenant, incident, and workflow scope.

4. **Agent triage performed**  
   The agent summarizes the alert, identifies likely relevance, and proposes a recommendation.

5. **Assurance check performed**  
   A judge or assurance component evaluates whether the recommendation is evidence-supported, scoped, clear, and safe for the intended output.

6. **Policy decision evaluated**  
   The PDP evaluates the recommendation, risk level, required approval, output destination, and allowed next step.

7. **Decision enforced**  
   The PEP allows, denies, restricts, routes for approval, or returns the recommendation for clarification.

8. **Audit event recorded**  
   The workflow emits an audit event that correlates request, agent output, judge output, policy decision, and final workflow state.

## Policy and Enforcement Points

Policy evaluation should occur before:

- a recommendation is written to a ticket or case record;
- a customer-facing summary is generated or released;
- a tool or API is called;
- a response action is recommended as ready for execution;
- a detection, containment, blocking, or remediation action is initiated;
- the alert is closed, downgraded, escalated, or routed.

The enforcement point should exist at the real boundary, such as:

- workflow orchestrator;
- tool wrapper;
- ticketing connector;
- case management connector;
- response automation connector;
- customer report or notification path;
- output publishing layer.

## Human Approval Triggers

Human review should be required when the recommendation involves:

- containment;
- isolation;
- blocking;
- quarantine;
- deletion;
- credential reset;
- customer notification;
- customer-facing report release;
- externally visible action;
- low-confidence recommendation;
- ambiguous tenant, customer, or incident scope;
- evidence-sensitive escalation;
- policy exception;
- potential business impact.

Read-only triage, internal summarization, and low-risk enrichment may not require human approval when policy allows them, but they still require scope, logging, and policy evaluation.

## Evidence, Audit, and Traceability

The example should preserve enough context to reconstruct the workflow.

Audit and traceability should include:

- request timestamp;
- alert or incident reference;
- tenant and customer context;
- workflow and agent identity;
- retrieved context references where used;
- judge or assurance result;
- policy input and decision;
- approval requirement;
- output destination;
- final recommendation or workflow outcome;
- deny, escalation, or clarification reason where applicable;
- `audit_reference_id`;
- `correlation_id`.

For this alert triage example, `evidence_object_ids` may be empty or omitted unless the alert has escalated into DFIR evidence handling. If evidence is used, evidence references must be explicit and scoped to the case.

## Failure and Deny Paths

The workflow should fail closed or return for clarification when:

- tenant or customer scope is missing;
- incident or alert reference is missing;
- the agent requests unapproved data;
- retrieved context crosses customer, tenant, or incident boundaries;
- recommendation is unsupported by alert context;
- output destination is missing or unauthorized;
- policy cannot be evaluated;
- required human approval is missing;
- customer authorization is required but absent;
- the recommendation implies sensitive action without approval.

## What This Example Should Not Do

This example should not:

- allow an agent to directly execute response actions;
- treat a recommendation as approval;
- bypass PDP / PEP controls;
- update customer-facing records without policy evaluation;
- close an alert solely based on model output;
- mix customer, tenant, incident, or case context;
- present unsupported conclusions as facts;
- force Private / Local LLM-assisted DFIR controls unless forensic escalation occurs.

## Expected Control Outcome

A successful run should produce:

- a scoped alert triage request;
- an agent recommendation;
- an assurance or judge output;
- a policy decision;
- an audit event;
- a clear next-state outcome such as allow, deny, restrict, require approval, return for clarification, or escalate.

## Acceptance Criteria

This example is acceptable when:

- the workflow is scoped to a specific tenant, customer, incident, and workflow;
- agent output is treated as a recommendation, not execution authority;
- policy is evaluated before tool use, ticket update, customer-facing output, or response action;
- human approval is triggered for sensitive or customer-impacting recommendations;
- retrieved context is scoped and auditable where used;
- audit records allow the workflow to be reconstructed;
- failure and deny paths are represented;
- DFIR and Private / Local LLM-assisted DFIR are included only where escalation into evidence handling or local forensic analysis naturally applies.

## Related Patterns

This example maps to:

- [`governed-agentic-security-operations-pattern.md`](../../patterns/governed-agentic-security-operations-pattern.md)
- [`policy-enforced-tool-use-pattern.md`](../../patterns/policy-enforced-tool-use-pattern.md)
- [`human-approved-sensitive-action-pattern.md`](../../patterns/human-approved-sensitive-action-pattern.md)
- [`tenant-safe-rag-memory-pattern.md`](../../patterns/tenant-safe-rag-memory-pattern.md)
- [`control-loop.md`](../../architecture/control-loop.md)
- [`layered-architecture.md`](../../architecture/layered-architecture.md)

## Summary

This example shows how alert triage can use agentic assistance without granting the agent uncontrolled authority.

The core principle is:

> The agent may triage and recommend, but policy, enforcement, human approval where required, and auditability determine what can happen next.
