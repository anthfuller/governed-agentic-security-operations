# Changelog

All notable architecture, governance-contract, schema, conformance-tooling, test, and documentation changes to this repository will be recorded in this file.

This repository is a conceptual reference architecture and adoption kit with bounded offline conformance tooling. Changelog entries do not imply a production security product or control plane.

These entries do not represent product releases, service releases, customer guidance, implementation guidance, or official guidance from Microsoft or any other organization.

## 2026-09-15

### Added

- Added a 36-control normative catalog and MSSP, MDR, and DFIR implementation profiles.
- Added JSON Schemas and synthetic templates for governance, approval, policy, tool, evidence, audit, fleet, assurance, recommendation, replay, and decision artifacts.
- Added the deterministic `gaso` CLI for offline schema, scope, policy, evidence, audit-chain, and replay checks.
- Added complete MSSP endpoint-isolation, MDR cloud-IAM, and DFIR local-model timeline walkthrough artifact sets with documented negative cases.
- Added request-digest-bound approvals, validate-only tool records, tamper-evident synthetic audit chains, and deterministic expected replay results.
- Added positive, negative, repository-integrity, link, placeholder, catalog, profile, fleet, and walkthrough tests plus GitHub Actions CI.
- Added adoption and architecture-to-control traceability guidance.

### Changed

- Completed every placeholder file and repaired case-sensitive internal links.
- Repositioned the repository from documentation-only scaffolding to a non-production adoption kit with bounded offline validation.
- Removed stale fixed inventory counts and statements requiring schemas, tests, or validation to live in another repository.
- Clarified throughout that `ALLOW` is a conformance result and never external action execution.

## 2026-06-03

### Added

- Added `Architecture Views` section to the root `README.md`.
- Added core architecture view navigation for:
  - Executive View
  - Engineering View
  - Layered Architecture View
- Added cross-cutting capability view navigation for:
  - Governed Agentic MSSP / MDR Fleet Operations
  - Agentic Fleet Control Loop
- Added governed agentic MSSP / MDR fleet operations architecture reference.
- Added agentic fleet control loop architecture reference.
- Added Fleet-related architecture, pattern, example, threat-model, service-model, and governance-library references.
- Added updated repository disclaimer.
- Added updated security policy.
- Added updated contributor guidance.

### Changed

- Improved root `README.md` navigation for architecture views, patterns, examples, service models, threat models, templates, and governance-library content.
- Clarified that Fleet Operations is a cross-cutting capability view rather than a replacement for the Executive or Engineering architecture views.
- Clarified that the repository is documentation-first and does not contain production implementation code.
- Strengthened language around tenant isolation, policy enforcement, human approval, evidence traceability, auditability, and fail-closed behavior.
- Improved public-facing repository governance language for contributors and security reporting.

### Notes

- All examples remain synthetic or clearly non-sensitive public test data.
- No production implementation code, customer data, tenant data, employer confidential information, or non-public product information is included.
- This repository remains a conceptual reference architecture and documentation scaffold.
- Views are the author's own.
