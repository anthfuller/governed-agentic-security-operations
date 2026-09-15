# MSSP Agent Fleet Operating Model

This model applies the [`MSSP implementation profile`](../profiles/mssp.yaml) to a multi-customer managed service. It is a governance contract, not a deployment topology.

## Accountabilities

| Role | Accountable for |
|---|---|
| Service governance owner | Control baseline, exceptions, residual risk |
| Tenant service owner | Customer scope, contract boundaries, tenant eligibility |
| Fleet owner | Release provenance, staged rollout, rollback, recall |
| Policy and enforcement owner | Policy versions and effective production enforcement |
| SOC analyst | Evidence review and escalation |
| Customer approver | Customer-impacting authorization where required |

## Operating Rules

- Customer and tenant identifiers are mandatory from ingestion through audit.
- Tenant-specific data, approvals, credentials, memory, and tool targets remain isolated.
- A fleet release declares eligible profiles and tenants; assignment is deny by default.
- Raw customer data is never propagated as fleet intelligence. Shared improvements require sanitization, provenance, review, release approval, and rollback.
- Agent recommendations and assurance results cannot authorize actions.
- Sensitive actions require an exact policy decision, required approvals, and external PEP enforcement.

## Lifecycle

Register and validate -> canary to explicitly eligible tenants -> evaluate declared thresholds -> promote by recorded gate -> monitor by release and tenant -> pause, rollback, or recall on threshold breach.

Required evidence includes agent cards, tool contracts, policy decisions, approval records, fleet release/recall records, and correlated audit events. Production operation additionally requires an identity provider, tenant-aware data plane, approval system, PEP, deployment system, and durable audit store.

Related controls: `GASO-TEN-001` through `003`, `GASO-FLT-001` through `003`, `GASO-POL-001`, `GASO-TOL-002`.
