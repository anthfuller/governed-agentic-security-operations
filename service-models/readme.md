# Service Models

## Purpose

This directory defines the operating models supported by the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The service models explain how governed agentic security operations apply across managed security services, managed detection and response, cloud incident response, and Private / Local LLM-assisted DFIR.

These files are not vendor-specific product designs. They define the service-level operating structure, control responsibilities, approval boundaries, evidence expectations, customer interaction points, and architecture alignment needed to operationalize the patterns in this repo.

## Directory Structure

```text
service-models/
├── README.md
├── mssp-operating-model.md
├── mdr-operating-model.md
├── cloud-ir-operating-model.md
├── private-local-llm-dfir-operating-model.md
└── diagrams/
    ├── mssp-operating-model.png
    ├── mdr-operating-model.png
    ├── dfir-operating-model.png
    └── shared-operating-boundaries.png
```

## Service Model Catalog

| File | Purpose |
|---|---|
| [`mssp-operating-model.md`](./mssp-operating-model.md) | Defines the managed security service provider operating model for multi-customer, governed, agentic security operations. |
| [`mdr-operating-model.md`](./mdr-operating-model.md) | Defines the managed detection and response operating model for investigation, escalation, recommendation, and response support. |
| [`cloud-ir-operating-model.md`](./cloud-ir-operating-model.md) | Defines the cloud incident response operating model for cloud security investigations, containment coordination, IAM compromise, and cloud evidence handling. |
| [`private-local-llm-dfir-operating-model.md`](./private-local-llm-dfir-operating-model.md) | Defines the Private / Local LLM-assisted DFIR operating model for local or isolated forensic analysis, timeline support, evidence review, and report preparation. |

## Diagram Catalog

| Diagram | Purpose |
|---|---|
| [`diagrams/mssp-operating-model.png`](./diagrams/mssp-operating-model.png) | Visualizes the MSSP operating model and shared control responsibilities. |
| [`diagrams/mdr-operating-model.png`](./diagrams/mdr-operating-model.png) | Visualizes the MDR operating model and response workflow boundaries. |
| [`diagrams/dfir-operating-model.png`](./diagrams/dfir-operating-model.png) | Visualizes the DFIR operating model, including evidence handling and review boundaries. |
| [`diagrams/shared-operating-boundaries.png`](./diagrams/shared-operating-boundaries.png) | Shows the shared control boundaries that apply across service models. |

## Operating Model Intent

Each service model should explain:

- what the service model does;
- which workflows are in scope;
- which workflows are out of scope;
- where agentic assistance is appropriate;
- where agentic assistance must be constrained;
- where policy decisions are required;
- where human approval is required;
- where customer authorization is required;
- what evidence, audit, and replay records are required;
- how the service model aligns to the shared architecture patterns.

## Shared Operating Boundaries

All service models should preserve the same non-negotiable operating boundaries where applicable:

- tenant and customer separation;
- case, incident, and evidence scope enforcement;
- no implicit agent-to-agent trust;
- policy before execution;
- PDP / PEP separation;
- least privilege and scoped credentials;
- controlled retrieval and memory;
- human approval for sensitive actions;
- customer authorization where required;
- evidence-backed outputs;
- auditability and replayability;
- fail-closed behavior;
- governed change control;
- no uncontrolled self-modification.

These controls should be applied where they naturally fit the service model. They should not be used as decorative language or forced into workflows that do not involve agentic assistance, tool use, retrieval, memory, or evidence handling.

## Service Model Comparison

| Service Model | Primary Focus | Agentic Role | Strongest Control Emphasis |
|---|---|---|---|
| MSSP | Multi-customer managed security operations | Assist with triage, enrichment, routing, reporting, and recommendation drafting | Tenant/customer separation, service consistency, customer reporting, auditability |
| MDR | Detection, investigation, response support, and escalation | Assist with investigation, response recommendation, containment preparation, and analyst workflow support | Policy-gated response, human approval, scoped tool use, evidence-backed recommendations |
| Cloud IR | Cloud incident response, IAM compromise, cloud resource investigation, and containment coordination | Assist with cloud context review, IAM risk assessment, approval package drafting, and response coordination | Privileged action control, customer authorization, cloud evidence handling, PEP enforcement |
| Private / Local LLM-assisted DFIR | Local or isolated forensic analysis and report support | Assist with evidence summarization, timeline drafting, artifact review, and report preparation | Evidence integrity, chain of custody, case-scoped retrieval, analyst validation, no unsupported conclusions |

## Relationship to Patterns

The service models operationalize the reusable patterns in the `patterns/` directory.

| Pattern | Service Model Usage |
|---|---|
| [`governed-agentic-security-operations-pattern.md`](../patterns/governed-agentic-security-operations-pattern.md) | Baseline pattern for governed agentic workflows across all service models. |
| [`policy-enforced-tool-use-pattern.md`](../patterns/policy-enforced-tool-use-pattern.md) | Applies where agents or workflows may use tools, APIs, scripts, connectors, or automation. |
| [`human-approved-sensitive-action-pattern.md`](../patterns/human-approved-sensitive-action-pattern.md) | Applies where workflows may propose privileged, destructive, customer-impacting, externally visible, or evidence-sensitive actions. |
| [`tenant-safe-rag-memory-pattern.md`](../patterns/tenant-safe-rag-memory-pattern.md) | Applies where RAG, vector search, knowledge stores, case memory, customer memory, or shared memory influence outputs. |
| [`private-local-llm-dfir-pattern.md`](../patterns/private-local-llm-dfir-pattern.md) | Applies to local, private, isolated, or customer-controlled LLM-assisted forensic analysis. |

## Relationship to Examples

The examples in `examples/` show how these operating models appear in practical workflows.

| Example | Service Model Relationship |
|---|---|
| [`alert-triage-to-recommendation`](../examples/alert-triage-to-recommendation/) | Primarily supports MSSP, MDR, and SOC / Incident Response. DFIR applies only if the workflow escalates into evidence handling. |
| [`cloud-iam-compromise`](../examples/cloud-iam-compromise/) | Primarily supports MDR, Cloud IR, and SOC / Incident Response. DFIR applies if formal evidence handling or timeline reconstruction is required. |
| [`local-llm-forensic-timeline`](../examples/local-llm-forensic-timeline/) | Primarily supports Private / Local LLM-assisted DFIR and DFIR. MDR and SOC / IR apply when they escalate into forensic timeline work. |

## Minimum Content Expected in Each Operating Model

Each operating model file should include:

1. **Purpose**
2. **Service Scope**
3. **In-Scope Workflows**
4. **Out-of-Scope Workflows**
5. **Operating Principles**
6. **Agentic Assistance Boundaries**
7. **Human Roles and Responsibilities**
8. **Policy and Enforcement Points**
9. **Human Approval and Customer Authorization**
10. **Data, Retrieval, Memory, and Evidence Boundaries**
11. **Audit and Replay Requirements**
12. **Failure and Escalation Paths**
13. **Relationship to Patterns and Examples**
14. **Acceptance Criteria**
15. **Non-Goals**

The goal is to make each operating model useful to architects, reviewers, builders, and service owners without turning it into a vendor-specific engineering design.

## Review Checklist

Before accepting a service model file, verify that:

- the service purpose is clear;
- the service model is distinct from the other models;
- agentic assistance is bounded and not treated as execution authority;
- tenant, customer, case, incident, and evidence scope are addressed where applicable;
- PDP / PEP responsibilities are clear where execution or tool use is involved;
- sensitive actions require human approval;
- customer authorization is represented where required;
- RAG and memory are scoped where used;
- DFIR evidence handling is included only where it naturally applies;
- Private / Local LLM-assisted DFIR is not forced into unrelated service models;
- audit and replayability are described;
- failure, deny, escalation, and fail-closed behavior are included;
- the file does not become generic AI governance filler.

## Non-Goals

This directory does not:

- define a vendor-specific SOC, SIEM, XDR, SOAR, cloud, or forensic product design;
- replace engineering diagrams or deployment guides;
- require every service model to use the same level of automation;
- require AI assistance in every DFIR workflow;
- remove human accountability;
- replace incident command, DFIR lead authority, customer contracts, legal requirements, or compliance obligations;
- claim that private or local LLM execution is automatically trustworthy.

## Summary

The `service-models/` directory defines how the architecture is operationalized across MSSP, MDR, Cloud IR, and Private / Local LLM-assisted DFIR.

The core principle is:

> Each service model may use agentic assistance differently, but all service models must preserve scope, policy enforcement, human accountability, evidence integrity where applicable, and auditability.
