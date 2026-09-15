# Scenario Walkthroughs

This directory contains concrete walkthroughs that show how the architecture applies to governed agentic security operations workflows.

Walkthroughs are documentation artifacts. They are not runnable playbooks, production procedures, or customer-ready managed service instructions.

## Available Walkthroughs

| Walkthrough | Focus |
|---|---|
| [`mssp-endpoint-isolation.md`](mssp-endpoint-isolation.md) | Agent recommendation, evidence support, policy decision, human approval, scoped tool execution, and audit replay. |
| [`mdr-cloud-iam-compromise.md`](mdr-cloud-iam-compromise.md) | Scope-bound cloud identity response with request-digest approvals and an external execution boundary. |
| [`dfir-local-llm-timeline.md`](dfir-local-llm-timeline.md) | Evidence manifest, derived timeline lineage, human review, and non-executing replay. |

## Walkthrough Pattern

Each walkthrough should identify:

- scenario context;
- governance objective;
- workflow steps;
- control points;
- approval boundaries;
- failure modes;
- representative documentation artifacts;
- related architecture references.

The machine-readable artifacts under [`artifacts/`](artifacts/) are synthetic and safe for offline conformance checks. No walkthrough performs a real security action.
