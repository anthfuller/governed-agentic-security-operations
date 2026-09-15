# Governance Artifact Templates

These templates create local, synthetic governance records that can be validated by `gaso`. They are reference contracts, not production authorizations or substitutes for an organization's identity, approval, policy, evidence, or audit systems.

| Artifact | Human guidance | Machine template | Schema |
|---|---|---|---|
| Agent card | [`agent-card-template.md`](agent-card-template.md) | [`agent-card.yaml`](agent-card.yaml) | [`../schemas/agent-card.schema.json`](../schemas/agent-card.schema.json) |
| Human approval | [`human-approval-record-template.md`](human-approval-record-template.md) | [`human-approval-record.yaml`](human-approval-record.yaml) | [`../schemas/approval-record.schema.json`](../schemas/approval-record.schema.json) |
| Customer approval | [`customer-approval-record-template.md`](customer-approval-record-template.md) | [`customer-approval-record.yaml`](customer-approval-record.yaml) | [`../schemas/approval-record.schema.json`](../schemas/approval-record.schema.json) |
| Policy decision | [`policy-decision-record-template.md`](policy-decision-record-template.md) | [`policy-decision-record.yaml`](policy-decision-record.yaml) | [`../schemas/policy-decision.schema.json`](../schemas/policy-decision.schema.json) |
| Tool contract | [`tool-contract-template.md`](tool-contract-template.md) | [`tool-contract.yaml`](tool-contract.yaml) | [`../schemas/tool-contract.schema.json`](../schemas/tool-contract.schema.json) |
| Evidence manifest | [`evidence-manifest-template.md`](evidence-manifest-template.md) | [`evidence-manifest.yaml`](evidence-manifest.yaml) | [`../schemas/evidence-manifest.schema.json`](../schemas/evidence-manifest.schema.json) |
| Audit event | [`audit-event-template.md`](audit-event-template.md) | [`audit-event.yaml`](audit-event.yaml) | [`../schemas/audit-event.schema.json`](../schemas/audit-event.schema.json) |
| Assurance result | [`judge-output-template.md`](judge-output-template.md) | [`assurance-result.yaml`](assurance-result.yaml) | [`../schemas/assurance-result.schema.json`](../schemas/assurance-result.schema.json) |
| Architecture decision | [`adr-template.md`](adr-template.md) | [`architecture-decision.yaml`](architecture-decision.yaml) | [`../schemas/adr.schema.json`](../schemas/adr.schema.json) |
| Security recommendation | — | [`security-recommendation.yaml`](security-recommendation.yaml) | [`../schemas/recommendation.schema.json`](../schemas/recommendation.schema.json) |
| Derived-artifact lineage | [`evidence-manifest-template.md`](evidence-manifest-template.md) | [`derived-artifact-lineage.yaml`](derived-artifact-lineage.yaml) | [`../schemas/derived-artifact.schema.json`](../schemas/derived-artifact.schema.json) |
| Tool execution request/result | [`tool-contract-template.md`](tool-contract-template.md) | [`tool-execution-request.yaml`](tool-execution-request.yaml), [`tool-execution-result.yaml`](tool-execution-result.yaml) | [`../schemas/tool-execution.schema.json`](../schemas/tool-execution.schema.json) |
| Fleet release/recall | [`adr-template.md`](adr-template.md) | [`fleet-release-manifest.yaml`](fleet-release-manifest.yaml), [`fleet-recall-record.yaml`](fleet-recall-record.yaml) | [`../schemas/fleet-record.schema.json`](../schemas/fleet-record.schema.json) |

All machine templates use synthetic identifiers and are validated by the test suite.

## Rules

- Replace every `example-*` value before adopting a record.
- Keep approval, policy, and scope identifiers exact across correlated artifacts.
- Do not put secrets or real customer, tenant, case, incident, or evidence data in this repository.
- Validation proves conformance with the published contract only; it does not prove external enforcement or factual correctness.
