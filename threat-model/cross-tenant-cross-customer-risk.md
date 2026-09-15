# Cross-Tenant and Cross-Customer Risk

Multi-customer services can disclose data, apply another customer's approval, target the wrong environment, or propagate customer-specific material across the fleet.

## Boundary Requirements

Carry customer, tenant, case or incident, evidence, target, and destination scope through ingestion, retrieval, recommendation, policy, approval, tool request, result, and audit. Validate every transition with exact matching and deny implicit wildcards.

Controls must also cover caches, queues, temporary files, indexes, service credentials, retries, batch jobs, analytics, support access, exports, backups, and error messages. Application-level identifiers do not prove infrastructure isolation.

Any missing or unresolved mismatch blocks retrieval, action, release, and reuse. Record the dimension that failed without copying the foreign customer's sensitive content into the error.

Use cross-scope negative fixtures and verify production identity, storage, network, retrieval, and target-tool enforcement separately.

Related controls: `GASO-TEN-001`, `GASO-TEN-002`, `GASO-TEN-003`, `GASO-ASR-003`.
