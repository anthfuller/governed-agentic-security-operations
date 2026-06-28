# Agent Fleet Governance

## Purpose

This document defines governance requirements for managing fleets of agents across MSSP, MDR, SOC, cloud incident response, and DFIR service models.

An agent fleet may include many agent instances, versions, roles, tenants, customers, workflows, tools, policies, and deployment cohorts. Fleet governance ensures that shared capabilities do not become shared risk across customers or tenants.

## Core Principle

Fleet scale must not weaken governance.

A change that is safe for one customer, tenant, case, environment, or service tower is not automatically safe for all others. Fleet distribution must be scoped, eligible, staged, monitored, auditable, and recallable.

## Fleet Governance Scope

Fleet governance applies when agents or agent components are distributed or reused across:

- multiple customers;
- multiple tenants;
- multiple SOC/MDR/MSSP service towers;
- multiple cloud accounts or subscriptions;
- multiple DFIR engagements;
- multiple environments;
- multiple tool integrations;
- shared model, prompt, policy, retrieval, memory, or workflow packages.

## Fleet Control Objects

| Control Object | Purpose |
|---|---|
| Fleet registry | Identifies fleet name, owner, service model, risk tier, active versions, and tenant eligibility. |
| Agent registry | Identifies individual agent identities and lifecycle states within the fleet. |
| Version manifest | Defines signed, approved package components. |
| Tenant eligibility policy | Defines which tenants/customers may receive which versions and capabilities. |
| Rollout plan | Defines canary, staged rollout, monitoring gates, halt criteria, and rollback plan. |
| Release approval | Records required approvals for fleet change. |
| Monitoring profile | Defines fleet-level telemetry, alert thresholds, and anomaly response. |
| Recall record | Records emergency block, rollback, or retirement of a fleet version. |

## Fleet Registry Example

```json
{
  "fleet_id": "mdr-triage-agent-fleet",
  "fleet_owner": "MDR Platform Engineering",
  "service_models": ["MDR", "MSSP"],
  "risk_tier": "high",
  "active_versions": ["triage-agent@1.4.2", "enrichment-agent@2.1.0"],
  "eligible_tenant_groups": ["standard-mdr", "premium-mdr"],
  "excluded_tenants": ["regulated-customer-x"],
  "allowed_tools": ["siem-query", "threat-intel-lookup", "case-note-draft"],
  "prohibited_actions": ["customer-notification", "endpoint-isolation-without-approval"],
  "rollout_strategy": "canary_then_cohort",
  "monitoring_profile": "mdr-agent-fleet-high-risk",
  "recall_contact": "mdr-platform-oncall"
}
```

The registry is an architecture example and should be implemented through validated, auditable records in production.

## Fleet Governance Requirements

### 1. Named Fleet Ownership

Every fleet must have an accountable owner responsible for lifecycle, tenant eligibility, rollout, monitoring, rollback, recall, and retirement.

Fleet ownership should be separate from customer approval authority and should not replace tenant-specific governance obligations.

### 2. Tenant Eligibility

Tenant eligibility must be explicit before a fleet version is distributed.

Eligibility should consider:

- customer contract and service model;
- tenant environment type;
- data residency and sovereignty constraints;
- regulated or restricted customer status;
- approved tools and integrations;
- evidence-handling requirements;
- customer approval obligations;
- known exclusions or temporary holds;
- rollback ability.

A tenant must be excluded from rollout when eligibility cannot be verified.

### 3. Version Signing and Provenance

Fleet packages should have a version manifest that records:

- agent version;
- prompt package version;
- model reference;
- tool-contract versions;
- policy bundle version;
- workflow definition version;
- retrieval and memory configuration;
- tests and validation evidence;
- package hash or signature;
- approvers;
- release date;
- rollback target.

Unsigned, unapproved, or unverifiable fleet packages should not be distributed.

### 4. Staged Rollout

Fleet rollout should use staged release rather than immediate global distribution.

A typical flow is:

1. internal validation environment;
2. non-production tenant or synthetic case;
3. internal canary tenant;
4. limited customer cohort;
5. broader eligible cohort;
6. general availability to eligible tenants.

Each stage should have monitoring gates, halt criteria, and rollback criteria.

### 5. Fleet-Wide Monitoring

Fleet governance must monitor both individual agent behavior and aggregate fleet behavior.

Fleet-level monitoring should track:

- version adoption;
- tenant rollout status;
- denied policy decisions;
- fail-closed events;
- output quality findings;
- unsupported claim rate;
- evidence-reference quality;
- cross-tenant/case attempt rate;
- tool errors and retries;
- customer-impacting exceptions;
- rollback or recall activity.

### 6. Tenant-Safe Intelligence Propagation

Fleet governance may support propagating sanitized intelligence across tenants, such as detection insights, indicator handling guidance, playbook refinements, or model/prompt improvements.

Propagation must not include raw customer data, evidence, secrets, customer identifiers, contractual information, or case-specific findings unless explicitly allowed through a governed release process.

Sanitized intelligence should include:

- source classification;
- sanitization review;
- release approval;
- tenant eligibility;
- retention label;
- audit record;
- rollback or removal path.

### 7. Emergency Recall

Fleet governance must be able to rapidly recall a compromised or defective version.

Recall should:

- block new invocations of the affected version;
- terminate or quarantine active sessions where appropriate;
- revoke affected credentials or tool access;
- pin tenants to a known-good version;
- notify owners and affected service teams;
- preserve audit evidence;
- identify affected tenants, cases, outputs, and tool actions;
- trigger retrospective review and corrective change management.

## Fleet Rollout Decision Flow

A governed rollout should follow this flow:

1. Create release candidate and version manifest.
2. Classify risk and identify affected tenants, customers, tools, data classes, and outputs.
3. Validate policy, PEP, tenant isolation, evidence support, monitoring, and rollback behavior.
4. Obtain required approvals.
5. Verify tenant eligibility and exclusions.
6. Deploy to canary stage.
7. Monitor gate metrics and failure conditions.
8. Progress by cohort only when gates pass.
9. Halt, rollback, or recall if gates fail.
10. Record rollout and final state in audit records.

## Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Fleet owner | Accountable for fleet operation, release, rollout, monitoring, and retirement. |
| Agent owner | Accountable for individual agent behavior and lifecycle. |
| Service owner | Confirms MSSP/MDR/SOC/DFIR service impact and customer obligations. |
| Policy owner | Reviews authorization, approval, and fail-closed behavior. |
| Tool owner | Reviews tool-contract impact and execution boundaries. |
| Tenant/customer owner | Confirms eligibility, exclusions, and customer-specific constraints. |
| Security reviewer | Reviews risk, abuse cases, cross-tenant exposure, and monitoring. |
| Release manager | Coordinates staged rollout and rollback readiness. |
| Incident responder | Executes emergency recall or containment for fleet defects. |

## Fleet Failure Modes

| Failure Mode | Required Control |
|---|---|
| Defect distributed to all tenants at once | Staged rollout and canary gates. |
| Tenant receives ineligible version | Tenant eligibility check and exclusion list. |
| Cross-tenant memory contamination | Tenant-bound memory and sanitized intelligence process. |
| Tool permission expansion through fleet update | Policy and tool-contract review before release. |
| Customer-specific data embedded in shared prompt or package | Sanitization and package inspection. |
| Defective version cannot be removed | Emergency recall and version pinning. |
| Monitoring cannot see fleet behavior | Rollout blocked until monitoring profile is active. |
| Version drift across tenants is unknown | Fleet inventory and version telemetry. |

## Audit Requirements

Fleet governance audit should include:

- fleet ID and owner;
- agent IDs and versions affected;
- version manifest and signature/hash;
- risk classification;
- affected tenant and customer cohorts;
- tenant eligibility decisions;
- approvals;
- validation evidence;
- rollout stage transitions;
- monitoring gate results;
- halt, rollback, or recall decisions;
- final rollout state;
- exceptions and customer-specific exclusions.

Audit records should support reconstruction of which tenants received which version, when, why, under whose approval, with what validation evidence, and with what rollback path.

## Fail-Closed Conditions

Fleet rollout must fail closed or halt when:

- fleet owner is missing;
- version manifest is missing or unsigned;
- affected tenants cannot be identified;
- tenant eligibility cannot be verified;
- required approval is missing;
- validation evidence is missing or failed;
- monitoring gates are unavailable;
- rollback or recall path is missing;
- package includes prohibited customer-specific data;
- policy or PEP compatibility cannot be validated;
- audit logging is unavailable.

## Acceptance Criteria

Agent fleet governance is acceptable when:

- every fleet has an owner, registry, version manifest, tenant eligibility policy, monitoring profile, and recall path;
- fleet changes are risk-classified, approved, validated, staged, monitored, and rollback-capable;
- tenants only receive versions they are eligible to receive;
- shared intelligence is sanitized and approved before propagation;
- fleet defects can be halted, rolled back, or recalled quickly;
- audit records can reconstruct distribution, approval, monitoring, and recovery.

## Summary

Agent fleet governance allows agentic capabilities to scale without turning one defect into a multi-tenant failure.

> Fleet distribution is a privileged change path and must be governed like one.
