# Fail-Closed Agent Rollout Pattern

Use this pattern when distributing a governed agent, policy, prompt package, tool contract, or model-assisted workflow.

## Preconditions

- release manifest is schema valid and integrity metadata is present;
- components and policy versions are registered;
- eligible profiles and tenant scope are explicit;
- automated conformance and required external tests pass;
- rollback target and recall authority are valid;
- release approval binds the exact manifest digest.

## Stages

Promote through offline validation, test environment, canary, limited cohort, and general availability. Each stage records its cohort, start and stop criteria, observations, decision, approver, and next permitted stage. Skipped or unordered stages fail closed.

## Stop Conditions

Pause promotion and block new assignments on scope mismatch, audit gaps, unexpected tool requests, policy errors, approval bypass, integrity failure, unexplained quality regression, or unavailable rollback. Recall active assignments when continued operation could cause harm.

Rollback and recall are governed actions with bounded scope and audit records. They do not imply approval for a replacement release.

Use [`../templates/fleet-release-manifest.yaml`](../templates/fleet-release-manifest.yaml) and [`../templates/fleet-recall-record.yaml`](../templates/fleet-recall-record.yaml).

Related controls: `GASO-GOV-003`, `GASO-FLT-001`, `GASO-FLT-002`, `GASO-FLT-003`.
