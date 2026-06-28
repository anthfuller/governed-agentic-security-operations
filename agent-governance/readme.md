# Agent Governance

## Purpose

This directory defines the control model for governing agents as managed enterprise identities and governed workloads inside the Agentic MSSP / MDR / DFIR security operations architecture.

Agent governance is the connective tissue between architecture intent and runtime enforcement. It defines how agents are registered, owned, scoped, reviewed, monitored, changed, versioned, rolled out, recalled, and retired before they are trusted to participate in security workflows.

## Core Principle

Agents are not trusted because they are useful, accurate, or well prompted.

Agents are trusted only within explicitly governed boundaries:

- known identity;
- named owner;
- approved purpose;
- authorized tenant, customer, case, and data scope;
- approved tools and actions;
- defined lifecycle state;
- monitored behavior;
- policy-mediated execution;
- auditable decisions and outcomes.

An unregistered, inactive, compromised, out-of-scope, or unreviewed agent must not retrieve data, call tools, communicate work instructions to other agents, release outputs, or affect customer systems.

## Scope

This directory covers governance requirements for:

- agent registration and identity lifecycle;
- least-privilege access scope;
- agent-to-agent communication boundaries;
- monitoring, oversight, and anomaly handling;
- change management for prompts, tools, policies, workflows, models, memory, and retrieval sources;
- fleet governance across customers, tenants, environments, and service towers;
- version lifecycle, rollback, emergency recall, and retirement.

It applies to agentic workflows supporting MSSP, MDR, SOC / Incident Response, cloud incident response, DFIR, and private/local LLM-assisted DFIR where agents may access customer data, evidence, security tools, case context, or governed outputs.

## Directory Contents

| File | Purpose |
|---|---|
| [`agent-identity-lifecycle.md`](agent-identity-lifecycle.md) | Defines agent registration, lifecycle states, owner accountability, suspension, retirement, and audit requirements. |
| [`agent-access-scope.md`](agent-access-scope.md) | Defines tenant, customer, case, evidence, data, tool, action, environment, and output boundaries for agent access. |
| [`agent-to-agent-communication.md`](agent-to-agent-communication.md) | Defines how agents may exchange tasks, context, outputs, and status without creating implicit trust or cross-boundary leakage. |
| [`agent-monitoring-and-oversight.md`](agent-monitoring-and-oversight.md) | Defines telemetry, behavioral monitoring, oversight responsibilities, alerting, and response actions for agent activity. |
| [`agent-change-management.md`](agent-change-management.md) | Defines controlled change for prompts, models, tools, policies, workflows, memory, retrieval, and agent configuration. |
| [`agent-fleet-governance.md`](agent-fleet-governance.md) | Defines governance for shared agent fleets, tenant eligibility, staged rollout, sanitized intelligence propagation, and recall. |
| [`agent-version-lifecycle-and-rollbacks.md`](agent-version-lifecycle-and-rollbacks.md) | Defines version states, release gates, version pinning, rollback triggers, rollback procedure, and replayability requirements. |

## Governance Model

Agent governance should be implemented as a control plane that exists beside the runtime workflow, not inside an agent prompt.

At minimum, the control plane should maintain:

| Control Object | Required Purpose |
|---|---|
| Agent registry | Identifies approved agents, owners, purposes, risk tiers, and lifecycle states. |
| Scope profile | Defines authorized tenants, customers, cases, tools, actions, data classes, evidence classes, environments, and output destinations. |
| Version record | Identifies approved prompt, model, workflow, tool contract, policy, retrieval, memory, and package versions. |
| Change record | Captures proposed changes, risk classification, approvals, validation evidence, rollout plan, rollback plan, and release decision. |
| Monitoring profile | Defines expected behavior, alert thresholds, telemetry requirements, review cadence, and response playbooks. |
| Audit correlation model | Links agent identity, request, policy decision, approval, tool execution, evidence references, version, and output. |

Agent governance must provide inputs to policy evaluation, tool enforcement, tenant isolation, human oversight, audit replay, and evidence traceability. It must not replace any of those controls.

## Minimum Agent Registry Record

Every governed agent should have a registry record before it can participate in a workflow.

```json
{
  "agent_id": "soc-triage-agent",
  "agent_name": "SOC Triage Agent",
  "owner_team": "SOC Engineering",
  "service_model": ["MDR", "MSSP"],
  "business_purpose": "Assist analysts with customer-scoped alert triage and evidence-backed recommendations.",
  "risk_tier": "medium",
  "lifecycle_state": "active",
  "approved_tenants": ["tenant-a", "tenant-b"],
  "approved_data_classes": ["security-telemetry", "case-notes", "threat-intelligence"],
  "approved_tools": ["siem-query", "threat-intel-lookup", "case-update-draft"],
  "prohibited_actions": ["endpoint-isolation", "user-disablement", "evidence-modification"],
  "current_version": "soc-triage-agent@1.4.2",
  "review_frequency": "quarterly",
  "last_access_review": "2026-06-01",
  "monitoring_profile": "soc-agent-medium-risk",
  "emergency_contact": "soc-platform-oncall"
}
```

The record is an architecture example, not an implementation schema. A production implementation should use validated schemas, ownership workflows, policy integration, and audit controls appropriate to its environment.

## Required Control Outcomes

Agent governance is acceptable only when the following outcomes are true:

- Every active agent has a unique identity and named owner.
- Every active agent has an approved purpose and service model.
- Every active agent has explicit tenant, customer, case, data, evidence, tool, action, environment, and output scope where applicable.
- Agent lifecycle state is checked before retrieval, reasoning handoff, tool access, output release, or workflow delegation.
- Agent-to-agent communication is authenticated, scoped, policy-visible, and auditable.
- Agent changes are reviewed, tested, approved, versioned, and rollback-capable.
- Shared fleet updates are signed, staged, monitored, tenant-eligible, and recallable.
- Monitoring can detect suspicious behavior, policy bypass attempts, cross-tenant activity, unexpected tool usage, unsupported claims, and version drift.
- Audit records can reconstruct which agent, version, policy decision, approval record, evidence references, tool calls, and outputs contributed to an outcome.
- Failure to validate identity, scope, policy, lifecycle state, approval, or auditability fails closed.

## Relationship to Other Directories

| Related Area | Relationship |
|---|---|
| [`architecture/`](../architecture/README.md) | Defines where the Agent Governance & Identity Control Plane sits in the architecture. |
| [`patterns/`](../patterns/readme.md) | Defines reusable agentic workflow patterns that depend on governed identity, scope, policy, and auditability. |
| [`policy-enforcement/`](../policy-enforcement/readme.md) | Uses agent identity, scope, version, risk tier, and lifecycle state as policy inputs. |
| [`tool-access/`](../tool-access/readme.md) | Enforces approved tool and action scope for agents. |
| [`tenant-isolation/`](../tenant-isolation/readme.md) | Validates customer, tenant, case, and data boundaries. |
| [`human-oversight/`](../human-oversight/readme.md) | Defines review and approval checkpoints for high-risk agent requests and changes. |
| [`audit-replay/`](../audit-replay/readme.md) | Records agent identity, decisions, approvals, versions, tool activity, and outputs for reconstruction. |
| [`evidence-traceability/`](../evidence-traceability/readme.md) | Ensures evidence-sensitive outputs preserve references, provenance, and handling requirements. |

## Non-Goals

This directory does not:

- define product-specific identity configuration;
- provide executable policy code;
- replace enterprise IAM, PAM, SIEM, SOAR, ITSM, GRC, or audit platforms;
- make agent outputs legally or forensically authoritative;
- permit autonomous sensitive action without policy evaluation and approval where required;
- make agent-to-agent communication trusted by default;
- eliminate the need for human accountability.

## Summary

Agent governance makes agents manageable, accountable, scoped, observable, and revocable.

Without agent governance, policy enforcement lacks reliable identity and scope inputs, monitoring cannot distinguish expected from unexpected behavior, audit replay cannot reconstruct agent contribution, and fleet updates can become a cross-tenant control failure.

> Agents may assist the security operation, but only governed agents operating inside explicit identity, scope, lifecycle, policy, oversight, and audit boundaries may participate in controlled workflows.
