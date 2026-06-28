# Repository Structure

## Purpose

This file provides the detailed repository inventory so the root `README.md` can stay readable.

The root README should explain the repository and guide the reader. This file carries the larger map, structure notes, and path-correction details.

## Summary

Current inventory:

| Metric | Count |
|---|---:|
| Total files | 173 |
| Markdown files | 137 |
| JSON example files | 24 |
| Diagram/image files | 10 |

## Actual Top-Level Structure

The governance control directories are currently top-level directories, not nested under `governance-library/`.

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

## Important Structure Corrections

The previous root README had a long hand-written tree that did not match the zip. The main corrections are:

1. `agent-governance/`, `policy-enforcement/`, `human-oversight/`, `tenant-isolation/`, `tool-access/`, `data-ingestion/`, `evidence-traceability/`, `local-llm-dfir/`, and `audit-replay/` are top-level directories.
2. `governance-library/` currently contains `readme.md` and the `ai-assurance/` subdirectory.
3. The actual control-loop diagram filename is `architecture/diagrams/control-Loop.png`.
4. There is no `architecture/diagrams/layered-architecture.png`; the shared operating model diagram is `architecture/diagrams/governed-agentic-shared-operating-model.png`.
5. Many directory README files are named `readme.md` rather than `README.md`. Links should match actual paths unless the repo standardizes casing later.

## Link Cleanup Notes

A local markdown-link check reports zero missing local links after this pass. The scenario README links that previously pointed to `../../control-loop.md` and `../../layered-architecture.md` were corrected to the architecture directory paths:

```text
../../architecture/control-loop.md
../../architecture/layered-architecture.md
```

## Diagram Path Notes

The diagrams are retained as-is. Links in the root README point to the diagram filenames present in the repository, including:

```text
architecture/diagrams/executive-architecture.png
architecture/diagrams/engineering-architecture.png
architecture/diagrams/governed-agentic-shared-operating-model.png
architecture/diagrams/control-Loop.png
architecture/diagrams/agentic-fleet-architecture.png
```

## README Casing Notes

The repo currently mixes `README.md` and `readme.md`. Links in this pass use the filenames currently present in the repository.
