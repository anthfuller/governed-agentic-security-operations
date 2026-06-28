# Agentic Fleet Architecture

## Purpose

This document defines the architecture view for operating a governed fleet of security agents across MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

The focus is fleet-level control: how agent identities, versions, tool access, policy gates, tenant eligibility, rollout, monitoring, rollback, and audit work together when agentic capabilities are deployed across multiple customers, tenants, environments, and service towers.

This is an architecture document, not deployment code or a product implementation guide.

![Agentic Fleet Architecture](diagrams/agentic-fleet-architecture.png)

## Scope

Agentic fleet governance applies to any reusable or centrally managed agent capability that may operate across more than one case, tenant, customer, service tower, or environment.

Examples include:

| Agent Type | Typical Role |
|---|---|
| SOC analyst agent | Alert triage, evidence summary, investigation notes, prioritization support |
| Incident enrichment agent | Asset, identity, threat intelligence, and cloud-context enrichment |
| Threat hunting agent | Hypothesis generation, query drafting, hunt result summarization |
| Phishing and email investigation agent | Message analysis, header review, sender reputation, user-impact summary |
| Response recommendation agent | Response-option drafting with policy, evidence, and approval constraints |
| Customer reporting agent | Drafting customer-facing incident summaries and service reports |
| Forensic case assistant agent | Timeline support, artifact parsing assistance, evidence-reference organization |
| Custom MSSP or MDR agent | Provider-specific workflows, playbooks, service-tier logic, and reporting patterns |

A fleet may include agent runtime definitions, prompts, tool contracts, model references, retrieval configuration, memory boundaries, policy bundles, approval requirements, monitoring profiles, and rollout metadata.

## Architecture Position

The fleet architecture is a cross-cutting view of the broader Agentic MSSP / MDR / DFIR security operations architecture.

```text
Customer and security data sources
        ↓
Ingestion, normalization, enrichment, and context assembly
        ↓
Agentic SOC / orchestration layer
        ↓
AI assurance and analytics checks
        ↓
Governance / control plane policy decision
        ↓
Human oversight where required
        ↓
Policy-enforced tool execution or customer-facing output
        ↓
Audit, replay, monitoring, and service outcomes

Cross-cutting control plane:
Agent identity, lifecycle, fleet governance, versioning, rollout, recall, and visibility
```

The fleet control plane does not replace the runtime governance path. It governs which agents exist, which versions are eligible to run, which tenants may receive them, which tools they may request, and how unsafe versions are stopped or rolled back.

## Core Architecture Principles

1. Every agent must have a managed identity, owner, version, purpose, and authorized scope.
2. Agent output is not authorization. Tool execution must be policy-gated.
3. Fleet rollout must be scoped, staged, observable, and reversible.
4. Tenant and customer boundaries must be enforced before context retrieval, reasoning, tool use, memory use, reporting, or intelligence propagation.
5. Shared intelligence must be sanitized and approved before reuse across customers or tenants.
6. Sensitive actions require the approval path defined by policy, not by agent confidence.
7. Evidence-derived summaries must preserve references to source evidence.
8. Unsupported claims, missing evidence, missing approval, missing tenant scope, missing audit, or missing rollback path must block governed workflow execution.

## Fleet Control-Plane Responsibilities

| Control Area | Responsibility |
|---|---|
| Agent registry | Records agent identity, owner, purpose, version, service tower, risk tier, and lifecycle state |
| Identity and access | Binds agents to managed identities, scoped credentials, allowed tenants, allowed tools, and allowed actions |
| Version management | Tracks signed agent packages, prompt versions, model references, policy bundles, tool contracts, and rollback targets |
| Tenant eligibility | Determines which customers, tenants, environments, and service tiers may receive a specific version or capability |
| Policy enforcement | Uses PDP/PEP controls to allow, deny, escalate, or fail closed before tool execution or sensitive output release |
| Human oversight | Routes sensitive decisions to analyst review, formal approval, customer approval, or escalation as required |
| AI assurance | Evaluates output quality, evidence support, unsupported claims, tenant-boundary risk, and HITL requirements |
| Tool governance | Restricts agents to registered tools, scoped inputs, approved credentials, and auditable execution paths |
| Monitoring | Tracks fleet behavior, version adoption, anomalies, policy denials, failed checks, and customer-impacting exceptions |
| Rollback and recall | Stops unsafe versions, pins known-good versions, revokes access, preserves audit evidence, and supports investigation |
| Audit and replay | Records decisions, approvals, context references, versions, evidence references, tool actions, and final outcomes |

## Control Stack Mapping

The fleet architecture uses layered controls so that no single agent, model, prompt, or workflow can bypass the operating model.

| Layer | Control Focus |
|---|---|
| Prompts | Approved task framing, instruction boundaries, and output-format expectations |
| Grounding / RAG | Tenant-scoped retrieval, source metadata, evidence references, and memory boundaries |
| Planner | Workflow planning within allowed case, customer, tenant, and action scope |
| Tools | Registered tools, tool contracts, scoped credentials, and mediated execution |
| Policy | PDP/PEP decisions, approval requirements, tenant eligibility, and risk classification |
| Sandbox | Restricted execution, containment, validation, and safe test environments |
| Monitoring | Runtime telemetry, behavior analytics, anomaly detection, audit replay, and recall triggers |

## Agent Package Model

A fleet-deployed agent should be represented as a versioned package. The package is the unit that can be reviewed, approved, distributed, monitored, rolled back, or recalled.

A package should identify:

- agent name and version;
- owner and accountable service team;
- supported service towers;
- intended task scope;
- allowed tenants, customers, or tenant groups;
- excluded tenants or customer groups;
- prompt package version;
- model or model-route reference;
- retrieval and memory configuration;
- tool-contract versions;
- policy bundle version;
- approval requirements;
- validation evidence;
- monitoring profile;
- rollout plan;
- rollback target;
- signature, checksum, or provenance record.

Example package manifest shape:

```json
{
  "agent_package_id": "mdr-incident-enrichment-agent@1.4.2",
  "agent_role": "incident_enrichment",
  "owner": "mdr-platform-engineering",
  "service_towers": ["managed-soc", "mdr"],
  "risk_tier": "medium",
  "prompt_package": "incident-enrichment-prompts@3.1.0",
  "model_route": "approved-security-operations-model-route",
  "policy_bundle": "mdr-agent-policy@2.7.0",
  "tool_contracts": [
    "siem-readonly-query@1.8.0",
    "identity-risk-lookup@1.2.0",
    "case-note-draft@1.5.0"
  ],
  "retrieval_scope": "tenant_case_bound",
  "memory_scope": "tenant_case_bound_no_cross_customer_memory",
  "eligible_tenant_groups": ["standard-mdr", "premium-mdr"],
  "excluded_tenants": ["regulated-customer-example"],
  "approval_profile": "human_review_for_customer_visible_output",
  "monitoring_profile": "mdr-agent-fleet-medium-risk",
  "rollout_strategy": "canary_then_cohort",
  "rollback_target": "mdr-incident-enrichment-agent@1.4.1"
}
```

The manifest is an architecture record shape. Production implementations should validate it through controlled schemas, release workflows, and audit systems.

## Fleet Runtime Flow

A governed fleet runtime should follow a consistent control path.

```text
1. Agent invocation request is created.
2. Agent identity, version, tenant, customer, case, and requested task are resolved.
3. Tenant eligibility and lifecycle state are checked.
4. Context is assembled from approved, tenant-scoped, evidence-linked sources.
5. Agent performs the approved task and produces structured output.
6. AI assurance evaluates output quality, evidence support, unsupported claims, tenant-boundary risk, and HITL requirements.
7. PDP evaluates the requested action or output release.
8. PEP enforces allow, deny, require-approval, or fail-closed decision.
9. Human or customer approval is obtained when required.
10. Approved tool execution or output release occurs through mediated channels.
11. Audit records capture context references, decisions, approvals, actions, versions, and outcomes.
12. Fleet monitoring evaluates behavior, failures, drift, and recall triggers.
```

## Fleet Update Lifecycle

Fleet updates must be controlled as operational changes because a single bad update can affect many tenants or cases.

| Stage | Required Control |
|---|---|
| Change request | Identify purpose, owner, affected agents, affected tenants, risk tier, and expected behavior |
| Package assembly | Bind prompts, model route, tool contracts, policy bundle, retrieval scope, and monitoring profile |
| Risk classification | Classify impact to tenants, tools, evidence, customer-facing output, and response actions |
| Validation | Test policy behavior, tool boundaries, tenant isolation, output quality, evidence references, rollback, and monitoring |
| Approval | Obtain required engineering, service-owner, policy-owner, security, and customer approval where applicable |
| Tenant eligibility | Confirm allowed tenants, excluded tenants, service tiers, data residency, and contractual constraints |
| Canary | Deploy to limited internal or controlled tenant scope |
| Cohort rollout | Expand only when monitoring gates pass |
| Monitoring | Watch denials, fail-closed events, unsupported claims, tool errors, boundary violations, and customer impact |
| Rollback or recall | Stop distribution, pin known-good versions, revoke access, preserve audit evidence, and notify owners |
| Closeout | Record final state, exceptions, approval evidence, and lessons learned |

## Policy Gate Examples

| Request | Baseline Decision Pattern |
|---|---|
| Read-only SIEM query within authorized tenant and case | Allow if identity, tenant, case, and tool scope are valid |
| Draft investigation summary for analyst review | Allow with evidence references and unsupported-claim checks |
| Customer-facing incident report | Require human review and applicable customer approval path |
| Endpoint isolation, account disablement, firewall block, or containment action | Require formal approval and policy-enforced tool execution |
| DFIR timeline conclusion based on evidence artifacts | Require evidence references and forensic review |
| Cross-tenant sanitized intelligence release | Require sanitization review, release approval, and tenant eligibility |
| Retrieval from another customer, tenant, case, or evidence store | Deny or fail closed |
| Tool request without valid scope, policy, approval, or audit path | Deny or fail closed |

## Tenant and Customer Boundary Requirements

Fleet operation must preserve customer and tenant isolation at every control point.

Minimum requirements:

- agent identity must be authorized for the tenant and customer;
- context retrieval must be tenant-scoped and case-scoped;
- memory must not mix customer, tenant, case, or evidence boundaries;
- tool calls must carry tenant, customer, case, action, and approval context;
- customer-specific service obligations must be evaluated before output release or response action;
- shared detections, playbooks, prompts, or intelligence must be sanitized before reuse;
- tenant exclusions and regulated-customer restrictions must override broad rollout rules;
- audit records must identify which tenant, customer, case, agent version, and policy decision were involved.

## Sanitized Intelligence Propagation

Fleet-level learning may improve operations across customers, but raw customer data must not become shared fleet memory or shared prompt content.

Allowed examples after review:

- generic detection logic improvements;
- de-identified indicators or behavior patterns;
- generalized playbook refinements;
- improved investigation checklists;
- sanitized tool-use lessons;
- generalized model or prompt safety improvements.

Prohibited without explicit authorization:

- raw logs, alerts, evidence, or forensic artifacts;
- customer names, tenant IDs, account IDs, hostnames, user names, secrets, tokens, or private identifiers;
- customer-specific incident narratives;
- case notes copied into shared memory;
- contractual, legal, regulatory, or privileged information;
- unreviewed agent conclusions from a single customer case.

Sanitized intelligence release should record source classification, sanitization method, reviewer, release approval, destination scope, retention label, and rollback or removal path.

## Human Oversight Points

Human oversight is required where policy, customer obligation, evidence sensitivity, or operational impact requires accountable review.

Common oversight points:

- escalation from triage to incident response;
- customer-facing report release;
- containment or remediation recommendation approval;
- endpoint isolation or account disablement;
- firewall, IAM, SaaS, or cloud-control-plane changes;
- DFIR finding validation;
- evidence-handling decisions;
- sanitized intelligence release;
- fleet package approval;
- emergency recall or exception handling.

Human review and formal approval are separate controls. Review may assess quality or completeness. Approval authorizes a governed decision within a defined scope.

## Monitoring and Detection

Fleet monitoring should cover individual agent behavior and aggregate fleet behavior.

Required monitoring signals include:

| Signal | Purpose |
|---|---|
| Active versions by tenant | Detect version drift and unauthorized rollout |
| Invocation volume by agent and tenant | Detect abnormal usage or runaway automation |
| Policy denials and fail-closed events | Identify blocked unsafe behavior and policy mismatches |
| Tool-call requests and outcomes | Monitor attempted actions, errors, retries, and high-impact requests |
| Evidence-support failures | Detect unsupported or weakly supported outputs |
| Unsupported-claim rate | Detect hallucination-like or ungrounded conclusions |
| Tenant-boundary check failures | Detect attempted cross-tenant or cross-case access |
| Approval queue metrics | Detect workflow bottlenecks and approval bypass attempts |
| Customer-impacting exceptions | Prioritize service-impacting defects |
| Recall and rollback activity | Track emergency response and version containment |

Monitoring must support investigation of who invoked what, under which agent version, against which tenant and case, using which context, resulting in which policy decision and action.

## Rollback and Emergency Recall

Fleet architecture must include a tested path to stop unsafe versions.

Recall triggers may include:

- compromised agent identity;
- unauthorized tool request pattern;
- cross-tenant data exposure risk;
- prompt or retrieval contamination;
- defective policy bundle;
- unsafe response recommendation pattern;
- customer-impacting reporting defect;
- evidence-handling defect;
- monitoring or audit failure;
- unauthorized version distribution.

Emergency recall actions should include:

1. block new invocations of the affected agent version;
2. terminate or quarantine active sessions where appropriate;
3. revoke or rotate affected credentials;
4. pin eligible tenants to a known-good version;
5. identify affected tenants, cases, outputs, and tool actions;
6. preserve audit evidence;
7. notify fleet owners, service owners, and affected operational teams;
8. open corrective change management;
9. prevent redeployment until validation and approvals are complete.

## Service Tower Application

| Service Tower | Fleet Architecture Use |
|---|---|
| Managed SOC / MSSP | Repeatable alert triage, enrichment, reporting, escalation support, and customer-specific service boundaries |
| MDR | Investigation support, containment recommendation drafting, threat hunting, response guidance, and analyst review workflows |
| Cloud Incident Response | Identity, IAM, workload, control-plane, and cloud-log analysis with policy-gated response recommendations |
| Private / Local LLM DFIR | Sensitive evidence analysis, timeline assistance, artifact parsing support, chain-of-custody-aware review, and forensic validation |
| LLM Forensic Teams | Local IR, malware or memory-analysis support, identity compromise investigations, and legal or sovereignty-sensitive workflows |

## Required Architecture Records

| Record | Purpose |
|---|---|
| Agent card | Identifies agent owner, purpose, scope, lifecycle state, tools, risks, and review requirements |
| Tool contract | Defines allowed tool inputs, actions, credentials, policy requirements, and audit fields |
| Policy decision record | Captures allow, deny, require-approval, or fail-closed decision with reasons |
| Human approval record | Captures accountable approval for sensitive actions or releases |
| Customer approval record | Captures customer-specific authorization where required |
| Evidence manifest | Links outputs and conclusions to source evidence references |
| Fleet update request | Defines proposed fleet change, affected versions, scope, risk, and rollout plan |
| Fleet rollout audit event | Records staged rollout, gate outcomes, exceptions, rollback, and final state |
| Recall record | Captures emergency recall trigger, affected scope, containment actions, and recovery state |

## Fail-Closed Conditions

Fleet operations should deny, halt, or fail closed when any required control is missing or invalid.

Examples:

- agent identity is unknown, expired, suspended, or unregistered;
- agent version is unsigned, unapproved, recalled, or not eligible for the tenant;
- tenant, customer, case, or evidence scope is missing or ambiguous;
- retrieval would cross tenant, customer, case, retention, or sovereignty boundaries;
- requested tool is not registered or not allowed for the agent;
- policy decision cannot be reached;
- required approval is missing or stale;
- output lacks required evidence references;
- audit logging is unavailable;
- monitoring profile is inactive for a rollout;
- rollback target is missing;
- package contains unapproved customer-specific data.

## Public-Facing Product Position

Vendor product names in diagrams are capability placement examples, not requirements, endorsements, or claims that a specific product provides every control described here.

The required architecture capabilities are:

- managed agent identity;
- lifecycle governance;
- policy enforcement;
- scoped authorization;
- human approval workflow;
- tenant and evidence isolation;
- tool mediation;
- monitoring and anomaly detection;
- audit and replay;
- rollback and recall.

Organizations can implement these capabilities with the platforms, identity systems, SIEM/XDR tools, SOAR systems, policy engines, evidence systems, and approval workflows appropriate to their environment.

## Acceptance Criteria

An agentic fleet architecture is acceptable when it can demonstrate the following:

- every active agent has a registered identity, owner, version, lifecycle state, and approved scope;
- every deployed package has provenance, policy binding, tool-contract binding, monitoring profile, and rollback target;
- tenant eligibility is evaluated before rollout;
- sensitive actions are policy-gated and approval-controlled;
- customer-facing outputs are evidence-backed and reviewable;
- cross-tenant intelligence propagation uses sanitization and release controls;
- policy, approval, context, tool execution, and audit records can be replayed;
- unsafe versions can be halted, rolled back, or recalled;
- monitoring can detect abnormal behavior, boundary violations, unsupported claims, and customer-impacting failures.

## Related Repository Areas

- [`agent-governance/`](../agent-governance/readme.md) for agent identity, lifecycle, access scope, communication, monitoring, fleet governance, and rollback.
- [`policy-enforcement/`](../policy-enforcement/readme.md) for PDP/PEP behavior, risk classification, approval policy, and fail-closed decisions.
- [`human-oversight/`](../human-oversight/readme.md) for human review, approval boundaries, customer approval, and escalation.
- [`tenant-isolation/`](../tenant-isolation/readme.md) for tenant scope validation and cross-tenant failure modes.
- [`tool-access/`](../tool-access/readme.md) for tool registration, scoped execution, and tool audit.
- [`evidence-traceability/`](../evidence-traceability/readme.md) for evidence references, finding support, and DFIR evidence handling.
- [`audit-replay/`](../audit-replay/readme.md) for audit events, replayability, correlation, failure audit, and immutable audit guidance.
