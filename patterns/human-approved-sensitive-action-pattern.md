# Human-Approved Sensitive Action Pattern

## Purpose

This pattern defines how sensitive, high-impact, privileged, customer-impacting, or evidence-sensitive actions are routed for explicit human approval within the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

It supports **MSSP**, **MDR**, **SOC / Incident Response**, **DFIR**, and **Private / Local LLM-assisted DFIR** where applicable by ensuring that agentic workflows cannot execute sensitive actions solely because an agent proposed them, a prompt requested them, or another agent delegated them.

## Pattern Summary

Sensitive actions require a governed approval path before execution.

The core pattern is:

**Agent proposes sensitive action**  
→ **policy classifies the action and requires approval**  
→ **human reviewer evaluates scope, evidence, risk, and authority**  
→ **approval decision is recorded**  
→ **PEP enforces the approved, denied, modified, or escalated outcome**  
→ **execution and results are logged, validated, and auditable**

Human approval is not a replacement for policy enforcement. The Policy Decision Point determines whether approval is required, and the Policy Enforcement Point enforces the final decision at the execution boundary.

## Context

Agentic security operations may propose actions that affect customers, users, hosts, identities, data, evidence, business operations, or external communications.

Examples include:

- isolating an endpoint;
- blocking an IP address, URL, domain, account, or hash;
- disabling or resetting credentials;
- quarantining files;
- deleting or modifying data;
- updating detection rules;
- notifying a customer;
- publishing a customer-facing report;
- modifying a case record or evidence package;
- escalating an incident externally;
- using a privileged tool or connector;
- approving a policy exception.

In MSSP and MDR operations, these actions may affect customer environments. In SOC / Incident Response, they may affect production systems or incident coordination. In DFIR and Private / Local LLM-assisted DFIR, they may affect evidence integrity, chain of custody, forensic findings, and customer-facing conclusions.

## Problem

How can agentic security workflows support sensitive operations without allowing agents to independently execute high-risk actions, bypass human accountability, or produce unapproved customer-impacting outcomes?

## Forces

This pattern balances the following forces:

- **Speed vs. risk** — security teams need fast action, but high-impact actions must not execute without review.
- **Automation vs. accountability** — agents may recommend actions, but accountable humans must approve sensitive execution.
- **Policy vs. judgment** — policy can classify risk and enforce boundaries, but human judgment is required for context-sensitive decisions.
- **Customer impact vs. operational need** — containment or notification may be necessary, but must align with customer authority and service agreements.
- **DFIR support vs. forensic integrity** — AI assistance may accelerate analysis, but evidence-sensitive conclusions and actions require human validation.
- **Approval vs. enforcement** — approval authorizes an action within scope; enforcement ensures the action cannot exceed that approval.

## Applicability

Use this pattern when an agentic workflow may propose, trigger, draft, recommend, or execute an action that is:

- destructive;
- privileged;
- customer-impacting;
- externally visible;
- evidence-sensitive;
- legally or contractually sensitive;
- policy-exception based;
- low-confidence;
- cross-tenant or cross-case ambiguous;
- related to containment, isolation, blocking, quarantine, deletion, credential reset, customer notification, evidence handling, or customer-facing reporting.

This pattern applies to:

- **MSSP** — customer notifications, ticket updates with impact, response recommendations, service escalations, and customer-facing reports.
- **MDR** — containment recommendations, endpoint isolation requests, detection tuning changes, response actions, and escalations.
- **SOC / Incident Response** — incident command support, privileged actions, containment decisions, coordination updates, and operational response steps.
- **DFIR** — evidence-sensitive actions, forensic conclusions, report release, timeline interpretation, and chain-of-custody-impacting decisions.
- **Private / Local LLM-assisted DFIR** — local or isolated AI-assisted forensic workflows where evidence interpretation, report preparation, or tool-assisted analysis requires human validation.

Do not force this pattern onto low-risk, read-only, internal enrichment that policy allows without human approval. Those workflows still require policy evaluation, logging, and scoped access, but may not require an approval checkpoint.

## Solution

Implement a human-approved sensitive action pattern with seven required elements:

1. **Sensitive Action Classification**  
   The workflow classifies the proposed action by risk, impact, scope, reversibility, customer exposure, privilege level, evidence sensitivity, and policy requirements.

2. **Policy Decision Before Approval**  
   The PDP evaluates whether the action is allowed, denied, requires approval, requires clarification, or must be escalated.

3. **Approval Request Package**  
   The system presents the human reviewer with enough information to make a decision: mission, tenant, customer, case, evidence, proposed action, reason, risk, affected assets, expected impact, rollback or recovery options, and policy basis.

4. **Qualified Human Review**  
   An authorized reviewer evaluates whether the action is appropriate, scoped, evidence-supported, and permitted under service, customer, legal, and operational boundaries.

5. **Recorded Approval Decision**  
   The reviewer decision is captured as an approval record with reviewer identity, timestamp, decision, scope, conditions, rationale, and expiration where applicable.

6. **PEP-Enforced Execution**  
   The PEP executes only the approved action, within the approved scope, parameters, identity, tool, output destination, and time window.

7. **Post-Action Validation and Audit**  
   The result is validated, logged, correlated to the approval record, and available for audit, replay, and review.

## Architecture Roles

### Agent

The agent may:

- recommend a sensitive action;
- explain the reason for the recommendation;
- provide supporting evidence;
- identify expected impact;
- draft a customer-facing message or report;
- summarize approval context.

The agent must not approve its own action, bypass approval, modify approval records, or execute sensitive actions without enforcement.

### Policy Decision Point

The PDP determines whether approval is required.

It should evaluate:

- tenant and customer scope;
- case or incident scope;
- requester identity;
- agent identity;
- action type;
- risk class;
- tool and API permissions;
- evidence sensitivity;
- customer impact;
- output destination;
- confidence level;
- policy exceptions;
- service model requirements.

### Policy Enforcement Point

The PEP enforces the approval outcome.

It should:

- block execution until approval is present where required;
- verify the approval record;
- verify that the approval matches the requested action;
- restrict execution to approved parameters;
- prevent approval reuse outside scope;
- fail closed if approval is missing, expired, invalid, or mismatched;
- log both approved and denied attempts.

### Human Reviewer

The human reviewer provides accountable review.

The reviewer should be authorized for the relevant service model, customer, case, action type, and risk level.

The reviewer may:

- approve;
- deny;
- modify scope or parameters;
- request clarification;
- escalate;
- require customer authorization;
- require additional evidence.

### Customer Approver

Some actions may require customer authorization, not just internal human approval.

Customer authorization may be required for:

- customer-impacting containment;
- production changes;
- externally visible notifications;
- report release;
- evidence transfer;
- data export;
- actions defined by contract, engagement rules, or legal hold.

Internal human approval should not be treated as a substitute for customer authorization when customer authorization is required.

### Audit and Assurance Layer

The audit and assurance layer records:

- approval request;
- supporting context;
- reviewer decision;
- policy decision;
- approval conditions;
- execution attempt;
- result;
- evidence references;
- output destination;
- audit and correlation identifiers.

## Reference Flow

A human-approved sensitive action flow should operate as follows:

1. An agentic workflow receives a mission-scoped task.
2. The agent proposes an action or output.
3. The workflow binds the proposal to tenant, customer, case, workflow, identity, evidence, and output context.
4. The PDP classifies the proposed action and determines whether approval is required.
5. If approval is required, the workflow creates an approval request package.
6. The human reviewer evaluates risk, scope, authority, evidence, impact, and policy basis.
7. The reviewer approves, denies, modifies, requests clarification, escalates, or requires customer authorization.
8. The approval decision is recorded with conditions and scope.
9. The PEP verifies the approval record before execution.
10. Approved execution occurs only within the approved scope and parameters.
11. Results are validated and logged.
12. Monitoring and assurance findings feed governed improvements to policy, approval criteria, prompts, tests, and procedures.

## Decision Outcomes

The pattern requires explicit approval decision outcomes:

- **Approve** — authorize the action within defined scope, parameters, and time window.
- **Deny** — block the action and record the reason.
- **Approve with Conditions** — allow only with modified scope, safer parameters, read-only mode, staged execution, or additional controls.
- **Request Clarification** — require more information before approval.
- **Escalate** — route to incident commander, DFIR lead, service owner, legal, compliance, or customer approver.
- **Require Customer Authorization** — pause until the required customer authority approves.
- **Expire** — invalidate approval after time, context, case state, or risk changes.

## Sensitive Action Categories

### Destructive or State-Changing Actions

Examples:

- delete;
- quarantine;
- isolate;
- disable;
- reset;
- block;
- revoke;
- modify;
- publish;
- export.

Controls:

- mandatory policy evaluation;
- human approval;
- scoped execution;
- rollback or recovery plan where applicable;
- full audit.

### Customer-Impacting Actions

Examples:

- customer notification;
- containment in customer environment;
- production-impacting change;
- customer-facing report release;
- data export or evidence transfer.

Controls:

- internal human approval;
- customer authorization where required;
- explicit output destination;
- audit and communication record.

### Evidence-Sensitive Actions

Examples:

- forensic conclusion;
- evidence transformation;
- artifact extraction;
- timeline interpretation;
- report drafting;
- evidence package preparation;
- evidence movement.

Controls:

- evidence provenance;
- chain-of-custody validation;
- read-only handling where required;
- human validation before findings are released;
- audit trail tied to evidence object identifiers.

### Privileged Tool Actions

Examples:

- administrative API calls;
- identity changes;
- rule deployment;
- containment tool execution;
- high-privilege connector use;
- access to sensitive logs or evidence stores.

Controls:

- scoped credentials;
- PEP enforcement;
- approval record;
- least privilege;
- strong logging.

## Approval Request Package

A reviewer should receive enough information to make a decision without guessing.

The approval request should include, where applicable:

- `tenant_id`;
- `customer_id`;
- `case_id`;
- `incident_id`;
- `workflow_id`;
- requesting user or service identity;
- agent identity;
- proposed action;
- action category and risk level;
- affected assets, users, systems, or evidence objects;
- policy decision and approval trigger;
- supporting evidence;
- retrieved context scope;
- expected impact;
- rollback or recovery option where applicable;
- output destination;
- customer authorization requirement;
- time sensitivity;
- recommendation confidence;
- known uncertainties;
- audit reference and correlation identifiers.

## Approval Record Requirements

The approval record should capture:

- approval request identifier;
- reviewer identity;
- reviewer role;
- approval timestamp;
- decision outcome;
- approved action;
- approved scope;
- approved parameters;
- approved tool or workflow;
- approval expiration;
- rationale or decision notes;
- conditions or restrictions;
- customer authorization reference where required;
- **cryptographic binding (signature hash, signature method, and signed payload references);**
- linked policy decision;
- linked execution result;
- audit reference and correlation identifiers.

## Enforcement Requirements

The PEP must verify approval before sensitive execution.

A valid enforcement implementation should:

- deny by default;
- fail closed if approval is missing or invalid;
- prevent action execution before approval;
- prevent approval reuse across tenants, customers, cases, workflows, tools, or time windows;
- verify that approved parameters match execution parameters;
- **cryptographically verify the approval signature against the original payload references;**
- enforce restricted or conditional approvals;
- prevent direct agent execution of sensitive actions;
- log approval verification and execution results;
- block execution if policy, context, evidence, or output destination changes after approval.

## DFIR and Private / Local LLM-assisted DFIR Requirements

For DFIR and Private / Local LLM-assisted DFIR, approval must protect forensic integrity.

Human approval should be required before:

- releasing forensic findings;
- making customer-facing forensic conclusions;
- modifying, exporting, or transferring evidence;
- relying on AI-generated forensic interpretation;
- using tools that may alter evidence;
- finalizing incident timelines;
- including model-generated analysis in reports;
- moving evidence across environments or trust boundaries.

Private or local execution does not remove the need for approval. Local AI assistance should still preserve case scope, evidence references, reviewer identity, approval records, and auditability.

## Output and Release Controls

Sensitive outputs should not be released only because an agent drafted them.

Customer-facing or externally visible outputs should be checked for:

- evidence support;
- tenant and case scope;
- accuracy;
- unsupported claims;
- sensitive data exposure;
- legal or contractual sensitivity;
- customer authorization requirements;
- approval record linkage.

Final release should be controlled by an authorized human, customer approver, or defined release process where required.

## Human Oversight Triggers

Human approval should be triggered when an action is:

- destructive;
- privileged;
- externally visible;
- customer-impacting;
- evidence-sensitive;
- legally sensitive;
- policy-exception based;
- low-confidence;
- irreversible or difficult to reverse;
- cross-tenant, cross-customer, or cross-case ambiguous;
- dependent on stale, unverified, or uncertain context;
- related to containment, isolation, blocking, deletion, quarantine, credential reset, evidence modification, customer notification, or report release.

## Failure Modes

This pattern is intended to reduce the following failure modes:

- agent executes a sensitive action without approval;
- reviewer approves without adequate context;
- approval is reused outside scope;
- customer authorization is skipped;
- PEP does not enforce approval conditions;
- action parameters change after approval;
- evidence-sensitive output is released without validation;
- approval records cannot be tied to execution records;
- policy says approval is required, but workflow proceeds anyway;
- local DFIR analysis produces unsupported conclusions without human review.

## Anti-Patterns

Avoid the following anti-patterns:

- **Agent self-approval** — agents must not approve their own actions.
- **Approval as a prompt instruction** — approval must be recorded and enforced, not only described in a prompt.
- **Review after high-risk execution** — sensitive actions require approval before execution.
- **Blanket approval** — approval must be scoped to action, tenant, customer, case, parameters, and time window.
- **Approval without enforcement** — approval has no value if the PEP does not enforce it.
- **Approval without evidence** — evidence-sensitive decisions require supporting evidence references.
- **Customer-impacting action without customer authority** — internal approval is not always enough.
- **Unlogged local DFIR approval** — private or local workflows still require approval records where AI-assisted sensitive actions are used.
- **Approval reuse across cases** — approvals must not carry across tenants, customers, cases, or unrelated workflows.

## Service Model Mapping

| Service Model | Pattern Usage |
|---|---|
| MSSP | Governs customer-facing outputs, customer-impacting workflow steps, escalations, and managed-service actions that require review or authorization. |
| MDR | Governs containment recommendations, response actions, detection tuning changes, escalation, and customer-impacting response support. |
| SOC / Incident Response | Governs incident command decisions, privileged actions, containment coordination, and externally visible incident communications. |
| DFIR | Governs evidence-sensitive decisions, forensic findings, evidence movement, chain-of-custody-impacting steps, and report release. |
| Private / Local LLM-assisted DFIR | Applies when local or isolated AI assistance supports forensic interpretation, evidence review, report drafting, or tool-assisted analysis requiring human validation. |

## Implementation Guidance

A practical implementation should start with:

1. **Approval trigger policy**
   - action categories;
   - risk classes;
   - service model requirements;
   - customer authorization requirements;
   - evidence-sensitive triggers;
   - low-confidence or ambiguous-scope triggers.

2. **Approval request contract**
   - required context;
   - proposed action;
   - evidence basis;
   - expected impact;
   - risk rating;
   - policy reason;
   - output destination;
   - reviewer role requirement.

3. **Approval record**
   - reviewer identity;
   - decision;
   - scope;
   - conditions;
   - expiration;
   - rationale;
   - customer authorization reference where required.

4. **PEP verification**
   - approval exists;
   - approval is valid;
   - approval matches execution request;
   - approval has not expired;
   - execution parameters do not exceed approved scope.

5. **Audit and assurance**
   - approval request logged;
   - policy decision logged;
   - reviewer decision logged;
   - execution result logged;
   - evidence references preserved;
   - replay and reconstruction supported.

## Minimum Metadata

Where applicable, approval events should carry or reference:

- `tenant_id`;
- `customer_id`;
- `case_id`;
- `incident_id`;
- `workflow_id`;
- `agent_id`;
- `user_id` or service identity;
- `reviewer_id`;
- `reviewer_role`;
- `requested_action`;
- `action_category`;
- `risk_level`;
- `tool_id`;
- `source_system_id`;
- `destination_system_id`;
- `output_destination`;
- `data_classification`;
- `sensitivity_label`;
- `evidence_object_ids`;
- `knowledge_store_or_memory_scope`;
- `retrieved_context_scope`;
- `policy_decision`;
- `approval_required`;
- `approval_record_id`;
- `customer_authorization_reference`;
- `approval_expiration`;
- `audit_reference_id`;
- `correlation_id`.

## Acceptance Criteria

A human-approved sensitive action implementation is acceptable when:

- sensitive actions are classified before execution;
- policy determines when approval is required;
- approval requests include enough context for informed review;
- approvals are recorded with reviewer identity, scope, conditions, and timestamp;
- approvals are bounded to tenant, customer, case, workflow, action, parameters, and time window where applicable;
- customer authorization is required where service agreements, legal requirements, or impact require it;
- the PEP blocks execution without a valid matching approval;
- high-risk actions cannot execute through agent self-approval;
- evidence-sensitive decisions preserve provenance and chain of custody;
- outputs are validated before customer-facing release;
- all approval, denial, escalation, and execution events are auditable and replayable.

## Non-Goals

This pattern does not:

- require human approval for every low-risk read-only action;
- replace policy decisioning or PEP enforcement;
- replace incident command authority;
- replace customer contractual requirements;
- make AI-generated analysis automatically trustworthy;
- remove human accountability;
- define a vendor-specific approval system;
- require AI assistance for manual DFIR workflows.

## Related Architecture Views

This pattern complements:

- `governed-agentic-security-operations-pattern.md` — defines the broader governed agentic security operations pattern.
- `policy-enforced-tool-use-pattern.md` — defines how tools are accessed through PDP/PEP controls.
- `control-loop.md` — defines runtime execution governance.
- `layered-architecture.md` — defines the operating layers.
- shared operating boundary visuals — define non-negotiable controls across service models.

## Summary

The Human-Approved Sensitive Action Pattern ensures that sensitive agentic actions cannot proceed solely because an agent proposed them.

The pattern supports MSSP, MDR, SOC / Incident Response, DFIR, and Private / Local LLM-assisted DFIR where applicable by requiring policy-triggered approval, qualified human review, customer authorization where required, PEP-enforced execution, evidence-aware validation, and complete auditability.

The core principle is:

> Agents may recommend sensitive actions, but sensitive actions execute only after policy evaluation, qualified approval where required, scoped enforcement, and auditable validation.
