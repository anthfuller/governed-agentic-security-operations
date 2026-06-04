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
- Better examples using synthetic data
- Corrections to terminology, structure, or broken links
- Improvements to readability, consistency, and navigation
- Additional architecture patterns that align with the repository scope

Contributions should remain aligned to the repository purpose: governed agentic security operations with explicit policy enforcement, human accountability, tenant isolation, evidence traceability, auditability, and controlled use of AI-assisted workflows.

## Out of Scope

Do not submit contributions that add:

- Production deployment code
- Real customer data, tenant data, incident data, forensic evidence, or regulated data
- Employer confidential information or non-public implementation details
- Non-public product, service, architecture, roadmap, or operational information
- Vendor-specific endorsement language
- Marketing claims, product claims, or compliance-certification claims
- Autonomous response patterns that bypass policy enforcement, approval, tenant boundaries, or audit requirements
- Instructions for unauthorized access, exploitation, persistence, evasion, credential theft, or destructive activity

Runtime code, tests, schemas, policy execution files, KQL query packs, infrastructure automation, Docker files, CI pipelines, and implementation-specific control-plane code belong in a separate companion implementation or PoC repository, not in this architecture repository.

## Data and Example Requirements

All examples must use synthetic data unless explicitly stated otherwise.

Do not submit:

- Secrets, API keys, tokens, credentials, certificates, private keys, or connection strings
- Real customer names, tenant identifiers, case identifiers, alert identifiers, hostnames, IP addresses, domains, users, or evidence references
- Production logs, incident records, forensic artifacts, or regulated data
- Internal employer, vendor, partner, or customer materials

Use obviously synthetic identifiers such as:

```text
tenant-example-001
customer-example-001
case-example-2026-0001
alert-example-0001
evidence://tenant-example-001/case-example-2026-0001/object-example-0001
```

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

## Pull Request Expectations

Before opening a pull request, confirm that the contribution:

- Uses synthetic data only
- Does not include confidential, proprietary, customer, employer, or regulated information
- Does not imply Microsoft or employer endorsement, sponsorship, approval, or authorship
- Preserves policy enforcement, approval, tenant isolation, evidence, audit, and fail-closed boundaries
- Avoids unnecessary framework, compliance, or marketing language
- Improves the repository without weakening existing control language
- Keeps documentation clear, practical, and architecture-focused
- Updates links, file paths, or directory references if new files are added

## Style Guidelines

Use clear, direct language.

Prefer:

- Specific control requirements
- Concrete architecture boundaries
- Short explanations
- Tables when they improve readability
- If/Then decision rules where enforcement logic matters
- Explicit failure behavior for governed workflows

Avoid:

- Fluff
- Vendor marketing language
- Unsupported claims
- Product endorsements
- Generic compliance filler
- Decorative framework references
- Overstating what the architecture proves or guarantees

## Review and Acceptance

Maintainers may reject or request changes to contributions that:

- Create security, privacy, legal, employment, customer, tenant, or confidentiality risk
- Add unsupported product, vendor, compliance, or security claims
- Weaken governance boundaries
- Add real or sensitive data
- Shift the repository from conceptual architecture into production implementation
- Introduce ambiguity around authorization, approval, tenant isolation, evidence handling, or auditability

Acceptance of a contribution does not imply endorsement by any employer, vendor, customer, standards body, or product provider.

## License

Unless otherwise stated, contributions are submitted under the same license as this repository.

By contributing, you confirm that you have the right to submit the contribution and that it does not contain confidential, proprietary, restricted, or unauthorized material.
