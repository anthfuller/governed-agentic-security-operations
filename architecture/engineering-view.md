# Engineering View

## Document Purpose

This document defines the engineering view of the **Governed Agentic Security Operations Architecture**.

It translates the reference architecture into technical control boundaries, data flows, interfaces, decision points, failure behavior, and implementation-oriented requirements for enterprise security operations.

This document is intended for security architects, SOC platform engineers, cloud security engineers, identity teams, AI engineers, detection engineers, DFIR practitioners, and platform owners responsible for designing or evaluating governed Agentic SOC, MSSP, MDR, Cloud Incident Response, or DFIR capabilities.

This is not a production deployment guide. It does not define a single vendor implementation, customer design, or compliance-certified architecture.

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

This file defines the engineering view of the reference architecture. Detailed control contracts, schemas, and implementation-specific requirements belong in the deeper policy-enforcement, human-oversight, AI-assurance, tenant-boundary, evidence, and governance documents.

---

## Engineering Architecture Diagram

![Agentic MSSP, MDR, and DFIR security operations architecture — engineering view](diagrams/engineering-architecture.png)

The diagram is a conceptual engineering view. It organizes responsibilities and trust boundaries; it does not represent a deployed production environment or claim that every depicted capability is implemented by this repository.

---

## Repository and Production Boundary

This repository is an independent personal reference architecture and adoption kit. Its `gaso` CLI performs deterministic offline validation of local artifacts and does not invoke agents or models, contact security platforms, or execute external actions.

The runtime components in this document describe responsibilities that adopters would need to implement, integrate, operate, and validate in their own environments. Production identity, authorization, policy enforcement, approval authority, tenant isolation, tool mediation, sandboxing, evidence preservation, audit storage, deployment, and response execution remain external implementation responsibilities. Passing repository validation does not establish production enforcement, security, compliance, factual correctness, evidentiary validity, or operational safety.

Microsoft products are shown only where they provide relevant candidate capabilities. The architecture does not imply that Microsoft Agent 365, Microsoft Entra Agent ID, or any other product supplies every depicted control or replaces an organization's policy, approval, isolation, audit, and operational responsibilities.

---

## Engineering Objective

The engineering objective is to support AI-assisted security operations without allowing agents to become uncontrolled automation.

The architecture must ensure that every agentic workflow is:

- identity-bound
- tenant-scoped
- data-minimized
- policy-mediated
- tool-constrained
- human-overseen where required
- evidence-backed
- auditable
- fail-closed
- service-aligned

The core engineering position is:

> Agents can assist with analysis and recommendations. They MUST NOT directly own policy decisions, sensitive approvals, or unrestricted tool execution.

---

## Engineering Control Model

The engineering model separates the runtime into distinct control responsibilities.

```text
Telemetry / Evidence
        ↓
Ingestion and normalization
        ↓
Approved context assembly
        ↓
Agent analysis
        ↓
Agent Judge / AI assurance evaluation
        ↓
PEP/PDP policy decision
        ↓
Human approval when required
        ↓
Mediated tool execution
        ↓
Audit, traceability, and service reporting
```

No single component MUST combine all of these functions without separation of duties, policy mediation, auditability, and governance.

---

## Layered Engineering Model

```text
+----------------------------------------------------------------------------------+
| Business / Operational Outcomes                                                   |
+----------------------------------------------------------------------------------+
| Service Delivery Towers                                                           |
+----------------------------------------------------------------------------------+
| Governance / Control Plane                                                        |
+----------------------------------------------------------------------------------+
| AI Assurance / Evaluation / Analytics Layer                                       |
+----------------------------------------------------------------------------------+
| Agentic SOC / Orchestration Layer                                                 |
+----------------------------------------------------------------------------------+
| Ingestion / Normalization / Integration Layer                                     |
+----------------------------------------------------------------------------------+
| Customer / Data Source Layer                                                      |
+----------------------------------------------------------------------------------+

Side control plane across the architecture:
+----------------------------------------------------------------------------------+
| Agent Governance & Identity Control Plane                                         |
+----------------------------------------------------------------------------------+
```

The Agent Governance & Identity Control Plane is not a downstream runtime layer. It governs agent identity, registration, lifecycle, ownership, visibility, access boundaries, and review obligations across the architecture.

---

## Engineering Domain Responsibilities

| Domain | Engineering Responsibility |
|---|---|
| Data Source | Provide telemetry, evidence, and source metadata |
| Ingestion | Normalize, enrich, classify, and route data |
| Data Services and Storage | Preserve tenant-scoped case data, knowledge, and immutable evidence references |
| Context Assembly | Build tenant-scoped, evidence-linked context for agents |
| Agent Runtime | Analyze approved context and produce structured outputs |
| AI Assurance | Evaluate output quality, evidence support, and risk |
| Policy Enforcement | Decide allow, deny, or require human approval |
| Human Oversight | Approve sensitive actions and final accountability points |
| Tool Gateway | Execute authorized actions only |
| Audit and Traceability | Record replayable evidence, decisions, approvals, and outcomes |
| Agent Governance | Govern agent identity, lifecycle, ownership, and visibility |
| Fleet Governance | Govern package versioning, tenant eligibility, rollout, monitoring, rollback, recall, and release audit |

---

## Layer 1: Customer / Data Source Layer

### Purpose

This layer provides raw telemetry, alerts, incidents, case data, and forensic artifacts.

### Representative Data Sources

- Microsoft Sentinel incidents, alerts, and logs
- Defender XDR incidents and evidence
- Defender for Endpoint telemetry
- Defender for Identity signals
- Defender for Cloud recommendations and alerts
- Entra ID sign-in, audit, and identity-risk data
- M365 audit and email telemetry
- AWS GuardDuty, CloudTrail, VPC Flow Logs, and IAM events
- GCP Security Command Center and Cloud Audit Logs
- EDR, NDR, firewall, DNS, proxy, and email security sources
- SaaS logs and business application telemetry
- Ticketing and case management systems
- DFIR evidence stores, disk images, memory captures, packet captures, and timelines

### Required Metadata

Every event, artifact, or case object MUST preserve sufficient metadata when it influences investigation, DFIR conclusions, customer-facing outputs, escalation, containment recommendations, policy decisions, governed tool execution, or audit reconstruction. Baseline metadata SHOULD include:

| Metadata Field | Purpose |
|---|---|
| `source_system` | Identifies the originating platform |
| `tenant_id` | Defines customer or tenant boundary |
| `customer_id` | Maps to service delivery ownership |
| `case_id` | Associates data with an investigation |
| `source_timestamp` | Original event time |
| `ingestion_timestamp` | Platform ingestion time |
| `data_classification` | Sensitivity and handling requirement |
| `evidence_ref` | Stable evidence reference |
| `collection_method` | How the data was obtained |
| `retention_policy` | Retention or deletion requirement |

### Engineering Controls

- Enforce tenant tagging at ingestion.
- Preserve source references before normalization.
- Separate raw evidence from derived summaries.
- Prevent raw customer data from entering shared agent memory.
- Treat log content and ticket content as untrusted input.
- Apply data minimization before agent context assembly.

---

## Layer 2: Ingestion / Normalization / Integration Layer

### Purpose

This layer converts raw data into controlled, normalized, enriched, and agent-consumable context.

### Engineering Functions

- connector management
- event ingestion
- schema validation
- normalization
- enrichment
- case correlation
- tenant filtering
- evidence reference preservation
- tenant-scoped case data, knowledge, vector, and immutable evidence storage
- prompt-injection labeling or filtering
- routing to approved workflows
- retrieval boundary enforcement

### Normalized Event Pattern

A normalized event should include at minimum:

```json
{
  "event_id": "evt-001",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "source_system": "siem",
  "event_type": "suspicious_sign_in",
  "source_timestamp": "2026-05-22T10:15:00Z",
  "ingestion_timestamp": "2026-05-22T10:16:12Z",
  "entity_refs": ["user-123", "ip-203.0.113.10"],
  "data_classification": "customer-security-telemetry",
  "evidence_ref": "evidence://customer-a/inc-10422/events/evt-001"
}
```

### Context Assembly Requirements

Before data is sent to an agent, the platform MUST validate applicable context assembly requirements:

1. Tenant scope is present.
2. Case scope is present.
3. Agent is authorized for the tenant.
4. Agent is authorized for the data class.
5. Data is relevant to the task.
6. Sensitive data is masked or excluded where required.
7. Evidence references are preserved.
8. Untrusted content is labeled.
9. Retrieval is limited to approved sources.
10. The context package is logged.

### Engineering Risks

| Risk | Control Requirement |
|---|---|
| Prompt injection through logs | Label, filter, constrain, and review untrusted content |
| Cross-tenant retrieval | Tenant-scoped indexes and retrieval filters |
| Loss of evidence lineage | Preserve raw and normalized references |
| Overbroad context | Use data minimization and retrieval constraints |
| Unsafe external enrichment | Tag enrichment source and confidence |

---

## Layer 3: Agentic SOC / Orchestration Layer

### Purpose

This layer hosts agents and workflows that assist security operations.

### Agent Runtime Responsibilities

Agents may:

- summarize incidents
- correlate evidence
- enrich indicators
- draft investigation notes
- propose hypotheses
- identify missing evidence
- generate response recommendations
- draft customer-facing reports
- request approved tool actions

Agents MUST NOT:

- directly execute high-impact remediation
- approve their own recommendations
- bypass tenant filters
- access arbitrary tools
- retrieve arbitrary customer data
- suppress detections without approval
- issue final forensic conclusions
- modify or delete evidence

### Agent Output Contract

Agent outputs MUST be structured and reviewable when they influence investigation, DFIR conclusions, customer-facing outputs, escalation, containment recommendations, policy decisions, approval routing, or governed tool execution.

```json
{
  "agent_id": "soc-analyst-agent",
  "agent_role": "triage",
  "tenant_id": "customer-a",
  "case_id": "inc-10422",
  "summary": "Suspicious sign-in followed by mailbox rule creation.",
  "findings": [
    {
      "finding": "Mailbox rule was created after anomalous sign-in.",
      "evidence_refs": [
        "evidence://customer-a/inc-10422/events/evt-001",
        "evidence://customer-a/inc-10422/events/evt-002"
      ],
      "confidence": "medium"
    }
  ],
  "assumptions": [
    "The sign-in event and mailbox rule activity are associated with the same user account."
  ],
  "recommended_next_steps": [
    "Review user sign-in history.",
    "Check mailbox forwarding and rule configuration.",
    "Validate device and IP reputation."
  ],
  "sensitive_action_requested": false,
  "requires_human_review": true
}
```

### Agent Orchestration Controls

- Use task-specific agents instead of general unrestricted agents.
- Bind each agent to an approved role and tenant scope.
- Require structured output for downstream evaluation.
- Do not allow direct tool execution from free-form model output.
- Route tool requests through a policy enforcement point.
- Log prompts, context packages, model outputs, and tool requests where they influence governed decisions, evidence handling, customer-facing outputs, approvals, or tool execution.

---

## Layer 4: AI Assurance / Evaluation / Analytics Layer

### Purpose

This layer evaluates agent output before it is trusted, escalated, reported, or used to support action.

### Agent Judge Responsibilities

Agent Judges may evaluate:

- whether claims are supported by evidence
- whether evidence references exist
- whether confidence is justified
- whether tenant boundaries are preserved
- whether human approval is required
- whether customer-facing language is appropriate
- whether ATT&CK or ATLAS mapping is reasonable
- whether the recommendation contains sensitive action risk
- whether more evidence is required

### Judge Output Contract

```json
{
  "judge_id": "evidence-support-judge",
  "tenant_id": "customer-a",
  "case_id": "inc-10422",
  "agent_output_id": "out-0091",
  "evaluation_result": "requires_review",
  "evidence_supported": true,
  "unsupported_claims": [],
  "tenant_boundary_risk": false,
  "sensitive_action_detected": true,
  "hitl_required": true,
  "recommended_disposition": "require_approval_review",
  "rationale": "The recommendation involves containment and should be reviewed before execution."
}
```

### Assurance Boundaries

Agent Judges are not enforcement components.

Correct relationship:

```text
Agent Judge evaluates risk and evidence.
PEP/PDP enforces policy.
Human approves sensitive actions.
Tool executes only after authorization.
```

### Engineering Risks

| Risk | Control Requirement |
|---|---|
| Judge treated as authority | Make judge output advisory and policy-consumable, not final |
| Unsupported findings | Require evidence references |
| Weak customer report | Route customer-facing content through review |
| Same-model reinforcement | Consider independent model or rules-based checks for critical flows |
| Missing uncertainty | Require confidence and assumptions |

---

## Layer 5: Governance / Control Plane

### Purpose

This layer enforces runtime policy, approval, access control, and audit requirements.

### Core Components

- PEP
- PDP
- policy engine
- action classifier
- approval workflow
- scoped credentials
- sandbox or scoped execution environment
- tool gateway
- audit logger
- replay and traceability store

### Policy Request Contract

```json
{
  "request_id": "req-10422-01",
  "tenant_id": "customer-a",
  "case_id": "inc-10422",
  "agent_id": "response-recommendation-agent",
  "agent_role": "response_recommendation",
  "agent_lifecycle_state": "active",
  "requested_tool": "endpoint-isolation-tool",
  "requested_operation": "isolate_endpoint",
  "target_entity": "device-123",
  "action_risk": "high",
  "evidence_refs": [
    "evidence://customer-a/inc-10422/events/evt-001",
    "evidence://customer-a/inc-10422/events/evt-004"
  ],
  "judge_result": {
    "evidence_supported": true,
    "hitl_required": true
  }
}
```

### Policy Decision Contract

```json
{
  "request_id": "req-10422-01",
  "decision": "REQUIRE_APPROVAL",
  "reason": "Endpoint isolation is a high-impact containment action.",
  "required_approver_role": "incident_commander_or_customer_authorized_approver",
  "expires_at": "2026-05-22T12:30:00Z",
  "audit_required": true
}
```

### Decision Outcomes

Policy decisions MUST remain aligned to the governed decision contract.

| Decision | Meaning |
|---|---|
| `ALLOW` | Request is authorized and may proceed |
| `DENY` | Request is not authorized and must stop |
| `REQUIRE_APPROVAL` | Request requires authorized approval before execution |

`REQUIRE_MORE_EVIDENCE`, `ESCALATE`, `FAIL_CLOSED`, and exception handling may be implemented as workflow states, policy reasons, or routing outcomes. They MUST NOT be treated as additional PDP decision outcomes unless the governed decision contract is formally revised.

### Sensitive Action Defaults

| Action | Default Decision |
|---|---|
| Summarize incident | `ALLOW` if tenant and data scope are valid |
| Enrich indicator | `ALLOW` if tool and tenant scope are valid |
| Create internal case note | `ALLOW` or `REQUIRE_APPROVAL` based on policy |
| Draft customer report | `REQUIRE_APPROVAL` before customer-facing release |
| Isolate endpoint | `REQUIRE_APPROVAL` |
| Disable user | `REQUIRE_APPROVAL` |
| Revoke token | `REQUIRE_APPROVAL` |
| Suppress detection | `REQUIRE_APPROVAL` |
| Delete or modify evidence | `DENY` unless explicitly authorized by approved process |

### Fail-Closed Conditions

The system MUST deny, stop execution, fail closed, or route to authorized review when:

- tenant ID is missing
- agent identity is missing
- agent lifecycle state is not active
- requested tool is not registered
- requested operation is outside tool contract
- policy engine is unavailable
- required approval is missing
- evidence reference is missing for sensitive action
- cross-tenant access is detected
- schema validation fails
- audit logging is unavailable for a sensitive action

---

## Layer 6: Agent Governance & Identity Control Plane

### Purpose

This layer governs agents as enterprise identities and managed workloads.

### Capabilities

- agent registration
- agent ownership
- agent lifecycle management
- agent identity
- authentication
- authorization
- access reviews
- visibility and monitoring
- rogue or shadow agent detection
- policy assignment
- retirement and disablement

### Agent Registry Record

```json
{
  "agent_id": "soc-analyst-agent",
  "agent_name": "SOC Analyst Agent",
  "owner": "SOC Engineering",
  "business_purpose": "Assist with incident triage and enrichment",
  "approved_tenants": ["customer-a", "customer-b"],
  "allowed_data_classes": ["security-telemetry", "case-notes"],
  "allowed_tools": ["siem-query-tool", "threat-intel-lookup-tool"],
  "prohibited_actions": ["endpoint_isolation", "user_disablement"],
  "risk_tier": "medium",
  "lifecycle_state": "active",
  "review_frequency": "quarterly"
}
```

### Engineering Rules

- Agents MUST have unique identities.
- Agents MUST have named owners.
- Agents MUST have defined tenant scope.
- Agents MUST have defined tool scope.
- Agents MUST have defined action restrictions.
- Agent access MUST be reviewed.
- Inactive agents MUST NOT retrieve data or request tools.
- Rogue or unregistered agents MUST be detected and blocked.

### Product Placement Caution

Microsoft Agent 365 is represented for agent registry, lifecycle, policy, visibility, monitoring, and shadow-agent governance capabilities. Microsoft Entra Agent ID is represented for agent identity, authentication, authorization, ownership, access, federation, and trust capabilities.

They MUST NOT be represented as ordinary SOC investigation agents. Neither product is asserted to provide every control shown in the diagram, and neither replaces runtime PEP/PDP enforcement, human approval, tenant isolation, sandboxing, tool mediation, evidence controls, audit storage, or response execution.

### Fleet Governance and Cross-Tenant Propagation Boundary

Fleet updates are governed operational changes, not normal runtime agent actions.

Agent packages, prompts, retrieval configurations, policy bundles, tool contracts, detection packages, playbooks, report templates, and sanitized intelligence releases must have versioning, ownership, validation evidence, tenant eligibility checks, rollout scope, monitoring, rollback or recall support, and replayable audit records.

Runtime approval to use tenant-scoped context does not authorize cross-tenant reuse, shared-memory writes, package rollout, prompt updates, detection updates, or report-template distribution.

Cross-tenant propagation requires sanitization, human review, policy approval, destination-scope control, tenant eligibility checks, monitoring, audit, and rollback or recall support.

---

## Layer 7: Service Delivery Towers

### Purpose

Service towers define how the technical architecture supports operational services.

### Managed SOC / MSSP

Engineering requirements:

- customer tenant isolation
- standardized triage workflow
- customer-specific escalation paths
- case ownership tracking
- auditable reporting
- multi-tenant access controls

### MDR

Engineering requirements:

- endpoint evidence correlation
- containment recommendation workflow
- human approval for response actions
- response playbook mapping
- evidence-backed customer reporting

### Cloud Incident Response

Engineering requirements:

- cloud account/subscription/project scoping
- identity and control-plane evidence collection
- cloud audit log preservation
- blast-radius analysis
- approval before containment

### Private / Local LLM DFIR

Engineering requirements:

- controlled evidence store
- local/private model execution where required
- no unnecessary external data egress
- model, prompt, and case versioning
- analyst validation of outputs
- chain-of-custody support
- human-owned conclusions

### Detection Engineering

Engineering requirements:

- detection logic review
- tuning workflow approval
- ATT&CK mapping
- false-positive measurement
- no unsupervised detection suppression

### Threat Hunting

Engineering requirements:

- tenant-scoped queries
- reproducible hunt logic
- evidence-backed findings
- source and query audit trail

---

## End-to-End Engineering Sequence

### Agent-Assisted Investigation

```text
1. Alert is received from SIEM, XDR, cloud, endpoint, SaaS, or identity source.
2. Ingestion layer validates schema and assigns tenant context.
3. Event is normalized and enriched.
4. Evidence references are created or preserved.
5. Context assembly service builds an approved context package.
6. Agent receives only approved context.
7. Agent produces structured analysis and recommendations.
8. Agent Judge evaluates evidence support, unsupported claims, and risk.
9. PEP receives any requested tool action.
10. PDP returns `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`.
11. Human approval workflow is triggered when required.
12. Tool gateway executes only authorized actions.
13. Audit trail records all steps.
14. Case or report is updated.
```

### Sensitive Action Flow

```text
1. Agent recommends disabling a user account.
2. Recommendation includes supporting evidence references.
3. Agent Judge validates that evidence exists but marks action as sensitive.
4. PEP classifies action as high risk.
5. PDP returns `REQUIRE_APPROVAL`.
6. Authorized approver reviews recommendation and evidence.
7. If approved, identity tool executes the action through controlled interface.
8. Execution result is logged.
9. Customer or case record is updated.
```

### Local / Private LLM DFIR Flow

```text
1. Evidence is collected into an approved evidence store.
2. Evidence metadata is recorded.
3. Analyst selects approved artifacts for local/private model review.
4. Local/private model receives limited case context.
5. Model assists with summarization, timeline reconstruction, or artifact explanation.
6. Analyst validates output against source evidence.
7. Unsupported statements are removed or corrected.
8. Final report remains human-owned and evidence-backed.
9. Prompt, model, case, and output references are logged.
```

---

## Data and Context Isolation Requirements

### Tenant Isolation

Tenant ID MUST be present in:

- ingestion records
- normalized events
- evidence references
- context packages
- agent prompts
- agent outputs
- judge results
- policy requests
- tool requests
- audit records

If tenant ID is missing, ambiguous, mismatched, or cannot be validated, the workflow MUST fail closed, block execution, or route to authorized review.

### RAG and Knowledge Isolation

If retrieval or RAG is used:

- customer indexes MUST be isolated or tenant-filtered
- shared knowledge MUST be clearly separated from customer evidence
- retrieval queries MUST include tenant and case scope when customer evidence is queried
- retrieved customer evidence MUST include evidence references when it influences investigation, DFIR conclusions, customer-facing outputs, escalation, containment recommendations, policy decisions, governed tool execution, or audit reconstruction
- retrieved untrusted content MUST be labeled
- model memory MUST NOT be shared across customers without explicit controls

### Prompt Context Isolation

Prompt context MUST NOT mix customer data unless explicitly authorized by policy, tenant boundary controls, and customer handling requirements.

Prompt context SHOULD include:

- tenant ID
- case ID
- evidence references
- agent role
- task objective
- output format
- action restrictions
- data handling instruction

Prompt context MUST exclude:

- unrelated customer data
- secrets
- credentials
- unnecessary raw evidence
- unrestricted tool instructions
- untrusted content without labeling

---

## Tool Execution Requirements

### Tool Registry

Every tool available to agents MUST have a registry entry.

Minimum tool registry fields:

| Field | Purpose |
|---|---|
| `tool_name` | Unique tool identifier |
| `owner` | Responsible team |
| `allowed_operations` | Approved operations |
| `prohibited_operations` | Explicitly denied operations |
| `required_scopes` | Permissions required |
| `risk_category` | Low, medium, high |
| `approval_required` | Whether HITL is required |
| `input_schema` | Required input contract |
| `output_schema` | Required output contract |
| `audit_level` | Logging requirement |
| `tenant_restrictions` | Tenant execution boundary |

### Tool Call Pattern

Agents MUST request tool actions through mediated interfaces. They MUST NOT execute tools directly from free-form model output.

```text
Agent output
    ↓
Tool request
    ↓
Schema validation
    ↓
PEP/PDP decision
    ↓
Approval if required
    ↓
Tool execution
    ↓
Execution audit
```

### Tool Execution Token Requirements

After a tool request is authorized, the Tool Gateway MUST NOT pass broad credentials or rely only on the original agent request.

The Tool Gateway SHOULD exchange the approved `policy_decision` for a short-lived, cryptographically signed execution token. The execution token SHOULD be scoped to the approved action and SHOULD include, where applicable:

| Claim | Purpose |
|---|---|
| `tenant_id` | Tenant or customer boundary |
| `customer_id` | Customer service boundary |
| `case_id` | Incident or case boundary |
| `workflow_id` | Approved workflow context |
| `agent_id` | Requesting agent identity |
| `tool_id` | Authorized tool |
| `allowed_operations` | Explicit operations approved for execution |
| `target_entity` | Approved asset, identity, evidence object, or resource target |
| `policy_decision_id` | Policy decision authorizing the action |
| `approval_record_id` | Human approval reference when required |
| `audit_reference_id` | Audit chain reference |
| `correlation_id` | End-to-end trace identifier |
| `iat` | Token issue time |
| `nbf` | Not-before time |
| `exp` | Token expiration time |

Downstream tools and APIs MUST validate the execution token before action. Execution MUST fail closed if the token is missing, expired, reused outside scope, cryptographically invalid, mismatched to the request, missing required claims, or authorizes an operation outside the approved policy decision.

The execution token MUST NOT grant broader access than the PDP decision, approval record, tool contract, tenant scope, case scope, or customer authorization allow.

---

## Audit and Traceability Requirements

A governed workflow MUST be replayable.

Minimum audit fields:

| Field | Description |
|---|---|
| `correlation_id` | End-to-end trace ID |
| `tenant_id` | Customer or tenant boundary |
| `case_id` | Incident or case reference |
| `agent_id` | Agent identity |
| `agent_role` | Assigned role |
| `model_ref` | Model or runtime reference |
| `prompt_ref` | Prompt/template reference |
| `context_refs` | Evidence and retrieval references |
| `agent_output_ref` | Stored output reference |
| `judge_result_ref` | Assurance result |
| `policy_request_ref` | Policy request |
| `policy_decision` | `ALLOW`, `DENY`, or `REQUIRE_APPROVAL` |
| `approver` | Human approver if required |
| `tool_action` | Tool and operation |
| `execution_result` | Outcome |
| `timestamp` | Time of each event |

Audit logs MUST support reconstruction of governed decisions, approvals, tool execution, evidence handling, DFIR conclusions, customer-facing outputs, and operational response actions where applicable. Audit logs SHOULD support:

- incident review
- customer reporting
- internal quality review
- policy tuning
- model evaluation
- forensic reconstruction
- service assurance

---

## Engineering Non-Functional Requirements

| Requirement | Engineering Expectation |
|---|---|
| Security | Least privilege, scoped credentials, tenant isolation, mediated tools |
| Reliability | Fail-closed for missing identity, tenant, policy, approval, or audit path |
| Observability | End-to-end correlation IDs, decision logging, tool execution logs |
| Explainability | Evidence-linked outputs and documented policy decisions |
| Maintainability | Clear contracts for agents, judges, policies, and tools |
| Portability | Avoid hard dependency on one implementation pattern where possible |
| Governance | Agent ownership, lifecycle, access review, and auditability |
| Privacy | Data minimization, masking, and controlled evidence handling |
| Resilience | Workflow stops or escalates when controls fail |
| Performance / Latency | Deterministic controls such as schema validation, token validation, policy checks, and PEP enforcement SHOULD have defined latency budgets and remain materially faster than LLM inference. Remote PDP calls SHOULD define timeout, cache, retry, and fail-closed behavior. |
| Service Alignment | Service tower boundaries, escalation paths, and customer approvals |

---

## Implementation Planning Gates

Before implementing a proof of concept, confirm:

1. Target use case is narrow and defined.
2. Tenant boundary is explicit.
3. Data sources are approved.
4. Agent identity model exists.
5. Agent role and tool scope are defined.
6. Context assembly is tenant-scoped.
7. Agent output format is structured.
8. Agent Judge evaluation criteria are defined.
9. Policy decision contract is defined.
10. Human approval workflow is defined.
11. Audit schema is defined.
12. Failure behavior is fail-closed.
13. Customer-facing outputs require review.
14. Sensitive actions require approval.
15. Evidence references are preserved.
16. Fleet rollout, rollback, and recall process is defined where shared agent packages are used.
17. Sanitized intelligence release controls are defined where cross-tenant learning is used.

---

## Recommended First Build Slice

Do not implement the full architecture first.

The recommended first engineering slice is:

```text
Alert
    ↓
Tenant-scoped context package
    ↓
Agent analysis
    ↓
Agent Judge review
    ↓
PEP/PDP decision
    ↓
HITL approval if required
    ↓
Audited case update or controlled tool action
```

This slice validates the most important architecture principle:

> Agentic assistance can be useful only when it is surrounded by identity, policy, approval, audit, and evidence controls.

---

## Engineering Anti-Patterns

Avoid:

- agents using human analyst credentials directly
- unrestricted tool access
- cross-tenant shared memory
- policy embedded only in prompts
- customer reports generated without review
- detection suppression without approval
- direct endpoint containment by agent
- agent self-approval
- missing evidence references
- missing audit trail
- no agent owner
- no agent lifecycle state
- no fail-closed behavior
- treating local LLM output as forensic truth
- treating Agent Judge output as policy authorization
- treating runtime approval as approval for fleet-wide distribution
- writing tenant-scoped case content into shared memory, prompts, detections, or report templates

---

## Engineering Position

The engineering view is intentionally control-first.

The success of this architecture depends less on whether an agent can produce a useful answer and more on whether the organization can prove:

- which agent acted
- which tenant it acted within
- which evidence it used
- which policy was applied
- who approved the action
- which tool executed
- what outcome occurred
- whether the action was appropriate

That is the engineering standard for governed Agentic Security Operations.
