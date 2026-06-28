# Sample Judge Results

## Purpose

This document provides sample AI assurance and Agent Judge result records for governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

The examples show how judge outputs can be represented as reviewable architecture artifacts. They are intended to support architecture discussion, policy design, audit replay, and implementation planning.

These samples are not executable schemas, product guidance, production validation rules, or approval records.

## Scope

Sample judge results in this document cover:

- unsupported-claim evaluation;
- evidence-support evaluation;
- tenant-boundary evaluation;
- output-quality evaluation;
- human-review recommendation;
- sensitive-action recommendation review;
- customer-facing output review;
- DFIR finding review;
- sanitized intelligence release review;
- fleet update safety validation.

Agent Judge results are assurance records. They may inform policy, review, approval, routing, remediation, or fail-closed handling. They do not authorize tool execution, customer-facing release, cross-tenant propagation, or fleet rollout by themselves.

## Core Principle

A judge result is not an approval.

A judge may evaluate output quality, evidence support, unsupported claims, tenant-boundary risk, review requirements, and policy-relevant conditions. Authorization remains with the appropriate policy decision, enforcement point, human approval, customer approval, service-owner approval, or emergency authority.

## Common Judge Result Envelope

Judge results should use a consistent envelope so they can be correlated, audited, and replayed.

```json
{
  "judge_result_id": "judge-result-example",
  "judge_id": "example-judge",
  "judge_version": "example-judge@1.0.0",
  "evaluation_type": "unsupported_claim_check",
  "evaluation_time": "2026-05-22T11:38:41Z",
  "correlation_id": "corr-example",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "agent_output_ref": "agent-output://customer-a/inc-10422/out-0007",
  "context_package_id": "ctx-10422-0004",
  "overall_result": "FAIL",
  "required_action": "revise_before_release",
  "routing": "analyst_review",
  "audit_refs": {
    "agent_invocation_id": "agent-run-10422-0007",
    "policy_request_required": false,
    "approval_required": false
  }
}
```

## Result Values

| Result | Meaning |
|---|---|
| `PASS` | No material issue was detected for the evaluation type and supplied context. |
| `WARNING` | Issue detected that requires qualification, review, monitoring, or limited use. |
| `FAIL` | Material issue detected. Output, action, release, or rollout should not proceed without remediation or review. |
| `INCONCLUSIVE` | The judge could not complete evaluation because required context, evidence, references, or scope were insufficient. |
| `FAIL_CLOSED` | The workflow must halt because required control context is missing or invalid for a governed action, output, release, or rollout. |

## Required Actions

| Action | Meaning |
|---|---|
| `continue` | Proceed to the next governed workflow step. |
| `revise_before_release` | Correct output before release or use. |
| `remove_claim` | Remove unsupported or out-of-scope claim. |
| `qualify_claim` | Restate as hypothesis, limitation, or uncertainty. |
| `add_evidence_reference` | Add valid evidence or source reference before use. |
| `route_to_analyst_review` | Human analyst review is required. |
| `route_to_forensic_review` | DFIR or forensic reviewer validation is required. |
| `route_to_policy_evaluation` | Policy decision is required before action, release, propagation, or rollout. |
| `route_to_customer_approval` | Customer approval is required. |
| `deny_release` | Output or release should not proceed. |
| `fail_closed` | Halt because required control context is missing or invalid. |

## Sample 1: Unsupported Claim Judge Result

This sample shows a customer-facing draft that claims there was no data access without supporting evidence.

```json
{
  "judge_result_id": "judge-result-2026-0042",
  "judge_id": "unsupported-claim-judge",
  "judge_version": "unsupported-claim-judge@1.0.0",
  "evaluation_type": "unsupported_claim_check",
  "evaluation_time": "2026-05-22T11:38:41Z",
  "correlation_id": "corr-2026-05-22-10422",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "agent_output_ref": "agent-output://customer-a/inc-10422/out-0007",
  "context_package_id": "ctx-10422-0004",
  "output_destination": "customer_facing_report_draft",
  "overall_result": "FAIL",
  "claim_results": [
    {
      "claim_id": "claim-001",
      "claim_type": "impact_claim",
      "claim_summary": "The draft states that no data was accessed.",
      "support_status": "unsupported",
      "supporting_refs": [],
      "reason": "No supplied evidence, tool result, or reviewer record establishes data-access scope.",
      "required_action": "remove_claim_or_qualify_as_unconfirmed",
      "routing": "analyst_review"
    }
  ],
  "required_action": "revise_before_release",
  "routing": "analyst_review",
  "audit_refs": {
    "agent_invocation_id": "agent-run-10422-0007",
    "review_record_required": true,
    "approval_required_before_customer_release": true
  }
}
```

Expected handling:

- do not release the report;
- remove or qualify the unsupported impact claim;
- route the draft to analyst review;
- require approval before customer-facing release.

## Sample 2: Evidence Support Judge Result

This sample shows a response recommendation that is partially supported by evidence but still requires policy and human approval before action.

```json
{
  "judge_result_id": "judge-result-2026-0043",
  "judge_id": "evidence-support-judge",
  "judge_version": "evidence-support-judge@1.0.0",
  "evaluation_type": "evidence_support_check",
  "evaluation_time": "2026-05-22T11:41:09Z",
  "correlation_id": "corr-2026-05-22-10422",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "agent_output_ref": "agent-output://customer-a/inc-10422/out-0008",
  "context_package_id": "ctx-10422-0004",
  "output_destination": "sensitive_action_recommendation",
  "overall_result": "WARNING",
  "finding_results": [
    {
      "finding_id": "finding-001",
      "finding_summary": "Suspicious encoded PowerShell execution was observed on the endpoint.",
      "support_status": "supported",
      "supporting_refs": [
        "evidence://customer-a/inc-10422/events/evt-001",
        "evidence://customer-a/inc-10422/events/evt-004"
      ],
      "limitations": []
    },
    {
      "finding_id": "finding-002",
      "finding_summary": "Endpoint isolation is recommended.",
      "support_status": "weakly_supported",
      "supporting_refs": [
        "evidence://customer-a/inc-10422/events/evt-001"
      ],
      "limitations": [
        "Recommendation requires policy decision and formal approval before execution."
      ]
    }
  ],
  "required_action": "route_to_policy_evaluation",
  "routing": "policy_evaluation",
  "audit_refs": {
    "policy_request_required": true,
    "approval_required_for_execution": true
  }
}
```

Expected handling:

- use the result as input to policy evaluation;
- require approval before endpoint isolation;
- do not treat evidence support as execution authorization.

## Sample 3: Tenant Boundary Judge Result

This sample shows a retrieval or context package that appears to include material outside the authorized tenant or case boundary.

```json
{
  "judge_result_id": "judge-result-2026-0044",
  "judge_id": "tenant-boundary-judge",
  "judge_version": "tenant-boundary-judge@1.0.0",
  "evaluation_type": "tenant_boundary_check",
  "evaluation_time": "2026-05-22T11:44:23Z",
  "correlation_id": "corr-2026-05-22-10422",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "context_package_id": "ctx-10422-0005",
  "retrieval_refs": [
    "retrieval://customer-a/inc-10422/query-003"
  ],
  "overall_result": "FAIL_CLOSED",
  "boundary_findings": [
    {
      "finding_id": "boundary-001",
      "boundary_type": "case_scope_mismatch",
      "description": "Retrieved context includes a record not associated with the authorized case boundary.",
      "source_ref": "retrieval-result://redacted/ref-009",
      "required_action": "quarantine_context_package"
    }
  ],
  "required_action": "fail_closed",
  "routing": "tenant_isolation_review",
  "audit_refs": {
    "exception_required": true,
    "blocked_context_package": "ctx-10422-0005"
  }
}
```

Expected handling:

- block agent invocation or downstream use;
- quarantine the invalid context package;
- create an exception audit event;
- route to tenant-isolation review.

## Sample 4: Output Quality Judge Result

This sample shows an internal investigation summary that is usable but needs qualification before analyst reliance.

```json
{
  "judge_result_id": "judge-result-2026-0045",
  "judge_id": "output-quality-judge",
  "judge_version": "output-quality-judge@1.0.0",
  "evaluation_type": "output_quality_check",
  "evaluation_time": "2026-05-22T12:03:10Z",
  "correlation_id": "corr-2026-05-22-10422",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "agent_output_ref": "agent-output://customer-a/inc-10422/out-0011",
  "context_package_id": "ctx-10422-0004",
  "output_destination": "internal_analyst_note",
  "overall_result": "WARNING",
  "quality_findings": [
    {
      "finding_id": "quality-001",
      "issue": "summary_overstates_confidence",
      "description": "The output describes the activity as confirmed compromise, but supplied evidence supports suspicious activity only.",
      "required_action": "qualify_claim"
    },
    {
      "finding_id": "quality-002",
      "issue": "missing_limitations",
      "description": "The output does not state that endpoint telemetry coverage is incomplete.",
      "required_action": "add_limitation"
    }
  ],
  "required_action": "revise_before_use",
  "routing": "analyst_review"
}
```

Expected handling:

- revise the language before use;
- preserve uncertainty;
- avoid using internal notes as customer-facing language.

## Sample 5: Human Review Recommendation Result

This sample shows an assurance result that recommends human review but does not itself approve or deny the workflow.

```json
{
  "judge_result_id": "judge-result-2026-0046",
  "judge_id": "hitl-routing-judge",
  "judge_version": "hitl-routing-judge@1.0.0",
  "evaluation_type": "human_review_recommendation",
  "evaluation_time": "2026-05-22T12:09:37Z",
  "correlation_id": "corr-2026-05-22-10422",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "agent_output_ref": "agent-output://customer-a/inc-10422/out-0012",
  "overall_result": "WARNING",
  "review_recommendation": {
    "review_required": true,
    "review_type": "formal_approval",
    "recommended_reviewer_role": "incident_commander",
    "reason": "The output recommends a high-impact containment action."
  },
  "required_action": "route_to_policy_evaluation",
  "routing": "policy_evaluation",
  "audit_refs": {
    "approval_record_required": true
  }
}
```

Expected handling:

- route to policy evaluation and approval workflow;
- do not execute based on judge recommendation alone.

## Sample 6: DFIR Finding Judge Result

This sample shows a local/private LLM-assisted DFIR output where a timeline conclusion lacks enough source support.

```json
{
  "judge_result_id": "judge-result-2026-0047",
  "judge_id": "dfir-evidence-support-judge",
  "judge_version": "dfir-evidence-support-judge@1.0.0",
  "evaluation_type": "dfir_finding_support_check",
  "evaluation_time": "2026-05-22T13:18:56Z",
  "correlation_id": "corr-dfir-2026-0091",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "dfir-0091",
  "agent_output_ref": "agent-output://customer-a/dfir-0091/timeline-draft-0003",
  "context_package_id": "ctx-dfir-0091-0002",
  "output_destination": "dfir_report_draft",
  "overall_result": "FAIL",
  "finding_results": [
    {
      "finding_id": "dfir-finding-001",
      "finding_summary": "The draft states that lateral movement occurred after credential theft.",
      "support_status": "unsupported",
      "supporting_refs": [],
      "reason": "The supplied artifact references do not establish credential theft or lateral movement sequence.",
      "required_action": "remove_or_restate_as_hypothesis",
      "routing": "forensic_review"
    }
  ],
  "required_action": "route_to_forensic_review",
  "routing": "forensic_review",
  "audit_refs": {
    "chain_of_custody_ref_required": true,
    "forensic_reviewer_required": true
  }
}
```

Expected handling:

- do not release the DFIR conclusion;
- route to forensic reviewer;
- require source artifact references and reviewed finding support.

## Sample 7: Sanitized Intelligence Release Judge Result

This sample shows a cross-tenant sanitized intelligence proposal that still contains indirect identifiers.

```json
{
  "judge_result_id": "judge-result-2026-0048",
  "judge_id": "sanitized-intelligence-release-judge",
  "judge_version": "sanitized-intelligence-release-judge@1.0.0",
  "evaluation_type": "sanitized_intelligence_release_check",
  "evaluation_time": "2026-05-22T14:02:18Z",
  "correlation_id": "corr-sanitized-intel-2026-0017",
  "release_id": "sanitized-intel-release-2026-0017",
  "source_scope_ref": "authorized-source-scope-ref",
  "destination_scope": "managed-mdr-detection-library",
  "overall_result": "FAIL",
  "sanitization_findings": [
    {
      "finding_id": "sanitization-001",
      "issue": "indirect_identifier_risk",
      "description": "The proposed release includes a customer-specific supplier relationship that could reveal the source case.",
      "required_action": "remove_or_generalize_identifier"
    }
  ],
  "required_action": "revise_before_release",
  "routing": "tenant_isolation_review",
  "audit_refs": {
    "release_approval_required": true,
    "policy_decision_required": true,
    "recall_path_required": true
  }
}
```

Expected handling:

- block release;
- revise sanitization;
- require review, policy decision, and release approval;
- preserve source references only for authorized reviewers.

## Sample 8: Fleet Update Safety Evaluation Result

This sample shows a fleet update that passes validation with rollout conditions.

```json
{
  "judge_result_id": "judge-result-2026-0049",
  "judge_id": "fleet-update-safety-evaluator",
  "judge_version": "fleet-update-safety-evaluator@1.0.0",
  "evaluation_type": "fleet_update_safety_validation",
  "evaluation_time": "2026-05-22T15:11:04Z",
  "correlation_id": "corr-fleet-release-2026-0031",
  "release_id": "fleet-release-2026-0031",
  "package_ref": "mdr-response-recommendation-agent",
  "package_version": "1.8.0",
  "previous_version": "1.7.4",
  "destination_scope": "premium-mdr-canary",
  "excluded_scope": ["regulated-customer-example"],
  "overall_result": "PASS_WITH_CONDITIONS",
  "checks_performed": [
    "tenant_boundary_check",
    "evidence_support_check",
    "unsupported_claim_check",
    "policy_gate_check",
    "tool_contract_check",
    "approval_path_check",
    "fail_closed_check",
    "rollback_readiness_check"
  ],
  "conditions": [
    "canary_only_until_gate_metrics_pass",
    "human_approval_required_for_containment_recommendations",
    "rollback_target_must_remain_pinned_until_cohort_expansion"
  ],
  "required_action": "route_to_policy_evaluation",
  "routing": "fleet_release_review",
  "audit_refs": {
    "policy_decision_required": true,
    "service_owner_approval_required": true,
    "monitoring_profile": "high-risk-agent-canary-monitoring",
    "rollback_target": "mdr-response-recommendation-agent@1.7.4"
  }
}
```

Expected handling:

- proceed only to the approved canary scope;
- require policy decision and service-owner approval;
- monitor gate metrics before expansion;
- keep rollback target available.

## Sample 9: Policy Integration Result

This sample shows how a judge result can be referenced by policy without becoming authorization.

```json
{
  "policy_request_id": "policy-req-2026-0055",
  "requested_action": "customer_report_release",
  "tenant_id": "customer-a",
  "case_id": "inc-10422",
  "input_refs": {
    "agent_output_ref": "agent-output://customer-a/inc-10422/report-draft-002",
    "judge_result_refs": [
      "judge-result-2026-0042",
      "judge-result-2026-0045"
    ],
    "evidence_refs": [
      "evidence://customer-a/inc-10422/events/evt-001",
      "evidence://customer-a/inc-10422/events/evt-004"
    ]
  },
  "policy_decision": {
    "decision": "REQUIRE_REVIEW",
    "decision_reason": "One judge result found unsupported customer-facing impact language.",
    "required_role": "incident_commander",
    "release_allowed": false
  }
}
```

Expected handling:

- policy references judge results;
- policy still makes the decision;
- release remains blocked until review and approval requirements are satisfied.

## Sample 10: Inconclusive Judge Result

This sample shows a judge result that cannot complete because required evidence references are missing.

```json
{
  "judge_result_id": "judge-result-2026-0050",
  "judge_id": "unsupported-claim-judge",
  "judge_version": "unsupported-claim-judge@1.0.0",
  "evaluation_type": "unsupported_claim_check",
  "evaluation_time": "2026-05-22T16:22:39Z",
  "correlation_id": "corr-2026-05-22-10422",
  "tenant_id": "customer-a",
  "case_id": "inc-10422",
  "agent_output_ref": "agent-output://customer-a/inc-10422/out-0015",
  "context_package_id": "ctx-10422-0008",
  "overall_result": "INCONCLUSIVE",
  "reason": "The agent output contains evidence-backed claims, but the referenced evidence objects were not available to the judge.",
  "missing_inputs": [
    "evidence_refs",
    "tool_result_refs"
  ],
  "required_action": "fail_closed",
  "routing": "audit_and_context_review",
  "audit_refs": {
    "exception_required": true,
    "policy_decision_allowed": false
  }
}
```

Expected handling:

- do not proceed as if the output passed;
- route to remediation;
- create exception audit where required;
- restore evidence references before reevaluation.

## Anti-Patterns

Avoid the following:

- treating a judge result as authorization;
- using a judge `PASS` as approval for tool execution;
- ignoring `WARNING`, `FAIL`, `INCONCLUSIVE`, or `FAIL_CLOSED` results;
- allowing judge results without correlation identifiers;
- storing judge results without agent output references;
- allowing judge output to rewrite evidence history;
- treating an agent summary as evidence because a judge did not fail it;
- releasing customer-facing content after unsupported-claim failure;
- propagating sanitized intelligence after tenant-boundary failure;
- rolling out fleet updates based only on improved output wording.

## Acceptance Criteria

Sample judge results are useful when they demonstrate that:

- judge results are structured and replayable;
- judge identity and version are recorded;
- evaluated output, context package, tenant, case, and correlation identifiers are present;
- findings distinguish supported, weakly supported, unsupported, contradicted, out-of-scope, and inconclusive results where applicable;
- required actions route to review, policy, approval, remediation, or fail-closed handling;
- judge results inform policy but do not replace policy decisions;
- sensitive outputs, DFIR conclusions, customer-facing releases, cross-tenant propagation, and fleet rollout remain governed by policy and approval paths.

## Related Repository Areas

- [`ai-assurance/agent-judge-contract.md`](ai-assurance/agent-judge-contract.md) for Agent Judge responsibilities and limits.
- [`ai-assurance/unsupported-claim-judge.md`](ai-assurance/unsupported-claim-judge.md) for unsupported claim judge behavior.
- [`ai-assurance/unsupported-claim-checks.md`](ai-assurance/unsupported-claim-checks.md) for reusable unsupported-claim check patterns.
- [`ai-assurance/tenant-boundary-checks.md`](ai-assurance/tenant-boundary-checks.md) for tenant and destination-scope assurance checks.
- [`ai-assurance/fleet-update-evaluation-and-safety-validation.md`](ai-assurance/fleet-update-evaluation-and-safety-validation.md) for fleet update safety validation.
- [`../audit-replay/audit-event-model.md`](../audit-replay/audit-event-model.md) for audit event structure.
- [`../audit-replay/audit-correlation-model.md`](../audit-replay/audit-correlation-model.md) for correlation and replay chains.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) for PDP/PEP behavior and policy decisions.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) for review, approval, customer approval, and escalation.
