# Tenant Isolation Audit Requirements

Audit records must make both successful boundary enforcement and attempted violations reconstructable.

## Minimum Record

Each governed event records:

- stable event and correlation identifiers;
- actor identity, type, and accountable owner where applicable;
- customer, tenant, case or incident, and target scope;
- action and lifecycle stage;
- referenced request, policy decision, approvals, evidence, and tool records;
- result, reason code, and timestamp;
- previous-event hash and event hash for ordered fixtures.

For a mismatch, record the affected dimension and safe references to expected and received values. Do not copy another tenant's sensitive content into the denial event.

## Retention and Access

Production audit storage must enforce tenant-aware access, retention, immutability or tamper evidence, time synchronization, and monitored export. These properties are external to this repository. The included CLI verifies the documented fixture hash chain and reconstructs a replay without invoking external systems.

Related controls: `GASO-TEN-003`, `GASO-AUD-001`, `GASO-AUD-002`, `GASO-AUD-003`.
