# Audit Event Model

## Purpose

This document defines the audit event model for governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

The model defines a baseline event shape needed to reconstruct governed decisions, approvals, evidence references, tool execution, output release, fleet rollout, rollback, recall, and failure handling without treating model output as the source of truth.

An audit event should answer:

1. What happened?
2. When did it happen?
3. Who or what initiated it?
4. Which tenant, customer, case, evidence set, agent, version, tool, policy, approval, or fleet release was involved?
5. What decision or outcome occurred?
6. Can the event be correlated and replayed with the rest of the workflow?

## Scope

This model applies to audit events created by governed security operations workflows, including:

- telemetry ingestion, parsing, normalization, enrichment, and routing;
- tenant-scoped context assembly and retrieval;
- agent invocation, prompt use, model routing, and structured output generation;
- AI assurance checks and Agent Judge evaluations;
- policy requests, PDP decisions, and PEP enforcement;
- human review, customer approval, escalation, and emergency override;
- mediated tool execution;
- evidence access, evidence reference creation, finding support, and DFIR review;
- case updates, customer-facing output review, and report release;
- fleet package creation, rollout, rollback, recall, and kill-switch activity;
- sanitized intelligence release and cross-tenant propagation control;
- exceptions, denials, failures, and fail-closed outcomes.

This file defines audit event structure. It does not define immutable storage design, retention policy, complete production schemas, transport protocols, or SIEM-specific field mappings.

## Core Principle

Every governed action or decision that can affect a tenant, customer, case, evidence object, tool, report, fleet package, or operational outcome must produce a replayable audit event.

Audit events must preserve enough context to reconstruct the workflow without exposing data outside the authorized tenant, case, evidence, or destination boundary.

Model output, agent confidence, generated summaries, and chat transcripts are not sufficient audit records by themselves. They may be referenced by audit events, but they do not replace structured audit fields, evidence references, policy decisions, approval records, or execution results.

## Event Model Overview

An audit event is a structured record with six major parts.

| Event Part | Purpose |
|---|---|
| Event identity | Identifies the audit record, event type, version, timestamp, and producer. |
| Correlation | Links the event to the larger workflow, parent event, causation event, case, tenant, and related records. |
| Actor | Identifies the human, agent, system, tool, workflow, or policy component responsible for the event. |
| Scope | Defines the tenant, customer, case, environment, evidence, data classification, and destination boundary. |
| Action and decision | Describes what was requested, evaluated, approved, denied, executed, released, rolled back, or failed closed. |
| Outcome and integrity | Records the result, error or exception state, retention label, integrity metadata, and audit storage requirements. |

## Baseline Audit Event Envelope

The following fields form the baseline envelope for audit events.

| Field | Requirement | Purpose |
|---|---|---|
| `audit_event_id` | Required | Unique identifier for the audit event. |
| `event_type` | Required | Normalized event type, such as `agent.invocation.completed` or `policy.decision.created`. |
| `event_version` | Required | Version of the event shape used by the producer. |
| `event_time` | Required | Time the event occurred. |
| `recorded_time` | Required | Time the event was written to the audit system. |
| `producer` | Required | Component that created the audit event. |
| `correlation_id` | Required | End-to-end workflow or decision-chain identifier. |
| `tenant_id` | Conditional | Required when the event touches tenant-scoped data, tools, cases, outputs, or fleet eligibility. |
| `customer_id` | Conditional | Required when the workflow is customer-scoped or service-delivery scoped. |
| `case_id` | Conditional | Required when the event belongs to an incident, investigation, ticket, matter, or DFIR case. |
| `actor` | Required | Human, agent, system, tool, policy engine, workflow, or service that initiated or performed the activity. |
| `action` | Required | Requested, evaluated, executed, released, denied, approved, or failed action. |
| `outcome` | Required | Result of the event. |
| `data_classification` | Conditional | Required when sensitive, customer, evidence, privileged, regulated, or derived intelligence is involved. |
| `evidence_refs` | Conditional | Required when evidence influences a finding, decision, approval, report, DFIR conclusion, or tool action. |
| `policy_refs` | Conditional | Required when policy evaluation, authorization, or enforcement is involved. |
| `approval_refs` | Conditional | Required when human, customer, service-owner, or emergency approval is involved. |
| `integrity` | Recommended | Hash, signature, sequence, or storage integrity metadata where supported. |

## Example Audit Event Shape

```json
{
  "audit_event_id": "audit-2026-05-22-000184",
  "event_type": "tool.execution.completed",
  "event_version": "1.0",
  "event_time": "2026-05-22T11:42:18Z",
  "recorded_time": "2026-05-22T11:42:21Z",
  "producer": {
    "component": "tool-gateway",
    "component_version": "tool-gateway@2.1.0",
    "environment": "managed-mdr-control-plane"
  },
  "correlation": {
    "correlation_id": "corr-2026-05-22-10422",
    "parent_event_id": "audit-2026-05-22-000181",
    "causation_id": "policy-decision-10422-0015",
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
    "actor_type": "tool_gateway",
    "actor_id": "tool-gateway",
    "on_behalf_of_agent_id": "response-recommendation-agent",
    "on_behalf_of_agent_package_id": "response-recommendation-agent@1.6.3"
  },
  "action": {
    "action_category": "mediated_tool_execution",
    "requested_tool": "endpoint-isolation-tool",
    "requested_operation": "isolate_endpoint",
    "target_type": "endpoint",
    "target_ref": "device-123",
    "action_risk": "high"
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
    "execution_token_id": "exec-token-10422-0009"
  },
  "outcome": {
    "status": "executed",
    "execution_result": "success",
    "customer_impacting": true,
    "requires_follow_up": true
  },
  "integrity": {
    "audit_store": "immutable-audit-logical-store",
    "record_hash": "sha256:example",
    "retention_label": "security-operations-audit"
  }
}
```

This example is an architecture record shape. Implementations should validate event fields through controlled schemas, access control, retention rules, and audit storage controls.

## Event Type Naming

Event types should be predictable and stable. A recommended pattern is:

```text
<domain>.<object>.<activity>
```

Examples:

| Event Type | Meaning |
|---|---|
| `ingestion.event.received` | Source event, alert, log, ticket, or artifact was received. |
| `ingestion.event.normalized` | Source event was parsed, mapped, enriched, or normalized. |
| `context.package.created` | Tenant-scoped context package was assembled for an agent or judge. |
| `agent.invocation.started` | Agent execution started. |
| `agent.invocation.completed` | Agent execution completed. |
| `agent.output.created` | Structured agent output was stored or referenced. |
| `judge.evaluation.completed` | AI assurance or Agent Judge evaluation completed. |
| `policy.request.created` | A policy decision request was submitted. |
| `policy.decision.created` | PDP returned allow, deny, or require-approval. |
| `approval.requested` | Human, customer, service-owner, or emergency approval was requested. |
| `approval.decision.recorded` | Approval, denial, expiration, or withdrawal was recorded. |
| `tool.execution.requested` | A mediated tool action was requested. |
| `tool.execution.completed` | Tool execution completed or failed. |
| `evidence.reference.created` | Evidence reference was created, transformed, or linked. |
| `output.review.completed` | Internal, customer-facing, or DFIR output was reviewed. |
| `output.release.completed` | Case note, customer report, notification, or final output was released. |
| `fleet.change.requested` | Agent, prompt, policy, tool, detection, playbook, or report-template change was requested. |
| `fleet.rollout.stage.completed` | Canary, cohort, broad rollout, rollback, or recall stage completed. |
| `fleet.recall.triggered` | Emergency recall or kill-switch action was triggered. |
| `intelligence.release.requested` | Sanitized intelligence release was requested. |
| `intelligence.release.completed` | Sanitized intelligence was released to an approved destination scope. |
| `exception.fail_closed` | Workflow stopped because a required control was missing or invalid. |

## Required Event Categories

### Ingestion and Normalization Events

Create audit events when telemetry, alerts, logs, tickets, case records, threat intelligence, or forensic artifacts are received, transformed, enriched, routed, or rejected.

Required fields include:

| Field | Requirement |
|---|---|
| `source_system` | Original platform, connector, or evidence source. |
| `source_event_id` | Source-side event identifier where available. |
| `source_timestamp` | Timestamp from the source system. |
| `ingestion_timestamp` | Timestamp recorded by the ingestion pipeline. |
| `tenant_id` | Required for tenant-scoped sources. |
| `customer_id` | Required for customer-scoped managed services. |
| `case_id` | Required when the event is attached to a case, incident, ticket, or matter. |
| `data_classification` | Sensitivity and handling requirement. |
| `transformation_ref` | Normalization, enrichment, parsing, or mapping reference where applicable. |
| `evidence_refs` | Required when the event becomes evidence or influences findings. |
| `outcome.status` | Received, normalized, enriched, routed, rejected, quarantined, or failed. |

### Context Assembly Events

Create audit events when approved context is assembled for an agent, judge, workflow, report, or local/private model review.

Context assembly events must show that the supplied context was scoped, minimized, and evidence-linked.

Required fields include:

| Field | Requirement |
|---|---|
| `context_package_id` | Unique context package identifier. |
| `tenant_id` | Tenant boundary. |
| `case_id` | Case, incident, investigation, or DFIR matter boundary. |
| `authorized_agent_id` | Agent authorized to receive the context. |
| `retrieval_refs` | Retrieval query, index, corpus, or knowledge source references. |
| `evidence_refs` | Evidence references included or used to build context. |
| `data_minimization_result` | Result of filtering, masking, redaction, or exclusion. |
| `untrusted_content_labels` | Markers for logs, emails, tickets, or tool output that may contain adversarial content. |
| `outcome.status` | Created, denied, failed closed, or routed for review. |

### Agent Invocation Events

Create audit events when an agent starts, completes, fails, is blocked, or is recalled during a workflow.

Required fields include:

| Field | Requirement |
|---|---|
| `agent_invocation_id` | Unique run or invocation identifier. |
| `agent_id` | Registered agent identity. |
| `agent_package_id` | Versioned package used for execution. |
| `agent_lifecycle_state` | Active, suspended, recalled, retired, canary, or other approved state. |
| `agent_owner` | Owning team or service owner. |
| `prompt_ref` | Prompt package or template reference. |
| `model_ref` | Model route, hosted model, or local/private model reference. |
| `policy_bundle_ref` | Policy bundle relevant to the invocation where applicable. |
| `context_package_id` | Approved context supplied to the agent. |
| `requested_task` | Task objective or workflow step. |
| `outcome.status` | Started, completed, failed, blocked, denied, or recalled. |

Agent invocation events should not store unnecessary raw prompt or customer data directly in the audit event. Store controlled references to the prompt, context package, and output record.

### Agent Output Events

Create audit events when an agent produces structured output that may influence investigation, triage, DFIR conclusions, customer-facing content, escalation, policy decisions, approval routing, tool execution, or fleet updates.

Required fields include:

| Field | Requirement |
|---|---|
| `agent_output_ref` | Stored output reference. |
| `agent_invocation_id` | Invocation that produced the output. |
| `context_package_id` | Context package used to generate the output. |
| `output_type` | Summary, finding, recommendation, report draft, tool request, detection proposal, sanitized intelligence proposal, or other type. |
| `evidence_refs` | Required for findings, recommendations, reports, DFIR conclusions, and sensitive-action requests. |
| `requested_action` | Required when the output requests or recommends an action. |
| `customer_facing_candidate` | Whether the output may become customer-facing. |
| `requires_review` | Whether review is required by policy or risk. |
| `outcome.status` | Created, rejected, routed for assurance, routed for approval, or blocked. |

### AI Assurance and Judge Events

Create audit events when an AI assurance check or Agent Judge evaluates agent output.

Required fields include:

| Field | Requirement |
|---|---|
| `judge_result_ref` | Stored judge or assurance result reference. |
| `judge_id` | Judge or assurance component identity. |
| `judge_version` | Version of the evaluation logic, prompt, model route, or ruleset. |
| `agent_output_ref` | Output being evaluated. |
| `evaluation_type` | Evidence support, unsupported claim, tenant boundary, HITL requirement, output quality, ATT&CK mapping, or other check. |
| `evaluation_result` | Pass, fail, warning, requires review, inconclusive, or not applicable. |
| `unsupported_claims` | References or counts where applicable. |
| `tenant_boundary_risk` | Whether a tenant boundary issue was detected. |
| `hitl_recommendation` | Human review or approval recommendation where applicable. |
| `outcome.status` | Completed, failed, inconclusive, or blocked. |

AI assurance output is not authorization. If the result affects execution or release, it must feed a policy or approval process.

### Policy Request and Decision Events

Create audit events when a policy request is submitted and when a policy decision is returned.

Required fields include:

| Field | Requirement |
|---|---|
| `policy_request_id` | Unique policy request identifier. |
| `policy_decision_id` | Required for decision events. |
| `policy_bundle_ref` | Versioned policy bundle or rule set. |
| `pep_id` | Enforcement component requesting or enforcing the decision. |
| `pdp_id` | Decision component that returned the decision. |
| `requested_action` | Requested operation, output release, tool execution, package rollout, recall, or propagation. |
| `action_risk` | Low, medium, high, critical, or organization-defined risk tier. |
| `tenant_id` | Required for tenant-scoped policy decisions. |
| `case_id` | Required for case-scoped policy decisions. |
| `evidence_refs` | Required for sensitive actions and evidence-backed decisions. |
| `judge_result_ref` | Required when assurance output influenced the decision. |
| `decision` | `ALLOW`, `DENY`,`REQUIRE_REVIEW`,`REQUIRE_APPROVAL` or `FAIL_CLOSED`. |
| `decision_reason` | Reason code or policy rationale. |
| `expires_at` | Required when decision validity is time-limited. |
| `outcome.status` | Decision created, denied, approval required, failed closed, or escalated. |

Policy decision outcomes must remain explicit. `REQUIRE_REVIEW` means a human review is needed before the workflow continues. `REQUIRE_APPROVAL` means accountable authorization is required before execution, release, rollout, or propagation. `FAIL_CLOSED` means the workflow must halt because a required control is missing or invalid.

### Human Review and Approval Events

Create audit events when human review, formal approval, customer approval, service-owner approval, escalation, denial, expiration, or emergency override occurs.

Required fields include:

| Field | Requirement |
|---|---|
| `approval_record_id` | Unique approval or review record. |
| `approval_type` | Human review, human approval, customer approval, emergency override, service-owner approval, or legal review. |
| `reviewer_id` | Human, group, role, or approval authority reference. |
| `reviewer_role` | Role or authority used for the review or approval. |
| `policy_decision_id` | Required when approval is tied to a policy decision. |
| `reviewed_refs` | Evidence, output, recommendation, policy decision, or release record reviewed. |
| `decision` | Approved, denied, returned, escalated, expired, withdrawn, or emergency approved. |
| `approval_scope` | Exact action, output, tenant, case, tool, package, release, or time scope approved. |
| `conditions` | Approval constraints, expiry, customer conditions, or restrictions. |
| `outcome.status` | Recorded, denied, expired, escalated, or superseded. |

Human review and formal approval are separate controls. Audit events must not collapse review, approval, and execution into a single unstructured note.

### Tool Execution Events

Create audit events when a tool action is requested, authorized, denied, executed, fails, is retried, or is rolled back.

Required fields include:

| Field | Requirement |
|---|---|
| `tool_execution_id` | Unique tool execution record. |
| `tool_id` | Registered tool identifier. |
| `tool_contract_ref` | Versioned tool contract. |
| `requested_operation` | Operation requested. |
| `target_type` | Endpoint, identity, mailbox, cloud resource, ticket, detection, evidence object, report, or other target. |
| `target_ref` | Scoped target reference. |
| `execution_token_id` | Required when scoped execution tokens are used. |
| `policy_decision_id` | Policy decision authorizing or denying the action. |
| `approval_record_id` | Required when approval was required. |
| `input_ref` | Controlled reference to request payload where required. |
| `output_ref` | Controlled reference to tool output where required. |
| `execution_result` | Success, failed, partial, denied, timeout, rollback, or no-op. |
| `outcome.status` | Requested, executed, failed, denied, reverted, or failed closed. |

Tools must not rely on agent output alone as authorization. Tool execution events should prove that policy and approval requirements were satisfied or that the action was denied.

### Evidence and DFIR Events

Create audit events when evidence is collected, referenced, transformed, accessed, summarized, used to support a finding, reviewed, released, quarantined, or excluded.

Required fields include:

| Field | Requirement |
|---|---|
| `evidence_event_id` | Unique evidence audit event identifier where separate from `audit_event_id`. |
| `evidence_refs` | Evidence reference identifiers. |
| `evidence_action` | Collected, accessed, hashed, parsed, transformed, summarized, reviewed, excluded, released, or quarantined. |
| `evidence_store_ref` | Evidence system or vault reference. |
| `chain_of_custody_ref` | Required for DFIR evidence where applicable. |
| `artifact_type` | Log, email, endpoint artifact, disk image, memory image, packet capture, timeline, screenshot, report, or other artifact type. |
| `hash_ref` | Required where hash verification is applicable. |
| `analyst_reviewer` | Required when evidence influences final DFIR findings or customer-facing conclusions. |
| `agent_or_model_ref` | Required when AI-assisted review is used. |
| `outcome.status` | Recorded, accessed, validated, transformed, rejected, quarantined, or released. |

Evidence-derived outputs are not original evidence. Audit events must preserve the distinction between source evidence, derived summaries, and reviewed findings.

### Output Review and Release Events

Create audit events when internal case notes, customer reports, incident summaries, DFIR findings, notifications, or service records are reviewed and released.

Required fields include:

| Field | Requirement |
|---|---|
| `output_release_id` | Unique release record. |
| `output_type` | Internal case note, customer report, notification, DFIR report, incident closure, detection note, or service record. |
| `output_ref` | Stored output reference. |
| `agent_output_ref` | Required when AI contributed to the output. |
| `evidence_refs` | Required when the output contains findings, conclusions, recommendations, or customer-facing statements. |
| `judge_result_ref` | Required when AI assurance was used. |
| `review_record_id` | Required for reviewed outputs. |
| `approval_record_id` | Required for customer-facing, sensitive, or contractual outputs. |
| `destination_scope` | Internal, customer, legal, executive, service tower, tenant, or other destination. |
| `outcome.status` | Drafted, reviewed, approved, released, denied, withdrawn, or superseded. |

Customer-facing output must be traceable to evidence, review, and approval. The audit record should identify the released version and avoid embedding sensitive report content directly unless the audit store is authorized for that content.

### Fleet Rollout, Rollback, and Recall Events

Create audit events when shared agent packages, prompt packages, policy bundles, tool contracts, retrieval configurations, detection packages, playbooks, report templates, or sanitized intelligence are requested, built, validated, approved, rolled out, rolled back, recalled, or retired.

Required fields include:

| Field | Requirement |
|---|---|
| `release_id` | Package, detection, prompt, playbook, report-template, or sanitized-intelligence release identifier. |
| `rollout_id` | Required for staged rollout. |
| `rollback_id` | Required for rollback events. |
| `recall_id` | Required for recall or kill-switch events. |
| `package_ref` | Agent package, prompt package, model route, policy bundle, tool contract, detection, playbook, or report template. |
| `package_version` | Version being released, rolled back, recalled, or retired. |
| `rollback_target` | Required where rollback is supported or required. |
| `tenant_eligibility_result` | Included tenants, excluded tenants, cohorts, or service towers. |
| `approval_record_id` | Required for release, broad rollout, recall, or emergency override. |
| `monitoring_profile` | Monitoring gate or profile for the rollout. |
| `stage` | Validation, approval, canary, limited rollout, broad rollout, rollback, recall, or retired. |
| `outcome.status` | Requested, approved, released, blocked, rolled back, recalled, retired, or failed closed. |

Fleet events must support reconstruction of who approved the change, which tenants were eligible, which version ran, which tenants received it, which monitoring gates passed, and how rollback or recall was handled.

### Sanitized Intelligence Release Events

Create audit events when customer-derived learning is proposed for reuse outside the source tenant or case boundary.

Required fields include:

| Field | Requirement |
|---|---|
| `release_id` | Sanitized intelligence release identifier. |
| `source_scope_ref` | Internal authorized reference to the source tenant, case, or workflow. |
| `source_classification` | Sensitivity, evidence, legal, contractual, regulatory, sovereignty, and retention classification. |
| `sanitization_summary` | High-level description of what was removed or generalized. |
| `direct_identifier_check` | Pass, fail, or not applicable. |
| `indirect_identifier_check` | Pass, fail, or not applicable. |
| `evidence_support_ref` | Internal reference to source support or validation. |
| `review_record_id` | Reviewer record. |
| `approval_record_id` | Release approval record. |
| `policy_decision_id` | Policy decision for destination scope. |
| `destination_scope` | Exact approved destination. |
| `tenant_eligibility_result` | Included and excluded tenants or groups. |
| `recall_path` | Removal, rollback, quarantine, or disablement path. |
| `outcome.status` | Proposed, sanitized, approved, denied, released, recalled, or failed closed. |

Destination tenants must not receive source tenant identifiers, raw evidence references, source case identifiers, privileged context, or source-specific incident narratives through audit fields.

### Exception and Failure Events

Create audit events when a workflow is denied, blocked, escalated, fails closed, times out, violates a boundary, loses required auditability, or cannot validate policy, identity, approval, tenant, case, evidence, or tool scope.

Required fields include:

| Field | Requirement |
|---|---|
| `exception_id` | Unique exception or failure identifier. |
| `failed_control` | Identity, tenant scope, case scope, evidence reference, policy engine, approval, tool contract, audit logging, monitoring, or other failed control. |
| `attempted_action` | Action or release that was attempted. |
| `risk_classification` | Risk category or severity. |
| `failure_reason` | Controlled reason code. |
| `fail_closed` | True or false. |
| `containment_action` | Blocked, quarantined, denied, recalled, escalated, disabled, or reverted. |
| `affected_scope` | Tenant, case, agent, package, tool, output, evidence object, or release affected. |
| `next_required_action` | Review, approval, remediation, investigation, rollback, recall, or closeout. |
| `outcome.status` | Failed closed, escalated, contained, unresolved, remediated, or closed. |

A failure that cannot be audited is itself a critical audit condition. Workflows that require auditability must not proceed when audit logging is unavailable.

## Actor Model

Audit events should identify the actor without relying on free-form notes.

| Actor Type | Examples | Required Detail |
|---|---|---|
| `human` | Analyst, incident commander, customer approver, forensic reviewer, service owner | User or role reference, authority, approval scope where applicable. |
| `agent` | SOC analyst agent, threat hunting agent, response recommendation agent, forensic assistant | Agent ID, package version, owner, lifecycle state, tenant eligibility. |
| `judge` | Evidence support judge, unsupported-claim judge, tenant-boundary judge | Judge ID, version, evaluation type, output evaluated. |
| `policy_component` | PDP, policy engine, approval router | Component ID, policy bundle, decision or routing outcome. |
| `enforcement_component` | PEP, tool gateway, retrieval gateway, memory gateway | Component ID, enforced decision, allowed or blocked operation. |
| `tool` | SIEM query tool, endpoint isolation tool, identity tool, ticketing tool, evidence parser | Tool ID, contract version, operation, target, execution result. |
| `system` | Ingestion pipeline, context assembly service, monitoring service, fleet release service | Component ID, event type, state transition, result. |

When a system acts on behalf of an agent or human, the audit event should record both the executing component and the on-behalf-of identity.

## Scope Model

Audit events must preserve the boundary where the action occurred.

| Scope Field | Purpose |
|---|---|
| `tenant_id` | Tenant or customer security boundary. |
| `customer_id` | Managed-service customer boundary where applicable. |
| `case_id` | Incident, case, investigation, ticket, or DFIR matter boundary. |
| `workspace_id` | SIEM, XDR, cloud, case management, or evidence workspace boundary where applicable. |
| `environment_id` | Cloud account, subscription, project, SaaS tenant, endpoint group, or lab environment. |
| `service_tower` | MSSP, MDR, SOC, cloud IR, DFIR, detection engineering, threat hunting, or local/private DFIR. |
| `data_classification` | Sensitivity and handling rule. |
| `retention_label` | Retention requirement. |
| `sovereignty_scope` | Region, residency, or jurisdictional handling requirement where applicable. |
| `destination_scope` | Approved destination for outputs, releases, packages, or sanitized intelligence. |

Missing, ambiguous, or conflicting scope must block governed actions or route them to authorized review.

## Outcome Model

Audit events should use controlled outcome values rather than free-form result descriptions.

| Outcome | Meaning |
|---|---|
| `created` | Record, request, output, context package, or release was created. |
| `started` | Workflow, agent invocation, rollout stage, or tool process started. |
| `completed` | Workflow step completed without requiring execution-state semantics. |
| `allowed` | Policy or enforcement allowed a request. |
| `denied` | Policy or enforcement denied a request. |
| `approval_required` | Policy requires approval before execution or release. |
| `approved` | Authorized approver approved the scoped request. |
| `rejected` | Reviewer or approver rejected the request. |
| `executed` | Tool, action, or release executed. |
| `failed` | Workflow or action failed. |
| `failed_closed` | Workflow halted because required controls were missing or invalid. |
| `escalated` | Workflow was sent to a higher review or approval authority. |
| `rolled_back` | Version, release, detection, playbook, output, or action was reverted. |
| `recalled` | Package, version, session, credential, release, or intelligence item was recalled or disabled. |
| `superseded` | Record or release was replaced by a newer approved version. |
| `retired` | Agent, package, policy, prompt, release, or artifact was retired. |

Outcome values should be paired with reason codes where possible.

## Required Fields by Control Point

| Control Point | Required Audit Linkage |
|---|---|
| Agent receives context | `agent_id`, `agent_package_id`, `tenant_id`, `case_id`, `context_package_id`, `evidence_refs` where applicable. |
| Agent creates finding | `agent_output_ref`, `context_package_id`, `evidence_refs`, `confidence` or uncertainty where used, `requires_review`. |
| Judge evaluates output | `judge_result_ref`, `judge_id`, `judge_version`, `agent_output_ref`, `evaluation_result`. |
| Policy decision occurs | `policy_request_id`, `policy_decision_id`, `policy_bundle_ref`, `decision`, `decision_reason`. |
| Human approves | `approval_record_id`, `reviewer_id` or role, `approval_scope`, `decision`, `reviewed_refs`. |
| Tool executes | `tool_execution_id`, `tool_id`, `tool_contract_ref`, `policy_decision_id`, `approval_record_id` when required, `execution_result`. |
| Customer output releases | `output_release_id`, `output_ref`, `evidence_refs`, `review_record_id`, `approval_record_id`, `destination_scope`. |
| Evidence influences conclusion | `evidence_refs`, `chain_of_custody_ref` where applicable, reviewer reference, output or finding reference. |
| Fleet package rolls out | `release_id`, `rollout_id`, `package_ref`, `package_version`, `tenant_eligibility_result`, `approval_record_id`, `monitoring_profile`. |
| Fleet recall occurs | `recall_id`, `trigger_event_id`, `affected_package`, `affected_tenants`, `containment_actions`, `recovery_state`. |
| Sanitized intelligence propagates | `release_id`, `source_scope_ref`, `sanitization_summary`, `approval_record_id`, `policy_decision_id`, `destination_scope`, `recall_path`. |
| Failure occurs | `exception_id`, `failed_control`, `attempted_action`, `failure_reason`, `fail_closed`, `affected_scope`. |

## Data Handling Requirements

Audit records must avoid becoming another source of uncontrolled sensitive data.

Audit events should store controlled references instead of raw content when possible.

Use references for:

- raw logs and telemetry;
- prompts and context packages;
- model outputs;
- forensic artifacts;
- evidence images, memory captures, packet captures, and malware samples;
- customer reports;
- ticket content;
- email content;
- secrets, tokens, credentials, or sensitive identifiers;
- privileged, legal, or contractual material.

Directly embedding sensitive content in audit events should require an explicit storage and access-control decision. When audit records contain sensitive content, they must inherit the appropriate tenant, case, evidence, retention, sovereignty, and access restrictions.

## Integrity Requirements

Audit integrity controls should make records difficult to alter without detection.

Recommended integrity fields include:

| Field | Purpose |
|---|---|
| `record_hash` | Hash of the audit event payload or canonicalized record. |
| `previous_record_hash` | Optional chain link for ordered records where supported. |
| `signature` | Producer or audit service signature where supported. |
| `sequence_number` | Ordered sequence for a workflow, component, or audit stream. |
| `write_once_ref` | Reference to immutable or append-only storage. |
| `retention_label` | Retention requirement applied to the record. |
| `legal_hold` | Legal hold status where applicable. |
| `redaction_profile` | Redaction or masking profile applied to the record. |

Integrity metadata does not replace access control, tenant isolation, or evidence handling. It supports audit defensibility and replay confidence.

## Schema Versioning

Audit event producers should include `event_version` and avoid breaking existing consumers without a controlled migration.

Versioning rules:

1. Additive fields should be preferred over breaking field changes.
2. Required-field changes must be versioned.
3. Event type changes must preserve mapping to previous event semantics.
4. Deprecated fields should remain readable during migration.
5. Replay tools must understand the event versions needed for the replay window.
6. Field meaning must not change without a new version.

## Validation Rules

Audit events should be rejected, quarantined, or routed for remediation when validation fails.

Baseline validation rules:

- `audit_event_id` is unique.
- `event_type` is recognized.
- `event_version` is supported.
- `event_time` and `recorded_time` are present.
- `correlation_id` is present.
- `tenant_id` is present for tenant-scoped actions.
- `case_id` is present for case-scoped actions.
- actor identity is present.
- action and outcome are present.
- policy references exist for policy-mediated decisions.
- approval references exist when approval was required.
- evidence references exist for evidence-backed findings, reports, DFIR conclusions, and sensitive actions.
- tool execution events include tool contract and authorization references.
- fleet rollout events include package version, tenant eligibility, monitoring profile, and rollback target where required.
- sanitized intelligence releases include sanitization, destination scope, approval, policy decision, and recall path.

Validation failure must be audited as an exception event when the failed record relates to governed workflow behavior.

## Replay Requirements

An audit event is replay-ready when it can be placed into the workflow sequence and linked to the records that caused it and resulted from it.

Replay-ready audit events must include:

- `correlation_id`;
- `parent_event_id` or enough sequence metadata to reconstruct order;
- `causation_id` where a decision, failure, approval, or policy result caused the event;
- tenant, customer, case, or destination scope where applicable;
- actor identity;
- action and outcome;
- references to evidence, context, output, policy, approval, tool, package, or release records where applicable.

Replay should be able to answer:

1. What context was provided?
2. What did the agent or workflow produce?
3. What assurance checks occurred?
4. What policy decision was made?
5. Who approved or denied the action?
6. What tool, output, package, or release was affected?
7. What evidence supported the decision?
8. What failed, rolled back, or was recalled?

## Anti-Patterns

Avoid the following patterns:

- storing only a chat transcript as the audit record;
- storing only model output without policy, approval, evidence, and execution references;
- using correlation IDs as authorization tokens;
- embedding raw customer data in shared audit events without tenant and case controls;
- omitting agent package, prompt, model, policy, or tool-contract versions;
- logging tool execution without the authorizing policy decision;
- logging approval without the exact scope approved;
- treating Agent Judge output as an approval decision;
- releasing customer-facing output without evidence, review, and approval references;
- allowing fleet rollout without rollout, tenant eligibility, monitoring, and rollback audit events;
- allowing sanitized intelligence propagation without sanitization, destination-scope, policy, approval, and recall records;
- allowing governed workflow execution when audit logging is unavailable.

## Acceptance Criteria

The audit event model is acceptable when:

- every governed workflow emits structured audit events;
- events include stable identifiers, event types, timestamps, producer identity, actor identity, scope, action, outcome, and correlation data;
- tenant, customer, case, evidence, policy, approval, tool, output, and fleet release boundaries are represented where applicable;
- sensitive content is stored by controlled reference unless direct storage is explicitly authorized;
- agent, prompt, model, policy, tool-contract, and package versions are recorded where they influence behavior;
- policy decisions and human approvals are separate records;
- tool execution links back to policy decisions and approval records where required;
- evidence-backed findings and outputs link to evidence references;
- fleet rollout, rollback, recall, and sanitized intelligence propagation are replayable;
- denials, exceptions, and fail-closed events are audited;
- missing auditability blocks governed actions that require audit records.

## Related Repository Areas

- [`audit-correlation-model.md`](audit-correlation-model.md) for how audit records are linked into replayable chains.
- [`replayability-requirements.md`](replayability-requirements.md) for replay requirements and review workflows.
- [`exception-and-failure-audit.md`](exception-and-failure-audit.md) for denial, exception, and fail-closed audit behavior.
- [`fleet-rollout-audit-and-replay-model.md`](fleet-rollout-audit-and-replay-model.md) for fleet rollout, rollback, and recall audit requirements.
- [`immutable-audit-guidance.md`](immutable-audit-guidance.md) for storage integrity, immutability, and tamper-resistance guidance.
- [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) for evidence references, findings, and DFIR evidence handling.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) for PDP/PEP decisions, policy contracts, and fail-closed behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) for review, approval, customer approval, and escalation records.
