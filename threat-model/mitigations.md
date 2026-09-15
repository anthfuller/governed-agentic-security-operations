# Threat Mitigation Catalog

| Threat surface | Prevent | Detect | Contain or recover |
|---|---|---|---|
| Prompt injection | Separate instructions and untrusted data; mediate tools | Unexpected actions, unsupported claims, policy denials | Quarantine input and derived output; review affected decisions |
| Cross-tenant access | Exact scope binding and external isolation | Scope mismatch and negative tests | Deny, revoke unsafe artifacts, investigate correlation chain |
| Poisoned retrieval | Provenance, trust, integrity, scoped ingestion | Conflicting or revoked sources, drift | Quarantine source, re-index, re-evaluate dependents |
| Tool misuse | Registered contract, PDP decision, PEP enforcement | Parameter mismatch, replay, unusual target | Block credentials or operation; verify side effects |
| Approval abuse | Authenticated, exact, expiring approval | Reuse, mismatch, abnormal approval patterns | Revoke decision, stop action, require new approval |
| Compromised identity | Distinct least-privilege identity | Lifecycle and behavioral monitoring | Revoke credentials and active assignments |
| Fleet poisoning | Provenance, integrity, separation of duties, staging | Drift, threshold breach, tenant anomalies | Pause, rollback, recall, revoke release |
| Local-model leakage | Declared environment and enforced egress | Network and telemetry testing | Isolate environment, preserve records, assess exposure |
| Unsupported conclusions | Source lineage and qualified review | Assurance and reviewer disagreement | Reject or relabel output; obtain more evidence |
| Audit tampering | Durable external storage and hash-linked records | Chain verification and gap detection | Fail closed, preserve copies, investigate missing events |

## Priority Order

Implement hard boundaries first: identity, tenant scope, policy, approval, tool enforcement, evidence integrity, and audit. Advisory assurance improves detection but cannot replace those controls.

Every mitigation must have an owner, enforcement location, observable evidence, negative test, failure response, and review cadence. Controls implemented only as prompt instructions are not sufficient for authorization or tenant isolation.
