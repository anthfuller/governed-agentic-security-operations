# Threat Model

## Purpose

This directory defines the threat model for the **Governed Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The threat model identifies how agentic security operations can fail, be abused, be bypassed, or produce unsafe outcomes across customer-scoped security operations, MDR workflows, SOC/IR processes, cloud incident response, DFIR, and private/local LLM-assisted forensic analysis.

This directory is designed to support engineering review, architecture review, control validation, audit readiness, and implementation planning. It maps threats to concrete control surfaces, including PDP decisions, PEP enforcement, Agent Judge assurance, human approval, customer authorization, evidence handling, identity governance, and audit/replay controls.

## Scope

This directory covers threats involving:

- agentic SOC and MDR workflows;
- MSSP multi-customer and multi-tenant service operations;
- cloud IAM compromise and cloud response workflows;
- private/local LLM-assisted DFIR workflows;
- retrieval-augmented generation, vector search, memory, and knowledge stores;
- prompt injection through telemetry, logs, alerts, tickets, emails, case notes, reports, and evidence;
- privileged tool use, automation, API execution, and state-changing actions;
- human approval, customer authorization, and customer-facing release;
- agent identity, lifecycle, ownership, registration, monitoring, and revocation;
- evidence provenance, chain of custody, timeline generation, forensic conclusions, and report release.

This directory does not replace detailed implementation specifications, product-specific deployment guides, formal legal review, customer contractual requirements, or production security validation.

## Architecture Boundary

This threat model assumes the following architecture boundary:

- operational SOC/MDR/DFIR agents assist with triage, investigation, enrichment, summarization, recommendation drafting, timeline support, and report preparation;
- Agent Judges provide assurance by checking evidence support, hallucination risk, tenant boundaries, policy alignment, output quality, and release readiness;
- the PDP decides whether an action, retrieval, output, release, or state transition is allowed, denied, or requires approval;
- the PEP enforces the PDP decision at workflow, tool, retrieval, identity, evidence, output, and API boundaries;
- human approval is required for sensitive, privileged, customer-impacting, externally visible, or evidence-sensitive actions;
- customer authorization is required where the action, service agreement, impact, legal sensitivity, or release path requires it;
- audit records must support replay, investigation, and reconstruction.

**Microsoft Entra Agent ID and Microsoft Agent 365 belong in the Agent Governance and Identity Control Plane, not in the operational SOC agent layer.** They govern agent identity, registration, lifecycle, ownership, monitoring, policy, and trust. They are not represented as SOC triage, investigation, enrichment, or response agents.

## Directory Structure

```text
threat-model/
├── README.md
├── agentic-security-operations-threat-model.md
├── mitre-atlas-threats.md
├── prompt-injection-through-logs.md
├── rag-memory-contamination.md
├── rag-poisoning.md
├── cross-tenant-cross-customer-risk.md
├── tool-use-and-automation-risk.md
├── malicious-tool-output.md
├── human-approval-and-release-risk.md
├── overreliance-on-ai.md
├── compromised-agent-identity.md
├── rogue-agent-risk.md
├── local-llm-dfir-risk.md
└── mitigations.md
```

## File Responsibilities

| File | Responsibility |
|---|---|
| `README.md` | Defines the directory purpose, scope, control principles, file ownership, and minimum review expectations. |
| `agentic-security-operations-threat-model.md` | Provides the architecture-wide threat model across agentic security operations, control planes, service models, and trust boundaries. |
| `mitre-atlas-threats.md` | Maps relevant AI, model, prompt, retrieval, agent, and tool threats to MITRE ATLAS-aligned categories and architecture-specific controls. |
| `prompt-injection-through-logs.md` | Covers instruction injection through logs, alerts, tickets, emails, evidence, telemetry, reports, case notes, and analyst-entered text. |
| `rag-memory-contamination.md` | Covers cross-tenant, cross-customer, cross-case, stale, unauthorized, or untrusted retrieval and memory contamination. |
| `rag-poisoning.md` | Covers poisoning of retrieval sources, vector indexes, summaries, embeddings, case knowledge, analyst notes, and derived artifacts. |
| `cross-tenant-cross-customer-risk.md` | Covers tenant, customer, case, incident, workflow, evidence, output, and retrieval boundary failures in MSSP/MDR/DFIR operations. |
| `tool-use-and-automation-risk.md` | Covers unsafe tool execution, automation misuse, privileged connector abuse, workflow state changes, and API execution risk. |
| `malicious-tool-output.md` | Covers compromised, misleading, malformed, stale, prompt-injected, or adversarial tool output that could influence agent reasoning or execution. |
| `human-approval-and-release-risk.md` | Covers approval bypass, approval spoofing, approval reuse, weak review, release errors, customer authorization gaps, and rubber-stamp risk. |
| `overreliance-on-ai.md` | Covers automation bias, weak analyst review, over-trust in model outputs, unsupported conclusions, and unsafe customer-facing use. |
| `compromised-agent-identity.md` | Covers stolen, abused, overprivileged, mis-scoped, or unmanaged agent identities and credentials. |
| `rogue-agent-risk.md` | Covers shadow agents, unregistered agents, unsafe delegation, unmanaged lifecycle, unauthorized agent-to-agent activity, and agent sprawl. |
| `local-llm-dfir-risk.md` | Covers private/local LLM-assisted DFIR, evidence integrity, chain of custody, local retrieval, forensic timeline generation, and report release. |
| `mitigations.md` | Provides a consolidated mitigation catalog mapped to PDP, PEP, Agent Judge, human approval, customer authorization, identity, evidence, and audit controls. |

## Non-Duplication Rules

This directory should avoid redundant alias files that split ownership without adding a distinct threat surface.

The following files should not be added as separate files unless a future architecture decision creates a distinct control surface:

| File | Reason |
|---|---|
| `threat-model-overview.md` | Covered by `README.md` and `agentic-security-operations-threat-model.md`. |
| `tool-misuse.md` | Covered by `tool-use-and-automation-risk.md`. |
| `cross-tenant-data-leakage.md` | Covered by `cross-tenant-cross-customer-risk.md`. |

New files should be added only when they introduce a distinct threat surface, control surface, service-model boundary, or review responsibility not already covered by the current directory.

## Service Model Coverage

| Service Model | Threat Focus |
|---|---|
| MSSP | Multi-customer isolation, customer authorization, tenant-safe retrieval, reporting boundaries, and managed-service action control. |
| MDR | Alert triage, containment recommendation, response automation, tool access, approval workflows, and customer-impacting response actions. |
| SOC / Incident Response | Investigation support, incident coordination, state changes, escalation, analyst review, and operational response safety. |
| Cloud Incident Response | Cloud IAM compromise, SaaS/cloud audit scope, privileged access, token/session revocation, OAuth abuse, and customer authorization. |
| DFIR | Evidence integrity, chain of custody, timeline accuracy, forensic conclusions, report release, and audit replay. |
| Private / Local LLM-assisted DFIR | Isolated model execution, case-scoped retrieval, evidence-sensitive analysis, local workspaces, and controlled report drafting. |

## Threat Modeling Method

Each threat model file should use the following structure:

1. **Purpose** — the specific risk surface addressed by the file.
2. **Scope** — the service models, architecture layers, actors, data, tools, evidence, outputs, and trust boundaries in scope.
3. **Threat Scenarios** — concrete ways the architecture can fail, be abused, or be bypassed.
4. **Attack Paths** — how an attacker, rogue agent, compromised identity, poisoned context, unsafe tool, or weak process could trigger the threat.
5. **Required Controls** — enforceable controls required before the pattern is acceptable.
6. **PDP / PEP Mapping** — which decisions are made by policy and where enforcement occurs.
7. **Agent Judge and Human Review Mapping** — where assurance and human approval apply, without confusing them with authorization.
8. **Deny and Fail-Closed Conditions** — exact conditions that block retrieval, execution, release, approval, or state change.
9. **Audit and Replay Requirements** — required records for reconstruction and investigation.
10. **Acceptance Criteria** — objective pass/fail criteria.

## Core Threat Surfaces

| Threat Surface | Description | Required Boundary |
|---|---|---|
| Prompt injection through operational data | Logs, alerts, tickets, emails, reports, telemetry, case notes, and evidence may contain hostile instructions. | Treat all operational content as untrusted data. Separate retrieved content from instructions. Validate outputs before action or release. |
| RAG and memory contamination | Retrieval or memory may mix tenants, customers, cases, incidents, stale content, unauthorized records, or prior unrelated context. | Enforce `knowledge_store_or_memory_scope`, `knowledge_memory_scope_result`, retrieval freshness, tenant/customer/case scope, and retrieval audit. |
| RAG poisoning | Indexed content, embeddings, summaries, documents, notes, or knowledge entries may be manipulated to bias the agent. | Validate source provenance, parser version, ingestion path, sensitivity label, trust classification, freshness, and evidence support. |
| Cross-tenant and cross-customer bleed | MSSP/MDR workflows may retrieve, summarize, act on, or release information outside the authorized customer scope. | Fail closed on missing or mismatched `tenant_id`, `customer_id`, `case_id`, `incident_id`, `workflow_id`, or evidence attribution. |
| Tool and automation misuse | Agents may trigger privileged tools, connectors, APIs, or workflows outside approval or policy scope. | Require PDP decision and PEP enforcement at workflow, tool wrapper, API gateway, identity, evidence, and output boundaries. |
| Malicious tool output | Tool responses may be compromised, malformed, stale, deceptive, prompt-injected, or outside expected schema. | Validate tool identity, owner, schema, source/destination metadata, parser version, output classification, and confidence before use. |
| Human approval and release risk | Approval may be missing, vague, spoofed, expired, reused, rubber-stamped, or disconnected from the executed action. | Require scoped, time-bounded, cryptographically bound approval records; policy validation; PEP verification; customer authorization where required; and audit. |
| Overreliance on AI | Analysts may treat model output as authoritative without validating evidence support or uncertainty. | Require evidence support, uncertainty labeling, Agent Judge checks, human review, and separate customer-release controls. |
| Compromised agent identity | Agent identity, credentials, or permissions may be stolen, abused, or over-scoped. | Enforce agent registration, ownership, least privilege, credential scope, lifecycle controls, monitoring, and revocation. |
| Rogue agent risk | Unregistered or unmanaged agents may operate outside governance and monitoring. | Require agent registry, attestation, lifecycle state, owner accountability, policy binding, and blocking of unregistered agents. |
| Local LLM DFIR risk | Local models may mishandle evidence, generate unsupported conclusions, or break forensic integrity. | Enforce isolated execution, read-only originals, derived artifact separation, chain-of-custody preservation, analyst review, and release controls. |

## Required Control Principles

The following principles are mandatory across this directory:

- **No implicit agent trust.** Agent-to-agent, agent-to-tool, agent-to-retrieval, and agent-to-output requests must be validated before they affect customer environments, tools, evidence, or outputs.
- **PDP decides, PEP enforces.** A policy decision is not sufficient unless the execution boundary enforces it.
- **Agent Judges are assurance, not authorization.** Agent Judges evaluate quality, evidence support, hallucination risk, tenant boundaries, and policy alignment. They do not approve sensitive execution.
- **Human review is not automatically execution approval.** Sensitive execution requires a scoped approval record, policy validation, PEP enforcement, and audit linkage.
- **Customer authorization is separate from internal approval.** Customer-impacting actions and customer-facing releases require customer authorization where service agreement, legal, contractual, or operational impact requires it.
- **Private/local execution is not proof of correctness.** Local LLM-assisted DFIR still requires evidence provenance, human review, audit, and chain-of-custody controls.
- **Missing control metadata fails closed.** Missing scope, policy decision, approval record, evidence reference, output destination, or audit linkage must block execution or release.

## Minimum Control Metadata

Threat model files should require the following fields where relevant:

| Control Surface | Required Metadata |
|---|---|
| Tenant and customer boundary | `tenant_id`, `customer_id`, `case_id`, `incident_id`, `workflow_id` |
| Evidence traceability | `evidence_object_ids`, `evidence_ref`, source timestamps, ingestion timestamp, provenance, chain-of-custody reference where applicable |
| Retrieval and memory | `knowledge_store_or_memory_scope`, `knowledge_memory_scope_result`, retrieved context IDs, freshness result, cross-scope detection result |
| Tool use | `tool_id`, `tool_owner`, `source_system_id`, `destination_system_id`, `requested_action`, approved parameters, output destination |
| Policy decision | `policy_decision_id`, `decision`, `reason`, `expires_at`, `audit_required`, obligations, denied operations |
| Human approval | `approval_record_id`, reviewer identity, reviewer role, approved action, approved scope, approved parameters, expiration, cryptographic binding, customer authorization reference where required |
| Agent identity | `agent_id`, owner, lifecycle state, permissions, credential scope, registration state, attestation state |
| Audit and replay | `audit_reference_id`, `correlation_id`, request IDs, prompt references, model references, policy references, execution results, final workflow state |

## If / Then Control Rules

| Condition | Required Outcome |
|---|---|
| If tenant, customer, case, incident, or workflow scope is missing or mismatched | Deny or return for clarification; do not retrieve, execute, or release. |
| If retrieved context crosses customer, tenant, case, incident, or evidence boundaries | Deny the retrieval result, mark a scope violation, and emit an audit event. |
| If RAG content is untrusted, stale, poisoned, or lacks provenance | Exclude it from authoritative reasoning or route for validation. |
| If an agent requests sensitive execution without a valid policy decision | Deny execution. |
| If policy requires approval and no valid approval record exists | Deny execution and route to the approval workflow. |
| If approval exists but is expired, reused, mismatched, unsigned, or outside scope | Fail closed. |
| If an action changes after approval | Re-run policy evaluation and require new approval where sensitive. |
| If a tool call targets a different system, identity, evidence object, customer, or output destination than approved | Block at the PEP. |
| If a tool output is malformed, unexpected, malicious, stale, or outside schema | Treat it as untrusted and block downstream action until validated. |
| If an output is customer-facing | Require release review, policy decision, customer authorization where required, and audit linkage. |
| If local LLM output contains forensic conclusions | Require analyst review and evidence support before internal use; require separate release approval before customer use. |
| If a model, agent, tool, retrieval source, or workflow is unregistered or unapproved | Deny or quarantine the workflow depending on severity. |

## Relationship to Architecture Layers

| Layer | Threat Model Concern |
|---|---|
| Customer / Telemetry Sources | Treat all logs, alerts, emails, evidence, SaaS data, tickets, and customer-provided content as untrusted input. |
| Ingestion / Normalization | Preserve source metadata, evidence references, timestamps, parser version, schema version, data classification, sensitivity label, and destination metadata. |
| Agentic SOC / Orchestration | Prevent unsafe delegation, unsupported conclusions, unapproved actions, cross-scope orchestration, and direct execution. |
| AI Assurance & Human Oversight | Validate evidence support, hallucination risk, tenant boundaries, HITL/HOTL triggers, release readiness, and unsupported claims. |
| Governance & Policy Control Plane | Enforce PDP/PEP decisions, scoped credentials, approval workflows, fail-closed controls, audit, replay, and monitoring. |
| Private / Local DFIR Processing | Protect evidence integrity, local retrieval scope, isolated model execution, timeline review, and forensic release gates. |
| Agent Governance and Identity Control Plane | Register, identify, authenticate, authorize, monitor, and lifecycle-manage agents. Entra Agent ID and Microsoft Agent 365 belong here, not in the operational SOC agent layer. |

## Acceptance Criteria

This directory is acceptable when:

- each threat-model file maps threats to concrete control surfaces;
- each file identifies deny and fail-closed paths;
- each file distinguishes Agent Judge assurance from PDP authorization and PEP enforcement;
- each file addresses tenant, customer, case, workflow, evidence, retrieval, tool, output, approval, and audit boundaries where relevant;
- RAG, vector search, memory, retrieved context, stale context, and poisoned context are treated as threat surfaces;
- human approval is scoped, time-bounded, cryptographically bound, policy-validated, and PEP-enforced where sensitive actions are involved;
- customer-facing release is handled separately from internal recommendation, internal analysis, or reviewed draft output;
- private/local LLM-assisted DFIR does not weaken evidence integrity, chain-of-custody, analyst-review, or release requirements;
- Entra Agent ID and Microsoft Agent 365 are consistently represented as governance and identity control-plane capabilities, not operational SOC agents;
- all threat files support audit and replay.

## Non-Goals

This directory does not:

- define a vendor-specific product implementation;
- replace formal STRIDE, MITRE ATLAS, ATT&CK, NIST AI RMF, legal, regulatory, or customer-specific risk assessments;
- authorize production containment actions;
- treat AI-generated analysis as final truth;
- require human approval for every low-risk read-only action;
- duplicate architecture, examples, or pattern files except where a threat boundary must be restated for clarity.

## Reading Order

Recommended reading order:

1. `README.md`
2. `agentic-security-operations-threat-model.md`
3. `mitre-atlas-threats.md`
4. `prompt-injection-through-logs.md`
5. `rag-memory-contamination.md`
6. `rag-poisoning.md`
7. `cross-tenant-cross-customer-risk.md`
8. `tool-use-and-automation-risk.md`
9. `malicious-tool-output.md`
10. `human-approval-and-release-risk.md`
11. `overreliance-on-ai.md`
12. `compromised-agent-identity.md`
13. `rogue-agent-risk.md`
14. `local-llm-dfir-risk.md`
15. `mitigations.md`

## Summary

This threat model directory supports governed agentic security operations by identifying where trust can fail and defining the control surfaces required to contain that failure.

The architecture is acceptable only when sensitive actions, evidence handling, retrieval, output release, agent identity, tool use, and customer-impacting decisions are bound to explicit scope, policy decisions, enforcement points, human approval where required, customer authorization where required, and complete auditability.
