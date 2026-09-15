# Adoption Guide

Use this guide to turn the reference architecture into a reviewable organization-specific control package without treating the repository as a production control plane.

## 1. Select a Profile

Choose [MSSP](profiles/mssp.yaml), [MDR](profiles/mdr.yaml), or [DFIR](profiles/dfir.yaml). Apply conditional controls when the stated condition is true. Record why any catalog control is added, specialized, deferred, or declared not applicable; do not silently remove it.

## 2. Assign Accountable Roles

Map each profile role and each control's `accountable_role` to a real organizational role. Separately identify service owner, policy owner, identity owner, evidence custodian, tool owner, approver, customer approver where required, audit owner, and fleet owner. An agent or assurance component cannot fill an accountable human authorization role.

## 3. Define Boundaries and Dependencies

Document the customer, tenant, case, evidence, environment, target, operation, purpose, destination, and time dimensions that apply. For each control, identify the real system that enforces identity, tenant isolation, approval authority, policy, tool access, evidence preservation, audit durability, deployment, or network egress.

## 4. Complete the Contracts

Copy the relevant files from [`templates/`](templates/), replace synthetic values, and preserve `artifact_type` and schema version. At minimum complete agent cards, tool contracts, policy, governed requests, approval records, evidence manifests and lineage, audit events, and fleet records where applicable. Never put credentials or raw sensitive evidence into these repository artifacts.

## 5. Validate Before Integration

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"

gaso validate <artifacts>
gaso verify-tenant-scope <correlated-artifacts>
gaso evaluate-policy <request> --policy <policy> --approvals <approval-records>
gaso verify-evidence-manifest <manifest> --lineage <lineage-records>
gaso verify-audit-chain <events.jsonl>
gaso replay <events.jsonl>
pytest
```

Treat exit `0` as a passing repository check, exit `1` as a conformance block or fail-closed result, and exit `2` as invalid invocation or configuration. `ALLOW` never means a real action occurred.

## 6. Exercise Negative Cases

For the selected workflow, change tenant, case, target, operation, allowed parameter, approval digest, approval time, evidence source, audit order, and event content one at a time. Each prohibited or inconsistent case must deny, require new approval, or fail closed for the documented reason.

## 7. Review Exceptions and Decisions

Record material tailoring and exceptions in an [architecture decision record](templates/architecture-decision.yaml). Identify owner, rationale, affected controls and profiles, risk, compensating controls, approval, expiration, and reversal plan. An exception must not be encoded as an undocumented wildcard or permanent emergency override.

## 8. Verify External Enforcement

Use [`TRACEABILITY.md`](TRACEABILITY.md) to separate repository checks from external enforcement. Before production use, obtain evidence that the actual identity, approval, PDP, PEP, tool, tenant-isolation, evidence, audit, model-environment, and fleet systems enforce the declared contract. Re-run conformance checks when policy, tool, profile, schema, or workflow scope changes.

## Adoption Exit Criteria

- selected profile and tailoring are approved;
- accountable roles and external enforcement owners are assigned;
- required artifacts validate and correlated scope matches;
- positive and negative tests pass;
- approval and policy changes invalidate old authority;
- audit records replay without re-execution;
- production enforcement evidence is reviewed outside this repository;
- residual risk and exceptions have owners and expiration dates.
