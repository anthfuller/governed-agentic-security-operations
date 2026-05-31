# Patterns

## Purpose

This directory contains reusable architecture patterns for the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The patterns define repeatable ways to govern agentic security operations across **MSSP**, **MDR**, **SOC / Incident Response**, **DFIR**, and **Private / Local LLM-assisted DFIR** where applicable.

These files are not final engineering designs. They define architecture intent, control requirements, decision boundaries, anti-patterns, and acceptance criteria that can be implemented through detailed engineering, policies, schemas, tests, workflows, and platform-specific designs.

## Pattern Scope

The patterns in this directory focus on governed agentic security operations where agents, automation, retrieval, memory, tools, or LLM-assisted workflows may affect:

- tenants or customers;
- cases or incidents;
- evidence or forensic artifacts;
- security tools and APIs;
- analyst workflows;
- customer-facing outputs;
- response recommendations;
- sensitive or privileged actions.

The patterns should be applied where they fit. They should not be forced into purely manual workflows that do not use AI assistance, automation, tool use, retrieval, or memory.

## Pattern Catalog

| Pattern | Purpose |
|---|---|
| [`governed-agentic-security-operations-pattern.md`](./governed-agentic-security-operations-pattern.md) | Defines the overall governed agentic security operations pattern across MSSP, MDR, SOC / IR, DFIR, and Private / Local LLM-assisted DFIR. |
| [`policy-enforced-tool-use-pattern.md`](./policy-enforced-tool-use-pattern.md) | Defines how agentic workflows use tools, APIs, scripts, connectors, and automation through PDP / PEP enforcement. |
| [`human-approved-sensitive-action-pattern.md`](./human-approved-sensitive-action-pattern.md) | Defines how sensitive, privileged, customer-impacting, destructive, or evidence-sensitive actions require human approval before execution. |
| [`tenant-safe-rag-memory-pattern.md`](./tenant-safe-rag-memory-pattern.md) | Defines how RAG, knowledge retrieval, case memory, shared memory, and agent memory remain tenant-safe, case-safe, evidence-aware, and auditable. |
| [`private-local-llm-dfir-pattern.md`](./private-local-llm-dfir-pattern.md) | Defines how private, local, isolated, or customer-controlled LLMs can assist DFIR while preserving evidence integrity, chain of custody, human validation, and auditability. |

## How to Use These Patterns

Use these patterns as reusable architecture references when designing or reviewing agentic security workflows.

A workflow should identify:

1. which service model it supports;
2. which tenant, customer, case, incident, or evidence scope applies;
3. whether the workflow uses agents, tools, retrieval, memory, or LLM assistance;
4. whether actions are read-only, state-changing, sensitive, customer-impacting, or evidence-sensitive;
5. which policy, enforcement, approval, audit, and assurance controls are required.

## Service Model Alignment

| Service Model | Pattern Relevance |
|---|---|
| MSSP | Multi-customer operations, customer-scoped reporting, alert enrichment, workflow routing, tool use, and governed service delivery. |
| MDR | Investigation support, response recommendations, containment support, escalation, detection tuning, and policy-gated tool use. |
| SOC / Incident Response | Triage, incident coordination, approval routing, investigation support, privileged actions, and evidence-backed decision support. |
| DFIR | Evidence handling, artifact analysis, timeline support, chain-of-custody protection, forensic findings, and report preparation. |
| Private / Local LLM-assisted DFIR | Local or isolated AI-assisted forensic analysis, local RAG, local memory, report drafting, evidence review, and human-validated conclusions. |

## Common Control Principles

All patterns in this directory should preserve the following principles where applicable:

- explicit mission, tenant, customer, case, and workflow scope;
- no implicit agent-to-agent trust;
- policy before execution;
- PDP / PEP separation;
- least privilege and scoped credentials;
- tenant, customer, case, and evidence boundary enforcement;
- fail-closed behavior;
- human approval for sensitive actions;
- evidence-backed outputs;
- controlled retrieval and memory;
- auditability and replayability;
- governed change control;
- no uncontrolled self-modification.

## Pattern vs. Engineering Design

A pattern defines the reusable control model.

An engineering design defines the concrete implementation.

For example, a pattern may require:

- PDP / PEP enforcement;
- scoped tool credentials;
- approval records;
- evidence object references;
- retrieval scope validation;
- audit correlation IDs.

A final engineering design should specify:

- exact platform services;
- exact APIs and schemas;
- exact policy rules;
- exact identity configuration;
- exact tool wrappers;
- exact logging destinations;
- exact test cases;
- exact deployment topology;
- exact monitoring and alerting.

## Relationship to Other Architecture Views

These patterns complement other repo artifacts:

| Artifact | Role |
|---|---|
| `layered-architecture.md` | Explains how the architecture is organized into operating layers. |
| `control-loop.md` | Explains runtime execution governance for agentic actions. |
| Shared operating boundary visuals | Show non-negotiable controls across service models. |
| Executive architecture visuals | Provide leadership-level system framing. |
| Engineering architecture visuals | Show deeper component, control-plane, and integration structure. |

## Minimum Review Questions

Before accepting a pattern-based workflow, reviewers should ask:

- Is the workflow bound to tenant, customer, case, incident, or evidence scope where applicable?
- Is policy evaluated before tool use or execution?
- Is the enforcement point located at the real execution boundary?
- Are sensitive actions routed for human approval before execution?
- Are retrieval and memory scoped and auditable?
- Are evidence-sensitive outputs tied to evidence references?
- Can the workflow be audited, replayed, or reconstructed?
- Does the workflow fail closed when scope, policy, approval, or context is missing?
- Are customer-facing outputs validated before release?
- Are updates to prompts, policies, models, and workflows governed?

## Non-Goals

This directory does not:

- define vendor-specific implementations;
- replace detailed engineering designs;
- require every workflow to be automated;
- require AI assistance in every DFIR process;
- remove human accountability;
- replace legal, contractual, customer, or compliance requirements;
- claim that private or local LLM execution is automatically trustworthy.

## Summary

The `patterns/` directory provides reusable architecture patterns for governed agentic security operations.

The patterns help ensure that agentic workflows across MSSP, MDR, SOC / Incident Response, DFIR, and Private / Local LLM-assisted DFIR remain scoped, policy-gated, human-overseen where required, evidence-aware, auditable, and safe to operationalize.
