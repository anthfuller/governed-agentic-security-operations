# PDP and PEP Model

The Policy Decision Point (PDP) evaluates a request. The Policy Enforcement Point (PEP) controls access to the external tool or resource. Keeping them separate prevents a recommendation, agent, or tool client from treating a decision as self-executing authority.

## PDP Inputs

- request and correlation identifiers;
- actor and agent identity state;
- exact scope and target;
- tool contract and operation risk class;
- policy version;
- required approval records;
- relevant evidence and assurance results;
- decision time and validity requirements.

## PDP Outputs

`ALLOW`, `DENY`, `REQUIRE_APPROVAL`, or `FAIL_CLOSED`, plus reason codes, obligations, scope, policy version, and expiration.

## PEP Responsibilities

Immediately before an external action, the PEP must revalidate the decision, request binding, tool and operation, target, parameters, approvals, identity, scope, and expiration. The PEP denies any mismatch and records the result.

The repository implements a deterministic reference PDP only. It has no production PEP and cannot execute a tool. Controls: `GASO-POL-001` through `GASO-POL-003` and `GASO-TOL-002`.
