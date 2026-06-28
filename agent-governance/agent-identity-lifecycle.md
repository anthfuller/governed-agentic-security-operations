# Agent Identity Lifecycle

## Purpose

This document defines how agents are registered, activated, reviewed, suspended, retired, and revoked within the governed Agentic MSSP / MDR / DFIR security operations architecture.

The goal is to ensure that agents are treated as managed enterprise identities and governed workloads, not anonymous scripts, prompts, automations, or informal assistants.

## Core Principle

An agent must have a valid identity and lifecycle state before it can participate in governed workflows.

If the agent identity is unknown, duplicated, expired, inactive, suspended, compromised, retired, or not linked to an accountable owner, the workflow must fail closed or route to authorized review.

## Lifecycle States

| State | Meaning | Permitted Activity |
|---|---|---|
| `proposed` | Agent concept is being evaluated. | No production data access, no tool execution, no customer-facing output. |
| `registered` | Agent has an identity record, owner, purpose, and initial scope. | Limited design and validation activity only. |
| `validated` | Agent has passed required review, testing, policy checks, and risk classification. | May be approved for controlled activation. |
| `active` | Agent is approved for governed workflow participation. | Activity allowed only within approved scope and policy. |
| `restricted` | Agent remains active but with reduced scope due to risk, degraded confidence, or temporary conditions. | Only explicitly allowed low-risk activities. |
| `suspended` | Agent is temporarily blocked due to anomaly, policy issue, investigation, expired review, or operational hold. | No retrieval, tool use, delegation, or output release. |
| `deprecated` | Agent is approved for limited legacy use while replacement is being adopted. | Only pinned or exception-approved use. |
| `retired` | Agent is permanently removed from service. | No activity; records retained for audit. |
| `revoked` | Agent identity is invalidated due to compromise, rogue behavior, or emergency recall. | No activity; credentials and sessions terminated. |

Lifecycle state is a policy input. It must be checked before the agent can retrieve context, receive delegated work, request tool execution, produce customer-facing output, or participate in fleet rollout.

## Minimum Identity Requirements

Every governed agent must have an identity record containing at least:

| Field | Requirement |
|---|---|
| `agent_id` | Globally unique identifier for the agent. |
| `agent_name` | Human-readable name. |
| `owner_team` | Accountable team responsible for operation and review. |
| `business_owner` | Accountable service or business owner where applicable. |
| `technical_owner` | Engineering owner responsible for implementation and maintenance. |
| `business_purpose` | Approved reason the agent exists. |
| `service_model` | MSSP, MDR, SOC / IR, cloud IR, DFIR, private/local LLM-assisted DFIR, or other approved model. |
| `risk_tier` | Risk tier used for policy, monitoring, and review cadence. |
| `lifecycle_state` | Current governance state. |
| `current_version` | Active approved version or pinned version. |
| `approved_scope_profile` | Link to approved tenant, customer, case, data, tool, action, and output scope. |
| `monitoring_profile` | Expected behavior and alerting profile. |
| `review_frequency` | Required access and governance review cadence. |
| `emergency_contact` | Contact path for suspension, rollback, or recall. |
| `created_at` / `updated_at` | Record maintenance timestamps. |

A production implementation should also track workload identity, credential issuer, signing identity, package hash, model lineage, prompt version, tool-contract versions, policy bundle version, and audit correlation identifiers where applicable.

## Registration Flow

A new agent should follow this governance flow before activation:

1. **Purpose submission** — define the use case, service model, data boundaries, expected users, and business owner.
2. **Risk classification** — classify the agent by data access, tool access, customer impact, evidence sensitivity, privilege level, autonomy, and tenant scope.
3. **Scope definition** — define allowed tenants, customers, cases, data classes, evidence classes, tools, actions, environments, and output destinations.
4. **Owner assignment** — assign accountable business, service, and technical owners.
5. **Validation** — validate expected behavior, policy integration, monitoring, output boundaries, failure behavior, and audit record completeness.
6. **Approval** — record approval from required governance, service, security, and customer-authority paths where applicable.
7. **Activation** — set lifecycle state to `active` only after identity, scope, policy, monitoring, audit, and rollback controls are ready.

An agent should not move directly from proposed to active without registration, risk classification, validation, approval, and audit readiness.

## Identity and Credential Rules

Agent identity must be separate from human analyst identity.

Agent identity must not be shared across unrelated agents, customers, tenants, service towers, or environments unless explicitly designed as a governed fleet identity with tenant-safe scope boundaries.

Agent credentials should be:

- issued through an approved identity or secrets broker;
- scoped to approved tools and environments;
- short-lived where practical;
- rotated on defined cadence;
- revoked immediately on suspension, compromise, retirement, or emergency recall;
- unavailable to prompts, model output, user-provided content, or retrieved context;
- bound to audit records for every governed request.

Agents must not use personal accounts, shared analyst credentials, static unmanaged secrets, or credentials copied into prompts, memory, case notes, tickets, or unstructured configuration.

## Lifecycle Transitions

| Transition | Required Controls |
|---|---|
| `proposed` → `registered` | Owner assigned, purpose documented, risk triage completed. |
| `registered` → `validated` | Scope profile, tests, policy checks, monitoring profile, and audit requirements reviewed. |
| `validated` → `active` | Approval recorded, version pinned, rollback path defined, lifecycle state changed by authorized owner. |
| `active` → `restricted` | Risk or incident reason recorded; scope reduction enforced by policy. |
| `active` → `suspended` | Trigger recorded; credentials and tool access blocked; owners notified. |
| `suspended` → `active` | Root cause reviewed; required remediation validated; approval recorded. |
| `active` → `deprecated` | Replacement plan documented; allowed legacy usage pinned and monitored. |
| `deprecated` → `retired` | Access removed; credentials revoked; audit records retained. |
| Any state → `revoked` | Emergency recall or compromise response; all sessions, credentials, and fleet distribution blocked. |

Lifecycle transitions must be auditable. Changes to lifecycle state must not be performed by the agent whose state is changing.

## Access Review

Access reviews should evaluate whether:

- the agent still has a valid business purpose;
- the owner and emergency contacts are current;
- approved tenants, customers, cases, environments, tools, and actions remain necessary;
- any policy exceptions remain justified;
- monitoring findings indicate scope reduction or retirement;
- the current version remains approved;
- outstanding audit, incident, or assurance findings have been remediated.

Review cadence should increase with risk tier, sensitive data access, state-changing tool access, evidence impact, customer-facing output, cross-tenant fleet distribution, or history of policy exceptions.

## Suspension and Revocation Triggers

An agent should be suspended or revoked when any of the following occur:

- unregistered or duplicate identity is detected;
- owner is missing or no longer accountable;
- access review expires;
- current version is blocked, recalled, or no longer approved;
- policy bypass attempt is detected;
- cross-tenant, cross-customer, or cross-case activity is attempted;
- unexpected tool use or privilege escalation is observed;
- evidence handling boundary is violated;
- unsupported claims repeatedly affect customer-facing output;
- credential compromise is suspected;
- audit logging is incomplete for governed actions;
- emergency recall is issued for a fleet version.

Suspension should block retrieval, tool use, workflow delegation, and output release until reviewed.

Revocation should terminate active sessions, invalidate credentials, block future scheduling, prevent fleet distribution, and preserve records for investigation.

## Audit Requirements

Identity lifecycle events must produce audit records that include:

- agent identity;
- previous and new lifecycle state;
- owner and approver identity;
- reason for change;
- scope profile affected;
- version affected;
- policy or change record reference;
- time of change;
- emergency or normal workflow flag;
- downstream credential, session, and tool-access changes;
- rollback or reinstatement decision where applicable.

Audit records must support reconstruction of when an agent became active, what it was allowed to do, which version was active, who approved it, why it was suspended or retired, and whether credentials were revoked.

## Fail-Closed Conditions

The workflow must fail closed or route to authorized review when:

- agent identity cannot be verified;
- lifecycle state is missing or not active for the requested workflow;
- owner is missing;
- scope profile is missing or stale;
- access review has expired;
- current version is not approved;
- required monitoring profile is missing;
- policy cannot evaluate lifecycle state;
- audit logging cannot record the identity decision.

## Acceptance Criteria

Agent identity lifecycle governance is acceptable when:

- every active agent has a unique governed identity;
- every active agent has a current owner, purpose, risk tier, scope profile, version, and monitoring profile;
- lifecycle state is enforced before retrieval, delegation, tool use, and output release;
- suspended, retired, revoked, or unregistered agents cannot operate;
- lifecycle changes are performed by authorized humans or governance workflows, not by the agent itself;
- audit records can reconstruct lifecycle state over time;
- emergency suspension and revocation paths are tested.

## Summary

The agent identity lifecycle turns agents into accountable, reviewable, revocable participants in security operations.

> No identity, no owner, no active lifecycle state, no governed participation.
