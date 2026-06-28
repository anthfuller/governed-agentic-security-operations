# Agent Monitoring and Oversight

## Purpose

This document defines monitoring and oversight requirements for governed agents operating within Agentic MSSP / MDR / DFIR security operations.

Monitoring ensures that agents remain within approved identity, scope, lifecycle, version, policy, tool, tenant, evidence, and output boundaries. Oversight ensures that anomalous behavior leads to review, suspension, rollback, recall, policy adjustment, or retirement when required.

## Core Principle

Governed agents must be observable enough to control.

If agent behavior cannot be monitored, correlated, audited, or reviewed, the agent should not participate in workflows that affect customers, tenants, evidence, tools, approvals, or production security operations.

## Monitoring Objectives

Agent monitoring should answer:

- Which agent acted?
- Which version acted?
- Which tenant, customer, case, evidence, tool, and output scope applied?
- What did the agent request?
- What did policy decide?
- What did the PEP enforce?
- Was human or customer approval required?
- What output was produced?
- Was the output supported by evidence?
- Did behavior match expected patterns?
- Did the agent attempt to exceed scope?
- Was the workflow auditable and replayable?

## Monitoring Surfaces

| Surface | Monitoring Need |
|---|---|
| Identity | Agent sign-in, token use, credential issuance, lifecycle state, owner, access review status. |
| Runtime | Agent invocation, model/prompt version, workflow state, runtime errors, timeout, retry behavior. |
| Retrieval and memory | Tenant/case/evidence scope, query pattern, memory reads/writes, RAG source, denied retrieval. |
| Policy | PDP decision, reason codes, risk classification, approval requirement, fail-closed events. |
| Tool access | Tool request, parameters, PEP result, before/after state, tool error, execution scope. |
| Human oversight | Review queue, approval status, approver identity, approval expiration, denial reason. |
| Output | Destination, data classification, evidence support, unsupported claim flags, customer-release state. |
| Fleet | Version distribution, tenant eligibility, rollout cohort, drift, rollback, recall, blocked version. |
| Audit | Missing audit fields, correlation gaps, replay failures, immutable log integrity. |

## Required Telemetry Fields

Telemetry should include enough structured data to correlate behavior across systems.

Minimum fields should include:

| Field | Purpose |
|---|---|
| `event_id` | Unique telemetry event identifier. |
| `correlation_id` | Workflow, case, or transaction correlation. |
| `agent_id` | Governed agent identity. |
| `agent_version` | Active version at time of event. |
| `lifecycle_state` | Lifecycle state at time of event. |
| `owner_team` | Accountable owner. |
| `tenant_id` / `customer_id` / `case_id` | Scope boundaries. |
| `evidence_refs` | Evidence or source references used where applicable. |
| `requested_action` | What the agent attempted. |
| `tool_id` | Tool or connector requested where applicable. |
| `policy_decision` | Allow, deny, require approval, clarify, or fail closed. |
| `pep_result` | Enforced result at execution boundary. |
| `approval_ref` | Approval record where required. |
| `output_destination` | Where output was sent or proposed. |
| `risk_tier` | Agent or action risk tier. |
| `reason_code` | Explanation for allow, deny, approval, or failure outcome. |
| `timestamp` | Time of event. |

Telemetry should avoid storing secrets, raw credentials, unnecessary sensitive content, or unredacted evidence unless the logging destination is explicitly approved for that data class.

## Behavioral Signals

Monitoring should detect expected and unexpected behavior.

| Signal | Risk Indicated |
|---|---|
| Sudden increase in denied policy decisions | Possible prompt injection, misuse, misconfiguration, or changed workflow conditions. |
| Cross-tenant or cross-case access attempts | Tenant isolation failure or malicious/compromised behavior. |
| Tool requests outside approved scope | Policy bypass attempt, version defect, or prompt/tool confusion. |
| Repeated requests requiring approval after denial | Automation loop, adversarial prompt, or insufficient guardrail. |
| Output without evidence references | Unsupported claim risk, DFIR quality risk, or reporting failure. |
| Memory writes outside case or tenant scope | Memory contamination risk. |
| Unexpected model, prompt, tool, or policy version | Version drift or unauthorized change. |
| High-risk requests from low-risk agent | Scope misclassification or compromised workflow. |
| Agent activity after suspension or retirement | Identity enforcement failure. |
| Missing audit correlation | Replayability and accountability gap. |
| Unusual time, volume, tenant spread, or tool pattern | Possible rogue behavior or automation defect. |

## Oversight Responsibilities

| Role | Oversight Responsibility |
|---|---|
| Agent owner | Ensures purpose, scope, lifecycle, version, monitoring, and review remain current. |
| SOC / MDR service owner | Confirms operational fitness, escalation behavior, and customer-service boundaries. |
| Security platform owner | Confirms runtime, policy, tool, logging, and monitoring controls operate correctly. |
| Identity owner | Confirms identity issuance, credential handling, access review, and revocation. |
| DFIR lead | Reviews evidence-sensitive behavior and forensic output boundaries. |
| Governance / risk reviewer | Reviews policy exceptions, high-risk changes, and customer-impacting controls. |
| On-call responder | Executes suspension, rollback, or recall during operational incidents. |

Oversight must be assigned to humans or accountable teams. An agent cannot be the final oversight authority for itself.

## Alert Classes

| Alert Class | Examples | Expected Response |
|---|---|---|
| Informational | Normal rollout progress, review due soon, low-risk denied request. | Review in routine queue. |
| Warning | Increased denial rate, missing optional metadata, repeated clarification loops. | Owner review and possible scope or prompt adjustment. |
| High | Tool request outside scope, output release blocked, unexpected version, audit gap. | Suspend affected workflow or agent pending review. |
| Critical | Cross-tenant access attempt, credential compromise, evidence modification attempt, active retired agent, recall trigger. | Immediate suspension, credential revocation, rollout halt, incident response, and audit preservation. |

## Monitoring Review Cadence

Review cadence should align to risk tier.

| Risk Tier | Example Use | Suggested Oversight Cadence |
|---|---|---|
| Low | Read-only enrichment with no sensitive output. | Periodic dashboard review and exception review. |
| Medium | Customer-scoped triage, case-draft support, recommendation drafting. | Regular owner review, denial review, and access review. |
| High | Sensitive data, evidence support, privileged recommendation, customer-facing drafts. | Frequent review, approval-path monitoring, and quality sampling. |
| Critical | State-changing actions, fleet-wide updates, evidence-impacting workflows. | Near-real-time alerting, change board oversight, and tested rollback/recall. |

Cadence should increase after incidents, repeated policy denials, version changes, new tools, new customers, new data classes, or fleet rollout.

## Response Actions

Monitoring findings should map to response actions.

| Condition | Response |
|---|---|
| Suspicious behavior but no confirmed impact | Restrict scope, increase monitoring, require owner review. |
| Policy violation or out-of-scope request | Deny request, record reason, notify owner, review workflow. |
| Cross-tenant or evidence-boundary violation | Fail closed, suspend agent, preserve audit, initiate incident review. |
| Version drift | Block or pin version, investigate release process, restore approved version. |
| Credential anomaly | Revoke credentials, terminate sessions, rotate secrets, review access logs. |
| Unsupported customer-facing output | Block release, require human review, update evidence-support checks. |
| Fleet defect | Halt rollout, roll back or recall affected version, restrict tenant eligibility. |
| Missing audit path | Block sensitive workflow until auditability is restored. |

## Dashboards

Operational dashboards should show:

- active agents by lifecycle state and risk tier;
- agents with expired reviews;
- policy decision trends by agent, tenant, tool, and action type;
- failed-closed events and reasons;
- approval-required events and approval outcomes;
- cross-tenant/case denied attempts;
- tool usage by scope and risk tier;
- outputs blocked for evidence or quality reasons;
- version adoption, drift, rollback, and recall status;
- audit correlation completeness.

Dashboards should be used for operations, governance review, and continuous assurance. They do not replace audit records.

## Audit Requirements

Monitoring and oversight events should record:

- detected condition;
- agent identity and version;
- scope involved;
- triggering telemetry;
- policy and PEP references;
- owner notification;
- human reviewer or responder;
- response action taken;
- suspension, rollback, or recall record where applicable;
- closure rationale;
- lessons learned or control update reference.

## Fail-Closed Conditions

The workflow must fail closed or route to authorized review when:

- monitoring profile is missing for a governed agent;
- audit correlation is unavailable for sensitive workflow activity;
- lifecycle state cannot be monitored;
- policy decisions cannot be logged;
- PEP enforcement result cannot be verified;
- high-risk tool activity cannot be observed;
- output release cannot be traced to evidence and approval;
- critical alert response path is unavailable.

## Acceptance Criteria

Agent monitoring and oversight are acceptable when:

- every active agent has an assigned monitoring profile;
- telemetry captures identity, version, scope, policy, PEP, approval, and output events;
- anomalous behavior triggers defined review or response actions;
- suspended, retired, or recalled agents cannot continue operating;
- dashboards show operational status and governance exceptions;
- audit records can reconstruct monitoring findings and response actions;
- high-risk failures can trigger suspension, rollback, or recall.

## Summary

Monitoring makes governed agents observable. Oversight makes observations actionable.

> An agent that cannot be monitored, reviewed, suspended, rolled back, or recalled should not be allowed to affect governed security operations.
