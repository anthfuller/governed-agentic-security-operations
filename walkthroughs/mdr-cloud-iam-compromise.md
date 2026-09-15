# Walkthrough: MDR Cloud IAM Compromise

## Scenario

An MDR workflow correlates synthetic sign-in indicators for one customer identity and recommends revoking that identity's active sessions. Revocation changes customer state, so the recommendation cannot authorize execution.

## Governed Path

1. Bind the evidence and target identity to customer, tenant, and case.
2. Preserve evidence references and produce a derived recommendation.
3. Treat assurance as advisory; unresolved source or scope issues stop the workflow.
4. Evaluate `revoke_identity_sessions` under the versioned reference policy.
5. Collect exact human and customer approval records.
6. Revalidate policy, approval digest, scope, tool, operation, and target at the external PEP.
7. Record the external result and correlated audit events.

## Run the Gates

The complete synthetic set is under [`artifacts/mdr-cloud-iam-compromise/`](artifacts/mdr-cloud-iam-compromise/). It includes evidence, recommendation, assurance limitations, policy and decision, approvals, tool contract, validate-only request/result, audit events, and expected replay.

```bash
gaso validate walkthroughs/artifacts/mdr-cloud-iam-compromise/*.yaml \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/expected-replay.json

gaso verify-tenant-scope \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/request.yaml \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/human-approval.yaml \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/customer-approval.yaml

gaso evaluate-policy \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/request.yaml \
  --policy walkthroughs/artifacts/mdr-cloud-iam-compromise/policy.yaml \
  --approvals \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/human-approval.yaml \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/customer-approval.yaml

gaso verify-evidence-manifest \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/evidence-manifest.yaml
gaso verify-audit-chain \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/audit-events.jsonl
gaso replay \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/audit-events.jsonl
```

Expected result: `ALLOW`, `external_action_executed: false`. Change the request reason, target, tenant, tool, action, or policy version without issuing new bound approvals and the request must block or fail closed.

The negative fixture changes an allowed parameter after both approvals. This must return `REQUIRE_APPROVAL` with exit `1` because the request digest no longer matches:

```bash
gaso evaluate-policy \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/negative/request-changed-after-approval.yaml \
  --policy walkthroughs/artifacts/mdr-cloud-iam-compromise/policy.yaml \
  --approvals \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/human-approval.yaml \
  walkthroughs/artifacts/mdr-cloud-iam-compromise/customer-approval.yaml
```

The automated assertion is in [`../tests/test_walkthroughs.py`](../tests/test_walkthroughs.py).

## Production Boundary

The repository does not query a cloud identity provider or revoke sessions. Production use needs tenant-aware evidence retrieval, authenticated approval authority, a policy enforcement point, least-privilege identity tooling, outcome verification, and durable audit storage.

Related controls: `GASO-GOV-001`, `GASO-TEN-002`, `GASO-POL-001`, `GASO-APR-002`, `GASO-APR-003`, `GASO-TOL-002`, `GASO-AUD-001`. Profile: [`../profiles/mdr.yaml`](../profiles/mdr.yaml).
