# Tenant-Safe Fleet Intelligence Propagation Pattern

Fleet learning must propagate a reviewed improvement, not another customer's data.

## Allowed Propagation

Examples include a versioned detection rule, sanitized behavioral pattern, control improvement, parser fix, or policy change. Each item must have an owner, source provenance, classification, sanitization record, target profiles, validation results, approval, version, and rollback path.

## Prohibited Propagation

- raw alerts, logs, evidence, tickets, case notes, identifiers, or credentials;
- customer-specific embeddings, prompts, memory, or summaries;
- conclusions whose provenance or licensing cannot be established;
- content whose tenant attribution cannot be removed and verified;
- an improvement automatically learned and released by the same component.

## Gate

Extract candidate -> classify and sanitize -> verify no customer-specific content -> test against synthetic or authorized fixtures -> review operational effect -> authorize release -> stage rollout -> monitor and retain rollback.

Any failed provenance, classification, sanitization, tenant-isolation, or approval check blocks release. The production data-loss-prevention, package distribution, and deployment mechanisms are external dependencies.

Related controls: `GASO-TEN-003`, `GASO-GOV-003`, `GASO-FLT-001`, `GASO-FLT-002`, `GASO-ING-001`.
