# Examples

## Purpose

This directory contains concrete examples that show how the **Agentic MSSP / MDR / DFIR Security Operations Architecture** can be applied in practical workflows.

The examples are designed to demonstrate how agentic workflows should be scoped, policy-gated, evaluated, audited, and routed through human approval where required. They are not vendor-specific implementation designs and should not be treated as final engineering specifications.

## Scope

The examples support the following service models where applicable:

- **MSSP** — multi-customer alert handling, enrichment, routing, recommendations, and reporting support.
- **MDR** — investigation support, response recommendations, escalation, and detection or containment workflows.
- **SOC / Incident Response** — triage, incident coordination, policy-gated investigation, and operational response support.
- **DFIR** — evidence-aware investigation support, timeline assistance, report preparation, and chain-of-custody-sensitive workflows.
- **Private / Local LLM-assisted DFIR** — local or isolated AI-assisted forensic workflows where evidence, prompts, retrieval, outputs, and tool use remain scoped and auditable.

Private / Local LLM-assisted DFIR should only be included in examples where local or private AI-assisted forensic analysis naturally applies. It should not be forced into alert triage examples unless the workflow escalates into forensic evidence handling or local DFIR analysis.

## Current Example Structure

```text
examples/
├── README.md
├── alert-triage-to-recommendation/
│   ├── README.md
│   ├── example-request.json
│   ├── example-judge-output.json
│   ├── example-policy-decision.json
│   └── example-audit-event.json
```

## Example Catalog

| Example | Purpose | Primary Service Models |
|---|---|---|
| [`alert-triage-to-recommendation/`](./alert-triage-to-recommendation/) | Demonstrates how an agentic workflow receives a security alert, enriches context, produces a recommendation, evaluates the output, receives a policy decision, and records an audit event. | MSSP, MDR, SOC / Incident Response |

## How Examples Should Be Used

Each example should show a complete governed workflow, not just a happy-path agent response.

A good example should demonstrate:

- the mission or request context;
- tenant, customer, case, incident, and workflow scope where applicable;
- the agentic task or recommendation;
- policy decisioning before execution or release;
- judge or assurance output where applicable;
- human approval triggers for sensitive actions;
- tool, retrieval, memory, or evidence constraints where applicable;
- audit events that support replay and accountability;
- deny, fail-closed, or escalation paths where applicable.

## Example File Roles

Each example directory should include a short README plus structured artifacts that show how the workflow behaves.

| File | Role |
|---|---|
| `README.md` | Explains the example scenario, service model applicability, actors, flow, controls, failure paths, and related patterns. |
| `example-request.json` | Shows the incoming request or event that starts the workflow. |
| `example-judge-output.json` | Shows assurance or judge output, such as evidence support, output quality, boundary checks, or confidence concerns. |
| `example-policy-decision.json` | Shows the PDP decision, required approval, deny reason, restrictions, or allow decision. |
| `example-audit-event.json` | Shows the audit event required to reconstruct the workflow and correlate request, decision, output, and execution context. |

Not every future example must use the exact same JSON files, but every example should preserve clear request, decision, assurance, and audit traceability.

## Required Example Controls

Examples should demonstrate the following controls where relevant:

- explicit tenant and customer scope;
- case, incident, or evidence scope where applicable;
- agent and workflow identity;
- data classification and sensitivity label;
- policy decision before execution or release;
- PDP / PEP separation where tool use or execution is involved;
- human approval for sensitive, privileged, destructive, customer-impacting, or evidence-sensitive actions;
- retrieval and memory scope where RAG or memory is used;
- output destination control;
- audit reference and correlation identifiers;
- fail-closed handling for missing scope, missing policy, missing approval, or insufficient evidence.

## Common Metadata

Where applicable, example artifacts should include or reference:

- `tenant_id`;
- `customer_id`;
- `case_id`;
- `incident_id`;
- `workflow_id`;
- `agent_id`;
- `user_id` or service identity;
- `requested_action`;
- `policy_decision`;
- `approval_required`;
- `approval_record_id`;
- `evidence_object_ids`;
- `knowledge_store_or_memory_scope`;
- `knowledge_memory_scope_result`;
- `data_classification`;
- `sensitivity_label`;
- `output_destination`;
- `audit_reference_id`;
- `correlation_id`.

Examples should not invent these fields as decorative metadata. Include them when they are relevant to the workflow being demonstrated.

## Relationship to Patterns

Examples should map back to the architecture patterns in the `patterns/` directory.

| Pattern | How Examples Should Use It |
|---|---|
| `governed-agentic-security-operations-pattern.md` | Use as the baseline for mission-scoped, policy-gated, auditable agentic workflows. |
| `policy-enforced-tool-use-pattern.md` | Use when the example includes tools, APIs, scripts, connectors, or automation actions. |
| `human-approved-sensitive-action-pattern.md` | Use when the example includes sensitive, privileged, destructive, customer-impacting, externally visible, or evidence-sensitive actions. |
| `tenant-safe-rag-memory-pattern.md` | Use when the example includes RAG, vector search, shared memory, case memory, customer memory, or retrieved context. |
| `private-local-llm-dfir-pattern.md` | Use when the example includes private, local, isolated, or customer-controlled LLM-assisted forensic analysis. |

## Example Review Checklist

Before accepting an example, verify that:

- the scenario is clear and realistic;
- the service model applicability is explicit;
- the workflow is scoped to tenant, customer, case, incident, or evidence context where applicable;
- the agent does not receive implicit authority to execute;
- policy decisioning is represented;
- enforcement or approval is shown where required;
- audit events are sufficient to reconstruct the workflow;
- sensitive actions do not bypass human approval;
- evidence-sensitive outputs are evidence-backed;
- RAG or memory does not cross tenant, customer, case, or authorization boundaries;
- failure, deny, clarification, or escalation paths are represented where relevant.

## Non-Goals

The examples directory does not:

- define a vendor-specific product implementation;
- replace engineering designs, schemas, tests, or deployment guides;
- claim that all workflows require full automation;
- require every example to include DFIR or Private / Local LLM-assisted DFIR;
- replace policy, legal, compliance, customer, or incident command requirements;
- treat agent output as authoritative without policy, evidence, review, and audit controls.

## Summary

The `examples/` directory demonstrates how the architecture patterns are applied in practical workflows.

Each example should make the control path visible: scoped request, agentic processing, assurance, policy decision, human approval where required, controlled execution or recommendation, and auditability.

The core principle is:

> Examples should show how agentic security workflows operate safely in practice, not simply how an agent produces an answer.
