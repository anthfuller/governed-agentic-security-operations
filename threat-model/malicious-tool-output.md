# Malicious Tool Output

A registered tool can still return compromised, malformed, stale, mis-scoped, or instruction-bearing output.

## Controls

- authenticate the tool endpoint and bind the response to the request;
- validate response schema, content type, size, status, target, tenant, and freshness;
- preserve a safe reference and integrity value for consequential output;
- treat free text as untrusted data, not workflow instructions;
- quarantine unexpected fields and cross-scope objects;
- require source support before tool output becomes a finding or action input;
- distinguish transport success from operation success and verified outcome.

Malformed, unauthenticated, replayed, scope-conflicting, or ambiguous output fails closed. A tool-reported success must not become final status without the contract's required verification and audit event.

Negative tests should cover injected text, schema confusion, oversized responses, old responses, mixed targets, false success, partial completion, and duplicate delivery.

Related controls: `GASO-TOL-001`, `GASO-TOL-003`, `GASO-ING-003`, `GASO-AUD-001`.
