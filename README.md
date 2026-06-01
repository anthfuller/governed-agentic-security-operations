# Governed Agentic Security Operations Architecture

## Purpose

This repository is a conceptual reference architecture and pattern library for governed agentic security operations across MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

The purpose is to define architecture views, reusable patterns, scenario documentation, service operating models, threat models, templates, and governance-library control references for designing agentic security operations that are controlled rather than blindly trusted.

This repository is not a runnable implementation repository. Runtime code, tests, schemas, policy execution files, KQL query packs, infrastructure automation, Docker files, CI pipelines, and implementation-specific control-plane code belong in the separate companion PoC repository.

## What This Repository Is

This repository is a documentation-first architecture library. It helps security architects, SOC leaders, MDR and MSSP teams, DFIR practitioners, and AI security engineers reason about how agentic systems can assist security operations while remaining bounded by policy, oversight, evidence, tenant isolation, and audit requirements.

It is intended to support architecture review, design discussion, governance planning, service-model alignment, and implementation alignment.

## What This Repository Is Not

This repository is not production deployment code.

It does not provide a SOC automation product, autonomous response platform, production control plane, SIEM/SOAR deployment package, legally sufficient DFIR evidence system, or customer-ready managed security service by itself.

It does not contain a runnable application, tests, schemas, policy execution files, KQL query packs, infrastructure automation, Docker files, CI pipelines, runtime source code, or implementation-specific control-plane code.

## Core Governance Invariants

This architecture is built around one principle: agentic systems may assist security operations, but they do not authorize themselves.

The following boundaries are non-negotiable:

- Agent outputs do not authorize execution.
- Agent Judges are assurance components only; they do not grant approval.
- The Policy Decision Point decides whether an action is allowed, denied, escalated, or failed closed.
- The Policy Enforcement Point enforces the decision before any tool, tenant, evidence store, or production system is affected.
- Human review is not the same as formal approval.
- Customer approval is separate from internal MSSP, MDR, SOC, or DFIR review.
- Tool registration and tool availability are not authorization.
- Evidence-derived summaries are not original evidence.
- Private/local LLM execution is not proof of correctness, evidentiary validity, or forensic completeness.
- Customer-facing release requires proper review and approval paths.
- RAG, memory, retrieval, vector search, customer context, case memory, shared context, evidence retrieval, and retrieved context must preserve tenant, customer, case, evidence, retention, and data-sovereignty boundaries.
- Missing, ambiguous, stale, unauthorized, cross-tenant, cross-customer, cross-case, retention-inconsistent, or unauditable context must fail closed where governed workflow behavior depends on it.

## Reader Path

Use the repository in this order:

```text
architecture → patterns → examples → service-models → threat-model → templates → governance-library
```

Start with `architecture/` to understand the operating model, architecture views, control loop, assumptions, and principles.

Move to `patterns/` for reusable design patterns, then `examples/` for scenario-oriented documentation artifacts. Use `service-models/` to reason about MSSP, MDR, cloud incident response, and private/local LLM-assisted DFIR operating boundaries. Review `threat-model/` before adapting the records in `templates/`.

Use `governance-library/` when detailed control requirements are needed.

## Full Repository Structure

```text
governed-agentic-security-operations-architecture/
│
├── README.md
│
├── architecture/
│   ├── README.md
│   ├── executive-view.md
│   ├── engineering-view.md
│   ├── layered-architecture.md
│   ├── control-loop.md
│   ├── architecture-principles.md
│   ├── architecture-assumptions.md
│   └── diagrams/
│       ├── executive-architecture.png
│       ├── engineering-architecture.png
│       ├── layered-architecture.png
|       ├── f7-las-executive-control-loop-agentic-systems.png
│       └── control-loop.png
│
├── patterns/
│   ├── README.md
│   ├── governed-agentic-security-operations-pattern.md
│   ├── policy-enforced-tool-use-pattern.md
│   ├── human-approved-sensitive-action-pattern.md
│   ├── tenant-safe-rag-memory-pattern.md
│   └── private-local-llm-dfir-pattern.md
│
├── examples/
│   ├── README.md
│   ├── alert-triage-to-recommendation/
│   │   ├── README.md
│   │   ├── example-request.json
│   │   ├── example-judge-output.json
│   │   ├── example-policy-decision.json
│   │   └── example-audit-event.json
│   │
│   ├── cloud-iam-compromise/
│   │   ├── README.md
│   │   ├── example-request.json
│   │   ├── example-approval-record.json
│   │   ├── example-policy-decision.json
│   │   └── example-audit-event.json
│   │
│   └── local-llm-forensic-timeline/
│       ├── README.md
│       ├── example-evidence-manifest.json
│       ├── example-timeline-output.json
│       ├── example-review-record.json
│       └── example-audit-event.json
│
├── service-models/
│   ├── README.md
│   ├── mssp-operating-model.md
│   ├── mdr-operating-model.md
│   ├── cloud-ir-operating-model.md
│   ├── private-local-llm-dfir-operating-model.md
│   └── diagrams/
│       ├── mssp-operating-model.png
│       ├── mdr-operating-model.png
│       ├── dfir-operating-model.png
│       └── shared-operating-boundaries.png
│
├── threat-model/
│   ├── README.md
│   ├── agentic-security-operations-threat-model.md
|   |── mitre-atlas-threats.md
│   ├── prompt-injection-through-logs.md
│   ├── rag-memory-contamination.md
|   ├── rag-poisoning.md
│   ├── cross-tenant-cross-customer-risk.md
│   ├── tool-use-and-automation-risk.md
|   ├── malicious-tool-output.md
│   ├── human-approval-and-release-risk.md
|   ├── overreliance-on-ai.md
│   ├── compromised-agent-identity.md
│   ├── rogue-agent-risk.md
│   ├── local-llm-dfir-risk.md
|   └── mitigations.md
│
├── templates/
│   ├── README.md
│   ├── agent-card-template.md
│   ├── tool-contract-template.md
│   ├── policy-decision-record-template.md
│   ├── judge-output-template.md
│   ├── human-approval-record-template.md
│   ├── customer-approval-record-template.md
│   ├── audit-event-template.md
│   ├── evidence-manifest-template.md
│   └── adr-template.md
│
└── governance-library/
    ├── README.md
    │
    ├── ai-assurance/
    │   ├── README.md
    │   ├── agent-judges-overview.md
    │   ├── judge-evaluation-contract.md
    │   ├── evidence-support-judge.md
    │   ├── output-quality-judge.md
    │   ├── tenant-boundary-judge.md
    │   ├── unsupported-claim-judge.md
    │   ├── hitl-requirement-check.md
    │   ├── attack-atlas-mapping-judge.md
    │   └── judge-limitations.md
    │
    ├── policy-enforcement/
    │   ├── README.md
    │   ├── pep-pdp-model.md
    │   ├── policy-decision-flow.md
    │   ├── policy-contract.md
    │   ├── action-risk-classification.md
    │   ├── approval-policy-requirements.md
    │   └── fail-closed-behavior.md
    │
    ├── agent-governance/
    │   ├── README.md
    │   ├── agent-identity-lifecycle.md
    │   ├── agent-access-scope.md
    │   ├── agent-to-agent-communication.md
    │   ├── agent-monitoring-and-oversight.md
    │   └── agent-change-management.md
    │
    ├── human-oversight/
    │   ├── README.md
    │   ├── human-review-model.md
    │   ├── approval-boundaries.md
    │   ├── customer-approval-model.md
    │   ├── escalation-paths.md
    │   └── review-record-requirements.md
    │
    ├── tenant-isolation/
    │   ├── README.md
    │   ├── tenant-boundary-model.md
    │   ├── cross-tenant-failure-modes.md
    │   ├── tenant-scope-validation.md
    │   └── tenant-isolation-audit-requirements.md
    │
    ├── tool-access/
    │   ├── README.md
    │   ├── tool-access-model.md
    │   ├── tool-registration-requirements.md
    │   ├── restricted-tool-patterns.md
    │   └── tool-execution-audit.md
    │
    ├── data-ingestion/
    │   ├── README.md
    │   ├── data-ingestion-model.md
    │   ├── source-system-metadata.md
    │   ├── normalization-and-enrichment.md
    │   ├── ingestion-failure-handling.md
    │   └── ingestion-audit-replay.md
    │
    ├── evidence-traceability/
    │   ├── README.md
    │   ├── evidence-traceability-model.md
    │   ├── evidence-reference-requirements.md
    │   ├── finding-support-requirements.md
    │   ├── dfir-evidence-handling.md
    │   └── evidence-audit-replay.md
    │
    ├── local-llm-dfir/
    │   ├── README.md
    │   ├── local-llm-dfir-model.md
    │   ├── evidence-handling-requirements.md
    │   ├── local-model-output-boundaries.md
    │   ├── dfir-review-approval-requirements.md
    │   └── local-llm-dfir-audit-replay.md
    │
    └── audit-replay/
        ├── README.md
        ├── audit-event-model.md
        ├── replayability-requirements.md
        ├── audit-correlation-model.md
        ├── exception-and-failure-audit.md
        └── immutable-audit-guidance.md
```

## Directory Role Summary

| Directory | Role |
|---|---|
| `architecture/` | Architecture views, principles, assumptions, control loops, and diagrams |
| `patterns/` | Reusable architecture patterns for governed agentic security operations |
| `examples/` | Concrete workflow examples with request, decision, approval, and audit artifacts |
| `service-models/` | Operating models for MSSP, MDR, cloud IR, and private/local LLM-assisted DFIR |
| `threat-model/` | Threat scenarios and risk models for agentic security operations |
| `templates/` | Standard records and reusable documentation templates |
| `governance-library/` | Deep control library for assurance, policy enforcement, identity, oversight, isolation, tooling, ingestion, evidence, local LLM DFIR, and audit replay |

## Governance Library Summary

| Subdirectory | Control Focus |
|---|---|
| `ai-assurance/` | Agent judges, evidence support, output quality, unsupported claims, tenant boundaries, HITL checks, and ATLAS mapping |
| `policy-enforcement/` | PEP/PDP model, policy contracts, risk classification, approval requirements, and fail-closed behavior |
| `agent-governance/` | Agent identity, lifecycle, access scope, communication, monitoring, oversight, and change management |
| `human-oversight/` | Human review model, approval boundaries, customer approval, escalation, and review records |
| `tenant-isolation/` | Tenant boundary model, cross-tenant failure modes, validation, and audit requirements |
| `tool-access/` | Tool access model, registration, restricted tool patterns, and execution audit |
| `data-ingestion/` | Source metadata, normalization, enrichment, failure handling, and ingestion audit replay |
| `evidence-traceability/` | Evidence references, finding support, DFIR evidence handling, and evidence audit replay |
| `local-llm-dfir/` | Local LLM DFIR model, evidence handling, output boundaries, review approval, and audit replay |
| `audit-replay/` | Audit event model, replayability, correlation, exception audit, and immutable audit guidance |

## Examples and Documentation Artifacts

The JSON files under `examples/` are non-runnable documentation artifacts. They show representative shapes of requests, judge outputs, approval records, policy decisions, evidence manifests, timeline outputs, review records, and audit events for architecture discussion.

They are not executable payloads and are not intended to validate runtime behavior.

Runnable request payloads, executable validation examples, tests, schemas, policy examples, KQL queries, and runtime behavior belong in the companion PoC repository.

## Companion Implementation Repo

This architecture can be paired with a separate runnable reference implementation:

```text
agentic-security-operations-control-plane-poc/
```

The companion repo demonstrates selected control-plane concepts using sample code, including schema validation, policy-gated agent actions, PDP/PEP flow, approval checks, audit event generation, and replay-oriented telemetry.

The companion repo is a PoC. It does not replace enterprise identity, SIEM, SOAR, approval, audit, DFIR evidence, customer governance, or production enforcement systems.

## Intended Audience

This repository is intended for:

- MSSP and MDR architects designing governed agentic security operations.
- SOC transformation leaders evaluating agent-assisted workflows.
- Cloud incident response teams designing controlled response patterns.
- DFIR teams evaluating private/local LLM-assisted forensic workflows.
- AI security architects defining assurance, policy, and governance boundaries.
- Governance, risk, compliance, and customer-assurance stakeholders reviewing control models.
- Engineering teams building separate implementations that need architecture and governance alignment.

## Final Repository Principle

This structure keeps the repository focused, navigable, and enforceable.

It separates architecture from patterns, patterns from examples, examples from service models, service models from threat models, templates from governance controls, and governance controls from implementation-specific artifacts.
