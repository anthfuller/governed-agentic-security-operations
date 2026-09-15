# Fleet Update Rollout

This example models a governed production rollout for a versioned update to a managed MDR triage agent fleet.

The candidate release moves `pkg-mdr-triage-agent` from version `2.3.4` to `2.4.0`. The update improves evidence-reference handling, output-contract consistency, and tenant-boundary validation while preserving the existing tool set, action scope, approval requirements, and tenant-local data boundaries.

The records show how a fleet update request, policy decision, human approval record, and rollout audit event bind the exact package manifest, eligible destination scope, staged rollout plan, monitoring gates, rollback target, and final outcome. A request, validation result, Agent Judge result, or human approval does not independently authorize activation. The Policy Decision Point decides. The Policy Enforcement Point enforces that policy decision at package signing, release registration, activation, stage progression, rollback, and prior-version retirement boundaries by verifying the approved package, version, stage, tenant scope, validity window, and release conditions before each governed transition.

## Files

| File | Purpose |
| --- | --- |
| [`example-fleet-update-request.json`](./example-fleet-update-request.json) | Fleet change request. Records the current and proposed versions, package contents, change rationale, risk classification, candidate rollout scope, validation inputs, tenant eligibility requirements, monitoring plan, halt criteria, rollback target, and actions not authorized by the request. |
| [`example-fleet-policy-decision.json`](./example-fleet-policy-decision.json) | Policy decision record. Captures the Policy Decision Point result, approved package and manifest bindings, eligible and excluded scope, rollout-stage obligations, approval requirements, enforcement constraints, decision validity, and fail-closed behavior. |
| [`example-fleet-approval-record.json`](./example-fleet-approval-record.json) | Human fleet-change approval record. Records the accountable approver, reviewed package and policy decision, authorized rollout stages, approval conditions, expiration, rollback expectations, exclusions, and limitations. |
| [`example-fleet-audit-event.json`](./example-fleet-audit-event.json) | Rollout closeout audit event. Correlates the request, policy decision, approval, signed package, tenant eligibility results, stage transitions, monitoring outcomes, activations, exclusions, rollback readiness, and final fleet state. It represents a replay-oriented summary linked to the underlying rollout ledger; it does not replace stage-level audit events in an implementation. |

Supporting validation, AI assurance, signing, tenant eligibility, stage-gate, activation-receipt, and rollout-ledger records are referenced by these four artifacts but are not represented as separate files in this scenario.

## Scenario summary

The managed fleet `mdr-triage-agent-fleet` currently runs `pkg-mdr-triage-agent@2.3.4` as the known-good production version. The fleet owner proposes `pkg-mdr-triage-agent@2.4.0` for eligible MSSP and MDR tenant scopes.

The proposed release package contains versioned references for:

- the agent runtime definition;
- the prompt package;
- the structured output contract;
- the approved model-route binding;
- the existing tool-contract binding;
- the policy-bundle binding;
- the tenant-scoped retrieval and memory profile;
- the AI assurance evaluation profile;
- the rollout monitoring profile;
- the rollback target and recovery instructions.

The update does not add tools, broaden credentials, authorize new state-changing actions, weaken approval requirements, expand retrieval scope, enable shared tenant memory, or carry tenant-derived data inside the package.

The requested rollout uses three bounded destination cohorts:

1. `tenant-group-mdr-canary-001`
2. `tenant-group-mdr-limited-001`
3. `tenant-group-mdr-standard-001`

`tenant-regulated-example-001` is excluded because compatibility and rollback validation for its restricted operating profile are not complete. The exclusion remains in force until a separate request, validation package, policy decision, and approval authorize that tenant.

The policy decision permits staged rollout with conditions. Human approval is required before package signing and production activation. Canary and limited-cohort monitoring must pass before progression. Broad activation is limited to policy-eligible tenants, and `pkg-mdr-triage-agent@2.3.4` remains available as the tested rollback target.

The expected final state for this example is:

- the exact approved package is signed and registered;
- canary and limited stages complete within approved monitoring thresholds;
- broad rollout completes only for eligible tenant scopes;
- the excluded tenant remains pinned to the known-good version;
- no tenant-boundary violation, unapproved tool use, or package drift is detected;
- rollback remains available but is not invoked;
- the rollout ledger supports deterministic replay from request through closeout.

## Service model applicability

| Service model | Applicability |
| --- | --- |
| MSSP | Primary use case for centrally governed agent packages distributed across multiple customer and tenant service scopes. |
| MDR | Primary use case for staged release of shared triage, enrichment, investigation, and recommendation agents. |
| SOC / Incident Response | Applies when a centrally managed agent fleet is used across multiple operational teams, environments, or business units. |
| Cloud Incident Response | Applies when cloud investigation or response-assistance agents are released through the same package, eligibility, policy, monitoring, and rollback controls. |
| Private / Local LLM-assisted DFIR | Applies only when centrally managed agent, prompt, model-route, tool, or assurance packages are distributed to approved isolated forensic environments. Case evidence and case memory are not distributed by this rollout. |

## Key identifiers and version anchors

| Identifier | Value |
| --- | --- |
| Example name | `fleet-update-rollout` |
| Correlation ID | `corr-fleet-update-mdr-triage-0001` |
| Fleet update request ID | `fleet-update-req-mdr-triage-0001` |
| Policy decision ID | `fleet-policy-decision-mdr-triage-0001` |
| Approval record ID | `fleet-approval-mdr-triage-0001` |
| Rollout ID | `fleet-rollout-mdr-triage-0001` |
| Rollout audit reference ID | `audit-ref-fleet-rollout-mdr-triage-0001` |
| Fleet ID | `mdr-triage-agent-fleet` |
| Package ID | `pkg-mdr-triage-agent` |
| Current known-good version | `2.3.4` |
| Proposed version | `2.4.0` |
| Rollback target | `pkg-mdr-triage-agent@2.3.4` |

These identifiers are repeated across the four records so correlation checks can detect missing, stale, unrelated, or mismatched inputs.

## Governed sequence

1. **Submit the fleet update request.** The fleet owner records the proposed behavior change, package components, current and target versions, risk classification, candidate destination cohorts, tenant eligibility inputs, validation evidence, monitoring requirements, halt conditions, and rollback target. The request is a proposal and does not authorize signing or activation.
2. **Validate the candidate package.** Package integrity, provenance, dependency compatibility, policy bindings, tool bindings, retrieval and memory boundaries, output contract, safety evaluations, rollback readiness, and monitoring coverage are checked against the candidate manifest. Validation output is evidence for policy and human review; it is not an approval decision.
3. **Evaluate policy.** The Policy Decision Point verifies the request, package hash, manifest, fleet ownership, change risk, destination scope, tenant eligibility, required validation records, approval path, decision validity, monitoring obligations, and fail-closed requirements. The decision may allow with conditions, deny, require clarification, or fail closed.
4. **Obtain accountable human approval.** The authorized fleet-change approver reviews the exact package, policy decision, rollout scope, exclusions, stage plan, monitoring profile, rollback target, and residual risk. Approval satisfies the required human gate but cannot expand the policy decision or alter the approved manifest.
5. **Sign and register the approved release.** The release service signs the exact approved package and registers its immutable manifest, component references, signature, provenance, policy binding, monitoring profile, and rollback target. Any post-approval package or manifest change invalidates the decision and approval and requires a new governed cycle.
6. **Activate the canary stage.** The Policy Enforcement Point verifies the current decision, approval, signature, manifest, tenant eligibility, cohort scope, monitoring availability, and audit readiness before issuing stage-scoped activation authority. Only the approved canary cohort may receive the package.
7. **Evaluate stage gates.** Monitoring and assurance results are evaluated against the approved progression criteria. A passed stage permits evaluation of the next stage; it does not create unrestricted authority for broad rollout. A failed, incomplete, stale, or unavailable gate pauses or stops progression.
8. **Progress through limited and broad rollout.** Each stage revalidates the current policy decision and approval, together with eligibility, integrity, monitoring, and audit readiness. A new policy decision is required only when the package, scope, risk, conditions, or decision validity changes. Activation is limited to the tenants and cohorts allowed for that stage. Excluded tenants remain on the known-good version.
9. **Close out or recover.** The final audit event records the signed package, actual activation scope, exclusions, stage outcomes, monitoring results, final active-version state, and rollback readiness. If a halt or rollback had occurred, the same correlation chain would preserve the trigger, affected scope, containment, recovery, and final state.

## Package and data boundaries

The release package is a control-plane artifact, not a carrier for customer or case content.

It may contain or reference approved agent definitions, prompts, schemas, policies, tool contracts, model routes, retrieval rules, assurance profiles, and monitoring configuration. It must not contain:

- tenant or customer identifiers used as embedded targeting logic;
- raw alerts, logs, evidence, case notes, investigation narratives, or report content;
- credentials, tokens, secrets, connection strings, or tenant-specific keys;
- tenant-local retrieval results, vector content, case memory, or runtime conversation memory;
- hidden tool permissions or action paths not represented in the approved tool contract;
- policy exceptions, bypass instructions, or hard-coded approval substitutes;
- unsigned or unmanifested components;
- unapproved tenant-specific configuration values.

Tenant-specific configuration is resolved only after tenant eligibility and activation checks. Each activated agent continues to retrieve, reason, use memory, call tools, and release outputs within its own tenant, customer, case, evidence, environment, and destination boundaries.

This scenario does not authorize cross-tenant intelligence propagation. Reuse of tenant-derived defensive intelligence requires the separate sanitization, release, destination-scope, policy, approval, and audit path defined for cross-tenant sanitized intelligence.

## Authority and enforcement boundaries

| Actor or component | Authority boundary |
| --- | --- |
| Fleet owner or change requester | May propose and document the update. Cannot approve its own request or activate the package through the request alone. |
| Validation and AI assurance components | May evaluate package safety, behavior, evidence support, compatibility, and boundary conformance. Their outputs are advisory control inputs, not authorization. |
| Policy Decision Point | Decides whether the exact request and package are allowed, denied, restricted, escalated, or failed closed. Defines obligations, eligible scope, exclusions, and validity. |
| Human fleet-change approver | Provides accountable approval where policy requires it. Cannot override a denial, expand scope, substitute a different package, or approve beyond delegated authority. |
| Policy Enforcement Point and fleet release service | Enforce the decision and approval before signing, registration, activation, stage progression, rollback, or retirement of the prior version. |
| Tenant eligibility service | Supplies policy-verifiable eligibility and exclusion results. It does not independently activate packages. |
| Monitoring and assurance services | Produce stage-gate evidence and halt signals. They cannot silently relax thresholds or authorize progression outside the approved plan. |
| Audit and rollout ledger | Preserve the request, validation, policy, approval, signing, activation, monitoring, exception, rollback, and closeout chain. Audit records do not grant authority. |

## Rollout lifecycle

| Lifecycle stage | Required state before progression |
| --- | --- |
| Validated | Candidate manifest is complete; provenance, integrity, compatibility, safety, tenant-boundary, monitoring, and rollback checks have passed. |
| Approved | A valid policy decision and required human approval bind the same package, manifest, scope, conditions, and validity window. |
| Signed | The exact approved package is cryptographically signed and registered with an immutable manifest and rollback target. |
| Canary | Activation is limited to the approved canary cohort; monitoring and audit are active before execution. |
| Limited rollout | Canary results satisfy the approved gate; activation is limited to the approved limited cohort. |
| Broad rollout | Prior gates pass; only remaining eligible tenant scopes receive the package. Exclusions remain enforced. |
| Rollback or recall | Unsafe activation is stopped, affected scope is identified, the known-good version is restored or pinned, and recovery is audited. |

A lifecycle label is not authorization by itself. Every stage transition must be backed by current policy, approval where required, exact package integrity, tenant eligibility, monitoring readiness, and audit availability.

## Required control gates

| Gate | Required result |
| --- | --- |
| Fleet identity and ownership | Fleet, package, change owner, approver roles, and release service identities are registered and active. |
| Package manifest and provenance | All components, versions, dependencies, hashes, signatures, policy bindings, tool bindings, and rollback references are present and consistent. |
| Behavior-change review | The change delta is documented, risk-classified, validated, and shown not to create hidden scope or authority expansion. |
| Tool and action scope | The proposed version cannot call unregistered tools, request broader credentials, or perform actions outside the existing approved contract. |
| Tenant eligibility | Every target tenant or cohort is explicitly eligible for the package, service tier, environment, compatibility profile, and rollback path. |
| Boundary validation | Retrieval, memory, evidence, output, customer, tenant, case, and environment boundaries remain enforceable under the proposed version. |
| Policy decision | The decision is current, unexpired, single-purpose, and bound to the exact request, package, manifest, rollout scope, and conditions. |
| Human approval | The approval is current, unexpired, issued by an authorized role, and bound to the same package, scope, stages, and rollback plan. |
| Monitoring readiness | Required telemetry, assurance checks, thresholds, alerts, owners, and halt automation are active before activation. |
| Rollback readiness | The known-good package is available, integrity-verified, compatible with the target scope, and recoverable under the documented plan. |
| Audit readiness | Correlation, stage events, activation receipts, exclusions, monitoring results, and recovery events can be written to the rollout ledger. |

## Monitoring, pause, and halt behavior

The rollout must halt immediately when any of the following occurs:

- package signature, manifest, component hash, or provenance mismatch;
- activation request references a different package, version, stage, tenant, cohort, or validity window;
- an excluded or ineligible tenant is targeted or activated;
- a tenant, customer, case, evidence, retrieval, memory, or output boundary violation is detected;
- the proposed version requests an unapproved tool, credential, parameter class, or state-changing action;
- required policy, approval, monitoring, or audit services are unavailable;
- the rollback target is missing, invalid, unavailable, or no longer recoverable;
- package drift appears after validation or approval;
- a required stage record or activation receipt is missing or inconsistent.

The rollout must pause for review when configured monitoring thresholds are exceeded, including material increases in:

- policy denials or fail-closed events;
- unsupported claims or evidence-reference failures;
- analyst rejection, correction, or escalation rates;
- tool invocation errors, retries, timeouts, or malformed requests;
- output-contract failures or quality regressions;
- latency, resource consumption, or operational instability;
- false-positive or false-negative safety signals where measurable;
- unexplained differences between canary and prior-version behavior.

A paused or halted rollout does not automatically resume. Progression requires documented gate resolution and renewed policy evaluation or approval when the original decision, scope, package, risk, or validity conditions no longer hold.

## Fail-closed and rollback behavior

The workflow fails closed when required identity, scope, package, validation, policy, approval, eligibility, monitoring, rollback, or audit facts are missing, ambiguous, stale, mismatched, or unverifiable.

Fail-closed behavior includes:

- denying signing or registration of an unapproved package;
- blocking activation outside the approved stage or tenant scope;
- preventing broad rollout when canary or limited-stage evidence is incomplete;
- preserving excluded tenants on `pkg-mdr-triage-agent@2.3.4`;
- revoking stage-scoped activation authority after expiration, denial, halt, or rollback;
- preserving the attempted action and denial reason in the rollout ledger;
- requiring a new request, validation, policy decision, and approval for package drift or scope expansion.

If rollback is triggered, the release service must stop further activation, identify affected tenants and workflows, pin the known-good version, verify recovery, preserve outputs and tool actions produced under the affected version for review, and record the final active-version timeline. Emergency recall of a compromised agent or update channel is modeled separately under `examples/compromised-agent-recall/`.

## Audit and replay expectations

Together, the four example records should allow a reviewer to reconstruct:

- what changed between `2.3.4` and `2.4.0`;
- who requested, owned, reviewed, approved, signed, and released the update;
- which manifest, component versions, hashes, signatures, policy bindings, tool bindings, and model-route bindings governed the release;
- which validation and assurance records supported the decision;
- what the Policy Decision Point decided and what the Policy Enforcement Point enforced;
- which tenant groups were requested, eligible, activated, excluded, paused, or left on the known-good version;
- which approval authorized each rollout stage and when that authority expired;
- which monitoring profile and gate results controlled progression;
- whether any package drift, boundary violation, unapproved tool use, or scope expansion occurred;
- which version was active for each affected tenant or workflow at a specific time;
- whether rollback was available, invoked, completed, or unnecessary;
- what final fleet state was reached without relying on model memory, chat history, or informal release notes.

The audit chain must preserve successful, denied, paused, failed, rolled-back, and fail-closed paths. Correlation identifiers are traceability fields, not authorization tokens.

## Integrity invariants

| Invariant | Expected result |
| --- | --- |
| Fleet update request alone authorizes signing or activation | `false` |
| Validation or Agent Judge output grants approval | `false` |
| Policy decision required before production activation | `true` |
| Human approval required for this production fleet update | `true` |
| Approved package and manifest may change after approval | `false` |
| Package signature required before activation | `true` |
| Tenant eligibility required before activation | `true` |
| Excluded tenant may receive the proposed version | `false` |
| Canary and limited-stage gates required before broad rollout | `true` |
| Monitoring and audit must be active before each stage | `true` |
| Tool or action scope expanded by this update | `false` |
| Tenant data, case evidence, or runtime memory embedded in the package | `false` |
| Cross-tenant context or memory reuse authorized | `false` |
| Rollback target must remain available and integrity-verified | `true` |
| Scope expansion allowed without a new policy decision | `false` |
| Rollout may continue when required audit logging is unavailable | `false` |
| Excluded tenant remains on the known-good version | `true` |
| Audit records are append-only and replay-linked | `true` |

## Related repository areas

- [`architecture/agentic-fleet-architecture.md`](../../architecture/agentic-fleet-architecture.md) for fleet-level identity, version, eligibility, policy, rollout, monitoring, rollback, and audit architecture.
- [`architecture/agentic-fleet-control-loop.md`](../../architecture/agentic-fleet-control-loop.md) for the governed fleet release and recovery control loop.
- [`patterns/governed-agent-fleet-update-pattern.md`](../../patterns/governed-agent-fleet-update-pattern.md) for the reusable update pattern.
- [`patterns/fail-closed-agent-rollout-pattern.md`](../../patterns/fail-closed-agent-rollout-pattern.md) for deny, pause, halt, and rollback behavior.
- [`agent-governance/agent-change-management.md`](../../agent-governance/agent-change-management.md) for behavior-changing agent artifacts and change control.
- [`agent-governance/agent-fleet-governance.md`](../../agent-governance/agent-fleet-governance.md) for fleet ownership, tenant eligibility, staging, monitoring, and recall.
- [`agent-governance/agent-version-lifecycle-and-rollbacks.md`](../../agent-governance/agent-version-lifecycle-and-rollbacks.md) for version states, rollback targets, and retirement controls.
- [`policy-enforcement/fleet-update-authorization-and-policy-gates.md`](../../policy-enforcement/fleet-update-authorization-and-policy-gates.md) for fleet policy decisions and enforcement obligations.
- [`human-oversight/fleet-change-approval-and-emergency-override.md`](../../human-oversight/fleet-change-approval-and-emergency-override.md) for accountable approval and emergency authority boundaries.
- [`tenant-isolation/fleet-scope-and-cross-tenant-propagation-boundaries.md`](../../tenant-isolation/fleet-scope-and-cross-tenant-propagation-boundaries.md) for destination scope, exclusions, and cross-tenant controls.
- [`audit-replay/fleet-rollout-audit-and-replay-model.md`](../../audit-replay/fleet-rollout-audit-and-replay-model.md) for rollout ledger, stage events, active-version history, rollback, and replay requirements.
- [`governance-library/ai-assurance/fleet-update-evaluation-and-safety-validation.md`](../../governance-library/ai-assurance/fleet-update-evaluation-and-safety-validation.md) for assurance evaluation of candidate fleet updates.

## Documentation scope

The JSON files in this directory are non-runnable architecture artifacts. They illustrate record relationships, authorization boundaries, rollout stages, tenant eligibility, monitoring gates, rollback controls, and audit replay expectations. This repository supplies offline schemas and conformance tests; package signing, deployment automation, telemetry pipelines, and release enforcement remain external implementation responsibilities.
