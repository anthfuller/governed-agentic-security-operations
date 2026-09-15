# Approval Boundaries

Approval authorizes one defined action; it does not grant general trust to an agent, workflow, or operator.

## Required Binding

An approval record is valid only when it identifies all applicable values below and they exactly match the request presented to the enforcement point:

- approver identity and authorized role;
- decision (`approved` or `denied`);
- action, tool, operation, target, and parameters;
- customer, tenant, case, and evidence scope;
- conditions, issue time, and expiration time;
- request and policy-decision identifiers.

The approval schema is [`../schemas/approval-record.schema.json`](../schemas/approval-record.schema.json). Human and customer examples are in [`../templates/`](../templates/).

## Boundaries

- Analyst review is not approval.
- An assurance or judge result is not approval.
- Internal approval cannot substitute for required customer authorization.
- Approval for one target, tenant, case, action, or time window cannot be reused for another.
- A changed request requires policy re-evaluation and a new approval.
- An expired, revoked, ambiguous, or unverifiable approval is denied.

## Enforcement

The production policy enforcement point must compare the request, policy decision, and each required approval immediately before execution. This repository validates representative records but does not execute external actions.

Related controls: `GASO-APR-001`, `GASO-APR-002`, `GASO-APR-003`, `GASO-TOL-002`, `GASO-TOL-003`.
