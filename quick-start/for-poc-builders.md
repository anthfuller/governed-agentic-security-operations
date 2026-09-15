# Quick Start for Adoption-Kit Builders

This path is for engineers and architects using the repository's controls, profiles, templates, schemas, and deterministic conformance tooling.

## Goal

Use the kit to answer a bounded question:

> Are the selected governance artifacts structurally valid, consistently scoped, policy-complete, evidence-aware, and replayable before an external platform is asked to enforce them?

The kit does not operate a SOC, invoke an agent or model, or execute an action in a customer or production environment.

## Recommended Path

| Step | Read or run | Outcome |
|---:|---|---|
| 1 | [`../controls/README.md`](../controls/README.md) | Understand the normative controls and identifiers. |
| 2 | [`../profiles/README.md`](../profiles/README.md) | Select the MSSP, MDR, or DFIR profile. |
| 3 | [`../architecture/engineering-view.md`](../architecture/engineering-view.md) | Identify which controls are validated here and which require external enforcement. |
| 4 | [`../templates/readme.md`](../templates/readme.md) | Create the required local governance artifacts. |
| 5 | `gaso validate <artifact>` | Validate schema and artifact type. |
| 6 | `gaso verify-tenant-scope <artifact-set>` | Check tenant, customer, case, evidence, target, and tool-scope consistency. |
| 7 | `gaso evaluate-policy ...` | Evaluate a synthetic reference policy without executing an action. |
| 8 | `gaso verify-audit-chain ...` and `gaso replay ...` | Verify and reconstruct the recorded workflow. |

## Reference Flow

```text
synthetic request
→ scope and schema validation
→ recommendation and assurance records
→ deterministic reference policy decision
→ scope-bound approval validation
→ non-executing tool request validation
→ tamper-evident audit verification
→ deterministic replay
```

## Required Boundaries

- Use synthetic data only.
- Do not include credentials or real tenant, customer, incident, case, or evidence data.
- Do not interpret `gaso` output as authorization to execute an action.
- Implement identity, approval, policy enforcement, tool mediation, audit durability, and evidence preservation in the external systems that own those responsibilities.
- Record tailoring and exceptions explicitly; do not silently remove control requirements.

## Expected Output

After completing this path, a builder has a validated set of governance artifacts, explicit external enforcement dependencies, passing positive and negative conformance tests, and a replayable synthetic workflow. The result is evidence of repository conformance—not evidence that a production system is secure or compliant.
