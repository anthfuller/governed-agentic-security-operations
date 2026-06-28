# Repository Structure

## Purpose

This file provides a detailed map of the repository layout so the root `README.md` can stay focused on the architecture narrative.

## Top-Level Layout

```text
governed-agentic-security-operations-architecture/
├── README.md
├── REPO-STRUCTURE.md
├── CONTRIBUTOR.md
├── DISCLAIMER.md
├── LICENSE
├── SECURITY.md
├── architecture/
├── patterns/
├── examples/
├── service-models/
├── threat-model/
├── agent-governance/
├── policy-enforcement/
├── human-oversight/
├── tenant-isolation/
├── tool-access/
├── data-ingestion/
├── evidence-traceability/
├── local-llm-dfir/
├── audit-replay/
├── templates/
└── governance-library/
```

## Top-Level Directory Roles

| Directory | Role |
|---|---|
| `architecture/` | Architecture views, assumptions, principles, layered model, control loop, fleet architecture, and diagrams. |
| `patterns/` | Reusable architecture patterns for governed agentic security operations. |
| `examples/` | Scenario-oriented request, approval, policy-decision, judge-output, evidence, review, timeline, and audit artifacts. |
| `service-models/` | Operating models for MSSP, MDR, cloud incident response, private/local LLM-assisted DFIR, and fleet operations. |
| `threat-model/` | Threat scenarios and risk models for agentic security operations. |
| `agent-governance/` | Agent identity, lifecycle, access scope, communication, monitoring, change management, fleet governance, and rollback. |
| `policy-enforcement/` | Policy decision and enforcement model, risk classification, approval policy, and fail-closed behavior. |
| `human-oversight/` | Human review, formal approval, customer approval, escalation, and review records. |
| `tenant-isolation/` | Tenant boundary model, scope validation, cross-tenant failure modes, and tenant-aware audit requirements. |
| `tool-access/` | Tool registration, scoped execution, restricted tool patterns, and tool-access audit. |
| `data-ingestion/` | Source metadata, normalization, enrichment, failure handling, and ingestion replay. |
| `evidence-traceability/` | Evidence references, evidence support for findings, DFIR evidence handling, and evidence audit replay. |
| `local-llm-dfir/` | Local/private LLM DFIR boundaries, evidence handling, review workflow, and replay considerations. |
| `audit-replay/` | Audit event model, replayability, correlation, exception and failure audit, and immutable audit guidance. |
| `templates/` | Standard records and reusable documentation templates. |
| `governance-library/` | Shared governance-library material, including AI assurance and Agent Judge references. |

## Control Area Map

| Area | Control Focus |
|---|---|
| `governance-library/ai-assurance/` | Agent Judges, evidence support, output quality, unsupported claims, tenant-boundary checks, HITL checks, ATLAS mapping, and judge limitations. |
| `policy-enforcement/` | PEP/PDP model, policy contracts, risk classification, approval requirements, fleet authorization, and fail-closed behavior. |
| `agent-governance/` | Agent identity, lifecycle, access scope, communication, monitoring, oversight, fleet governance, and version rollback. |
| `human-oversight/` | Human review model, approval boundaries, customer approval, escalation, review records, and emergency override handling. |
| `tenant-isolation/` | Tenant boundary model, cross-tenant failure modes, tenant-scope validation, audit requirements, and fleet propagation boundaries. |
| `tool-access/` | Tool access model, registration requirements, restricted tool patterns, and execution audit. |
| `data-ingestion/` | Ingestion model, source metadata, normalization, enrichment, failure handling, sanitization, and replay. |
| `evidence-traceability/` | Evidence model, evidence references, finding support, DFIR evidence handling, and audit replay. |
| `local-llm-dfir/` | Local/private model use, evidence handling, output boundaries, review approval, and replay. |
| `audit-replay/` | Audit event model, replay requirements, correlation model, exception audit, rollout audit, and immutable audit guidance. |

## Example Scenario Areas

| Scenario Directory | Focus |
|---|---|
| `examples/alert-triage-to-recommendation/` | Alert triage, recommendation generation, judge output, policy decision, and audit event. |
| `examples/cloud-iam-compromise/` | Cloud IAM compromise workflow with approval, policy decision, and audit event. |
| `examples/local-llm-forensic-timeline/` | Private/local LLM-assisted forensic timeline workflow with evidence manifest, timeline output, review record, and audit event. |
| `examples/fleet-update-rollout/` | Fleet update request, policy decision, approval record, and rollout audit event. |
| `examples/compromised-agent-recall/` | Agent recall request, recall policy decision, approval record, and recall audit event. |
| `examples/cross-tenant-sanitized-intelligence-propagation/` | Sanitized intelligence release request, sanitization review, release policy decision, and release audit event. |

## Diagram Assets

```text
architecture/diagrams/executive-architecture.png
architecture/diagrams/engineering-architecture.png
architecture/diagrams/governed-agentic-shared-operating-model.png
architecture/diagrams/control-Loop.png
architecture/diagrams/agentic-fleet-architecture.png
```
