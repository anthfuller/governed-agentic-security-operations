# Rogue Agent Risk

A rogue agent is an unregistered, altered, ownerless, recalled, or intentionally noncompliant component that attempts to participate in governed workflows.

## Controls

- require a registered agent card, distinct identity, owner, version, lifecycle state, and approved profile;
- allow only registered policy and tool contracts;
- verify release provenance and integrity before fleet assignment;
- block direct access to protected data and tools outside enforcement boundaries;
- constrain delegation to registered identities and explicit scope;
- inventory active agents and reconcile them with runtime and deployment records;
- provide external revocation, recall, and credential-disable paths.

Unknown identity, unknown version, integrity mismatch, suspended lifecycle, missing owner, ineligible tenant, or undeclared delegation denies participation.

The repository can validate declared records. Runtime discovery, workload attestation, network control, deployment inventory, and credential revocation are external requirements.

Related controls: `GASO-IDN-001`, `GASO-IDN-003`, `GASO-FLT-001`, `GASO-FLT-003`.
