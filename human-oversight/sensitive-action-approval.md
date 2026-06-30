# Sensitive Action Approval

## Purpose

This file defines approval requirements for sensitive actions in governed Agentic MSSP / MDR / DFIR security operations.

Sensitive action approval ensures that high-impact, privileged, destructive, externally visible, customer-impacting, evidence-affecting, or policy-gated actions are not executed, released, routed, or treated as authorized without explicit, scoped, auditable approval.

Sensitive action approval does not replace PDP authorization, PEP enforcement, Agent Judge assurance, analyst review, customer approval, evidence authority, incident command authority, or forensic certification.

## Scope

This file applies to sensitive actions involving:

- Containment, isolation, blocking, disabling, quarantine, credential reset, access revocation, or equivalent response activity.
- Remediation, eradication, recovery, deletion, rollback, configuration change, or privileged operational change.
- Customer-facing reports, customer notifications, externally visible summaries, executive updates, or governance evidence.
- Evidence collection, evidence export, evidence release, evidence deletion, evidence transformation, or chain-of-custody-sensitive handling.
- DFIR conclusions, timelines, root-cause statements, impact statements, attribution-sensitive language, or final report content.
- Policy exceptions, break-glass handling, cross-tenant activity, cross-customer activity, shared context, or emergency operational action.
- Tool requests, MCP-mediated access, data ingestion, retrieval, memory, and downstream use where sensitive action approval is required.
- Private/local LLM-assisted DFIR workflows that affect reportable conclusions, evidence handling, or customer-facing outputs.

This file does not define PDP decision logic, PEP implementation behavior, Agent Judge scoring, customer approval workflow design, evidence repository internals, or incident command procedures.

## Non-Goals

Sensitive action approval MUST NOT be used to:

- Treat an agent recommendation as authorization to execute.
- Treat an Agent Judge finding as approval.
- Treat analyst review as formal approval unless a formal approval workflow explicitly provides that authority.
- Treat customer-facing release readiness as customer approval.
- Treat tool registration, tool permissioning, tool risk categorization, tool-call logging, or tool success as approval.
- Override a PDP `DENY` unless routed through a separately governed exception process explicitly permitted by policy.
- Permit agents, tools, workflows, or models to approve their own sensitive actions.
- Treat private/local LLM execution as proof of correctness, tenant safety, customer safety, or forensic validity.

## Sensitive Action Approval Principles

| Principle | Requirement |
|---|---|
| Explicit approval | Sensitive action approval MUST be represented as structured workflow state, not implied by comments or informal communication. |
| Scoped approval | Approval MUST apply only to the specific tenant, customer, case, action, evidence set, tool, output destination, validity period, and conditions. |
| Authority validation | Approver identity and authority scope MUST be validated before execution, release, routing, or downstream use. |
| Customer boundary | Customer approval MUST remain separate from internal approval when customer-facing release, evidence release, or customer-impacting action requires customer authorization. |
| PDP/PEP separation | PDP authorization and PEP enforcement MUST remain separate from human approval records. |
| Evidence-bound decision | Approval for DFIR conclusions, containment, evidence handling, governance evidence, or customer-facing output MUST reference supporting evidence. |
| Retrieval and memory boundary | Approval MUST preserve retrieval and memory scope when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context influences the request. |
| Expiring approval | Sensitive action approval MUST include expiration, validity, or revalidation boundaries where scoped approval is used. |
| Fail closed | Missing, expired, revoked, ambiguous, unauthorized, stale, inconsistent, unauditable, or out-of-scope approval context MUST block the workflow. |
| Auditability | Approval decisions, denials, conditions, revocations, escalations, exceptions, execution attempts, and downstream use MUST be auditable. |

## Sensitive Action Categories

| Category | Examples | Minimum Approval Handling |
|---|---|---|
| `CONTAINMENT_ACTION` | Isolate host, disable account, block IP/domain, quarantine file, revoke token, reset credential | PDP/PEP gating, approver authority validation, blast-radius context, rollback context, audit. |
| `REMEDIATION_ACTION` | Delete artifact, change configuration, remove persistence, update access, apply recovery step | Approval scope, operational impact, rollback/recovery context, evidence support, audit. |
| `CUSTOMER_FACING_RELEASE` | Customer report, executive summary, customer notification, external update | Evidence support, output destination validation, human review, customer approval where required, audit. |
| `EVIDENCE_HANDLING_ACTION` | Evidence export, release, deletion, transformation, legal hold change, chain-of-custody-sensitive action | Evidence object IDs, evidence attribution, authority validation, retention context, audit. |
| `DFIR_CONCLUSION_ACTION` | Root cause, scope, impact, timeline, exfiltration assessment, final conclusion | DFIR lead/examiner validation, evidence support, uncertainty handling, customer approval where required. |
| `PRIVILEGED_ACCESS_ACTION` | Admin access, break-glass access, scoped credential use, customer environment access | Least privilege, approval scope, expiration, token/role boundary, audit. |
| `CROSS_BOUNDARY_ACTION` | Cross-tenant, cross-customer, cross-case, shared context, aggregated reporting | Explicit authorization, tenant/customer validation, policy gating, fail-closed handling. |
| `RETRIEVAL_MEMORY_ACTION` | Use or reuse retrieved context, case memory, vector index, RAG result, evidence retrieval | `knowledge_store_or_memory_scope`, `knowledge_memory_scope_result`, freshness, retention, reuse validation. |
| `EXCEPTION_OR_BREAK_GLASS` | Emergency deviation from standard approval or policy path | Emergency justification, scoped authority, expiration, compensating controls, post-event review, audit. |

## Required Sensitive Action Approval Inputs

Sensitive action approval workflows MUST receive enough context to support accountable authorization.

| Input | Requirement | Purpose |
|---|---|---|
| `sensitive_action_request_id` | MUST | Unique identifier for the sensitive action approval request. |
| `workflow_id` | MUST | Identifies the originating workflow, run, case, or process. |
| `workflow_stage` | MUST when routing or authority depends on stage | Identifies triage, investigation, DFIR, containment, reporting, closure, approval, exception, or customer-release stage. |
| `requested_action` | MUST | Describes the proposed action, release, recommendation, evidence handling, escalation, exception, or downstream use. |
| `sensitive_action_category` | MUST | Classifies the sensitive action type. |
| `action_risk_level` | MUST | Classifies operational, customer, evidence, legal, or governance risk. |
| `requester_identity` | MUST | Identifies the human, agent, workflow, service, or process requesting approval. |
| `requester_authority_context` | MUST when requester authority affects routing or approval | Identifies requester role, team, tenant authorization, and case relationship. |
| `agent_id` | MUST when an agent generated, influenced, routed, or consumed the requested action | Identifies the associated agent. |
| `agent_session_id` or `run_id` | MUST when an agent generated, influenced, routed, or consumed the requested action | Supports replay and run-level traceability. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` or `incident_id` | MUST when the action relates to an investigation, alert, incident, ticket, or DFIR matter | Links approval to the governed operational record. |
| `workspace_id` | MUST when workspace scope affects telemetry, evidence, action, routing, or downstream use | Preserves SIEM, XDR, cloud, or logging workspace context. |
| `subscription_id`, `account_id`, or `project_id` | MUST when cloud account scope affects the action | Preserves cloud account, subscription, or project boundary. |
| `evidence_object_ids` | MUST when the action relies on evidence, investigation context, DFIR findings, governance evidence, or customer-facing content | Preserves evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context affects the approval request | Defines approved retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| `data_classification` | MUST when classification affects approval, routing, release, reuse, evidence handling, or downstream use | Preserves data-handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when use is constrained to workflow, case, customer, legal, governance, evidence-handling, reporting, or DFIR purposes | Defines permitted downstream use. |
| `retention_policy_id` | MUST when retention affects evidence, retrieved context, output storage, release, reuse, or disposal | Preserves retention boundary. |
| `output_destination` | MUST when release, routing, disclosure, reporting, evidence handling, governance evidence, or downstream use depends on destination | Identifies where output is sent, stored, released, displayed, or consumed. |
| `policy_decision_reference` | MUST when approval is triggered by PDP result or policy obligation | Links approval to policy context. |
| `approval_reason` | MUST | Explains why sensitive action approval is required. |
| `blast_radius_context` | MUST when action can affect systems, identities, workloads, tenants, customers, evidence, or service availability | Describes operational impact and affected scope. |
| `rollback_or_recovery_context` | MUST when action is reversible, partially reversible, or requires mitigation planning | Supports recovery planning and approval conditions. |
| `human_review_record_id` | MUST when human review is required or completed | Links approval to the human review outcome. |
| `approval_record_id` | MUST when formal approval is required or completed | Links approval to approval state, scope, approver, timestamp, and expiration. |
| `customer_approval_record_id` | MUST when customer-side approval is required or completed | Links approval to customer authorization. |
| `audit_reference_id` | MUST when approval is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, review, approval, customer approval, and audit records. |

## Approval Decision Outcomes

Sensitive action approval workflows MUST define explicit outcomes.

| Outcome | Meaning |
|---|---|
| `SENSITIVE_ACTION_APPROVED` | The action is approved only within the recorded scope, conditions, and validity boundary. |
| `SENSITIVE_ACTION_REJECTED` | The action is not approved and MUST NOT proceed under the current request. |
| `SENSITIVE_ACTION_REQUEST_MORE_EVIDENCE` | Additional evidence or context is required before approval can be considered. |
| `SENSITIVE_ACTION_ESCALATE` | The request requires higher authority, customer approver, DFIR lead, incident commander, legal/compliance/privacy function, or governance review. |
| `SENSITIVE_ACTION_APPROVED_WITH_CONDITIONS` | The action may proceed only if recorded conditions and scope limits are satisfied. |
| `SENSITIVE_ACTION_ROUTE_TO_CUSTOMER_APPROVAL` | The action requires customer-side approval before proceeding. |
| `SENSITIVE_ACTION_EXPIRED` | The approval request or prior approval is no longer valid. |
| `SENSITIVE_ACTION_REVOKED` | A previously granted approval is withdrawn before execution or continued use. |
| `SENSITIVE_ACTION_BLOCKED_FAIL_CLOSED` | The workflow is blocked because required context, evidence, approval, review, authority, policy, or auditability is missing or invalid. |

Approval outcomes are human authorization states only when produced by an authorized approval workflow. They MUST NOT be represented as PDP authorization decisions by themselves.

## Required Approval Attributes

Every sensitive action approval decision MUST include:

| Attribute | Requirement | Purpose |
|---|---|---|
| `approval_record_id` | MUST | Unique identifier for the approval decision. |
| `sensitive_action_request_id` | MUST | Links approval to the sensitive action request. |
| `decision_outcome` | MUST | Records the explicit approval outcome. |
| `approval_status` | MUST | Records pending, approved, rejected, expired, revoked, escalated, conditional, or blocked_fail_closed state. |
| `approver_identity` | MUST | Identifies the approving or rejecting human authority. |
| `approver_role` | MUST | Identifies the approver function or responsibility. |
| `approver_authority_scope` | MUST | Records or references the approver authority scope. |
| `decision_timestamp` | MUST | Records when the decision occurred. |
| `decision_rationale` | MUST | Explains the basis for the decision. |
| `approved_scope` | MUST | Defines tenant, customer, case, action, evidence, tool, output, destination, and validity boundaries. |
| `approval_valid_until` | MUST where scoped approval is used | Defines expiration. |
| `conditions` | MUST when approval is conditional | Records required conditions or limits. |
| `evidence_references_reviewed` | MUST when evidence supports the action | Records evidence considered by the approver. |
| `knowledge_store_or_memory_scope` | MUST when retrieval or memory affects approval | Records retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse scope. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval and memory remained within approved boundaries. |
| `data_classification` | MUST when classification affects approval or release | Records classification context. |
| `sensitivity_label` | MUST when applicable | Records sensitivity, privacy, legal, or customer-specific label context. |
| `allowed_use` | MUST when use is constrained | Records permitted downstream use. |
| `retention_policy_id` | MUST when retention affects the approved item | Records retention and disposal boundary. |
| `human_review_record_id` | MUST when human review is required or completed | Links approval to the human review outcome. |
| `customer_approval_record_id` | MUST when customer-side approval is required or completed | Links approval to customer authorization. |
| `policy_decision_reference` | MUST when approval is triggered by PDP result or policy obligation | Links approval to PDP context. |
| `audit_event_id` or `audit_reference_id` | MUST | Links the decision to the audit trail. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, review, approval, customer approval, and audit records. |

## PEP/PDP Relationship

Sensitive action approval does not replace policy enforcement.

| PDP Result | Sensitive Action Approval Handling |
|---|---|
| `ALLOW` | Workflow MAY proceed only if no separate sensitive action approval, human review, customer approval, evidence, or destination requirement applies. |
| `REQUIRE_APPROVAL` | Workflow MUST remain blocked until valid sensitive action approval exists within scope. |
| `DENY` | Workflow MUST fail closed. Escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default. |

The PEP MUST enforce the PDP decision and returned obligations. If sensitive action approval context, approval scope, approver authority, customer approval, or audit logging cannot be verified where required, the workflow MUST fail closed.

The PEP or workflow gate MUST revalidate approval status, scope, expiration, approver authority, conditions, and required customer approval before execution or release.

## Customer Approval Boundary

Customer approval MUST be required when the sensitive action affects customer-facing release, customer evidence release, customer-owned operational risk, externally visible recommendations, contractual escalation, customer notification, or customer-impacting containment/remediation.

Customer approval MUST preserve:

- customer identity,
- tenant context,
- case or incident scope,
- evidence references,
- knowledge store or memory scope where applicable,
- data classification,
- sensitivity label,
- allowed use,
- retention policy,
- output destination,
- requested action or release,
- customer approver identity,
- customer approval record,
- expiration or validity boundary where applicable,
- audit reference.

Customer approval MUST NOT be assumed from informal communication, ticket comments, prior discussion, general awareness, or engagement participation unless the operating model explicitly permits that form of authorization and captures it in the audit trail.

## Sensitive Action Execution Boundary

Sensitive action approval is a precondition for execution where required. It is not the execution mechanism.

Before execution or release, the governed workflow, PEP, or execution gate MUST verify:

- valid approval outcome,
- approval scope,
- approval expiration,
- approver authority,
- required customer approval,
- PDP decision and obligations,
- PEP enforcement path,
- tenant, customer, case, evidence, and destination scope,
- knowledge store or memory scope where applicable,
- evidence support,
- data classification, sensitivity label, allowed use, and retention policy,
- audit logging.

If any required verification fails, execution or release MUST NOT proceed.

## Private / Local LLM-Assisted DFIR Approval

For private/local LLM-assisted DFIR workflows, sensitive action approval is required when:

- Model output affects reportable DFIR conclusions.
- Evidence export, release, deletion, transformation, or customer-facing use is involved.
- Timeline reconstruction, root cause, scope, impact, attribution-sensitive statements, or final report content is involved.
- Knowledge store or memory scope is missing, stale, cross-customer, cross-tenant, cross-case, or retention-inconsistent.
- Legal-sensitive output, governance evidence, or customer-facing release is involved.
- Customer approval is required for report release, evidence handling, or customer-impacting response.

Private/local execution does not make model output authoritative. It only changes where processing occurs. Examiner validation, evidence review, sensitive action approval, and required customer approval paths still apply.

## Fail-Closed Conditions

Sensitive action approval workflows MUST fail closed, remain blocked, or route to controlled review when:

- Required sensitive action approval is missing, expired, revoked, incomplete, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope.
- Approver identity, role, authority scope, decision rationale, approval scope, approval expiration, or decision outcome is missing, ambiguous, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required tenant, customer, workspace, case, evidence, destination, review, approval, customer approval, or policy context is missing, conflicting, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, or retention policy is missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where sensitive action approval, customer-facing release, DFIR conclusions, governance evidence, approval routing, execution, or downstream use depends on it.
- Evidence references are missing for material investigative, DFIR, governance, approval, or customer-facing output.
- Material claims are unsupported or contradicted by evidence.
- Agent Judge findings identify unresolved unsupported claims, tenant-boundary risk, evidence insufficiency, output-quality risk, or HITL non-compliance.
- PDP returns `DENY`; escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution by default.
- PDP returns `REQUIRE_APPROVAL` and valid approval is not present.
- Customer approval is required but missing, expired, revoked, incomplete, ambiguous, unauditable, or out of scope.
- Tool output, agent output, or model output attempts to imply approval, execution, containment success, closure, legal determination, forensic proof, or customer notification without governed workflow context.
- Audit logging or context preservation fails.
- The approval package cannot distinguish facts from model-generated inference.

Fail-closed handling MUST preserve the request context, evidence references, approval reason, routing reason, authority context, approval context where applicable, customer approval context where applicable, and audit reference.

## Audit Requirements

Sensitive action approval workflows MUST audit:

- Sensitive action request identifier.
- Approval record identifier.
- Requested action, sensitive action category, risk level, outcome, and rationale.
- Requester identity and authority context.
- Approver identity, role, and authority context.
- Tenant, customer, workspace, case, incident, alert, and service-tower context.
- Agent identity, session identity, workflow identity, and initiating user or system.
- Evidence references and evidence tenant/customer attribution metadata.
- `knowledge_store_or_memory_scope` where retrieval or memory influenced approval, evidence interpretation, routing, customer-facing wording, governance evidence, approval package, DFIR conclusions, execution, or downstream use.
- `knowledge_memory_scope_result` where retrieval or memory scope was evaluated.
- `data_classification`, `sensitivity_label`, `allowed_use`, and `retention_policy_id` where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, execution, or DFIR conclusions are involved.
- Agent Judge findings considered during approval.
- PEP/PDP decision and obligations, where applicable.
- `human_review_record_id`, `approval_record_id`, and `customer_approval_record_id` where review, formal approval, or customer approval is required or completed.
- Output destination and approved audience.
- Approval timestamp, expiration, revocation, conditions, correlation identifier, and workflow step.
- Escalation reason, rejection reason, request-more-evidence reason, or fail-closed reason.
- Execution attempt following approval, where applicable.
- Mismatch between approval scope and requested execution, where applicable.
- Known limitations or unresolved uncertainty.

If the workflow cannot create the required audit record, the sensitive action approval workflow MUST remain blocked until the issue is reviewed or remediated.

## Operational Anti-Patterns

Avoid the following:

- Treating an agent recommendation as approval to execute.
- Treating Agent Judge output as approval.
- Treating analyst review as sensitive action approval without an approval workflow.
- Treating policy evaluation as human authorization.
- Treating approval as reusable across tenants, customers, cases, evidence sets, destinations, or time windows.
- Treating customer-facing release readiness as customer approval.
- Executing sensitive actions after PDP `DENY` outside a separately governed exception process.
- Allowing agents, tools, or workflows to approve their own sensitive actions.
- Allowing missing approval records to default to execution or release.
- Releasing customer-facing content without required evidence, review, approval, and customer approval where applicable.
- Approving DFIR conclusions based only on model output.
- Using local/private LLM execution as a reason to skip DFIR validation.
- Treating Entra Agent ID, agent registry, identity governance, or lifecycle controls as operational SOC agents.

## Acceptance Criteria

This file is acceptable when:

- Sensitive action approval is explicit, scoped, attributable, expiring where applicable, and auditable.
- Sensitive action approval remains separate from Agent Judge assurance, PEP/PDP enforcement, analyst review, customer approval, tool execution, evidence authority, and forensic certification.
- Sensitive action approval records preserve tenant, customer, case, evidence, destination, review, approval, and customer approval boundaries.
- Sensitive action approval records preserve `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result` where retrieval or memory affects approval or downstream use.
- Sensitive action approval records preserve data classification, sensitivity label, allowed use, and retention policy where sensitive data handling, release, reuse, customer-facing output, governance evidence, approval routing, execution, or DFIR conclusions are involved.
- Valid approval or customer approval is required before customer-facing release, customer-impacting action, evidence release, or externally visible output where required.
- The PEP or workflow gate revalidates approval status, scope, expiration, approver authority, conditions, customer approval, and audit logging before execution or release.
- Fail-closed handling exists for missing context, unsupported claims, invalid approvals, unauthorized approvers, unresolved retrieval/memory scope, scope mismatch, and audit failures.
- Audit replay can reconstruct requester identity, approver identity, approver authority, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, human review record, approval record, customer approval record, decision rationale, approval outcome, routing, execution attempt, and downstream use.
