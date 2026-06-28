# Replayability Requirements

## Purpose

This document defines replayability requirements for governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

Replayability means a governed workflow can be reconstructed after the fact with enough fidelity to understand the original scope, inputs, decisions, approvals, actions, failures, and outcomes.

A replayable workflow should answer:

1. What was the original mission, tenant, customer, case, and evidence scope?
2. What context was available to the agent or workflow at the time?
3. What did the agent produce, recommend, request, or attempt?
4. What assurance, policy, approval, and enforcement decisions occurred?
5. What tools, outputs, reports, fleet packages, or shared intelligence were affected?
6. Which failures, denials, exceptions, overrides, rollbacks, or recalls occurred?
7. Can the decision path be reviewed without exposing data outside the authorized tenant, case, evidence, or release boundary?

## Scope

These requirements apply to workflows where agentic systems, AI-assisted workflows, automation, policy decisioning, human approval, evidence handling, tool execution, report release, fleet rollout, or sanitized intelligence propagation influence security operations.

In scope:

- telemetry ingestion, parsing, normalization, enrichment, and routing;
- tenant-scoped context assembly and retrieval;
- agent invocation, prompts, model routing, and structured outputs;
- AI assurance and Agent Judge evaluation;
- policy request, PDP decision, and PEP enforcement;
- human review, formal approval, customer approval, escalation, and emergency override;
- mediated tool execution;
- evidence reference creation, evidence access, evidence transformation, and DFIR review;
- customer-facing report, notification, or case-output release;
- fleet package validation, rollout, rollback, recall, and kill-switch activity;
- sanitized intelligence release and cross-tenant propagation;
- exception handling, denial, failure, and fail-closed behavior.

Out of scope:

- production database design;
- vendor-specific audit platform configuration;
- legal advice about evidentiary sufficiency or retention;
- complete audit event schema definition;
- immutable storage implementation details;
- SIEM, SOAR, case-management, or data-lake field mappings.

Detailed event fields belong in `audit-event-model.md`. Correlation rules belong in `audit-correlation-model.md`. Immutable storage guidance belongs in `immutable-audit-guidance.md`. Failure-specific audit handling belongs in `exception-and-failure-audit.md`. Fleet rollout replay belongs in `fleet-rollout-audit-and-replay-model.md`.

## Core Principle

Every governed workflow must be reconstructable from durable audit records, stable references, versioned artifacts, evidence links, policy decisions, approval records, tool execution results, and outcome records.

Replayability must preserve enough context to reconstruct decisions, approvals, evidence references, and outcomes without exposing data outside the authorized tenant, case, evidence, or release boundary.

Replayability does not require blindly re-running an LLM and expecting identical text. It requires preserving the records needed to understand and validate the original workflow state, inputs, decisions, controls, and outputs.

## What Replayability Means

For this architecture, replayability means the organization can reconstruct a governed workflow from trustworthy records.

| Property | Meaning |
|---|---|
| Correlatable | Events share identifiers that connect the full workflow chain. |
| Ordered | Events can be placed in the sequence in which they occurred. |
| Scope-bound | Tenant, customer, case, evidence, destination, and release boundaries are known. |
| Version-aware | Agents, prompts, policies, tools, models, detections, playbooks, and packages are tied to versions. |
| Evidence-linked | Findings, conclusions, approvals, and actions can be traced to evidence references where required. |
| Decision-backed | Policy decisions and approval outcomes are preserved. |
| Outcome-backed | Tool execution, report release, rollout, rollback, recall, or failure outcomes are recorded. |
| Tamper-evident where required | Critical events are protected from unauthorized modification or deletion. |
| Access-controlled | Replay does not become a way to expose tenant, case, evidence, or customer data to unauthorized viewers. |

Replayability does not mean:

- raw evidence must be copied into every audit record;
- sensitive evidence should be duplicated into a general audit store;
- replay viewers should automatically receive access to all referenced evidence;
- LLM output becomes evidence by being logged;
- a later model run proves the original output was correct;
- incomplete telemetry can be treated as complete because a replay exists;
- audit logs alone prove that a decision was appropriate.

## Replayability Objectives

Replayability supports several practical needs.

| Objective | Purpose |
|---|---|
| Investigation review | Reconstruct how a case, alert, escalation, report, or response decision was handled. |
| Customer assurance | Explain governed activity affecting a customer, tenant, environment, report, or service outcome. |
| DFIR defensibility | Show which evidence, prompts, outputs, reviews, and approvals supported a forensic conclusion. |
| Policy debugging | Determine why a policy allowed, denied, required approval, escalated, or failed closed. |
| Tool-action review | Confirm whether a tool action was authorized, scoped, executed, failed, reversed, or blocked. |
| Fleet safety review | Reconstruct rollout, tenant eligibility, validation gates, monitoring, rollback, and recall activity. |
| Sanitized intelligence review | Confirm how tenant-derived learning was sanitized, reviewed, approved, scoped, released, and monitored. |
| Exception review | Understand control failures, missing fields, denied actions, failed dependencies, emergency overrides, and remediation. |
| Assurance improvement | Identify where prompts, policy, evidence requirements, tool contracts, or approval workflows need correction. |

## Replay Scope

Replay scope must be explicit before records are collected or reviewed.

Common replay scopes include:

| Replay Scope | Description |
|---|---|
| Single action replay | Reconstruct one tool request, policy decision, approval, or output release. |
| Case replay | Reconstruct an incident, investigation, ticket, or DFIR case workflow. |
| Agent invocation replay | Reconstruct one agent task, context package, prompt, model route, output, judge result, and downstream decision path. |
| Evidence replay | Reconstruct how evidence was referenced, transformed, summarized, validated, or used in a finding. |
| Policy replay | Reconstruct the policy request, policy inputs, policy version, decision, reason, and enforcement result. |
| Approval replay | Reconstruct who reviewed or approved an action, what they saw, and what decision they made. |
| Tool execution replay | Reconstruct the mediated execution path, execution token, target, action, result, and follow-up. |
| Report replay | Reconstruct how a customer-facing report, notification, or final output was drafted, reviewed, approved, and released. |
| Fleet rollout replay | Reconstruct package validation, tenant eligibility, rollout gates, monitoring, rollback, recall, and final state. |
| Sanitized intelligence replay | Reconstruct sanitization, review, approval, destination scope, tenant eligibility, release, and recall path. |
| Failure replay | Reconstruct why a workflow denied, failed, escalated, or failed closed. |

The replay scope determines which audit events, records, evidence references, approvals, versions, and access controls are required.

## Minimum Replay Chain

A complete governed workflow should preserve a replay chain from request to outcome.

```text
Mission or workflow request
        ↓
Tenant, customer, case, and evidence scope resolution
        ↓
Context assembly and retrieval
        ↓
Agent invocation and output
        ↓
AI assurance or Agent Judge evaluation where used
        ↓
Policy request and PDP decision
        ↓
PEP enforcement
        ↓
Human or customer approval where required
        ↓
Mediated tool execution, output release, or workflow update
        ↓
Monitoring, validation, exception handling, rollback, or recall
        ↓
Final audit and replay record
```

Not every workflow requires every step. Read-only enrichment may not require human approval. A denied policy request may stop before tool execution. A fleet rollout may require validation and tenant eligibility before any runtime agent invocation occurs. Replayability requires the chain that actually occurred, including the missing or blocked steps that caused the workflow to stop.

## Required Replay Questions

A replay should be able to answer the following questions where applicable.

| Question | Required Evidence |
|---|---|
| What started the workflow? | Trigger event, request record, alert, ticket, case, fleet change request, or release request. |
| Who or what acted? | Actor identity, agent identity, analyst identity, tool identity, service identity, or workflow identity. |
| What authority did the actor have? | Agent lifecycle state, user role, scoped credential, tool contract, policy decision, approval record. |
| What tenant or customer was in scope? | Tenant ID, customer ID, service tower, workspace, subscription, account, environment, or case boundary. |
| What case or evidence was in scope? | Case ID, evidence references, evidence manifest, collection record, chain-of-custody record, data classification. |
| What context was supplied? | Context package reference, retrieval references, prompt reference, data minimization record, source metadata. |
| What output was produced? | Stored agent output, judge result, report draft, case note, recommendation, finding, or release package. |
| What decision was made? | Policy request, PDP decision, reason code, approval requirement, PEP enforcement result. |
| Who approved or denied? | Human approval record, customer approval record, emergency override record, denial reason. |
| What executed or changed? | Tool execution record, output release record, package activation, detection update, playbook update, rollback, recall. |
| What happened afterward? | Execution result, monitoring result, failure record, exception record, remediation record, closeout state. |
| Can it be safely reviewed? | Access-control decision, data minimization, tenant boundary, redaction, authorized evidence access. |

## Replay Record Categories

Replay depends on stable records across the architecture. The following record categories should be retained or referenced.

| Record Category | Replay Purpose |
|---|---|
| Request record | Shows the workflow, action, case, or release that was requested. |
| Scope record | Shows tenant, customer, case, evidence, destination, retention, and classification boundaries. |
| Context package record | Shows what data and retrieval results were supplied to the agent, judge, reviewer, or policy engine. |
| Prompt and model record | Shows prompt version, model route, model configuration reference, and generation settings where applicable. |
| Agent output record | Shows findings, recommendations, assumptions, requested actions, and evidence references. |
| Assurance record | Shows Agent Judge or review checks, unsupported-claim findings, evidence support, and risk flags. |
| Policy request record | Shows the action, target, risk, evidence, agent, tool, tenant, and approval context submitted for decision. |
| Policy decision record | Shows allow, deny, require-approval, fail-closed, reason code, policy version, and expiry. |
| Enforcement record | Shows PEP enforcement, token issuance, denial, blocked action, or scoped execution grant. |
| Approval record | Shows human, customer, service-owner, or emergency approval decision and conditions. |
| Tool execution record | Shows tool, operation, target, token, result, error, and side effects. |
| Evidence record | Shows source evidence references, transformations, derived artifacts, chain-of-custody events, and finding support. |
| Output release record | Shows case note, report, notification, detection, playbook, or template release and review state. |
| Fleet record | Shows package, version, eligibility, validation, rollout, rollback, recall, and kill-switch activity. |
| Sanitized intelligence record | Shows source classification, sanitization, review, destination scope, release channel, and recall path. |
| Failure record | Shows exception, denial, missing control, failed dependency, retry, escalation, or fail-closed result. |
| Monitoring record | Shows post-action health, anomalies, policy denials, rollback triggers, and customer-impact indicators. |

## Replay Identifiers

Replay requires stable identifiers across records. The following identifiers should be carried consistently where applicable.

| Identifier | Requirement |
|---|---|
| `correlation_id` | Required for end-to-end replay across a workflow. |
| `workflow_id` | Required where a named workflow, playbook, investigation path, or release path is used. |
| `audit_event_id` | Required for each audit event. |
| `parent_event_id` | Recommended for event ordering and hierarchy. |
| `causation_id` | Recommended to show which event caused another event. |
| `tenant_id` | Required for tenant-scoped activity. |
| `customer_id` | Required for customer-scoped service activity. |
| `case_id` | Required for incident, investigation, ticket, matter, or DFIR activity. |
| `evidence_ref` | Required when evidence supports a finding, conclusion, approval, policy decision, or action. |
| `agent_id` | Required when an agent participates. |
| `agent_package_id` | Required when a versioned agent package participates. |
| `prompt_ref` | Required when prompt content influences output or decision support. |
| `model_ref` | Required when model route or model configuration influences output. |
| `judge_result_id` | Required when an assurance result influences routing, policy, approval, or release. |
| `policy_request_id` | Required when policy evaluation occurs. |
| `policy_decision_id` | Required when a PDP decision occurs. |
| `approval_record_id` | Required when approval is requested, granted, denied, expired, or overridden. |
| `tool_execution_id` | Required when a mediated tool action occurs. |
| `fleet_release_id` | Required for fleet rollout, rollback, recall, or package release. |
| `sanitized_intelligence_release_id` | Required for cross-tenant sanitized intelligence release. |

Identifiers must not be reused across unrelated workflows. Identifiers that reveal customer-sensitive information should be opaque or access-controlled.

## Replay Data Handling

Replay records must preserve context without becoming a cross-tenant data exposure path.

Required handling rules:

- store references to raw evidence rather than copying raw evidence into general audit records;
- protect audit records that contain sensitive tenant, customer, case, or evidence metadata;
- redact or minimize secrets, credentials, tokens, private keys, session artifacts, and unnecessary raw payloads;
- preserve hashes, versions, and stable references where raw data cannot be retained in the audit store;
- enforce tenant-aware access control for replay queries;
- prevent replay tooling from joining records across tenants unless explicitly authorized;
- prevent replay reports from exposing source tenant context to destination tenants;
- maintain separate access paths for audit metadata and original evidence.

Replayability must not weaken tenant isolation or evidence handling.

## Replay Requirements by Workflow Stage

### 1. Ingestion and Normalization Replay

Ingestion replay reconstructs how telemetry, alerts, tickets, threat intelligence, logs, or forensic artifacts entered the workflow.

Required records:

| Requirement | Description |
|---|---|
| Source system identity | Original platform, connector, collector, export source, or evidence acquisition method. |
| Source timestamp | Time the source event or artifact was created or collected. |
| Ingestion timestamp | Time the platform received or recorded the item. |
| Tenant and customer scope | Tenant, customer, workspace, account, subscription, project, environment, or service boundary. |
| Case linkage | Case, incident, ticket, investigation, matter, or workflow identifier where applicable. |
| Source metadata | Original event ID, collector ID, parser version, schema version, data classification, and retention label. |
| Transformation record | Normalization, parsing, enrichment, filtering, deduplication, suppression, or routing actions. |
| Evidence reference | Stable reference to the source item or evidence object when used downstream. |
| Failure record | Rejection, schema failure, malformed data, missing tenant ID, or incomplete ingestion state. |

Replay must show whether the downstream agent or reviewer used raw source data, normalized data, enriched data, a summary, or a derived evidence reference.

### 2. Context Assembly and Retrieval Replay

Context replay reconstructs what information was supplied to an agent, judge, reviewer, policy engine, or report workflow.

Required records:

| Requirement | Description |
|---|---|
| Context package ID | Stable identifier for the assembled context. |
| Context purpose | Task objective, workflow stage, agent role, reviewer role, policy decision, or report purpose. |
| Tenant and case filters | Filters used to limit retrieval and context assembly. |
| Retrieval sources | Indexes, evidence repositories, case systems, threat-intelligence sources, or knowledge bases queried. |
| Retrieved references | Evidence refs, document refs, alert refs, event refs, ticket refs, knowledge refs, or sanitized intelligence refs. |
| Excluded material | Material intentionally excluded due to scope, sensitivity, retention, policy, or minimization. |
| Untrusted-content marking | Prompt-injection risk, user-supplied content, log content, email content, or external enrichment labeling. |
| Context version | Version of context assembler, retrieval configuration, filters, and minimization policy. |
| Hash or digest | Hash of the assembled context package where feasible. |

Replay must identify the context available at the time of the original workflow, not the current state of the case or retrieval index.

### 3. Agent Invocation and Output Replay

Agent replay reconstructs which agent ran, under which identity, using which package, prompt, model route, context, and restrictions.

Required records:

| Requirement | Description |
|---|---|
| Agent identity | Registered agent ID, owner, lifecycle state, risk tier, and service tower. |
| Agent package version | Versioned package including prompt package, model route, tool contracts, policy bundle, retrieval config, and monitoring profile. |
| Invocation reason | Task request, alert, ticket, workflow stage, analyst request, or fleet-triggered action. |
| Prompt reference | Prompt, template, system instruction, task instruction, or output-format reference. |
| Model reference | Model route, deployment, local/private model reference, or approved runtime route. |
| Context package reference | Exact context package supplied to the agent. |
| Runtime constraints | Tool restrictions, output schema, action restrictions, tenant scope, evidence requirements, and memory scope. |
| Agent output reference | Stored structured output, findings, recommendations, assumptions, requested actions, confidence, and evidence references. |
| Error or refusal state | Failed invocation, timeout, blocked prompt, insufficient context, refusal, or guardrail stop. |

Replay must preserve the original agent output. A later model re-run may be useful for evaluation, but it is not the original event.

### 4. AI Assurance and Agent Judge Replay

Assurance replay reconstructs how agent output was evaluated before routing, policy, approval, reporting, or execution.

Required records:

| Requirement | Description |
|---|---|
| Judge or assurance identity | Judge ID, review control, evaluator version, owner, and purpose. |
| Input reference | Agent output, context package, report draft, evidence references, or release candidate evaluated. |
| Evaluation criteria | Evidence support, unsupported claims, tenant boundary risk, HITL requirement, output quality, report suitability, or policy fit. |
| Evaluation result | Pass, fail, requires review, requires more evidence, unsupported claim found, boundary risk found, or other normalized result. |
| Rationale | Short reason or finding explaining the result. |
| Downstream effect | Whether the result informed policy, approval routing, remediation, report review, or blocking. |
| Limitations | Known evaluator limitations, skipped checks, incomplete inputs, or confidence caveats. |

Agent Judge output must remain replayable as an assurance signal. It must not be treated as policy authorization or human approval.

### 5. Policy and Enforcement Replay

Policy replay reconstructs why a workflow was allowed, denied, routed for approval, escalated, or failed closed.

Required records:

| Requirement | Description |
|---|---|
| Policy request | Requested action, target, tool, tenant, customer, case, agent, analyst, risk, evidence refs, and requested scope. |
| Policy bundle version | Policy set, ruleset, decision table, or policy-as-code version used at decision time. |
| Input attributes | Attributes evaluated by the policy engine, including tenant, risk, action, tool, evidence, approval, classification, and service obligations. |
| Decision | `ALLOW`, `DENY`, `REQUIRE_REVIEW`, `REQUIRE_APPROVAL`, or `FAIL_CLOSED`, with reason code, escalation reason, or fail-closed reason where applicable. |
| Decision reason | Reason code or policy rationale. |
| Decision expiry | Time limit, token lifetime, or revalidation requirement. |
| PEP enforcement | Whether the decision was enforced, blocked, converted into an execution token, or routed to approval. |
| Enforcement failure | Missing decision, stale decision, invalid token, policy engine unavailable, schema failure, or PEP denial. |

Replay must show the policy that existed at the time of the original decision. Current policy state is not enough.

### 6. Human, Customer, and Emergency Approval Replay

Approval replay reconstructs accountable review and authorization decisions.

Required records:

| Requirement | Description |
|---|---|
| Approval request | Requested action, output, release, exception, or fleet change requiring approval. |
| Approver identity | Human, role, customer approver, service owner, incident commander, forensic reviewer, or emergency approver. |
| Approval authority | Basis for approval authority, role membership, customer authorization, or escalation path. |
| Materials reviewed | Agent output, evidence refs, judge result, policy decision, risk classification, tool target, report draft, or release record. |
| Decision | Approved, denied, returned for more evidence, escalated, expired, withdrawn, or emergency override. |
| Conditions | Scope, target, time limit, tenant, customer, case, or operational constraints applied to approval. |
| Separation of duties | Whether requester, reviewer, approver, and executor were separate where required. |
| Expiry or revocation | Approval expiration, revocation, supersession, or invalidation record. |

Replay must distinguish human review from formal approval. Review may assess quality. Approval authorizes a governed action, output, exception, or release within scope.

### 7. Tool Execution Replay

Tool replay reconstructs how an approved action moved from request to execution and outcome.

Required records:

| Requirement | Description |
|---|---|
| Tool identity | Registered tool name, owner, contract version, operation, and risk class. |
| Tool request | Requested operation, target, inputs, tenant, case, evidence support, and requesting agent or user. |
| Authorization path | Policy decision, approval record, execution token, and PEP enforcement result. |
| Execution token | Token ID, scope, claims, expiry, and binding to policy decision and approval where applicable. |
| Target validation | Target tenant, asset, identity, endpoint, evidence object, cloud resource, or case record validation. |
| Execution result | Success, failure, partial success, no-op, timeout, denied by downstream system, or reversed. |
| Side effects | Case update, endpoint state change, identity change, detection change, report release, or rollback action. |
| Error handling | Retry, compensation action, escalation, manual intervention, or fail-closed state. |

Replay must be able to show that the tool executed only the action authorized by policy and approval.

### 8. Evidence and DFIR Replay

Evidence replay reconstructs how source evidence supported findings, conclusions, approvals, reports, or actions.

Required records:

| Requirement | Description |
|---|---|
| Evidence reference | Stable evidence URI, manifest ID, artifact ID, or case evidence reference. |
| Evidence source | Collection method, source system, device, log source, image, memory capture, export, or artifact origin. |
| Evidence metadata | Collection time, collector, hash, classification, chain-of-custody record, and retention label. |
| Transformation history | Parsing, normalization, extraction, summarization, timeline generation, enrichment, or derived artifact creation. |
| Finding support | Which evidence references support which finding, report statement, recommendation, or DFIR conclusion. |
| Reviewer validation | Analyst or forensic reviewer confirmation, rejection, correction, or limitation. |
| Local/private model use | Local model reference, prompt reference, evidence subset, output reference, and validation record where applicable. |
| Evidence boundary | Tenant, case, legal hold, retention, sovereignty, and access constraints. |

Replay must not treat model summaries as source evidence. Model output may help explain evidence, but the source reference remains the evidence anchor.

### 9. Output and Report Release Replay

Output replay reconstructs how internal notes, customer-facing reports, notifications, investigation summaries, or final conclusions were drafted, reviewed, approved, and released.

Required records:

| Requirement | Description |
|---|---|
| Draft reference | Agent-generated draft, analyst draft, report template, or case note reference. |
| Evidence support | Evidence references supporting material findings, conclusions, recommendations, or customer-facing statements. |
| Review record | Reviewer identity, review criteria, corrections, unsupported claim removal, and approval status. |
| Policy decision | Release policy evaluation where required. |
| Customer approval | Customer authorization where customer-facing release or contractual obligation requires it. |
| Released output | Final released version, destination, audience, timestamp, and release channel. |
| Redaction or limitation | Redactions, confidence limitations, known gaps, and excluded claims. |
| Supersession | Correction, revision, withdrawal, reissue, or replacement record. |

Replay must distinguish drafts from released outputs.

### 10. Fleet Rollout, Rollback, and Recall Replay

Fleet replay reconstructs how shared agent packages, prompts, tools, policy bundles, detection packages, playbooks, report templates, retrieval configurations, or sanitized intelligence were changed across tenants or environments.

Required records:

| Requirement | Description |
|---|---|
| Change request | Proposed change, owner, affected package, reason, risk tier, and expected behavior. |
| Package manifest | Agent package, prompt version, model route, policy bundle, tool contracts, retrieval configuration, monitoring profile, and rollback target. |
| Validation evidence | Test results for policy behavior, tenant isolation, tool scope, output quality, evidence support, rollback, and monitoring. |
| Approval record | Engineering, service-owner, policy-owner, security, customer, or emergency approval where required. |
| Tenant eligibility | Included tenants, excluded tenants, service tiers, data-residency limits, and contractual restrictions. |
| Rollout stage | Canary, cohort, broad rollout, activation, pause, rollback, recall, or retired state. |
| Monitoring gates | Metrics, thresholds, denials, fail-closed events, unsupported claims, boundary violations, and customer impact. |
| Rollback or recall | Trigger, scope, action taken, version pinned, sessions terminated, access revoked, and final state. |

Replay must show which tenants or environments were eligible, which actually received the change, and how the change could be stopped or reversed.

### 11. Sanitized Intelligence Release Replay

Sanitized intelligence replay reconstructs how learning derived from one tenant, case, or evidence boundary became approved shared intelligence.

Required records:

| Requirement | Description |
|---|---|
| Source classification | Source tenant reference, source case reference, sensitivity, retention, sovereignty, legal, contractual, and evidence status. |
| Release category | Detection logic, playbook, prompt improvement, report template, enrichment logic, indicator, behavior pattern, or package update. |
| Sanitization record | What was removed, generalized, retained, and transformed. |
| Leakage checks | Direct identifier, indirect re-identification, privileged context, unsupported claim, and tenant boundary checks. |
| Human review | Reviewer decision on sanitization quality and operational value. |
| Policy decision | Release decision, destination scope, tenant eligibility, and restrictions. |
| Release channel | Detection repository, prompt package, retrieval corpus, playbook library, report template, or agent package. |
| Monitoring and recall | Adoption, false positives, boundary exceptions, recall trigger, removal path, and final state. |

Replay must not expose source evidence or source tenant context to destination tenants.

### 12. Exception and Failure Replay

Failure replay reconstructs what went wrong, what control stopped or allowed the workflow, and what remediation occurred.

Required records:

| Requirement | Description |
|---|---|
| Failure type | Denial, missing field, failed dependency, timeout, schema error, policy failure, approval failure, tool failure, audit failure, or boundary violation. |
| Failing control | Policy engine, PEP, agent registry, context assembler, retrieval filter, approval workflow, tool gateway, audit logger, or monitoring gate. |
| Required control state | The field, approval, decision, identity, evidence, policy, tenant scope, or audit path that was missing or invalid. |
| Actual outcome | Denied, failed closed, escalated, retried, quarantined, rolled back, recalled, or manually handled. |
| Impact scope | Tenant, customer, case, agent version, tool, package, output, evidence object, or destination scope affected. |
| Remediation | Corrective action, owner, due date, exception closure, or control improvement. |

Replay must include denied and blocked activity. Denials are important control evidence, not noise.

## Replay Packet

A replay packet is a curated set of references and records used to reconstruct a workflow.

A replay packet should not automatically duplicate raw evidence or expose protected customer data. It should contain enough metadata and references for an authorized reviewer to retrieve source material through the correct access path.

Example replay packet shape:

```json
{
  "replay_packet_id": "replay-2026-05-22-10422",
  "replay_scope": "case_replay",
  "correlation_id": "corr-2026-05-22-10422",
  "scope": {
    "tenant_id": "customer-a",
    "customer_id": "cust-a",
    "case_id": "inc-10422",
    "service_tower": "mdr",
    "data_classification": "customer-security-telemetry"
  },
  "records": {
    "trigger_event_ids": ["audit-0001"],
    "context_package_ids": ["ctx-10422-0003"],
    "agent_invocation_ids": ["agent-run-10422-0004"],
    "agent_output_ids": ["agent-output-10422-0004"],
    "judge_result_ids": ["judge-result-10422-0005"],
    "policy_request_ids": ["policy-req-10422-0006"],
    "policy_decision_ids": ["policy-decision-10422-0006"],
    "approval_record_ids": ["approval-10422-0007"],
    "tool_execution_ids": ["tool-exec-10422-0008"],
    "output_release_ids": ["case-note-release-10422-0009"],
    "failure_record_ids": []
  },
  "versions": {
    "agent_package_id": "response-recommendation-agent@1.6.3",
    "prompt_package": "response-recommendation-prompts@2.4.1",
    "policy_bundle": "mdr-response-policy@3.2.0",
    "tool_contracts": ["endpoint-isolation-tool@1.8.0"],
    "context_assembler": "tenant-context-assembler@2.1.5"
  },
  "evidence": {
    "evidence_refs": [
      "evidence://customer-a/inc-10422/events/evt-001",
      "evidence://customer-a/inc-10422/events/evt-004"
    ],
    "evidence_access_required": true,
    "raw_evidence_included": false
  },
  "integrity": {
    "audit_chain_verified": true,
    "missing_required_events": [],
    "replay_generated_at": "2026-05-22T14:05:00Z"
  }
}
```

This example is an architecture record shape. Implementations should validate replay packets through controlled schemas, access control, retention policy, and immutable audit storage.

## Replay Procedure

A standard replay procedure should follow a controlled sequence.

| Step | Activity |
|---|---|
| 1. Define replay scope | Identify whether the replay covers an action, case, agent invocation, policy decision, tool execution, report, fleet rollout, sanitized intelligence release, or failure. |
| 2. Authorize replay access | Confirm reviewer access to tenant, customer, case, evidence, fleet, or release records. |
| 3. Collect audit chain | Retrieve correlated events by `correlation_id`, parent event, causation ID, workflow ID, case ID, release ID, or package ID. |
| 4. Verify integrity | Check event completeness, ordering, hash, signature, append-only state, and missing required records. |
| 5. Reconstruct scope | Confirm tenant, customer, case, evidence, destination, retention, and sovereignty boundaries. |
| 6. Reconstruct versions | Identify agent, prompt, model, policy, tool, detection, playbook, report template, and package versions active at the time. |
| 7. Reconstruct context | Identify what context, retrieval results, evidence references, and exclusions were available. |
| 8. Review outputs | Inspect agent output, judge result, report draft, release item, or derived intelligence. |
| 9. Review decisions | Inspect policy decisions, enforcement actions, approvals, denials, overrides, and fail-closed events. |
| 10. Review outcomes | Inspect tool execution, output release, package rollout, rollback, recall, monitoring, or exception outcomes. |
| 11. Record replay finding | Document what was confirmed, what could not be reconstructed, and what remediation is required. |

Replay should be read-only by default. Any corrective action must be performed through governed change, case, evidence, tool, or fleet processes.

## Replay Findings

A replay should produce a concise finding record.

Recommended fields:

| Field | Purpose |
|---|---|
| `replay_finding_id` | Unique identifier for the replay result. |
| `replay_packet_id` | Reference to the replay packet used. |
| `replay_scope` | Action, case, policy, approval, tool, output, fleet, intelligence release, or failure scope. |
| `reviewer` | Person or team that performed the replay. |
| `authorized_scope` | Tenant, customer, case, evidence, package, or release scope reviewed. |
| `reconstruction_status` | Complete, partial, blocked, failed, or not replayable. |
| `missing_records` | Required records not found or not accessible. |
| `scope_findings` | Tenant, case, evidence, destination, or access-boundary observations. |
| `decision_findings` | Policy, approval, enforcement, exception, or fail-closed observations. |
| `outcome_findings` | Tool, report, rollout, rollback, recall, or monitoring observations. |
| `remediation_required` | Yes or no, with owner and recommended action. |

## Deterministic Replay and Contextual Replay

Agentic workflows often include non-deterministic model behavior. Replay requirements must distinguish deterministic reconstruction from contextual evaluation.

| Replay Type | Meaning |
|---|---|
| Deterministic replay | Reconstruct exact recorded events, records, versions, decisions, approvals, and outcomes. |
| Contextual replay | Reconstruct the context and evaluate whether the original output or decision was reasonable based on available records. |
| Re-execution test | Run a model, policy, tool simulator, or validation workflow again in a controlled environment for comparison. |

Deterministic replay is required for governance. Contextual replay is useful for quality review. Re-execution tests are optional validation aids and must not replace the original audit record.

When model re-execution is performed, the replay record should preserve:

- reason for re-execution;
- model route used for re-execution;
- whether the original model version was available;
- whether the original context was reconstructed exactly or approximately;
- differences between original output and re-execution output;
- reviewer conclusion.

## Versioning Requirements

Replay requires version-aware records for all artifacts that influence behavior.

Required version references include, where applicable:

- agent package version;
- prompt package version;
- model route or local/private model reference;
- context assembler version;
- retrieval configuration version;
- vector index or knowledge corpus version;
- policy bundle version;
- tool contract version;
- execution token contract version;
- approval workflow version;
- detection package version;
- playbook version;
- report template version;
- sanitizer or release workflow version;
- monitoring profile version;
- schema version for audit events and replay packets.

A workflow is not fully replayable when a material behavior-changing artifact lacks a stable version reference.

## Handling Mutable Systems

Operational systems change over time. Replay must avoid relying only on current state.

| Mutable System | Replay Requirement |
|---|---|
| Case management | Preserve case state changes as events rather than relying only on current status. |
| Agent registry | Preserve lifecycle state, owner, tool scope, and package version at time of action. |
| Policy engine | Preserve policy bundle version and evaluated inputs. |
| Approval workflow | Preserve approval request, decision, approver authority, conditions, and expiry. |
| Tool registry | Preserve tool contract version, allowed operations, and execution constraints at time of action. |
| Retrieval index | Preserve retrieved document references, index version, filters, and recall state. |
| Evidence store | Preserve evidence reference, metadata, hash, chain-of-custody state, and access path. |
| Fleet registry | Preserve package manifest, eligibility, rollout stage, rollback target, and recall state. |
| Report repository | Preserve draft, review, approval, release, revision, and supersession events. |

Mutable operational state may be updated. Replay requires the historical path to that state.

## Missing or Partial Replay

A workflow should be marked partially replayable or not replayable when critical records are missing.

| Missing Item | Impact |
|---|---|
| Missing `correlation_id` | Events cannot be reliably connected into one chain. |
| Missing tenant or customer scope | Tenant boundary cannot be validated. |
| Missing case ID | Investigation or incident context cannot be reconstructed. |
| Missing evidence references | Findings, approvals, or actions may not be evidence-backed. |
| Missing agent package version | Agent behavior cannot be reconstructed. |
| Missing prompt or context reference | Agent input cannot be reviewed. |
| Missing policy decision | Authorization path cannot be proven. |
| Missing approval record | Sensitive action or release may not be accountable. |
| Missing tool execution result | Outcome and side effects cannot be confirmed. |
| Missing audit integrity metadata | Record tampering or ordering concerns may remain unresolved. |
| Missing rollback or recall record | Fleet or release recovery cannot be proven. |

Missing replay records should create a follow-up action. For sensitive actions, customer-facing outputs, DFIR findings, fleet releases, and cross-tenant propagation, missing critical replay records should trigger escalation or remediation.

## Access Control for Replay

Replay access must be governed.

Required controls:

- authorize replay requests by role, tenant, customer, case, evidence, package, or release scope;
- log replay access, queries, exports, and reports;
- prevent replay users from crossing tenant or customer boundaries without explicit authorization;
- restrict raw evidence access to authorized reviewers;
- redact sensitive fields in replay outputs where the reviewer does not need raw values;
- protect privileged, legal, regulated, customer-confidential, and evidence-sensitive records;
- separate internal source references from destination-tenant-visible replay outputs;
- preserve audit of who replayed what and why.

Replay tooling must not become a privileged bypass around tenant isolation, evidence controls, or customer confidentiality.

## Replay and Retention

Replayability depends on retention alignment across audit, evidence, policy, approval, tool, and fleet records.

Requirements:

- define retention labels for audit records, evidence references, context packages, agent outputs, policy decisions, approvals, and tool execution records;
- avoid storing raw evidence in general audit logs unless explicitly required and controlled;
- preserve hashes or stable references when raw evidence follows a different retention policy;
- mark records affected by legal hold or investigation hold;
- handle deletion or expiry through auditable lifecycle events;
- preserve enough metadata to explain that a record was lawfully expired or removed;
- ensure recalled fleet material and sanitized intelligence release records remain replayable after removal from runtime systems.

A replay chain may be valid even when raw evidence is no longer retained, but the replay finding must clearly state the limitation.

## Replay and Monitoring

Monitoring records should support replay of post-action behavior.

Monitoring replay should include:

- policy denials and fail-closed counts;
- agent invocation anomalies;
- unsupported-claim rates;
- evidence-support failures;
- tenant-boundary check failures;
- tool errors and retries;
- approval queue age and bypass attempts;
- fleet version drift;
- rollout gate failures;
- recall triggers;
- customer-impacting exceptions;
- detection false-positive spikes after release;
- retrieval of stale, recalled, or superseded intelligence.

Monitoring records do not replace audit events. They provide operational signals that help interpret outcomes.

## Local and Private LLM DFIR Replay

Private/local LLM-assisted DFIR may run in isolated, offline, customer-controlled, or evidence-sensitive environments. Replay requirements still apply.

Required controls:

- record local model reference, version, runtime environment, and configuration where available;
- record prompt reference, prompt hash, or approved template reference;
- record the evidence subset supplied to the model;
- preserve evidence references and chain-of-custody metadata;
- record generated output and reviewer validation;
- distinguish source evidence from model interpretation;
- preserve export audit when replay records are moved from an isolated environment to a central audit system;
- prevent raw forensic evidence from being copied into replay packages unless explicitly authorized;
- document gaps when an air-gapped or isolated environment cannot export complete logs.

DFIR replay should support review of evidence handling and conclusion support, not just agent behavior.

## Fleet and Cross-Tenant Replay

Fleet and cross-tenant replay must preserve both source and destination controls.

For fleet package replay, records must show:

- package manifest;
- validation evidence;
- policy approval;
- tenant eligibility;
- rollout stage;
- monitoring gates;
- rollback target;
- recall path;
- tenants or environments affected;
- final state.

For sanitized intelligence replay, records must show:

- source classification;
- sanitization summary;
- reviewer decision;
- policy decision;
- destination scope;
- tenant eligibility;
- release channel;
- monitoring;
- recall or removal path.

Replay must not expose source tenant details to destination tenants. Source traceability should remain available only to authorized reviewers.

## Fail-Closed Conditions

Replayability controls should fail closed or escalate when required replay data is missing or invalid for sensitive workflows.

Fail-closed examples:

- audit logging unavailable for a sensitive action;
- `correlation_id` missing for a governed workflow;
- tenant ID missing or ambiguous;
- evidence reference missing for a finding, DFIR conclusion, or sensitive action;
- policy decision missing before tool execution;
- approval record missing for an approval-required action;
- tool execution token missing or outside approved scope;
- agent package version unknown or recalled;
- fleet rollout lacks rollback target;
- sanitized intelligence release lacks sanitization record;
- replay chain cannot distinguish draft from released output;
- audit events cannot be written to the required immutable store;
- replay access request crosses tenant boundaries without authorization.

Where fail-closed behavior is not possible because the workflow already occurred, the replay finding should mark the workflow as deficient and route to remediation.

## Anti-Patterns

Avoid:

- relying on chat transcript exports as the audit record;
- storing raw evidence in general audit logs without need or controls;
- treating model re-execution as proof of the original decision;
- relying on current policy or current agent version to explain a past action;
- omitting denied, blocked, or fail-closed events from audit;
- allowing agents to write directly to shared memory without replayable release records;
- losing tenant scope during context assembly or report generation;
- recording approval without recording what was approved;
- recording tool execution without policy decision and approval linkage;
- recording a fleet rollout without tenant eligibility and rollback target;
- making replay reports visible to tenants or teams outside their authorized scope;
- treating audit storage as a replacement for evidence chain of custody.

## Acceptance Criteria

A governed workflow is replayable when all applicable criteria are met:

- the workflow has an end-to-end `correlation_id`;
- tenant, customer, case, evidence, destination, or release scope is explicit;
- source records, context packages, prompts, models, agent packages, policies, tools, approvals, and outputs are versioned or referenced;
- agent outputs are stored or referenced separately from source evidence;
- findings, DFIR conclusions, customer-facing outputs, and sensitive actions preserve evidence references;
- policy requests and decisions are preserved with reason codes and policy versions;
- PEP enforcement and execution-token behavior are recorded where applicable;
- human, customer, service-owner, or emergency approvals are recorded when required;
- tool execution records show target, scope, authorization, result, and side effects;
- failures, denials, exceptions, and fail-closed events are recorded;
- fleet rollout, rollback, recall, and sanitized intelligence release records include tenant eligibility and rollback or recall paths;
- immutable audit handling is applied to critical records where required;
- replay access is tenant-aware, case-aware, and evidence-aware;
- a reviewer can produce a replay finding that states what happened, what was authorized, what evidence supported it, what changed, and what limitations remain.

## Related Repository Areas

- [`audit-event-model.md`](audit-event-model.md) for audit event structure and event categories.
- [`audit-correlation-model.md`](audit-correlation-model.md) for correlation identifiers and replay chain linkage.
- [`exception-and-failure-audit.md`](exception-and-failure-audit.md) for denial, exception, failure, escalation, and fail-closed records.
- [`fleet-rollout-audit-and-replay-model.md`](fleet-rollout-audit-and-replay-model.md) for fleet release, rollback, recall, and package replay.
- [`immutable-audit-guidance.md`](immutable-audit-guidance.md) for tamper-evident audit storage guidance.
- [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) for evidence references, finding support, and DFIR evidence handling.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) for tenant boundary and cross-tenant replay constraints.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) for policy decision and enforcement behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) for review, approval, customer authorization, and escalation records.
