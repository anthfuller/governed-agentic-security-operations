# Governed Agent Fleet Update Pattern

This pattern separates build evidence, release authorization, tenant assignment, and deployment enforcement.

## Release Record

The fleet release manifest must identify the release, components, immutable integrity values, provenance, owner, compatible profiles, tenant eligibility rule, policy and tool-contract dependencies, test results, rollout stages, rollback target, and approval state.

## Decision Sequence

1. Build and sign or hash the release outside this repository.
2. Validate the manifest and referenced governance artifacts.
3. Verify conformance and organization-required security tests.
4. Approve the exact manifest and rollout plan.
5. At each assignment, check tenant eligibility and current release state.
6. Promote only after the current stage meets recorded criteria.
7. Monitor by release, tenant, operation, and failure reason.
8. Pause, roll back, or recall when a stop condition is reached.

No component may self-promote. A fleet owner cannot use a successful build as release approval, and an approval cannot override an ineligible tenant assignment.

This repository records and validates the governance artifacts. Artifact signing, package distribution, deployment, monitoring, and identity revocation remain external enforcement responsibilities.

Related controls: `GASO-GOV-003`, `GASO-FLT-001`, `GASO-FLT-002`, `GASO-FLT-003`, `GASO-AUD-001`.
