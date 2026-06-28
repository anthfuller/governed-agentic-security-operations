# Agent Version Lifecycle and Rollbacks

## Purpose

This document defines lifecycle and rollback requirements for versions of governed agents and their behavior-affecting components.

An agent version is more than executable code. Agent behavior may depend on prompts, model references, tool contracts, policy bundles, orchestration definitions, retrieval indexes, memory rules, output templates, and evaluation tests. These components must be versioned together so behavior can be approved, monitored, reproduced, and rolled back.

## Core Principle

A governed agent must run an approved, identifiable, replayable version.

If the active version cannot be identified, validated, approved, pinned, monitored, or rolled back, the agent should not participate in governed workflows that affect tenants, customers, evidence, tools, or customer-facing outputs.

## Versioned Components

A complete agent version record should identify all behavior-affecting components.

| Component | Why It Matters |
|---|---|
| Agent package | Defines agent role, runtime wrapper, orchestration behavior, and dependencies. |
| System prompt or instruction set | Shapes reasoning, boundaries, refusal behavior, and output expectations. |
| Model reference | Affects output quality, latency, privacy, and risk. |
| Tool contract versions | Defines available tools, parameters, actions, and validation. |
| Policy bundle version | Defines allow/deny/approval/fail-closed behavior. |
| PEP configuration | Defines actual enforcement behavior at execution boundary. |
| Workflow definition | Defines handoffs, escalation, retries, and output routing. |
| Retrieval index | Defines knowledge sources and tenant/case/evidence boundaries. |
| Memory configuration | Defines memory reads/writes, retention, tenant/case scope, and contamination controls. |
| Output templates | Define customer-facing or analyst-facing output structure. |
| Evaluation/test pack | Defines validation evidence for release and rollback. |
| Monitoring profile | Defines expected behavior, alerts, and rollout gates. |

A version record should be immutable once approved. Corrections should create a new version or a formal rollback record.

## Version States

| State | Meaning | Allowed Use |
|---|---|---|
| `draft` | Version is being authored. | No governed workflow use. |
| `candidate` | Version is ready for validation. | Test/lab validation only. |
| `validated` | Version passed required tests and review. | Eligible for approval. |
| `approved` | Version approved for release. | Eligible for controlled rollout. |
| `canary` | Version deployed to limited cohort. | Limited, monitored production or pre-production use. |
| `active` | Version is approved and in normal use for eligible tenants. | Governed use within scope. |
| `pinned` | Tenant or workflow is locked to a specific version. | Required when rollout should not automatically advance. |
| `deprecated` | Version remains available only for transition or compatibility. | Limited exception-based use. |
| `blocked` | Version cannot be invoked due to risk, defect, or policy decision. | No new use. |
| `recalled` | Version is emergency withdrawn from fleet or tenant use. | No use; active sessions addressed. |
| `retired` | Version is permanently removed from active service. | No use; records retained. |

## Version Manifest Example

```json
{
  "agent_version": "soc-triage-agent@1.5.0",
  "agent_id": "soc-triage-agent",
  "release_id": "rel-2026-06-27-001",
  "state": "approved",
  "owner_team": "SOC Engineering",
  "risk_level": "medium",
  "package_hash": "sha256:example",
  "prompt_version": "soc-triage-prompt@3.2.0",
  "model_reference": "approved-model-profile:triage-medium-v2",
  "tool_contracts": ["siem-query@2.0", "case-note-draft@1.1"],
  "policy_bundle": "mdr-triage-policy@4.0",
  "workflow_definition": "triage-workflow@2.3",
  "retrieval_profile": "tenant-case-rag@1.2",
  "memory_profile": "case-scoped-memory@1.0",
  "output_template": "analyst-recommendation@1.5",
  "evaluation_pack": "triage-eval-pack@2026-06",
  "rollback_target": "soc-triage-agent@1.4.2",
  "approved_by": ["soc-service-owner", "security-reviewer"],
  "approved_at": "2026-06-27T20:00:00Z"
}
```

The manifest is an architecture example. Production manifests should be validated, signed, stored immutably, and linked to release and audit systems.

## Release Gates

A version should not become `approved`, `canary`, or `active` until it passes required gates.

| Gate | Required Evidence |
|---|---|
| Identity and ownership | Agent owner, release owner, emergency contact, lifecycle state. |
| Scope review | Tenant, customer, case, evidence, data, tool, action, and output scope impact. |
| Policy validation | Allow/deny/approval/fail-closed behavior tested. |
| PEP validation | Execution boundary enforces policy and parameters. |
| Tenant-isolation validation | Cross-tenant and cross-case attempts denied. |
| Evidence validation | Evidence references preserved for evidence-sensitive outputs. |
| Output-quality validation | Unsupported claims, confidence, and review requirements checked. |
| Monitoring readiness | Telemetry, dashboards, alert thresholds, and gates active. |
| Rollback readiness | Known-good rollback target and procedure tested. |
| Approval | Required owner, security, service, governance, and customer authority where applicable. |

## Version Pinning

Version pinning locks a tenant, customer, workflow, or agent to a specific version.

Pinning is appropriate when:

- customer environment has special restrictions;
- regulated or evidence-sensitive workflow requires stability;
- a new version is in staged rollout;
- a defect is suspected in later version;
- rollback is needed;
- customer approval is pending;
- compatibility with tool or policy version is limited.

Pinned versions must still be monitored, reviewed, and eventually upgraded, deprecated, or retired.

## Rollback Triggers

Rollback should be considered when:

- policy denial rate increases unexpectedly;
- fail-closed events increase materially;
- cross-tenant or cross-case attempts occur;
- unsupported claims increase;
- evidence references are missing or incorrect;
- customer-facing output is inaccurate or unsafe;
- tool calls are malformed or out of scope;
- latency or reliability degrades operationally;
- monitoring or audit fields are missing;
- tenant eligibility was misapplied;
- security issue or compromise is suspected.

Critical triggers should result in immediate halt, rollback, recall, or suspension depending on blast radius.

## Rollback Procedure

A governed rollback should follow this sequence:

1. Identify affected agent, version, tenants, customers, workflows, tools, and outputs.
2. Classify severity and decide rollback, recall, suspension, or restriction.
3. Preserve audit and monitoring evidence.
4. Block additional rollout of the affected version.
5. Pin affected tenants or workflows to known-good rollback target.
6. Revoke or rotate credentials if compromise is suspected.
7. Validate that active sessions use the intended version or are terminated.
8. Monitor rollback outcome and error rate.
9. Review affected outputs, tool actions, and customer impacts.
10. Record root cause, corrective action, and closure decision.

Rollback should be rehearsed for high-risk and critical agents before it is needed.

## Emergency Recall

Recall is stronger than rollback. Recall blocks a version from use because it is unsafe, compromised, unauthorized, or materially defective.

Recall should be used when:

- a version leaks or mixes tenant data;
- policy or PEP bypass is found;
- credentials or package integrity is compromised;
- evidence modification or chain-of-custody risk is present;
- customer-impacting output defect is severe;
- malicious or rogue behavior is detected;
- distribution included unauthorized tenants.

A recalled version should be marked `recalled` or `blocked` in the version registry, removed from eligible rollout, denied by policy, and visible in monitoring dashboards.

## Compatibility and Migration

Agent version changes may require compatibility review for:

- tool schemas;
- policy bundles;
- case systems;
- approval records;
- memory schema;
- retrieval index format;
- audit event fields;
- output templates;
- evidence manifest references;
- monitoring queries;
- customer-specific workflow variations.

State migration must be explicit and reversible where practical. Silent migration of memory, evidence references, or customer-facing output format should be treated as high risk.

## Audit Requirements

Version lifecycle and rollback audit records should include:

- agent ID;
- previous and new version state;
- version manifest;
- release ID;
- owner and approvers;
- risk level;
- validation evidence;
- rollout cohort;
- tenant eligibility;
- pinning decisions;
- rollback or recall trigger;
- rollback target;
- affected tenants, customers, cases, outputs, and tool actions;
- monitoring evidence;
- closure decision.

Audit must support reconstruction of what version ran, where it ran, when it ran, why it was approved, which tenants received it, and how it was rolled back or recalled.

## Fail-Closed Conditions

A version lifecycle workflow must fail closed or halt when:

- version manifest is missing;
- active version cannot be identified;
- package signature or hash cannot be verified;
- required validation evidence is missing;
- required approval is missing;
- tenant eligibility cannot be determined;
- rollback target is missing for high-risk or critical releases;
- monitoring gates are not active;
- policy bundle compatibility cannot be verified;
- audit logging cannot capture version and rollout decisions.

## Acceptance Criteria

Agent version lifecycle and rollback governance is acceptable when:

- every active agent runs an approved, identifiable version;
- version manifests identify behavior-affecting components;
- high-risk versions have validation evidence, approval, monitoring gates, and rollback targets;
- tenants can be pinned to known-good versions;
- unsafe versions can be blocked, rolled back, or recalled;
- audit records can reconstruct version state and distribution over time;
- rollback procedures are tested for high-risk and critical agents.

## Summary

Version governance makes agent behavior traceable and recoverable.

> If you cannot identify, approve, monitor, pin, roll back, or recall the version, it should not run in a governed security workflow.
