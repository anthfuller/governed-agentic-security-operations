# Fleet Rollout Audit and Replay Model

## Purpose

This document defines the audit and replay model for governed fleet rollout, rollback, recall, and emergency containment across agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

Fleet changes can affect many tenants, customers, cases, service towers, analysts, agents, detections, playbooks, prompts, report templates, retrieval sources, policy bundles, and tool paths. The audit model must make each rollout decision reconstructable without relying on chat history, model output, informal release notes, or operational memory.

The model answers these questions:

1. What changed?
2. Who requested, reviewed, approved, and released it?
3. Which package, prompt, policy, tool contract, retrieval configuration, detection, playbook, report template, or sanitized intelligence item was affected?
4. Which tenants, customers, service towers, cohorts, or environments were eligible?
5. Which rollout gates passed, failed, paused, or required exception handling?
6. Which version was active at a specific time for a specific tenant or workflow?
7. What triggered rollback, recall, or emergency containment?
8. Can the rollout be replayed from proposal through final state?

## Scope

This model applies to audit records created for fleet-level changes, including:

- agent package rollout;
- prompt package rollout;
- model route or local/private model configuration rollout;
- policy bundle rollout;
- tool contract rollout;
- retrieval, RAG, memory, or knowledge-source configuration rollout;
- detection package rollout;
- playbook or response workflow rollout;
- report template rollout;
- sanitized intelligence release to shared fleet context;
- tenant eligibility targeting and exclusions;
- canary, cohort, staged, or broad rollout;
- rollback to a known-good version;
- recall, kill switch, or emergency disablement;
- monitoring gates and post-release validation;
- rollout exceptions, denials, failures, and final closeout.

Out of scope:

- the baseline audit event schema, which belongs in `audit-event-model.md`;
- audit correlation rules, which belong in `audit-correlation-model.md`;
- exception and failure details, which belong in `exception-and-failure-audit.md`;
- immutable storage and retention guidance, which belongs in `immutable-audit-guidance.md`;
- tenant sanitization standards, which belong in `tenant-isolation/fleet-scope-and-cross-tenant-propagation-boundaries.md`;
- implementation-specific CI/CD, repository, package-signing, or SIEM query logic.

## Core Principle

Fleet rollout is a governed operational release, not a routine runtime agent action.

Every material fleet change must have a replayable audit chain that connects request, ownership, package contents, validation evidence, policy decision, approval, tenant eligibility, rollout scope, monitoring, rollback target, recall path, and final state.

Runtime approval for an agent to use tenant-scoped context does not authorize cross-tenant reuse, shared-memory writes, package distribution, prompt updates, detection updates, playbook updates, report-template release, or fleet rollout.

## Definitions

| Term | Meaning |
|---|---|
| Fleet change | A change to an agent, prompt, policy bundle, tool contract, retrieval configuration, detection, playbook, report template, sanitized intelligence item, or supporting control package used by more than one workflow, tenant, customer, case, or service tower. |
| Release package | Versioned unit prepared for rollout. It may contain one or more agent definitions, prompt packages, policy bundles, tool contracts, detection rules, playbooks, retrieval configuration, report templates, or sanitized intelligence items. |
| Rollout | Controlled activation of a release package for approved tenants, cohorts, service towers, environments, or workflows. |
| Rollout stage | A bounded rollout step such as internal validation, canary, limited tenant cohort, service-tower rollout, broad rollout, pause, rollback, recall, or retirement. |
| Gate | Required validation, approval, policy, tenant eligibility, monitoring, or release-integrity checkpoint. |
| Tenant eligibility | Policy-backed determination that a tenant, customer group, environment, or service tier may receive or consume a specific release package. |
| Activation | Moment when a package version becomes usable by an agent, workflow, detection engine, playbook, retrieval system, report generator, or tool path. |
| Rollback | Reverting from a released version to a known-good prior version or pinned safe version. |
| Recall | Removing, disabling, quarantining, or blocking a released version or shared intelligence item after release. |
| Kill switch | Emergency control that immediately blocks execution, activation, retrieval, or distribution of an unsafe package, version, tool path, prompt, detection, playbook, or intelligence item. |
| Rollout ledger | Ordered audit trail of all events, decisions, approvals, stage transitions, activations, monitoring results, exceptions, rollback actions, recall actions, and closeout state for a release. |

## Architecture Position

Fleet rollout audit sits between change governance, tenant eligibility, policy enforcement, monitoring, and replay.

```text
Fleet change request
        ↓
Package assembly and manifest creation
        ↓
Validation and safety review
        ↓
Policy decision and approval
        ↓
Tenant eligibility and destination scope
        ↓
Signed release package
        ↓
Canary or staged rollout
        ↓
Monitoring and gate evaluation
        ↓
Cohort or broad rollout
        ↓
Rollback, recall, retirement, or closeout
        ↓
Replayable rollout ledger
```

The rollout ledger must preserve the complete decision path from proposed change to final state.

## Rollout Record Hierarchy

Fleet rollout audit records should be organized around stable identifiers.

```text
change_request_id
        ↓
release_id
        ↓
package_id / package_version
        ↓
rollout_id
        ↓
rollout_stage_id
        ↓
tenant_eligibility_record_id
        ↓
gate_event_id
        ↓
activation_event_id
        ↓
monitoring_event_id
        ↓
rollback_id / recall_id / closeout_id
```

Each record does not need to duplicate every detail. Records should reference each other through stable identifiers so the full rollout can be replayed.

## Required Identifiers

| Identifier | Requirement | Purpose |
|---|---|---|
| `change_request_id` | Required | Connects rollout to the original requested change. |
| `release_id` | Required | Identifies the approved release unit. |
| `package_id` | Required | Identifies the package being distributed. |
| `package_version` | Required | Identifies the exact version being released. |
| `package_manifest_ref` | Required | References the manifest describing package contents, dependencies, scope, and rollback target. |
| `rollout_id` | Required | Identifies the rollout sequence for the release. |
| `rollout_stage_id` | Required for staged rollout | Identifies the specific stage, cohort, canary, pause, rollback, or recall action. |
| `correlation_id` | Required | Connects rollout audit events into one replayable chain. |
| `tenant_id` | Conditional | Required for tenant-specific eligibility, activation, monitoring, rollback, recall, or exception events. |
| `customer_id` | Conditional | Required where service ownership or customer-specific authorization is involved. |
| `service_tower` | Recommended | Indicates MSSP, MDR, cloud IR, DFIR, detection engineering, threat hunting, or other tower impacted. |
| `policy_decision_id` | Required when policy is evaluated | Links rollout or activation to PDP decision. |
| `approval_record_id` | Required when approval is required | Links rollout to human, customer, service-owner, or emergency approval. |
| `tenant_eligibility_record_id` | Required for tenant distribution | Records included tenants, excluded tenants, and eligibility reason codes. |
| `validation_record_id` | Required before release | Links to safety, policy, tenant, evidence, output-quality, or technical validation evidence. |
| `monitoring_profile_id` | Required for rollout | Defines required monitoring signals and gates. |
| `rollback_target` | Required for reversible release | Identifies the known-good version or safe pinned state. |
| `recall_path_id` | Required for broad or shared release | Identifies how the package can be disabled, removed, quarantined, or blocked. |

## Rollout State Model

Fleet rollout audit should preserve state transitions.

| State | Meaning |
|---|---|
| `draft` | Change is proposed but not ready for validation. |
| `submitted` | Change request has been submitted for review. |
| `validated` | Required technical, policy, tenant, evidence, and safety validations have passed. |
| `validation_failed` | One or more required validations failed. |
| `approved` | Required human, service-owner, policy-owner, customer, or emergency approvals are recorded. |
| `denied` | Release or rollout is not authorized. |
| `signed` | Package integrity, provenance, and version are recorded. |
| `ready_for_rollout` | Package is eligible for controlled deployment. |
| `canary_active` | Package is active for limited internal, tenant, service, or workflow scope. |
| `cohort_active` | Package is active for a defined tenant or service cohort. |
| `broad_active` | Package is active for all eligible destination scope. |
| `paused` | Rollout has stopped but package may remain active for existing scope. |
| `rollback_in_progress` | Rollout is reverting to a known-good version. |
| `rolled_back` | Rollback completed. |
| `recall_in_progress` | Package is being disabled, removed, quarantined, or blocked. |
| `recalled` | Recall completed. |
| `superseded` | Package has been replaced by a newer approved version. |
| `retired` | Package is no longer available for activation. |
| `closed` | Rollout is complete and final audit state is recorded. |

State transitions must be auditable. A package should not move from `draft` to `broad_active` without recorded validation, approval, signing, tenant eligibility, and rollout gate outcomes.

## Audit Event Categories

Fleet rollout should emit audit events at each material decision or state change.

| Event Type | When Created | Required Outcome |
|---|---|---|
| `fleet.change.requested` | A fleet change is proposed. | Change request created or rejected. |
| `fleet.package.assembled` | Package contents are bound into a release unit. | Manifest created with version, dependencies, scope, and rollback target. |
| `fleet.validation.completed` | Required validation completes. | Passed, failed, partially passed, or requires remediation. |
| `fleet.policy.requested` | Policy evaluation is requested for release or activation. | Policy request created. |
| `fleet.policy.decided` | PDP returns decision. | Allow, deny, require approval, or fail closed. |
| `fleet.approval.recorded` | Human, service-owner, customer, or emergency approval is recorded. | Approved, denied, expired, withdrawn, or escalated. |
| `fleet.package.signed` | Package integrity and provenance are finalized. | Signature, checksum, or provenance record created. |
| `fleet.tenant_eligibility.evaluated` | Destination eligibility is evaluated. | Included, excluded, denied, deferred, or requires approval. |
| `fleet.rollout.started` | Rollout sequence begins. | Rollout ID and initial scope created. |
| `fleet.rollout.stage.started` | Canary, cohort, broad rollout, pause, rollback, or recall stage begins. | Stage ID and scope created. |
| `fleet.rollout.stage.completed` | Stage completes or fails. | Passed, failed, paused, rolled back, recalled, or escalated. |
| `fleet.activation.completed` | Version becomes active for a tenant, cohort, service, workflow, or environment. | Active, denied, deferred, or failed. |
| `fleet.monitoring.evaluated` | Monitoring gate evaluates rollout health. | Pass, fail, warning, pause, rollback, recall, or continue. |
| `fleet.exception.recorded` | A rollout exception, denial, drift, or failure occurs. | Stopped, escalated, accepted by exception, rolled back, or recalled. |
| `fleet.rollback.initiated` | Rollback begins. | Rollback target and affected scope recorded. |
| `fleet.rollback.completed` | Rollback completes. | Success, partial success, failed, or escalated. |
| `fleet.recall.invoked` | Recall or kill switch is invoked. | Affected package, scope, and containment actions recorded. |
| `fleet.recall.completed` | Recall completes. | Success, partial success, failed, or requires remediation. |
| `fleet.rollout.closed` | Rollout reaches final state. | Closed, superseded, retired, failed, recalled, or rolled back. |

## Package Manifest Audit Requirements

The package manifest is central to replay. It should identify what was released and what controls were attached to it.

Minimum manifest fields:

| Field | Purpose |
|---|---|
| `package_id` | Unique package identifier. |
| `package_version` | Exact version released. |
| `package_type` | Agent, prompt, policy, tool contract, detection, playbook, report template, retrieval config, model route, or sanitized intelligence. |
| `owner` | Accountable team or person. |
| `service_towers` | MSSP, MDR, SOC, cloud IR, DFIR, detection engineering, threat hunting, or other tower. |
| `risk_tier` | Release risk classification. |
| `package_contents` | References to included components and versions. |
| `dependency_refs` | Required policy bundles, tool contracts, model routes, retrieval configs, or approval profiles. |
| `allowed_destination_scope` | Approved service, tenant group, customer group, or environment scope. |
| `excluded_tenants` | Tenants or customers excluded from release. |
| `data_boundary_classification` | Whether the package contains customer-derived, sanitized, public, internal, or evidence-linked material. |
| `validation_refs` | Test, assurance, review, and safety validation references. |
| `policy_refs` | Policy requests, decisions, and policy bundles. |
| `approval_refs` | Human, service-owner, customer, or emergency approval references. |
| `signature_or_checksum` | Integrity reference for package provenance. |
| `monitoring_profile` | Required monitoring for rollout health and recall triggers. |
| `rollback_target` | Known-good version or safe pinned state. |
| `recall_path` | Removal, disablement, quarantine, or kill-switch path. |

## Required Rollout Gates

A rollout gate is a control checkpoint that must produce an auditable result.

| Gate | Audit Requirement |
|---|---|
| Ownership gate | Record accountable owner, service owner, and support owner. |
| Scope gate | Record destination scope, tenant group, service tower, environment, and exclusions. |
| Risk gate | Record risk tier and sensitive-action impact. |
| Validation gate | Record test results, assurance checks, policy checks, and known limitations. |
| Evidence gate | Record evidence or engineering support for detections, playbooks, or DFIR-derived logic. |
| Sanitization gate | Required when customer-derived learning is used. Record sanitization review and release approval. |
| Policy gate | Record PDP request and decision for release, activation, and destination scope. |
| Approval gate | Record human, service-owner, customer, or emergency approval where required. |
| Integrity gate | Record manifest hash, package signature, or provenance evidence. |
| Tenant eligibility gate | Record included and excluded tenants with reason codes. |
| Monitoring gate | Record required health signals, thresholds, and gate outcome. |
| Rollback gate | Record rollback target and tested recovery path. |
| Recall gate | Record recall path and kill-switch readiness for high-impact or broad release. |

A failed gate must stop rollout, deny activation, route to remediation, or require authorized exception handling.

## Tenant Eligibility Audit

Tenant eligibility determines whether a release may be activated for a destination tenant, customer group, service tier, environment, or workflow.

Eligibility audit must record:

| Field | Purpose |
|---|---|
| `tenant_id` or `tenant_group_id` | Destination boundary evaluated. |
| `service_tier` | Service package or operating model receiving the release. |
| `region` | Data residency or regional control context. |
| `eligibility_result` | Included, excluded, denied, deferred, or requires approval. |
| `reason_codes` | Why the tenant is included or excluded. |
| `contractual_constraints` | Customer-specific restrictions where applicable. |
| `sovereignty_constraints` | Regional, legal, or residency restrictions. |
| `required_approvals` | Customer, service-owner, policy-owner, or legal approval requirements. |
| `activation_window` | Allowed time period for release activation. |
| `monitoring_requirements` | Tenant-specific monitoring signals or thresholds. |
| `rollback_target` | Tenant-specific known-good fallback where different from the package default. |

Eligibility should be checked before rollout and again before activation if there is any meaningful delay, policy change, customer exception, recall, or superseding release.

## Rollout Stage Audit

Each rollout stage should record its scope, start condition, gate results, and outcome.

| Stage | Required Audit Detail |
|---|---|
| Internal validation | Test scope, validation records, reviewer, defects, and remediation. |
| Canary | Selected tenant, cohort, workflow, or internal environment; monitoring thresholds; exit criteria. |
| Limited cohort | Included tenant group, excluded tenants, activation window, gate result, and customer impact. |
| Broad rollout | Final eligible scope, remaining exclusions, active monitoring, and rollback readiness. |
| Pause | Reason, trigger, current active scope, owner, and next review time. |
| Rollback | Trigger, target version, affected scope, success criteria, and completion state. |
| Recall | Trigger, package or intelligence item blocked, affected tenants, sessions, outputs, retrieval entries, or detections. |
| Retirement | Replacement package, deactivation time, remaining dependencies, and final state. |

## Activation Audit

Activation is the point where a release becomes usable. It must be auditable at the tenant, service, workflow, or environment level.

Activation records should include:

- package ID and version;
- release ID and rollout ID;
- tenant, customer, service tower, workflow, or environment scope;
- activation time;
- activating component;
- policy decision reference;
- tenant eligibility reference;
- approval reference where required;
- previous active version;
- rollback target;
- monitoring profile;
- activation outcome;
- failure or exception reference if activation did not complete.

A release should not become active when tenant eligibility, policy decision, package integrity, approval state, monitoring profile, or audit logging is missing or invalid.

## Monitoring and Gate Evaluation

Fleet rollout replay requires monitoring records that show whether the release behaved as expected after activation.

Monitoring should track:

| Signal | Purpose |
|---|---|
| Active versions by tenant | Detect unauthorized rollout, drift, or stale versions. |
| Invocation volume | Detect runaway or unexpected agent usage. |
| Policy denials | Detect policy mismatches, unsafe requests, or blocked behavior. |
| Fail-closed events | Detect missing scope, approval, audit, policy, or tool context. |
| Tool request rate | Detect unexpected tool use or high-impact action patterns. |
| Tool execution failures | Detect integration, permission, or scoped-token failures. |
| Unsupported-claim rate | Detect output quality degradation. |
| Evidence-support failures | Detect missing or weak evidence references. |
| Tenant-boundary failures | Detect cross-tenant, cross-case, or retrieval-scope defects. |
| Report review failures | Detect customer-facing output quality or approval failures. |
| Detection alert volume | Detect noisy or broken detection package releases. |
| False-positive signals | Detect operational harm from detection or playbook changes. |
| Recall trigger conditions | Detect when rollback, pause, or recall must occur. |

Monitoring events should be tied to rollout stage and tenant scope so a replay can show when a release passed, failed, paused, rolled back, or required recall.

## Rollback Audit

Rollback restores a known-good package, policy, prompt, detection, playbook, retrieval configuration, or report template.

Rollback audit must record:

1. rollback trigger;
2. triggering monitoring event or exception record;
3. package being rolled back;
4. affected tenants, cohorts, service towers, workflows, or environments;
5. previous active version;
6. rollback target;
7. approval or emergency authorization;
8. rollback start time;
9. activation status of target version;
10. failed or skipped tenants;
11. validation that unsafe version is no longer active;
12. final rollback state;
13. follow-up change or remediation reference.

Rollback must not destroy the audit trail of the bad release. The rollout ledger must preserve both the failed version and the recovery action.

## Recall and Kill-Switch Audit

Recall removes, disables, quarantines, or blocks an unsafe package or shared intelligence item. A kill switch is the emergency form of recall.

Recall audit must record:

| Field | Purpose |
|---|---|
| `recall_id` | Unique recall sequence identifier. |
| `recall_type` | Standard recall, emergency recall, kill switch, quarantine, retrieval block, detection disablement, or package pinning. |
| `trigger` | Compromised agent, unsafe output, cross-tenant risk, bad detection, policy defect, prompt contamination, tool abuse, or monitoring failure. |
| `triggering_event_ref` | Monitoring, exception, policy, approval, or incident record that caused recall. |
| `affected_package_refs` | Package, prompt, detection, playbook, policy, tool contract, retrieval, or report template versions affected. |
| `affected_scope` | Tenants, cohorts, service towers, workflows, cases, outputs, or environments affected. |
| `containment_actions` | Stop invocation, revoke tokens, disable package, block retrieval, quarantine memory, suppress detection, or pin version. |
| `active_session_handling` | Whether active sessions were stopped, allowed to finish, quarantined, or reviewed. |
| `output_review_scope` | Reports, notes, recommendations, detections, or customer-facing outputs requiring review. |
| `approval_record_id` | Emergency or accountable recall approval where required. |
| `completion_state` | Complete, partial, failed, escalated, or requires remediation. |

Recall must be replayable even when invoked under emergency conditions.

## Replay Requirements

A reviewer should be able to replay a rollout from the audit record alone.

Replay must support the following questions:

| Replay Question | Required Evidence |
|---|---|
| What version was active for this tenant at this time? | Activation events, tenant eligibility records, package manifest, rollback or recall records. |
| Why did this tenant receive the package? | Tenant eligibility result, rollout scope, policy decision, approval records. |
| Who approved the rollout? | Approval record, approver identity, approval scope, approval time. |
| What controls were validated before release? | Validation records, gate outcomes, risk classification, policy decisions. |
| What changed between versions? | Package manifest, component references, previous version, release notes or change summary. |
| Was the package signed or provenance-checked? | Signature, checksum, package integrity record. |
| What monitoring gates were active? | Monitoring profile, gate evaluations, thresholds, outcomes. |
| Did rollout cause failures or exceptions? | Exception records, policy denials, fail-closed events, tool failures, customer-impacting signals. |
| Was rollback possible and tested? | Rollback target, validation result, rollback event records. |
| Was recall invoked? | Recall record, trigger, affected scope, containment actions, completion state. |
| Did cross-tenant sanitized intelligence participate? | Sanitization record, release approval, destination scope, tenant eligibility, recall path. |

## Replay Procedure

A standard replay should follow this sequence:

1. Identify `release_id`, `package_id`, `package_version`, or `rollout_id`.
2. Retrieve the package manifest and integrity record.
3. Retrieve the original change request and owner record.
4. Retrieve validation records and gate outcomes.
5. Retrieve policy requests and PDP decisions.
6. Retrieve approval records.
7. Retrieve tenant eligibility records and exclusions.
8. Retrieve rollout stage events.
9. Retrieve activation events by tenant, cohort, service tower, workflow, or environment.
10. Retrieve monitoring gate evaluations.
11. Retrieve exception, denial, or failure records.
12. Retrieve rollback, recall, or retirement events if present.
13. Confirm final state and active version timeline.
14. Verify audit chain integrity and identify any missing records.

A replay is incomplete if the active version cannot be determined, approval cannot be verified, tenant eligibility cannot be reconstructed, monitoring gate outcome is missing, or rollback/recall state is unknown for an affected release.

## Example Rollout Audit Record

```json
{
  "audit_event_id": "audit-2026-05-22-004201",
  "event_type": "fleet.rollout.stage.completed",
  "event_version": "1.0",
  "event_time": "2026-05-22T18:45:31Z",
  "recorded_time": "2026-05-22T18:45:35Z",
  "producer": {
    "component": "fleet-governance-service",
    "component_version": "fleet-governance-service@2.4.0",
    "environment": "managed-security-control-plane"
  },
  "correlation": {
    "correlation_id": "corr-fleet-release-2026-0017",
    "change_request_id": "change-2026-0017",
    "release_id": "release-2026-0017",
    "rollout_id": "rollout-identity-abuse-pack-2.3.4",
    "rollout_stage_id": "stage-canary-001"
  },
  "package": {
    "package_id": "identity-abuse-detection-pack",
    "package_version": "2.3.4",
    "package_type": "detection_package",
    "package_manifest_ref": "manifest://fleet/identity-abuse-detection-pack/2.3.4",
    "previous_version": "2.3.3",
    "rollback_target": "identity-abuse-detection-pack@2.3.3",
    "signature_ref": "sig://fleet/identity-abuse-detection-pack/2.3.4"
  },
  "scope": {
    "service_towers": ["mdr", "managed-soc"],
    "destination_scope": "canary_mdr_tenant_group",
    "tenant_group_id": "mdr-canary-group-01",
    "excluded_tenants": ["regulated-customer-example"],
    "data_boundary_classification": "derived_sanitized_intelligence"
  },
  "controls": {
    "validation_refs": [
      "validation://release-2026-0017/policy-boundary-check",
      "validation://release-2026-0017/detection-quality-check",
      "validation://release-2026-0017/sanitization-review"
    ],
    "policy_decision_id": "policy-decision-release-2026-0017",
    "approval_record_id": "approval-release-2026-0017",
    "tenant_eligibility_record_id": "eligibility-release-2026-0017-canary",
    "monitoring_profile_id": "monitoring-profile-medium-impact-detection-rollout"
  },
  "stage_result": {
    "stage": "canary",
    "decision": "continue_to_limited_cohort",
    "outcome": "passed",
    "monitoring_summary": {
      "policy_denials": 0,
      "tenant_boundary_failures": 0,
      "false_positive_signal": "within_expected_range",
      "customer_impact": "none_detected"
    }
  },
  "next_step": {
    "next_stage": "limited_cohort",
    "requires_additional_approval": false
  }
}
```

This example shows the audit shape for one rollout stage. Production implementations should validate event shapes, field names, identifiers, access control, retention, and storage integrity against their own control requirements.

## Example Recall Audit Record

```json
{
  "audit_event_id": "audit-2026-05-23-000817",
  "event_type": "fleet.recall.invoked",
  "event_version": "1.0",
  "event_time": "2026-05-23T03:14:22Z",
  "recorded_time": "2026-05-23T03:14:24Z",
  "producer": {
    "component": "fleet-governance-service",
    "environment": "managed-security-control-plane"
  },
  "correlation": {
    "correlation_id": "corr-fleet-release-2026-0017",
    "release_id": "release-2026-0017",
    "rollout_id": "rollout-identity-abuse-pack-2.3.4",
    "recall_id": "recall-2026-0017-emergency"
  },
  "recall": {
    "recall_type": "emergency_recall",
    "trigger": "unexpected_false_positive_spike",
    "triggering_event_ref": "monitoring://rollout-identity-abuse-pack-2.3.4/anomaly-003",
    "affected_package_refs": ["identity-abuse-detection-pack@2.3.4"],
    "affected_scope": {
      "tenant_groups": ["mdr-canary-group-01"],
      "service_towers": ["mdr", "managed-soc"]
    },
    "containment_actions": [
      "disable_detection_version_2.3.4",
      "pin_to_identity-abuse-detection-pack@2.3.3",
      "block_new_activation",
      "open_review_for_generated_alerts"
    ],
    "approval_record_id": "emergency-approval-recall-2026-0017",
    "completion_state": "recall_in_progress"
  }
}
```

## Data Minimization and Access Control

Fleet rollout audit records should preserve control facts without copying unnecessary customer data, evidence content, secrets, prompts, raw logs, or case narratives.

Audit records should reference sensitive material by controlled identifiers such as evidence references, package references, validation records, approval records, and policy decision records.

Access to rollout audit records should be scoped because they may reveal:

- customer eligibility or exclusion status;
- operational capabilities deployed to specific tenants;
- security detection logic or playbook behavior;
- emergency recall triggers;
- service delivery defects;
- customer approval requirements;
- investigation-sensitive context;
- package provenance and control-plane behavior.

## Failure and Exception Handling

Rollout failures must be audited and correlated to the rollout ledger.

| Failure | Required Audit Response |
|---|---|
| Package manifest missing | Stop rollout and create fail-closed event. |
| Package signature invalid | Block release, preserve package integrity evidence, and route to investigation. |
| Validation record missing | Deny rollout or require remediation. |
| Approval missing or expired | Stop rollout or route to approval workflow. |
| Tenant eligibility missing | Block activation for affected tenants. |
| Tenant exclusion ignored | Recall affected scope and preserve eligibility records. |
| Monitoring unavailable | Pause rollout or fail closed for high-impact release. |
| Rollback target missing | Deny broad rollout until recovery path exists. |
| Activation drift detected | Identify affected tenants, stop further rollout, and reconcile active version state. |
| Cross-tenant sanitized intelligence issue | Recall or quarantine release and preserve sanitization and destination-scope records. |
| Audit logging unavailable | Stop or fail closed for governed rollout. |

Failure details should be recorded in `exception-and-failure-audit.md` format and correlated back to the rollout ledger.

## Audit Queries the Model Should Support

The audit model should support review and operational queries such as:

- Which version of an agent, prompt, detection, playbook, or policy bundle was active for a tenant at a specific time?
- Which tenants received a specific release?
- Which tenants were excluded and why?
- Which approval authorized a release or emergency recall?
- Which validation records supported release readiness?
- Which monitoring signal triggered rollback or recall?
- Which package versions are currently active, paused, recalled, retired, or superseded?
- Which releases used sanitized intelligence derived from customer operations?
- Which active workflows used a recalled version?
- Which customer-facing outputs or case notes may require review after recall?
- Which tool actions occurred under an affected package version?
- Did all affected tenants return to a known-good version after rollback?

## Retention and Integrity

Fleet rollout audit records should be retained according to organizational, customer, contractual, regulatory, and operational requirements.

Retention decisions should consider:

- customer reporting obligations;
- service assurance requirements;
- incident and DFIR review needs;
- policy tuning and release governance;
- evidence and case retention requirements;
- legal hold or regulatory preservation;
- operational need to replay historical package behavior.

Where supported, rollout audit records should include sequence numbers, hashes, signatures, append-only storage references, or integrity metadata. Immutable storage guidance belongs in `immutable-audit-guidance.md`.

## Acceptance Criteria

Fleet rollout audit is acceptable when all of the following are true:

- every release has a change request, owner, package manifest, version, and destination scope;
- every rollout has a stable rollout ID and correlation ID;
- package contents, dependencies, policy bindings, and rollback target are recorded;
- validation, approval, policy, tenant eligibility, monitoring, and integrity gates are recorded;
- activation can be reconstructed by tenant, customer, cohort, service tower, workflow, or environment;
- rollout stage transitions are auditable;
- denied, paused, failed, rolled-back, recalled, superseded, and retired states are preserved;
- monitoring events can be tied to rollout gates and affected scope;
- rollback and recall can be reconstructed from trigger to completion;
- audit records avoid unnecessary raw customer data while preserving authorized references;
- replay can determine what version was active, why it was active, who approved it, which controls passed, and what happened after release.

## Related Repository Areas

- [`agent-governance/`](../agent-governance/readme.md) for agent identity, lifecycle, fleet governance, versioning, rollback, and recall.
- [`policy-enforcement/`](../policy-enforcement/readme.md) for PDP/PEP behavior, release authorization, action risk, and fail-closed decisions.
- [`human-oversight/`](../human-oversight/readme.md) for review, approval, customer approval, escalation, and emergency override.
- [`tenant-isolation/`](../tenant-isolation/readme.md) for tenant boundaries, tenant eligibility, and cross-tenant propagation controls.
- [`data-ingestion/`](../data-ingestion/readme.md) for sanitization inputs, metadata, normalization, and enrichment context.
- [`evidence-traceability/`](../evidence-traceability/readme.md) for evidence support and source references used by release decisions.
- [`tool-access/`](../tool-access/readme.md) for mediated tool execution and controlled publishing paths.
- [`audit-replay/audit-event-model.md`](audit-event-model.md) for baseline event fields.
- [`audit-replay/audit-correlation-model.md`](audit-correlation-model.md) for correlation identifiers and replay chains.
- [`audit-replay/exception-and-failure-audit.md`](exception-and-failure-audit.md) for rollout failures, denials, and fail-closed events.
- [`audit-replay/immutable-audit-guidance.md`](immutable-audit-guidance.md) for storage integrity and immutability guidance.

