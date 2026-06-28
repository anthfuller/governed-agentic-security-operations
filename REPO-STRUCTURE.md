# Repository Structure

## Purpose

This file provides the detailed repository inventory for the governed agentic security operations architecture.

Use this file when you need the full repository layout, directory roles, diagram paths, and README casing conventions.

## Summary

| Metric | Count |
|---|---:|
| Total files | 173 |
| Markdown files | 137 |
| JSON example files | 24 |
| Diagram/image files | 10 |

## Top-Level Structure

The governance control areas are top-level directories. The `governance-library/` directory currently contains AI assurance and agent judge materials.

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

## Directory Inventory

| Directory | Files | Role |
|---|---:|---|
| root docs | 7 | Repository-level documentation, contribution guidance, security policy, disclaimer, and license. |
| `architecture/` | 15 | Architecture views, diagrams, assumptions, principles, layered model, control loop, and fleet architecture materials. |
| `patterns/` | 9 | Reusable architecture patterns for governed agentic security operations. |
| `examples/` | 31 | Scenario-oriented request, approval, policy-decision, judge-output, evidence, review, timeline, and audit artifacts. |
| `service-models/` | 11 | Operating models for MSSP, MDR, cloud incident response, private/local LLM-assisted DFIR, and fleet operations. |
| `threat-model/` | 18 | Threat-model overview and scenario-specific risk topics for agentic security operations. |
| `agent-governance/` | 8 | Agent identity, lifecycle, access scope, communication, monitoring, change management, fleet governance, and rollback. |
| `policy-enforcement/` | 8 | Policy decision and enforcement model, risk classification, approval policy, and fail-closed behavior. |
| `human-oversight/` | 7 | Human review, formal approval, customer approval, escalation, and review records. |
| `tenant-isolation/` | 6 | Tenant boundary model, scope validation, cross-tenant failure modes, and tenant-aware audit requirements. |
| `tool-access/` | 5 | Tool registration, scoped execution, restricted tool patterns, and tool-access audit. |
| `data-ingestion/` | 7 | Source metadata, normalization, enrichment, failure handling, and ingestion replay. |
| `evidence-traceability/` | 6 | Evidence references, evidence support for findings, DFIR evidence handling, and evidence audit replay. |
| `local-llm-dfir/` | 6 | Local/private LLM DFIR boundaries, evidence handling, review workflow, and replay considerations. |
| `audit-replay/` | 7 | Audit event model, replayability, correlation, exception and failure audit, and immutable audit guidance. |
| `templates/` | 10 | Standard records and reusable documentation templates. |
| `governance-library/` | 12 | AI assurance and agent judge materials under `governance-library/ai-assurance/`. |

## Structure Notes

- `agent-governance/`, `policy-enforcement/`, `human-oversight/`, `tenant-isolation/`, `tool-access/`, `data-ingestion/`, `evidence-traceability/`, `local-llm-dfir/`, and `audit-replay/` are top-level governance control directories.
- `governance-library/` currently contains `readme.md` and the `ai-assurance/` subdirectory.
- Scenario README files should link to shared architecture materials under `architecture/`.

## Diagram Paths

The root README references the following diagram files:

```text
architecture/diagrams/executive-architecture.png
architecture/diagrams/engineering-architecture.png
architecture/diagrams/governed-agentic-shared-operating-model.png
architecture/diagrams/control-Loop.png
architecture/diagrams/agentic-fleet-architecture.png
```

## README Casing

The repository currently uses both `README.md` and `readme.md`.

Links should match the filenames currently present in the repository. If the repository later standardizes on one casing convention, update links at the same time.
