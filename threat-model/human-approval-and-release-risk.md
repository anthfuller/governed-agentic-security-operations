# Human Approval and Release Risk

Approval can be spoofed, reused, rushed, expired, detached from the reviewed artifact, or confused with ordinary analyst review.

## Controls

- separate reviewer, approver, customer approver, and release authority roles;
- authenticate the approver through the organization's approval system;
- display the exact action, target, parameters, scope, evidence, risk, and limitations;
- bind the decision to request and policy identifiers plus an expiration;
- require a new decision after any material change;
- record rejection, timeout, revocation, and escalation as explicit states;
- measure repeated or unusually fast approvals as review signals, not automatic guilt.

Missing, ambiguous, stale, mismatched, or unverifiable approval is denied. Customer authorization cannot be inferred from internal approval, and emergency authority cannot silently become a permanent exception.

Related controls: `GASO-APR-001`, `GASO-APR-002`, `GASO-APR-003`, `GASO-GOV-001`.
