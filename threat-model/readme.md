# Finalized Threat Model Directory Structure

## Status

The updated `threat-model/` directory structure is locked in.

The `README.md` file is the authoritative source for this directory structure and its deduplication decisions.

Files such as `threat-model-overview.md`, `tool-misuse.md`, and `cross-tenant-data-leakage.md` should **not** be created as separate files because they would duplicate stronger existing or planned files and increase documentation drift risk.

## Finalized `threat-model/` Directory Structure

```text
threat-model/
├── README.md
├── agentic-security-operations-threat-model.md
├── mitre-atlas-threats.md
├── prompt-injection-through-logs.md
├── rag-memory-contamination.md
├── rag-poisoning.md
├── cross-tenant-cross-customer-risk.md
├── tool-use-and-automation-risk.md
├── malicious-tool-output.md
├── human-approval-and-release-risk.md
├── overreliance-on-ai.md
├── compromised-agent-identity.md
├── rogue-agent-risk.md
├── local-llm-dfir-risk.md
└── mitigations.md
```

## Why This Is the Correct Structure

### Prevented Overlap

`threat-model-overview.md` is intentionally excluded because the overview function is already covered by:

- `README.md`
- `agentic-security-operations-threat-model.md`

`tool-misuse.md` is intentionally excluded because it is covered by:

- `tool-use-and-automation-risk.md`

`cross-tenant-data-leakage.md` is intentionally excluded because it is covered by:

- `cross-tenant-cross-customer-risk.md`

This avoids redundant files, inconsistent updates, and competing ownership across the threat-model directory.

### Operational Clarity

The structure maps specific threat areas to concrete architecture control surfaces:

- PDP / PEP enforcement
- Agent Judge assurance
- human approval and release gates
- tenant, customer, case, workflow, and evidence boundaries
- RAG, vector search, memory, and retrieved-context controls
- tool and automation boundaries
- agent identity and rogue-agent governance
- private/local LLM-assisted DFIR evidence controls

### Audit and Review Readiness

This directory is ready to populate and review against the existing `examples/`, `patterns/`, and architecture files.

For example:

- `rag-poisoning.md` should inform and validate `tenant-safe-rag-memory-pattern.md`.
- `tool-use-and-automation-risk.md` should align with `policy-enforced-tool-use-pattern.md`.
- `human-approval-and-release-risk.md` should align with `human-approved-sensitive-action-pattern.md`.
- `local-llm-dfir-risk.md` should align with private/local LLM-assisted DFIR examples and evidence-handling requirements.
- `compromised-agent-identity.md` and `rogue-agent-risk.md` should align with the Agent Governance and Identity Control Plane.

## Next Recommended File

The next file to build should be:

```text
threat-model/agentic-security-operations-threat-model.md
```

This should become the core anchor threat model for the directory.

It should define the primary architecture-wide threats, cross-layer trust boundaries, deny/fail-closed paths, control-surface mappings, audit requirements, and acceptance criteria for governed Agentic MSSP / MDR / DFIR Security Operations.

## Final Recommendation

Leave the finalized directory structure as-is.

Do not add duplicate overview or narrow alias files unless a future file introduces a clearly distinct threat surface, control surface, or review responsibility that is not already covered by the current structure.
