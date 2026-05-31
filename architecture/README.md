# Architecture

This directory contains the reader-facing architecture views for the governed Agentic MSSP / MDR / DFIR security operations reference architecture.

The files in this directory explain the overall operating model, major architecture views, control-loop flow, and how agent-assisted security workflows remain scoped, reviewable, policy-mediated, and auditable.

## What This Directory Contains

| File | Purpose |
|---|---|
| `executive-view.md` | Summarizes the architecture for leadership, governance, and service-owner audiences. |
| `engineering-view.md` | Describes the major engineering components, handoffs, and implementation considerations. |
| `layered-architecture.md` | Organizes the architecture into practical layers for agentic security operations. |
| `control-loop.md` | Defines the repo-native governed agentic security operations loop. |
| `architecture-principles.md` | Agents do not remove human accountability. |
| `architecture-assumptions.md` | Defines the assumptions and contraints behind the Governed Agentic Operations Architecture. |
| `diagrams/` | Stores architecture diagrams used by the architecture views. |

## How to Use This Directory

Start here to understand the architecture before moving into patterns, examples, service models, templates, or the governance library.

Use these files to understand:

- the intended architecture shape
- the major workflow stages
- the separation between agent assistance, assurance checks, policy decisions, enforcement, approval, action, and audit
- how the architecture supports MSSP, MDR, SOC, cloud incident response, and DFIR scenarios

## Control Detail Boundary

This directory should remain short, reader-facing, and architecture-oriented.

Dense control details, detailed control requirements, assurance models, policy-enforcement mechanics, tenant-isolation requirements, evidence-traceability requirements, and audit-replay requirements belong in [`../governance-library/`](../governance-library/).

Architecture files may summarize or point to those controls, but should not duplicate the governance library.
