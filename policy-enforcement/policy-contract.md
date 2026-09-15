# Policy Contract

A policy contract defines the inputs, outcomes, and obligations that an implementation must support. The canonical machine-readable example is [`../policies/endpoint-response-policy.yaml`](../policies/endpoint-response-policy.yaml).

## Required Policy Fields

- stable policy ID and semantic version;
- implementation profile;
- default outcome of `FAIL_CLOSED`;
- decision time-to-live;
- registered action name and risk class;
- required tool ID;
- allowed parameter names;
- required scope fields;
- required human and customer approval types;
- explicit allowed or denied state.

## Decision Contract

The decision must identify the request, policy version, outcome, exact scope, reason codes, required approvals, obligations, evaluation time, expiration, and that the decision did not execute an action.

Policy versions are immutable after release. A change to action authority, scope, required approval, allowed parameter, or default behavior requires a new version and change review under `GASO-GOV-003`.
