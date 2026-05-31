# Architecture Patterns

This directory contains concise architecture patterns for governed Agentic MSSP / MDR / DFIR security operations.

Patterns are intended to help readers understand repeatable design approaches, control boundaries, and workflow decisions without turning this directory into a dense control catalog.

Detailed control requirements belong in [`../governance-library/`](../governance-library/).

---

## Planned Pattern Files

| File | Purpose |
|---|---|
| `governed-agentic-security-operations-pattern.md` | Describes the overall governed agent-assisted SOC, MDR, and DFIR workflow. |
| `policy-enforced-tool-use-pattern.md` | Shows how agent tool use is mediated through authorization decisions, enforcement, obligations, and audit. |
| `human-approved-sensitive-action-pattern.md` | Distinguishes human review, formal approval, and customer approval for sensitive, high-impact, or customer-impacting actions before execution or release. |
| `tenant-safe-rag-memory-pattern.md` | Describes safe use of retrieval and memory while preserving tenant, customer, case, evidence, allowed-use, and retention boundaries. |
| `private-local-llm-dfir-pattern.md` | Describes private or local LLM-assisted DFIR workflows where LLM output remains assistive, evidence-backed, reviewed, and auditable. |

---

## How to Use This Directory

Use these pattern files as short architecture references for common governed agentic security operations scenarios.

Each pattern should explain:

- the scenario it addresses
- the workflow boundary it defines
- the major control decisions involved
- when to use or avoid the pattern
- where to find deeper control requirements

For dense governance, assurance, policy enforcement, tenant isolation, tool-access, evidence, DFIR, and audit requirements, use [`../governance-library/`](../governance-library/).
