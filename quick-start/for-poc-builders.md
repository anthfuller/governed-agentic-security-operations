# Quick Start for PoC Builders

This path is for builders planning a separate runnable proof-of-concept control plane.

## Recommended Reading Order

1. [`../architecture/engineering-view.md`](../architecture/engineering-view.md)
2. [`../architecture/control-loop.md`](../architecture/control-loop.md)
3. [`../examples/readme.md`](../examples/readme.md)
4. [`../templates/readme.md`](../templates/readme.md)
5. [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md)
6. [`../tool-access/readme.md`](../tool-access/readme.md)
7. [`../audit-replay/readme.md`](../audit-replay/readme.md)
8. [`../walkthroughs/mssp-endpoint-isolation.md`](../walkthroughs/mssp-endpoint-isolation.md)

## Minimum PoC Flow

A separate companion PoC can demonstrate:

```text
fake alert
→ agent recommendation record
→ judge validation record
→ PDP decision record
→ human approval record
→ PEP-scoped tool execution simulation
→ audit event
→ replay summary
```

The PoC should use synthetic data only. It should not include customer data, tenant data, real production actions, or employer confidential information.
