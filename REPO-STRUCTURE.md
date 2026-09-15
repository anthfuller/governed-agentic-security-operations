# Repository Structure

The repository is a documentation-first architecture and adoption kit with a bounded executable layer for deterministic, offline conformance checks. File counts are not maintained in prose because they become stale; repository tests discover and validate the current inventory on every run.

## Top-Level Layout

| Path | Responsibility |
|---|---|
| [`README.md`](README.md) | Scope, navigation, installation, and non-production boundary |
| [`ADOPTION-GUIDE.md`](ADOPTION-GUIDE.md) | Profile selection, tailoring, validation, exceptions, and external verification |
| [`TRACEABILITY.md`](TRACEABILITY.md) | Architecture-to-control-to-test and external-dependency mapping |
| [`controls/`](controls/) | Canonical normative control catalog |
| [`profiles/`](profiles/) | MSSP, MDR, and DFIR implementation profiles |
| [`schemas/`](schemas/) | JSON Schemas and artifact-type registry |
| [`templates/`](templates/) | Human-readable guidance and machine-readable synthetic templates |
| [`policies/`](policies/) | Deterministic reference policy fixtures |
| [`src/gaso/`](src/gaso/) | Offline Python CLI and conformance logic |
| [`tests/`](tests/) | Positive, negative, repository-integrity, and walkthrough tests |
| [`.github/workflows/`](.github/workflows/) | CI running the documented offline test path |
| [`walkthroughs/`](walkthroughs/) | MSSP, MDR, and DFIR scenario guidance and complete synthetic artifact sets |
| [`architecture/`](architecture/) | Conceptual executive, engineering, layered, control-loop, and fleet views |
| [`patterns/`](patterns/) | Reusable governance patterns |
| [`examples/`](examples/) | Legacy synthetic scenario artifacts migrated under schema validation |
| [`service-models/`](service-models/) | MSSP, MDR, cloud IR, DFIR, and fleet operating boundaries |
| [`threat-model/`](threat-model/) | Misuse, adversarial, supply-chain, tenant, tool, approval, and model risks |
| [`agent-governance/`](agent-governance/) | Identity, lifecycle, access, monitoring, release, rollback, and recall guidance |
| [`policy-enforcement/`](policy-enforcement/) | PDP/PEP separation, risk classes, approval policy, and fail-closed rules |
| [`human-oversight/`](human-oversight/) | Review, approval, customer authority, escalation, and release boundaries |
| [`tenant-isolation/`](tenant-isolation/) | End-to-end scope model, validation, failure modes, and audit requirements |
| [`tool-access/`](tool-access/) | Registration, contracts, restrictions, scoped requests, and audit |
| [`data-ingestion/`](data-ingestion/) | Provenance, normalization, quarantine, and ingestion replay |
| [`evidence-traceability/`](evidence-traceability/) | Evidence references, support, lineage, and DFIR handling |
| [`local-llm-dfir/`](local-llm-dfir/) | Private/local-model case, evidence, egress, review, and replay boundaries |
| [`audit-replay/`](audit-replay/) | Event model, integrity, correlation, failures, and replay requirements |
| [`governance-library/ai-assurance/`](governance-library/ai-assurance/) | Non-authoritative assurance and judge guidance |

## Executable Boundary

The `gaso` package may parse local JSON/YAML/JSONL, validate schemas and semantic invariants, evaluate repository reference policies, compare declared scope, verify evidence lineage, verify the documented audit hash chain, and reconstruct a recorded timeline.

It does not invoke agents or models, contact vendor or customer platforms, acquire evidence, make production authorization decisions, execute tool actions, deploy fleet releases, or prove production enforcement.

## Machine-Readable Inventory

[`schemas/index.json`](schemas/index.json) is the artifact-type registry. The schema test discovers controls, profiles, templates, policies, examples, and walkthrough artifacts and requires every declared `artifact_type` to resolve and validate. JSON/YAML/JSONL parsing and Markdown link resolution are independently tested.

## Walkthrough Artifact Layout

```text
walkthroughs/artifacts/
├── mssp-endpoint-isolation/
├── mdr-cloud-iam-compromise/
└── dfir-local-llm-timeline/
```

Each set contains applicable evidence or lineage, recommendation or derived output, assurance limitations, policy, request, decision, approval, tool contract, validate-only tool request, `not_executed` result, hash-chained audit events, and expected deterministic replay.

## Validation

```bash
python -m pip install -e ".[dev]"
pytest
```

The same offline test suite runs in GitHub Actions. See [`ADOPTION-GUIDE.md`](ADOPTION-GUIDE.md) for command-level use and [`TRACEABILITY.md`](TRACEABILITY.md) for control coverage.
