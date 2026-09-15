# Fleet Update Poisoning

A compromised build, dependency, manifest, distribution path, or approval can introduce harmful behavior across many tenants.

## Controls

- identify every component and immutable integrity value in the release manifest;
- retain build and source provenance under organizational controls;
- separate build, validation, approval, and deployment authority;
- verify package and manifest integrity at assignment and deployment;
- restrict releases to explicitly eligible profiles and tenants;
- use canary and staged promotion with recorded stop criteria;
- maintain tested rollback and emergency recall paths.

Unknown provenance, integrity mismatch, missing approval, skipped stage, ineligible tenant, unavailable rollback, or recalled version blocks deployment. A trusted signer does not make unsafe content acceptable; conformance and security validation are separate gates.

Production signing, build isolation, distribution, attestation, deployment, monitoring, and revocation are outside this repository.

Related controls: `GASO-GOV-003`, `GASO-FLT-001`, `GASO-FLT-002`, `GASO-FLT-003`.
