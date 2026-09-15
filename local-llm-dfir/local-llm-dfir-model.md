# Local LLM DFIR Model

## Declared Processing Boundary

Every model-assisted task must identify:

- customer or matter and case;
- evidence objects permitted for processing;
- processing purpose and expected output type;
- analysis environment and accountable owner;
- model, runtime, retrieval store, and configuration versions;
- permitted storage and retention;
- allowed and denied egress paths;
- reviewer and release requirements.

## Processing Flow

Authorize case access -> verify evidence manifest and hashes -> create a read-only analysis view -> assemble only approved context -> run the local model -> store output separately -> create lineage -> review source support and limitations -> approve the stated internal use or separate external release -> append audit events.

Original evidence must not be modified, renamed without traceability, embedded into an unscoped shared index, or replaced by a generated summary. A model output that lacks source lineage, case scope, environment identity, or review state fails closed.

## External Controls

The organization must verify filesystem and evidence-store permissions, workload identity, network egress, model and dependency provenance, telemetry behavior, patch/update channels, logging, secure deletion, retention, and backup boundaries. Passing the repository schemas does not prove these controls.

Related controls: `GASO-LLM-001`, `GASO-LLM-003`, `GASO-EVD-001`, `GASO-IDN-002`.
