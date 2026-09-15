# DFIR Review and Approval Requirements

Review establishes whether model-assisted material is fit for a stated investigative use. Approval authorizes a bounded use or release. They must be separate records when both are required.

## Reviewer Checks

- identity, case, evidence, environment, and purpose match;
- cited source objects exist in the manifest;
- material claims are supported by those sources;
- timestamps, normalization, and time-zone assumptions are documented;
- contrary evidence and uncertainty are visible;
- output is labeled derived and has complete lineage;
- no undeclared customer, case, or external context appears;
- limitations are suitable for the intended audience.

The reviewer records `reviewed`, `rejected`, or `more_evidence_required`; lack of response is not acceptance.

## Separate Approval Triggers

Require a separately authorized record for external report release, customer notification, privileged or sensitive evidence access, material processing-purpose change, case transfer, retention exception, or any action against a live system.

An approval must bind the exact artifact version, intended use, audience, case, conditions, and expiration. A changed artifact or audience requires new approval. No repository check substitutes for the organization's legal, evidentiary, or customer obligations.

Related controls: `GASO-APR-001`, `GASO-APR-002`, `GASO-EVD-003`, `GASO-LLM-002`.
