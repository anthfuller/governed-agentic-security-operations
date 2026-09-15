# Fleet Update Authorization and Policy Gates

Fleet updates change behavior across multiple agents or tenants and therefore require staged, reversible authorization. A release approval does not authorize every later transition automatically.

## Required Gates

| Transition | Minimum evidence |
|---|---|
| Candidate to validated | Versioned manifest, provenance, integrity, dependency, scope, and negative-test results. |
| Validated to approved | Named accountable approval and policy decision. |
| Approved to canary | Eligible canary scope, monitoring, halt criteria, rollback target. |
| Canary to limited | Recorded success criteria and zero unresolved boundary or authority failures. |
| Limited to broad | Fresh eligibility, monitoring results, approval if required by policy. |
| Any active stage to rollback/recall | Trigger evidence, bounded affected scope, known-good target, authorized emergency path. |

## Deny or Halt Conditions

- package or manifest integrity mismatch;
- unknown component or provenance;
- ineligible tenant assignment;
- missing monitoring or audit capability;
- boundary, authority, evidence, or tool-scope regression;
- missing tested rollback target;
- an approval or policy decision that does not cover the requested stage.

Controls: `GASO-FLT-001`, `GASO-FLT-002`, `GASO-FLT-003`, and `GASO-GOV-003`.
