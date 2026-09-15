# Tenant Isolation

Tenant isolation is an end-to-end invariant, not only a database configuration. Customer, tenant, case, incident, evidence, retrieval, approval, tool, output, and audit scope must remain attributable through every handoff.

## Rules

- Bind every governed artifact to all applicable scope identifiers.
- Carry the same scope through ingestion, retrieval, recommendation, policy, approval, tool request, result, and audit.
- Compare scope values exactly; do not infer or silently translate missing identifiers.
- Deny unresolved mismatches and record the conflicting values without exposing unrelated tenant data.
- Keep credentials, memory, indexes, caches, queues, and output destinations tenant aware.
- Test both positive and negative cross-scope fixtures.

Run `gaso verify-tenant-scope <artifact> [<artifact> ...]` for offline record comparison. This check does not prove production storage, identity, network, or target-tool isolation; those controls require external verification.

See [`tenant-boundary-model.md`](tenant-boundary-model.md), [`tenant-scope-validation.md`](tenant-scope-validation.md), and [`cross-tenant-failure-modes.md`](cross-tenant-failure-modes.md).

Related controls: `GASO-TEN-001`, `GASO-TEN-002`, `GASO-TEN-003`, `GASO-ASR-003`.
