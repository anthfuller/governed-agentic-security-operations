# Local LLM DFIR Audit and Replay

Replay reconstructs the recorded analysis path without reprocessing evidence or rerunning a nondeterministic model.

## Required References

The correlated event set should identify the case and environment; evidence manifest and object IDs; actor and model/runtime versions; retrieval or context references; derived artifacts and hashes; review and approval records; policy decisions; output destination; and final disposition.

Do not place raw evidence, prompts containing sensitive evidence, or unrestricted model output in a general audit record. Store protected artifacts in their controlled repositories and audit stable references plus integrity values.

## Replay Procedure

1. Authorize the reviewer for the case.
2. Verify event structure and the documented hash chain.
3. Confirm scope consistency across correlated records.
4. Order events and resolve referenced versions and integrity values.
5. Reconstruct what was available, produced, reviewed, approved, and released.
6. Report missing references or chain failures; do not infer the missing state.

Use `gaso verify-audit-chain <events.jsonl>` and `gaso replay <events.jsonl>`. A passing offline result shows internal consistency of the supplied fixture, not immutability of a production audit store.

Related controls: `GASO-AUD-001`, `GASO-AUD-002`, `GASO-AUD-003`, `GASO-LLM-002`.
