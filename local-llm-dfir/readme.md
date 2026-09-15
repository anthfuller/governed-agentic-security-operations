# Local LLM-Assisted DFIR

This directory defines governance boundaries for using a private or local model to assist digital-forensics and incident-response work. Local execution reduces some disclosure paths; it does not establish accuracy, evidentiary integrity, or authorization.

## Non-Negotiable Boundaries

- Original evidence remains read only and is referenced by an evidence manifest.
- Model inputs and outputs are bound to an approved customer, case, evidence set, purpose, environment, and time window.
- Network, telemetry, update, retrieval, and support-channel egress is declared and externally enforced.
- Model output is a derived artifact, never original evidence.
- Material findings cite source evidence and receive qualified human review.
- A model, agent, or judge cannot approve investigative conclusions or external release.
- Replay reconstructs recorded activity; it does not rerun the model.

Start with the [`DFIR implementation profile`](../profiles/dfir.yaml), [`evidence manifest`](../templates/evidence-manifest.yaml), and [`derived-artifact lineage record`](../templates/derived-artifact-lineage.yaml).

The repository can validate declared records and lineage. Evidence storage, access control, isolated compute, network enforcement, model supply chain, and legal or forensic process remain organizational responsibilities.

Related controls: `GASO-EVD-001` through `003`, `GASO-LLM-001` through `003`, `GASO-AUD-003`.
