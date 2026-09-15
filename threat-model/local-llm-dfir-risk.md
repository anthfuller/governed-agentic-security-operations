# Local LLM DFIR Risk

Private or local execution can still alter evidence, leak through undeclared channels, mix cases, use compromised model artifacts, and produce unsupported forensic conclusions.

## Controls

- preserve originals externally and process a controlled read-only view;
- bind environment, model, data, case, purpose, storage, telemetry, and egress;
- verify model/runtime provenance and integrity under organizational process;
- disable or govern external retrieval, updates, crash reporting, and support channels;
- classify all model output as derived and record source lineage;
- require qualified review before investigative reliance or report release;
- audit by reference without copying sensitive evidence into a general log.

Unknown evidence scope, missing lineage, undeclared egress, integrity failure, cross-case context, or missing required review fails closed. Local placement alone does not establish chain of custody, correctness, confidentiality, or legal sufficiency.

Related controls: `GASO-LLM-001`, `GASO-LLM-002`, `GASO-LLM-003`, `GASO-EVD-001`.
