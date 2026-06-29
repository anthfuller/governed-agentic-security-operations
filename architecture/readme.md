# Architecture

This directory contains the reader-facing architecture views for the governed Agentic MSSP / MDR / DFIR security operations reference architecture.

The files in this directory explain the overall operating model, major architecture views, control-loop flow, and how agent-assisted security workflows remain scoped, reviewable, policy-mediated, and auditable.

## What This Directory Contains

| File | Purpose |
|---|---|
| `executive-view.md` | Summarizes the architecture for leadership, governance, and service-owner audiences. |
| `engineering-view.md` | Describes the major engineering components, handoffs, and implementation considerations. |
| `governed-agentic-shared-operating-model.md` | Organizes the shared operating model across security operations, governance, oversight, and service delivery boundaries. |
| `control-loop.md` | Defines the repo-native governed agentic security operations loop. |
| `architecture-principles.md` | Defines architecture guardrails for agent trust, policy enforcement, evidence integrity, tenant isolation, auditability, and human accountability. |
| `architecture-assumptions.md` | Defines the assumptions and constraints behind the governed agentic security operations architecture. |
| `diagrams/` | Stores architecture diagrams used by the architecture views. |
| `layered-architecture.md` | Describes the layered operating model for governed agentic security operations. |
| `agentic-fleet-architecture.md` | Defines fleet-level agent governance, rollout, rollback, recall, tenant eligibility, and sanitized intelligence propagation. |
| `agentic-fleet-control-loop.md` | Defines the control loop for fleet updates, release gates, monitoring, rollback, and replayability. |

## How to Use This Directory

Start here to understand the architecture before moving into patterns, examples, service models, templates, or the governance library.

Use these files to understand:

- the intended architecture shape
- the major workflow stages
- the separation between agent assistance, assurance checks, policy decisions, enforcement, approval, action, and audit
- how the architecture supports MSSP, MDR, SOC, cloud incident response, and DFIR scenarios
