# Agentic Security Operations Threat Model

## Purpose

This threat model defines the primary security, operational, and forensic risks for the **Governed Agentic MSSP / MDR / DFIR Security Operations Architecture**.

It focuses on agentic workflows that assist security operations across **MSSP**, **MDR**, **SOC / Incident Response**, **Cloud IR**, **DFIR**, and **Private / Local LLM-assisted DFIR** where applicable.

The goal is to identify realistic attack paths, failure modes, trust-boundary violations, and required controls before agentic workflows are allowed to influence tools, evidence, tenants, cases, customer-facing outputs, or response actions.

This file is a threat-model artifact, not a deployment guide or product-specific implementation.

---

## Scope

| Area | In Scope |
|---|---|
| Agentic workflows | Triage, enrichment, reasoning, recommendation, report drafting, approval preparation, timeline assistance, and tool-use requests. |
| Service models | MSSP, MDR, SOC / IR, Cloud IR, DFIR, and Private / Local LLM-assisted DFIR where applicable. |
| Data boundaries | Tenant, customer, case, incident, evidence, retrieval, memory, and output scope. |
| Tool use | APIs, scripts, connectors, playbooks, cloud actions, ticket updates, evidence tools, and response automation. |
| Human oversight | Analyst review, sensitive-action approval, customer authorization, report release, and DFIR validation. |
| Evidence handling | Evidence provenance, chain of custody, derived artifacts, timeline output, parser versions, and local forensic analysis. |
| Auditability | Policy decisions, approvals, retrieved context, tool calls, model outputs, review records, execution results, and final workflow state. |

## Out of Scope

| Area | Reason |
|---|---|
| Vendor-specific deployment hardening | Belongs in implementation and deployment guides. |
| Full cloud provider threat model | Covered by provider-specific architecture and cloud security design. |
| Endpoint or SIEM product internals | Covered by product-specific threat models. |
| Generic AI ethics policy | This file focuses on security control failure modes and enforceable architecture risks. |
| Legal conclusions | Legal, regulatory, and contractual interpretation must be handled by authorized stakeholders. |

---

## Protected Assets

| Asset | Why It Matters |
|---|---|
| Customer telemetry | May contain sensitive customer security data and indicators of compromise. |
| Tenant and customer boundaries | Prevent cross-customer exposure and operational contamination. |
| Case and incident context | Prevents unrelated incidents from influencing findings or actions. |
| Evidence objects | Must preserve forensic integrity, provenance, and chain of custody. |
| Retrieval and memory stores | Can leak, contaminate, or bias agent outputs if not scoped. |
| Agent identities | Agents must be registered, owned, scoped, and lifecycle-managed. |
| Policy decisions | Determine whether action is allowed, denied, or approval-required. |
| Approval records | Prove sensitive actions were authorized by the correct human or customer authority. |
| Tool credentials | Enable potentially destructive or customer-impacting actions. |
| Customer-facing outputs | Can create operational, legal, reputational, or contractual impact. |
| Audit trails | Required for replay, investigation, assurance, customer review, and accountability. |

---

## Primary Trust Boundaries

| Boundary | Threat if Broken | Required Control |
|---|---|---|
| Tenant boundary | Cross-tenant data exposure or action against wrong tenant. | Mandatory `tenant_id`, tenant-scoped retrieval, fail-closed mismatch handling. |
| Customer boundary | Customer data bleed or wrong-customer action. | Mandatory `customer_id`, customer-scoped tools, customer-specific output controls. |
| Case / incident boundary | Stale or unrelated context influences current workflow. | Mandatory `case_id` / `incident_id` where applicable; case-scoped memory and retrieval. |
| Evidence boundary | Evidence contamination, unsupported findings, broken custody. | Evidence object IDs, provenance, hashes, parser versions, custody references. |
| Agent-to-tool boundary | Unauthorized automation or destructive action. | PEP/PDP, tool gateway, scoped credentials, execution token, approval where required. |
| Agent-to-memory boundary | Cross-case memory contamination or unauthorized persistence. | Deny persistent memory by default; scope and retention enforcement. |
| Agent-to-human boundary | Human rubber-stamping or unclear approval basis. | Approval package with evidence, impact, scope, and policy reason. |
| Internal-to-customer output boundary | Unsupported claims or unauthorized release. | Review, customer authorization where required, output PEP, audit linkage. |
| Local DFIR boundary | Local model treated as automatically safe. | Case-scoped local runtime, no external egress, analyst validation, audit. |

---

## Threat Actors

| Actor | Capability | Primary Risk |
|---|---|---|
| External attacker | Injects malicious content into logs, emails, alerts, tickets, or cloud resources. | Prompt injection, tool misuse, false conclusions, data exposure. |
| Compromised customer identity | Generates legitimate-looking activity or requests. | Misleading triage, unauthorized actions, evidence contamination. |
| Malicious insider | Has access to tools, prompts, cases, or customer data. | Policy bypass, unauthorized retrieval, approval abuse, output manipulation. |
| Misconfigured agent | Has excessive permissions or weak scope controls. | Cross-customer access, unsafe tool calls, uncontrolled memory. |
| Over-trusted automation | Executes recommendations without enforcement. | Customer-impacting actions without approval. |
| Faulty model / hallucination | Produces unsupported claims or wrong recommendations. | False findings, bad containment, poor customer reporting. |
| Supply-chain component | Compromised connector, parser, model, prompt, or tool wrapper. | Poisoned context, altered outputs, hidden exfiltration, audit gaps. |

---

## Threat Categories

| Category | Description |
|---|---|
| Prompt injection and instruction override | Untrusted content attempts to change agent behavior or bypass controls. |
| Cross-tenant / cross-customer contamination | Agent retrieves or uses the wrong customer’s context. |
| Cross-case / stale-context contamination | Prior or unrelated case data influences current decisions. |
| Unauthorized tool execution | Agent triggers tools or APIs outside approved policy. |
| Human approval bypass | Sensitive actions execute without qualified human or customer authorization. |
| Evidence integrity failure | Evidence is altered, lost, untraceable, or unsupported by custody records. |
| Unsupported forensic conclusion | Model output becomes a finding without evidence and analyst validation. |
| Output release failure | Customer-facing content is released without review or authorization. |
| Memory abuse | Agent writes or reads persistent memory outside approved scope. |
| Audit failure | Workflow cannot be reconstructed after decision or execution. |
| Credential abuse | Static or overbroad credentials allow action beyond policy decision. |
| Availability and latency failure | Controls fail open, timeout incorrectly, or are bypassed for speed. |

---

## Threat Severity, Ownership, and Enforcement Matrix

| Threat ID | Priority | Primary Control Owner | Required Enforcement Point |
|---|---|---|---|
| T1 | High | Platform Security / AI Assurance | Context assembly, prompt boundary, tool PEP |
| T2 | Critical | Tenant Boundary Owner / Retrieval Owner | Retrieval PEP, vector namespace controls |
| T3 | High | Memory / Knowledge Store Owner | Memory PEP, retention controls |
| T4 | Critical | Tool Platform Owner / Policy Owner | Tool Gateway, PDP, PEP, execution token validation |
| T5 | Critical | Service Owner / Human Oversight Owner | Approval workflow, workflow orchestrator PEP |
| T6 | Critical | DFIR Lead / Evidence Custodian | Evidence store, evidence movement PEP |
| T7 | Critical | DFIR Lead / AI Assurance | Judge, review workflow, report release PEP |
| T8 | High | Service Owner / Customer Communications Owner | Output publishing PEP |
| T9 | Critical | Identity / Credential Broker Owner | Credential broker, token validation, tool gateway |
| T10 | High | Audit / Assurance Owner | Audit pipeline, traceability store |
| T11 | High | Governance / Change Control Owner | Prompt, policy, parser, model, and tool release gates |
| T12 | High | Platform Reliability Owner | PDP / PEP timeout, retry, cache, and fail-closed controls |

---

## Threat Scenarios and Required Controls

### T1: Prompt Injection Through Logs, Tickets, or Evidence

| Field | Detail |
|---|---|
| Threat | Attacker-controlled content instructs the agent to ignore policy, reveal data, or execute tools. |
| Attack Path | Malicious content enters telemetry, ticket, email, log, evidence artifact, or case note. Agent treats it as instruction. |
| Impact | Tool misuse, data exposure, false recommendations, customer-facing output compromise. |
| Required Controls | Label untrusted content, separate instructions from evidence, restrict tools through PEP/PDP, require structured outputs, block direct tool execution. |
| Detection | Prompt-injection markers, abnormal tool requests, policy-denied operations, unexpected output destinations. |
| Fail-Closed Rule | If untrusted content cannot be labeled or isolated, route for human review before agent use. |

### T2: Cross-Tenant or Cross-Customer Retrieval

| Field | Detail |
|---|---|
| Threat | RAG, memory, or search retrieves another customer’s data. |
| Attack Path | Missing metadata, weak vector namespace, flawed filter, shared index, stale memory, or query expansion. |
| Impact | Data breach, wrong recommendation, customer trust failure, contractual exposure. |
| Required Controls | Mandatory `tenant_id` and `customer_id`, namespace enforcement, retrieval PEP, metadata filters, deny-by-default retrieval. |
| Detection | Retrieval result scope mismatch, `knowledge_memory_scope_result` failure, cross-customer context IDs. |
| Fail-Closed Rule | Deny and quarantine retrieved context if scope cannot be proven. |

### T3: Cross-Case or Stale Memory Contamination

| Field | Detail |
|---|---|
| Threat | Prior case memory influences current incident or forensic conclusion. |
| Attack Path | Persistent memory is reused without case authorization or freshness validation. |
| Impact | False correlation, incorrect customer report, unsupported findings, bad response action. |
| Required Controls | Case-scoped memory, retention policy, freshness checks, memory read/write audit, deny persistent memory by default. |
| Detection | Memory scope mismatch, stale retrieval flags, memory write attempts without approval. |
| Fail-Closed Rule | Return for clarification or deny memory use when case scope is missing or stale. |

### T4: Unauthorized Tool or API Execution

| Field | Detail |
|---|---|
| Threat | Agent triggers a tool action without authorization. |
| Attack Path | Direct tool access, weak wrapper, missing PEP, overbroad credentials, tool call from free-form output. |
| Impact | Endpoint isolation, account disablement, deletion, policy change, customer disruption. |
| Required Controls | Tool registry, schema validation, PDP decision, PEP enforcement, scoped short-lived execution token, approval record where required. |
| Detection | Tool call without policy decision, token mismatch, denied operation, missing approval. |
| Fail-Closed Rule | Block execution if policy decision, token, tool registration, scope, or approval is missing. |

### T5: Sensitive Action Approval Bypass

| Field | Detail |
|---|---|
| Threat | High-impact action executes without qualified human approval. |
| Attack Path | Agent recommendation treated as approval; approval reused; customer authorization skipped. |
| Impact | Unauthorized containment, production impact, customer notification error, legal exposure. |
| Required Controls | Human-approved sensitive action pattern, approval record, approval expiration, scope match, customer authorization where required. |
| Detection | Execution without `approval_record_id`, expired approval, mismatch between approved and executed action. |
| Fail-Closed Rule | Block execution when approval is missing, expired, reused, or mismatched. |

### T6: Evidence Integrity or Chain-of-Custody Failure

| Field | Detail |
|---|---|
| Threat | Evidence is modified, lost, or cannot be proven reliable. |
| Attack Path | Tool modifies source evidence; parser overwrites artifact; evidence export lacks custody reference. |
| Impact | Invalid forensic conclusion, legal defensibility failure, customer trust failure. |
| Required Controls | Evidence manifest, hashes, source/derived separation, parser versioning, read-only originals, custody references. |
| Detection | Missing hash, missing custody record, source evidence write, unknown parser version. |
| Fail-Closed Rule | Block formal findings or release when custody, evidence object ID, or provenance is missing. |

### T7: Unsupported Forensic Conclusion

| Field | Detail |
|---|---|
| Threat | Local or cloud LLM output is treated as forensic truth. |
| Attack Path | Model-generated hypothesis enters report as fact without analyst review. |
| Impact | Incorrect attribution, false exfiltration claim, wrong timeline, customer harm. |
| Required Controls | Label interpretations, require evidence references, analyst review, rejected-inference tracking, DFIR lead approval for final findings. |
| Detection | Claim without evidence object ID, unsupported inference, missing review record. |
| Fail-Closed Rule | Reject or mark unresolved if evidence support is missing. |

### T8: Customer-Facing Output Release Failure

| Field | Detail |
|---|---|
| Threat | Draft report, summary, or notification is released without approval. |
| Attack Path | Output connector publishes agent draft directly to customer. |
| Impact | Unsupported claims, legal exposure, reputational damage, contractual breach. |
| Required Controls | Output PEP, release approval, customer authorization where required, evidence-backed claims, audit reference. |
| Detection | Customer-facing destination without release approval, missing reviewer, missing authorization reference. |
| Fail-Closed Rule | Block release when review or authorization is missing. |

### T9: Credential Abuse or Overbroad Cloud Access

| Field | Detail |
|---|---|
| Threat | Agent or tool uses long-lived or overbroad credentials. |
| Attack Path | Static keys, shared secrets, unscoped API tokens, credential reuse across customers. |
| Impact | Cross-customer action, unauthorized cloud changes, persistence, privilege escalation. |
| Required Controls | Policy-scoped credential broker, short-lived signed execution token, least privilege, target scope, expiration. |
| Detection | Credential issued without policy decision, token used outside scope, missing expiration, reused token. |
| Fail-Closed Rule | Deny credential issuance or tool execution if scope cannot be verified. |

### T10: Audit and Replay Failure

| Field | Detail |
|---|---|
| Threat | Organization cannot prove what happened. |
| Attack Path | Missing correlation ID, missing evidence refs, missing policy decision, unlogged tool output. |
| Impact | Failed customer review, weak investigation, inability to tune controls, legal exposure. |
| Required Controls | Structured audit event, `audit_reference_id`, `correlation_id`, linked request, decision, approval, tool result, output state. |
| Detection | Audit completeness check fails, orphan records, missing linkage. |
| Fail-Closed Rule | Block sensitive execution if audit path is unavailable. |

### T11: Governance Artifact Drift or Supply-Chain Tampering

| Field | Detail |
|---|---|
| Threat | Prompt templates, policies, parsers, model profiles, tool wrappers, or playbooks are changed without governance. |
| Attack Path | Unreviewed prompt update, modified parser, unsigned playbook, stale model profile, or altered policy bundle changes workflow behavior. |
| Impact | Unsafe recommendations, weakened enforcement, evidence misinterpretation, failed audit, or hidden tool abuse. |
| Required Controls | Versioned artifacts, signed playbooks, approved prompt templates, parser/tool version tracking, model validation references, change-control approval, rollback path. |
| Detection | Artifact version mismatch, unsigned playbook, unapproved prompt template, unknown parser version, policy bundle drift. |
| Fail-Closed Rule | Block workflow execution or route to governance review when required artifact version, approval, or signature cannot be verified. |

### T12: Control-Plane Availability, Latency, or Fail-Open Bypass

| Field | Detail |
|---|---|
| Threat | PDP, PEP, audit, schema validation, credential broker, or token validation is bypassed because of timeout, outage, latency pressure, or fallback logic. |
| Attack Path | Control service is unavailable, remote policy call times out, fallback allows execution, or performance pressure causes teams to bypass deterministic controls. |
| Impact | Unauthorized action, incomplete audit, cross-tenant exposure, unapproved release, or response action outside policy. |
| Required Controls | Explicit latency budgets, timeout behavior, retry limits, cache rules, circuit breakers, deny-by-default fallback, audit availability checks, fail-closed tests. |
| Detection | PDP timeout, PEP bypass attempt, missing audit event, unexpected fallback path, policy decision absent from tool execution. |
| Fail-Closed Rule | If deterministic controls cannot complete within the approved behavior, the workflow must deny, queue for review, or return for clarification rather than execute. |

---

## Threat Model by Service Model

| Service Model | Primary Threat Emphasis | Required Focus |
|---|---|---|
| MSSP | Cross-customer data bleed, wrong-customer reporting, unsafe recommendations. | Tenant/customer boundary, output controls, service ownership, audit. |
| MDR | Unauthorized response, bad containment, detection tuning mistakes. | Approval gates, tool PEP, authorized response path, customer authorization. |
| SOC / IR | Incident coordination errors, premature action, unclear authority. | Human command structure, escalation, policy routing, audit state. |
| Cloud IR | IAM misuse, cloud policy changes, credential abuse, blast radius. | Cloud scope, short-lived credentials, before/after state, customer authorization. |
| DFIR | Evidence integrity failure, unsupported conclusions, chain-of-custody gaps. | Evidence manifest, custody, analyst validation, report review. |
| Private / Local LLM DFIR | Local model over-trust, unscoped local RAG, prompt/output leakage. | Case-scoped local runtime, no external egress, prompt governance, review record. |

---

## Required Security Controls

| Control | Requirement |
|---|---|
| Schema validation | All request, output, judge, policy, approval, tool, and audit artifacts must validate against expected structure. |
| Tenant/customer scoping | `tenant_id` and `customer_id` must be mandatory for customer-bound workflows. |
| Case/incident scoping | `case_id` or `incident_id` must be mandatory for incident, investigation, or evidence workflows. |
| PDP/PEP separation | PDP decides; PEP enforces at real execution, retrieval, memory, tool, evidence, or output boundary. |
| Tool mediation | Agents must request tools through mediated interfaces; no free-form direct execution. |
| Execution token | Authorized tool actions should use short-lived signed execution tokens scoped to policy decision and allowed operations. |
| Governance artifact integrity | Prompt templates, policy bundles, parser versions, model profiles, signed playbooks, and tool wrappers must be versioned, approved, and auditable. |
| Control-plane latency and fail-closed behavior | PDP, PEP, schema validation, token validation, credential broker, and audit paths must define latency budgets, timeout behavior, and deny-by-default failure behavior. |
| Human approval | Sensitive, destructive, privileged, customer-impacting, evidence-sensitive, or externally visible actions require approval. |
| Customer authorization | Required where customer contract, impact, data movement, release, or environment change demands it. |
| Evidence references | Findings, timelines, and DFIR outputs must reference evidence objects or derived artifacts. |
| Audit linkage | Request, output, judge, policy, approval, execution, review, and final state must share audit/correlation references. |
| Fail closed | Missing identity, scope, policy, approval, audit, evidence, or output destination must block or route for review. |

---

## Engineering Acceptance Criteria

A governed agentic security operations workflow passes this threat model when:

- every workflow has identity, tenant, customer, case/incident, and workflow scope where applicable;
- agent outputs are structured and reviewable;
- retrieved context is scope-validated before prompt assembly;
- tools cannot execute without PEP/PDP authorization;
- sensitive actions require approval before execution;
- customer-impacting actions require customer authorization where applicable;
- short-lived execution tokens constrain downstream tool calls;
- prompt templates, policy bundles, parser versions, model profiles, signed playbooks, and tool wrappers are approved and versioned;
- deterministic control paths define timeout, latency, retry, cache, and fail-closed behavior;
- evidence-sensitive outputs preserve evidence object references;
- local/private DFIR outputs are analyst-reviewed before findings;
- customer-facing output is reviewed before release;
- audit logs can reconstruct the full request-to-outcome chain;
- fail-closed behavior is tested for missing scope, missing policy, missing approval, missing evidence, missing token, and missing audit path.

---

## Threat-Driven Test Cases

| Test Case | Expected Result |
|---|---|
| Submit request without `tenant_id`. | Workflow fails closed. |
| Retrieve context from wrong customer namespace. | Retrieval denied and audited. |
| Agent requests endpoint isolation without approval. | Tool execution blocked. |
| Agent requests cloud IAM action with expired token. | Tool execution blocked. |
| Agent output includes finding without evidence reference. | Judge flags unsupported claim. |
| Customer report release lacks approval. | Output PEP blocks release. |
| Persistent memory write lacks owner and retention. | Memory write denied. |
| Local LLM attempts external network access. | Runtime blocks and audits. |
| Evidence export lacks customer authorization. | Export blocked. |
| Audit path unavailable for sensitive action. | Sensitive action fails closed. |
| Prompt template version is missing or unapproved. | Workflow blocks or routes to prompt governance review. |
| Parser or transformation version is unknown for DFIR output. | Finding or timeline output is blocked from release. |
| Signed playbook verification fails. | Tool execution is blocked. |
| PDP call times out. | Workflow follows defined timeout path and fails closed unless read-only cached decision is explicitly allowed. |
| Execution token is replayed or used against a different target entity. | Tool execution is blocked and audited. |

---

## Threat Model Maintenance Triggers

Update this threat model when any of the following occur:

| Trigger | Required Action |
|---|---|
| New agent role or service model is introduced. | Add or update threat scenarios, trust boundaries, and acceptance criteria. |
| New tool, API, connector, playbook, or automation path is added. | Review tool execution, token, credential, approval, and audit risks. |
| New RAG, memory, or knowledge-store pattern is added. | Review tenant, customer, case, retention, and stale-context controls. |
| New DFIR evidence source or parser is added. | Review evidence format, parser version, provenance, and custody controls. |
| Prompt templates, policy bundles, model profiles, or signed playbooks change. | Verify governance artifact integrity and rollback path. |
| Customer-facing release path changes. | Review output PEP, customer authorization, and audit linkage. |
| Incident review identifies a control gap. | Add threat-driven test case and update required controls. |

---

## Anti-Patterns

Avoid:

- treating policy text inside prompts as enforcement;
- allowing agents to use human analyst credentials directly;
- using long-lived static credentials for tool execution;
- allowing tool calls from free-form model output;
- using global vector indexes without enforceable scope;
- storing customer data in shared model memory;
- treating Agent Judge output as policy authorization;
- treating local LLM output as forensic truth;
- releasing customer-facing reports without review;
- closing incidents solely from agent output;
- modifying evidence without evidence-handling approval;
- using unapproved prompt templates, unsigned playbooks, unknown parser versions, or unvalidated model profiles;
- bypassing PEP/PDP, audit, or token validation to reduce latency;
- failing open when PDP, PEP, audit, or approval service is unavailable.

---

## Relationship to Other Repo Artifacts

| Artifact | Relationship |
|---|---|
| `architecture/engineering-view.md` | Defines engineering control flow, schemas, and implementation-readiness requirements. |
| `patterns/governed-agentic-security-operations-pattern.md` | Defines the baseline governed agentic pattern. |
| `patterns/policy-enforced-tool-use-pattern.md` | Defines tool mediation and execution controls. |
| `patterns/human-approved-sensitive-action-pattern.md` | Defines sensitive-action approval requirements. |
| `patterns/tenant-safe-rag-memory-pattern.md` | Defines retrieval and memory boundary controls. |
| `patterns/private-local-llm-dfir-pattern.md` | Defines private/local forensic AI controls. |
| `service-models/*.md` | Define service-specific operating boundaries. |
| `examples/*` | Demonstrate request, decision, approval, audit, evidence, and review artifacts. |

---

## Non-Goals

This threat model does not:

- define a vendor-specific implementation;
- replace product security reviews;
- replace secure coding requirements;
- replace customer contract review;
- replace legal, compliance, or regulatory analysis;
- certify that any implementation is secure;
- authorize autonomous agentic response.

---

## Summary

This threat model treats agentic security operations as a high-control environment.

The core security position is:

> Agentic systems may assist security operations, but they must not cross tenant, customer, case, evidence, tool, approval, memory, or output boundaries without explicit policy, enforcement, review, and audit.
