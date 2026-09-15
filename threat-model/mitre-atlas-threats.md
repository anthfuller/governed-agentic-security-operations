# MITRE ATLAS Alignment Method

This file provides a controlled mapping method, not a frozen claim that repository threats match specific external technique identifiers. The external catalog evolves; maintainers must verify names, identifiers, and relationships against the current official MITRE ATLAS source before publishing a versioned mapping.

## Mapping Worksheet

| Repository threat | Candidate ATLAS topic to review | Primary GASO controls |
|---|---|---|
| Prompt injection through operational data | Prompt injection and indirect instruction manipulation | `GASO-ING-001`, `GASO-TOL-002` |
| Retrieval or memory poisoning | Data, knowledge-base, or model-context poisoning | `GASO-ING-001` through `003` |
| Sensitive data disclosure | Model or system information disclosure | `GASO-TEN-003`, `GASO-LLM-003` |
| Tool and agent misuse | Agent, plugin, or external-tool abuse | `GASO-TOL-001` through `003` |
| Model or package supply-chain compromise | Model, dependency, or artifact compromise | `GASO-FLT-001`, `GASO-FLT-002` |
| Evasion and unsafe output | Guardrail, policy, or output-control evasion | `GASO-POL-002`, `GASO-ASR-002` |

## Acceptance Rule

For every published mapping, record the external catalog version or retrieval date, official technique identifier and name, architecture threat, applicability rationale, preventive and detective controls, test evidence, owner, and review date. Remove or mark stale mappings when the external source changes.

ATLAS alignment does not prove mitigation. Each mapped GASO control still requires implementation and test evidence.
