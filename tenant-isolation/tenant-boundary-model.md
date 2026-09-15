# Tenant Boundary Model

The boundary is the intersection of identity, customer, tenant, case or incident, evidence set, data store, tool target, permitted operation, destination, and validity window.

## Boundary Layers

| Layer | Required binding | External enforcement example |
|---|---|---|
| Identity | actor, service, agent, owner, lifecycle state | identity provider and workload identity |
| Data | customer, tenant, case, evidence object | tenant-aware storage and query filters |
| Retrieval | index or memory namespace, query scope, result scope | retrieval gateway |
| Decision | request, policy version, risk, scope | policy decision point |
| Approval | approver, action, target, scope, expiration | approval service |
| Tool | registered tool, operation, target, parameters | policy enforcement point and target platform |
| Output | audience, customer, classification, purpose | release workflow and destination control |
| Audit | correlation, actor, scope, references, time | durable audit store |

Identifiers are opaque values. Matching must be exact after the documented normalization in the implementation; substring, prefix, similarity, and model-based matching are not acceptable authorization checks.

Missing applicable scope fails closed. Legitimate cross-tenant operations must be modeled as separately authorized scopes with a named owner and purpose, never as an implicit wildcard.

Related controls: `GASO-TEN-001`, `GASO-TEN-002`, `GASO-TEN-003`, `GASO-IDN-002`.
