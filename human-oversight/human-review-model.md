# Human Review Model

Human involvement has three distinct functions. Implementations must not collapse them into one checkbox.

| Function | Purpose | Can authorize execution? |
|---|---|---|
| Analyst review | Check evidence, scope, uncertainty, and operational reasonableness | No |
| Formal approval | Authorize an exact action under policy | Yes, when the policy recognizes the approver role |
| Release review | Authorize distribution of a finding, report, intelligence item, or fleet change | Only for that release |

## Required Outcomes

A reviewer must select an explicit outcome: accept for the stated use, reject, request more evidence, or escalate. Silence, timeout, and interface dismissal are not approval.

Review records must identify the reviewer, role, artifact and version reviewed, evidence references, scope, outcome, limitations, and time. Formal approvals additionally follow [`approval-boundaries.md`](approval-boundaries.md).

## Reviewer Responsibilities

- confirm customer, tenant, case, target, and evidence scope;
- test material claims against cited evidence;
- identify uncertainty, missing evidence, and conflicting context;
- confirm the proposed use and destination;
- route sensitive actions through policy and formal approval;
- reject outputs that cannot be adequately evaluated.

Review does not override a policy denial. Exceptions require a separately governed process with an accountable owner and complete audit record.

Related controls: `GASO-GOV-001`, `GASO-APR-001`, `GASO-APR-002`, `GASO-ASR-001`, `GASO-ASR-002`.
