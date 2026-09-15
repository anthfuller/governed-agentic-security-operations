# Cross-Tenant Failure Modes

| Failure | Detection | Required response |
|---|---|---|
| Missing customer or tenant identifier | Schema or scope validation | Fail closed; do not retrieve, decide, act, or release |
| Retrieval returns another tenant's object | Result-scope comparison | Quarantine result, deny workflow, audit violation |
| Approval belongs to another request or tenant | Exact approval binding | Deny and require new authorization |
| Tool target differs from the approved target | PEP parameter comparison | Block tool call and record mismatch |
| Shared cache, queue, or memory loses scope | Isolation test or runtime monitor | Disable affected path, assess exposure, invalidate unsafe state |
| Fleet release assigned to ineligible tenant | Eligibility gate | Deny assignment and pause affected stage |
| Audit event omits scope | Schema/audit verification | Fail closed for governed execution |
| Customer output contains foreign data | Release review or DLP control | Block release and start incident handling |

Do not repair a mismatch by guessing the intended tenant. Preserve the request, minimize sensitive details in error output, revoke or quarantine unsafe derived artifacts, and investigate the full correlation chain.

Production response may require containment in identity, storage, messaging, retrieval, deployment, and target-tool systems outside this repository.

Related controls: `GASO-TEN-001`, `GASO-TEN-002`, `GASO-TEN-003`, `GASO-ING-003`, `GASO-AUD-001`.
