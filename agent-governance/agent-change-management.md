# Agent Change Management

## Purpose

This document defines change-management requirements for governed agents in Agentic MSSP / MDR / DFIR security operations.

Agent behavior can change through prompts, models, tools, policies, retrieval sources, memory behavior, workflow configuration, orchestration logic, safety checks, output formats, and fleet packaging. These changes must be controlled because even a small change can affect tenant boundaries, evidence handling, policy decisions, customer-facing output, or privileged action paths.

## Core Principle

Agent behavior is production behavior when it can influence security operations.

Changes to agent behavior must be reviewed, tested, approved, versioned, monitored, and rollback-capable before they are used in governed workflows.

## Change Categories

| Change Type | Examples | Risk Considerations |
|---|---|---|
| Prompt or instruction | System prompt, task prompt, guardrail instruction, output rubric. | Can alter reasoning, risk posture, refusal behavior, evidence support, or output style. |
| Model | Model provider, model version, local model, fine-tune, inference parameters. | Can alter quality, latency, hallucination risk, privacy boundary, or tool-use behavior. |
| Tool contract | New tool, modified parameters, expanded action, changed permission. | Can introduce state-changing or privileged capability. |
| Policy | PDP rules, approval thresholds, risk classification, exceptions, fail-closed rules. | Can change authorization behavior. |
| PEP behavior | Tool wrapper, enforcement gateway, validation, parameter filtering. | Can weaken or strengthen actual execution controls. |
| Retrieval or memory | RAG source, vector index, memory write policy, case memory, shared intelligence. | Can create tenant, case, retention, or evidence contamination risk. |
| Workflow | Orchestration steps, delegation path, escalation route, retry logic. | Can bypass review or change when actions occur. |
| Output | Report template, customer message format, case note schema, evidence citation rules. | Can affect customer-facing accuracy and auditability. |
| Monitoring | Telemetry fields, alert thresholds, dashboards, anomaly rules. | Can hide or surface risky behavior. |
| Fleet packaging | Signed package, deployment artifact, release channel, cohort rules. | Can propagate defects across customers or tenants. |

## Risk Classification

Every change should be classified before approval.

| Risk Level | Typical Change | Minimum Governance |
|---|---|---|
| Low | Wording clarification, non-functional documentation, dashboard label. | Owner review and audit record. |
| Medium | Prompt tuning, output format change, new read-only retrieval source, minor workflow refinement. | Peer review, policy check, test evidence, owner approval. |
| High | New tool, expanded data scope, customer-facing output change, evidence-support change, model upgrade. | Security review, service-owner approval, validation evidence, rollback plan, staged rollout. |
| Critical | State-changing tool, tenant-scope expansion, fleet-wide rollout, policy exception, evidence modification path. | Formal change approval, human/customer authority where applicable, canary rollout, monitoring, emergency rollback/recall plan. |

Risk classification should consider tenant impact, customer impact, evidence sensitivity, privilege level, data classification, autonomy, reversibility, blast radius, and ability to audit or replay.

## Change Request Record

A governed change request should include:

```json
{
  "change_id": "chg-2026-06-27-001",
  "agent_id": "soc-triage-agent",
  "change_type": "prompt_and_output_schema",
  "current_version": "soc-triage-agent@1.4.2",
  "proposed_version": "soc-triage-agent@1.5.0",
  "owner_team": "SOC Engineering",
  "risk_level": "medium",
  "affected_service_models": ["MDR", "MSSP"],
  "affected_tenants": ["tenant-a", "tenant-b"],
  "affected_tools": ["siem-query", "case-note-draft"],
  "affected_data_classes": ["security-telemetry", "case-notes"],
  "policy_impact": "no new tool or data scope",
  "approval_requirements": ["agent_owner", "soc_service_owner"],
  "validation_evidence": ["test-run-123", "judge-eval-456"],
  "rollout_plan": "canary to internal tenant, then tenant-a, then tenant-b",
  "rollback_plan": "re-pin tenants to soc-triage-agent@1.4.2",
  "monitoring_plan": "watch denial rate, unsupported claim rate, and case-note edits for 72 hours"
}
```

The record is an architecture example. Production implementations should validate fields, enforce approvals, and link the record to release, audit, and rollback systems.

## Required Change Controls

### 1. Separation of Duties

The agent must not approve its own change.

The person or automation proposing a change should not be the only approver for high-risk or critical changes. Sensitive changes should require independent review from appropriate owners.

### 2. Scope Impact Review

Every change should identify whether it affects:

- tenant or customer scope;
- case or evidence scope;
- data classification;
- retrieval or memory boundaries;
- tool or action permissions;
- output destination;
- approval requirements;
- audit and replayability;
- rollback or recall capability.

A change that silently expands scope should be blocked.

### 3. Policy and PEP Impact Review

Changes that affect policy or enforcement must be reviewed for:

- allow/deny behavior;
- approval triggers;
- fail-closed behavior;
- tool parameter validation;
- evidence-reference requirements;
- tenant and case validation;
- output release gates;
- audit completeness.

### 4. Validation Evidence

Validation should include normal and failure-path tests.

Examples include:

- expected output examples;
- policy decision tests;
- PEP enforcement tests;
- tenant-boundary tests;
- prompt-injection or malicious-context tests;
- unsupported-claim checks;
- evidence-reference checks;
- tool-parameter validation;
- rollback tests;
- replayability checks.

Validation must not rely solely on the agent saying the change is safe.

### 5. Versioning

Every behavior-affecting change should produce or reference a versioned artifact.

Versioned artifacts may include prompt packages, workflow definitions, model references, tool contracts, policy bundles, retrieval indexes, memory schema, output templates, test packs, and deployment manifests.

### 6. Rollout Control

High-risk and critical changes should use staged rollout.

Rollout should define:

- eligible tenants or customers;
- excluded tenants or customers;
- canary cohort;
- monitoring gates;
- halt criteria;
- rollback trigger;
- owner and on-call contact;
- customer communication path where applicable.

### 7. Rollback and Recall

Every high-risk or critical change should have a tested rollback plan before release.

Fleet-wide or cross-tenant changes should also have an emergency recall path that blocks the affected version from further use.

## Emergency Changes

Emergency changes may be required for active incidents, compromised agents, dangerous outputs, policy defects, credential exposure, or cross-tenant risk.

Emergency change flow should:

1. record the emergency reason;
2. identify affected agents, versions, tenants, tools, and customers;
3. assign an accountable responder;
4. apply the minimum safe change needed;
5. preserve audit evidence;
6. notify required owners;
7. require retrospective review;
8. convert temporary controls into normal governed changes or retire them.

Emergency change must not become a permanent bypass for approval, testing, or audit.

## Change Freeze and Rollout Halt Conditions

Change rollout should halt when:

- policy denial rate exceeds threshold;
- unsupported claims increase;
- cross-tenant or cross-case attempts occur;
- tool errors or retries increase materially;
- audit records are incomplete;
- customer-facing output quality degrades;
- evidence references are missing or wrong;
- monitoring cannot validate behavior;
- rollback test fails;
- owners cannot be reached for critical issues.

## Audit Requirements

Change audit records should include:

- change ID;
- agent ID and affected versions;
- change type and risk level;
- proposer and approvers;
- scope impact;
- policy and PEP impact;
- validation evidence;
- approval decision;
- rollout plan;
- rollout status;
- monitoring findings;
- rollback or recall decision;
- emergency classification where applicable;
- closure rationale.

Audit records should support reconstruction of why a change was made, who approved it, what was tested, where it was deployed, which tenants were affected, and how it was rolled back or retired.

## Fail-Closed Conditions

The change process must fail closed or halt rollout when:

- change owner is missing;
- risk classification is missing;
- affected scope is unknown;
- policy impact is unknown;
- required approval is missing;
- validation evidence is missing or failed;
- rollback plan is missing for high-risk or critical changes;
- version record is missing;
- monitoring plan is missing;
- audit logging is unavailable;
- tenant eligibility cannot be verified.

## Acceptance Criteria

Agent change management is acceptable when:

- behavior-affecting changes are versioned and reviewed;
- risk classification determines approval, validation, rollout, and rollback requirements;
- changes cannot silently expand scope or bypass policy;
- high-risk changes have validation evidence and rollback plans;
- fleet-wide changes use staged rollout and monitoring gates;
- emergency changes are auditable and retrospectively reviewed;
- audit records can reconstruct the full change lifecycle.

## Summary

Agent changes are security changes when they influence security operations.

> Prompts, policies, tools, models, retrieval, memory, workflow logic, and output templates must be governed as behavior-changing control-plane artifacts.
