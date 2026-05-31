# Private / Local LLM-Assisted DFIR Pattern

## Purpose

This pattern defines how private, local, isolated, or customer-controlled LLMs can be used to assist **Digital Forensics and Incident Response (DFIR)** without weakening forensic integrity, evidence handling, customer trust, or operational accountability.

It supports the broader **Agentic MSSP / MDR / DFIR Security Operations Architecture** where applicable by defining how local LLM-assisted forensic workflows should preserve case scope, evidence provenance, chain of custody, policy enforcement, human review, auditability, and controlled tool use.

## Pattern Summary

Private or local LLM execution does not automatically make DFIR safe, trustworthy, or forensically valid.

The core pattern is:

**Case-scoped forensic workspace**  
→ **approved evidence and context ingestion**  
→ **private / local LLM-assisted analysis**  
→ **policy-controlled retrieval, memory, and tool use**  
→ **human validation of findings**  
→ **evidence-backed reporting**  
→ **auditable, replayable, governed workflow**

This pattern allows an LLM to assist forensic work while ensuring that final findings, conclusions, and customer-facing outputs remain evidence-supported, human-validated, and traceable.

## Context

DFIR workflows often involve sensitive evidence, customer data, legal-sensitive material, regulated data, privileged logs, malware artifacts, identity records, endpoint telemetry, memory captures, disk images, cloud logs, timelines, and incident reports.

Private or local LLM-assisted DFIR may be used when:

- evidence cannot be sent to a public or shared AI service;
- customer requirements require local processing;
- legal, regulatory, sovereignty, or contractual requirements restrict data movement;
- forensic teams need offline or air-gapped analysis support;
- local models are used to summarize artifacts, timelines, logs, or reports;
- private RAG is used over case files, evidence metadata, or approved reference material;
- agentic workflows assist analysts but must not alter evidence or bypass review.

This pattern is not about replacing the forensic analyst. It is about using AI assistance safely inside a controlled DFIR workflow.

## Problem

How can a security organization use private or local LLMs to assist DFIR while preserving evidence integrity, case boundaries, chain of custody, auditability, and human accountability?

## Forces

This pattern balances the following forces:

- **Data sensitivity vs. AI assistance** — forensic teams may benefit from LLM support, but evidence and customer data may not be allowed to leave controlled environments.
- **Speed vs. forensic validity** — LLMs can accelerate review and summarization, but forensic conclusions must remain evidence-backed and analyst-validated.
- **Local execution vs. governance** — local execution reduces some data exposure risks, but does not remove the need for policy, audit, and review.
- **RAG usefulness vs. case contamination** — local retrieval over case materials is useful, but must not blend evidence, cases, customers, or stale context.
- **Tool assistance vs. evidence preservation** — tools can parse artifacts and generate timelines, but must not modify source evidence unless explicitly approved.
- **Automation vs. legal defensibility** — AI outputs may assist analysis, but reports and findings must be traceable, explainable, and reviewable.
- **Analyst productivity vs. overreliance** — LLMs can assist, but analysts remain responsible for validation, interpretation, and final conclusions.

## Applicability

Use this pattern when DFIR work uses:

- local LLMs;
- private hosted LLMs;
- offline LLM runtimes;
- customer-controlled LLM environments;
- isolated forensic workstations;
- local RAG over case material;
- local vector stores or knowledge stores;
- LLM-assisted evidence summarization;
- LLM-assisted artifact review;
- LLM-assisted timeline creation;
- LLM-assisted report drafting;
- LLM-assisted query generation;
- agentic forensic workflow assistance.

This pattern may apply to:

- **DFIR** — forensic analysis, timeline support, evidence review, report preparation, and case documentation.
- **SOC / Incident Response** — incident analysis support when forensic evidence or case records are involved.
- **MDR** — response support when forensic triage, evidence interpretation, or customer-impacting conclusions are involved.
- **MSSP** — customer reporting or escalation support where local/private DFIR analysis feeds managed service delivery.

Do not force this pattern onto purely manual DFIR work that does not use LLM assistance, retrieval, memory, or AI-assisted tooling. Manual DFIR still requires evidence integrity, chain of custody, human review, and auditability, but may not require LLM-specific controls.

## Solution

Implement Private / Local LLM-assisted DFIR as a controlled forensic analysis pattern with eight required elements:

1. **Case-Scoped Workspace**  
   Each DFIR workflow must be bound to a specific customer, case, incident, engagement, evidence set, and authorized purpose.

2. **Controlled Evidence Ingestion**  
   Evidence, artifacts, logs, timelines, and reports must be ingested only through approved processes that preserve provenance, hashes, timestamps, source identifiers, parser versions, and chain-of-custody metadata.

3. **Private / Local Model Boundary**  
   LLM execution must occur within an approved local, private, isolated, or customer-controlled environment that prevents unauthorized data movement.

4. **Policy-Gated Retrieval and Memory**  
   Local RAG, vector search, case memory, and workflow memory must remain scoped to the authorized case, customer, evidence set, and retention boundary.

5. **Policy-Enforced Tool Use**  
   Forensic tools, parsers, scripts, notebooks, APIs, and local automation must execute only through approved, logged, and scoped workflows.

6. **Human-Validated Findings**  
   LLM-generated summaries, interpretations, hypotheses, timelines, and report sections must be reviewed by qualified human analysts before being treated as findings.

7. **Evidence-Backed Output**  
   Reports and conclusions must distinguish observed evidence from model-generated interpretation and must tie claims to evidence references.

8. **Audit and Replayability**  
   Prompts, retrieved context, memory reads/writes, tool actions, evidence references, analyst approvals, and output versions must be logged sufficiently to reconstruct the workflow.

## Architecture Roles

### DFIR Analyst

The DFIR analyst remains accountable for investigation quality and final findings.

The analyst may use the LLM to:

- summarize evidence;
- explain logs;
- identify timeline gaps;
- draft report sections;
- generate investigative hypotheses;
- prepare query ideas;
- compare artifacts;
- organize case notes.

The analyst must validate outputs against evidence before using them as findings.

### Private / Local LLM Runtime

The LLM runtime provides local or controlled model execution.

It should:

- operate within an approved environment;
- prevent unauthorized network egress where required;
- avoid sending evidence to unapproved external services;
- log model version and configuration;
- preserve prompt and response records where policy allows;
- enforce approved context boundaries;
- avoid uncontrolled model or prompt self-modification.

### Case Workspace

The case workspace organizes DFIR work around the authorized investigation.

It should include:

- case identifier;
- customer identifier;
- incident identifier;
- evidence inventory;
- analyst notes;
- approved reports;
- tool outputs;
- timelines;
- retrieval indexes;
- local memory or case summaries where approved;
- audit references.

### Evidence Store

The evidence store preserves original and derived evidence.

It should:

- preserve original evidence in read-only form where required;
- record source, hash, timestamp, and provenance;
- maintain chain-of-custody metadata;
- separate originals from derived artifacts;
- restrict access by case and role;
- log evidence access and transformation.

### Local RAG / Knowledge Store

The local RAG or knowledge store provides approved case context to the model.

It may include:

- case notes;
- evidence metadata;
- parsed logs;
- extracted indicators;
- artifact summaries;
- approved reference material;
- customer-approved documentation;
- prior validated findings.

It must not include unrelated cases, unauthorized customer data, stale memory, or uncontrolled global context.

### Forensic Tooling Layer

The forensic tooling layer may include local scripts, parsers, notebooks, timeline tools, malware analysis tools, log analysis utilities, and case management workflows.

Tool use should be:

- read-only by default for source evidence;
- scoped to case and evidence objects;
- logged;
- versioned;
- repeatable;
- reviewed when outputs support findings.

### Policy and Approval Layer

Policy and approval controls determine whether retrieval, memory use, tool actions, outputs, or report release are allowed.

This layer should enforce:

- case scope;
- evidence scope;
- analyst role;
- tool permissions;
- output destination;
- approval requirements;
- customer authorization where required;
- fail-closed behavior.

### Audit and Assurance Layer

The audit and assurance layer supports review, reconstruction, and quality control.

It should capture:

- prompt references;
- model version;
- retrieved context;
- memory reads and writes;
- evidence references;
- tool execution;
- analyst validation;
- approval records;
- report versions;
- output destinations.

## Reference Flow

A Private / Local LLM-assisted DFIR workflow should operate as follows:

1. A DFIR case is opened with customer, case, incident, and engagement scope.
2. Evidence is collected and registered with provenance, hash, timestamp, source, owner, and chain-of-custody metadata.
3. Original evidence is stored in a protected evidence store.
4. Derived artifacts are generated through approved parsers or forensic tools.
5. Approved case material is indexed for local retrieval where needed.
6. The analyst submits a case-scoped question, task, or analysis request.
7. The retrieval layer returns only approved case-scoped context.
8. The local LLM generates a summary, hypothesis, explanation, draft, or recommended next step.
9. Any proposed tool action is evaluated through policy-enforced tool use.
10. Any sensitive output, forensic conclusion, or customer-facing material is routed for human validation.
11. Validated findings are tied to evidence references.
12. Reports distinguish observed evidence, analyst interpretation, and LLM-assisted draft text.
13. Prompts, context, tool actions, approvals, and outputs are logged.
14. Case closure triggers retention, deletion, archive, or transfer handling according to policy and customer requirements.

## Decision Outcomes

The pattern requires explicit decision outcomes:

- **Allow** — proceed with local analysis, retrieval, memory access, or tool use within approved case scope.
- **Deny** — block the request and fail closed.
- **Restrict** — allow only read-only, reduced-scope, redacted, or non-persistent operation.
- **Require Human Review** — route findings, report text, evidence-sensitive actions, or tool use to a qualified analyst.
- **Require Customer Authorization** — pause when customer authority is required for evidence transfer, report release, external communication, or customer-impacting action.
- **Return for Clarification** — request more detail when case, evidence, purpose, authority, or output destination is unclear.
- **Quarantine** — isolate untrusted, mis-scoped, contaminated, or unverified data.
- **Expire / Delete** — remove local memory, indexes, derived data, or outputs according to retention and case closure requirements.

## DFIR Use Cases

### Evidence Summarization

LLM assistance may summarize approved evidence or derived artifacts.

Controls:

- source evidence must remain preserved;
- summaries must include evidence references;
- generated summaries must not replace original evidence;
- analyst validation is required before findings are used.

### Timeline Assistance

LLM assistance may help organize events into timeline form.

Controls:

- timeline entries must reference source artifacts;
- timestamps and time zones must be preserved;
- inferred sequence must be distinguished from observed evidence;
- analyst validation is required.

### Artifact Explanation

LLM assistance may explain logs, commands, registry keys, scripts, files, indicators, or observed behavior.

Controls:

- explanations must be grounded in evidence and approved references;
- uncertain interpretation must be labeled;
- analyst review is required for conclusions.

### Report Drafting

LLM assistance may draft internal or customer-facing report sections.

Controls:

- report text must be reviewed;
- claims must be evidence-backed;
- sensitive data must be handled according to policy;
- customer-facing release requires approved process and authorization where required.

### Query and Script Assistance

LLM assistance may draft queries or scripts for analyst review.

Controls:

- generated queries or scripts must be reviewed before use;
- execution must occur through approved tooling;
- scripts must not modify evidence unless explicitly approved;
- tool outputs must be logged.

### Local RAG Over Case Material

LLM assistance may retrieve case-scoped context.

Controls:

- retrieval must be case-scoped;
- unrelated cases must not be returned;
- stale or expired memory must not influence findings;
- retrieval results must be logged.

## Evidence Integrity Requirements

Private / Local LLM-assisted DFIR must preserve forensic integrity.

Required controls include:

- original evidence preserved in read-only form where required;
- evidence hash recorded before and after authorized processing where applicable;
- derived artifacts separated from originals;
- chain-of-custody metadata maintained;
- evidence object identifiers used in findings;
- tool and parser versions recorded;
- transformations logged;
- analyst validation documented;
- model-generated interpretation separated from observed facts;
- customer-facing conclusions tied to evidence references.

## Local Model and Runtime Requirements

The local or private LLM runtime should enforce:

- approved model selection;
- model version tracking;
- approved configuration;
- controlled prompt templates;
- restricted network egress where required;
- no unauthorized external API calls;
- local storage controls;
- access control by analyst, case, and role;
- logging of prompt and response metadata;
- retention and deletion handling;
- governed model, prompt, and workflow updates.

If prompts or responses contain sensitive evidence, logs must follow evidence, privacy, legal, and customer requirements. Where full prompt logging is not allowed, metadata and references should still support review and reconstruction.

## RAG and Memory Requirements

Local RAG and memory must be scoped and governed.

Required controls include:

- case-specific namespaces;
- customer and tenant labels;
- evidence object references;
- data classification and sensitivity labels;
- retention policy identifiers;
- approved ingestion sources;
- parser and transformation versioning;
- memory write approval for persistent memory;
- deletion and expiration handling;
- cross-case retrieval tests;
- audit logs for retrieval and memory influence.

Agents must not store persistent case memory by default. Persistent memory should require explicit purpose, owner, retention, approval, and audit trail.

## Tool Use Requirements

Local forensic tools and agent-assisted tool calls must be governed.

Required controls include:

- approved tool registry;
- tool owner;
- tool purpose;
- tool version;
- source evidence identifiers;
- destination or output location;
- read-only default for source evidence;
- scoped execution;
- parameter logging;
- output validation;
- failure logging;
- analyst approval for destructive or evidence-changing actions.

Tool outputs that influence findings should be tied to evidence references and report sections.

## Human Review Requirements

Human review is required before:

- treating LLM output as a forensic finding;
- releasing customer-facing reports;
- making timeline conclusions;
- attributing activity;
- recommending containment based on forensic interpretation;
- modifying, exporting, or transferring evidence;
- using generated scripts against evidence or systems;
- storing persistent memory based on case findings;
- closing a case based on AI-assisted analysis.

The reviewer should be qualified for the case, evidence type, service model, and risk level.

## Output and Reporting Requirements

Reports and outputs should distinguish:

- observed evidence;
- derived artifacts;
- analyst interpretation;
- LLM-assisted summaries;
- hypotheses;
- confirmed findings;
- unresolved questions;
- limitations.

Customer-facing outputs should include only validated findings and should not present model-generated speculation as fact.

## Customer Authorization Requirements

Customer authorization may be required for:

- evidence transfer;
- data export;
- customer-facing report release;
- externally visible notifications;
- production-impacting recommendations;
- cross-environment evidence movement;
- sharing case outputs with third parties;
- actions defined by contract, engagement rules, legal hold, or customer policy.

Internal analyst approval should not replace customer authorization where customer authority is required.

## Security and Isolation Requirements

Private / Local LLM-assisted DFIR environments should consider:

- isolated network segments;
- restricted outbound connectivity;
- controlled package and model updates;
- malware-safe analysis boundaries;
- separation between cases;
- separation between customer workspaces;
- encrypted storage;
- access controls;
- monitored administrative activity;
- secure disposal or archival at case closure.

For air-gapped or disconnected workflows, offline operation must still preserve auditability, version tracking, and chain of custody.

## Minimum Metadata

Where applicable, Private / Local LLM-assisted DFIR events should carry or reference:

- `tenant_id`;
- `customer_id`;
- `case_id`;
- `incident_id`;
- `engagement_id`;
- `workflow_id`;
- `analyst_id`;
- `agent_id`;
- `model_id`;
- `model_version`;
- `prompt_template_id`;
- `evidence_object_ids`;
- `evidence_hashes`;
- `chain_of_custody_reference`;
- `source_system_id`;
- `document_id`;
- `chunk_id`;
- `knowledge_store_id`;
- `memory_store_id`;
- `knowledge_store_or_memory_scope`;
- `knowledge_memory_scope_result`;
- `retrieved_context_ids`;
- `retrieved_context_scope`;
- `tool_id`;
- `tool_version`;
- `parser_or_transformation_version`;
- `requested_action`;
- `policy_decision`;
- `approval_record_id`;
- `customer_authorization_reference`;
- `data_classification`;
- `sensitivity_label`;
- `output_destination`;
- `report_version`;
- `retention_policy_id`;
- `audit_reference_id`;
- `correlation_id`.

## Logging and Audit Requirements

The workflow should log:

- case opening and scope;
- evidence registration;
- evidence access;
- evidence transformation;
- retrieval requests and returned context references;
- memory reads and writes;
- prompts and responses where policy allows;
- model version and configuration;
- tool calls and results;
- analyst validations;
- approvals and customer authorizations;
- report drafts and final versions;
- export, transfer, deletion, archive, or retention actions.

Audit records should support reconstruction of how a finding or report section was produced.

## Failure Modes

This pattern is intended to reduce the following failure modes:

- LLM output is treated as a forensic finding without validation;
- evidence is modified by an AI-assisted tool;
- local model sends data to an external service;
- unrelated cases influence the current case;
- local memory persists beyond retention limits;
- case summaries omit evidence references;
- generated report includes unsupported conclusions;
- chain of custody is not preserved;
- prompt and retrieval context cannot be reconstructed;
- model version or parser version is unknown;
- customer authorization is skipped;
- local execution is assumed to be safe without audit.

## Anti-Patterns

Avoid the following anti-patterns:

- **Local equals safe** — local execution reduces some data movement risk but does not replace governance.
- **LLM as forensic authority** — the model may assist, but validated evidence and analyst judgment determine findings.
- **Evidence-free conclusions** — findings must be tied to evidence references.
- **Unscoped local RAG** — local indexes must not blend customers, cases, or evidence sets.
- **Persistent memory by default** — case memory must be scoped, approved, retained, and deleted according to policy.
- **Prompt-only evidence controls** — prompts cannot replace evidence handling, retrieval enforcement, or chain-of-custody controls.
- **Unlogged offline work** — offline or air-gapped workflows still require logs and reconstruction.
- **Unreviewed report release** — customer-facing outputs require qualified review and authorization where required.
- **Tool execution outside the case boundary** — local tools must remain scoped to approved evidence and case context.
- **Generated scripts against evidence without review** — scripts must be reviewed and controlled before execution.

## Service Model Mapping

| Service Model | Pattern Usage |
|---|---|
| DFIR | Primary pattern for AI-assisted forensic analysis, evidence review, timeline support, report drafting, and evidence-backed findings. |
| SOC / Incident Response | Applies when local or private AI assistance supports incident investigation, evidence interpretation, containment recommendations, or incident reporting. |
| MDR | Applies when managed detection and response workflows include local/private forensic triage, investigation support, or customer-impacting findings. |
| MSSP | Applies when managed security services use private/local DFIR analysis to support customer escalation, reporting, evidence review, or incident support. |

## Implementation Guidance

A practical implementation should start with:

1. **Case workspace standard**
   - required case fields;
   - customer and engagement scope;
   - evidence inventory;
   - authorized analysts;
   - approved tools;
   - approved model runtime;
   - output destinations.

2. **Evidence handling baseline**
   - evidence registration;
   - hashing;
   - provenance;
   - chain-of-custody tracking;
   - read-only originals;
   - derived artifact separation;
   - retention and deletion handling.

3. **Local model controls**
   - approved model list;
   - model version tracking;
   - prompt template governance;
   - network egress restrictions;
   - storage controls;
   - access controls;
   - logging requirements.

4. **Local RAG and memory controls**
   - case-scoped namespaces;
   - approved ingestion sources;
   - retrieval policy;
   - memory write policy;
   - cross-case retrieval tests;
   - retention and deletion process.

5. **Tool governance**
   - approved tool registry;
   - tool versioning;
   - read-only defaults;
   - execution logging;
   - parameter validation;
   - analyst approval for evidence-changing actions.

6. **Review and release process**
   - analyst validation;
   - evidence-reference checks;
   - report quality review;
   - customer authorization where required;
   - final report versioning;
   - audit correlation.

## Acceptance Criteria

A Private / Local LLM-assisted DFIR implementation is acceptable when:

- every workflow is bound to customer, case, incident, engagement, and evidence scope where applicable;
- source evidence is preserved and protected;
- evidence provenance and chain of custody are maintained;
- local model execution does not send evidence to unauthorized external services;
- retrieval and memory are case-scoped and policy-controlled;
- persistent memory is disabled by default or governed by explicit policy;
- forensic tools are controlled, versioned, and logged;
- generated outputs distinguish evidence from interpretation;
- findings are evidence-backed and human-validated;
- customer-facing reports are reviewed before release;
- customer authorization is required where applicable;
- prompts, retrieved context, tool outputs, approvals, and reports are auditable;
- case closure triggers retention, deletion, archive, or transfer handling.

## Non-Goals

This pattern does not:

- claim that private or local LLMs are automatically safe;
- replace trained DFIR analysts;
- replace chain-of-custody requirements;
- replace legal, contractual, or customer requirements;
- require LLM use in every DFIR case;
- define a vendor-specific forensic platform;
- define a specific model, vector database, or runtime;
- permit agents to alter evidence without approval;
- make model-generated conclusions legally or forensically sufficient without validation.

## Related Architecture Views

This pattern complements:

- `governed-agentic-security-operations-pattern.md` — defines the broader governed agentic security operations pattern.
- `policy-enforced-tool-use-pattern.md` — defines policy-enforced tool and API access.
- `human-approved-sensitive-action-pattern.md` — defines approval controls for sensitive actions and outputs.
- `tenant-safe-rag-memory-pattern.md` — defines tenant-safe retrieval and memory controls.
- `control-loop.md` — defines runtime execution governance.
- `layered-architecture.md` — defines the operating layers.
- shared operating boundary visuals — define non-negotiable controls across service models.

## Summary

The Private / Local LLM-assisted DFIR Pattern provides a governed way to use local or private AI assistance in forensic workflows without weakening evidence integrity, chain of custody, case boundaries, analyst accountability, or customer trust.

The pattern supports DFIR first, and also supports SOC / Incident Response, MDR, and MSSP workflows where private or local AI-assisted forensic analysis contributes to investigation, escalation, reporting, or customer-facing outcomes.

The core principle is:

> Private or local LLMs may assist DFIR, but forensic conclusions must remain case-scoped, evidence-backed, human-validated, policy-controlled, and auditable.
