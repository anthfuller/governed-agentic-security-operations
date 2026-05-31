# Layered Architecture

| Layer | Purpose | Concrete control |
| --- | --- | --- |
| Customer/data source | Source telemetry and target resources | `TenantContext`, `TargetResource` |
| Ingestion/fabric | Normalize and enrich context | evidence/context hashes |
| Agent orchestration | Propose plans and tool calls | typed `PolicyRequest` only |
| AI assurance | Validate agent output before trust | `AssuranceSignals` |
| Governance/control plane | Policy, identity, approvals, audit | PDP/PEP, approvals, ledger |
| Service towers | MSSP, MDR, cloud IR, local DFIR | service-model documents |
| Outcomes | Trust, evidence integrity, scale | replayable decisions |
