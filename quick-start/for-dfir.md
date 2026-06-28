# Quick Start for DFIR

This path is for DFIR practitioners evaluating private or local LLM-assisted workflows where evidence integrity, supported claims, review accountability, and replay matter more than automation speed.

## Goal

Use this path to answer one question:

> How can LLM assistance support DFIR analysis without turning evidence-derived summaries into original evidence or unsupported findings?

## Recommended Path

| Step | Read | What to Look For |
|---:|---|---|
| 1 | [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) | Boundaries for private/local LLM-assisted forensic workflows. |
| 2 | [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) | How findings should reference supporting evidence. |
| 3 | [`../data-ingestion/readme.md`](../data-ingestion/readme.md) | How source metadata, normalization, enrichment, and replay affect trust. |
| 4 | [`../governance-library/ai-assurance/readme.md`](../governance-library/ai-assurance/readme.md) | How output checks and unsupported-claim checks support review. |
| 5 | [`../human-oversight/readme.md`](../human-oversight/readme.md) | What requires human review before use in reporting or decision-making. |
| 6 | [`../audit-replay/readme.md`](../audit-replay/readme.md) | How analysis steps, evidence references, exceptions, and conclusions can be reconstructed. |
| 7 | [`../templates/readme.md`](../templates/readme.md) | Reusable record formats for evidence references, reviews, and audit events. |

## DFIR Review Checklist

Use this checklist when reviewing a private/local LLM-assisted DFIR workflow:

- Does the workflow distinguish original evidence from summaries, timelines, and derived findings?
- Are claims linked to evidence references?
- Are unsupported, ambiguous, or overbroad claims flagged before reporting?
- Is the model prohibited from modifying or replacing original evidence?
- Is human review required before findings are used in reports, escalation, or customer-facing outputs?
- Are tool outputs, prompts, evidence references, analyst decisions, and exceptions preserved for audit replay?
- Are local/private model limitations documented clearly?

## Expected Output

After this path, a reader should be able to evaluate whether an LLM-assisted DFIR workflow preserves evidence boundaries, supports findings with references, and remains reviewable.
