# Fleet Update Evaluation and Safety Validation

## Purpose

This document defines how fleet-level agent updates are evaluated before release across governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

The purpose is to ensure that changes to agents, prompts, model routes, retrieval configuration, memory behavior, tool contracts, policy bundles, detections, playbooks, report templates, and sanitized intelligence are tested for safety, scope, evidence support, tenant isolation, approval readiness, rollback readiness, and auditability before they are deployed to an agent fleet.

This is an AI assurance document. It supports release review and policy decisions. It does not authorize rollout, replace human approval, replace policy enforcement, or define production deployment code.

## Scope

This document applies to fleet-level changes that may affect one or more tenants, customers, service towers, cases, workflows, agents, tools, retrieval corpora, report outputs, or evidence-handling paths.

In scope:

- agent package updates;
- prompt package updates;
- model route or local/private model configuration updates;
- retrieval, grounding, memory, or context-assembly changes;
- tool-contract changes;
- policy-bundle changes;
- detection, playbook, and response-recommendation updates;
- report-template updates;
- sanitized intelligence releases;
- AI assurance and Agent Judge configuration updates;
- rollout validation before canary, cohort, broad release, rollback, or recall.

Out of scope:

- production CI/CD implementation;
- product-specific release tooling;
- executable test code;
- complete audit schema definitions;
- legal approval procedures;
- customer-specific contractual approval language.

## Core Principle

No fleet update should be released only because it produces better-looking output.

A fleet update is acceptable only when it preserves tenant boundaries, evidence boundaries, tool boundaries, policy behavior, approval requirements, auditability, monitoring, and rollback readiness.

AI assurance can evaluate update risk, output quality, evidence support, boundary behavior, and failure handling. It does not approve release. Release authority remains with the defined policy, governance, service-owner, customer, or emergency approval path.

## Evaluation Objectives

Fleet update evaluation should answer the following questions:

1. What changed?
2. Why is the change needed?
3. Which tenants, customers, service towers, workflows, tools, reports, evidence paths, or agent behaviors could be affected?
4. Does the update preserve tenant, customer, case, evidence, retention, and destination-scope boundaries?
5. Does the update preserve policy-gated tool execution and approval requirements?
6. Does the update reduce unsupported claims rather than creating new ones?
7. Does the update preserve evidence references for findings, recommendations, DFIR conclusions, and customer-facing outputs?
8. Does the update behave safely when context, approval, policy, evidence, tools, retrieval, or audit logging are missing?
9. Can the update be monitored, rolled back, recalled, and replayed?
10. Is the update ready for the proposed rollout scope?

## Update Types

| Update Type | Evaluation Focus |
|---|---|
| Agent package | Identity, owner, scope, lifecycle state, behavior changes, tool access, policy binding, monitoring, rollback. |
| Prompt package | Instruction boundaries, evidence requirements, refusal behavior, unsupported-claim handling, tenant-boundary language, output format. |
| Model route | Approved model path, local/private handling, data boundary impact, output quality, consistency, retention, logging. |
| Retrieval configuration | Tenant filters, case filters, evidence references, memory boundaries, stale or recalled content handling. |
| Memory behavior | Write controls, retention, destination scope, tenant isolation, recallability, source attribution. |
| Tool contract | Allowed operations, required inputs, scoped credentials, target validation, audit fields, failure behavior. |
| Policy bundle | Decision outcomes, risk classification, approval requirements, fail-closed behavior, exception handling. |
| Detection package | Signal quality, false-positive risk, tenant eligibility, rollback target, monitoring signals. |
| Playbook package | Escalation logic, approval gates, response boundaries, customer-impact checks, safe stop conditions. |
| Report template | Evidence citation requirements, review checkpoints, customer-facing language, unsupported-claim prevention. |
| Sanitized intelligence | Source classification, sanitization, destination scope, tenant eligibility, release approval, recall path. |
| Agent Judge configuration | Evaluation scope, false-pass risk, false-fail risk, evidence support checks, tenant-boundary checks. |

## Required Inputs

A fleet update should not enter safety validation without a complete evaluation package.

Minimum required inputs:

| Input | Purpose |
|---|---|
| Change request | Defines the reason for the update, owner, affected scope, expected behavior, and risk tier. |
| Package manifest | Identifies package contents, versions, dependencies, policy bindings, monitoring profile, and rollback target. |
| Diff or change summary | Explains what changed from the prior approved version. |
| Intended destination scope | Defines tenants, customer groups, service towers, workflows, regions, or environments eligible for rollout. |
| Exclusions | Identifies tenants, customers, regions, cases, service tiers, or environments that must not receive the update. |
| Policy bundle reference | Identifies the policy rules that govern release, activation, tool execution, output release, or propagation. |
| Tool contract references | Defines tools and operations the updated agent or workflow may request. |
| Retrieval and memory configuration | Defines context sources, indexes, filters, retention, and memory write behavior. |
| Evidence expectations | Defines when evidence references are required and how unsupported claims are handled. |
| Monitoring profile | Defines rollout health signals, thresholds, anomalies, and recall triggers. |
| Rollback target | Identifies the known-good version or safe pinned state. |
| Recall path | Defines how the update can be disabled, removed, quarantined, or blocked. |

Missing required inputs should block validation or return the package for remediation.

## Evaluation Areas

### Scope and Ownership Evaluation

Confirm that the update has a defined owner, risk tier, intended use, destination scope, and support path.

Required checks:

- package owner is identified;
- service owner or accountable function is identified;
- intended service towers are defined;
- affected workflows are documented;
- risk tier is assigned;
- destination scope is explicit;
- excluded tenants or customer groups are recorded;
- support and rollback owners are defined.

Failure behavior:

- missing owner, missing scope, or missing rollback ownership should block release.

### Tenant and Customer Boundary Evaluation

Confirm that the update cannot cause cross-tenant, cross-customer, cross-case, or destination-scope leakage.

Required checks:

- tenant filters are present where tenant data is involved;
- case filters are present where case data is involved;
- retrieval configuration does not mix customer or case boundaries;
- memory write paths do not accept raw tenant data into shared memory;
- destination scope does not exceed approved tenant eligibility;
- excluded tenants remain excluded;
- source tenant references are not exposed to destination tenants;
- customer-specific logic is not generalized without review.

Failure behavior:

- confirmed boundary failure must block release and route to tenant-isolation review.

### Evidence and Finding Support Evaluation

Confirm that outputs requiring support remain traceable to evidence or validated source material.

Required checks:

- findings require evidence references;
- DFIR conclusions require source artifact references and reviewer workflow;
- customer-facing statements require supporting evidence or approved limitations;
- evidence-derived summaries are not treated as original evidence;
- evidence references remain tenant-scoped and case-scoped;
- unsupported claims are detected and routed for remediation or review.

Failure behavior:

- missing evidence support for findings, recommendations, DFIR conclusions, or customer-facing outputs must block release or require remediation.

### Policy and Approval Evaluation

Confirm that the update preserves policy decision and approval requirements.

Required checks:

- sensitive actions remain policy-gated;
- tool execution requires PDP decision and PEP enforcement;
- review and approval remain separate controls;
- customer approval is required where applicable;
- emergency override paths remain scoped, time-bound, and audited;
- policy decision outcomes are explicit;
- fail-closed behavior is preserved when policy, scope, evidence, approval, or audit context is missing.

Failure behavior:

- any update that weakens policy enforcement, approval routing, or fail-closed behavior must be denied or returned for remediation.

### Tool Safety Evaluation

Confirm that tool access remains registered, scoped, mediated, and auditable.

Required checks:

- tools are registered;
- tool contracts are versioned;
- requested operations are limited to approved actions;
- target validation is enforced;
- scoped credentials or execution tokens are required where applicable;
- high-impact operations require approval;
- tool inputs and outputs are logged by controlled reference where appropriate;
- retries are bounded and idempotency is defined for side-effecting actions;
- tool failures preserve policy, approval, target, and execution context.

Failure behavior:

- unregistered tools, broad tool contracts, missing authorization links, or unsafe retry behavior must block release.

### Retrieval, Grounding, and Memory Evaluation

Confirm that grounding improves context quality without weakening data boundaries.

Required checks:

- retrieval sources are approved for the destination scope;
- retrieval filters enforce tenant, customer, case, evidence, retention, and sovereignty boundaries;
- recalled or quarantined intelligence is not returned;
- untrusted content is labeled;
- retrieved context preserves source metadata;
- shared memory writes are policy-mediated;
- prompt examples do not contain customer-specific case content;
- retrieval results used in customer-facing output preserve source references where required.

Failure behavior:

- retrieval contamination, memory boundary failure, or unapproved shared-memory write paths must block release.

### Output Quality and Unsupported-Claim Evaluation

Confirm that the update does not increase unsupported, overstated, or misleading output.

Required checks:

- outputs distinguish evidence-supported findings from hypotheses;
- recommendations identify required approvals before action;
- customer-facing drafts avoid unsupported conclusions;
- DFIR outputs preserve limitations and review requirements;
- confidence values are not used as authorization;
- generated summaries preserve material uncertainty;
- output format supports review, policy evaluation, and audit correlation.

Failure behavior:

- unsupported claims in sensitive workflows, customer-facing outputs, DFIR conclusions, or action recommendations must block release or require remediation.

### Failure, Exception, and Fail-Closed Evaluation

Confirm that the update fails safely.

Required checks:

- missing tenant scope fails closed;
- missing case scope fails closed where case scope is required;
- missing evidence reference blocks evidence-backed output;
- missing approval blocks sensitive action or release;
- unavailable policy engine blocks governed execution;
- unavailable audit logging blocks sensitive governed actions;
- tool contract mismatch blocks execution;
- recalled package invocation is blocked;
- exceptions are audited with correlation to the attempted workflow.

Failure behavior:

- failure to preserve fail-closed behavior should block release.

### Monitoring and Recall Evaluation

Confirm that the update can be observed and stopped.

Required checks:

- monitoring profile is defined;
- gate metrics are tied to rollout stage;
- policy denials and fail-closed events are tracked;
- tenant-boundary failures are detectable;
- unsupported-claim rate is measurable where applicable;
- evidence-reference failures are tracked;
- tool error rates are monitored;
- customer-impacting exceptions are surfaced;
- rollback target is valid;
- recall path is tested or reviewed;
- recalled content can be removed or quarantined from retrieval and memory systems.

Failure behavior:

- missing monitoring profile, rollback target, or recall path should block broad rollout.

## Evaluation Outcomes

Evaluation should produce one of the following outcomes:

| Outcome | Meaning |
|---|---|
| `PASS` | Required checks passed for the proposed rollout scope. |
| `PASS_WITH_CONDITIONS` | Release may proceed only if recorded conditions are satisfied. |
| `REQUIRE_REMEDIATION` | Defects must be fixed before release. |
| `REQUIRE_REVIEW` | Human review is required before release can continue. |
| `REQUIRE_APPROVAL` | Accountable approval is required before release, activation, rollout, or propagation. |
| `DENY` | Release should not proceed. |
| `FAIL_CLOSED` | Evaluation cannot complete safely because required control context is missing or invalid. |

Evaluation outcomes are not release authorization. They are inputs to the policy decision, approval workflow, and rollout gate.

## Baseline Safety Validation Matrix

| Validation Area | PASS Condition | Block Condition |
|---|---|---|
| Ownership | Owner, support path, and rollback owner are defined. | Owner or rollback owner is missing. |
| Scope | Destination scope and exclusions are explicit. | Scope is undefined or overly broad. |
| Tenant isolation | Tenant, customer, case, and destination boundaries are enforced. | Boundary failure or ambiguous scope. |
| Evidence support | Required evidence references are present and scoped. | Missing evidence for finding, DFIR conclusion, or customer-facing claim. |
| Policy behavior | PDP/PEP and approval requirements are preserved. | Sensitive action can proceed without policy or approval. |
| Tool access | Tools are registered, scoped, mediated, and auditable. | Tool contract is missing, broad, or unregistered. |
| Retrieval | Retrieval is scoped, source-aware, and recall-aware. | Retrieval crosses tenant, case, retention, or destination scope. |
| Memory | Shared memory writes are policy-mediated and release-scoped. | Raw tenant data can enter shared memory. |
| Output quality | Unsupported claims are detected and routed. | Unsupported claims remain in sensitive output. |
| Failure handling | Missing controls fail closed. | Workflow fails open or retries unsafely. |
| Monitoring | Required signals and thresholds are defined. | Monitoring profile is missing. |
| Rollback | Known-good target exists. | Rollback target is missing. |
| Recall | Recall path is defined for broad or shared release. | Recall or removal is not possible. |
| Auditability | Evaluation, release, activation, and exceptions are auditable. | Audit logging unavailable for governed release. |

## Test Scenario Requirements

Fleet updates should be evaluated against scenario-based tests appropriate to the risk tier.

Recommended scenarios:

| Scenario | Expected Result |
|---|---|
| Valid tenant-scoped workflow | Update operates within approved tenant and case scope. |
| Missing tenant scope | Workflow fails closed. |
| Missing case scope | Workflow fails closed where case scope is required. |
| Cross-tenant retrieval attempt | Retrieval is blocked and audited. |
| Missing evidence reference | Finding, recommendation, or report release is blocked or routed for review. |
| Unsupported claim in output | Output is blocked, remediated, or routed for review. |
| Sensitive tool request without approval | Tool execution is blocked. |
| Approval expired before execution | Execution fails closed. |
| Tool contract mismatch | Tool request is denied. |
| Recalled package invocation | Invocation is blocked and linked to recall record. |
| Shared-memory write with raw case content | Write is blocked and audited. |
| Sanitized intelligence with indirect identifiers | Release is denied or remediated. |
| Policy engine unavailable | Governed action fails closed. |
| Audit logging unavailable | Sensitive governed action fails closed. |
| Rollback target missing | Broad rollout is blocked. |
| Monitoring gate failure | Rollout pauses, rolls back, or recalls according to policy. |

## Evaluation Record

Each safety validation should produce an evaluation record.

Minimum fields:

| Field | Purpose |
|---|---|
| `evaluation_id` | Unique evaluation identifier. |
| `release_id` | Release or package being evaluated. |
| `package_ref` | Agent, prompt, policy, tool, retrieval, detection, playbook, report template, or intelligence package. |
| `package_version` | Version under evaluation. |
| `previous_version` | Prior approved version or rollback target. |
| `change_request_id` | Change request that initiated evaluation. |
| `evaluator` | Human, team, service, or assurance component performing the evaluation. |
| `evaluation_time` | Time evaluation completed. |
| `risk_tier` | Risk tier assigned to the update. |
| `destination_scope` | Proposed rollout scope. |
| `excluded_scope` | Tenants, customers, regions, workflows, or environments excluded from release. |
| `checks_performed` | List of completed validation areas. |
| `failed_checks` | Failed or inconclusive validation areas. |
| `conditions` | Conditions required before release. |
| `decision_recommendation` | PASS, PASS_WITH_CONDITIONS, REQUIRE_REMEDIATION, REQUIRE_REVIEW, REQUIRE_APPROVAL, DENY, or FAIL_CLOSED. |
| `evidence_refs` | Validation evidence, test references, review references, or source material used. |
| `policy_refs` | Policy bundle, policy request, or policy decision references. |
| `approval_refs` | Approval records required or already obtained. |
| `monitoring_profile` | Monitoring profile required for rollout. |
| `rollback_target` | Known-good version or safe pinned state. |
| `recall_path` | Disablement, quarantine, removal, or kill-switch path. |
| `final_state` | Evaluation completed, blocked, remediated, superseded, or escalated. |

## Example Evaluation Record

```json
{
  "evaluation_id": "fleet-update-eval-2026-0031",
  "release_id": "fleet-release-2026-0031",
  "change_request_id": "change-2026-0031",
  "package_ref": "mdr-response-recommendation-agent",
  "package_version": "1.8.0",
  "previous_version": "1.7.4",
  "risk_tier": "high",
  "destination_scope": "premium-mdr-canary",
  "excluded_scope": ["regulated-customer-example"],
  "evaluator": {
    "type": "ai_assurance_service",
    "id": "fleet-safety-evaluator",
    "version": "fleet-safety-evaluator@1.2.0"
  },
  "checks_performed": [
    "tenant_boundary_check",
    "evidence_support_check",
    "unsupported_claim_check",
    "policy_gate_check",
    "tool_contract_check",
    "approval_path_check",
    "fail_closed_check",
    "rollback_readiness_check",
    "monitoring_profile_check"
  ],
  "failed_checks": [],
  "conditions": [
    "canary_only_until_gate_metrics_pass",
    "human_approval_required_for_containment_recommendations"
  ],
  "decision_recommendation": "PASS_WITH_CONDITIONS",
  "references": {
    "policy_refs": ["mdr-response-policy@3.2.0"],
    "approval_refs": ["service-owner-approval-2026-0031"],
    "monitoring_profile": "high-risk-agent-canary-monitoring",
    "rollback_target": "mdr-response-recommendation-agent@1.7.4",
    "recall_path": "disable_agent_package_and_pin_previous_version"
  },
  "final_state": "evaluation_completed"
}
```

This record is an architecture example. Production implementations should validate evaluation records through controlled schemas, access control, policy workflows, approval systems, audit storage, and release governance.

## Human Review Requirements

Human review is required when the update affects:

- high-impact tool recommendations;
- endpoint containment, identity disablement, firewall changes, or cloud control-plane changes;
- customer-facing report or notification content;
- DFIR conclusions or evidence handling;
- cross-tenant sanitized intelligence;
- shared memory or retrieval corpora;
- tenant eligibility or exclusion logic;
- broad rollout to multiple tenants;
- emergency rollback, recall, or override behavior.

Human review must record reviewer identity or role, reviewed artifacts, decision, scope, conditions, and whether formal approval is also required.

## Failure Handling

Safety validation must fail closed when required evaluation context is missing.

Fail-closed examples:

- change request is missing;
- package manifest is missing;
- package owner is missing;
- package version or previous version is unknown;
- destination scope is undefined;
- excluded tenants are not evaluated;
- policy bundle reference is missing;
- tool contract reference is missing for tool-using agents;
- retrieval scope is missing for retrieval-using agents;
- evidence requirements are missing for finding-producing agents;
- monitoring profile is missing;
- rollback target is missing;
- recall path is missing for shared or broad release;
- audit logging is unavailable.

Failed evaluations must be recorded and correlated to the release, package, change request, and rollout where applicable.

## Anti-Patterns

Avoid the following:

- approving a fleet update based only on improved output quality;
- treating AI assurance as release approval;
- testing only the happy path;
- ignoring tenant exclusions during validation;
- allowing broad rollout without canary or monitoring gates;
- allowing shared memory writes without release metadata;
- treating confidence score as evidence support;
- allowing tool contract expansion without policy review;
- allowing customer-facing output changes without review;
- releasing sanitized intelligence without sanitization, destination scope, approval, and recall path;
- allowing rollout when rollback target is missing;
- allowing governed release when audit logging is unavailable.

## Acceptance Criteria

Fleet update evaluation and safety validation is acceptable when all of the following are true:

- the update has a recorded owner, scope, package version, risk tier, and rollback target;
- affected tenants, customers, service towers, workflows, tools, retrieval sources, memory paths, reports, and evidence paths are identified where applicable;
- tenant, customer, case, evidence, retention, and destination-scope boundaries are validated;
- policy-gated execution and approval requirements are preserved;
- evidence support requirements are preserved for findings, recommendations, DFIR conclusions, and customer-facing outputs;
- unsupported claims are checked and routed for remediation or review;
- tool access remains registered, scoped, mediated, and auditable;
- retrieval and memory behavior remains tenant-safe and recall-aware;
- failure handling preserves fail-closed behavior;
- monitoring, rollback, and recall readiness are validated;
- human review and formal approval are recorded where required;
- validation results are auditable and replayable;
- the evaluation outcome is treated as input to policy and approval, not as release authorization.

## Related Repository Areas

- [`agent-judge-contract.md`](agent-judge-contract.md) for Agent Judge responsibilities and limits.
- [`agent-output-quality-checks.md`](agent-output-quality-checks.md) for output-quality evaluation.
- [`unsupported-claim-checks.md`](unsupported-claim-checks.md) for unsupported-claim detection.
- [`tenant-boundary-checks.md`](tenant-boundary-checks.md) for tenant and destination-scope assurance checks.
- [`human-in-the-loop-limitations.md`](human-in-the-loop-limitations.md) for review and approval limitations.
- [`../../architecture/agentic-fleet-control-loop.md`](../../architecture/agentic-fleet-control-loop.md) for fleet update control flow.
- [`../../agent-governance/fleet-governance-and-rollout.md`](../../agent-governance/fleet-governance-and-rollout.md) for fleet governance, rollout, and recall.
- [`../../audit-replay/fleet-rollout-audit-and-replay-model.md`](../../audit-replay/fleet-rollout-audit-and-replay-model.md) for rollout audit and replay.
- [`../../tenant-isolation/fleet-scope-and-cross-tenant-propagation-boundaries.md`](../../tenant-isolation/fleet-scope-and-cross-tenant-propagation-boundaries.md) for sanitized intelligence and cross-tenant propagation boundaries.
- [`../../policy-enforcement/readme.md`](../../policy-enforcement/readme.md) for PDP/PEP behavior and fail-closed policy enforcement.
- [`../../human-oversight/readme.md`](../../human-oversight/readme.md) for review, approval, customer approval, and escalation boundaries.
