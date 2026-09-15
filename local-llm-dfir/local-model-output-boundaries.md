# Local Model Output Boundaries

A local model output is derived material with an uncertain relationship to source evidence until a reviewer verifies it.

## Required Classification

Store output separately from originals and record its artifact identifier, case scope, source evidence identifiers, transformation or prompt purpose, producer and versions, integrity value, creation time, and review state. Use [`../templates/derived-artifact-lineage.yaml`](../templates/derived-artifact-lineage.yaml).

## Permitted States

| State | Permitted use |
|---|---|
| Unreviewed | Internal queueing and review only |
| Reviewed | Only the purpose accepted by the reviewer |
| Rejected | Preserve according to policy; do not rely on or release |

Generated summaries, timelines, extracted entities, classifications, hypotheses, and draft findings must cite their source objects. Unsupported statements remain labeled as hypotheses or are removed. Human review cannot transform derived output into original evidence.

External reports require a separate release decision that considers audience, privilege, sensitivity, customer authorization, and applicable investigative procedure. This repository does not determine legal admissibility or forensic sufficiency.

Related controls: `GASO-LLM-002`, `GASO-EVD-002`, `GASO-EVD-003`, `GASO-ASR-002`.
