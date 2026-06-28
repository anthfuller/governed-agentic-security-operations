# Quick Start for MSSP / MDR

This path is for MSSP, MDR, and SOC leaders or architects evaluating governed agentic security operations in multi-customer or managed-service environments.

## Goal

Use this path to answer one question:

> How can an agent-assisted MDR or MSSP workflow recommend action without bypassing tenant boundaries, policy, human approval, customer approval, or auditability?

## Recommended Path

| Step | Read | What to Look For |
|---:|---|---|
| 1 | [`../architecture/executive-view.md`](../architecture/executive-view.md) | The overall operating model and stakeholder-level control story. |
| 2 | [`../architecture/engineering-view.md`](../architecture/engineering-view.md) | Where orchestration, assurance, policy, enforcement, tools, and audit fit. |
| 3 | [`../architecture/control-loop.md`](../architecture/control-loop.md) | How recommendations move through policy and enforcement before action. |
| 4 | [`../service-models/readme.md`](../service-models/readme.md) | How MSSP, MDR, cloud IR, and DFIR service boundaries differ. |
| 5 | [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) | How customer, tenant, case, and evidence boundaries are preserved. |
| 6 | [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) | How PDP and PEP responsibilities are separated. |
| 7 | [`../human-oversight/readme.md`](../human-oversight/readme.md) | Where human review, formal approval, and customer approval are required. |
| 8 | [`../agent-governance/readme.md`](../agent-governance/readme.md) | How agent lifecycle, access scope, rollout, recall, and rollback are governed. |
| 9 | [`../audit-replay/readme.md`](../audit-replay/readme.md) | How decisions and actions can be reconstructed after the fact. |
| 10 | [`../walkthroughs/mssp-endpoint-isolation.md`](../walkthroughs/mssp-endpoint-isolation.md) | A concrete end-to-end example of the control path. |

## MSSP / MDR Review Checklist

Use this checklist when reviewing an agentic workflow design:

- Does the workflow identify the customer, tenant, case, and evidence scope before retrieval or action?
- Is the agent limited to recommendation, summarization, classification, or preparation of approval packages?
- Is the policy decision made outside the agent?
- Is enforcement performed before tool execution?
- Is customer approval separated from internal analyst review where required?
- Are cross-tenant, cross-customer, stale, missing, or unsupported contexts blocked or escalated?
- Can an auditor replay the recommendation, evidence references, approval decision, tool request, and final outcome?

## Expected Output

After this path, a reader should be able to describe the minimum governance controls needed before using agents in a managed security operations workflow.
