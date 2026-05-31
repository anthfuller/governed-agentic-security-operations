# Architecture Assumptions

## Purpose

This document defines the assumptions and constraints behind the Governed Agentic Security Operations Architecture.

These assumptions help prevent overclaiming, clarify architectural guardrails, and identify the conditions required before the architecture is adapted into a real design, proof of concept, pilot, or production implementation.

This repository provides a reference architecture and control model. Organizations should adapt these patterns to their own security requirements, customer obligations, regulatory environment, technology stack, operating model, and risk-management process.

This file is an assumptions and constraints document. It is not a complete control contract and does not replace deeper control files for agent governance, policy enforcement, AI assurance, tenant isolation, human oversight, evidence handling, or audit logging.

---

## General Assumptions

1. The architecture is conceptual and docs-first.
2. The architecture is not a production implementation.
3. The architecture is intended for enterprise security operations, MSSP, MDR, Cloud Incident Response, and DFIR discussions.
4. The architecture assumes human oversight remains required for sensitive decisions.
5. The architecture assumes agent outputs require validation before trust.
6. The architecture assumes policy enforcement is externalized from the agent wherever practical.
7. The architecture assumes strong tenant isolation is required for MSSP and MDR use cases.
8. The architecture assumes evidence, policy decisions, approvals, and outputs must be traceable across the workflow.
9. The architecture assumes agents operate within registered identities, scoped permissions, mediated tools, and explicit control boundaries.
10. Implementation details will vary by organization and must be validated before operational use.

---

## Data Assumptions

The architecture assumes access to one or more telemetry or evidence sources, such as:

- SIEM data
- XDR data
- EDR data
- identity logs
- cloud audit logs
- SaaS logs
- firewall or network telemetry
- email security telemetry
- case management records
- threat intelligence
- forensic artifacts

The architecture assumes data must be normalized, enriched, filtered, and attributed before being supplied to agent workflows.

For MSSP, MDR, and DFIR use cases, evidence and telemetry must be associated with the correct tenant, customer, case, workspace, investigation, and source system wherever applicable.

The architecture does not assume that raw telemetry, model-generated summaries, or agent-produced interpretations are sufficient evidence by themselves.

---

## Agent Assumptions

The architecture assumes agents can support analyst, responder, and forensic workflows by receiving approved context, reasoning over case data, summarizing events, generating hypotheses, recommending next steps, requesting mediated tool actions, and producing structured outputs.

The architecture assumes agents MUST NOT:

- directly execute sensitive actions without mediated authorization
- bypass policy, PEP/PDP enforcement, approval workflows, or audit controls
- access arbitrary tools outside registered and authorized tool scopes
- retrieve arbitrary customer data outside approved tenant, case, workspace, investigation, or evidence scope
- make final forensic conclusions
- make final customer-impacting decisions
- approve containment, eradication, disclosure, escalation, reporting, or customer-facing release actions
- override human reviewers, customer approvers, PDP decisions, or operational policy

Agents are treated as workflow participants that require identity, ownership, scope, governance, monitoring, and auditability.

---

## Agent Judge Assumptions

The architecture assumes Agent Judges may support assurance activities such as output quality review, evidence-support review, consistency checks, unsupported-claim detection, tenant-boundary review, and human-review routing recommendations.

Agent Judges are not assumed to make enforcement decisions, approve sensitive actions, authorize tool execution, replace PDP/PEP controls, or act as accountable human approvers.

---

## Policy Assumptions

The architecture assumes a runtime policy model exists or can be introduced.

Policy decisions MUST remain aligned to the governed decision contract:

- `ALLOW`
- `DENY`
- `REQUIRE_APPROVAL`

Policy evaluation may consider tenant, customer, case, agent identity, analyst identity, action type, requested tool, evidence references, evidence confidence, data sensitivity, customer approval requirements, risk classification, destination system, and time or scope of access.

Where policy, identity, tenant context, evidence attribution, approval state, or tool authorization cannot be validated, workflows MUST fail closed, block execution, or route to authorized human review rather than proceed automatically.

The architecture does not assume that policy enforcement is performed by the LLM, the agent, the prompt, or an Agent Judge.

---

## PEP / PDP Enforcement Assumptions

The architecture assumes PEP/PDP enforcement is used to mediate access to tools, data retrieval, workflow actions, output release, and execution paths where policy decisions are required.

The architecture does not assume that every organization must use the same policy engine, policy language, or enforcement platform.

---

## Human Oversight Assumptions

The architecture assumes humans remain responsible for approving sensitive actions, validating forensic conclusions, communicating customer-impacting findings, authorizing containment recommendations, deciding when evidence is sufficient, handling legal or contractual escalation, accepting residual risk, and rejecting or overriding agent recommendations.

Human review and human approval are related but not identical.

Human review may evaluate quality, evidence support, completeness, uncertainty, or operational impact.

Human approval is an accountability decision authorizing a workflow, output, disclosure, escalation, containment recommendation, or customer-impacting action.

The architecture assumes customer approval may be required where actions affect customer environments, customer-facing reporting, incident declarations, containment recommendations, evidence release, or contractual obligations.

---

## Tenant Boundary Assumptions

The architecture assumes tenant isolation is a core control boundary for MSSP and MDR use cases.

Agents must not retrieve, mix, disclose, or reuse customer data across tenants unless explicitly authorized by policy, operating model, and customer obligations.

Ambiguous tenant context MUST trigger fail-closed handling or authorized human review before agent-assisted analysis, tool execution, customer-facing reporting, or DFIR conclusions are trusted.

---

## Auditability and Evidence Traceability Assumptions

The architecture assumes audit records must be able to connect the responsible agent, owner, analyst, tenant or customer context, case or investigation context, evidence references, policy decision, enforcement result, tool request, review or approval decision, model output, and released output where applicable.

The architecture does not assume that model output alone is a durable audit record or forensic evidence record.

---

## Local / Private LLM DFIR Assumptions

The architecture assumes local or private LLM-assisted DFIR may be needed when evidence cannot leave a controlled environment, cloud LLM use is restricted, sensitive artifacts require isolated analysis, customer or legal requirements limit data movement, or chain-of-custody expectations require stronger control of artifact access and transformation.

LLM-assisted DFIR output MUST be treated as an analytical aid, not evidence by itself, and MUST require evidence support, reviewer validation, and appropriate limitations before customer-facing conclusions are produced or released.

---

## Governance Assumptions

The architecture assumes governance frameworks may inform design, including:

- NIST AI RMF
- NIST Generative AI Profile
- EU AI Act considerations
- MITRE ATLAS
- MITRE ATT&CK
- F7-LAS

These references are used for alignment, threat-model context, and assurance framing, not as compliance claims.

F7-LAS is treated as a supporting control lens for agentic security architecture. It does not replace the SOC, MSSP, MDR, DFIR, policy-enforcement, human-oversight, tenant-isolation, or evidence-handling operating model.

---

## Product Assumptions

The architecture may reference Microsoft ecosystem concepts such as:

- Microsoft Sentinel
- Defender XDR
- Security Copilot agents
- Azure AI Foundry
- Microsoft Agent 365
- Microsoft Entra Agent ID
- Azure Functions
- Logic Apps

These references do not imply product roadmap alignment, guaranteed product capability, or a specific Microsoft implementation.

Microsoft Agent 365 and Microsoft Entra Agent ID, where referenced, are treated as Agent Governance and Identity Control Plane concepts, not as operational SOC agents, investigation agents, DFIR agents, or orchestration-layer workers.

The architecture does not assume that any named product natively provides all controls described in this repository.

---

## Constraints

Potential constraints include:

- model quality
- context-window limits
- hallucination risk
- telemetry quality
- incomplete or stale evidence
- prompt injection risk
- tool permission boundaries
- policy-engine availability
- customer data isolation requirements
- analyst trust
- audit logging completeness
- regulatory requirements
- contractual customer obligations
- cost and operational complexity
- model and workflow evaluation maturity
- integration limits across SIEM, XDR, SOAR, case management, identity, and DFIR systems

---

## Out-of-Scope Assumptions

The architecture does not assume:

- autonomous SOC replacement
- autonomous containment without approval
- unrestricted cross-tenant data access
- unrestricted agent tool access
- LLM-generated forensic conclusions as authoritative evidence
- product-native enforcement unless explicitly implemented
- framework alignment as proof of compliance
- agents replacing analysts, incident responders, forensic examiners, policy engines, or human approvers
- deployment readiness without validation, testing, governance review, and operational acceptance

---

## Validation Required

Before implementation, pilot, or production adoption, teams MUST validate data flows, permissions, tenant boundaries, tool execution paths, approval workflows, logging completeness, model behavior, prompt-injection resistance, incident-response procedures, evidence-handling requirements, fail-closed behavior, and customer-facing output controls.

Validation MUST include normal workflow behavior and failure scenarios, including ambiguous tenant context, missing evidence references, denied policy decisions, unavailable approval state, failed tool calls, incomplete audit records, and unsupported agent conclusions.

---

## Acceptance Criteria

This assumptions file is acceptable when it clearly states the architecture boundaries, avoids product or compliance overclaims, preserves the Agent Governance and Identity Control Plane placement for Microsoft Agent 365 and Microsoft Entra Agent ID, and does not replace the deeper control files for policy enforcement, tenant isolation, AI assurance, auditability, evidence handling, or human oversight.
