# Architecture Principles

## Purpose

These principles guide the design and interpretation of the Governed Agentic Security Operations Architecture.

They should be used when creating docs, diagrams, workflows, samples, templates, and future proof-of-concept implementations.

This file defines architecture guardrails; it does not replace the detailed control contracts in the deeper directories.

---

## Principle 1: Treat LLM Output as Untrusted Until Reviewed

Agent output MUST NOT be treated as authoritative by default.

LLM and agent outputs may contain:

- hallucinations
- unsupported claims
- weak assumptions
- missing context
- policy violations
- unsafe recommendations
- incorrect mappings
- tenant boundary errors

Agent outputs MUST be evaluated by assurance controls and reviewed by humans when they influence DFIR conclusions, customer-facing outputs, escalation, containment recommendations, policy decisions, or governed tool execution.

---

## Principle 2: Separate Reasoning from Enforcement

Agents can reason. They MUST NOT be the enforcement mechanism.

Runtime enforcement belongs to:

- PEP/PDP
- policy engine
- access controls
- approval workflows
- tool gateways
- audit systems

Agent Judges may evaluate risk, quality, consistency, and evidence support, but they do not replace deterministic policy enforcement.

---

## Principle 3: Require Human Approval for Sensitive Actions

Sensitive actions MUST require human approval. Any pre-approved automated action MUST be explicitly classified as low-risk, policy-authorized, scoped, audited, and outside the sensitive-action category.

Examples include:

- isolate endpoint
- disable user
- revoke token
- change firewall rule
- suppress detection
- close incident
- notify customer
- delete or alter evidence
- initiate containment at customer scale

Human approval is an accountability boundary, not a cosmetic workflow step.

---

## Principle 4: Preserve Evidence Integrity

The architecture MUST preserve sufficient evidence traceability where evidence influences DFIR conclusions, customer-facing outputs, escalation, containment recommendations, policy decisions, or governed tool execution.

Baseline traceability attributes SHOULD include, where applicable:

- original source
- collection timestamp
- chain-of-custody metadata
- transformation history
- analyst notes
- model prompts and outputs
- judge evaluations
- policy decisions
- approvals and actions

LLM-generated summaries, classifications, or conclusions are not evidence by themselves.

---

## Principle 5: Maintain Tenant Isolation

MSSP and MDR architectures MUST enforce strict customer boundaries.

Controls MUST prevent:

- cross-tenant prompt context
- cross-tenant retrieval
- cross-tenant tool execution
- cross-tenant reporting
- shared memory leakage
- shared vector index contamination
- unauthorized customer-to-customer correlation

Tenant context MUST remain explicit across ingestion, retrieval, reasoning, policy evaluation, approval, execution, reporting, and audit trails.

---

## Principle 6: Use Least Privilege and Governed Agent Identity

Agents and tools MUST operate with the minimum permissions required.

Access MUST be:

- scoped
- auditable
- tied to identity
- tied to purpose
- mediated through policy

Access SHOULD be time-bound where possible.

Agents MUST NOT receive broad standing privileges without governance, ownership, scope, monitoring, and auditability.

---

## Principle 7: Fail Closed

If policy cannot be evaluated, identity cannot be verified, tenant context is missing, evidence attribution is insufficient, approval state is invalid, or tool authorization cannot be validated, the workflow MUST fail closed, block, or route to authorized review.

Fail-closed behavior applies to:

- missing tenant ID
- invalid agent identity
- unauthorized tool request
- unsupported sensitive action
- missing approval
- policy engine failure
- schema validation failure

Fail-open behavior is not an acceptable default for governed MSSP, MDR, Cloud IR, or DFIR workflows.

---

## Principle 8: Design for Auditability

Audit records MUST include sufficient context to reconstruct governed decisions, approvals, tool execution, evidence handling, DFIR conclusions, customer-facing outputs, or operational response actions.

Baseline fields SHOULD include, where applicable:

- agent identity
- user or analyst identity
- tenant context
- evidence references
- prompt and output references
- judge result
- policy decision
- approval state
- tool action
- timestamp
- outcome

Auditability is required for accountability, incident review, customer trust, exception handling, and governance review.

---

## Principle 9: Govern Fleet Changes as Operational Releases

Agent packages, prompts, retrieval configurations, tool contracts, policy bundles, detection packages, playbooks, report templates, and sanitized intelligence updates MUST be treated as governed operational releases.

Fleet changes MUST have:

- an accountable owner
- versioning
- validation evidence
- tenant eligibility checks
- policy approval
- rollout scope
- monitoring
- rollback or recall path
- replayable audit records

Cross-tenant learning MUST only be distributed as sanitized, approved, policy-scoped intelligence.

Raw customer data, case context, forensic evidence, tenant identifiers, privileged information, or customer-specific conclusions MUST NOT become shared fleet context, shared memory, prompt content, detection packages, playbooks, report templates, or agent workflows.

---

## Principle 10: Keep Governance Alignment Distinct from Compliance Claims

Frameworks may inform control design. They do not automatically make the architecture compliant.

Use language such as:

- aligned to
- informed by
- mapped to
- considerations
- control themes

Avoid language such as:

- compliant with
- certified
- meets all requirements
- regulatory-ready

Framework alignment should support governance, assurance, threat modeling, and control design without implying certification or regulatory sufficiency.

---

## Principle 11: Use AI to Scale Analysts, Not Replace Accountability

The architecture should improve analyst productivity and consistency while preserving human accountability.

AI may assist with:

- summarization
- correlation
- triage
- hypothesis generation
- report drafting
- evidence organization
- recommendation drafting

Humans remain responsible for validation, judgment, communication, and sensitive approvals.
