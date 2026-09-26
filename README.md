# Governed Agentic Security Operations Architecture

An implementation-oriented governance and adoption kit for MSSP, MDR, and DFIR teams designing agent-assisted security workflows with explicit scope, policy, approval, evidence, audit, and replay boundaries.

> **Independent project:** This is an independent personal reference architecture and adoption kit. It is not affiliated with, sponsored by, endorsed by, reviewed by, approved by, or maintained by Microsoft or any other employer. See [`DISCLAIMER.md`](DISCLAIMER.md).

> Agentic systems may assist security operations, but they do not authorize themselves.

## At a Glance

- 36-control normative governance catalog
- MSSP, MDR, and DFIR implementation profiles
- Deterministic `gaso` offline conformance CLI
- Schema-governed requests, approvals, decisions, evidence, and audit records
- AI Assurance and Agent Judge patterns for evidence support, unsupported claims, tenant boundaries, HITL compliance, output quality, and ATT&CK/ATLAS mapping
- Request-digest-bound approvals
- Tenant, customer, case, and target-scope validation
- Hash-chained audit-record verification and deterministic replay
- 56 automated tests
- Three end-to-end walkthroughs

## What This Demonstrates

- Governed agentic security architecture
- Translation of governance requirements into machine-readable contracts
- Deterministic policy and approval validation
- Tenant-scope-aware MSSP, MDR, and DFIR operating models
- Evidence lineage, auditability, and replay
- Separation of Agent Judge assurance from PDP authorization, PEP enforcement, and human approval
- Clear separation between offline conformance validation and external production enforcement

## Relationship to F7-LAS

This repository applies the [F7-LAS™ framework](https://github.com/anthfuller/F7-LAS) as a supporting control lens for governed agentic security operations. The current framework publication is the [F7-LAS Whitepaper v4.1 — Restored Full Edition](https://github.com/anthfuller/F7-LAS/blob/main/docs/whitepaper/F7-LAS-Whitepaper-v4.1-Restored-Full-Edition.pdf). F7-LAS does not replace the MSSP, MDR, or DFIR operating model, tenant isolation, policy enforcement, human oversight, or evidence-handling responsibilities defined in this repository.

## Scope Boundary

This repository is not a SOC product, autonomous response platform, production control plane, SIEM/SOAR replacement, legally sufficient DFIR evidence system, or customer-ready managed security service.

The `gaso` CLI validates local, synthetic artifacts and reconstructs recorded audit timelines. It does **not** invoke agents or models, contact security platforms, or execute external actions. Production identity, authorization, policy enforcement, approval authority, tenant isolation, tool mediation, evidence preservation, audit storage, deployment, and response execution remain external implementation responsibilities.

Passing repository validation establishes conformance of supplied artifacts to the checks implemented by this offline kit. It does **not** establish production enforcement, security, compliance, factual correctness, evidentiary validity, or operational safety. See [`TRACEABILITY.md`](TRACEABILITY.md) for the implemented-versus-external boundary.

## 60-Second Technical Review

| Artifact | What it shows |
|---|---|
| [`controls/control-catalog.yaml`](controls/control-catalog.yaml) | The 36 normative controls, accountable roles, evidence expectations, failure behavior, and enforcement boundaries. |
| [`TRACEABILITY.md`](TRACEABILITY.md) | Mapping from architecture components to controls, profiles, schemas, walkthrough evidence, tests, and external dependencies. |
| [`src/gaso/policy.py`](src/gaso/policy.py) | Deterministic policy evaluation, request-digest approval binding, parameter restrictions, scope checks, and retroactive-approval rejection. |
| [`src/gaso/audit.py`](src/gaso/audit.py) | Canonical hashing, audit-chain verification, scope and correlation checks, and deterministic replay. |
| [`tests/test_policy.py`](tests/test_policy.py) | Positive and negative tests for approvals, request mutation, prohibited actions, tools, parameters, scope, and timing. |
| [`walkthroughs/README.md`](walkthroughs/README.md) | MSSP, MDR, and DFIR end-to-end scenarios with synthetic, non-executing artifacts. |

## Architecture Views

The diagrams remain available through their supporting architecture documents:

- [Executive view](architecture/executive-view.md)
- [Engineering view](architecture/engineering-view.md)
- [Shared operating model](architecture/layered-architecture.md)
- [Runtime control loop](architecture/control-loop.md)
- [Agentic fleet operations](architecture/agentic-fleet-architecture.md)

## Quick Start

Choose the path closest to your objective:

| Role or objective | Start here |
|---|---|
| MSSP or MDR architect | [`quick-start/for-mssp-mdr.md`](quick-start/for-mssp-mdr.md) |
| DFIR practitioner | [`quick-start/for-dfir.md`](quick-start/for-dfir.md) |
| Adoption-kit builder | [`quick-start/for-poc-builders.md`](quick-start/for-poc-builders.md) |

### Local Validation

The `gaso` CLI requires Python 3.11 or later and operates on local synthetic artifacts only.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"

gaso validate controls/control-catalog.yaml profiles/mssp.yaml
gaso verify-tenant-scope \
  templates/governed-action-request.yaml \
  templates/human-approval-record.yaml \
  templates/customer-approval-record.yaml
gaso evaluate-policy templates/governed-action-request.yaml \
  --policy policies/endpoint-response-policy.yaml \
  --approvals templates/human-approval-record.yaml templates/customer-approval-record.yaml
gaso verify-evidence-manifest templates/evidence-manifest.yaml \
  --lineage templates/derived-artifact-lineage.yaml
gaso verify-audit-chain tests/fixtures/audit-valid.jsonl
gaso replay tests/fixtures/audit-valid.jsonl
pytest
```

An `ALLOW` result means only that the synthetic request satisfied the selected reference policy. The CLI never invokes the requested action.

## End-to-End Walkthroughs

| Walkthrough | Focus |
|---|---|
| [`MSSP endpoint isolation`](walkthroughs/mssp-endpoint-isolation.md) | Tenant- and target-scoped recommendation, evidence, policy, approvals, validate-only tool records, and replay. |
| [`MDR cloud IAM compromise`](walkthroughs/mdr-cloud-iam-compromise.md) | Cloud identity containment recommendation with request-digest approvals and explicit execution boundaries. |
| [`DFIR local-LLM timeline`](walkthroughs/dfir-local-llm-timeline.md) | Evidence manifest, derived-artifact lineage, human review, and replay without evidentiary claims. |

## Repository Navigation

| Need | Start here |
|---|---|
| Adopt and tailor a profile | [`ADOPTION-GUIDE.md`](ADOPTION-GUIDE.md) |
| Review architecture assumptions and principles | [`architecture/`](architecture/readme.md) |
| Review normative controls | [`controls/`](controls/README.md) |
| Compare MSSP, MDR, and DFIR profiles | [`profiles/`](profiles/README.md) |
| Inspect schemas and templates | [`schemas/`](schemas/index.json) and [`templates/`](templates/readme.md) |
| Review policy and enforcement boundaries | [`policy-enforcement/`](policy-enforcement/readme.md) |
| Review AI assurance and Agent Judge patterns | [`AI Assurance & Analytics`](governance-library/ai-assurance/readme.md) and [`Agent Judges overview`](governance-library/ai-assurance/agent-judges-overview.md) |
| Review threats and failure modes | [`threat-model/`](threat-model/readme.md) |
| Browse the complete repository structure | [`REPO-STRUCTURE.md`](REPO-STRUCTURE.md) |

Architecture, machine-readable contracts, synthetic examples, offline checks, and external production responsibilities remain deliberately separated throughout the repository.
