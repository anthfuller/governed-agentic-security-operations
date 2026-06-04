# Contributor Guidelines

Thank you for your interest in contributing to this repository.

This repository is a conceptual reference architecture and documentation scaffold for governed agentic security operations across MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

It is documentation-first. Contributions should strengthen architecture clarity, governance boundaries, operating-model usefulness, threat-model accuracy, reusable templates, or control-surface completeness.

## Independent Project Notice

This repository is an independent personal project.

It is not created, sponsored, endorsed, reviewed, approved, supported, or maintained by Microsoft Corporation, its affiliates, or any current or former employer of the author.

Contributions must not imply that this repository represents Microsoft products, Microsoft services, Microsoft architecture guidance, Microsoft security guidance, Microsoft roadmap direction, Microsoft customer guidance, or official statements on behalf of Microsoft or any other organization.

## Contribution Scope

Good contributions may include:

- Clearer architecture explanations
- Better diagrams or diagram descriptions
- Improved threat-model coverage
- Stronger policy, approval, audit, evidence, tenant-isolation, or fail-closed control language
- Better examples using synthetic data or clearly non-sensitive public test data
- Corrections to terminology, structure, spelling, formatting, or broken links
- Improvements to readability, consistency, and navigation
- Additional architecture patterns that align with the repository scope
- Additional governance-library controls that preserve policy, tenant, evidence, approval, and audit boundaries
- Additional synthetic example records that improve architecture discussion without becoming runtime payloads

Contributions should remain aligned to the repository purpose: governed agentic security operations with explicit policy enforcement, human accountability, tenant isolation, evidence traceability, auditability, and controlled use of AI-assisted workflows.

## Out of Scope

Do not submit contributions that add:

- Production deployment code
- Runtime source code
- CI/CD workflows
- Docker files
- Infrastructure-as-code deployment artifacts
- Real customer data, tenant data, incident data, forensic evidence, or regulated data
- Employer confidential information or non-public implementation details
- Non-public product, service, architecture, roadmap, or operational information
- Vendor-specific endorsement language
- Marketing claims, product claims, or compliance-certification claims
- Autonomous response patterns that bypass policy enforcement, approval, tenant boundaries, or audit requirements
- Instructions for unauthorized access, exploitation, persistence, evasion, credential theft, or destructive activity
- Live exploit chains against real systems
- Customer-specific security findings or incident details
- Sensitive forensic material or chain-of-custody records
- Confidential employer, vendor, partner, or customer information

Runtime code, tests, schemas, policy execution files, KQL query packs, infrastructure automation, Docker files, CI pipelines, and implementation-specific control-plane code belong in a separate companion implementation or PoC repository, not in this architecture repository.

## Data and Example Requirements

All examples must use synthetic data or clearly non-sensitive public test data.

Do not submit, upload, reference, or embed:

- Secrets, API keys, tokens, credentials, certificates, private keys, or connection strings
- Real customer names, tenant identifiers, case identifiers, alert identifiers, hostnames, IP addresses, domains, users, or evidence references
- Production logs, incident records, forensic artifacts, telemetry exports, packet captures, or regulated data
- Internal employer, vendor, partner, or customer materials
- Proprietary detection logic, response procedures, service documentation, or internal operational material
- Material copied from private tickets, private chats, private incidents, customer cases, internal service documentation, or restricted repositories

Use obviously synthetic identifiers such as:

```text
tenant-example-001
customer-example-001
case-example-2026-0001
alert-example-0001
user-example-001
host-example-001
ip-example-192-0-2-10
domain-example.test
evidence://tenant-example-001/case-example-2026-0001/object-example-0001
```

When examples need realistic structure, prefer synthetic fields and clearly fake values over redacted real data.

## AI-Assisted Contributions

AI-assisted contributions are allowed, but contributors are responsible for reviewing, validating, and editing the contribution before submission.

AI-assisted content must not include confidential, proprietary, customer, employer, regulated, or non-public information.

AI-generated text, examples, diagrams, or templates must still follow all repository boundaries, licensing requirements, attribution requirements, synthetic-data requirements, and security-content restrictions.

Do not submit AI-generated material that:

- Invents unsupported claims
- Implies product functionality that does not exist
- Suggests production readiness
- Weakens policy, approval, tenant, evidence, or audit boundaries
- Introduces unsafe security instructions
- Copies protected or restricted content from another source

## Architecture Boundaries to Preserve

Contributions must preserve the following governance boundaries:

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

## Fleet Operations Boundaries to Preserve

Contributions involving governed agent fleets, fleet updates, shared intelligence, or cross-tenant propagation must preserve the following boundaries:

- Raw customer data does not leave the tenant boundary.
- Shared intelligence must be sanitized, validated, approved, and versioned before release.
- Fleet updates must preserve tenant eligibility, policy-scoped distribution, rollout controls, rollback, recall, and auditability.
- Agent packages, prompts, playbooks, detection bundles, and policy bundles should be traceable to versioned release records.
- Emergency recall, token/session revocation, rollback, and last-known-good recovery must remain explicit controls.
- Cross-tenant pattern generalization must not expose customer identifiers, sensitive evidence, case-specific details, regulated data, or proprietary customer context.
- Sanitized intelligence is not original evidence.
- Fleet-wide improvement does not override tenant isolation, customer approval boundaries, or release gates.

## Security and Sensitive Content

Do not report sensitive security concerns, secret exposure, customer data exposure, or real vulnerability details through public issues, pull requests, comments, or discussions.

Use the private reporting path described in [`SECURITY.md`](SECURITY.md).

Public contribution channels must not contain:

- Secrets, credentials, tokens, keys, or certificates
- Customer data or tenant identifiers
- Real incident data or forensic evidence
- Exploitable implementation details
- Non-public product, service, architecture, or operational information
- Material that could bypass tenant, customer, evidence, approval, or policy boundaries

High-level defensive threat modeling and architecture discussion are appropriate. Operational abuse instructions, live-target exploitation details, and confidential security material are not.

## Pull Request Expectations

Before opening a pull request, confirm that the contribution:

- Uses synthetic data or clearly non-sensitive public test data
- Does not include confidential, proprietary, customer, employer, or regulated information
- Does not imply Microsoft or employer endorsement, sponsorship, approval, review, maintenance, or authorship
- Preserves policy enforcement, approval, tenant isolation, evidence, audit, and fail-closed boundaries
- Avoids unnecessary framework, compliance, or marketing language
- Improves the repository without weakening existing control language
- Keeps documentation clear, practical, and architecture-focused
- Updates links, file paths, diagrams, directory references, or README files if new files are added
- Does not shift this repository from conceptual architecture into production implementation
- Does not add unsupported claims about security outcomes, compliance outcomes, production readiness, forensic validity, or operational safety

For large structural changes, new architecture views, new control areas, new example families, new threat-model categories, or new governance-library sections, open an issue or discussion first so the scope can be reviewed before a pull request is created.

Pull requests should be focused and reviewable. Avoid combining unrelated architecture, threat-model, template, diagram, and formatting changes in one pull request.

If a contribution adds, removes, or renames files, update any affected README files, directory references, diagram links, repository-structure documentation, and navigation tables.

## Style Guidelines

Use clear, direct language.

Prefer:

- Specific control requirements
- Concrete architecture boundaries
- Short explanations
- Tables when they improve readability
- If/Then decision rules where enforcement logic matters
- Explicit failure behavior for governed workflows
- Consistent terminology for policy, approval, tenant, evidence, audit, and fleet controls
- Relative links for repository files and diagrams

Avoid:

- Fluff
- Vendor marketing language
- Unsupported claims
- Product endorsements
- Generic compliance filler
- Decorative framework references
- Overstating what the architecture proves or guarantees
- Language that implies autonomous agents can approve or authorize their own actions
- Language that implies conceptual examples are production-ready controls

Use lowercase kebab-case for new Markdown file names where practical.

Examples:

```text
tenant-boundary-model.md
fleet-update-authorization-and-policy-gates.md
shared-intelligence-sanitization-and-release-controls.md
emergency-agent-recall-and-kill-switch.md
```

Diagrams should avoid:

- Vendor logos
- Employer branding
- Product screenshots
- Customer identifiers
- Real case data
- Decorative framework references
- Visual elements that imply sponsorship, endorsement, or official guidance

Diagram text should be spell-checked before submission, especially:

- Control labels
- Risk labels
- Rule banners
- Architecture titles
- Tenant-boundary language
- Rollout and recall labels
- Audit and evidence labels

## Documentation Link Hygiene

When adding or changing Markdown files:

- Use relative links for repository-local references.
- Verify image paths.
- Verify links to templates, examples, governance-library files, and architecture views.
- Keep diagram names aligned with the referenced Markdown files.
- Avoid linking to private, internal, or access-restricted sources.
- Avoid stale links to renamed files.

## Review and Acceptance

Maintainers may reject or request changes to contributions that:

- Create security, privacy, legal, employment, customer, tenant, or confidentiality risk
- Add unsupported product, vendor, compliance, or security claims
- Weaken governance boundaries
- Add real or sensitive data
- Shift the repository from conceptual architecture into production implementation
- Introduce ambiguity around authorization, approval, tenant isolation, evidence handling, or auditability
- Add unsafe operational security instructions
- Create confusion about Microsoft, employer, vendor, customer, or standards-body endorsement
- Make the repository harder to navigate or review

Acceptance of a contribution does not imply endorsement by any employer, vendor, customer, standards body, product provider, or other organization.

## License

Unless otherwise stated, contributions are submitted under the same license as this repository.

By contributing, you confirm that you have the right to submit the contribution and that it does not contain confidential, proprietary, restricted, sensitive, regulated, or unauthorized material.

## Maintainer Note

This repository is intended to remain a conceptual reference architecture and documentation scaffold.

The goal is to improve the quality, clarity, and usefulness of the architecture without turning this repository into a production system, product claim, implementation guide, or vendor-specific reference.
