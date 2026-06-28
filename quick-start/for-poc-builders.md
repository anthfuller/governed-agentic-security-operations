# Quick Start for PoC Builders

This path is for engineers or architects planning a separate runnable proof-of-concept control plane based on the architecture in this repository.

This repository remains documentation-first. The PoC should live in a separate companion repository.

## Goal

Use this path to answer one question:

> What is the smallest safe demonstration that shows agent recommendation, policy decision, approval, scoped enforcement, audit event generation, and replay without touching real systems?

## Recommended Path

| Step | Read | What to Extract for a PoC |
|---:|---|---|
| 1 | [`../architecture/engineering-view.md`](../architecture/engineering-view.md) | Core components: orchestration, AI assurance, PDP, PEP, tools, audit. |
| 2 | [`../architecture/control-loop.md`](../architecture/control-loop.md) | The runtime sequence to simulate. |
| 3 | [`../examples/readme.md`](../examples/readme.md) | Example record shapes for requests, decisions, approvals, evidence, and audit. |
| 4 | [`../templates/readme.md`](../templates/readme.md) | Candidate templates to convert into schemas later. |
| 5 | [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) | PDP decision logic, risk classification, approval policy, and fail-closed behavior. |
| 6 | [`../tool-access/readme.md`](../tool-access/readme.md) | How to model scoped tools without performing real actions. |
| 7 | [`../audit-replay/readme.md`](../audit-replay/readme.md) | What events must be emitted so the flow can be replayed. |
| 8 | [`../walkthroughs/mssp-endpoint-isolation.md`](../walkthroughs/mssp-endpoint-isolation.md) | A first end-to-end scenario to implement with synthetic data. |

## Minimum PoC Flow

A separate companion PoC should start with a narrow synthetic flow:

```text
synthetic alert
→ scoped evidence references
→ agent recommendation record
→ assurance / judge validation record
→ PDP decision record
→ human approval record
→ PEP-scoped tool execution simulation
→ audit event
→ replay summary
```

## Suggested Companion Repo Skeleton

```text
agentic-security-operations-control-plane-poc/
├── README.md
├── data/
│   ├── alerts/
│   ├── evidence/
│   └── tenants/
├── schemas/
│   ├── agent-recommendation.schema.json
│   ├── policy-decision.schema.json
│   ├── approval-record.schema.json
│   ├── tool-execution.schema.json
│   └── audit-event.schema.json
├── examples/
│   └── endpoint-isolation/
├── src/
│   ├── pdp/
│   ├── pep/
│   ├── judges/
│   ├── approvals/
│   └── audit/
└── tests/
```

## PoC Boundaries

The PoC should use synthetic data only. It should not include customer data, tenant data, real EDR actions, real SIEM/SOAR actions, employer confidential information, or non-public product information.

## Expected Output

After this path, a builder should know what to implement first and what to intentionally leave out of the documentation-first architecture repository.
