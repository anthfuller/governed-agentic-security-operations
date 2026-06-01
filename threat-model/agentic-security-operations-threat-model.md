# Agentic Security Operations Threat Model

## Purpose

This document defines the architecture-wide threat model for the **Governed Agentic MSSP / MDR / DFIR Security Operations Architecture**.

It identifies how agentic security operations can fail, be attacked, be bypassed, or produce unsafe outcomes across multi-customer security operations, managed detection and response, SOC / Incident Response, Cloud Incident Response, DFIR, and Private / Local LLM-assisted DFIR workflows.

This file is the parent threat model for the `threat-model/` directory. More specific threat files refine individual risk surfaces such as prompt injection, RAG contamination, rogue agents, tool automation, human approval, and local LLM-assisted DFIR.

## Scope

This threat model applies to agentic workflows that support:

- alert triage;
- investigation and enrichment;
- case summarization;
- incident correlation;
- response recommendation;
- approval package drafting;
- tool-use recommendation;
- customer notification drafting;
- customer-facing report preparation;
- cloud IAM compromise response support;
- evidence review;
- forensic timeline generation;
- private/local LLM-assisted DFIR analysis.

The threat model covers the following architecture layers:

| Architecture Layer | In Scope |
|---|---|
| Customer / Telemetry Sources | Logs, alerts, tickets, emails, case notes, cloud audit events, endpoint events, SaaS events, evidence, and customer-provided content. |
| Ingestion / Normalization | Source metadata, parser versions, schema versions, timestamps, evidence references, data classification, sensitivity labels, tenant/customer/case binding. |
| Agentic SOC / Orchestration | Agent tasks, agent-to-agent requests, workflow routing, recommendations, summarization, investigation support, and output generation. |
| AI Assurance & Human Oversight | Agent Judges, output validation, evidence support checks, hallucination checks, tenant-boundary checks, human approval, and release review. |
| Governance & Policy Control Plane | PDP decisions, PEP enforcement, policy bundles, approval validation, execution tokens, fail-closed handling, audit, and replay. |
| Private / Local DFIR Processing | Local model runtime, isolated workspaces, case-scoped retrieval, evidence handling, timeline generation, forensic conclusions, and release controls. |
| Agent Governance and Identity Control Plane | Agent identity, registration, ownership, lifecycle, attestation, monitoring, credential scope, and revocation. |

## Explicit Architecture Boundary

Microsoft Entra Agent ID and Microsoft Agent 365 belong in the **Agent Governance and Identity Control Plane**.

They govern:

- agent identity;
- agent registration;
- ownership;
- lifecycle state;
- monitoring;
- policy binding;
- trust posture;
- authorization context;
- agent inventory and governance.

They are **not** operational SOC agents and must not be placed inside the SOC agentic execution layer. They do not perform alert triage, investigation, enrichment, containment recommendation, DFIR analysis, or incident response workflow execution.

## Security Objectives

The architecture must satisfy the following security objectives:

| Objective | Requirement |
|---|---|
| Tenant isolation | Agentic workflows must not retrieve, infer, summarize, act on, or release data outside authorized tenant, customer, case, incident, workflow, and evidence scope. |
| Evidence integrity | Evidence must remain attributable, traceable, preserved, and separated from derived artifacts. |
| Tool safety | Agents must not directly execute privileged, destructive, customer-impacting, or evidence-sensitive actions. |
| Policy enforcement | PDP decisions must be enforced by PEPs at real execution boundaries. |
| Human accountability | Sensitive actions require qualified human approval, scoped approval records, and customer authorization where required. |
| Agent accountability | Every agent must have identity, owner, lifecycle state, permissions, audit trail, and revocation path. |
| Retrieval integrity | RAG, vector search, and memory must be scoped, fresh, authorized, and auditable. |
| Output safety | Customer-facing outputs require validation, policy decision, release control, and audit linkage. |
| DFIR defensibility | Local/private LLM analysis must preserve chain of custody and must not turn model output into final forensic conclusions without review. |
| Audit replay | Each workflow must be reconstructable from request, context, model, prompt reference, policy decision, approval, tool action, output, and final state. |

## Protected Assets

| Asset | Protection Requirement |
|---|---|
| Customer telemetry | Must remain tenant/customer/case scoped and must not be exposed across customers or workflows. |
| Security alerts and incidents | Must preserve source metadata, timestamps, alert identifiers, confidence, severity, and evidence references. |
| Evidence objects | Must preserve provenance, chain of custody, hashes where applicable, original/derived artifact separation, and legal hold references. |
| Retrieved context | Must be scoped, freshness-validated, and traceable to source documents or evidence. |
| Knowledge stores and vector indexes | Must enforce namespace boundaries and prevent cross-customer, cross-case, stale, poisoned, or unauthorized retrieval. |
| Agent outputs | Must be treated as recommendations or draft analysis until validated by assurance, policy, and human review where required. |
| Tools and connectors | Must be accessed only through PEP-enforced wrappers with scoped permissions and audit logging. |
| Agent identities | Must be registered, owned, scoped, monitored, and revocable. |
| Approval records | Must be scoped, time-bounded, cryptographically bound, policy-validated, PEP-verified, and auditable. |
| Policy decisions | Must be deterministic, machine-parseable, time-bounded, and enforceable. |
| Customer-facing outputs | Must require release review, customer authorization where required, and evidence support. |

## Threat Actors and Failure Sources

| Actor or Failure Source | Description |
|---|---|
| External attacker | Attempts to inject malicious instructions through logs, emails, tickets, evidence, URLs, files, or telemetry. |
| Compromised customer asset | Produces logs or artifacts containing hostile instructions, forged context, or misleading activity. |
| Malicious insider | Attempts to bypass approval, alter evidence, poison retrieval, or force unsafe tool execution. |
| Compromised agent identity | Uses legitimate agent credentials outside approved scope or lifecycle state. |
| Rogue or shadow agent | Operates outside registration, ownership, monitoring, or policy enforcement. |
| Overprivileged tool connector | Allows action beyond approved scope or parameters. |
| Weak approval process | Allows approval replay, spoofing, broad approval, expired approval, or rubber-stamp review. |
| Misconfigured retrieval system | Returns stale, cross-tenant, cross-customer, cross-case, or unauthorized context. |
| Malicious tool output | Returns misleading, malformed, compromised, or prompt-injected results that influence agents or humans. |
| Model failure | Produces hallucinated findings, unsupported conclusions, unsafe recommendations, or overconfident summaries. |
| Process failure | Treats AI output as final, skips review, releases drafts, or acts without audit linkage. |

## Trust Boundaries

| Boundary | Trust Risk | Required Control |
|---|---|---|
| Telemetry to ingestion | Logs, tickets, alerts, and evidence may contain hostile instructions or forged context. | Treat input as untrusted data; normalize, classify, preserve metadata, and do not execute embedded instructions. |
| Ingestion to retrieval | Parsed content may be stale, poisoned, misclassified, or incorrectly scoped. | Enforce schema version, parser version, source metadata, sensitivity label, freshness, and scope binding. |
| Retrieval to agent | Retrieved content may cross customer/case boundaries or contain prompt injection. | Enforce `knowledge_store_or_memory_scope`, `knowledge_memory_scope_result`, source provenance, and prompt injection checks. |
| Agent to Agent Judge | Agent outputs may include unsupported claims, hallucinations, unsafe recommendations, or scope violations. | Agent Judge evaluates evidence support, policy alignment, tenant boundary, uncertainty, and release readiness. |
| Agent / Judge to PDP | Outputs and assurance findings may be incomplete or misleading. | PDP consumes deterministic request metadata, policy inputs, approval state, output destination, action type, and scope. |
| PDP to PEP | Policy decisions may be unavailable, stale, malformed, or not enforceable. | PEP validates decision fields, expiry, obligations, scope, approval record, and execution token. |
| Human approval to execution | Approval may be missing, spoofed, expired, reused, or mismatched. | Approval must be scoped, time-bounded, cryptographically bound, validated by PDP, and enforced by PEP. |
| Tool gateway to external system | Tool calls may exceed approved scope or affect wrong customer, identity, host, evidence, or output. | PEP blocks mismatched parameters, unauthorized targets, and unapproved state changes. |
| Internal output to customer release | Drafts may be mistaken for approved customer-facing findings. | Require release review, policy decision, customer authorization where required, and audit linkage. |
| Local DFIR workspace to report output | Model-generated forensic interpretation may be treated as final evidence. | Require analyst review, evidence support, chain-of-custody preservation, and separate release authorization. |

## Architecture-Wide Threat Inventory

| Threat ID | Threat | Primary Risk | Required Control |
|---|---|---|---|
| TM-001 | Prompt injection through logs, alerts, tickets, emails, reports, or evidence | Agent follows attacker-controlled instructions embedded in operational data. | Treat operational content as untrusted; separate data from instructions; use Agent Judge checks; block tool execution without PDP/PEP. |
| TM-002 | RAG or memory contamination | Agent retrieves stale, unauthorized, cross-customer, or unrelated context. | Enforce knowledge scope, retrieval freshness, tenant/customer/case binding, and retrieval audit. |
| TM-003 | RAG poisoning | Poisoned documents, summaries, notes, or embeddings bias the agent. | Validate provenance, parser version, source trust, evidence support, and sensitivity labels. |
| TM-004 | Cross-tenant or cross-customer data exposure | MSSP/MDR workflow leaks or acts on another customer's data. | Fail closed on scope mismatch; require tenant/customer/case metadata on request, retrieval, evidence, output, and audit. |
| TM-005 | Unauthorized tool execution | Agent triggers containment, identity, cloud, endpoint, ticketing, or evidence tool outside approval. | PDP decision plus PEP enforcement at tool wrapper, API gateway, workflow, and output boundary. |
| TM-006 | Weak human approval or approval replay | Approval is spoofed, reused, expired, too broad, or mismatched. | Require cryptographic binding, scoped approval records, expiration, PDP validation, PEP verification, and audit. |
| TM-007 | Customer-facing release without authorization | Draft recommendation, report, or timeline is released externally without validation. | Require output validation, release review, policy decision, customer authorization where required, and audit. |
| TM-008 | Overreliance on AI | Analysts treat model-generated recommendations or summaries as authoritative. | Require uncertainty labels, evidence support, Agent Judge review, human validation, and no final finding from model alone. |
| TM-009 | Compromised agent identity | Agent credentials are used outside intended owner, lifecycle, customer, or workflow scope. | Enforce agent registration, least privilege, credential scoping, lifecycle state, monitoring, and revocation. |
| TM-010 | Rogue or shadow agent | Unregistered agent participates in workflow or communicates with other agents. | Require agent registry, attestation, identity validation, policy binding, owner accountability, and blocking of unknown agents. |
| TM-011 | Malicious or misleading tool output | Tool output manipulates agent reasoning or causes unsafe recommendations. | Validate tool identity, schema, provenance, source/destination metadata, and output classification before use. |
| TM-012 | Policy or PEP bypass | Workflow proceeds when policy is unavailable, malformed, or not enforced. | Deny by default and fail closed on policy unavailable, missing decision, expired decision, or missing PEP enforcement. |
| TM-013 | Local LLM DFIR evidence integrity failure | Local model or workflow alters evidence or creates unsupported forensic conclusions. | Preserve originals, use working copies, separate derived artifacts, require analyst review, and enforce chain-of-custody. |
| TM-014 | Model routing or fallback failure | Workflow uses unvalidated model or external fallback for sensitive customer/evidence data. | Enforce approved model routing, version pinning, no unapproved fallback, and audit model references. |
| TM-015 | Audit and replay failure | Incident cannot be reconstructed after action, output, approval, or release. | Require correlation IDs, audit references, prompt references, model references, policy references, approval records, tool action records, and final state. |

## Threat Scenarios and Required Controls

### TM-001: Prompt Injection Through Operational Data

#### Scenario

An attacker embeds instructions in logs, emails, tickets, alerts, telemetry, analyst notes, document content, or evidence artifacts. The agent retrieves the content and treats the attacker-controlled text as instructions instead of untrusted data.

#### Attack Path

1. Attacker places hostile instructions into an operational source.
2. Ingestion normalizes the source without marking prompt-injection risk.
3. Retrieval returns the content as context.
4. Agent follows the embedded instruction.
5. Agent recommends or attempts tool use, data release, memory write, or customer notification.

#### Required Controls

- Treat all telemetry, evidence, logs, tickets, emails, and case notes as untrusted input.
- Preserve source system, parser version, schema version, evidence reference, and ingestion timestamp.
- Separate retrieved content from system, developer, policy, and workflow instructions.
- Agent Judge must evaluate whether output appears influenced by retrieved hostile instructions.
- PEP must block tool execution unless PDP authorization and approval requirements are satisfied.
- Customer-facing release must require separate validation.

#### Fail-Closed Conditions

- Retrieved content attempts to override policy, scope, approval, model routing, or tool restrictions.
- Agent output references instructions from telemetry as if they are workflow instructions.
- Prompt-injection risk is detected and no review or sanitization result exists.
- Output requests sensitive execution without valid PDP decision and approval where required.

### TM-002: RAG or Memory Contamination

#### Scenario

The retrieval layer returns information from the wrong customer, tenant, case, incident, evidence set, historical case, or stale knowledge entry.

#### Attack Path

1. Workflow sends an underspecified retrieval request.
2. Vector search or memory returns semantically similar but unauthorized context.
3. Agent uses that context in a recommendation, timeline, report, approval request, or tool request.
4. Output leaks information or triggers action based on unrelated context.

#### Required Controls

- Every retrieval request must include `tenant_id`, `customer_id`, `case_id`, `incident_id`, `workflow_id`, and authorized namespace where applicable.
- Retrieval must return `knowledge_store_or_memory_scope` and `knowledge_memory_scope_result`.
- Retrieval must log retrieved context IDs, source system IDs, data classification, sensitivity label, and freshness result.
- Cross-customer, cross-tenant, cross-case, and stale-context detection must be enforced.
- Agent Judge must check retrieved-context scope before release or action.

#### Fail-Closed Conditions

- Missing or mismatched tenant, customer, case, incident, workflow, or evidence scope.
- Retrieval result lacks source attribution or freshness.
- Knowledge scope result is not scoped to the authorized customer/case/incident.
- Cross-scope context is detected.

### TM-003: RAG Poisoning

#### Scenario

An attacker or compromised source injects misleading content into documents, notes, case knowledge, embeddings, summaries, or indexed evidence to bias model output.

#### Attack Path

1. Poisoned content enters a retrieval source.
2. Ingestion indexes the content without provenance or trust classification.
3. Agent retrieves the poisoned content.
4. Agent produces a biased recommendation, false conclusion, or unsafe action proposal.

#### Required Controls

- Source provenance, parser version, ingestion timestamp, source system ID, and sensitivity label must be preserved.
- Retrieved content must distinguish original evidence, derived artifact, analyst note, model-generated summary, and external reference.
- Evidence-sensitive conclusions must cite evidence object IDs.
- Agent Judge must detect unsupported claims and overreliance on low-trust context.
- High-impact actions cannot be based solely on unvalidated retrieved content.

#### Fail-Closed Conditions

- Retrieved source lacks provenance.
- Retrieved source is model-generated but not labeled as derived or unverified.
- Evidence-sensitive output lacks evidence object IDs.
- A recommendation relies on low-trust or poisoned content without validation.

### TM-004: Cross-Tenant or Cross-Customer Exposure

#### Scenario

An MSSP or MDR workflow retrieves, summarizes, recommends action on, or releases data belonging to another customer or tenant.

#### Attack Path

1. Workflow context is missing or ambiguous.
2. Retrieval returns another customer's context.
3. Agent includes cross-customer data in an output.
4. Tool execution or customer-facing release affects the wrong customer.

#### Required Controls

- Tenant/customer/case/workflow/evidence scope must be mandatory on requests, retrieval, outputs, policy decisions, approvals, tool calls, and audit records.
- PEP must enforce tenant/customer/case scope at retrieval, tool, output, and workflow boundaries.
- Customer-facing output must be blocked on scope ambiguity.
- Audit records must include scope result and scope violation result.

#### Fail-Closed Conditions

- Missing `tenant_id` or `customer_id`.
- Output destination does not match authorized customer scope.
- Tool target differs from approved customer or tenant.
- Retrieval includes other customer, tenant, or unrelated case context.

### TM-005: Unauthorized Tool Execution

#### Scenario

An agent attempts to execute or cause execution of endpoint isolation, credential reset, session revocation, indicator blocking, evidence export, ticket closure, or customer notification without authorization.

#### Attack Path

1. Agent recommends sensitive action.
2. Workflow treats recommendation as executable instruction.
3. Tool call is made without policy decision or approval.
4. Customer environment, evidence, or incident state is changed.

#### Required Controls

- Agent outputs are recommendations only unless PDP and PEP authorize execution.
- Tool execution must be denied by default.
- Tool calls require `tool_id`, `tool_owner`, `source_system_id`, `destination_system_id`, `requested_action`, target scope, approved parameters, and output destination.
- PEP must enforce at tool wrapper and API gateway boundaries.
- Sensitive actions require approval and customer authorization where applicable.

#### Fail-Closed Conditions

- Missing policy decision.
- Missing approval where required.
- Tool target or parameters differ from approval record.
- Tool execution token is missing, expired, invalid, or mismatched.
- Policy unavailable or PEP unavailable.

### TM-006: Weak Human Approval or Approval Replay

#### Scenario

Approval is represented as a simple boolean, reused outside scope, spoofed by a compromised component, expired, or applied to different action parameters than the reviewer approved.

#### Attack Path

1. Approval record is created without cryptographic binding or scope.
2. Downstream workflow modifies target identity, customer, action, or parameters.
3. PEP checks only that approval exists.
4. Unauthorized action executes.

#### Required Controls

- Approval records must include reviewer identity, reviewer role, timestamp, action, scope, parameters, conditions, expiration, customer authorization reference where required, and cryptographic binding.
- Approval must be bound to signed payload references such as request ID, evidence reference, action target, and approval request.
- PDP must validate approval before final authorization.
- PDP may mint a time-bounded execution token after approval validation.
- PEP must verify token signature, scope, target, action, and `expires_at`.

#### Fail-Closed Conditions

- Approval is missing, expired, reused, unsigned, or mismatched.
- Approval scope does not match execution target.
- Customer authorization is required but absent.
- Execution token is missing or invalid.
- Action changes after approval.

### TM-007: Customer-Facing Release Without Authorization

#### Scenario

An internal recommendation, timeline, report draft, or model-generated summary is released to the customer without proper review, approval, or customer authorization.

#### Attack Path

1. Agent drafts customer-facing language.
2. Workflow incorrectly treats draft as approved output.
3. Unsupported claims, sensitive data, or inaccurate findings are released.
4. Customer, legal, or operational impact occurs.

#### Required Controls

- Customer-facing release must require policy decision and release review.
- Agent Judge must evaluate evidence support, unsupported claims, tenant boundary, sensitive data exposure, and release readiness.
- Human reviewer must approve release where required.
- Customer authorization must be represented where required.
- Output destination must be enforced by PEP.

#### Fail-Closed Conditions

- Output destination is missing or unauthorized.
- Customer-facing flag is true and release review is absent.
- Output contains final forensic conclusions without evidence support and review.
- Customer authorization required but missing.

### TM-008: Overreliance on AI

#### Scenario

Analysts or workflows treat AI output as authoritative, resulting in unsupported conclusions, false findings, unsafe containment, or premature customer communication.

#### Attack Path

1. Model produces plausible but unsupported summary or recommendation.
2. Analyst accepts output without checking evidence.
3. Workflow routes output to action, report, or customer release.
4. Incorrect or unsupported action is taken.

#### Required Controls

- Outputs must distinguish observed facts, model-assisted interpretation, hypotheses, and final findings.
- Agent Judge must identify unsupported claims and uncertainty.
- Human review must be required for sensitive or evidence-sensitive outputs.
- Final forensic findings and customer-facing statements require separate review.
- Policy must prevent model output from authorizing execution.

#### Fail-Closed Conditions

- Output contains final finding but lacks evidence object IDs.
- Confidence is overstated relative to evidence.
- Unsupported claims are not flagged.
- Human review is required but absent.

### TM-009: Compromised Agent Identity

#### Scenario

A legitimate agent identity is stolen, overprivileged, or used outside its approved customer, workflow, or lifecycle state.

#### Attack Path

1. Agent credentials or token are compromised.
2. Attacker uses agent identity to request retrieval, tool use, or output release.
3. Workflow trusts the agent identity.
4. Unauthorized access or action occurs.

#### Required Controls

- All agents must be registered, owned, scoped, monitored, and lifecycle-managed.
- Agent permissions must be least privilege and task-specific.
- Agent credentials must be scoped and revocable.
- Agent identity must be validated before retrieval, tool use, and output release.
- Agent activity must be audited and anomaly-monitored.

#### Fail-Closed Conditions

- Agent is unregistered, disabled, expired, or outside lifecycle state.
- Agent owner is missing.
- Agent requests action outside allowed permissions.
- Agent attempts cross-customer, cross-case, or unauthorized tool activity.

### TM-010: Rogue or Shadow Agent

#### Scenario

An unregistered agent participates in workflow routing, delegates to other agents, accesses tools, or produces outputs outside governance.

#### Attack Path

1. Shadow agent is created outside registry or lifecycle controls.
2. Agent receives task or context through unmanaged channel.
3. Agent delegates, retrieves, or recommends action without policy binding.
4. Output enters workflow as if trusted.

#### Required Controls

- Agent registry must be authoritative for runtime participation.
- Agent-to-agent communication must require identity, authorization, purpose, scope, and audit.
- Unknown agents must be blocked or quarantined.
- Agent lifecycle state must be checked before task execution.
- Ownership and monitoring must be mandatory.

#### Fail-Closed Conditions

- Agent not found in registry.
- Agent lacks owner or lifecycle state.
- Agent-to-agent request lacks authorized purpose.
- Agent attempts to delegate outside policy.

### TM-011: Malicious or Misleading Tool Output

#### Scenario

A tool returns compromised, malformed, stale, adversarial, or prompt-injected output that influences agent decisions or human approval.

#### Attack Path

1. Agent invokes or receives result from tool.
2. Tool output includes false data, hidden instructions, unexpected schema, or stale state.
3. Agent treats output as trusted.
4. Recommendation, approval request, or action is based on compromised output.

#### Required Controls

- Tool outputs must include tool identity, version, owner, source system, destination system, timestamp, schema version, and classification.
- PEP or validation layer must reject malformed or unexpected output.
- Tool outputs must be treated as data, not instructions.
- High-impact recommendations require corroboration.

#### Fail-Closed Conditions

- Tool output schema is invalid.
- Source or destination metadata is missing.
- Tool output includes instruction-like content.
- Output conflicts with approved scope or policy.

### TM-012: Policy or PEP Bypass

#### Scenario

Workflow proceeds when policy is unavailable, malformed, ambiguous, expired, or not enforced at the execution boundary.

#### Attack Path

1. PDP is unavailable or returns ambiguous decision.
2. Workflow defaults to allow or uses cached decision improperly.
3. PEP does not enforce or is bypassed.
4. Tool execution, retrieval, or release occurs without authorization.

#### Required Controls

- Deny by default.
- Fail closed on policy unavailable.
- Policy decisions must use deterministic root-level fields where applicable, including `decision`, `reason`, `expires_at`, and `audit_required`.
- PEP must enforce at runtime boundary, not only at planning stage.
- Decision expiry must be checked before execution.

#### Fail-Closed Conditions

- PDP unavailable.
- Decision is missing, expired, malformed, or unsupported.
- PEP enforcement result missing.
- Requested action differs from policy decision.

### TM-013: Local LLM DFIR Evidence Integrity Failure

#### Scenario

Private/local LLM-assisted DFIR modifies evidence, mixes case context, generates unsupported conclusions, or creates unreviewed customer-facing forensic output.

#### Attack Path

1. Evidence is loaded into local LLM workflow.
2. Model generates timeline or findings.
3. Original evidence or derived artifacts are not separated.
4. Model output is treated as final or released without review.

#### Required Controls

- Original evidence must remain read-only.
- Working copies and derived artifacts must be separated.
- Evidence object IDs, hashes, chain-of-custody references, and legal hold references must be preserved where applicable.
- Local retrieval must be case/evidence scoped.
- Human review must approve internal use of timelines or findings.
- Customer-facing release requires separate authorization.

#### Fail-Closed Conditions

- Evidence scope missing.
- Original evidence modified.
- Chain-of-custody reference missing where required.
- Timeline contains final findings without analyst review.
- Customer-facing release attempted without release review.

### TM-014: Model Routing or Fallback Failure

#### Scenario

Sensitive workflow uses an unapproved model, unvalidated fallback, external API, or model profile not authorized for customer data or evidence.

#### Attack Path

1. Approved model unavailable.
2. Workflow silently falls back to unapproved model.
3. Sensitive customer or evidence data leaves approved boundary.
4. Output is generated without validation or audit.

#### Required Controls

- Approved model routing required.
- Model version pinning required where sensitive.
- Unvalidated fallback must be denied.
- External network access must be blocked where prohibited.
- Model references must be logged in audit event.

#### Fail-Closed Conditions

- Model profile unapproved.
- Model version missing.
- External fallback attempted.
- Model routing policy unavailable.
- Training on customer data attempted.

### TM-015: Audit and Replay Failure

#### Scenario

The organization cannot reconstruct what happened, what context was used, what policy was evaluated, what approval was granted, what tool executed, or what output was released.

#### Attack Path

1. Workflow omits prompt reference, policy request reference, retrieval IDs, approval record, or tool action.
2. Incident is later challenged.
3. SOC, legal, audit, or DFIR team cannot reconstruct the event.
4. Accountability and defensibility fail.

#### Required Controls

Audit records must include, where relevant:

- request ID;
- correlation ID;
- audit reference ID;
- prompt reference;
- model reference;
- policy request reference;
- policy decision ID;
- approval record ID;
- customer authorization reference;
- evidence object IDs;
- retrieved context IDs;
- tool action;
- source system ID;
- destination system ID;
- output destination;
- final workflow state.

#### Fail-Closed Conditions

- Sensitive action lacks audit event.
- Customer-facing output lacks release record.
- Evidence-sensitive output lacks evidence references.
- Tool execution lacks action result and PEP enforcement result.

## Threat-to-Control Mapping

| Threat ID | PDP | PEP | Agent Judge | Human Approval | Customer Authorization | Audit / Replay |
|---|---|---|---|---|---|---|
| TM-001 | Determines if output/action is allowed after injection risk. | Blocks tool use and release on unsafe content. | Checks influence from hostile retrieved content. | Required for sensitive output/action. | Required for customer release where applicable. | Logs source content, prompt ref, decision, output. |
| TM-002 | Determines retrieval authorization. | Enforces retrieval namespace and output scope. | Checks retrieved-context scope. | Required if contaminated context affects sensitive action. | Required if customer impact exists. | Logs retrieved context IDs and scope result. |
| TM-003 | Determines whether context is trusted enough for use. | Blocks unsafe use of poisoned context. | Checks unsupported claims and provenance. | Required for high-impact decisions. | As required by action/release. | Logs provenance, parser, source, evidence refs. |
| TM-004 | Determines tenant/customer/case authorization. | Enforces scope at retrieval, tool, and output. | Checks boundary violations. | Required for sensitive action. | Required for customer-impacting action. | Logs scope result and violations. |
| TM-005 | Determines tool authorization. | Enforces approved action, scope, and parameters. | Evaluates recommendation quality. | Required for sensitive action. | Required where customer-impacting. | Logs tool action and execution result. |
| TM-006 | Validates approval record and final authorization. | Verifies execution token and approval scope. | May flag approval mismatch in output flow. | Required and must be cryptographically bound. | Required where applicable. | Logs approval, signature refs, decision, token. |
| TM-007 | Determines release authorization. | Enforces output destination and release boundary. | Checks evidence support and release readiness. | Required for release. | Required where customer-facing. | Logs release decision and output destination. |
| TM-008 | Blocks action based on unsupported AI output. | Blocks execution/release without validation. | Detects unsupported claims and uncertainty issues. | Required for sensitive/evidence outputs. | Required where applicable. | Logs review and rejected claims. |
| TM-009 | Determines agent authorization. | Enforces agent identity and permissions. | May flag anomalous agent output. | Required for sensitive requests. | As applicable. | Logs agent identity and lifecycle state. |
| TM-010 | Blocks unregistered agent participation. | Enforces registry and communication controls. | N/A unless output is produced. | Required for sensitive workflows. | As applicable. | Logs agent registry and delegation. |
| TM-011 | Determines whether tool output may influence decision. | Blocks malformed or untrusted tool output. | Checks tool-output support in conclusions. | Required for high-impact decisions. | As applicable. | Logs tool output schema and metadata. |
| TM-012 | Produces deterministic decision or fail closed. | Enforces decision, expiry, and obligations. | May flag missing policy alignment. | Required where policy requires. | As applicable. | Logs decision and enforcement result. |
| TM-013 | Determines DFIR action/release authorization. | Enforces evidence and output boundaries. | Checks evidence support and final finding risk. | Required for timeline/report/finding use. | Required for customer release. | Logs evidence, chain of custody, review. |
| TM-014 | Determines approved model routing. | Enforces model gateway restrictions. | Checks model reference and confidence. | Required if high-risk output. | As applicable. | Logs model profile and version. |
| TM-015 | Requires audit for sensitive paths. | Blocks execution or release if audit cannot be emitted. | Checks traceability where applicable. | Approval must be linked. | Authorization must be linked. | Primary control objective. |

## Required Control Surface Metadata

| Control Surface | Minimum Required Fields |
|---|---|
| Request | `request_id`, `correlation_id`, `audit_reference_id`, `created_at`, `tenant_id`, `customer_id`, `case_id`, `incident_id`, `workflow_id`, `authorized_purpose`, `output_destination` |
| Normalized event | `source_system_id`, `evidence_ref`, `source_timestamp`, `ingestion_timestamp`, `entity_refs`, `data_classification`, `sensitivity_label` |
| Retrieval | `knowledge_store_or_memory_scope`, `knowledge_memory_scope_result`, `retrieved_context_ids`, `freshness_result`, `cross_scope_result` |
| Agent output | `agent_id`, `task_id`, `output_destination`, `confidence`, `uncertainties`, `supporting_context`, `proposed_sensitive_actions` |
| Judge output | `judge_id`, `evaluation_result`, `evidence_supported`, `unsupported_claims`, `tenant_boundary_risk`, `sensitive_action_detected`, `hitl_required` |
| Policy decision | `policy_decision_id`, `decision`, `reason`, `required_approver_role`, `expires_at`, `audit_required`, `obligations`, `denied_operations` |
| Approval record | `approval_record_id`, `reviewer_id`, `reviewer_role`, `approved_action`, `approved_scope`, `approved_parameters`, `expires_at`, `cryptographic_binding` |
| Tool action | `tool_action`, `tool_id`, `tool_owner`, `source_system_id`, `destination_system_id`, `target_scope`, `parameters_enforced`, `execution_result` |
| Audit event | `audit_event_id`, `audit_reference_id`, `correlation_id`, `source_artifacts`, `prompt_ref`, `policy_request_ref`, `final_state`, `reconstruction_fields_present` |

## Deny and Fail-Closed Conditions

The architecture must deny, fail closed, or return for clarification when any of the following occur:

| Condition | Required Behavior |
|---|---|
| Missing tenant, customer, case, incident, or workflow scope | Deny retrieval, tool execution, and customer-facing release. |
| Scope mismatch between request, retrieval, policy, approval, tool target, or output destination | Fail closed. |
| Retrieved context crosses customer, tenant, case, incident, or evidence boundary | Block context use and emit audit event. |
| Retrieved content lacks provenance or freshness result | Treat as untrusted and exclude from authoritative reasoning. |
| Prompt injection risk is detected without mitigation or review | Block sensitive action and release. |
| Agent output contains unsupported final findings | Require review; block customer-facing release. |
| Agent requests tool execution without PDP decision | Deny execution. |
| PDP is unavailable or decision is malformed | Fail closed. |
| PEP is unavailable or cannot enforce | Fail closed. |
| Approval required but missing | Deny execution and route for approval. |
| Approval expired, reused, unsigned, or mismatched | Fail closed. |
| Customer authorization required but missing | Deny customer-impacting action or release. |
| Tool output is malformed, stale, or outside schema | Treat as untrusted and block dependent action. |
| Model routing attempts unapproved fallback | Deny model execution. |
| Evidence original is modified by analysis workflow | Escalate as evidence integrity violation. |
| Audit event cannot be emitted for sensitive action | Block execution or release. |

## Audit and Replay Requirements

Every high-impact or evidence-sensitive workflow must support audit replay.

Audit events must reconstruct:

- who or what requested the workflow;
- what scope was authorized;
- what prompt template or prompt reference was used;
- what model profile and version were used;
- what retrieval sources and context IDs were used;
- what evidence objects or derived artifacts were referenced;
- what agent output was produced;
- what Agent Judge evaluated;
- what unsupported claims were identified;
- what policy decision was returned;
- whether approval was required;
- what approval record was used;
- whether customer authorization was required;
- what tool action was attempted or executed;
- what PEP enforced;
- what output destination was used;
- what final workflow state resulted.

Minimum audit references include:

- `audit_reference_id`;
- `correlation_id`;
- `request_id`;
- `prompt_ref`;
- `policy_request_ref`;
- `policy_decision_id`;
- `approval_record_id` where applicable;
- `customer_authorization_reference` where applicable;
- `tool_action`;
- `source_system_id`;
- `destination_system_id`;
- `output_destination`;
- `final_state`.

## Service Model Impact

| Service Model | Impact of Threat Model |
|---|---|
| MSSP | Prevents cross-customer bleed, unauthorized customer-facing release, weak customer authorization, and unsafe managed-service actions. |
| MDR | Prevents unsafe containment, unapproved response automation, weak analyst review, and policy bypass during alert triage and response. |
| SOC / Incident Response | Prevents unsupported incident conclusions, unsafe escalation, state-changing actions without authorization, and poor auditability. |
| Cloud Incident Response | Prevents unsafe IAM changes, OAuth removal, session revocation, credential reset, customer notification, and cloud evidence misuse. |
| DFIR | Prevents evidence integrity failure, unsupported forensic findings, weak chain-of-custody linkage, and premature report release. |
| Private / Local LLM-assisted DFIR | Prevents local retrieval contamination, evidence mishandling, unreviewed timelines, unsupported conclusions, and unapproved external release. |

## Acceptance Criteria

This threat model is acceptable when:

- every architecture-wide threat maps to enforceable controls;
- Agent Judges are treated as assurance, not approval;
- PDP decisions are treated as authorization decisions, not advisory text;
- PEP enforcement occurs at real boundaries, not only in documentation;
- human approval is scoped, time-bounded, cryptographically bound, policy-validated, PEP-verified, and audited where sensitive actions are involved;
- customer authorization is represented separately from internal approval where required;
- RAG, vector search, memory, retrieved context, and tool output are treated as untrusted until validated;
- tenant, customer, case, incident, workflow, evidence, retrieval, tool, output, and audit boundaries are explicit;
- private/local LLM-assisted DFIR preserves evidence integrity and requires analyst review;
- Microsoft Entra Agent ID and Microsoft Agent 365 are represented only in the governance and identity control plane;
- audit and replay can reconstruct sensitive workflows end-to-end.

## Non-Goals

This file does not:

- define a vendor-specific implementation;
- replace formal STRIDE analysis, MITRE ATLAS mapping, ATT&CK mapping, NIST AI RMF review, legal review, or customer-specific risk assessment;
- authorize production containment;
- define every schema field for every artifact;
- treat AI output as a final finding;
- require human approval for every low-risk read-only action;
- replace specific threat files in this directory.

## Related Files

| File | Relationship |
|---|---|
| `README.md` | Directory scope, file map, control expectations, and reading order. |
| `mitre-atlas-threats.md` | AI and model threat mapping. |
| `prompt-injection-through-logs.md` | Detailed prompt injection threat model. |
| `rag-memory-contamination.md` | Retrieval and memory contamination model. |
| `rag-poisoning.md` | Poisoned retrieval/index/content model. |
| `cross-tenant-cross-customer-risk.md` | Tenant/customer/case boundary threat model. |
| `tool-use-and-automation-risk.md` | Tool execution and automation threat model. |
| `malicious-tool-output.md` | Tool output integrity threat model. |
| `human-approval-and-release-risk.md` | Approval and release threat model. |
| `overreliance-on-ai.md` | Automation bias and weak review threat model. |
| `compromised-agent-identity.md` | Agent identity compromise threat model. |
| `rogue-agent-risk.md` | Rogue and unmanaged agent threat model. |
| `local-llm-dfir-risk.md` | Private/local LLM-assisted DFIR threat model. |
| `mitigations.md` | Consolidated mitigation catalog. |

## Summary

This threat model defines the architecture-wide failure modes and required controls for governed agentic security operations.

The architecture is acceptable only when agents, tools, retrieval systems, memory, approvals, policy decisions, outputs, and humans are not implicitly trusted. Sensitive actions, evidence handling, retrieval, tool use, agent identity, customer-facing release, and forensic conclusions must be bound to explicit scope, deterministic policy decisions, enforceable PEP controls, qualified human approval where required, customer authorization where required, and complete auditability.
