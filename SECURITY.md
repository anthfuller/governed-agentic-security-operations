# Security Policy

## Supported Scope

This repository contains conceptual reference architecture, documentation, templates, examples, diagrams, and synthetic sample data.

This repository is not production software, a deployable security product, a managed service, a SOC automation platform, a DFIR evidence system, or an implementation of an agentic security control plane.

Because this repository is documentation-first, traditional software vulnerability support does not apply in the same way it would for production code.

## Security Issue Reporting

Do not open a public GitHub issue, pull request, discussion, or comment containing:

- Secrets, API keys, tokens, credentials, certificates, private keys, or connection strings
- Customer data, tenant identifiers, case data, incident data, forensic evidence, regulated data, or confidential material
- Exploitable implementation details
- Sensitive vulnerability details affecting a real system, vendor, customer, employer, or production environment
- Non-public product, service, architecture, or operational information

If you identify a concern involving a real system, product, service, customer environment, employer environment, or regulated data, report it through the appropriate authorized security intake process for that organization.

This repository is not an intake path for third-party product vulnerabilities, customer incidents, employer security issues, or live operational findings.

If you identify a repository-specific concern, such as accidental secret exposure, unsafe sample data, or documentation that could create security confusion, report it privately through GitHub private vulnerability reporting if enabled, or through the maintainer-approved private contact path listed for the repository.

## Data Handling Requirements

Contributors and users must not commit, submit, upload, or reference:

- Secrets, API keys, tokens, credentials, certificates, private keys, or connection strings
- Customer data, tenant data, production logs, incident data, forensic evidence, or regulated data
- Employer confidential information or non-public implementation details
- Proprietary detection logic, response procedures, service documentation, or internal operational material
- Real user, customer, tenant, host, IP, domain, case, alert, or evidence identifiers

All examples, alerts, logs, decisions, outputs, policies, schemas, workflows, tenants, customers, users, identifiers, and scenarios must be synthetic or clearly non-sensitive public test data.

## Responsible Use

Agentic security operations must include explicit human accountability, policy enforcement, auditability, tenant isolation, evidence traceability, and fail-closed behavior for sensitive actions.

The examples in this repository must not be treated as production-ready controls.

Any implementation based on these concepts should be reviewed, adapted, tested, and approved by qualified security, legal, privacy, compliance, AI governance, incident response, DFIR, engineering, and operational stakeholders before use.

## Prohibited Content

Do not use this repository to submit, request, or publish:

- Instructions for unauthorized access, exploitation, persistence, evasion, credential theft, or destructive activity
- Real exploit chains against live systems
- Customer-specific security findings or incident details
- Sensitive forensic material or chain-of-custody records
- Confidential employer, vendor, partner, or customer information
- Material that could bypass tenant, customer, evidence, approval, or policy boundaries

High-level defensive threat modeling and architecture discussion are appropriate. Operational abuse instructions, live-target exploitation details, and confidential security material are not.

## Independent Project Notice

This repository is an independent personal project.

It is not created, sponsored, endorsed, reviewed, approved, supported, or maintained by Microsoft or by any current or former employer of the author.

Nothing in this repository represents Microsoft products, Microsoft services, Microsoft architecture guidance, Microsoft security guidance, Microsoft roadmap direction, Microsoft customer guidance, or official statements on behalf of Microsoft.

See [`DISCLAIMER.md`](DISCLAIMER.md) for the full repository disclaimer.

## No Security Warranty

This repository is provided for conceptual architecture discussion only.

It does not guarantee security outcomes, compliance outcomes, forensic validity, incident response correctness, operational safety, or production readiness.
