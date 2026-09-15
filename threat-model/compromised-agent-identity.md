# Compromised Agent Identity

Stolen credentials or an abused workload identity can make unauthorized activity appear attributable to a registered agent.

## Controls

- assign each agent or service a distinct, owned, lifecycle-managed identity;
- grant only registered tools, operations, tenants, and environments;
- keep credentials out of prompts, model context, output, and general logs;
- prefer short-lived credentials and controlled issuance where supported;
- monitor unusual scope, tool, target, time, and volume patterns;
- revoke credentials and active assignments on suspension, compromise, or recall;
- require policy and PEP checks even for authenticated identities.

Authentication is not authorization. Expired, suspended, recalled, ownerless, over-scoped, or unverifiable identity state fails closed.

Incident handling should revoke externally, preserve audit references, identify affected tenants and decisions, invalidate unsafe derived artifacts, and require controlled recovery before reactivation.

Related controls: `GASO-IDN-001`, `GASO-IDN-002`, `GASO-IDN-003`, `GASO-AUD-001`.
