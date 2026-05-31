# Tenant-Safe RAG and Memory Pattern

## Purpose

This pattern defines how retrieval-augmented generation, knowledge retrieval, case memory, shared memory, and agent memory should be governed within the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

It supports **MSSP**, **MDR**, **SOC / Incident Response**, **DFIR**, and **Private / Local LLM-assisted DFIR** where applicable by ensuring that retrieved context and memory do not cross tenant, customer, case, incident, evidence, authorization, retention, or data-sovereignty boundaries.

## Pattern Summary

RAG and memory must not operate as shared, implicit context across customers, cases, or workflows.

The core pattern is:

**Ingest approved data with scope metadata**  
→ **partition and label knowledge / memory stores**  
→ **policy-check retrieval and memory access**  
→ **assemble context only within authorized tenant / customer / case scope**  
→ **validate retrieved context before agent use**  
→ **log retrieval, memory reads, memory writes, and output influence**  
→ **expire, delete, or quarantine stale and unauthorized context**

This pattern makes retrieved context and memory controlled security assets, not uncontrolled prompt material.

## Context

Agentic security operations may use RAG and memory to support:

- alert enrichment;
- investigation assistance;
- case summarization;
- customer reporting;
- prior case lookup;
- detection engineering support;
- threat intelligence lookup;
- asset and identity context;
- evidence review;
- forensic timeline support;
- local or isolated DFIR analysis;
- operational recommendations.

In MSSP and MDR environments, RAG and memory can easily become high-risk if shared infrastructure contains data from multiple customers or tenants. In DFIR and Private / Local LLM-assisted DFIR, retrieved context may include evidence, timelines, forensic artifacts, case notes, legal-sensitive materials, or customer-controlled data.

Without a tenant-safe RAG and memory pattern, agentic systems may retrieve the wrong customer context, reuse stale findings, blend unrelated cases, expose sensitive evidence, or produce outputs based on unauthorized memory.

## Problem

How can agentic security workflows use RAG, knowledge retrieval, and memory without causing cross-tenant contamination, cross-case leakage, stale-context influence, evidence misuse, or unauthorized output generation?

## Forces

This pattern balances the following forces:

- **Context depth vs. boundary enforcement** — agents need rich context, but retrieval must remain tenant, customer, case, and authorization scoped.
- **Shared platforms vs. customer isolation** — MSSP and MDR platforms may centralize indexes and stores, but customers must not bleed into each other.
- **Memory usefulness vs. retention risk** — memory can improve continuity, but persistent memory creates privacy, retention, and stale-context risks.
- **Forensic assistance vs. evidence integrity** — DFIR retrieval may help analysis, but findings must remain evidence-backed and chain-of-custody aware.
- **Automation speed vs. source validation** — retrieved context accelerates work, but source, freshness, classification, and authorization must be verified.
- **Continuous learning vs. uncontrolled memory writes** — agents may generate useful summaries, but memory updates must be governed and auditable.

## Applicability

Use this pattern when agentic workflows rely on:

- vector search;
- RAG pipelines;
- semantic search;
- knowledge stores;
- shared memory;
- case memory;
- customer memory;
- agent memory;
- investigation memory;
- prior summaries;
- retrieval over evidence;
- local DFIR knowledge stores;
- prompt context assembled from stored or retrieved content.

This pattern applies to:

- **MSSP** — customer-scoped retrieval, service history, alert enrichment, reporting context, and managed-service knowledge.
- **MDR** — investigation retrieval, detection context, prior incident context, response recommendations, and escalation support.
- **SOC / Incident Response** — incident context retrieval, playbook lookup, asset context, identity context, and operational coordination support.
- **DFIR** — evidence-aware retrieval, artifact summaries, timeline context, report support, and case-specific forensic memory.
- **Private / Local LLM-assisted DFIR** — local or isolated retrieval and memory used for forensic analysis, artifact review, summarization, or report preparation.

Do not force this pattern onto workflows that do not use RAG, retrieval, knowledge stores, or memory. Manual DFIR workflows still require evidence integrity, chain of custody, human review, and auditability, but may not require RAG or memory controls.

## Solution

Implement tenant-safe RAG and memory as a governed context-access pattern with six required elements:

1. **Scoped Ingestion**  
   Every indexed document, chunk, embedding, evidence object, summary, memory item, and knowledge record must be tagged with tenant, customer, case, source, classification, sensitivity, retention, and authorization metadata where applicable.

2. **Partitioned Knowledge and Memory Stores**  
   Knowledge stores and memory stores must be separated by tenant, customer, case, environment, or policy-enforced namespace. Shared indexes may be used only when policy-enforced metadata filtering, isolation, and auditability are strong enough for the risk.

3. **Policy-Gated Retrieval**  
   Retrieval requests must pass through policy and enforcement controls before context is returned to an agent or workflow.

4. **Context Validation Before Use**  
   Retrieved context must be checked for scope, source, freshness, classification, sensitivity, evidence relevance, and authorization before it is included in the prompt or used to support an output.

5. **Controlled Memory Writes**  
   Agents must not write persistent memory by default. Memory writes must be policy-approved, scoped, labeled, auditable, and subject to retention and deletion requirements.

6. **Audit, Replay, and Continuous Assurance**  
   Retrievals, memory reads, memory writes, prompt assembly, evidence references, and output influence must be logged so the workflow can be reviewed or reconstructed.

## Architecture Roles

### Ingestion Pipeline

The ingestion pipeline prepares data for retrieval or memory.

It should:

- validate source authorization;
- preserve source metadata;
- classify and label data;
- tag tenant, customer, case, incident, and evidence scope;
- record parser, transformation, and summarization versions;
- prevent ingestion of unauthorized or unclassified data;
- enforce retention and deletion rules;
- quarantine ambiguous or unscoped content.

### Knowledge Store

The knowledge store contains approved retrievable content.

It may include:

- documentation;
- playbooks;
- alerts;
- incidents;
- case notes;
- asset context;
- identity context;
- threat intelligence;
- evidence metadata;
- forensic artifacts;
- customer-approved reference material.

The knowledge store must not be treated as globally safe simply because content was indexed.

### Memory Store

The memory store contains prior context that may influence future agent behavior.

Memory may be:

- session memory;
- workflow memory;
- case memory;
- customer memory;
- tenant memory;
- agent memory;
- ephemeral memory;
- persistent memory.

Persistent memory should be used only when there is a defined purpose, scope, owner, retention rule, and audit trail.

### Retrieval Policy Decision Point

The PDP evaluates whether retrieval or memory access is allowed.

It should consider:

- requester identity;
- agent identity;
- tenant and customer scope;
- case or incident scope;
- evidence scope;
- data classification;
- sensitivity label;
- knowledge or memory namespace;
- retrieval purpose;
- output destination;
- authorization;
- retention status;
- freshness and expiration;
- policy exceptions.

### Retrieval Policy Enforcement Point

The PEP enforces retrieval and memory decisions.

It should:

- deny by default;
- fail closed when policy cannot be evaluated;
- block retrieval without required scope;
- enforce metadata filters;
- prevent direct agent access to unrestricted indexes;
- restrict memory reads and writes;
- redact or exclude unauthorized context;
- log retrieval attempts and results;
- prevent prompt assembly with unauthorized content.

### Agentic Workflow

The agentic workflow may use retrieved context to reason, summarize, classify, recommend, draft, or prepare a proposed action.

The workflow must not treat retrieved content as automatically authoritative. It must preserve source attribution, evidence references, and policy scope.

### Assurance and Audit Layer

The assurance layer validates retrieval and memory behavior.

It should monitor:

- cross-tenant retrieval attempts;
- cross-case retrieval attempts;
- stale or expired context;
- unauthorized memory writes;
- missing metadata;
- prompt context assembly;
- output claims unsupported by retrieved evidence;
- retrieval drift or over-broad results;
- policy bypass attempts.

## Reference Flow

A tenant-safe RAG and memory flow should operate as follows:

1. Data is ingested only from authorized sources.
2. Content is classified, labeled, chunked, embedded, and tagged with required metadata.
3. Knowledge and memory records are stored in partitioned or policy-enforced namespaces.
4. An agentic workflow requests context for a specific mission, tenant, customer, case, and purpose.
5. The retrieval request is normalized into a retrieval contract.
6. The PDP evaluates whether the requested retrieval or memory access is allowed.
7. The PEP enforces the decision and applies required metadata filters.
8. Retrieved results are validated for scope, source, freshness, classification, sensitivity, evidence relevance, and authorization.
9. Only approved context is assembled into the agent prompt or workflow state.
10. The agent produces a recommendation, summary, action proposal, or output.
11. The output is validated against retrieved sources and evidence references where applicable.
12. Retrievals, memory reads, memory writes, prompt context, and output references are logged.
13. Stale, expired, unauthorized, or mis-scoped content is removed, quarantined, or denied.
14. Assurance findings feed governed improvements to ingestion, retrieval, memory, policies, tests, and evaluation procedures.

## Decision Outcomes

The pattern requires explicit retrieval and memory decision outcomes:

- **Allow** — return context within approved scope.
- **Deny** — block retrieval or memory access and fail closed.
- **Restrict** — return only reduced, filtered, redacted, or read-only context.
- **Require Human Approval** — pause when retrieval or memory use involves sensitive evidence, customer authorization, privileged context, or policy exception.
- **Return for Clarification** — request more context when tenant, customer, case, purpose, authority, or output destination is unclear.
- **Quarantine** — isolate unclassified, mis-scoped, stale, expired, or potentially contaminated content.
- **Expire / Delete** — remove memory or indexed content based on retention, case closure, customer request, or policy.

## RAG and Memory Scope Types

### Public or General Reference Context

Examples:

- general product documentation;
- approved public threat intelligence;
- public standards;
- approved operating procedures.

Controls:

- source validation;
- version tracking;
- freshness checks;
- no customer data mixing.

### Tenant or Customer Context

Examples:

- customer environment details;
- customer-specific detections;
- service history;
- reporting context;
- customer-approved knowledge.

Controls:

- tenant and customer partitioning;
- authorization checks;
- data classification;
- output destination controls;
- audit logging.

### Case or Incident Context

Examples:

- incident notes;
- investigation findings;
- alerts;
- timelines;
- related assets;
- response decisions.

Controls:

- case and incident scope enforcement;
- evidence references where applicable;
- stale-context validation;
- restricted memory reuse after case closure.

### Evidence Context

Examples:

- forensic artifacts;
- disk or memory analysis outputs;
- logs;
- extracted indicators;
- chain-of-custody metadata;
- timeline records.

Controls:

- evidence object identifiers;
- provenance and chain of custody;
- read-only handling where required;
- source attribution;
- human validation for conclusions.

### Persistent Memory

Examples:

- customer preferences;
- recurring service context;
- case history summaries;
- approved analyst notes;
- long-lived operational knowledge.

Controls:

- explicit purpose;
- owner;
- retention policy;
- deletion path;
- access boundary;
- review and audit.

## Control Requirements

### Ingestion Controls

- ingest only from authorized sources;
- preserve source identifiers;
- record parser and transformation versions;
- classify and label data;
- tag tenant, customer, case, incident, and evidence scope;
- reject or quarantine missing-scope content;
- track embedding model and version;
- enforce retention and deletion rules.

### Retrieval Controls

- require policy evaluation before context is returned;
- enforce tenant, customer, case, incident, and evidence filters;
- deny retrieval when scope is missing or ambiguous;
- validate freshness and expiration;
- prevent cross-tenant, cross-customer, or cross-case results;
- restrict results by classification and sensitivity;
- log retrieval query and returned context references.

### Memory Read Controls

- restrict memory reads by tenant, customer, case, workflow, purpose, and authorization;
- distinguish session memory from persistent memory;
- prevent unrelated cases from influencing current decisions;
- detect stale, expired, or low-trust memory;
- log memory reads and influence on output.

### Memory Write Controls

- deny persistent memory writes by default;
- require policy approval for long-lived memory;
- require owner, scope, purpose, retention, and sensitivity label;
- prevent agents from writing unsupported conclusions as memory;
- separate evidence-backed facts from generated interpretation;
- support deletion, correction, and expiration.

### Prompt Assembly Controls

- assemble only approved context;
- preserve source references;
- exclude unauthorized or stale content;
- label context by type and trust level;
- separate evidence, prior findings, reference material, and model-generated summaries;
- log prompt context references without exposing sensitive content unnecessarily.

### Output Controls

- validate outputs against retrieved sources;
- require evidence-backed claims for DFIR findings;
- prevent unsupported conclusions;
- control customer-facing output destinations;
- require human review for sensitive or externally visible outputs;
- log source references used in final outputs.

## DFIR and Private / Local LLM-assisted DFIR Requirements

For DFIR and Private / Local LLM-assisted DFIR, RAG and memory must preserve forensic integrity.

Required controls include:

- case-specific retrieval boundaries;
- evidence object identifiers;
- evidence provenance;
- chain-of-custody preservation;
- read-only evidence handling where required;
- separation of extracted facts from model-generated interpretation;
- human review of forensic conclusions;
- audit of prompts, retrieved context, memory reads, memory writes, and outputs;
- retention and deletion aligned to case, customer, legal, and engagement requirements.

Private or local execution does not automatically make retrieval or memory safe. Local indexes, local vector stores, local embeddings, local summaries, and local memory still require scope, retention, deletion, audit, and evidence controls.

## Retrieval, Memory, and Tool Use

RAG and memory often influence tool use. When retrieved context or memory is used to propose a tool action, the tool request should include the retrieval and memory scope used to support the recommendation.

Tool execution should fail closed when:

- retrieved context is unauthorized;
- memory scope is missing;
- context crosses tenant, customer, or case boundaries;
- context is stale or expired;
- evidence references are missing for evidence-sensitive actions;
- the retrieved context does not support the proposed action.

## Human Oversight Triggers

Human review should be required when retrieval or memory use involves:

- evidence-sensitive conclusions;
- customer-facing reports;
- persistent memory writes;
- cross-case context reuse;
- policy exceptions;
- low-confidence or conflicting retrieved context;
- stale or expired context used in a recommendation;
- customer authorization requirements;
- legal, contractual, or data-sovereignty concerns;
- private/local DFIR findings intended for release.

## Failure Modes

This pattern is intended to reduce the following failure modes:

- retrieval returns another customer’s data;
- agent memory blends unrelated cases;
- stale case summaries influence a current decision;
- evidence context is used without provenance;
- generated interpretation is stored as fact;
- memory persists beyond retention requirements;
- deleted customer data remains in embeddings or summaries;
- prompt context contains unauthorized content;
- agent recommends a tool action based on mis-scoped retrieval;
- output includes unsupported forensic conclusions;
- local DFIR indexes are treated as safe without audit;
- retrieval logs cannot reconstruct what influenced an output.

## Anti-Patterns

Avoid the following anti-patterns:

- **Global shared vector index without enforceable scope** — metadata labels alone are not enough if enforcement is weak.
- **Memory as implicit truth** — memory must be scoped, validated, and auditable.
- **Agent-controlled persistent memory** — agents should not write long-lived memory without policy control.
- **Unscoped retrieval** — retrieval must not cross tenant, customer, case, incident, evidence, or authorization boundaries.
- **Evidence-free forensic memory** — DFIR memory must be tied to evidence references where it supports findings.
- **Prompt-only data isolation** — prompts cannot replace retrieval enforcement.
- **Stale context reuse** — old findings or summaries must not influence new decisions without freshness checks.
- **Unlogged local RAG** — private or local systems still need auditability.
- **Embedding retention blind spot** — deletion and retention must consider chunks, embeddings, summaries, and memory records.
- **Cross-case learning by default** — prior case knowledge must not influence a new case unless explicitly authorized and scoped.

## Service Model Mapping

| Service Model | Pattern Usage |
|---|---|
| MSSP | Governs customer-scoped retrieval, service history, reporting context, customer knowledge, and multi-tenant knowledge separation. |
| MDR | Governs investigation context, detection knowledge, prior incident context, response recommendations, and memory-influenced triage. |
| SOC / Incident Response | Governs incident context retrieval, playbook lookup, asset and identity context, coordination notes, and incident memory. |
| DFIR | Governs evidence-aware retrieval, timeline context, artifact summaries, forensic notes, evidence-backed report support, and case memory. |
| Private / Local LLM-assisted DFIR | Applies when local indexes, local memory, local embeddings, or isolated RAG are used for forensic analysis, summarization, artifact review, or report preparation. |

## Implementation Guidance

A practical implementation should start with:

1. **Scope model**
   - tenant;
   - customer;
   - case;
   - incident;
   - evidence object;
   - workflow;
   - agent;
   - source system;
   - output destination.

2. **Knowledge and memory registry**
   - store name;
   - store owner;
   - store purpose;
   - namespace;
   - allowed tenants/customers;
   - data classification;
   - sensitivity label;
   - retention policy;
   - deletion process;
   - embedding model and version;
   - parser and transformation version.

3. **Retrieval contract**
   - requester identity;
   - agent identity;
   - query purpose;
   - tenant/customer/case scope;
   - knowledge or memory store requested;
   - allowed namespaces;
   - evidence scope;
   - output destination;
   - policy decision;
   - correlation identifiers.

4. **Memory write policy**
   - allowed memory types;
   - required owner;
   - required scope;
   - approval requirements;
   - retention;
   - deletion;
   - correction;
   - audit fields.

5. **Validation and testing**
   - cross-tenant retrieval tests;
   - cross-case retrieval tests;
   - stale-context tests;
   - missing-metadata tests;
   - unauthorized memory-write tests;
   - deleted-content retrieval tests;
   - output-source-support tests.

## Minimum Metadata

Where applicable, RAG and memory events should carry or reference:

- `tenant_id`;
- `customer_id`;
- `case_id`;
- `incident_id`;
- `workflow_id`;
- `agent_id`;
- `user_id` or service identity;
- `source_system_id`;
- `document_id`;
- `chunk_id`;
- `evidence_object_ids`;
- `knowledge_store_id`;
- `memory_store_id`;
- `knowledge_store_or_memory_scope`;
- `knowledge_memory_scope_result`;
- `retrieval_query_id`;
- `retrieved_context_ids`;
- `retrieved_context_scope`;
- `index_id`;
- `vector_namespace`;
- `embedding_model_id`;
- `embedding_version`;
- `parser_or_transformation_version`;
- `data_classification`;
- `sensitivity_label`;
- `retention_policy_id`;
- `expiration_timestamp`;
- `policy_decision`;
- `approval_record_id`;
- `output_destination`;
- `audit_reference_id`;
- `correlation_id`.

## Acceptance Criteria

A tenant-safe RAG and memory implementation is acceptable when:

- all indexed content has tenant, customer, case, source, classification, and retention metadata where applicable;
- retrieval is denied by default without valid scope;
- agents cannot directly query unrestricted knowledge or memory stores;
- policy is evaluated before retrieval or memory access;
- metadata filters are enforced by the retrieval PEP;
- cross-tenant, cross-customer, cross-case, and unauthorized retrieval tests fail closed;
- memory reads and writes are scoped, logged, and policy-controlled;
- persistent memory requires purpose, owner, retention, and deletion handling;
- evidence-sensitive retrieval preserves provenance and chain of custody;
- output claims can be traced to approved context and evidence references;
- stale, expired, or deleted context is not returned;
- all retrieval and memory influence can be reconstructed through audit logs.

## Non-Goals

This pattern does not:

- require every workflow to use RAG or memory;
- define a vendor-specific vector database or retrieval platform;
- make vector search inherently tenant-safe;
- replace policy enforcement with metadata tagging alone;
- make local or private LLM execution automatically safe;
- remove the need for human review of forensic conclusions;
- replace evidence handling, chain-of-custody, or legal requirements;
- allow agents to create uncontrolled persistent memory.

## Related Architecture Views

This pattern complements:

- `governed-agentic-security-operations-pattern.md` — defines the broader governed agentic security operations pattern.
- `policy-enforced-tool-use-pattern.md` — defines policy-enforced tool and API access.
- `human-approved-sensitive-action-pattern.md` — defines approval controls for sensitive actions and outputs.
- `control-loop.md` — defines runtime execution governance.
- `layered-architecture.md` — defines the operating layers.
- shared operating boundary visuals — define non-negotiable controls across service models.

## Summary

The Tenant-Safe RAG and Memory Pattern ensures that agentic systems retrieve and remember only what they are authorized to use within the correct tenant, customer, case, incident, evidence, and workflow scope.

The pattern supports MSSP, MDR, SOC / Incident Response, DFIR, and Private / Local LLM-assisted DFIR where applicable by requiring scoped ingestion, partitioned or policy-enforced knowledge stores, governed retrieval, controlled memory writes, evidence-aware validation, retention handling, auditability, and continuous assurance.

The core principle is:

> Agents may use retrieved context and memory, but retrieval and memory must remain scoped, policy-gated, evidence-aware, auditable, and prevented from crossing tenant, customer, case, or authorization boundaries.
