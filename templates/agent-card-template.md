# Agent Card Template

Use an agent card to register ownership, identity, lifecycle state, mission, allowed tools, prohibited actions, and scope before an agent participates in a governed workflow.

Required decisions:

- Name the accountable human or organizational owner role.
- Reference a distinct externally managed identity.
- List approved missions and allowed tool identifiers.
- State prohibited actions explicitly.
- Bind the approved tenant, customer, case, target, or environment scope.
- Record formal approval requirements separately from agent behavior.

Validate [`agent-card.yaml`](agent-card.yaml) with:

```bash
gaso validate templates/agent-card.yaml
```

An agent card registers intended boundaries. It does not grant runtime permissions and does not replace identity-provider, PDP, PEP, or target-system controls.
