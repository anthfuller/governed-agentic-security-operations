# MDR Agent Fleet Operating Model

This model applies the [`MDR implementation profile`](../profiles/mdr.yaml) to investigation, recommendation, and governed response. It does not authorize autonomous containment.

## Accountabilities

| Role | Accountable for |
|---|---|
| MDR service owner | Response boundaries, policy, and exceptions |
| MDR analyst | Evidence review and operational recommendation |
| Response approver | Exact response authorization |
| Customer approver | Contractually retained customer authorization |
| Fleet owner | Release eligibility, staged rollout, rollback, recall |
| Enforcement owner | Effective PEP and target-tool controls |

## Governed Response Path

1. Bind the alert and retrieved evidence to the customer, tenant, incident, and target.
2. Produce a recommendation with evidence references and limitations.
3. Run advisory assurance checks; unresolved scope or support failures block progression.
4. Evaluate the exact tool request under a versioned policy.
5. Collect human and customer approvals required by the policy.
6. Revalidate request, decision, approval, and tool contract at the external PEP.
7. Record the result and verify the audit chain.

Fleet changes follow staged, tenant-eligible rollout. A change to response logic, tool parameters, approval requirements, or target scope is material and requires a new release decision.

Production dependencies include tenant-aware SIEM/XDR data, an identity provider, approval service, external PEP, response tools, deployment controls, monitoring, and durable audit storage.

Related controls: `GASO-GOV-001`, `GASO-TEN-002`, `GASO-APR-002`, `GASO-TOL-002`, `GASO-FLT-002`, `GASO-AUD-003`.
