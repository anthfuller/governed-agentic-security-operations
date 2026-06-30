# Repository Structure

## Purpose

This file provides a detailed inventory of the repository layout for the Governed Agentic Security Operations Architecture project.

The root `README.md` explains the project at a high level. This file provides the deeper structural map for readers who want to understand how the quick-start guides, walkthroughs, architecture, governance patterns, service models, examples, threat models, and reusable templates are organized.

## Repository Summary

| Metric | Count |
|---|---:|
| Total files | 185 |
| Markdown files | 149 |
| JSON example files | 24 |
| Diagram/image files | 10 |

## Top-Level Layout

The repository is organized as a documentation-first architecture and governance library. Core architecture materials, reusable patterns, scenario examples, service models, threat models, governance controls, and templates are separated into dedicated top-level directories.

```text
governed-agentic-security-operations-architecture/
├── README.md
├── REPO-STRUCTURE.md
├── CONTRIBUTOR.md
├── DISCLAIMER.md
├── LICENSE
├── SECURITY.md
├── quick-start/
├── walkthroughs/
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

| Directory | Files | Purpose |
|---|---:|---|
| root docs | 7 | Repository-level documentation, contribution guidance, security policy, disclaimer, and license. |
| `quick-start/` | 4 | Role-based navigation guides for MSSP/MDR, DFIR, and PoC-builder readers. |
| `walkthroughs/` | 2 | Concrete scenario walkthroughs showing governed agentic security operations flows from recommendation through audit replay. |
| `architecture/` | 15 | Core architecture views, diagrams, assumptions, principles, layered model, control loop, and fleet architecture materials. |
| `patterns/` | 9 | Reusable architecture patterns for governed agentic security operations. |
| `examples/` | 31 | Scenario-oriented request, approval, policy-decision, judge-output, evidence, review, timeline, and audit artifacts. |
| `service-models/` | 11 | Operating models for MSSP, MDR, cloud incident response, private/local LLM-assisted DFIR, and fleet operations. |
| `threat-model/` | 18 | Threat-model overview and scenario-specific risk topics for agentic security operations. |
| `agent-governance/` | 8 | Agent identity, lifecycle, access scope, communication, monitoring, change management, fleet governance, and rollback. |
| `policy-enforcement/` | 8 | Policy decision and enforcement model, risk classification, approval policy, and fail-closed behavior. |
| `human-oversight/` | 13 | Human review, formal approval, analyst checkpoints, HITL/HOTL, accountability, sensitive-action approval, customer approval, escalation, fleet-change approval, and review records. |
| `tenant-isolation/` | 6 | Tenant boundary model, scope validation, cross-tenant failure modes, and tenant-aware audit requirements. |
| `tool-access/` | 5 | Tool registration, scoped execution, restricted tool patterns, and tool-access audit. |
| `data-ingestion/` | 7 | Source metadata, normalization, enrichment, failure handling, and ingestion replay. |
| `evidence-traceability/` | 6 | Evidence references, finding support, DFIR evidence handling, and evidence audit replay. |
| `local-llm-dfir/` | 6 | Local/private LLM-assisted DFIR boundaries, evidence handling, review workflow, and replay considerations. |
| `audit-replay/` | 7 | Audit event model, replayability, correlation, exception and failure audit, and immutable audit guidance. |
| `templates/` | 10 | Standard records and reusable documentation templates. |
| `governance-library/` | 12 | AI assurance and agent judge materials, including reusable assurance contracts and evaluation guidance. |

## Repository Organization Model

The repository separates architecture concerns from implementation concerns:

- `quick-start/` provides role-based navigation paths for different readers.
- `walkthroughs/` connects the architecture to concrete governed security operations scenarios.
- `architecture/` defines the conceptual and engineering views.
- `patterns/` captures reusable design patterns.
- `examples/` provides non-runnable example artifacts for architecture discussion.
- `service-models/` describes operational boundaries for MSSP, MDR, cloud incident response, and DFIR use cases.
- `threat-model/` captures adversarial, misuse, and failure-mode analysis.
- Governance control directories define control responsibilities across agent lifecycle, policy enforcement, human oversight, tenant isolation, tool access, ingestion, evidence traceability, local/private LLM-assisted DFIR, and audit replay.
- `templates/` provides reusable record formats for documenting decisions, approvals, reviews, evidence references, and audit events.
- `governance-library/` contains supporting AI assurance materials, including agent judge concepts and output quality checks.

This structure is intended to make the repository easier to review, navigate, extend, and audit.

## Governance Control Areas

The governance control areas are maintained as top-level directories so each control domain can be reviewed independently.

| Control Area | Directory |
|---|---|
| Agent identity, lifecycle, fleet change control, recall, and rollback | `agent-governance/` |
| Policy decision, policy enforcement, approval policy, and fail-closed behavior | `policy-enforcement/` |
| Human review, formal approval, escalation, and customer approval boundaries | `human-oversight/` |
| Tenant, customer, case, and evidence boundary protection | `tenant-isolation/` |
| Tool registration, scoped tool execution, and restricted tool access | `tool-access/` |
| Source metadata, enrichment, normalization, and ingestion replay | `data-ingestion/` |
| Evidence references, evidence support, and DFIR evidence handling | `evidence-traceability/` |
| Local/private LLM-assisted DFIR boundaries and review workflow | `local-llm-dfir/` |
| Audit events, replayability, correlation, and failure audit | `audit-replay/` |

## Diagram References

The main architecture diagrams referenced by the root `README.md` are stored under `architecture/diagrams/`.

```text
architecture/diagrams/executive-architecture.png
architecture/diagrams/engineering-architecture.png
architecture/diagrams/governed-agentic-shared-operating-model.png
architecture/diagrams/control-Loop.png
architecture/diagrams/agentic-fleet-architecture.png
```

## File Naming and Link Conventions

Some directories use `README.md`; others use `readme.md`.

Links in this repository should match the actual filename casing used in the target path. If the repository later standardizes on a single casing convention, update the linked paths at the same time to avoid broken links on case-sensitive systems.

## Public Repository Scope

This repository is intended to remain documentation-first. The `quick-start/` and `walkthroughs/` directories are documentation aids, not runtime implementation artifacts.

It does not contain production implementation code, customer data, tenant data, employer confidential information, non-public product information, runnable control-plane code, KQL query packs, infrastructure automation, CI/CD pipelines, or deployment artifacts.

Runnable examples, executable schemas, policy-as-code examples, tests, telemetry generation, and implementation-specific control-plane code should live in a separate companion implementation repository.
