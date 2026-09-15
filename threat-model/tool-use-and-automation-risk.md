# Tool Use and Automation Risk

Tool access can turn an incorrect or manipulated recommendation into a customer-impacting change.

## Required Boundary

Every tool operation must be registered in a current contract that declares its owner, permitted operations, parameters, scope, risk, identity, and failure behavior. The external PEP must compare the exact request against the current policy decision and all required approvals immediately before execution.

Agents, model output, assurance checks, and analyst review do not issue execution authority. Credentials must be least privileged, short lived where supported, and unavailable to the reasoning component.

Unknown tool or operation, altered target or parameter, missing or expired decision, missing approval, scope mismatch, stale contract, or unavailable audit sink denies execution. Retrying cannot broaden scope or bypass a denial.

Test parameter substitution, replay, target swapping, concurrency, timeout, partial failure, and misleading success responses in the production integration.

Related controls: `GASO-TOL-001`, `GASO-TOL-002`, `GASO-TOL-003`, `GASO-IDN-002`.
