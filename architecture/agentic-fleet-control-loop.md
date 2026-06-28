# Agentic Fleet Control Loop

## Purpose

Define the control loop used to govern agent fleet changes across MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR operations.

The loop governs how agent updates, prompt changes, tool-contract changes, policy-bundle changes, retrieval changes, detection or playbook updates, and sanitized intelligence updates move from proposal through validation, approval, rollout, monitoring, rollback, recall, and audit replay.

The control loop applies to fleet-level change. Runtime security actions still require the operational policy gates defined for the specific tenant, case, evidence boundary, tool, and customer obligation.

## Scope

In scope:

- agent package changes;
- prompt package changes;
- policy bundle changes;
- tool contract changes;
- retrieval, grounding, and memory-scope changes;
- model-route or local model configuration changes;
- detection, playbook, and response-recommendation package changes;
- sanitized intelligence distribution;
- tenant eligibility and rollout targeting;
- canary, cohort, and broad rollout;
- rollback, recall, and emergency stop actions;
- audit records required to replay fleet decisions.

Out of scope:

- live incident command decisions;
- customer-specific contractual approval language;
- production schema definitions;
- implementation-specific deployment pipelines;
- executable policy code.

## Core Principle

No agent, prompt, model route, tool contract, detection package, playbook package, or shared intelligence update may reach the fleet without a recorded owner, scope, validation result, approval path, policy decision, tenant eligibility result, monitoring plan, rollback target, and audit trail.

An agent may assist with drafting, summarizing, validating, or monitoring a fleet update. It must not approve its own release, broaden its own tenant scope, bypass policy enforcement, write directly into shared fleet context, or remove recall requirements.

## Control Loop Overview

```text
Signal or change request
        ↓
Triage and risk classification
        ↓
Package assembly
        ↓
Validation and safety checks
        ↓
Human review and required approval
        ↓
Policy decision and release gate
        ↓
Tenant eligibility and rollout targeting
        ↓
Canary or limited rollout
        ↓
Monitoring and feedback
        ↓
Cohort or broad rollout
        ↓
Continuous monitoring, audit, rollback, or recall
```

The loop is continuous. Production telemetry, analyst feedback, customer impact, policy denials, recall events, and audit replay results feed back into the next change request.

## Control Loop Phases

| Phase | Purpose | Required Output |
|---|---|---|
| 1. Signal intake | Capture the reason for a fleet change or recall action. | Change request or recall request |
| 2. Triage | Identify affected agents, tenants, service towers, tools, data boundaries, and risk tier. | Triage record |
| 3. Package assembly | Bind prompts, policies, tools, retrieval scope, model route, monitoring profile, and rollback target. | Versioned package manifest |
| 4. Validation | Test policy gates, tenant isolation, tool boundaries, evidence support, output quality, and rollback behavior. | Validation record |
| 5. Review | Confirm operational value, safety, boundary handling, and release readiness. | Reviewer record |
| 6. Approval | Authorize release for a defined scope. | Approval record |
| 7. Policy gate | PDP decides allow, deny, require approval, or fail closed. | Policy decision record |
| 8. Tenant eligibility | Confirm eligible tenants, excluded tenants, service tiers, regions, and contractual constraints. | Tenant eligibility result |
| 9. Canary | Release to limited scope with active monitoring. | Canary rollout event |
| 10. Cohort rollout | Expand only when gate metrics pass. | Cohort rollout event |
| 11. Broad rollout | Release to approved fleet scope. | Fleet rollout event |
| 12. Monitor | Track behavior, denials, failures, exceptions, customer impact, and drift. | Monitoring record |
| 13. Rollback or recall | Stop unsafe behavior, pin known-good versions, revoke access, or remove propagated material. | Rollback or recall record |
| 14. Replay and closeout | Confirm the decision path, exceptions, outcomes, and lessons learned. | Audit replay summary |

## Change Inputs

Fleet changes should begin from explicit signals, not informal edits.

| Input | Example |
|---|---|
| Analyst feedback | Investigation summary lacks evidence references or produces noisy recommendations. |
| Detection engineering update | New analytic pattern, false-positive reduction, or detection tuning package. |
| Threat intelligence update | Sanitized behavior pattern or indicator set approved for limited release. |
| Policy exception | Existing policy denies a needed workflow or allows too much scope. |
| Tool contract update | Tool input schema, credential scope, action list, or audit requirement changes. |
| Retrieval update | New corpus, updated grounding rules, memory boundary change, or recalled content removal. |
| Prompt update | Safer output format, stronger evidence rules, improved escalation behavior, or unsupported-claim handling. |
| Model route update | Approved model route change for a service tower, risk tier, or local DFIR workflow. |
| Tenant eligibility change | Customer tier, region, exclusion, contract, or sovereignty requirement changes. |
| Monitoring signal | Boundary check failure, tool-call anomaly, output-quality defect, or abnormal invocation pattern. |
| Recall trigger | Compromised identity, unsafe version, prompt contamination, bad detection release, or audit failure. |

## Fleet Package Manifest Requirements

A fleet update should produce a versioned package manifest before release.

Minimum fields:

- package identifier and version;
- package owner and accountable service team;
- change reason and affected service towers;
- affected agents, prompts, policies, tools, retrieval configuration, model routes, detections, or playbooks;
- risk tier;
- eligible tenant groups;
- excluded tenants or customer groups;
- required approvals;
- validation evidence;
- monitoring profile;
- release strategy;
- rollback target;
- recall path;
- signature, checksum, or provenance record.

## State Model

| State | Meaning | Allowed Next States |
|---|---|---|
| Draft | Change has been proposed but not validated. | Validating, Cancelled |
| Validating | Package is under testing and assurance checks. | Needs remediation, Review, Cancelled |
| Needs remediation | Validation or review found defects. | Draft, Validating, Cancelled |
| Review | Human review is in progress. | Approved, Rejected, Needs remediation |
| Approved | Required approval has been recorded for a defined scope. | Policy gated, Rejected |
| Policy Gate | PDP decision is pending or completed. | Signed, Denied, Fail closed |
| Signed | Package is approved, policy-allowed, and release-ready. | Canary, Cancelled |
| Canary | Limited rollout is active. | Limited rollout, Rollback, Recall |
| Limited rollout | Controlled cohort rollout is active. | Broad rollout, Rollback, Recall |
| Broad rollout | Approved fleet scope is active. | Superseded, Rollback, Recall, Retired |
| Rollback | Package is reverted to a known-good version. | Closed, Remediated |
| Recall | Package or intelligence is blocked, removed, or quarantined. | Investigation, Closed |
| Retired | Package is no longer eligible for new use. | Closed |
| Fail closed | Required control is missing or invalid. | Needs remediation, Rejected |

## Validation Requirements

Validation should be risk-based, but the following checks are baseline requirements.

| Validation Area | Required Check |
|---|---|
| Agent identity | Agent identity is registered, owned, active, and authorized for the requested scope. |
| Version integrity | Package version, provenance, signature, checksum, and rollback target are recorded. |
| Tenant isolation | Context retrieval, memory, tools, and rollout targeting do not cross tenant or customer boundaries. |
| Tool access | Requested tools are registered, scoped, policy-mediated, and auditable. |
| Policy behavior | PDP/PEP decisions match the action risk, tenant scope, approval state, and fail-closed requirements. |
| Human oversight | Required review and approval paths are present for sensitive actions and customer-facing outputs. |
| Evidence support | Outputs requiring findings or conclusions preserve evidence references and do not overstate support. |
| Unsupported claims | Outputs are checked for conclusions that exceed evidence, context, or approved scope. |
| Retrieval and memory | Retrieval filters, retention labels, recall behavior, and shared-memory boundaries are enforced. |
| Sanitized intelligence | Cross-tenant material is sanitized, reviewed, approved, tenant-eligible, and recallable. |
| Monitoring | Required telemetry, alert thresholds, adoption metrics, and exception signals are active. |
| Rollback | Known-good version, rollback action, owner, and verification method are defined. |

A failed validation must stop release or return the package to remediation.

## Policy Gate Requirements

The release gate must evaluate the update before distribution.

Baseline decision pattern:

| Condition | Decision |
|---|---|
| Package owner is missing | Deny or fail closed |
| Agent identity is unregistered, suspended, expired, or recalled | Deny |
| Package is unsigned or provenance is missing | Deny |
| Risk tier is missing | Deny or require remediation |
| Tool contract is missing or too broad | Deny or require remediation |
| Tenant scope is undefined | Deny |
| Tenant exclusions are not evaluated | Deny |
| Required approval is missing | Require approval |
| Customer approval is required but absent | Deny or require customer approval |
| Validation failed | Deny |
| Monitoring profile is missing | Deny or delay rollout |
| Rollback target is missing | Deny |
| Audit logging is unavailable | Fail closed |
| All required controls pass | Allow for approved scope only |

## Rollout Strategy

Rollout should expand only when gates pass.

| Rollout Stage | Control Requirement |
|---|---|
| Internal validation | No tenant impact; validate package behavior, audit, and rollback. |
| Canary | Limited tenant or internal cohort; active monitoring and fast rollback. |
| Limited rollout | Controlled tenant groups based on eligibility, service tier, and risk. |
| Broad rollout | Approved tenant scope only; exclusions remain enforced. |
| Hold | Rollout pauses when monitoring, approval, policy, or tenant checks fail. |
| Rollback | Revert to known-good version when defects are confirmed or risk is unacceptable. |
| Recall | Block or remove a package when continued availability is unsafe. |

Rollout expansion should not be based only on elapsed time. Expansion requires gate metrics to pass.

## Gate Metrics

The following metrics should be reviewed before expanding from canary to wider rollout.

| Metric | Expansion Impact |
|---|---|
| Policy denial rate | High or unexpected denials indicate policy mismatch or unsafe requests. |
| Fail-closed events | Any unexpected fail-closed event requires review before expansion. |
| Tool error rate | Elevated errors may indicate contract, credential, or integration defects. |
| Tenant-boundary failures | Any confirmed boundary failure blocks expansion. |
| Unsupported-claim rate | Elevated rate requires prompt, grounding, or review remediation. |
| Evidence-reference failures | Blocks expansion for investigation, reporting, or DFIR workflows. |
| Approval bypass attempts | Blocks expansion and triggers investigation. |
| False-positive impact | High detection noise or poor recommendations require tuning. |
| Customer-impacting exceptions | Blocks expansion until impact is reviewed and corrected. |
| Recall-readiness check | Rollback or recall must be verified before expansion. |

## Emergency Recall

Emergency recall is used when a package, agent version, policy bundle, tool path, retrieval corpus, or propagated intelligence item creates unacceptable risk.

Recall triggers include:

- compromised or suspected compromised agent identity;
- unauthorized tool request pattern;
- cross-tenant or cross-case access risk;
- prompt, retrieval, or memory contamination;
- defective policy bundle;
- unsafe response recommendation pattern;
- bad detection or playbook rollout;
- customer-facing output defect;
- evidence-handling or DFIR validation defect;
- required audit or monitoring failure;
- unauthorized package distribution.

Required recall actions:

1. block new invocations of the affected version or package;
2. terminate or quarantine active sessions where appropriate;
3. revoke or rotate affected credentials;
4. pin eligible tenants to a known-good version;
5. remove or quarantine recalled retrieval content or propagated intelligence;
6. identify affected tenants, cases, outputs, tool actions, and reports;
7. preserve audit evidence;
8. notify fleet owners and affected operational teams;
9. open corrective change management;
10. require validation and approval before redeployment.

## Feedback Paths

The control loop depends on feedback from operations and governance systems.

| Feedback Source | Use |
|---|---|
| Runtime audit events | Reconstruct agent, policy, tool, approval, evidence, and tenant decisions. |
| Analyst review | Identify poor summaries, weak evidence support, missed escalations, and bad recommendations. |
| Customer review | Identify customer-facing report issues, approval gaps, and service-boundary concerns. |
| Policy denials | Detect policy drift, missing scope, missing approvals, and attempted unsafe actions. |
| AI assurance checks | Detect unsupported claims, weak evidence, tenant-boundary issues, and output-quality defects. |
| Tool telemetry | Detect unauthorized attempts, failed executions, schema errors, and excessive retries. |
| Detection metrics | Track false positives, alert volume, suppression, and customer impact. |
| Recall records | Identify systemic issues requiring package, policy, or process changes. |
| Audit replay | Verify whether the recorded decision path matches expected governance behavior. |

## Required Records

| Record | Purpose |
|---|---|
| Fleet change request | Captures reason, owner, scope, risk tier, affected packages, and expected outcome. |
| Package manifest | Defines the versioned unit being released. |
| Validation record | Captures test results, failed checks, remediations, and release readiness. |
| Review record | Captures human review findings and conditions. |
| Approval record | Captures accountable authorization for the defined scope. |
| Policy decision record | Captures PDP decision, reasons, obligations, and fail-closed behavior. |
| Tenant eligibility record | Captures allowed tenants, excluded tenants, cohorts, and constraints. |
| Rollout event | Captures canary, cohort, broad rollout, hold, rollback, or recall state. |
| Monitoring record | Captures gate metrics, anomalies, denials, failures, and impact. |
| Recall record | Captures trigger, containment actions, affected scope, and recovery status. |
| Replay summary | Confirms the complete decision path can be reconstructed. |

## Example Control Loop Record

```json
{
  "control_loop_record_id": "fleet-control-loop-2026-0042",
  "change_type": "agent_package_update",
  "package": {
    "package_id": "mdr-triage-agent@2.6.0",
    "previous_version": "mdr-triage-agent@2.5.3",
    "owner": "mdr-platform-engineering",
    "risk_tier": "medium",
    "rollback_target": "mdr-triage-agent@2.5.3"
  },
  "scope": {
    "service_towers": ["managed-soc", "mdr"],
    "eligible_tenant_groups": ["standard-mdr", "premium-mdr"],
    "excluded_tenants": ["regulated-customer-example"]
  },
  "validation": {
    "tenant_boundary_check": "passed",
    "tool_contract_check": "passed",
    "policy_gate_check": "passed",
    "evidence_reference_check": "passed",
    "rollback_check": "passed"
  },
  "approval": {
    "reviewer": "mdr-service-owner",
    "approval_record": "approval-2026-0042"
  },
  "policy": {
    "decision": "allow",
    "decision_scope": "canary_then_limited_rollout"
  },
  "rollout": {
    "state": "canary",
    "monitoring_profile": "medium-risk-agent-rollout",
    "expansion_gate": "no_boundary_failures_no_customer_impact"
  }
}
```

## Fail-Closed Conditions

Fleet control must deny, halt, or fail closed when required controls are missing or invalid.

Examples:

- package owner is missing;
- package version is unsigned, unapproved, recalled, or not eligible for the tenant;
- rollback target is missing;
- monitoring profile is missing or inactive;
- tenant eligibility cannot be determined;
- tenant exclusion applies;
- source or destination scope is ambiguous;
- required approval is missing or stale;
- policy decision cannot be reached;
- audit logging is unavailable;
- validation detects cross-tenant exposure risk;
- tool contract allows broader access than the package requires;
- shared retrieval content cannot be removed after recall;
- sanitized intelligence lacks release approval;
- DFIR output lacks required evidence review;
- customer-facing output lacks required review or approval.

## Acceptance Criteria

The fleet control loop is acceptable when it can demonstrate all of the following:

- every fleet change starts from a recorded request or recall trigger;
- every package has an owner, version, risk tier, scope, monitoring profile, and rollback target;
- validation covers tenant isolation, tool boundaries, policy behavior, evidence support, and recall readiness;
- required human and customer approvals are recorded before release where applicable;
- PDP/PEP gates decide and enforce release scope;
- tenant eligibility and exclusions are enforced before rollout and consumption;
- canary and cohort expansion depend on gate metrics;
- unsafe versions can be halted, rolled back, or recalled;
- propagated intelligence can be removed or quarantined;
- audit records can replay the full path from change request to rollout, denial, rollback, recall, or closeout.

## Related Repository Areas

- [`agent-governance/`](../agent-governance/readme.md) for agent identity, lifecycle, fleet governance, monitoring, versioning, and rollback.
- [`policy-enforcement/`](../policy-enforcement/readme.md) for PDP/PEP behavior, policy contracts, action-risk classification, approval policy, and fail-closed decisions.
- [`human-oversight/`](../human-oversight/readme.md) for review, approval, customer approval, and escalation paths.
- [`tenant-isolation/`](../tenant-isolation/readme.md) for tenant boundaries, scope validation, and cross-tenant propagation controls.
- [`tool-access/`](../tool-access/readme.md) for tool registration, scoped execution, restricted tool patterns, and tool audit.
- [`data-ingestion/`](../data-ingestion/readme.md) for source metadata, normalization, enrichment, and sanitization inputs.
- [`evidence-traceability/`](../evidence-traceability/readme.md) for evidence references, DFIR evidence handling, and finding support.
- [`audit-replay/`](../audit-replay/readme.md) for audit events, replayability, correlation, exception handling, and immutable audit guidance.
