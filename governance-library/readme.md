# Governance Library

## Purpose

The governance library defines reusable governance and assurance controls for agent-assisted security operations.

It supports governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows where agent outputs may influence investigation, reporting, escalation, containment recommendations, evidence interpretation, cross-tenant learning, or fleet updates.

The library provides control language for evaluating agent behavior, separating assurance from authorization, preserving evidence support, enforcing tenant boundaries, and connecting review outcomes to policy enforcement, human oversight, and audit replay.

## Scope

This directory focuses on governance and assurance controls that help determine whether agent outputs are safe, supported, scoped, and ready for the next governed workflow step.

In scope:

- AI assurance and Agent Judge responsibilities;
- judge evaluation contracts and result records;
- unsupported-claim checks;
- evidence-support checks;
- output-quality checks;
- tenant-boundary checks;
- human-review requirement checks;
- ATT&CK and ATLAS mapping review;
- fleet update safety validation;
- judge limitations and failure handling;
- alignment between assurance results, policy decisions, approvals, and audit records.

Out of scope:

- production judge code;
- model-specific evaluation pipelines;
- vendor-specific implementation guidance;
- executable policy code;
- production schema enforcement;
- legal approval procedures;
- customer-specific contractual approval language.

## Core Governance Rule

Assurance is not authorization.

Agent Judges and AI assurance controls may evaluate output quality, evidence support, tenant-boundary risk, unsupported claims, sensitive-action risk, review requirements, and fleet-update safety. They do not approve tool execution, customer-facing release, cross-tenant propagation, DFIR conclusions, or fleet rollout.

Authorization remains with the appropriate policy decision, enforcement point, human approver, customer approver, service owner, or emergency authority.

## Control Separation

| Concern | Primary Control Area | Required Separation |
|---|---|---|
| Agent output generation | Agentic workflow | Agents may propose, summarize, recommend, or draft. |
| AI assurance | `governance-library/ai-assurance/` | Judges evaluate quality, evidence support, scope, and risk. |
| Policy decision | `policy-enforcement/` | PDP decides whether an action or release is allowed, denied, or requires approval. |
| Enforcement | `policy-enforcement/` and `tool-access/` | PEP and tool gateways enforce decisions before execution. |
| Human accountability | `human-oversight/` | Review and approval are recorded by accountable roles. |
| Tenant boundaries | `tenant-isolation/` | Tenant, customer, case, destination, and cross-tenant propagation boundaries are enforced. |
| Evidence support | `evidence-traceability/` | Findings, recommendations, DFIR conclusions, and customer-facing claims remain evidence-linked. |
| Audit and replay | `audit-replay/` | Decisions, approvals, outputs, evidence references, tool actions, and outcomes are reconstructable. |
| Agent lifecycle | `agent-governance/` | Agents have identity, ownership, lifecycle state, access scope, versioning, monitoring, and recall support. |

## Directory Contents

| Path | Purpose |
|---|---|
| `ai-assurance/readme.md` | Overview of AI assurance and Agent Judge controls. |
| `ai-assurance/agent-judges-overview.md` | Explains Agent Judge roles, boundaries, and operating model. |
| `ai-assurance/judge-evaluation-contract.md` | Defines the expected structure and behavior of judge evaluations. |
| `ai-assurance/evidence-support-judge.md` | Defines how outputs are checked against evidence and source references. |
| `ai-assurance/output-quality-judge.md` | Defines quality checks for clarity, correctness, completeness, uncertainty, and destination fit. |
| `ai-assurance/tenant-boundary-judge.md` | Defines checks for tenant, customer, case, destination, and propagation-scope violations. |
| `ai-assurance/unsupported-claim-judge.md` | Defines how unsupported, weakly supported, contradicted, or out-of-scope claims are identified and handled. |
| `ai-assurance/hitl-requirement-check.md` | Defines when human review or formal approval should be required. |
| `ai-assurance/attack-atlas-mapping-judge.md` | Defines checks for ATT&CK and ATLAS mapping quality. |
| `ai-assurance/fleet-update-evaluation-and-safety-validation.md` | Defines validation expectations for fleet-level agent, prompt, policy, retrieval, detection, playbook, and sanitized-intelligence updates. |
| `ai-assurance/sample-judge-results.md` | Provides representative judge result records for architecture discussion and audit planning. |
| `ai-assurance/judge-limitations.md` | Defines limits of judge reliability, authority, and safe use. |

## Assurance Control Model

A governed assurance path should follow this pattern:

```text
Agent output or proposed update
        ↓
Scope resolution
        ↓
Evidence and context reference check
        ↓
AI assurance / Agent Judge evaluation
        ↓
Structured judge result
        ↓
Policy evaluation, review routing, remediation, or fail-closed handling
        ↓
Human or customer approval where required
        ↓
Controlled release, tool execution, propagation, or rejection
        ↓
Audit correlation and replay
```

The judge result should be treated as a controlled input to policy and review workflows, not as the final decision.

## Required Assurance Properties

AI assurance controls should preserve the following properties.

| Property | Requirement |
|---|---|
| Identity | The judge, judge version, evaluated output, agent, tenant, case, and workflow must be identifiable. |
| Scope | Evaluation must remain within the authorized tenant, customer, case, evidence, destination, and release boundary. |
| Evidence support | Material claims must be traceable to evidence, tool results, approved context, or reviewed source material. |
| Destination awareness | Internal notes, customer-facing reports, DFIR findings, tool requests, sanitized intelligence, and fleet updates require different handling. |
| Policy consumability | Results must be structured so policy can route, block, require approval, or fail closed. |
| Human accountability | Judges may recommend review, but accountable approval remains outside the judge. |
| Auditability | Results must include enough references to support replay without embedding sensitive content unnecessarily. |
| Failure safety | Missing context, missing evidence, missing tenant scope, or unavailable audit should produce inconclusive or fail-closed handling. |

## Standard Result Outcomes

AI assurance results should use controlled outcomes so they can be consumed consistently by policy, review, and audit workflows.

| Outcome | Meaning |
|---|---|
| `PASS` | No material issue was detected for the evaluation type and supplied context. |
| `WARNING` | Issue detected that requires qualification, review, monitoring, or limited use. |
| `FAIL` | Material issue detected. Output, action, release, or rollout should not proceed without remediation or review. |
| `INCONCLUSIVE` | Evaluation could not complete because required context, evidence, references, or scope were insufficient. |
| `FAIL_CLOSED` | Workflow must halt because required control context is missing or invalid for a governed action, output, release, or rollout. |

A `PASS` result does not approve execution, customer release, propagation, or rollout. It only means the judge did not detect the evaluated issue under the supplied context.

## Required Action Categories

Judge results should route to controlled next steps.

| Action | Use When |
|---|---|
| `continue` | Evaluation passed and the workflow may move to the next governed step. |
| `revise_before_release` | Output requires correction before release or use. |
| `remove_claim` | Unsupported or out-of-scope claim must be removed. |
| `qualify_claim` | Claim must be restated as hypothesis, limitation, or uncertainty. |
| `add_evidence_reference` | Valid evidence or source reference is required. |
| `route_to_analyst_review` | Analyst review is required. |
| `route_to_forensic_review` | DFIR or forensic reviewer validation is required. |
| `route_to_policy_evaluation` | PDP or policy workflow must evaluate the request. |
| `route_to_customer_approval` | Customer approval is required before release or action. |
| `deny_release` | Output, propagation, or rollout should not proceed. |
| `fail_closed` | Workflow must halt because required control context is missing or invalid. |

## When to Use This Library

Use this library when designing or reviewing workflows where agent outputs may affect:

- incident triage;
- alert enrichment;
- investigation summaries;
- response recommendations;
- containment recommendations;
- customer-facing reports;
- executive summaries;
- DFIR findings;
- evidence-derived timelines;
- detection or playbook changes;
- sanitized intelligence release;
- agent package updates;
- prompt, retrieval, tool-contract, or policy-bundle updates.

## Assurance Requirements by Workflow Type

| Workflow Type | Minimum Assurance Expectations |
|---|---|
| Internal investigation summary | Unsupported-claim check, evidence-support check, output-quality check, audit reference. |
| Sensitive action recommendation | Evidence-support check, HITL requirement check, policy evaluation, approval routing, audit reference. |
| Customer-facing report | Unsupported-claim check, evidence-support check, output-quality check, human review, approval record. |
| DFIR finding or timeline | Evidence-support check, forensic review, chain-of-custody awareness, limitation handling. |
| Tenant-scoped retrieval result | Tenant-boundary check, case-scope check, retrieval reference, fail-closed handling. |
| Sanitized intelligence release | Tenant-boundary check, identifier leakage review, evidence support, human approval, policy decision, recall path. |
| Fleet update | Fleet safety validation, tenant eligibility, policy approval, monitoring profile, rollback target, audit replay. |

## Integration with Policy Enforcement

AI assurance outputs should be available to policy evaluation, but they should not replace policy evaluation.

Policy may use judge results to:

- allow low-risk workflow continuation;
- require analyst review;
- require forensic review;
- require customer approval;
- require additional evidence;
- deny release;
- block sensitive tool execution;
- block cross-tenant propagation;
- block or pause fleet rollout;
- fail closed when required context is missing.

Policy must still produce the controlling decision. Enforcement points must still apply that decision before any governed action, release, tool execution, propagation, or rollout occurs.

## Integration with Human Oversight

Human review and approval remain separate from judge evaluation.

A judge may recommend review because an output is sensitive, weakly supported, high impact, customer-facing, DFIR-related, cross-tenant, or fleet-wide. The reviewer or approver must still make and record the accountable decision.

Human oversight records should include:

- reviewer or approver role;
- reviewed output or package reference;
- evidence or context references reviewed;
- judge result references;
- decision;
- approval scope;
- conditions;
- expiration where applicable;
- final disposition.

## Integration with Audit Replay

Assurance results must be replayable.

A replayable assurance record should identify:

- judge result ID;
- judge ID and version;
- agent output or release package evaluated;
- tenant, customer, case, and destination scope;
- context package and evidence references;
- policy request and decision references;
- approval references where required;
- required action and routing;
- final disposition.

Audit records should use controlled references where possible instead of duplicating sensitive evidence, prompts, or customer content.

## Failure Handling

AI assurance should fail safely when it cannot evaluate the workflow.

Fail-closed or inconclusive handling is required when:

- tenant scope is missing or ambiguous;
- case scope is required but missing;
- evidence references are required but unavailable;
- evaluated output cannot be resolved;
- context package is missing;
- policy state is missing for a sensitive action;
- approval state is required but unavailable;
- customer-facing output cannot be reviewed;
- DFIR finding lacks artifact support;
- sanitized intelligence contains unresolved identifiers;
- fleet update lacks validation evidence, monitoring, rollback, or recall path;
- audit logging is unavailable for a governed workflow.

A failed or inconclusive judge result must not be ignored. It should route to remediation, review, policy evaluation, exception handling, or fail-closed control.

## Anti-Patterns

Avoid the following:

- treating an Agent Judge as an approver;
- treating a judge `PASS` as authorization;
- using confidence score as evidence support;
- allowing customer-facing claims without evidence references;
- using an agent summary as original evidence;
- allowing unsupported DFIR conclusions;
- allowing sensitive actions based only on agent recommendation quality;
- bypassing policy because a judge found no issue;
- reusing tenant-specific outputs across customers without sanitization and approval;
- rolling out fleet updates because generated output appears more polished;
- ignoring `WARNING`, `FAIL`, `INCONCLUSIVE`, or `FAIL_CLOSED` results;
- storing judge results without correlation identifiers.

## Acceptance Criteria

The governance library is effective when it supports all of the following:

- agent outputs are evaluated before being trusted in sensitive workflows;
- assurance results are structured, scoped, and replayable;
- judge identity and version are recorded;
- evidence support and unsupported-claim handling are explicit;
- tenant, customer, case, evidence, and destination boundaries are preserved;
- judge results inform policy without replacing policy decisions;
- human review and formal approval remain accountable controls;
- customer-facing, DFIR, sensitive-action, cross-tenant, and fleet-update workflows have stronger assurance requirements;
- failed or inconclusive evaluations route to remediation, review, policy evaluation, or fail-closed handling;
- audit records can reconstruct evaluated output, decision path, approval path, and final disposition.

## Related Repository Areas

- [`../architecture/`](../architecture/readme.md) for architecture views, principles, assumptions, and control loops.
- [`../agent-governance/`](../agent-governance/readme.md) for agent identity, lifecycle, access scope, fleet governance, versioning, and recall.
- [`../policy-enforcement/`](../policy-enforcement/readme.md) for PDP/PEP behavior, policy contracts, action-risk classification, approval policy, and fail-closed decisions.
- [`../human-oversight/`](../human-oversight/readme.md) for human review, approval boundaries, customer approval, escalation, and emergency handling.
- [`../tenant-isolation/`](../tenant-isolation/readme.md) for tenant-boundary models, tenant-scope validation, and cross-tenant propagation controls.
- [`../tool-access/`](../tool-access/readme.md) for tool registration, scoped execution, restricted tool patterns, and tool audit.
- [`../data-ingestion/`](../data-ingestion/readme.md) for source metadata, normalization, enrichment, sanitization inputs, and ingestion replay.
- [`../evidence-traceability/`](../evidence-traceability/readme.md) for evidence references, finding support, DFIR evidence handling, and evidence audit replay.
- [`../local-llm-dfir/`](../local-llm-dfir/readme.md) for local/private LLM-assisted DFIR boundaries, output handling, and review requirements.
- [`../audit-replay/`](../audit-replay/readme.md) for audit event structure, replayability, correlation, exception audit, fleet rollout replay, and immutable audit guidance.
