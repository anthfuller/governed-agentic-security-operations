# Agent-to-Agent Communication

## Purpose

This document defines how agents may exchange tasks, context, outputs, status, and review requests without creating implicit trust, hidden authorization paths, or cross-boundary data leakage.

Agent-to-agent communication can be useful for triage, enrichment, evidence review, quality checks, policy-package preparation, and handoff between specialized agents. It also creates risk when one agent delegates work, transmits sensitive context, amplifies unverified claims, or attempts to bypass policy through another agent.

## Core Principle

No agent implicitly trusts another agent.

An agent-to-agent message is not an approval, authorization, evidence source, policy decision, or customer release decision. Communication must be authenticated, scoped, policy-visible, auditable, and constrained by the lifecycle state and access scope of both the sending and receiving agents.

## Communication Types

| Communication Type | Example | Required Boundary |
|---|---|---|
| Task delegation | Triage agent asks enrichment agent to look up an indicator. | Both agents must be active, scoped to the same tenant/customer/case, and allowed to perform the delegated task. |
| Context handoff | Investigation agent passes a scoped summary to report-draft agent. | Context must preserve provenance, data classification, tenant, customer, case, and evidence references. |
| Assurance request | Output-quality judge evaluates a draft recommendation. | Judge output is assurance only and must not approve execution. |
| Evidence-support request | DFIR assistant asks evidence-reference checker to validate citations. | Checker must reference evidence objects without modifying evidence. |
| Workflow status update | Agent notifies orchestrator that a subtask is complete. | Status must be correlated to workflow and audit IDs. |
| Clarification request | Agent asks another agent or human queue for missing context. | Missing scope or evidence cannot be guessed. |
| Fleet coordination | Rollout controller sends version status to monitoring agent. | Fleet messages must be signed, versioned, and tenant-eligible. |

## Message Envelope Requirements

Agent-to-agent messages should use a structured envelope rather than unstructured chat where governed workflow behavior depends on the message.

Minimum fields should include:

```json
{
  "message_id": "msg-2026-06-27-0001",
  "correlation_id": "case-1234-workflow-5678",
  "sender_agent_id": "soc-triage-agent",
  "sender_agent_version": "soc-triage-agent@1.4.2",
  "receiver_agent_id": "threat-intel-enrichment-agent",
  "message_type": "task_delegation",
  "tenant_id": "tenant-a",
  "customer_id": "customer-a",
  "case_id": "case-1234",
  "evidence_refs": ["alert:sentinel:abc123"],
  "data_classification": "security-telemetry",
  "requested_task": "enrich_indicator",
  "requested_action_scope": "read_only_enrichment",
  "policy_decision_ref": "pdp-decision-7890",
  "expires_at": "2026-06-27T22:00:00Z",
  "requires_human_review": false,
  "audit_required": true
}
```

The envelope is an architecture example. Production systems should validate schema, signatures, policy decisions, retention requirements, and audit correlation.

## Communication Rules

### 1. Sender and Receiver Must Be Governed

Both sending and receiving agents must have:

- known identity;
- active lifecycle state;
- approved scope for the tenant, customer, case, data, task, and output;
- compatible data-handling authorization;
- current approved version;
- monitoring and audit coverage.

If either side cannot be validated, communication must fail closed.

### 2. Delegation Does Not Transfer Authority

A sending agent cannot transfer authority it does not have.

A receiving agent must evaluate the delegated request against its own scope, lifecycle state, policy controls, and approval requirements. The delegated message is context, not authorization.

### 3. Context Must Preserve Scope and Provenance

Messages must preserve tenant, customer, case, evidence references, data classification, retention constraints, and output restrictions.

Agents must not strip scope metadata, flatten evidence references into unsupported claims, or convert restricted context into general shared memory.

### 4. Agent-to-Agent Communication Must Be Policy-Visible

Policy should be able to evaluate:

- who is sending;
- who is receiving;
- what task is requested;
- what context is included;
- which tenant, customer, case, evidence, and data class apply;
- whether the receiving agent is allowed to perform the task;
- whether the requested task requires human approval;
- whether the output destination is permitted.

### 5. Messages Must Be Auditable

Agent-to-agent communication should be recorded with enough detail to reconstruct the workflow.

Audit records should capture the message ID, sender, receiver, versions, tenant/customer/case scope, evidence references, policy decision, message type, task, output, and downstream action references.

### 6. Human Approval Cannot Be Bypassed Through Delegation

An agent must not delegate sensitive, privileged, customer-impacting, or evidence-impacting work to another agent to avoid human approval.

If a task requires approval, the approval requirement follows the task regardless of which agent receives it.

### 7. Shared Memory Is Not a Message Bus

Shared memory, RAG stores, vector databases, case notes, or ticket comments must not become uncontrolled agent-to-agent communication channels.

If agents communicate through shared stores, the same identity, scope, policy, data classification, and audit requirements apply.

## Prohibited Communication Patterns

The following patterns must be blocked or treated as policy violations:

- unregistered agents sending or receiving governed tasks;
- messages without tenant, customer, case, or evidence scope where required;
- cross-tenant task delegation without governed shared-intelligence approval;
- hidden instructions embedded in logs, evidence, case notes, or retrieved content;
- agent self-approval or mutual approval loops;
- passing secrets, tokens, credentials, or privileged session material through messages;
- delegating prohibited actions to a more privileged agent;
- instructing another agent to ignore policy, audit, tenant boundaries, evidence requirements, or human review;
- using agent-to-agent messages to release customer-facing content without approval;
- writing sensitive customer context into global memory or shared fleet state.

## Communication Risk Controls

| Risk | Control |
|---|---|
| Prompt injection through delegated context | Validate message structure, isolate retrieved content, preserve source labels, and prevent instruction execution from untrusted data. |
| Cross-tenant leakage | Require tenant/customer/case scope on every message and block mismatches. |
| Authority confusion | Require receiving agent to perform independent policy check. |
| Unsupported claim propagation | Require evidence references and assurance checks before downstream use. |
| Hidden tool access path | Force all tool use through PEP even when requested by another agent. |
| Approval bypass | Carry approval requirements with task type and risk classification. |
| Memory contamination | Enforce memory write policies, retention labels, and tenant/case boundaries. |
| Replay gaps | Store message, decision, output, and downstream action correlation IDs. |

## Agent-to-Agent Handoff Flow

A governed handoff should follow this sequence:

1. Sender prepares structured message with scope, task, evidence references, data classification, and requested output.
2. Sender-side policy verifies that the sender may delegate this task and disclose this context.
3. Message is delivered through an approved broker, orchestrator, queue, or workflow service.
4. Receiver-side policy verifies that the receiver may accept the task and access the context.
5. Receiver performs the task only within approved scope.
6. Any tool use is separately evaluated and enforced through the appropriate PEP.
7. Receiver returns structured output with evidence references, uncertainty, policy limitations, and output scope.
8. Audit records link message, policy decisions, tool calls, output, and downstream use.

## Audit Requirements

Agent-to-agent communication audit should include:

- message identifier;
- workflow correlation identifier;
- sender and receiver agent identities;
- sender and receiver versions;
- lifecycle states at time of communication;
- tenant, customer, case, and evidence scope;
- data classification and retention requirements;
- message type and requested task;
- policy decision references for send and receive checks;
- tool execution references where applicable;
- output references;
- denial, clarification, or fail-closed reason where applicable.

## Fail-Closed Conditions

Communication must fail closed or route to authorized review when:

- sender or receiver identity is unknown;
- sender or receiver lifecycle state is not active;
- tenant, customer, case, or evidence scope is missing where required;
- sender is not allowed to disclose the context;
- receiver is not allowed to receive or process the context;
- delegated task exceeds sender or receiver scope;
- policy cannot evaluate the communication;
- required approval is missing;
- message schema validation fails;
- message includes secrets, credentials, or prohibited content;
- audit logging is unavailable.

## Acceptance Criteria

Agent-to-agent communication governance is acceptable when:

- all governed communication uses authenticated, structured, scoped, and auditable messages;
- receiving agents independently evaluate authorization and scope;
- delegated work cannot bypass policy, PEP, approval, tenant isolation, or evidence requirements;
- cross-tenant and cross-case data movement is blocked unless explicitly governed;
- agent messages can be replayed as part of workflow reconstruction;
- hidden communication through memory, logs, or unstructured stores is controlled.

## Summary

Agent-to-agent communication is a controlled workflow mechanism, not a trust relationship.

> Agents may collaborate, but every handoff must preserve identity, scope, policy, evidence, and auditability.
