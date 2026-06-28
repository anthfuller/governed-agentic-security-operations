# Audit Correlation Model

## Purpose

This document defines how audit records are correlated across the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The model ensures that a governed workflow can be reconstructed across telemetry ingestion, context assembly, agent invocation, AI assurance, policy evaluation, human approval, tool execution, evidence handling, reporting, fleet rollout, rollback, recall, and exception handling.

Audit correlation answers five questions:

1. What workflow or decision chain did this event belong to?
2. Which tenant, customer, case, evidence set, agent, and version were involved?
3. Which policy, approval, and enforcement decisions controlled the action?
4. Which tools, outputs, reports, or fleet releases were affected?
5. Can the sequence be replayed without relying on model output as the source of truth?

## Scope

This model applies to audit records created by governed agentic security operations across:

- MSSP alert triage, enrichment, escalation, and customer reporting;
- MDR investigation, response recommendation, containment guidance, and threat hunting;
- SOC and cloud incident response workflows;
- private/local LLM-assisted DFIR workflows;
- policy-gated tool execution;
- evidence-backed findings and reports;
- human review and approval flows;
- agent fleet rollout, rollback, recall, and emergency override;
- sanitized intelligence propagation across eligible tenants or service towers;
- exception, denial, and fail-closed handling.

This file defines the correlation model. It does not define the complete audit event schema, immutable storage requirements, retention policy, or production logging implementation.

## Core Principle

Every governed workflow must have a replayable audit chain.

Correlation must connect records across components without weakening tenant isolation, evidence integrity, or approval boundaries. A correlation identifier links records for review. It does not authorize data sharing, cross-tenant access, tool execution, or evidence disclosure.

## Correlation Domains

Audit correlation must preserve relationships across the following domains.

| Domain | Correlation Need |
|---|---|
| Tenant and customer scope | Prove the workflow stayed inside the authorized customer, tenant, environment, and service boundary. |
| Case and investigation scope | Connect actions to the correct incident, case, investigation, ticket, or DFIR matter. |
| Agent identity and version | Identify which agent, package version, prompt version, model route, policy bundle, and tool contract participated. |
| Context assembly | Link the agent input context to approved retrieval sources, evidence references, and data minimization decisions. |
| Evidence traceability | Preserve references to source evidence used to support findings, recommendations, approvals, and outputs. |
| AI assurance | Link agent outputs to judge results, unsupported-claim checks, tenant-boundary checks, and evidence-support checks. |
| Policy enforcement | Link tool requests, output release requests, and fleet updates to policy requests and PDP decisions. |
| Human oversight | Link review records, approvals, denials, customer approvals, escalations, and emergency overrides. |
| Tool execution | Link approved requests to scoped execution tokens, tool calls, target entities, and execution results. |
| Output release | Link internal notes, customer reports, DFIR conclusions, notifications, and service records to review and approval. |
| Fleet operations | Link package changes, rollout stages, tenant eligibility, monitoring gates, rollback, and recall records. |
| Exceptions and failures | Link denials, policy failures, missing evidence, boundary violations, and fail-closed events to the attempted workflow. |

## Identifier Model

Correlation uses stable identifiers. Identifiers should be opaque, durable, and non-sensitive. They must not embed raw customer data, evidence content, secrets, usernames, hostnames, tenant names, or case narratives.

| Identifier | Purpose |
|---|---|
| `audit_event_id` | Unique identifier for one audit event record. |
| `correlation_id` | End-to-end identifier for a governed workflow, decision chain, or replayable sequence. |
| `parent_event_id` | Direct parent record that led to this audit event. |
| `causation_id` | Record or decision that caused this event, even if it is not the direct parent. |
| `workflow_id` | Identifier for the security workflow, playbook, investigation flow, or fleet update flow. |
| `tenant_id` | Tenant or customer boundary where the event occurred. |
| `customer_id` | Customer or service-delivery ownership boundary where applicable. |
| `case_id` | Incident, case, matter, ticket, or investigation identifier. |
| `evidence_refs` | References to evidence that influenced a finding, decision, approval, output, or action. |
| `context_package_id` | Identifier for the approved context package supplied to an agent or judge. |
| `agent_invocation_id` | Identifier for a specific agent run or task invocation. |
| `agent_id` | Registered identity of the agent. |
| `agent_package_id` | Versioned agent package used for the invocation. |
| `model_ref` | Model, model route, or local/private model reference used for generation or evaluation. |
| `prompt_ref` | Prompt, prompt package, or prompt template reference. |
| `retrieval_ref` | Retrieval query, corpus, index, or approved knowledge source reference. |
| `agent_output_ref` | Stored agent output or structured result reference. |
| `judge_result_ref` | AI assurance or Agent Judge result reference. |
| `policy_request_id` | Request sent to the policy decision process. |
| `policy_decision_id` | Policy decision record returned by the PDP. |
| `approval_record_id` | Human, customer, service-owner, or emergency approval record. |
| `execution_token_id` | Scoped execution token issued after authorization where applicable. |
| `tool_execution_id` | Tool gateway execution record. |
| `output_release_id` | Release record for customer-facing output, internal report, notification, or case update. |
| `release_id` | Sanitized intelligence release, package release, prompt release, playbook release, or detection release identifier. |
| `rollout_id` | Fleet rollout sequence identifier. |
| `rollback_id` | Rollback sequence identifier. |
| `recall_id` | Emergency recall or kill-switch sequence identifier. |
| `exception_id` | Exception, failure, denial, or fail-closed event identifier. |

## Correlation Rules

1. Every governed audit event must include an `audit_event_id` and `correlation_id`.
2. Events that affect a tenant, customer, case, evidence object, output, or tool action must include the applicable scope identifiers.
3. Agent events must include `agent_id`, `agent_package_id`, lifecycle state where available, and the relevant prompt, model, policy, and tool-contract versions.
4. Context assembly events must link to the approved context package and the evidence or retrieval references used to build it.
5. Agent outputs must be linked to the context package that produced them.
6. Judge results must be linked to the agent output they evaluated.
7. Policy decisions must be linked to the policy request, requested action, tenant scope, evidence references, judge results where applicable, and decision outcome.
8. Human approvals must be linked to the policy decision, reviewed evidence, reviewer identity or role, approval scope, expiration where applicable, and decision outcome.
9. Tool execution events must be linked to the policy decision and approval record that authorized execution.
10. Customer-facing output must be linked to supporting evidence, agent output, judge results where used, review record, and release approval.
11. Fleet rollout events must be linked to package version, tenant eligibility, approval record, monitoring gates, rollout stage, and rollback target.
12. Rollback and recall events must be linked to the affected package, affected tenants, trigger event, containment action, and recovery state.
13. Exception and failure events must be linked to the attempted action and the control that blocked, denied, escalated, or failed closed.
14. Cross-tenant sanitized intelligence releases must use release records and authorized internal references. Destination tenants must not receive source tenant identifiers, source case identifiers, raw evidence references, or source-specific case context.
15. Correlation identifiers must not be treated as authorization tokens.

## Runtime Workflow Correlation

A standard agent-assisted investigation should produce a linked chain of audit records.

| Step | Audit Record | Required Correlation |
|---|---|---|
| Alert or event ingestion | Ingestion audit event | `correlation_id`, `tenant_id`, `customer_id`, `case_id`, `source_system`, `evidence_refs` |
| Normalization and enrichment | Normalization audit event | Parent ingestion event, source metadata, transformation reference |
| Context assembly | Context package event | Evidence references, retrieval references, data minimization decision, agent eligibility |
| Agent invocation | Agent run event | Agent identity, package version, model reference, prompt reference, context package |
| Agent output | Agent output event | Agent invocation, output reference, findings, evidence references, requested action if any |
| AI assurance | Judge result event | Agent output reference, judge identity, evaluation result, unsupported claims, HITL recommendation |
| Policy request | Policy request event | Requested action, tenant scope, tool, target entity, evidence, judge result where applicable |
| Policy decision | Policy decision event | Policy request, decision, reason, required approval role, expiration where applicable |
| Human review or approval | Approval event | Policy decision, reviewer, reviewed evidence, approved scope, approval outcome |
| Tool execution | Tool execution event | Policy decision, approval record, execution token, tool contract, target entity, execution result |
| Case or report update | Output release event | Evidence references, review state, approval state, released output reference |
| Monitoring and feedback | Monitoring event | Runtime metrics, policy denials, anomalies, exceptions, follow-up action |

## Example Correlation Envelope

The following example shows how records can be linked. It is not a full audit event schema.

```json
{
  "correlation_id": "corr-2026-05-22-10422",
  "workflow_id": "mdr-agent-assisted-investigation",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "agent": {
    "agent_id": "response-recommendation-agent",
    "agent_package_id": "response-recommendation-agent@1.6.3",
    "prompt_ref": "response-recommendation-prompts@2.4.1",
    "model_ref": "approved-security-operations-model-route",
    "policy_bundle_ref": "mdr-response-policy@3.2.0"
  },
  "records": {
    "context_package_id": "ctx-10422-0004",
    "agent_invocation_id": "agent-run-10422-0007",
    "agent_output_ref": "agent-output://cust-a/inc-10422/out-0007",
    "judge_result_ref": "judge-result://cust-a/inc-10422/judge-0012",
    "policy_request_id": "policy-req-10422-0015",
    "policy_decision_id": "policy-decision-10422-0015",
    "approval_record_id": "approval-10422-0009",
    "execution_token_id": "exec-token-10422-0009",
    "tool_execution_id": "tool-exec-10422-0021"
  },
  "evidence_refs": [
    "evidence://customer-a/inc-10422/events/evt-001",
    "evidence://customer-a/inc-10422/events/evt-004"
  ],
  "final_state": "executed_after_approval"
}
```

## Parent and Causation Relationships

A correlation chain should support both sequence and cause.

| Relationship | Meaning | Example |
|---|---|---|
| `parent_event_id` | The immediate prior event in the workflow path. | A policy decision event has the policy request as its parent. |
| `causation_id` | The event, decision, or condition that caused this record to be created. | A fail-closed event caused by missing approval uses the missing approval check as causation. |
| `source_correlation_id` | Prior correlation chain that led to a new independent workflow. | A closed investigation creates a separate sanitized intelligence release request. |
| `linked_correlation_ids` | Related workflows that should be reviewed together. | Multiple affected tenants linked to one recalled fleet package. |

Use `parent_event_id` for replay order. Use `causation_id` for root-cause analysis. Use `source_correlation_id` when a new workflow is created from a previous workflow but should remain separately governed.

## Policy and Approval Correlation

Policy and approval records must remain separate.

A policy decision determines whether a request is allowed, denied, or requires approval. A human approval record captures accountable approval where required. Tool execution must link to both when approval was required.

| Record | Must Link To |
|---|---|
| Policy request | Agent output, requested tool, target entity, tenant, case, evidence, action risk, judge result where applicable |
| Policy decision | Policy request, policy bundle, decision, reason, required approval role, expiration, audit requirement |
| Human approval | Policy decision, approver identity or role, reviewed evidence, approved scope, approval decision, timestamp |
| Customer approval | Customer authority, customer obligation, approved action or release, expiration, conditions |
| Tool execution | Policy decision, approval record where required, execution token, tool contract, target entity, outcome |

A tool execution record without a valid policy decision and required approval link must be treated as unauthorized or incomplete.

## Evidence and Finding Correlation

Evidence references must connect findings, summaries, approvals, reports, and tool actions back to the source material that supported them.

Correlation requirements:

- Findings must link to evidence references or clearly state that additional evidence is required.
- Agent summaries must link to the context package and source evidence references that influenced the summary.
- DFIR conclusions must link to evidence references, analyst review, and report approval.
- Evidence-derived outputs must not be treated as original evidence.
- Evidence references must remain tenant-scoped and case-scoped.
- Source evidence must not be exposed to unauthorized destination tenants through correlation fields.

For private/local LLM-assisted DFIR, audit correlation should include local model reference, prompt reference, selected artifact references, reviewer record, and final report reference where applicable.

## Fleet Rollout Correlation

Fleet rollout correlation is required when agent packages, prompt packages, tool contracts, policy bundles, retrieval configurations, detection packages, playbooks, report templates, or sanitized intelligence are distributed across tenants, customers, service towers, or environments.

| Fleet Event | Required Correlation |
|---|---|
| Change request | Change owner, package or artifact, reason, affected service tower, risk tier |
| Package assembly | Agent package, prompt package, model route, tool contracts, policy bundle, retrieval scope, monitoring profile |
| Validation | Test run IDs, assurance checks, tenant-boundary checks, rollback validation, evidence of review |
| Approval | Engineering approval, service-owner approval, policy-owner approval, customer approval where required |
| Tenant eligibility | Included tenants, excluded tenants, service tier, region, contractual or sovereignty restrictions |
| Canary rollout | Rollout ID, tenant cohort, package version, monitoring gates, exceptions |
| Broad rollout | Rollout stage, destination scope, policy decision, monitoring profile, affected tenants |
| Rollback | Rollback ID, trigger, affected scope, rollback target, completion state |
| Recall | Recall ID, kill-switch trigger, stopped versions, revoked tokens, affected tenants, notification and recovery state |

Fleet rollout records must support answering:

- Which version was active for each tenant at a specific time?
- Which tenants were eligible, excluded, canaried, rolled out, rolled back, or recalled?
- Which approval and policy records authorized the rollout?
- Which monitoring events triggered rollback or recall?
- Which outputs or tool actions were produced by an affected version?

## Sanitized Intelligence Release Correlation

Cross-tenant sanitized intelligence propagation requires separate release correlation.

Required links:

- source workflow or source correlation ID;
- internal source tenant reference available only to authorized reviewers;
- source classification and sensitivity handling;
- sanitization review record;
- AI assurance checks where used;
- human release approval;
- policy decision;
- tenant eligibility result;
- destination scope;
- release channel;
- released version;
- monitoring profile;
- recall or removal path.

Destination tenants should receive only the approved sanitized release metadata required for use. They should not receive source tenant identifiers, source case identifiers, source evidence references, or reviewer-only internal notes.

## Exception and Failure Correlation

Exception and failure events must be first-class audit records. They are required for replay because a denied or failed action may be the most important part of the workflow.

| Failure Condition | Correlation Requirement |
|---|---|
| Missing tenant or case scope | Link attempted workflow, requesting agent, blocked component, and fail-closed reason. |
| Missing evidence reference | Link agent output, requested action, policy request, and evidence-support failure. |
| Policy engine unavailable | Link policy request, timeout or failure reason, and fail-closed outcome. |
| Required approval missing | Link policy decision, expected approval role, attempted execution, and block reason. |
| Tool contract mismatch | Link tool request, tool contract, schema validation failure, and enforcement point. |
| Cross-tenant access attempt | Link source tenant, attempted destination, retrieval or tool request, and boundary control. |
| Audit logging unavailable | Link attempted sensitive action, blocked execution, and operational escalation. |
| Recalled package invocation | Link agent invocation, package version, recall ID, and blocked runtime decision. |
| Sanitization failure | Link release request, failed check, reviewer decision, and release denial. |

Failure records should include `exception_id`, `failed_event_id`, `control_point`, `failure_reason`, `blocked_action`, `final_state`, and `required_remediation` where applicable.

## Replay Model

Replay reconstructs a governed workflow from the audit chain.

A replay process should be able to:

1. Start from `correlation_id`, `case_id`, `tool_execution_id`, `policy_decision_id`, `release_id`, `rollout_id`, `rollback_id`, or `recall_id`.
2. Load all linked audit records.
3. Validate tenant, customer, case, and evidence boundaries.
4. Reconstruct the event order using timestamps, `parent_event_id`, and `causation_id`.
5. Resolve agent identity, package version, prompt reference, model reference, tool contract, and policy bundle.
6. Verify context assembly and evidence references.
7. Verify judge result linkage where AI assurance was used.
8. Verify policy request and decision linkage.
9. Verify approval linkage where approval was required.
10. Verify execution token, tool execution, output release, and final outcome.
11. Identify denials, exceptions, fail-closed events, overrides, rollback, or recall actions.
12. Produce a reviewer-readable reconstruction without exposing data outside the authorized scope.

Replay should not depend on asking the model what happened. Replay depends on durable records, stable references, policy decisions, approvals, evidence links, and execution outcomes.

## Query and Investigation Patterns

Audit correlation should support the following investigation patterns.

| Query Pattern | Example Question |
|---|---|
| By case | What agents, evidence, policy decisions, approvals, and tool actions occurred in this case? |
| By tenant | Which governed workflows affected this tenant during a time window? |
| By agent version | Which cases or tenants used a specific agent package version? |
| By policy decision | Which requests were denied, required approval, or executed after approval? |
| By approval record | Which actions did a specific approval authorize? |
| By tool execution | Which policy decision and approval authorized this tool action? |
| By evidence reference | Which findings, reports, and actions relied on this evidence? |
| By output release | Which evidence, reviews, approvals, and policy decisions supported this report or notification? |
| By release ID | Which tenants received a sanitized intelligence release or fleet package? |
| By recall ID | Which versions, tenants, outputs, sessions, and tool actions were affected by recall? |
| By exception | Which workflows failed closed, why, and what remediation is required? |

## Data Minimization and Boundary Controls

Correlation records should preserve traceability without creating new leakage paths.

Required controls:

- Use opaque identifiers rather than customer names or sensitive values.
- Do not embed raw logs, evidence content, prompts, outputs, tokens, secrets, credentials, or customer narratives in correlation identifiers.
- Keep reviewer-only source references separate from destination-visible release metadata.
- Preserve tenant and case scope on every governed event.
- Restrict audit search and replay access by role, tenant, case, and evidence authorization.
- Do not expose source tenant references to destination tenants during sanitized intelligence propagation.
- Treat audit records as sensitive operational records.
- Do not use shared correlation fields to bypass tenant isolation or evidence access controls.

## Minimum Correlation Fields

The following fields should be present on governed audit events where applicable.

| Field | Required When |
|---|---|
| `audit_event_id` | Every audit event. |
| `event_type` | Every audit event. |
| `event_time` | Every audit event. |
| `correlation_id` | Every governed workflow event. |
| `parent_event_id` | Event is part of an ordered workflow chain. |
| `causation_id` | Event is caused by a prior decision, failure, approval, or trigger. |
| `tenant_id` | Event affects customer, tenant, case, evidence, retrieval, tool, or output scope. |
| `customer_id` | Event affects service ownership or customer-specific obligation. |
| `case_id` | Event relates to an incident, investigation, ticket, or DFIR matter. |
| `agent_id` | Event involves agent invocation, output, tool request, or agent policy. |
| `agent_package_id` | Event involves a versioned agent capability. |
| `context_package_id` | Event involves assembled context or model input. |
| `evidence_refs` | Event influences findings, approvals, reports, policy decisions, or tool execution. |
| `policy_request_id` | Event requests authorization. |
| `policy_decision_id` | Event is controlled by a policy decision. |
| `approval_record_id` | Event requires or follows approval. |
| `tool_execution_id` | Event involves mediated tool execution. |
| `release_id` | Event involves fleet release or sanitized intelligence release. |
| `rollout_id` | Event is part of a rollout sequence. |
| `rollback_id` | Event is part of rollback. |
| `recall_id` | Event is part of emergency recall. |
| `exception_id` | Event records failure, denial, or fail-closed behavior. |
| `final_state` | Event completes, blocks, denies, fails, rolls back, recalls, or closes a workflow step. |

## Required Controls

- Correlation IDs must be generated by trusted workflow, audit, or control-plane components, not by free-form model output.
- Agents may include correlation IDs in structured outputs only when the IDs were supplied by the platform.
- Policy and enforcement components must validate correlation scope before using a linked record.
- Tool gateways must reject execution requests that reference unrelated, stale, missing, or mismatched policy and approval records.
- Audit correlation must preserve denied, blocked, failed, and fail-closed paths, not only successful executions.
- Rollback and recall records must remain linked to the affected versions and affected tenants.
- Replay access must be authorized and scoped.

## Acceptance Criteria

The audit correlation model is acceptable when it can demonstrate the following:

- a governed workflow can be reconstructed from start to finish;
- tenant, customer, case, evidence, and tool boundaries are visible in the audit chain;
- agent identity, version, prompt, model, policy bundle, and tool contract are traceable;
- agent outputs are linked to context packages and evidence references;
- judge results are linked to the outputs they evaluated;
- policy requests and decisions are linked to requested actions and evidence;
- approvals are linked to the policy decisions and actions they authorized;
- tool execution is linked to policy, approval, scoped execution, and outcome;
- customer-facing outputs are linked to evidence, review, approval, and release records;
- fleet rollout, rollback, and recall records can identify affected tenants, versions, outputs, and actions;
- sanitized intelligence releases can be replayed without exposing source tenant data to destination tenants;
- failures, denials, exceptions, and fail-closed events are preserved;
- replay does not rely on model memory or model-generated explanations as the source of truth.

## Related Repository Areas

- [`audit-event-model.md`](audit-event-model.md) for the audit event structure.
- [`replayability-requirements.md`](replayability-requirements.md) for replay requirements and reviewer expectations.
- [`exception-and-failure-audit.md`](exception-and-failure-audit.md) for denied, failed, and fail-closed audit paths.
- [`fleet-rollout-audit-and-replay-model.md`](fleet-rollout-audit-and-replay-model.md) for fleet rollout, rollback, and recall replay.
- [`immutable-audit-guidance.md`](immutable-audit-guidance.md) for audit durability, tamper resistance, and storage guidance.
- [`../architecture/control-loop.md`](../architecture/control-loop.md) for the runtime execution control loop.
- [`../architecture/agentic-fleet-control-loop.md`](../architecture/agentic-fleet-control-loop.md) for fleet update control flow.
- [`../tenant-isolation/fleet-scope-and-cross-tenant-propagation-boundaries.md`](../tenant-isolation/fleet-scope-and-cross-tenant-propagation-boundaries.md) for sanitized intelligence propagation boundaries.
- [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) for evidence references and finding support.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) for policy decisions and enforcement behavior.
