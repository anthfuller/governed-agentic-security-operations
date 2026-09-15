# Policy Enforcement

This directory defines the decision and enforcement boundary for governed workflows. The repository can validate reference policies and records; production decisions and action enforcement require external PDP and PEP components.

## Contents

- [`action-risk-classification.md`](action-risk-classification.md): risk classes and minimum handling.
- [`policy-contract.md`](policy-contract.md): required policy inputs and outputs.
- [`policy-decision-flow.md`](policy-decision-flow.md): deterministic decision sequence.
- [`approval-policy-requirements.md`](approval-policy-requirements.md): approval type and scope rules.
- [`pep-pdp-model.md`](pep-pdp-model.md): separation between decision and enforcement.
- [`fail-closed-behavior.md`](fail-closed-behavior.md): indeterminate-state handling.
- [`fleet-update-authorization-and-policy-gates.md`](fleet-update-authorization-and-policy-gates.md): fleet transition gates.

## Normative Controls

- `GASO-POL-001`: require a policy decision.
- `GASO-POL-002`: fail closed on indeterminate state.
- `GASO-POL-003`: expire and revalidate decisions.
- `GASO-APR-001` through `GASO-APR-003`: validate approval authority and scope.
- `GASO-TOL-002` and `GASO-TOL-003`: enforce the decision at the external tool boundary.

## Local Verification

```bash
gaso evaluate-policy templates/governed-action-request.yaml \
  --policy policies/endpoint-response-policy.yaml \
  --approvals templates/human-approval-record.yaml templates/customer-approval-record.yaml
```

The result is a synthetic reference decision. It is not authorization for a real action.
