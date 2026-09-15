# Fleet Change Approval and Emergency Override

Fleet changes can alter behavior across many customers at once. Every release, rollout expansion, rollback, and recall therefore requires explicit scope, ownership, and a recorded authorization path.

## Normal Change Gate

Before a release may advance, require:

1. a versioned release manifest with component integrity values and provenance;
2. validation results for schemas, policy, tenant isolation, audit replay, and rollback;
3. an accountable fleet owner and change approver;
4. eligible tenant and profile declarations;
5. staged rollout thresholds and stop conditions;
6. a tested rollback target;
7. a release approval bound to the manifest digest and rollout scope.

Failure of any gate stops promotion. A successful canary is evidence for the next gate, not authorization to skip it.

## Emergency Recall

An emergency recall may stop or revoke a harmful release without waiting for normal promotion review. It must still record the caller, authority, reason, affected release, affected scope, timestamp, and required follow-up. Recall must not silently install a new version; a replacement follows the normal change gate.

Emergency authority should be narrowly assigned, time bounded, monitored, and reviewed after use. Production recall also depends on deployment and identity-revocation systems outside this repository.

Use [`../templates/fleet-release-manifest.yaml`](../templates/fleet-release-manifest.yaml) and [`../templates/fleet-recall-record.yaml`](../templates/fleet-recall-record.yaml).

Related controls: `GASO-GOV-003`, `GASO-FLT-001`, `GASO-FLT-002`, `GASO-FLT-003`.
