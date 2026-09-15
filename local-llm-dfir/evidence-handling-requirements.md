# Evidence Handling Requirements

## Before Processing

- assign stable evidence identifiers;
- record acquisition source, time, custodian, and approved SHA-256 value;
- bind each object to the customer or matter and case;
- verify access purpose and analyst authorization;
- preserve originals in an externally controlled, read-only repository;
- validate the evidence manifest.

## During Processing

- work from a controlled copy or read-only view;
- minimize inputs to the approved purpose;
- prevent cross-case retrieval and undeclared egress;
- record transformations, tools, model/runtime versions, and derived outputs;
- do not overwrite or silently normalize original evidence.

## After Processing

- hash and classify each derived artifact;
- link every derived artifact to source evidence identifiers;
- record reviewer disposition and limitations;
- retain or dispose according to the case policy;
- record access and release events in the audit chain.

Run `gaso verify-evidence-manifest <manifest> [--lineage <record> ...]` to check record structure, identifiers, scope, and lineage. It does not access or hash the external evidence object; the listed digest and custody process must be independently verified.

Related controls: `GASO-EVD-001`, `GASO-EVD-002`, `GASO-EVD-003`, `GASO-LLM-001`.
