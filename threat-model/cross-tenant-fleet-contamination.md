# Cross-Tenant Fleet Contamination

Fleet learning or configuration propagation can move one customer's sensitive data, policy, memory, or behavior into another customer's environment.

## Controls

- prohibit raw tenant evidence and identifiers in shared packages;
- separate customer-specific configuration from common components;
- require provenance, classification, sanitization, review, and release approval for shared intelligence;
- test packages for tenant-specific content using organization-approved controls;
- declare eligible profiles and tenants in the release manifest;
- monitor rollout by tenant and retain a bounded recall path.

Unknown source, failed sanitization, tenant-specific material, eligibility mismatch, or missing approval blocks propagation. Do not use an agent's own claim that data is sanitized as the release decision.

When contamination is detected, pause rollout, recall the affected release, revoke unsafe derived artifacts, identify exposed tenant assignments, and handle the event through the organization's incident process.

Related controls: `GASO-TEN-003`, `GASO-FLT-001`, `GASO-FLT-002`, `GASO-ING-001`.
