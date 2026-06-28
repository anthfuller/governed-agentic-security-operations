# Agent Access Scope

## Purpose

This document defines how agent access is scoped across tenants, customers, cases, evidence, data classes, tools, actions, environments, and output destinations.

Agent access scope ensures that agents can assist security operations only within explicit, policy-visible boundaries. Scope must be enforced by the control plane and execution boundaries, not by prompt text alone.

## Core Principle

Scope is a policy input, not a suggestion to the agent.

An agent may request access, retrieval, delegation, tool execution, or output release only within its approved scope. If scope is missing, ambiguous, stale, conflicting, unauthorized, cross-tenant, cross-customer, cross-case, or unauditable, the workflow must fail closed or route to authorized review.

## Scope Dimensions

Agent scope should be represented across multiple dimensions.

| Scope Dimension | Examples | Control Purpose |
|---|---|---|
| Tenant scope | MSSP tenant, MDR tenant, customer tenant, cloud tenant, workspace, subscription, project | Prevent cross-tenant and cross-customer activity. |
| Customer scope | Customer account, contract, service boundary, engagement | Preserve customer authority and service obligations. |
| Case scope | Incident, alert group, investigation, DFIR matter, ticket | Prevent unrelated case data mixing. |
| Evidence scope | Evidence object, manifest, forensic image, memory capture, log export, chain-of-custody record | Preserve evidence integrity and provenance. |
| Data-class scope | Security telemetry, case notes, identity logs, endpoint telemetry, forensic artifacts, customer report drafts | Enforce data handling and sensitivity boundaries. |
| Tool scope | SIEM query, threat-intel lookup, case draft, endpoint isolation, IAM containment, evidence store access | Limit available capabilities. |
| Action scope | Read, summarize, enrich, recommend, draft, update case, execute containment, release output | Separate low-risk assistance from state-changing actions. |
| Environment scope | Dev, test, lab, customer production, isolated DFIR enclave | Prevent accidental production impact. |
| Time scope | Session duration, approval window, incident window, temporary elevation | Limit standing access. |
| Output scope | Internal note, analyst draft, customer report, ticket update, detection rule, public release | Control where outputs may go. |
| Memory and retrieval scope | RAG index, case memory, customer knowledge base, shared intelligence, local evidence store | Prevent memory contamination and unauthorized reuse. |

An agent scope profile should be explicit about what is allowed and what is prohibited.

## Scope Profile Example

```json
{
  "scope_profile_id": "soc-triage-medium-risk-v1",
  "agent_id": "soc-triage-agent",
  "allowed_service_models": ["MDR", "MSSP"],
  "allowed_tenants": ["tenant-a", "tenant-b"],
  "allowed_customers": ["customer-a", "customer-b"],
  "allowed_case_types": ["alert-triage", "incident-investigation"],
  "allowed_data_classes": ["security-telemetry", "case-notes", "threat-intelligence"],
  "allowed_evidence_classes": ["log-event", "alert", "incident-record"],
  "allowed_tools": ["siem-query", "threat-intel-lookup", "case-note-draft"],
  "allowed_actions": ["retrieve", "summarize", "classify", "recommend", "draft"],
  "prohibited_actions": ["endpoint-isolation", "user-disablement", "evidence-modification", "customer-notification"],
  "allowed_output_destinations": ["internal-case-draft", "analyst-review-queue"],
  "requires_policy_evaluation": true,
  "requires_human_approval_for": ["customer-facing-output", "state-changing-action", "evidence-sensitive-conclusion"],
  "default_failure_behavior": "fail_closed"
}
```

The profile is an architecture example, not a final schema. A production schema should be validated, versioned, policy-integrated, and auditable.

## Access Scope Rules

### 1. Agent Scope Must Be Predefined

Agents must not define their own scope at runtime.

The agent may provide context for a request, but the authoritative scope must come from a registry, policy profile, approved workflow, case system, customer contract, evidence manifest, or authorized human approval record.

### 2. Scope Must Be Evaluated Before Access

Scope should be evaluated before:

- retrieving customer or case context;
- accessing memory or RAG stores;
- receiving delegated tasks from another agent;
- invoking tools or APIs;
- writing case notes or tickets;
- drafting customer-facing content;
- recommending sensitive actions;
- performing state-changing operations;
- touching evidence or forensic artifacts.

### 3. Least Privilege Applies to Agents

Agent access should be limited to the minimum required data, tool, action, time, environment, and output destination needed for the approved workflow.

Broad “SOC agent,” “all customers,” “all tools,” “all incidents,” or “admin” scope should be treated as high risk and require explicit justification, approval, monitoring, and periodic review.

### 4. Tool Availability Is Not Tool Authorization

A tool being registered does not mean the agent may use it.

The Policy Decision Point must evaluate whether the specific agent, tenant, customer, case, action, evidence reference, approval state, and requested parameters are authorized. The Policy Enforcement Point must enforce the resulting decision at the execution boundary.

### 5. Tenant and Case Scope Must Travel With Context

Tenant, customer, case, and evidence scope must remain attached to retrieved context, agent outputs, tool requests, approval packages, and audit records.

Scope must not be stripped, overwritten, inferred from free text, or silently defaulted to a broad value.

### 6. Scope Cannot Be Expanded by Agent Reasoning

An agent cannot reason itself into broader access.

Scope expansion requires a governed change, policy exception, human approval, customer approval where applicable, and updated audit record. The agent output may explain why additional scope is needed, but that output is not authorization.

## Risk-Based Scope Classes

| Scope Class | Description | Typical Controls |
|---|---|---|
| Read-only low risk | Internal enrichment, threat lookup, limited telemetry query. | Policy check, audit logging, rate limits, tenant/case validation. |
| Read-only sensitive | Evidence retrieval, identity data, customer-specific context, regulated data. | Stronger identity, evidence reference, purpose binding, human review where required. |
| State-changing operational | Case update, detection tuning draft, ticket transition, endpoint or identity action preparation. | PDP decision, PEP enforcement, approval checks, rollback/undo path where applicable. |
| Privileged or customer-impacting | Containment, identity disablement, token revocation, production configuration change, customer notification. | Formal approval, customer authority path where required, PEP enforcement, before/after audit. |
| Evidence-impacting | Evidence movement, acquisition, transformation, deletion, chain-of-custody change, forensic conclusion. | DFIR authority, evidence manifest validation, immutable audit, human forensic review. |
| Cross-tenant or shared fleet | Shared intelligence, fleet update, rule propagation, model/prompt distribution. | Sanitization, tenant eligibility, staged rollout, approval, signing, monitoring, recall path. |

## Scope Evaluation Flow

A governed access request should follow this sequence:

1. Identify the requesting agent and current lifecycle state.
2. Identify the workflow, service model, tenant, customer, case, incident, and evidence scope.
3. Identify requested data, memory, retrieval source, tool, action, parameters, and output destination.
4. Compare the request against the agent scope profile.
5. Evaluate risk classification and approval requirements.
6. Check customer authority and engagement boundaries where applicable.
7. Ask the PDP for `ALLOW`, `DENY`, `REQUIRE_APPROVAL`, `REQUIRE_CLARIFICATION`, or `FAIL_CLOSED`.
8. Enforce the decision at the relevant PEP.
9. Record the decision, enforcement result, evidence references, and output destination in audit records.

## Cross-Tenant and Cross-Customer Boundaries

Agents must not mix or reuse customer data across tenants unless a governed shared-intelligence workflow explicitly allows sanitized, approved, and auditable propagation.

Forbidden behavior includes:

- retrieving one customer’s data while operating under another customer’s case;
- using one tenant’s memory as context for another tenant;
- incorporating raw customer-specific indicators into shared outputs without sanitization and release approval;
- using fleet-level observations to make customer-specific claims without customer-scoped evidence;
- copying evidence-derived summaries across cases without provenance and authority.

Shared intelligence must be sanitized, source-controlled, approved for release, stripped of prohibited customer identifiers, scoped to eligible tenants, and audit-linked to the release decision.

## Output Destination Scope

Output scope is as important as input scope.

An agent may be allowed to draft an internal note but not release a customer-facing report. It may be allowed to prepare a containment recommendation but not execute containment. It may be allowed to summarize forensic artifacts for examiner review but not produce final findings.

Output release should be blocked when:

- the destination is not approved for the agent;
- required review or approval is missing;
- tenant or customer scope is ambiguous;
- evidence support is insufficient;
- data classification prohibits the destination;
- the output includes unsupported or policy-prohibited claims;
- customer approval is required but not present.

## Audit Requirements

Every governed access decision should record:

- requesting agent identity and version;
- lifecycle state;
- tenant, customer, case, and evidence scope;
- requested data, tool, action, and output destination;
- scope profile evaluated;
- policy decision and reason;
- approval record where required;
- PEP enforcement result;
- data returned or action performed at a reference level;
- denial, clarification, or fail-closed reason;
- correlation identifiers for replay.

## Fail-Closed Conditions

The workflow must fail closed or route to authorized review when:

- tenant, customer, case, evidence, or output destination scope is missing;
- scope conflicts with the agent profile;
- requested data class or tool is not approved;
- requested action exceeds approved risk tier;
- lifecycle state is not active;
- policy cannot evaluate the request;
- required approval is missing or stale;
- cross-tenant or cross-case context is detected;
- data retention, sovereignty, or handling constraints are unclear;
- audit logging cannot capture the decision.

## Acceptance Criteria

Agent access scope governance is acceptable when:

- every access request can be evaluated against an explicit scope profile;
- scope is checked before retrieval, tool use, delegation, and output release;
- broad access requires explicit approval and monitoring;
- tenant, customer, case, evidence, and output boundaries are preserved end to end;
- policy and PEP controls enforce scope rather than relying on prompts;
- audit records can reconstruct why access was allowed, denied, escalated, or failed closed.

## Summary

Agent access must be narrow, explicit, policy-visible, enforceable, and auditable.

> Scope is not what the agent says it is allowed to do. Scope is what the governance and enforcement layers can prove and enforce.
