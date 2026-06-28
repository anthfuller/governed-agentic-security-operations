# Unsupported Claim Judge

## Purpose

This document defines the role, scope, evaluation criteria, and output expectations for an Unsupported Claim Judge used in governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

The Unsupported Claim Judge evaluates whether an agent output makes claims, findings, recommendations, summaries, conclusions, or customer-facing statements that are not supported by the supplied evidence, approved context, policy records, tool results, or reviewed source material.

This is an AI assurance control. It does not authorize execution, approve customer-facing output, replace forensic review, replace policy enforcement, or decide whether a tool action may proceed.

## Scope

The Unsupported Claim Judge applies to agent outputs that may influence:

- alert triage;
- investigation summaries;
- incident classification;
- response recommendations;
- containment recommendations;
- threat hunting summaries;
- customer-facing reports;
- executive summaries;
- DFIR findings;
- timeline conclusions;
- evidence-derived summaries;
- sanitized intelligence proposals;
- detection or playbook recommendations;
- fleet update evaluation records.

In scope:

- identifying claims that lack evidence support;
- identifying conclusions that overstate available evidence;
- identifying recommendations that exceed approved context or policy scope;
- identifying customer-facing statements that are not traceable to reviewed evidence;
- identifying DFIR conclusions that are not supported by source artifacts or reviewer validation;
- distinguishing evidence-backed facts from hypotheses, assumptions, estimates, and recommendations;
- routing unsupported or weakly supported outputs for remediation, review, approval, or policy evaluation.

Out of scope:

- deciding whether a response action is authorized;
- approving tool execution;
- approving customer-facing release;
- replacing human review or forensic validation;
- determining legal sufficiency;
- determining final incident severity by itself;
- performing complete evidence collection;
- validating production schemas or deployment code.

## Core Principle

An agent output must not present unsupported content as fact.

The judge must identify where the output makes a claim that cannot be traced to the supplied context, evidence references, tool results, policy records, or approved reviewer notes.

A judge result is advisory and policy-consumable. It is not an approval decision, policy decision, or execution authorization.

## What Counts as a Claim

A claim is any statement that asserts or implies something about a tenant, customer, case, user, endpoint, identity, threat actor, root cause, impact, timeline, evidence item, tool result, policy state, approval state, or recommended action.

Examples:

| Claim Type | Example |
|---|---|
| Factual claim | `The endpoint executed encoded PowerShell at 10:14 UTC.` |
| Classification claim | `This alert is a confirmed compromise.` |
| Root-cause claim | `The incident was caused by stolen credentials.` |
| Impact claim | `No customer data was accessed.` |
| Scope claim | `Only one user was affected.` |
| Attribution claim | `This activity matches threat actor X.` |
| Evidence claim | `The memory image confirms credential theft.` |
| Timeline claim | `The attacker moved laterally after mailbox compromise.` |
| Policy claim | `This action is approved.` |
| Tool-result claim | `The account was disabled successfully.` |
| Recommendation claim | `The endpoint should be isolated immediately.` |
| Customer-facing claim | `The incident is fully contained.` |

## Supported, Unsupported, and Weakly Supported Claims

| Category | Meaning | Expected Handling |
|---|---|---|
| Supported | The claim is directly supported by supplied evidence, tool output, reviewed source material, or approved context. | May proceed to the next workflow step, subject to policy and approval. |
| Weakly supported | Some context suggests the claim, but evidence is incomplete, indirect, stale, ambiguous, or not specific enough. | Mark as requiring review, qualification, or additional evidence. |
| Unsupported | The claim is not supported by the supplied context or evidence. | Block, revise, remove, or route for review. |
| Contradicted | The claim conflicts with supplied evidence, policy, tool results, or reviewer notes. | Block and route for remediation or escalation. |
| Out of scope | The claim may be true elsewhere, but it exceeds the authorized tenant, case, evidence, time, or destination scope. | Block or require scoped review. |
| Requires human validation | The claim may require analyst, forensic, legal, customer, or service-owner validation before use. | Route for review or approval as required. |

## Required Inputs

The judge should evaluate an agent output against controlled references, not general model memory.

Minimum inputs:

| Input | Purpose |
|---|---|
| `agent_output_ref` | The output being evaluated. |
| `agent_invocation_id` | The agent run that produced the output. |
| `context_package_id` | Approved context supplied to the agent. |
| `evidence_refs` | Evidence references the output relies on. |
| `retrieval_refs` | Retrieval sources, indexes, or corpus references used to build context. |
| `tool_result_refs` | Tool outputs or execution results cited or relied on. |
| `policy_refs` | Policy requests, decisions, risk classifications, or approval requirements referenced. |
| `approval_refs` | Review, approval, denial, or customer approval records referenced. |
| `scope` | Tenant, customer, case, evidence, destination, and service tower scope. |
| `output_destination` | Internal note, analyst review, customer-facing report, DFIR report, tool request, fleet update, or sanitized intelligence proposal. |
| `evaluation_policy` | Rules defining claim support, required evidence, review routing, and blocking conditions. |

If required inputs are missing, the judge should return an inconclusive or fail-closed result rather than guessing.

## Evaluation Criteria

The judge should evaluate each material claim using the following criteria.

| Criterion | Evaluation Question |
|---|---|
| Evidence linkage | Does the claim link to a relevant evidence reference, tool result, reviewed note, or approved source? |
| Evidence sufficiency | Is the cited evidence strong enough to support the claim as stated? |
| Scope alignment | Is the claim within the authorized tenant, customer, case, evidence, time, and destination scope? |
| Specificity | Does the claim overstate precision, certainty, affected scope, or timeline? |
| Recency | Is the supporting evidence current enough for the claim? |
| Contradiction check | Does any supplied evidence, policy record, or tool result contradict the claim? |
| Source distinction | Does the output distinguish original evidence, derived summary, hypothesis, and recommendation? |
| Review requirement | Does the claim require analyst, forensic, customer, legal, or service-owner review? |
| Policy sensitivity | Could the claim influence sensitive action, customer-facing release, containment, or fleet rollout? |
| Destination risk | Is the claim safe for its intended destination, especially customer-facing or cross-tenant use? |

## Unsupported Claim Patterns

The judge should flag the following patterns.

| Pattern | Description |
|---|---|
| Uncited factual assertion | A factual statement appears without evidence or source reference. |
| Overstated confidence | The output says confirmed, proven, fully contained, or no impact when evidence is incomplete. |
| Unsupported root cause | The output assigns cause without sufficient evidence. |
| Unsupported attribution | The output names a threat actor, malware family, campaign, or technique without support. |
| Unsupported scope | The output claims only one user, one device, no lateral movement, or no data access without sufficient coverage. |
| Unsupported timeline | The output gives a sequence or timestamp not supported by evidence. |
| Unsupported containment | The output claims containment, remediation, or closure without tool results and approval records. |
| Unsupported policy state | The output claims an action is approved or allowed without policy and approval references. |
| Unsupported DFIR finding | The output states a forensic conclusion without artifact reference or reviewer validation. |
| Evidence laundering | The output treats an agent summary as original evidence. |
| Cross-tenant inference | The output uses source-tenant context to make claims for another tenant. |
| Hidden assumption | The output relies on an unstated assumption as if it were evidence. |

## Evaluation Workflow

A standard unsupported-claim evaluation should follow this sequence.

```text
1. Receive agent output and evaluation request.
2. Resolve tenant, customer, case, evidence, and destination scope.
3. Load approved context package and controlled references.
4. Extract material claims from the output.
5. Classify claims by type and destination risk.
6. Check each claim against evidence, tool results, policy records, approval records, and reviewed context.
7. Identify supported, weakly supported, unsupported, contradicted, out-of-scope, and review-required claims.
8. Produce a structured judge result.
9. Route failed or inconclusive results to remediation, review, policy evaluation, or fail-closed handling.
10. Record the judge result for audit correlation and replay.
```

The judge should not use external knowledge or general model memory to support claims unless that source is explicitly included in the approved context and allowed by policy.

## Output Requirements

The Unsupported Claim Judge should produce a structured result.

Minimum output fields:

| Field | Purpose |
|---|---|
| `judge_result_id` | Unique judge result identifier. |
| `judge_id` | Identity of the judge or assurance component. |
| `judge_version` | Version of judge prompt, ruleset, model route, or evaluation logic. |
| `agent_output_ref` | Output being evaluated. |
| `context_package_id` | Context package used for evaluation. |
| `correlation_id` | Workflow correlation identifier. |
| `tenant_id` | Tenant boundary where applicable. |
| `case_id` | Case or investigation boundary where applicable. |
| `evaluation_time` | Time evaluation completed. |
| `overall_result` | PASS, WARNING, FAIL, INCONCLUSIVE, or FAIL_CLOSED. |
| `claim_results` | Per-claim evaluation results. |
| `unsupported_claim_count` | Count of unsupported claims. |
| `weakly_supported_claim_count` | Count of weakly supported claims. |
| `contradicted_claim_count` | Count of contradicted claims. |
| `out_of_scope_claim_count` | Count of out-of-scope claims. |
| `required_action` | Continue, revise, remove, review, approve, deny, or fail closed. |
| `routing` | Analyst review, forensic review, policy evaluation, customer approval, service-owner review, or remediation. |
| `audit_refs` | References needed for audit replay. |

## Example Judge Result

```json
{
  "judge_result_id": "judge-result-2026-0042",
  "judge_id": "unsupported-claim-judge",
  "judge_version": "unsupported-claim-judge@1.0.0",
  "agent_output_ref": "agent-output://customer-a/inc-10422/out-0007",
  "context_package_id": "ctx-10422-0004",
  "correlation_id": "corr-2026-05-22-10422",
  "tenant_id": "customer-a",
  "case_id": "inc-10422",
  "evaluation_time": "2026-05-22T11:38:41Z",
  "overall_result": "FAIL",
  "claim_results": [
    {
      "claim_id": "claim-001",
      "claim_text_ref": "agent-output://customer-a/inc-10422/out-0007#claim-001",
      "claim_type": "impact_claim",
      "claim_summary": "The output states that no data was accessed.",
      "support_status": "unsupported",
      "supporting_refs": [],
      "reason": "No supplied evidence or tool result establishes data-access scope.",
      "required_action": "remove_or_qualify_claim",
      "routing": "analyst_review"
    },
    {
      "claim_id": "claim-002",
      "claim_text_ref": "agent-output://customer-a/inc-10422/out-0007#claim-002",
      "claim_type": "recommendation_claim",
      "claim_summary": "The output recommends endpoint isolation.",
      "support_status": "weakly_supported",
      "supporting_refs": [
        "evidence://customer-a/inc-10422/events/evt-001",
        "judge-result://customer-a/inc-10422/tenant-boundary-check-0003"
      ],
      "reason": "Suspicious execution is supported, but containment requires policy decision and approval before action.",
      "required_action": "route_to_policy_and_human_review",
      "routing": "policy_evaluation"
    }
  ],
  "required_action": "revise_before_release",
  "audit_refs": {
    "policy_request_required": true,
    "approval_required_for_action": true
  }
}
```

This record is an architecture example. Production implementations should validate judge results through controlled schemas, access control, audit storage, and workflow policy.

## Decision Outcomes

The judge should use controlled outcomes.

| Outcome | Meaning |
|---|---|
| `PASS` | No material unsupported, contradicted, or out-of-scope claims were detected. |
| `WARNING` | Weakly supported or review-sensitive claims were detected but may be remediated or routed. |
| `FAIL` | Unsupported, contradicted, or out-of-scope claims were detected. |
| `INCONCLUSIVE` | Required context, evidence, or references were insufficient to complete evaluation. |
| `FAIL_CLOSED` | Required control context is missing or invalid for a sensitive output, action, release, or DFIR conclusion. |

## Required Actions

| Required Action | Meaning |
|---|---|
| `continue` | Output may proceed to the next governed workflow step. |
| `revise_before_release` | Output must be corrected before release or use. |
| `remove_claim` | Unsupported claim must be removed. |
| `qualify_claim` | Claim must be restated as hypothesis, limitation, or uncertainty. |
| `add_evidence_reference` | Output requires a valid evidence or source reference. |
| `route_to_analyst_review` | Analyst review is required. |
| `route_to_forensic_review` | DFIR or forensic reviewer validation is required. |
| `route_to_policy_evaluation` | Policy decision is required before action or release. |
| `route_to_customer_approval` | Customer approval is required before release or action. |
| `deny_release` | Output should not be released. |
| `fail_closed` | Workflow must halt because required control context is missing or invalid. |

## Handling by Output Destination

| Destination | Unsupported Claim Handling |
|---|---|
| Internal analyst note | Mark unsupported claims, route for analyst review, preserve uncertainty. |
| Investigation summary | Require evidence references for material findings and recommendations. |
| Sensitive action recommendation | Route to policy evaluation and approval; judge result does not authorize action. |
| Customer-facing report | Block release until unsupported claims are removed, qualified, or evidence-backed and approved. |
| Executive summary | Require careful qualification of impact, containment, scope, and confidence. |
| DFIR report | Require source artifact references and forensic reviewer validation. |
| Sanitized intelligence proposal | Require source classification, sanitization, destination scope, and tenant-boundary checks. |
| Fleet update evaluation | Require validation evidence and do not allow output quality alone to justify rollout. |

## DFIR-Specific Requirements

For private/local LLM-assisted DFIR workflows, the judge must be stricter because generated output may influence forensic findings, customer reporting, legal handling, or evidence interpretation.

DFIR claims require:

- source artifact references;
- chain-of-custody reference where applicable;
- transformation or parsing reference where applicable;
- analyst or forensic reviewer validation for final conclusions;
- clear distinction between artifact observation, interpretation, hypothesis, and conclusion;
- limitations when evidence is incomplete, partial, corrupted, or inconclusive.

The judge must flag:

- generated timelines not supported by source artifacts;
- claims that an artifact proves intent without sufficient support;
- claims that a system was compromised without supporting evidence;
- claims that data was or was not accessed without coverage;
- claims based only on model interpretation of evidence-derived text;
- conclusions that lack reviewer validation.

## Policy Integration

Unsupported-claim results should be available to policy and approval workflows.

Policy may use judge results to:

- block customer-facing release;
- require human review;
- require forensic review;
- require additional evidence;
- deny sensitive tool execution;
- require customer approval;
- fail closed when evidence support is required but missing;
- prevent fleet rollout when update evaluation includes unsupported safety claims.

Policy must not treat a `PASS` result as automatic authorization. A `PASS` only means the judge did not detect material unsupported claims under the supplied context.

## Audit Requirements

Unsupported-claim evaluation must be auditable.

Audit records should capture:

- judge result identifier;
- judge identity and version;
- evaluated output reference;
- context package reference;
- evidence references reviewed;
- claims evaluated;
- claims flagged;
- outcome and required action;
- routing decision;
- policy or approval linkage where applicable;
- final disposition after remediation;
- reviewer record where human review occurred.

The audit record should avoid embedding full sensitive output text unless the audit store is authorized for that content. Use controlled references where possible.

## Failure and Inconclusive Handling

The judge should return `INCONCLUSIVE` or `FAIL_CLOSED` when it cannot evaluate safely.

Fail-closed examples:

- agent output is missing;
- context package is missing;
- tenant or case scope is missing for tenant-scoped output;
- evidence references are required but unavailable;
- output is customer-facing and cannot be evaluated;
- output recommends sensitive action but policy or approval context is missing;
- DFIR conclusion lacks artifact reference;
- audit logging is unavailable for the judge result.

A failed or inconclusive judge result must not be ignored. It should be routed according to the output destination, action risk, evidence sensitivity, and policy requirements.

## Limitations

The Unsupported Claim Judge has limits.

- It can miss unsupported claims if the output is vague or the evidence is incomplete.
- It can flag claims that a human reviewer may later validate.
- It cannot determine legal sufficiency.
- It cannot prove evidence completeness.
- It cannot authorize execution or release.
- It cannot replace DFIR reviewer judgment.
- It should not use external knowledge unless explicitly provided in approved context.
- It depends on accurate evidence references, context packaging, and source metadata.

## Anti-Patterns

Avoid the following:

- treating judge pass as approval;
- using confidence score as evidence support;
- allowing unsupported claims in customer-facing reports;
- treating an agent summary as original evidence;
- ignoring weakly supported claims in DFIR conclusions;
- using general model knowledge to support tenant-specific findings;
- failing to preserve uncertainty;
- hiding unsupported claims by rewriting them into vague language;
- approving sensitive actions because the output sounds plausible;
- allowing fleet rollout because updated output appears more polished;
- skipping audit when a judge result fails or is inconclusive.

## Acceptance Criteria

The Unsupported Claim Judge is acceptable when:

- material claims are identified and evaluated against supplied context and references;
- supported, weakly supported, unsupported, contradicted, out-of-scope, and review-required claims are distinguishable;
- findings, recommendations, DFIR conclusions, and customer-facing statements require evidence support;
- sensitive action recommendations route to policy and approval instead of execution;
- judge outcomes are auditable and correlated to the workflow;
- inconclusive or failed evaluations are routed for remediation or review;
- tenant, customer, case, evidence, and destination boundaries are preserved;
- judge output is treated as assurance input, not approval or authorization.

## Related Repository Areas

- [`agent-judge-contract.md`](agent-judge-contract.md) for general Agent Judge responsibilities and limits.
- [`unsupported-claim-checks.md`](unsupported-claim-checks.md) for reusable unsupported-claim check patterns.
- [`agent-output-quality-checks.md`](agent-output-quality-checks.md) for broader output-quality checks.
- [`tenant-boundary-checks.md`](tenant-boundary-checks.md) for tenant and destination-scope checks.
- [`human-in-the-loop-limitations.md`](human-in-the-loop-limitations.md) for review and approval limitations.
- [`fleet-update-evaluation-and-safety-validation.md`](fleet-update-evaluation-and-safety-validation.md) for fleet update validation.
- [`../../evidence-traceability/readme.md`](../../evidence-traceability/readme.md) for evidence references and finding support.
- [`../../policy-enforcement/readme.md`](../../policy-enforcement/readme.md) for policy decisions and fail-closed enforcement.
- [`../../human-oversight/readme.md`](../../human-oversight/readme.md) for review, approval, customer approval, and escalation.
- [`../../audit-replay/audit-event-model.md`](../../audit-replay/audit-event-model.md) for audit event structure.
