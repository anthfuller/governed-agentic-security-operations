# Governed Control Loop

The control loop is intentionally deterministic at the enforcement boundary.

1. Agent proposes an action.
2. Agent output is normalized into `PolicyRequest`.
3. Identity is derived from signed token claims when using the API.
4. Policy engine evaluates tenant, tool, risk, approvals, evidence, residency, and assurance signals.
5. A decision is written to audit.
6. Only `allow` decisions receive execution grants.
7. Tool gateway executes the registered tool.
8. Tool result hash is written to audit for replay.

The agent never receives ambient production credentials. It receives a decision and, if authorized, a scoped execution path.
