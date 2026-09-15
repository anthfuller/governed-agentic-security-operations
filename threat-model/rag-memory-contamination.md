# RAG and Memory Contamination

Retrieved or retained context can be wrong, stale, untrusted, or bound to another customer, tenant, case, purpose, or model session.

## Controls

- namespace data by customer, tenant, case, classification, and permitted use;
- enforce scope before the query and on every returned object;
- record source provenance, freshness, retention, and retrieval identifiers;
- deny persistent memory by default for evidence-sensitive work;
- keep shared knowledge free of raw tenant content;
- invalidate derived artifacts when relied-on context is quarantined or revoked.

A successful query is not evidence of correct scope. The result set must be checked independently. Missing metadata, mixed scope, unknown provenance, or an expired purpose fails closed and emits a bounded audit event.

Test cross-tenant, cross-case, stale, deleted, duplicate, and poisoned objects, plus cache and retry paths that could lose scope.

Related controls: `GASO-TEN-001`, `GASO-TEN-002`, `GASO-TEN-003`, `GASO-ING-003`.
