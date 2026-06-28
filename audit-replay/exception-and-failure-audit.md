# Exception and Failure Audit

## Purpose

This document defines how exceptions, denials, failures, failed control checks, and fail-closed outcomes are audited across governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

Exception and failure audit records are required because blocked actions, denied requests, incomplete approvals, missing evidence, tenant-boundary violations, failed tool calls, and unsafe fleet releases are often as important as successful execution records.

The goal is to make failure behavior reviewable, correlated, and operationally useful without weakening tenant isolation, evidence integrity, policy enforcement, human accountability, or audit replay.

## Scope

This file applies when a governed workflow cannot proceed as requested, proceeds only after exception handling, or produces an abnormal result that requires review.

In scope:

- policy denials;
- fail-closed events;
- missing or invalid tenant, customer, case, evidence, identity, approval, or policy context;
- schema validation failures;
- agent lifecycle, package, or version eligibility failures;
- context assembly and retrieval failures;
- AI assurance failures and unsupported-claim findings;
- tool request, execution, timeout, or authorization failures;
- approval workflow failures, expirations, withdrawals, or mismatches;
- evidence access, evidence reference, chain-of-custody, or DFIR review failures;
- customer-facing output release failures;
- cross-tenant sanitized intelligence release failures;
- fleet rollout, rollback, recall, and kill-switch failures;
- monitoring and audit logging failures;
- emergency override and exception approval records.

Out of scope:

- full audit event schema definitions, which belong in `audit-event-model.md`;
- full correlation rules, which belong in `audit-correlation-model.md`;
- immutable storage and retention design, which belong in `immutable-audit-guidance.md`;
- detailed service desk implementation procedures;
- SIEM-specific query language or dashboard implementation.

## Core Principle

A governed workflow must not fail silently.

Every material exception, denial, blocked action, failed control check, failed execution, emergency override, rollback, recall, or fail-closed state must produce an audit record that can be correlated to the attempted workflow.

Exception audit must answer:

1. What was attempted?
2. Who or what attempted it?
3. Which tenant, customer, case, evidence set, tool, policy, approval, agent, version, package, or release was involved?
4. Which control failed, denied, blocked, expired, escalated, or required review?
5. What happened next?
6. Was the workflow stopped, retried, escalated, approved by exception, rolled back, recalled, or recovered?
7. Can the event be replayed without exposing data outside the authorized boundary?

## Exception and Failure Categories

| Category | Description | Example |
|---|---|---|
| Policy denial | PDP denies the requested action or release. | Agent requests endpoint isolation outside approved scope. |
| Fail-closed control event | Workflow stops because required control context is missing or invalid. | Tenant ID is missing from a tool request. |
| Approval failure | Required approval is missing, expired, withdrawn, mismatched, or unauthorized. | Endpoint containment approval expired before execution. |
| Identity or lifecycle failure | Actor, agent, package, tool, or service identity is invalid or not eligible. | Agent package is recalled but still invoked. |
| Tenant or case boundary failure | Request crosses tenant, customer, case, evidence, or destination-scope boundary. | Retrieval attempts to include another customer case. |
| Evidence failure | Required evidence reference, chain-of-custody link, or source support is missing or invalid. | DFIR finding lacks source artifact reference. |
| AI assurance failure | Agent output fails evidence support, unsupported-claim, output-quality, or boundary checks. | Customer report draft includes unsupported conclusion. |
| Tool execution failure | Tool call fails, times out, returns partial result, or executes outside expected response pattern. | Identity tool rejects scoped execution token. |
| Output release failure | Internal or customer-facing output cannot be released because review, evidence, approval, or scope is invalid. | Customer notification lacks required approval. |
| Fleet rollout failure | Package rollout, canary, cohort expansion, rollback, or recall fails a release gate. | New detection package causes unexpected alert volume. |
| Sanitized intelligence failure | Cross-tenant release fails sanitization, destination eligibility, or recall validation. | Sanitized item still contains indirect customer identifiers. |
| Audit failure | Audit logging, correlation, storage, sequencing, or replay support is unavailable or incomplete. | Sensitive action cannot be logged. |
| Emergency override | Authorized emergency action bypasses the normal timing or sequence but remains scoped and audited. | Kill switch invoked to stop a compromised agent version. |

## Required Audit Behavior

Exception and failure records must be created when a governed workflow changes state because a required control failed, denied, blocked, escalated, or required exception handling.

Minimum required behavior:

- create an audit event for the attempted action;
- record the failing control, condition, or decision;
- preserve tenant, customer, case, agent, tool, evidence, policy, approval, package, and release references where applicable;
- record whether the workflow stopped, retried, escalated, failed closed, required approval, or entered emergency handling;
- link the failure record to the same `correlation_id` as the attempted workflow;
- record the actor that attempted the action and the component that blocked or failed it;
- preserve enough detail to support replay, review, governance, and root-cause analysis;
- avoid exposing raw customer data, evidence content, or source-tenant context to unauthorized scopes.

## Exception Severity

Exception severity should be based on operational impact, tenant-boundary risk, evidence impact, customer impact, tool risk, and whether the workflow failed safely.

| Severity | Meaning | Required Handling |
|---|---|---|
| Informational | Workflow did not proceed as requested, but no control failure or customer impact occurred. | Record for traceability and metrics. |
| Low | Recoverable issue with no sensitive action, no evidence impact, and no customer-facing impact. | Record, retry where safe, and monitor trend. |
| Medium | Workflow blocked or degraded because required context, policy, approval, evidence, or tool state was incomplete. | Record, route to owner or analyst review, and prevent silent retry loops. |
| High | Sensitive action, customer-facing output, DFIR conclusion, tenant boundary, or privileged tool path was blocked or failed. | Fail closed, escalate, preserve audit, and require authorized review. |
| Critical | Cross-tenant exposure risk, compromised agent identity, unsafe fleet release, evidence integrity risk, or audit failure affecting sensitive action. | Halt affected workflow, trigger incident or emergency process, preserve evidence, and consider rollback or recall. |

Severity is not authorization. A severity label supports routing, escalation, and reporting. It does not allow a denied action to proceed.

## Baseline Exception Audit Fields

Exception audit records should use the common audit event model and include the following fields where applicable.

| Field | Requirement | Purpose |
|---|---|---|
| `exception_id` | Required | Unique identifier for the exception or failure record. |
| `audit_event_id` | Required | Audit event that records the exception. |
| `event_type` | Required | Normalized event type, such as `exception.fail_closed` or `tool.execution.failed`. |
| `event_time` | Required | Time the failure or exception occurred. |
| `recorded_time` | Required | Time the event was written to audit storage. |
| `correlation_id` | Required | End-to-end workflow correlation identifier. |
| `parent_event_id` | Recommended | Prior event in the attempted workflow. |
| `causation_id` | Recommended | Event, decision, missing field, failed check, or error that caused the exception. |
| `tenant_id` | Conditional | Required when tenant-scoped data, tools, cases, outputs, packages, or releases are involved. |
| `customer_id` | Conditional | Required when customer-scoped service delivery is involved. |
| `case_id` | Conditional | Required when an incident, investigation, ticket, or DFIR case is involved. |
| `actor` | Required | Human, agent, system, tool, workflow, policy component, or fleet service involved. |
| `attempted_action` | Required | Action, release, retrieval, approval, tool call, or workflow step that was attempted. |
| `failure_category` | Required | Normalized category, such as `policy_denial`, `missing_approval`, or `tenant_boundary_failure`. |
| `failed_control` | Required | Control, gate, policy, schema, tool, approval, validation, monitor, or boundary that failed. |
| `failure_reason` | Required | Human-readable reason suitable for review and triage. |
| `decision` | Conditional | PDP decision when policy evaluation occurred. |
| `workflow_state` | Required | Resulting state such as `stopped`, `failed_closed`, `retry_pending`, `escalated`, `rolled_back`, or `recalled`. |
| `severity` | Required | Operational severity. |
| `evidence_refs` | Conditional | Evidence references involved in the attempted workflow. |
| `policy_refs` | Conditional | Policy request, decision, bundle, rule, or control reference. |
| `approval_refs` | Conditional | Approval request, approval decision, approver, expiration, or denial reference. |
| `tool_refs` | Conditional | Tool request, tool contract, execution token, or execution result reference. |
| `package_refs` | Conditional | Agent, prompt, model route, policy bundle, detection, playbook, or report-template package reference. |
| `release_refs` | Conditional | Fleet rollout, rollback, recall, or sanitized intelligence release reference. |
| `remediation` | Recommended | Required follow-up, owner, deadline, and recovery state. |
| `integrity` | Recommended | Audit integrity, retention, and immutability metadata where supported. |

## Normalized Failure States

Exception records should use consistent workflow states.

| State | Meaning |
|---|---|
| `blocked` | Control prevented the request from proceeding. |
| `denied` | PDP denied the request. |
| `failed_closed` | Workflow stopped because required control context was missing, invalid, or unavailable. |
| `requires_review` | Workflow requires analyst, service-owner, customer, legal, or security review. |
| `requires_approval` | Workflow requires accountable approval before proceeding. |
| `retry_pending` | Retry is allowed after a bounded, controlled wait or remediation. |
| `retry_exhausted` | Allowed retry budget was exhausted. |
| `escalated` | Workflow was routed to a higher authority or specialized team. |
| `exception_approved` | A scoped exception was approved by an accountable authority. |
| `partially_completed` | Some steps completed, but the workflow did not reach the intended final state. |
| `rolled_back` | Previous safe state was restored. |
| `recalled` | A package, release, detection, playbook, prompt, or intelligence item was removed or disabled. |
| `quarantined` | Data, output, memory, package, or release was isolated from further use. |
| `unresolved` | Final disposition is not yet known. |
| `recovered` | Workflow returned to a valid state after remediation. |

## Fail-Closed Audit Requirements

Fail-closed events must be explicit. They must not be hidden as generic errors.

A fail-closed audit event is required when a workflow is stopped because any required control cannot be validated.

Examples:

- tenant ID is missing, ambiguous, mismatched, or unauthorized;
- customer or case scope is missing where required;
- evidence reference is missing for a sensitive action, DFIR finding, or customer-facing conclusion;
- agent identity is unknown, suspended, expired, retired, or outside lifecycle state;
- agent package is unsigned, unapproved, recalled, or not tenant-eligible;
- requested tool is unregistered or outside the allowed tool contract;
- policy engine is unavailable;
- policy decision cannot be reached;
- approval state is missing, expired, or invalid;
- execution token is missing, expired, invalid, or outside scope;
- audit logging is unavailable for a sensitive action;
- rollback or recall path is missing for a fleet release;
- shared-memory write path lacks approved release metadata.

Required fail-closed fields:

| Field | Purpose |
|---|---|
| `failed_control` | Identifies the control that forced fail-closed handling. |
| `missing_or_invalid_context` | Lists required context that was absent, invalid, stale, or mismatched. |
| `attempted_action` | Describes the action that was blocked. |
| `scope` | Captures tenant, customer, case, evidence, package, or release scope where applicable. |
| `policy_state` | Records whether policy was evaluated, unavailable, denied, or incomplete. |
| `approval_state` | Records approval status when required. |
| `workflow_state` | Must indicate `failed_closed`. |
| `next_action` | Records escalation, remediation, retry, or closure path. |

## Policy Denial Audit

Policy denials are expected control outcomes and must be auditable.

A policy denial audit event should capture:

- policy request identifier;
- PDP decision identifier;
- policy bundle or rule reference;
- requested action, tool, operation, and target;
- agent identity, package version, and lifecycle state;
- tenant, customer, case, and evidence scope;
- denial reason;
- whether the denial is final or can be resubmitted with corrected context;
- whether the denial requires analyst, service-owner, security, legal, or customer review;
- whether the denial indicates a policy defect, attempted misuse, configuration issue, or expected boundary enforcement.

A denied request must not be retried automatically unless the retry condition is explicitly allowed, bounded, and audited.

## Approval Failure Audit

Approval failures must be recorded separately from policy denials.

Common approval failure conditions:

| Condition | Audit Requirement |
|---|---|
| Approval missing | Record required approver role, requested action, and blocked workflow state. |
| Approval expired | Record expiration time, attempted execution time, and decision linkage. |
| Approval withdrawn | Record withdrawal decision, actor, reason, and affected workflow. |
| Wrong approver | Record required approver role and actual actor or role mismatch. |
| Approval scope mismatch | Record approved scope and attempted scope. |
| Customer approval missing | Record customer approval requirement and blocked output or action. |
| Emergency approval used | Record emergency authority, scope, time limit, reason, and follow-up requirement. |

Human review and formal approval must remain distinct in audit records. A review record does not authorize execution unless it is also an approval record with the required scope and authority.

## Agent and Package Failure Audit

Agent and package failures must be audited when they affect execution, output trust, tool access, fleet rollout, or tenant eligibility.

Required audit cases:

- unregistered agent attempts invocation;
- agent lifecycle state is suspended, retired, recalled, or disabled;
- agent package is unsigned, tampered, unapproved, not active, or not eligible for the tenant;
- prompt package, model route, tool contract, retrieval configuration, or policy bundle version is missing or incompatible;
- package rollback target is missing;
- agent attempts to request a prohibited tool or operation;
- agent attempts to write to shared memory without approval;
- agent output exceeds allowed action, tenant, case, or evidence scope.

Agent failure records should include:

| Field | Purpose |
|---|---|
| `agent_id` | Agent identity involved. |
| `agent_package_id` | Versioned package involved. |
| `lifecycle_state` | Active, suspended, retired, recalled, or unknown. |
| `owner` | Owning team or accountable function. |
| `tenant_eligibility` | Whether the agent or package was eligible for the tenant. |
| `package_integrity_state` | Signature, checksum, provenance, or validation state where applicable. |
| `blocked_capability` | Tool, retrieval source, memory write, output release, or package action blocked. |

## Context Assembly and Retrieval Failure Audit

Context assembly failures must be audited when an agent, judge, policy decision, approval, report, or tool action depends on assembled context.

Common failure conditions:

- missing tenant filter;
- missing case scope;
- retrieval result includes another tenant, customer, case, or evidence boundary;
- source evidence reference is missing;
- shared knowledge is mixed with customer evidence without classification;
- untrusted content is not labeled;
- data minimization fails;
- restricted data is included in prompt context;
- retrieval corpus returns recalled, stale, quarantined, or ineligible intelligence;
- prompt context includes secrets, credentials, tokens, or privileged material.

Required response:

- block agent invocation or downstream use;
- quarantine invalid context package where appropriate;
- record the context package identifier;
- record source and destination scope;
- record failed boundary condition;
- preserve enough metadata for investigation without exposing raw data outside the authorized scope.

## AI Assurance Failure Audit

AI assurance failures must be recorded when agent outputs do not meet required quality, evidence, boundary, or review conditions.

Examples:

- unsupported claim detected;
- evidence reference missing or invalid;
- confidence unsupported by evidence;
- hallucination-like content identified;
- tenant boundary risk detected;
- customer-facing language fails review criteria;
- ATT&CK or ATLAS mapping is unsupported;
- response recommendation contains sensitive action risk;
- output quality score below release threshold;
- judge output is missing, invalid, or unavailable where required.

AI assurance failure records should link:

- agent output reference;
- judge or assurance check reference;
- evidence references reviewed;
- unsupported claims or failed check types;
- recommended routing;
- policy request or output release affected;
- reviewer or approver required.

Agent Judge output is advisory and policy-consumable. It is not an approval decision or tool authorization.

## Tool Execution Failure Audit

Tool execution failures must be recorded when a mediated tool request cannot be executed as authorized, executes partially, produces an error, or returns unexpected output.

Common failure conditions:

| Failure | Required Audit Detail |
|---|---|
| Tool not registered | Tool identifier, requested operation, requesting agent, and blocked state. |
| Operation outside contract | Contract version, allowed operation set, requested operation, and denial reason. |
| Execution token invalid | Token ID, validation failure reason, expiration, scope mismatch, or signature failure. |
| Target mismatch | Approved target versus attempted target. |
| Permission denied by downstream system | Downstream system, operation, target, and response code or reason. |
| Timeout | Timeout threshold, retry count, idempotency state, and final status. |
| Partial execution | Completed sub-actions, failed sub-actions, affected entities, and recovery requirement. |
| Unexpected tool output | Output validation failure, schema mismatch, and quarantine state. |
| Tool side effect uncertainty | Whether the action may have affected a target and what verification is required. |

Sensitive tool failures must preserve the policy decision, approval record, execution token, tool contract, target entity, and execution result.

## Evidence and DFIR Failure Audit

Evidence-related failures require careful audit because they can affect forensic defensibility, customer trust, incident conclusions, and legal handling.

Audit records are required when:

- evidence reference is missing, invalid, stale, or outside case scope;
- chain-of-custody metadata is incomplete;
- evidence transformation is not recorded;
- generated finding lacks source support;
- local/private LLM output is treated as evidence rather than analysis;
- evidence access fails because of permissions, storage, or retention state;
- forensic artifact parsing fails or produces partial output;
- report conclusion cannot be traced to source evidence;
- evidence object is quarantined, sealed, held, or subject to legal restrictions;
- evidence modification or deletion is attempted outside approved process.

Required response for evidence-sensitive failures:

- stop use of the affected finding or output;
- route to forensic reviewer where applicable;
- preserve the failed evidence reference, access attempt, and transformation state;
- record whether customer-facing output or case conclusion was affected;
- prevent release until evidence support is restored or the limitation is clearly documented and approved.

## Tenant Boundary Failure Audit

Tenant and customer boundary failures must be treated as high-priority audit events.

Examples:

- retrieval attempts to access another tenant or customer;
- prompt context includes cross-tenant data;
- tool request targets an asset outside approved tenant or case scope;
- case note, report, or summary includes another customer context;
- shared memory receives raw tenant data;
- sanitized intelligence still contains source-tenant identifiers;
- fleet rollout includes an excluded tenant;
- destination tenant is not eligible for a package, detection, playbook, or shared intelligence item.

Required response:

- block the action or fail closed;
- quarantine affected context, memory entry, output, or release candidate;
- record source and attempted destination scope;
- record whether data exposure occurred or was prevented;
- escalate according to tenant-boundary incident handling procedures;
- preserve audit evidence for review and replay.

## Output Release Failure Audit

Output release failures apply to customer reports, case updates, notifications, executive summaries, detection releases, playbook updates, and internal operational outputs where release is controlled.

Release must be blocked and audited when:

- required review is missing;
- customer approval is required but absent;
- evidence support is missing;
- unsupported claims remain;
- tenant or customer scope is ambiguous;
- content includes raw evidence, privileged information, secrets, or identifiers outside authorized release scope;
- policy decision denies or requires approval;
- output references stale, recalled, or quarantined intelligence;
- release channel is not approved or not auditable.

Release failure records should include release type, intended destination, failed control, reviewer state, approval state, evidence support state, policy decision, and final workflow state.

## Fleet Rollout, Rollback, and Recall Failure Audit

Fleet failures can affect many tenants or service towers. They require explicit audit and correlation.

Audit records are required for:

- failed validation gate;
- failed package signature or provenance check;
- tenant eligibility failure;
- canary failure;
- cohort rollout failure;
- unexpected policy denial spike;
- unsupported-claim spike after rollout;
- tool error spike after rollout;
- cross-tenant boundary signal;
- unsafe response recommendation pattern;
- missing rollback target;
- rollback failure;
- recall failure;
- kill-switch activation;
- recalled package invocation attempt;
- package remains active after recall.

Fleet failure records should include:

| Field | Purpose |
|---|---|
| `release_id` | Fleet release or sanitized intelligence release identifier. |
| `rollout_id` | Rollout sequence identifier. |
| `stage` | Validation, canary, cohort, broad rollout, rollback, recall, or kill switch. |
| `package_refs` | Agent package, prompt package, policy bundle, tool contract, detection, playbook, or report-template reference. |
| `affected_scope` | Tenants, customer groups, service towers, environments, or agents affected. |
| `excluded_scope` | Tenants or groups that must not receive the release. |
| `monitoring_signal` | Metric, alert, denial spike, failure threshold, or anomaly that triggered action. |
| `rollback_target` | Known-good version or recovery target. |
| `recall_action` | Block, disable, revoke, quarantine, pin, rollback, or notify. |
| `final_state` | Rolled back, recalled, partially recalled, unresolved, or recovered. |

## Sanitized Intelligence Release Failure Audit

Cross-tenant sanitized intelligence release failures must be recorded when a release candidate, retrieval entry, detection, playbook, prompt update, report template, or agent package fails boundary or release controls.

Failure examples:

- source tenant or source case is unknown;
- source classification is missing;
- sanitization record is missing;
- direct or indirect identifiers remain;
- evidence support is insufficient;
- privileged, contractual, legal, regulated, or sovereignty-restricted context is unresolved;
- destination scope is overly broad;
- tenant eligibility check fails;
- tenant exclusion applies;
- release approval is missing;
- release channel is unregistered;
- recall or removal path is missing;
- monitoring is unavailable;
- shared memory or retrieval corpus accepts material without release metadata.

Required response:

- block release;
- quarantine the candidate item;
- record failed sanitization or policy condition;
- preserve internal source references for authorized reviewers only;
- prevent destination tenants from seeing source tenant identifiers, case identifiers, raw evidence references, or customer-specific conclusions.

## Emergency Override Audit

Emergency overrides may be necessary for safety, containment, or recall. They must remain scoped, time-bound, accountable, and auditable.

Emergency override records must include:

- override identifier;
- emergency reason;
- accountable approver or authority;
- scope of override;
- affected tenant, customer, case, agent, package, release, or tool;
- policy or workflow path overridden;
- compensating controls;
- time limit or expiration;
- required post-action review;
- final disposition;
- evidence and audit references.

Emergency override must not be used to bypass tenant isolation, evidence integrity, audit logging, or customer approval requirements without explicit documented authority and follow-up review.

## Retry and Recovery Audit

Retries must be controlled. Unbounded retry loops can create noise, duplicate actions, inconsistent case states, or repeated policy denials.

Retry audit records should include:

| Field | Purpose |
|---|---|
| `retry_allowed` | Whether retry is allowed. |
| `retry_reason` | Why retry is safe or necessary. |
| `retry_count` | Number of attempts. |
| `retry_limit` | Maximum allowed attempts. |
| `idempotency_key` | Prevents duplicate side effects. |
| `backoff_policy` | Retry timing pattern. |
| `last_failure_reason` | Most recent failure condition. |
| `recovery_owner` | Team or role responsible for recovery. |
| `final_retry_state` | Succeeded, failed, escalated, abandoned, or recovered. |

Retries must not bypass policy, approval, tenant scope, execution token validation, or audit requirements.

## Exception Handling Flow

A standard exception handling path should follow this sequence.

```text
1. Workflow attempts action, release, retrieval, approval, tool execution, or fleet change.
2. Control check, policy decision, approval validation, tool execution, evidence check, or monitoring gate fails.
3. Workflow blocks, denies, fails closed, retries within policy, or escalates.
4. Exception audit event is created.
5. Exception event is correlated to the attempted workflow.
6. Required owner, reviewer, approver, service team, or customer path is notified where needed.
7. Remediation, rollback, recall, quarantine, or recovery action occurs.
8. Final exception disposition is recorded.
9. Replay confirms the attempted action, failure reason, response, and final state.
```

## Example Exception Audit Event

The following example shows a fail-closed event for a sensitive tool action. It is an architecture record shape, not a production schema.

```json
{
  "audit_event_id": "audit-2026-05-22-000241",
  "event_type": "exception.fail_closed",
  "event_version": "1.0",
  "event_time": "2026-05-22T12:04:11Z",
  "recorded_time": "2026-05-22T12:04:13Z",
  "producer": {
    "component": "policy-enforcement-point",
    "component_version": "pep@2.4.0",
    "environment": "managed-mdr-control-plane"
  },
  "correlation": {
    "correlation_id": "corr-2026-05-22-10422",
    "parent_event_id": "audit-2026-05-22-000238",
    "causation_id": "approval-check-10422-0011",
    "workflow_id": "mdr-agent-assisted-investigation"
  },
  "scope": {
    "tenant_id": "customer-a",
    "customer_id": "cust-a",
    "case_id": "inc-10422",
    "service_tower": "mdr",
    "data_classification": "customer-security-telemetry"
  },
  "actor": {
    "actor_type": "agent",
    "actor_id": "response-recommendation-agent",
    "agent_package_id": "response-recommendation-agent@1.6.3",
    "on_behalf_of_user": "analyst-214"
  },
  "attempted_action": {
    "action_category": "sensitive_tool_execution",
    "requested_tool": "endpoint-isolation-tool",
    "requested_operation": "isolate_endpoint",
    "target_type": "endpoint",
    "target_ref": "device-123",
    "action_risk": "high"
  },
  "failure": {
    "exception_id": "exception-10422-0006",
    "failure_category": "missing_required_approval",
    "failed_control": "human_approval_validation",
    "failure_reason": "Endpoint isolation requires active approval from an authorized approver. The referenced approval record was expired.",
    "severity": "high",
    "workflow_state": "failed_closed",
    "retry_allowed": false
  },
  "references": {
    "evidence_refs": [
      "evidence://customer-a/inc-10422/events/evt-001",
      "evidence://customer-a/inc-10422/events/evt-004"
    ],
    "agent_output_ref": "agent-output://cust-a/inc-10422/out-0007",
    "judge_result_ref": "judge-result://cust-a/inc-10422/judge-0012",
    "policy_request_id": "policy-req-10422-0015",
    "policy_decision_id": "policy-decision-10422-0015",
    "approval_record_id": "approval-10422-0009",
    "tool_contract_ref": "endpoint-isolation-tool@3.1.0"
  },
  "response": {
    "next_action": "request_new_authorized_approval",
    "routed_to": "incident_commander_approval_queue",
    "customer_impacting": false,
    "tool_execution_started": false
  },
  "integrity": {
    "retention_label": "security-operations-audit",
    "audit_store": "immutable-audit-logical-store",
    "record_hash": "sha256:example"
  }
}
```

## Example Fleet Recall Failure Event

The following example shows a recall-related exception.

```json
{
  "audit_event_id": "audit-2026-05-23-000088",
  "event_type": "fleet.recall.exception",
  "event_version": "1.0",
  "event_time": "2026-05-23T09:17:42Z",
  "recorded_time": "2026-05-23T09:17:45Z",
  "producer": {
    "component": "fleet-control-plane",
    "component_version": "fleet-control@1.9.0"
  },
  "correlation": {
    "correlation_id": "corr-fleet-recall-2026-0021",
    "parent_event_id": "audit-2026-05-23-000082",
    "causation_id": "monitoring-alert-unsupported-claim-spike-0021",
    "workflow_id": "agent-package-emergency-recall"
  },
  "release": {
    "release_id": "fleet-release-2026-0021",
    "recall_id": "recall-2026-0021",
    "agent_package_id": "customer-reporting-agent@2.8.0",
    "rollback_target": "customer-reporting-agent@2.7.4",
    "stage": "emergency_recall"
  },
  "failure": {
    "exception_id": "exception-fleet-2026-0044",
    "failure_category": "partial_recall",
    "failed_control": "package-disable-confirmation",
    "failure_reason": "One eligible tenant group did not confirm package disablement within the required recall window.",
    "severity": "critical",
    "workflow_state": "escalated"
  },
  "affected_scope": {
    "included_tenant_groups": ["premium-mdr"],
    "unconfirmed_tenant_groups": ["premium-mdr-eu"],
    "excluded_tenants": ["regulated-customer-example"]
  },
  "response": {
    "next_action": "force_block_invocation_and_notify_service_owner",
    "routed_to": ["fleet-owner", "mdr-service-owner", "audit-review"],
    "customer_impacting": "unknown_pending_review"
  }
}
```

## Monitoring and Metrics

Exception audit records should support operational metrics without weakening privacy or tenant boundaries.

Useful metrics include:

- policy denials by action type, agent, tool, tenant group, and service tower;
- fail-closed events by failed control;
- approval failures by approval type and expiration reason;
- tool execution failures by tool contract and operation;
- unsupported-claim failures by agent package and prompt version;
- tenant-boundary failures by workflow type;
- evidence support failures by service tower;
- customer-facing release blocks by reason;
- fleet rollout failures by release stage;
- rollback and recall completion times;
- repeated exceptions by agent, package, tool, policy bundle, or customer group;
- emergency override frequency and post-review disposition.

Metrics should use identifiers and aggregations appropriate to the authorized audience. Customer-specific or evidence-sensitive details must not be exposed through dashboards or reports outside approved scope.

## Exception Review and Ownership

Every material exception should have an owner or routing path.

| Exception Type | Typical Owner |
|---|---|
| Policy denial trend | Policy owner or control-plane engineering |
| Missing approval | Service owner, approval workflow owner, or incident commander |
| Tool execution failure | Tool owner or platform engineering |
| Tenant-boundary failure | Tenant isolation owner, security engineering, or incident response lead |
| Evidence or DFIR failure | DFIR lead, evidence custodian, or forensic reviewer |
| Agent output quality failure | AI assurance owner, agent owner, or prompt/package owner |
| Fleet rollout failure | Fleet owner, service owner, release owner, or change authority |
| Sanitized intelligence failure | Tenant-isolation owner, release approver, or threat intelligence owner |
| Audit logging failure | Audit platform owner and security governance owner |
| Emergency override | Accountable emergency authority and post-action reviewer |

Ownership must be recorded when the exception requires follow-up.

## Anti-Patterns

Avoid the following:

- logging only successful actions;
- recording failure as a generic error without policy, tenant, agent, tool, or evidence context;
- treating denial as a system defect by default;
- retrying denied or approval-required actions automatically;
- allowing tool execution after approval expiration;
- treating human review as approval;
- treating Agent Judge failure as policy denial without PDP evaluation where policy is required;
- exposing raw customer data in exception dashboards;
- suppressing tenant-boundary failures as low-priority noise;
- allowing fleet rollout to continue after a failed gate;
- failing open because audit logging is unavailable;
- losing correlation between failed action, policy decision, approval state, and final disposition.

## Acceptance Criteria

Exception and failure audit is acceptable when all of the following are true:

- material failures, denials, blocked actions, fail-closed events, emergency overrides, rollbacks, and recalls are recorded;
- exception records link to the attempted workflow through `correlation_id` and relevant parent or causation references;
- tenant, customer, case, evidence, agent, policy, approval, tool, package, release, and destination scope are recorded where applicable;
- failure category, failed control, reason, severity, and workflow state are clear;
- sensitive actions cannot proceed when required exception audit is unavailable;
- approval failures are distinct from policy denials;
- AI assurance failures are distinct from policy decisions;
- tenant-boundary failures are blocked, escalated, and reviewable;
- evidence and DFIR failures prevent unsupported conclusions or releases;
- fleet rollout, rollback, recall, and sanitized intelligence release failures are auditable and reversible where required;
- exception metrics support operational improvement without exposing unauthorized customer or evidence data;
- replay can reconstruct what was attempted, why it failed, what control responded, who owned follow-up, and what final state occurred.

## Related Repository Areas

- [`audit-event-model.md`](audit-event-model.md) for the baseline audit event structure.
- [`audit-correlation-model.md`](audit-correlation-model.md) for linking audit records into replayable chains.
- [`replayability-requirements.md`](replayability-requirements.md) for replay requirements across decisions, approvals, tools, evidence, and outputs.
- [`fleet-rollout-audit-and-replay-model.md`](fleet-rollout-audit-and-replay-model.md) for fleet rollout, rollback, recall, and kill-switch replay.
- [`immutable-audit-guidance.md`](immutable-audit-guidance.md) for immutable storage, retention, and tamper-resistance guidance.
- [`../policy-enforcement/`](../policy-enforcement/readme.md) for PDP/PEP behavior, approval policy, risk classification, and fail-closed decisions.
- [`../human-oversight/`](../human-oversight/readme.md) for review, approval, customer approval, escalation, and emergency override boundaries.
- [`../tenant-isolation/`](../tenant-isolation/readme.md) for tenant boundary validation and cross-tenant failure modes.
- [`../evidence-traceability/`](../evidence-traceability/readme.md) for evidence references, finding support, and DFIR evidence handling.
- [`../agent-governance/`](../agent-governance/readme.md) for agent lifecycle, access scope, fleet governance, and rollback.
