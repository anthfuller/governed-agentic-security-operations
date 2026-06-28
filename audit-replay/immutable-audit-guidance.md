# Immutable Audit Guidance

## Purpose

This document defines immutable audit guidance for governed agentic MSSP, MDR, SOC, cloud incident response, and private/local LLM-assisted DFIR workflows.

Immutable audit records provide a tamper-evident history of agent activity, policy decisions, human approvals, tool execution, evidence handling, tenant-boundary decisions, customer-facing output release, fleet rollout, rollback, recall, and exception handling.

The goal is to make governed workflows replayable without turning the audit store into a raw evidence repository, shared tenant memory, or unrestricted operational data lake.

## Scope

This guidance applies to audit records created by:

- agent invocation and task execution;
- context assembly and retrieval;
- evidence reference use;
- agent output generation;
- AI assurance and Agent Judge evaluation;
- policy request and policy decision events;
- human review and approval workflows;
- customer approval workflows;
- tool request, authorization, and execution events;
- case note, report, or customer-facing output release;
- tenant-boundary, case-boundary, and evidence-boundary enforcement;
- local/private LLM-assisted DFIR workflows;
- fleet package validation, rollout, rollback, and recall;
- sanitized intelligence release and propagation;
- exception, denial, escalation, and fail-closed behavior.

Out of scope:

- production database design;
- vendor-specific storage configuration;
- legal advice about retention or disclosure;
- forensic evidence storage design;
- full audit-event schema definition;
- implementation-specific SIEM, data lake, or archive configuration.

Detailed event field definitions belong in `audit-event-model.md`. Replay requirements belong in `replayability-requirements.md`. Correlation rules belong in `audit-correlation-model.md`.

## Core Principle

Immutable audit records must preserve a replayable, tamper-evident history of governed decisions and outcomes.

The audit chain must be strong enough to reconstruct who or what acted, under which tenant and case scope, using which context and evidence references, under which policy decision, with which approval, through which tool or release path, and with what outcome.

Immutable audit does not prove that a decision was correct. It proves that the decision path can be inspected, correlated, challenged, and reconstructed.

## What Immutability Means

For this architecture, immutable audit means audit records are:

| Property | Meaning |
|---|---|
| Append-only | Existing records are not edited in place. Corrections are added as new events. |
| Tamper-evident | Unauthorized modification, deletion, reordering, or backdating can be detected. |
| Time-bound | Events include trusted timestamps and ordering metadata. |
| Identity-bound | Events identify the agent, user, service, workflow, or control that produced them. |
| Scope-bound | Events include tenant, customer, case, evidence, release, or workflow scope where applicable. |
| Correlatable | Events carry identifiers that connect them into a replayable chain. |
| Protected | Audit records are encrypted, access-controlled, monitored, and retained according to policy. |
| Recoverable | Audit records remain available for review, replay, investigation, and governance needs. |

Immutable audit does not mean:

- all data is retained forever;
- raw evidence is copied into the audit log;
- customer data can be mixed across tenants;
- prompts, evidence, secrets, or credentials should be stored without minimization;
- immutable storage alone satisfies compliance, legal, or evidentiary requirements;
- audit records replace human review, policy enforcement, chain of custody, or evidence validation.

## Records Requiring Immutable Handling

The following records should be treated as immutable when they affect governed workflow behavior, customer trust, evidence handling, policy decisions, or operational outcomes.

| Record Type | Why It Requires Immutable Handling |
|---|---|
| Agent invocation | Establishes which agent version acted, under which purpose and scope. |
| Context package record | Shows what information was available to the agent at decision time. |
| Retrieval record | Shows which sources, indexes, evidence references, or knowledge items were retrieved. |
| Agent output | Captures recommendations, summaries, findings, assumptions, and requested actions. |
| Agent Judge result | Records assurance findings, unsupported-claim checks, boundary checks, and review triggers. |
| Policy request | Captures the action, tool, scope, risk, evidence references, and requested authorization. |
| Policy decision | Records `ALLOW`, `DENY`, `REQUIRE_REVIEW`, `REQUIRE_APPROVAL`, or `FAIL_CLOSED` and the reason for the decision. |
| Human review record | Captures reviewer assessment, quality decision, requested correction, or escalation. |
| Human approval record | Captures the accountable authorization for a sensitive action or release. |
| Customer approval record | Captures customer-specific authorization where required. |
| Tool execution record | Records what tool executed, against what target, under what authorization, and with what result. |
| Evidence handling record | Captures evidence reference use, transfer, access, transformation, or chain-of-custody event. |
| Report release record | Records customer-facing or externally visible output approval and release. |
| Boundary enforcement record | Captures tenant, case, evidence, region, retention, or sovereignty boundary decisions. |
| Failure or exception record | Preserves denied, failed, escalated, or fail-closed behavior. |
| Fleet rollout record | Records package validation, rollout gates, tenant eligibility, and release scope. |
| Rollback or recall record | Captures emergency stop, version pinning, session termination, rollback, and notification. |
| Sanitized intelligence release record | Captures sanitization, review, policy decision, destination scope, and recall path. |
| Policy or prompt change record | Preserves versioned changes to control behavior, instructions, or release logic. |

## Immutable Audit Architecture

The immutable audit path should be separate from normal operational logging.

```text
Workflow event
    ↓
Audit event creation
    ↓
Schema validation
    ↓
Sensitive-data minimization
    ↓
Canonicalization
    ↓
Hashing and signing
    ↓
Append-only write
    ↓
Replication or archival protection
    ↓
Correlation index
    ↓
Replay, review, investigation, and governance use
```

The append-only audit store is the system of record. Search indexes, dashboards, SIEM copies, case views, and analytics tables may be derived from it, but they should not be treated as the authoritative immutable record.

## Separation of Immutable History and Operational State

Operational systems often need mutable state. Cases are updated, tickets are reassigned, agent versions are retired, detections are tuned, and reports are revised.

Immutable audit should not prevent normal operations. It should record them.

| Mutable Operational State | Immutable Audit History |
|---|---|
| Current case status | Case status change events |
| Current agent lifecycle state | Agent lifecycle transition events |
| Current policy bundle | Policy version activation and retirement events |
| Current detection version | Detection release, rollback, and supersession events |
| Current report draft | Draft creation, review, approval, revision, and release events |
| Current approval queue | Approval request, approval, rejection, expiration, and escalation events |
| Current retrieval index | Index creation, ingestion, quarantine, recall, and removal events |

Systems may update current state. They must not erase the history of how that state was reached.

## Audit Event Envelope Requirements

Immutable audit events should use a consistent event envelope. The full event schema may vary by implementation, but the envelope should preserve enough information for ordering, integrity, scope, and replay.

Recommended baseline fields:

| Field | Purpose |
|---|---|
| `audit_event_id` | Unique immutable event identifier. |
| `event_type` | Type of event recorded. |
| `event_version` | Version of the audit-event schema or contract. |
| `occurred_at` | Time the underlying activity occurred. |
| `recorded_at` | Time the audit event was written. |
| `emitter_id` | System, service, agent, tool, or control that emitted the event. |
| `actor_type` | Human, agent, service, tool, policy engine, approval workflow, or system. |
| `actor_id` | Identity of the acting party. |
| `tenant_id` | Tenant or customer boundary where applicable. |
| `customer_id` | Customer or service delivery boundary where applicable. |
| `case_id` | Incident, investigation, or case boundary where applicable. |
| `workflow_id` | Workflow instance identifier. |
| `correlation_id` | End-to-end trace identifier. |
| `parent_event_id` | Prior event in the workflow chain where applicable. |
| `source_refs` | References to source events, evidence, context packages, policy records, or approvals. |
| `classification` | Data classification and handling label. |
| `decision` | Decision or outcome where applicable. |
| `outcome` | Success, failure, denied, approved, rejected, recalled, escalated, or failed closed. |
| `retention_label` | Retention requirement or archive class. |
| `legal_hold` | Whether the record is under legal hold. |
| `previous_hash` | Hash of the prior event in the relevant chain where applicable. |
| `event_hash` | Hash of the canonicalized event payload. |
| `signature` | Signature or integrity proof where implemented. |
| `key_id` | Signing key or integrity-key reference. |

## Example Immutable Audit Event

```json
{
  "audit_event_id": "audit-2026-00010422-0007",
  "event_type": "policy.decision.created",
  "event_version": "1.0",
  "occurred_at": "2026-05-22T10:24:31Z",
  "recorded_at": "2026-05-22T10:24:33Z",
  "emitter_id": "policy-decision-service",
  "actor_type": "policy_engine",
  "actor_id": "pdp-primary",
  "tenant_id": "customer-a",
  "customer_id": "cust-a",
  "case_id": "inc-10422",
  "workflow_id": "wf-10422-triage-01",
  "correlation_id": "corr-10422-01",
  "parent_event_id": "audit-2026-00010422-0006",
  "source_refs": {
    "policy_request_ref": "policy-request://customer-a/inc-10422/req-01",
    "agent_output_ref": "agent-output://customer-a/inc-10422/out-0091",
    "judge_result_ref": "judge-result://customer-a/inc-10422/judge-004",
    "evidence_refs": [
      "evidence://customer-a/inc-10422/events/evt-001",
      "evidence://customer-a/inc-10422/events/evt-004"
    ]
  },
  "classification": "customer-security-audit",
  "decision": "REQUIRE_APPROVAL",
  "decision_reason": "Endpoint isolation is a high-impact containment action.",
  "outcome": "approval_required",
  "retention_label": "security-operations-audit",
  "legal_hold": false,
  "previous_hash": "sha256:previous-event-hash",
  "event_hash": "sha256:canonical-event-hash",
  "signature": "sig:signature-over-event-hash",
  "key_id": "audit-signing-key-2026-q2"
}
```

This is an architecture example. Production implementations should validate field names, schemas, cryptographic controls, retention labels, and access controls before use.

## Hashing, Signing, and Ordering

Immutable audit should make tampering detectable.

Recommended integrity controls:

1. Canonicalize each audit event before hashing.
2. Compute a hash over the canonicalized event body.
3. Link related events using `parent_event_id`, `correlation_id`, and where appropriate `previous_hash`.
4. Sign the event hash or signed envelope using a managed signing key.
5. Preserve the signing key identifier and signing timestamp.
6. Use key rotation without breaking historical verification.
7. Maintain independent ordering metadata such as sequence number, ledger offset, or append timestamp.
8. Detect gaps, duplicate sequence values, invalid signatures, unexpected rewrites, and out-of-order events.

Hashing and signing should be applied to the audit record, not to mutable indexes or rendered dashboards.

## Chain Design

Not every event needs to be in one global chain. Large security operations environments may need multiple correlated chains.

Recommended chain scopes:

| Chain Scope | Use |
|---|---|
| Workflow chain | Reconstructs one governed workflow from invocation to outcome. |
| Tenant/case chain | Reconstructs activity within a tenant, case, or investigation boundary. |
| Evidence chain | Reconstructs evidence access, transformation, and reference use. |
| Policy chain | Reconstructs policy requests, decisions, approvals, denials, and exceptions. |
| Tool execution chain | Reconstructs tool requests, authorization, execution, and result handling. |
| Fleet release chain | Reconstructs package validation, approval, rollout, rollback, and recall. |
| Sanitized intelligence chain | Reconstructs sanitization, approval, destination scope, release, and recall. |

Chains should be connected through correlation identifiers rather than forced into one oversized audit stream.

## Storage Requirements

Immutable audit storage should meet the following requirements.

| Requirement | Guidance |
|---|---|
| Append-only writes | Prevent in-place modification of committed records. |
| Write authorization | Only approved audit emitters may write records. |
| Read authorization | Access must be role-scoped, tenant-scoped, case-scoped, and logged. |
| Encryption | Encrypt records in transit and at rest. |
| Retention | Apply retention labels based on record type, customer obligation, legal hold, and policy. |
| Legal hold | Support preservation when investigation, litigation, or customer obligation requires it. |
| Replication | Protect against loss, corruption, or regional outage according to requirements. |
| Time integrity | Use trusted time sources and record both occurrence time and write time. |
| Integrity verification | Support hash and signature verification during replay and periodic checks. |
| Index rebuild | Search indexes should be rebuildable from immutable source records. |
| Access logging | Reads, exports, administrative actions, and break-glass access must be audited. |
| Deletion control | Deletion, expiration, or tombstoning must be governed and auditable. |

Immutable audit storage may be implemented using WORM storage, append-only ledger patterns, object lock, signed event streams, write-once archives, or equivalent controls. The architecture does not require blockchain.

## Data Minimization

Immutable audit records often outlive operational workflow state. They must avoid unnecessary sensitive content.

Audit records should prefer references, hashes, and stable identifiers over full sensitive payloads.

Do record:

- evidence references;
- context package references;
- prompt template references;
- prompt hash where appropriate;
- model or route reference;
- output reference;
- policy request and decision references;
- approval record references;
- tool execution references;
- release package and version references;
- high-level sanitization summary;
- decision reason and outcome.

Do not record by default:

- raw evidence artifacts;
- full disk or memory content;
- packet captures;
- credentials, keys, tokens, or secrets;
- unnecessary raw log bodies;
- unrestricted customer data;
- full prompt context when it contains sensitive case material;
- unredacted customer report drafts unless policy allows it;
- legal, privileged, or regulated content beyond required references.

If full content must be retained for replay or legal requirements, it should be stored in an approved evidence or records system with stronger access control, classification, and retention handling. The immutable audit event should reference that controlled object rather than duplicate it unnecessarily.

## Prompt, Model, and Context Audit

Agentic workflows require auditability of model behavior, but prompt and context logging can expose sensitive data if handled carelessly.

Recommended audit pattern:

| Artifact | Preferred Audit Handling |
|---|---|
| Prompt template | Store template version and hash. |
| Runtime prompt | Store reference and hash; store full content only when approved. |
| System instruction | Store version and hash. |
| Model route | Store model route or approved model reference. |
| Retrieval context | Store retrieval query reference, source references, evidence references, and result identifiers. |
| Context package | Store context package ID, hash, tenant, case, and source references. |
| Agent output | Store output reference, hash, classification, evidence references, and release state. |
| Memory write | Store destination, policy decision, classification, write reason, and recall path. |

Model output should not be treated as evidence by itself. Audit records should identify which evidence references, context packages, and reviewer actions supported downstream conclusions.

## Tenant and Customer Isolation

Audit systems must preserve tenant and customer boundaries.

Required controls:

- every tenant-scoped audit record must include tenant or customer context;
- records must not be written into shared audit streams without scope metadata;
- audit search must enforce tenant, customer, case, and role restrictions;
- cross-tenant queries must be limited to authorized governance, security, legal, or service-assurance roles;
- shared dashboards must aggregate or sanitize customer data;
- audit exports must be scoped and approved;
- destination tenants must not see source-tenant evidence references unless explicitly authorized;
- sanitized intelligence release records must protect internal source references from destination consumers.

A missing, ambiguous, or mismatched tenant identifier must trigger fail-closed handling or authorized review before audit-dependent workflow execution proceeds.

## Evidence and Chain-of-Custody Handling

Immutable audit supports evidence traceability. It does not replace the evidence system of record.

Audit records should capture:

- evidence object references;
- collection or access events;
- transformation or derived-output events;
- reviewer validation events;
- chain-of-custody references;
- evidence hash or manifest reference where appropriate;
- case and custodian scope where authorized;
- access, export, quarantine, or transfer decisions;
- tool or model interaction with evidence-derived content.

Audit records should not copy raw evidence into the audit log unless the evidence handling model explicitly allows it.

For private/local LLM-assisted DFIR, audit must preserve enough information to reconstruct what evidence-derived context was supplied to the model, which prompts and model configuration were used, what output was generated, which analyst reviewed it, and how the finding was supported or rejected.

## Policy and Approval Integrity

Policy decisions and approvals must be immutable when they authorize, deny, block, escalate, or release governed activity.

Required records:

- policy request submitted;
- policy decision returned;
- policy bundle version used;
- policy input context references;
- decision reason;
- approval request created;
- approver identity and authority;
- approval, rejection, expiration, revocation, or escalation;
- approval scope and expiration;
- tool execution or release result.

A tool execution record must reference the policy decision and approval record that authorized it. A customer-facing release record must reference the review and approval path that authorized release.

Agents, Agent Judges, prompts, or confidence scores must not be recorded as approval authorities unless a formal human or policy approval actually occurred.

## Fleet Rollout, Rollback, and Recall Audit

Fleet operations can affect many tenants. Immutable audit must preserve the release and recovery path.

Required fleet audit records:

| Record | Required Content |
|---|---|
| Fleet change request | Owner, purpose, affected packages, risk, scope, and expected behavior. |
| Package manifest | Agent version, prompt version, model route, policy bundle, tool contracts, monitoring profile, rollback target. |
| Validation record | Test results, tenant-boundary checks, policy checks, evidence checks, and failure handling. |
| Approval record | Engineering, service owner, policy owner, customer, or emergency approval where required. |
| Tenant eligibility record | Included tenants, excluded tenants, service tiers, region, sovereignty, contractual constraints. |
| Rollout gate record | Canary, cohort, broad rollout, hold, failure, or rollback decision. |
| Monitoring record | Adoption, denials, unsupported claims, policy exceptions, tool failures, and customer impact. |
| Rollback record | Version reverted, affected scope, reason, authority, and outcome. |
| Recall record | Kill switch, session termination, package quarantine, credential revocation, notification, and recovery. |

Fleet audit must make it possible to answer:

- which version was active for a tenant at a given time;
- which package elements changed;
- who approved the release;
- which tenants were eligible or excluded;
- which rollout gate allowed expansion;
- what monitoring signal triggered rollback or recall;
- which cases, outputs, or actions may have been affected.

## Sanitized Intelligence Release Audit

Sanitized intelligence propagation must be replayable.

Immutable records should capture:

- source classification;
- source tenant and case reference visible only to authorized reviewers;
- proposed release category;
- sanitization method;
- direct and indirect identifier checks;
- evidence support or engineering validation;
- human review;
- release approval;
- policy decision;
- destination scope;
- tenant eligibility;
- release channel;
- version;
- monitoring profile;
- retention label;
- rollback, removal, or recall path.

Destination tenants should receive only approved sanitized material. They should not receive internal source evidence references unless policy explicitly authorizes that visibility.

## Exception, Failure, and Degraded-Mode Audit

Failures are part of the governed workflow and must be recorded.

Required failure records include:

- missing tenant, case, policy, approval, evidence, or audit context;
- failed schema validation;
- denied policy request;
- fail-closed decision;
- unavailable policy engine;
- unavailable approval workflow;
- unavailable audit logger;
- tool execution failure;
- agent identity failure;
- tenant-boundary mismatch;
- retrieval boundary failure;
- unsupported-claim failure;
- audit write failure;
- replay verification failure;
- emergency override or break-glass use.

If audit logging is unavailable for a sensitive action, customer-facing release, evidence-sensitive workflow, or fleet rollout, the workflow must halt, fail closed, or route to an approved degraded-mode process.

A degraded-mode process must still create a durable record as soon as possible and must preserve the reason, authority, scope, time, and recovery steps.

## Corrections, Redactions, and Retention

Immutable audit records should not be edited in place to correct mistakes.

Use append-only correction events.

| Need | Required Handling |
|---|---|
| Correct wrong metadata | Add a correction event referencing the original event. |
| Supersede an output | Add a supersession event and link the replacement. |
| Revoke approval | Add a revocation event and stop dependent workflow paths. |
| Recall release | Add recall events and record affected scope. |
| Remove recalled retrieval content | Add quarantine/removal event and verify retrieval block. |
| Apply retention expiration | Add retention or tombstone event where policy requires. |
| Handle legal hold | Add legal-hold event and preserve required records. |
| Handle redaction | Add redaction marker and retain authorized proof according to policy. |

Retention and deletion requirements may vary by jurisdiction, contract, legal hold, and data classification. The architecture should support lawful retention expiration or controlled redaction without silently rewriting history.

When deletion or redaction is required, preserve an auditable record that a governed removal occurred, who authorized it, which policy applied, which scope was affected, and whether cryptographic verification remains possible for non-redacted metadata.

## Access Control and Separation of Duties

Immutable audit is sensitive. Access must be controlled.

Required access controls:

- separate audit writers from audit administrators where possible;
- restrict audit readers by role, tenant, customer, case, and data classification;
- require elevated approval for cross-tenant audit search;
- log all audit reads, exports, administrative changes, and break-glass access;
- protect signing keys and storage administration separately from workflow operators;
- prevent agents from modifying, deleting, or suppressing audit records;
- prevent tools from executing sensitive actions without audit references;
- review access regularly;
- disable stale, suspended, or retired identities.

No agent should have permission to alter immutable audit history.

## Monitoring and Tamper Detection

Audit integrity must be monitored.

Recommended monitoring signals:

| Signal | Concern |
|---|---|
| Missing event sequence | Possible logging failure or dropped event. |
| Hash mismatch | Possible modification or corruption. |
| Invalid signature | Possible tampering, key issue, or emitter compromise. |
| Unexpected event deletion | Storage or retention control failure. |
| Backdated event | Clock, ordering, or malicious replay concern. |
| Duplicate event ID | Emitter defect or replay attack. |
| Missing tenant or case field | Boundary and replay failure. |
| Tool execution without policy reference | Authorization bypass. |
| Sensitive action without approval reference | Approval bypass. |
| Customer release without review record | Release-control failure. |
| Fleet rollout without rollback target | Unsafe release process. |
| Recall event without affected-scope record | Incomplete emergency response. |
| Audit read/export spike | Potential investigation, misuse, or data exposure. |
| Failed append-only write | Audit availability risk. |
| Index mismatch with source records | Search or dashboard integrity issue. |

Tamper detection alerts should route to an accountable owner and preserve their own audit records.

## Replay Support

Immutable audit must support replay of governed workflows.

A replay process should be able to reconstruct:

1. the initiating alert, case, task, or fleet change request;
2. the tenant, customer, case, evidence, or release scope;
3. the agent identity, lifecycle state, package version, prompt version, model reference, and tool contracts;
4. the context package and source references available at the time;
5. the agent output and requested action;
6. the AI assurance or Agent Judge result;
7. the policy request and decision;
8. the human or customer approval path;
9. the tool execution or release outcome;
10. exceptions, denials, escalations, or fail-closed branches;
11. monitoring signals and follow-up actions;
12. rollback, recall, correction, or supersession events.

Replay should use immutable records as the source of truth. Derived indexes, dashboards, or case views may assist replay, but they must be verifiable against the immutable source records.

## Fail-Closed Conditions

The audit path must fail closed or route to approved exception handling when:

- audit event schema validation fails;
- required tenant, customer, case, workflow, or correlation scope is missing;
- required policy, approval, evidence, or tool reference is missing;
- the audit store is unavailable for a sensitive action;
- the event cannot be canonicalized or hashed;
- the signing key is unavailable for a record that requires signing;
- append-only write fails;
- the audit chain cannot be verified for a governed release or sensitive action;
- retention or legal-hold status cannot be resolved;
- a workflow attempts to execute without an audit reference where one is required.

A low-risk read-only workflow may continue under degraded logging only if policy explicitly allows it. Sensitive actions, customer-facing releases, DFIR evidence-impacting workflows, and fleet rollout or recall operations must not proceed without an approved audit path.

## Anti-Patterns

Avoid the following:

- treating normal mutable application logs as immutable audit records;
- relying only on a SIEM index as the source of audit truth;
- storing raw evidence in audit logs without evidence-handling controls;
- storing secrets, tokens, keys, or credentials in audit records;
- omitting tenant, customer, case, workflow, or correlation identifiers;
- allowing agents to suppress, rewrite, or delete audit events;
- recording only successful actions and ignoring denials or failures;
- treating Agent Judge output as approval authority;
- allowing tool execution without policy and approval references;
- using free-form text only when structured audit fields are required;
- deleting records to correct mistakes instead of appending correction events;
- allowing broad cross-tenant audit search without authorization;
- creating dashboards that cannot be traced back to immutable source events;
- storing full prompts or retrieved content without minimization and access control;
- failing open when audit logging is unavailable for sensitive actions.

## Acceptance Criteria

Immutable audit guidance is satisfied when the architecture can demonstrate:

- governed workflows emit structured audit events;
- audit records are append-only or tamper-evident;
- events include tenant, customer, case, workflow, and correlation scope where applicable;
- policy decisions, approvals, tool executions, evidence references, and outputs are linked;
- failures, denials, exceptions, and fail-closed decisions are recorded;
- sensitive records are minimized, classified, encrypted, and access-controlled;
- audit reads, exports, administration, and break-glass access are logged;
- corrections and recalls are appended rather than silently rewriting history;
- immutable records can verify derived indexes or dashboards;
- replay can reconstruct decisions, approvals, actions, evidence references, and outcomes;
- fleet rollout, rollback, recall, and sanitized intelligence release records are replayable;
- retention, legal hold, redaction, and deletion handling are governed and auditable;
- audit failure blocks or escalates sensitive workflows rather than allowing unaudited execution.

## Related Repository Areas

- [`audit-event-model.md`](audit-event-model.md) for the audit event structure and event categories.
- [`audit-correlation-model.md`](audit-correlation-model.md) for correlation identifiers and replay chains.
- [`replayability-requirements.md`](replayability-requirements.md) for replay expectations and reconstruction requirements.
- [`exception-and-failure-audit.md`](exception-and-failure-audit.md) for failure, exception, denial, and degraded-mode audit behavior.
- [`fleet-rollout-audit-and-replay-model.md`](fleet-rollout-audit-and-replay-model.md) for fleet release, rollback, and recall audit handling.
- [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) for evidence references and DFIR evidence handling.
- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) for tenant boundary controls.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) for PDP/PEP behavior and policy decision records.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) for review and approval records.
- [`../agent-governance/readme.md`](../agent-governance/readme.md) for agent identity, lifecycle, fleet governance, and recall.
