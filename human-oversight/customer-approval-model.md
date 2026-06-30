# Customer Approval Model

## Purpose

This file defines the customer approval model for governed Agentic MSSP / MDR / DFIR security operations.

Customer approval is the customer-side authorization boundary for customer-facing release, customer-impacting action, evidence release, customer-owned operational risk, DFIR reporting, external disclosure, and customer-authorized containment or remediation.

Customer approval provides customer-side authorization only where policy, contract, engagement model, or customer operating procedure requires it. It does not replace analyst review, formal internal approval, PDP authorization, PEP enforcement, Agent Judge assurance, evidence authority, incident command, legal review, compliance review, privacy review, or forensic certification.

## Scope

This model applies to customer-side approval across:

- MSSP and MDR service delivery workflows.
- Cloud Incident Response coordination.
- Private/local LLM-assisted DFIR workflows.
- Customer-facing reports, summaries, findings, recommendations, notifications, and executive updates.
- Customer approval packages.
- Customer-facing DFIR reporting and reportable conclusions.
- Evidence handling, evidence export, evidence release, evidence transformation, retention exceptions, and customer-owned evidence decisions.
- Customer-impacting containment, remediation, access changes, recovery recommendations, or operational risk decisions.
- Contractual escalation, customer notification, external disclosure, and customer-authorized response handling.

This file focuses only on customer-side authorization. Internal approval workflows, analyst review checkpoints, sensitive action approval, escalation, HITL/HOTL oversight, PEP/PDP enforcement, Agent Judge assurance, evidence authority, and forensic certification remain separate controls.

## Non-Goals

Customer approval MUST NOT be treated as:

- Analyst review.
- Formal internal approval.
- PDP authorization.
- PEP enforcement.
- Agent Judge assurance.
- Evidence authority.
- Forensic certification.
- Legal, regulatory, or compliance determination.
- Incident truth or proof of containment, remediation, recovery, attribution, impact, or closure.
- Permission for agents, tools, models, or workflows to self-authorize customer-impacting actions.

Customer approval MUST NOT bypass policy enforcement, evidence validation, human review, internal approval requirements, customer contractual requirements, audit logging, or fail-closed behavior.

## Required Customer Approval Inputs

Customer approval workflows MUST receive enough structured context to support customer-side authorization, audit replay, scope validation, and downstream enforcement.

| Input | Requirement | Purpose |
|---|---|---|
| `customer_approval_request_id` | MUST | Unique identifier for the customer approval request. |
| `customer_approval_record_id` | MUST when customer approval is requested, granted, denied, expired, revoked, escalated, or blocked | Links the request to the customer approval record. |
| `workflow_id` | MUST | Identifies the originating workflow, run, case, or process. |
| `tenant_id` | MUST for tenant-scoped, multi-tenant, workspace-scoped, subscription-scoped, account-scoped, customer-facing, or governed workflows | Preserves tenant boundary context. |
| `customer_id` | MUST for MSSP, MDR, DFIR, customer-scoped, customer-facing, or multi-customer workflows | Preserves customer boundary separately from tenant identity. |
| `case_id` or `incident_id` | MUST when the request relates to an investigation, alert, incident, ticket, report, evidence package, or DFIR matter | Links approval to the governed operational record. |
| `requested_action` | MUST | Describes the proposed release, notification, evidence handling, containment, remediation, escalation, disclosure, report, or customer-impacting action. |
| `customer_impact_summary` | MUST | Summarizes the customer-facing, operational, evidence, reporting, contractual, or disclosure impact. |
| `output_destination` | MUST when release, routing, disclosure, reporting, evidence handling, governance evidence, or downstream use depends on destination | Identifies where output is sent, stored, released, displayed, exported, or consumed. |
| `evidence_object_ids` | MUST when approval relies on evidence, investigation context, DFIR findings, governance evidence, or customer-facing content | Preserves evidence traceability. |
| `evidence_tenant_ids` or equivalent tenant-attribution metadata | MUST when evidence is referenced in multi-tenant or customer-scoped workflows | Preserves evidence-to-tenant traceability. |
| `evidence_customer_ids` or equivalent customer-attribution metadata | MUST when evidence is referenced in customer-scoped workflows | Preserves evidence-to-customer traceability. |
| `knowledge_store_or_memory_scope` | MUST when RAG, vector search, shared memory, customer context, case memory, evidence retrieval, knowledge retrieval, or retrieved context affects customer approval | Defines approved retrieval, memory, tenant, customer, case, evidence, retention, freshness, and reuse boundary. |
| `knowledge_memory_scope_result` | MUST when retrieval or memory scope is evaluated | Records whether retrieval, memory, vector-store, customer-context, case-memory, evidence-retrieval, retention, and reuse scope remained within approved boundaries. |
| `data_classification` | MUST when classification affects release, disclosure, evidence handling, reporting, routing, retention, reuse, approval, or downstream use | Preserves data-handling context. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity, privacy, legal, regulated, or customer-specific handling context. |
| `allowed_use` | MUST when use is constrained to workflow, case, customer, legal, governance, evidence-handling, reporting, public disclosure, or DFIR purposes | Defines permitted downstream use. |
| `retention_policy_id` | MUST when retention affects evidence, retrieved context, output storage, release, reuse, disposal, or audit support | Preserves retention and disposal boundary. |
| `approver_identity` | MUST when customer approval is granted, denied, escalated, revoked, or expired by a customer-side authority | Identifies the customer approver or customer-authorized representative. |
| `approver_authority_source` | MUST | Identifies the contract, engagement model, customer contact model, delegation, role, approval matrix, ticketing workflow, or other authority source used to validate approver authority. |
| `approval_expiration` or `approval_valid_until` | MUST where scoped approval is time-bound or requires revalidation | Defines the approval validity boundary. |
| `policy_decision_reference` | MUST when customer approval is triggered by PDP result, policy obligation, approval requirement, or exception path | Links customer approval to policy context. |
| `pep_enforcement_reference` | MUST where applicable | Links customer approval to PEP enforcement outcome, obligations, or execution gate. |
| `human_review_record_id` | MUST when human review is required or completed before customer approval | Links customer approval to the human review outcome. |
| `approval_record_id` | MUST when formal internal approval is required or completed before customer approval | Links customer approval to internal approval context. |
| `audit_reference_id` | MUST when customer approval is consumed by governed workflows | Supports audit reconstruction. |
| `correlation_ids` | MUST when available | Links related workflow, tool, evidence, policy, review, approval, customer approval, execution, and audit records. |

## Customer Approval Outcomes

Customer approval workflows MUST define explicit outcomes.

| Outcome | Meaning |
|---|---|
| `CUSTOMER_APPROVED` | Customer-side authorization is granted within the recorded scope, conditions, and validity boundary. |
| `CUSTOMER_REJECTED` | Customer-side authorization is denied and the requested release, action, evidence handling, disclosure, or downstream use MUST NOT proceed under the current request. |
| `REQUEST_MORE_EVIDENCE` | The customer approver requires additional evidence, explanation, scope, impact, or handling context before deciding. |
| `ESCALATE_TO_CUSTOMER_AUTHORITY` | The request must be routed to a different or higher customer authority, designated approver, legal contact, executive sponsor, or contractual escalation path. |
| `CUSTOMER_APPROVAL_EXPIRED` | The approval request or prior customer approval is no longer valid. |
| `CUSTOMER_APPROVAL_REVOKED` | A previously granted customer approval has been withdrawn before execution, release, or continued use. |
| `BLOCKED_FAIL_CLOSED` | The workflow cannot proceed because required customer approval, authority, scope, evidence, policy, review, approval, or audit context is missing or invalid. |

Customer approval outcomes MUST be structured workflow states. Free-text comments, informal messages, ticket notes, or silence MUST NOT be treated as customer approval unless the operating model explicitly permits that form of authorization and captures it as an auditable customer approval record.

## Customer Approval Boundary

Customer approval is required before customer-facing release, customer-impacting action, evidence release, customer notification, external disclosure, or customer-owned operational risk where policy, contract, engagement model, statement of work, customer operating procedure, or delegated customer authority model requires it.

Customer approval MUST be scoped to the specific customer, tenant, case, evidence set, requested action, output destination, allowed use, validity period, and conditions.

Customer approval MUST NOT be reused across tenants, customers, cases, evidence sets, destinations, actions, reports, or time windows unless the operating model explicitly permits reuse and the reuse is recorded, scoped, and audited.

## Relationship to Analyst Review, Formal Approval, PDP/PEP, and Agent Judges

Customer approval is separate from analyst review, formal internal approval, PDP authorization, PEP enforcement, and Agent Judge assurance.

| Component | Responsibility |
|---|---|
| Analyst review | Validates evidence support, tenant/customer scope, uncertainty, and operational readiness. It does not provide customer-side authorization. |
| Formal internal approval | Provides internal human authorization where required. It does not replace customer approval where customer-side authorization is required. |
| Customer approval | Provides customer-side authorization for the scoped customer-facing release, customer-impacting action, evidence handling, notification, external disclosure, or customer-owned operational risk. |
| PDP | Produces governed authorization decisions according to the policy contract. |
| PEP | Enforces PDP decisions and obligations at the workflow, tool, release, or execution boundary. |
| Agent Judge | Provides assurance findings only. It does not approve customer release, customer notification, evidence release, containment, remediation, or external disclosure. |
| Evidence authority | Preserves evidence handling, provenance, integrity, retention, and chain-of-custody context. It is not replaced by customer approval. |
| Forensic authority | Validates forensic conclusions where required. It is not replaced by customer approval. |

Customer approval MUST NOT convert unsupported claims, missing evidence, unresolved Agent Judge findings, policy denial, tool success, or model output into approved operational facts.

## Execution-Time Revalidation

Before execution, release, notification, disclosure, evidence handling, or downstream use, the governed workflow, PEP, release gate, or execution gate MUST revalidate:

- Customer approval status.
- Customer approval scope.
- Customer approval expiration or validity.
- Customer approver authority.
- Tenant, customer, case, evidence, and output destination.
- Evidence tenant and customer attribution.
- Knowledge store or memory scope where applicable.
- Knowledge memory scope result where retrieval or memory scope was evaluated.
- Data classification, sensitivity label, allowed use, and retention policy.
- PDP decision and obligations.
- PEP enforcement obligations where applicable.
- Human review record where required.
- Formal internal approval record where required.
- Audit logging and correlation identifiers.

If any required revalidation fails, execution, release, notification, disclosure, evidence handling, or downstream use MUST NOT proceed.

## Fail-Closed Conditions

Customer approval workflows MUST fail closed, remain blocked, quarantine output, or route to controlled review when:

- Customer approval is missing, expired, revoked, incomplete, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope.
- Customer approver identity, approver authority source, approval scope, approval expiration, customer approval outcome, or decision rationale is missing, ambiguous, unauthorized, expired, revoked, stale, inconsistent, unauditable, or out of scope.
- Output destination is missing, ambiguous, unauthorized, inconsistent, or out of scope where customer-facing release, customer notification, external disclosure, evidence handling, reporting, or downstream use depends on it.
- Evidence object identifiers, evidence tenant attribution, or evidence customer attribution are missing, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where evidence affects customer approval or downstream use.
- Required retrieval or memory scope, knowledge memory scope result, data classification, sensitivity label, allowed use, retention policy, approval record, human review record, or audit context is missing, expired, revoked, ambiguous, unauthorized, stale, inconsistent, unauditable, or out of scope where customer approval, customer-facing release, DFIR conclusions, governance evidence, approval routing, execution, or downstream use depends on it.
- PDP returns `DENY`; escalation MAY occur only for separately governed exception review where explicitly permitted by policy and MUST NOT permit execution or release by default.
- PDP returns `REQUIRE_APPROVAL` and required formal approval or customer approval is not present.
- PEP enforcement obligations cannot be validated where execution or release depends on them.
- Customer-facing content contains unsupported claims, missing evidence, unresolved limitations, or unapproved disclosure.
- The workflow attempts to treat analyst review, ticket comments, silence, prior discussion, Agent Judge findings, PDP result, or general engagement participation as customer approval.
- Audit logging or context preservation fails.

Fail-closed handling MUST preserve the customer approval request, evidence references, customer approval reason, routing reason, approver context, approval context where applicable, customer approval context, policy context, execution or release attempt where applicable, and audit reference.

## Audit Requirements

Customer approval workflows MUST audit:

- Customer approval request identifier.
- Customer approval record identifier.
- Requester identity where available.
- Approver identity.
- Approver authority source.
- Customer approval status, outcome, rationale, timestamp, expiration, revocation, and conditions.
- Tenant, customer, case, workflow, and output destination context.
- Requested action, customer impact summary, routing path, and downstream use.
- Evidence object identifiers and evidence tenant/customer attribution metadata.
- `knowledge_store_or_memory_scope` where retrieval or memory influenced approval, evidence interpretation, routing, customer-facing wording, governance evidence, approval package, DFIR conclusions, execution, or downstream use.
- `knowledge_memory_scope_result` where retrieval or memory scope was evaluated.
- `data_classification`, `sensitivity_label`, `allowed_use`, and `retention_policy_id` where sensitive data handling, release, reuse, retention, customer-facing output, governance evidence, approval routing, execution, or DFIR conclusions are involved.
- Policy decision reference and policy obligations where applicable.
- PEP enforcement reference and enforcement result where applicable.
- `human_review_record_id` where human review is required or completed.
- `approval_record_id` where formal internal approval is required or completed.
- `customer_approval_record_id` where customer approval is requested, granted, denied, expired, revoked, escalated, or blocked.
- Execution result, release result, disclosure result, notification result, or evidence-handling result where applicable.
- Fail-closed, escalation, request-more-evidence, rejection, expiration, revocation, exception, or correction events.
- Audit reference identifiers and correlation identifiers needed for reconstruction.

Audit records MUST support reconstruction of customer approval request, customer approval record, requester identity, approver identity, approver authority, tenant, customer, case, evidence, retrieval/memory scope, classification, sensitivity label, allowed use, retention policy, output destination, policy decision, PEP enforcement, routing, downstream use, and execution result.

## Operational Anti-Patterns

The following patterns violate this customer approval model:

- Treating customer notification as customer approval.
- Treating ticket comments as customer approval without a structured customer approval record.
- Treating silence, timeout, or lack of objection as customer approval.
- Treating prior discussions as reusable customer approval outside the approved scope.
- Treating analyst approval as customer approval.
- Treating internal formal approval as customer approval.
- Treating Agent Judge findings as customer approval.
- Treating a PDP decision as customer approval.
- Treating PEP enforcement as customer approval.
- Treating general engagement participation as customer approval.
- Reusing customer approval across tenants, customers, cases, evidence sets, destinations, reports, actions, or time windows without explicit scoped authorization.
- Releasing customer-facing output without validating customer approval where required.
- Executing customer-impacting containment or remediation without validating customer approval where required.
- Releasing evidence, external disclosures, or DFIR conclusions without required customer approval where required.
- Allowing agents, tools, workflows, or models to approve their own customer-impacting actions.
- Treating private/local LLM execution as proof of correctness, customer approval, or forensic validity.
- Treating Entra Agent ID, agent registry, identity governance, or lifecycle controls as operational SOC agents.

## Acceptance Criteria

This file is acceptable when:

- The file is titled Customer Approval Model and focuses only on customer-side authorization.
- Customer approval is defined as the customer-side authorization boundary for customer-facing release, customer-impacting action, evidence release, customer-owned operational risk, DFIR reporting, external disclosure, and customer-authorized containment or remediation.
- Customer approval remains separate from analyst review, formal internal approval, PDP authorization, PEP enforcement, Agent Judge assurance, evidence authority, and forensic certification.
- Required customer approval inputs preserve customer approval request, customer approval record, workflow, tenant, customer, case, requested action, customer impact, destination, evidence, retrieval/memory, classification, sensitivity label, allowed use, retention, approver authority, policy, PEP, human review, internal approval, audit, and correlation context.
- Customer approval outcomes are explicit structured states.
- Execution-time revalidation checks customer approval status, scope, expiration, authority, tenant/customer/case/evidence/output destination, PDP/PEP obligations, and audit logging before execution or release.
- Fail-closed handling exists for missing, expired, revoked, ambiguous, unauthorized, stale, inconsistent, unauditable, or out-of-scope customer approval context.
- Audit replay can reconstruct customer approval request, customer approval record, requester identity, approver identity, approver authority, tenant, customer, case, evidence, retrieval/memory scope, data classification, sensitivity label, allowed use, retention policy, output destination, policy decision, PEP enforcement, routing, downstream use, and execution result.
