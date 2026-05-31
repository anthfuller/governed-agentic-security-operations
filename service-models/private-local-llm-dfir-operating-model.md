# Private / Local LLM-Assisted DFIR Operating Model

## Purpose

This file defines the **Private / Local LLM-assisted DFIR operating model** for the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The operating model describes how local, isolated, customer-controlled, or air-gapped LLM workflows can assist Digital Forensics and Incident Response without weakening evidence integrity, case scope, chain of custody, analyst accountability, customer authorization, or auditability.

This file is an operating model, not a vendor-specific engineering design.

## Service Scope

The Private / Local LLM-assisted DFIR service model supports evidence-aware forensic workflows where AI assistance is used inside a controlled DFIR environment.

| Area | In Scope |
|---|---|
| Evidence review support | Local analysis of approved evidence, derived artifacts, logs, timelines, memory captures, disk artifacts, endpoint telemetry, cloud audit exports, and analyst notes. |
| Timeline support | Drafting, organizing, normalizing, and reviewing timeline events with explicit evidence references. |
| Artifact parsing support | Assisting with interpretation of parsed artifacts while preserving original evidence and parser provenance. |
| Report drafting support | Drafting internal report sections, questions, summaries, and analyst notes before human validation. |
| Local RAG support | Case-scoped retrieval over approved evidence, derived artifacts, case notes, and approved reference material. |
| Analyst review workflow | Recording accepted entries, rejected inferences, required corrections, and final review status. |
| Evidence-aware audit | Preserving traceability across evidence, parser output, prompt context, local model output, analyst review, and final workflow state. |

## Out of Scope

| Area | Out-of-Scope Boundary |
|---|---|
| Model as forensic authority | LLM output must not be treated as a final forensic finding without analyst validation. |
| Evidence modification | Agents, models, scripts, and tools must not modify original evidence unless explicitly approved through a controlled evidence-handling workflow. |
| Unscoped retrieval | Local RAG must not retrieve unrelated customers, tenants, cases, incidents, or evidence sets. |
| Uncontrolled memory | Persistent memory writes are denied by default unless purpose, owner, retention, approval, and audit are present. |
| Customer-facing release | Local LLM output must not be released externally without review, approval, and customer authorization where required. |
| Evidence export | Evidence, artifacts, derived outputs, or prompts containing evidence must not leave the approved environment without authorization. |
| Autonomous response | Local DFIR agents must not trigger containment, remediation, notification, or environment changes unless routed through approved response models. |

## Operating Principles

| Principle | Required Behavior |
|---|---|
| Case-scoped execution | Every workflow must be bound to tenant, customer, case, incident or engagement, workflow, evidence, and analyst scope. |
| Evidence first | Findings must trace to evidence objects, derived artifacts, parser outputs, or analyst-validated observations. |
| Original evidence protection | Original evidence must remain preserved and read-only where required. |
| Local does not equal trusted | Local or private model execution reduces data movement risk, but does not replace policy, review, audit, or evidence controls. |
| Analyst accountability | Human analysts remain accountable for findings, interpretations, and report release. |
| Retrieval containment | RAG, indexes, embeddings, chunks, summaries, and memory must remain case-scoped. |
| No uncontrolled memory | Persistent memory writes are denied by default. |
| No unsupported conclusions | Model-generated interpretation must be labeled and reviewed before use. |
| Audit and replay | Evidence use, context retrieval, prompts, outputs, reviews, and release decisions must be reconstructable. |
| Fail closed | Missing case scope, evidence scope, chain-of-custody reference, policy, approval, or review must block release or route for clarification. |

## Workflow Classes

| Workflow Class | Agentic / LLM Assistance Allowed | Approval or Review Required? | Notes |
|---|---|---|---|
| Evidence manifest preparation | Limited assistance | Human review required | Evidence metadata and chain-of-custody references must be validated. |
| Artifact summarization | Yes | Analyst review before use in findings | Summary must reference evidence objects and parser versions. |
| Timeline drafting | Yes | Analyst review required | Timeline remains draft until reviewed. |
| Timeline correction | Yes | Human analyst controls final correction | Model may suggest corrections but cannot finalize. |
| Forensic hypothesis generation | Yes | Analyst validation required | Hypotheses must remain clearly labeled. |
| Report section drafting | Yes | Review and release approval required | Customer-facing release requires separate approval. |
| Evidence export preparation | Limited assistance | Customer authorization and evidence handling approval required | Export must use approved evidence path. |
| Tool-assisted parsing | Yes, if governed | Tool owner and evidence controls required | Original evidence must not be modified. |
| Persistent case memory | Usually no | Requires policy, owner, retention, and approval | Deny by default. |

## Roles and Responsibilities

| Role | Responsibility | Must Not Do |
|---|---|---|
| DFIR Analyst | Validate evidence, review LLM-assisted outputs, approve internal timeline use, and document accepted or rejected interpretations. | Treat model output as final finding without evidence validation. |
| DFIR Lead | Own case direction, review quality, report readiness, evidence handling decisions, and escalation. | Release customer-facing findings without review and authorization. |
| Evidence Custodian | Preserve evidence inventory, custody records, hashes, transfers, and retention state. | Allow untracked evidence movement or modification. |
| Local LLM Runtime | Assist with summarization, timeline drafting, artifact explanation, and hypothesis generation inside approved environment. | Access external services, train on customer data, write persistent memory, or make final findings. |
| Agent Orchestrator | Route local model tasks through case policy, retrieval controls, tool wrappers, and audit logging. | Bypass case scope, use external model endpoints, or inject unapproved context. |
| Prompt Governance Owner | Own approved prompt templates, validate template changes, require DFIR / assurance sign-off, and maintain prompt version history. | Allow unreviewed prompt changes, uncontrolled prompt drift, or prompt updates without audit linkage. |
| PDP | Decide whether retrieval, memory, tool use, output release, evidence movement, or report use is allowed, denied, restricted, approval-required, or clarification-required. | Enforce directly without a PEP. |
| PEP | Enforce decisions at retrieval, memory, tool, evidence store, model runtime, and output publishing boundaries. | Permit use when case, evidence, policy, approval, or review is missing. |
| Customer Approver | Authorize evidence transfer, report release, customer-facing communication, or other customer-controlled actions where required. | Be bypassed by internal approval. |
| Audit / Assurance | Preserve traceability, evaluate evidence linkage, and support replay. | Depend only on unstructured notes without structured identifiers. |

## Agentic Assistance Boundaries

| Agent / Local LLM May | Agent / Local LLM Must Not |
|---|---|
| Summarize approved evidence and derived artifacts. | Modify original evidence. |
| Draft timeline entries with evidence references. | Present draft entries as final forensic findings. |
| Identify gaps, uncertainty, and follow-up questions. | Convert hypotheses into confirmed conclusions. |
| Suggest analyst review focus. | Replace analyst judgment. |
| Draft internal report text. | Release customer-facing reports. |
| Use case-scoped local RAG. | Retrieve unrelated case, customer, tenant, or evidence context. |
| Propose tool-assisted parsing steps. | Execute destructive or evidence-changing tools without approval. |

## Policy and Enforcement Points

Service owners must map the PDP / PEP boundaries defined in this operating model to specific infrastructure components in their deployment guide, such as local model runtime controls, retrieval gateways, vector stores, evidence stores, forensic tool wrappers, workflow orchestrators, approval systems, report publishing controls, and audit pipelines.

| Boundary | PDP Decision Required When | PEP Enforcement Location |
|---|---|---|
| Evidence access | Evidence, derived artifacts, case notes, or chain-of-custody data are accessed. | Evidence store or case workspace PEP. |
| Local RAG retrieval | Evidence, chunks, embeddings, summaries, or case memory are retrieved. | Local retrieval gateway or vector store PEP. |
| Memory write | Workflow attempts to write persistent case, customer, or agent memory. | Memory PEP or knowledge-store gateway. |
| Local model execution | Prompt context includes customer evidence or derived artifacts. | Local model runtime gateway. |
| Forensic tool use | Parser, script, notebook, artifact extractor, or timeline tool is invoked. | Forensic tool wrapper or workflow orchestrator. |
| Evidence export / transfer | Evidence, derived artifacts, prompts, reports, logs, or indexes leave the workspace. | Evidence movement PEP. |
| Report / output release | Timeline, finding, report, summary, or conclusion may be released externally. | Output publishing layer. |
| Case closure | Workflow proposes closure based on LLM-assisted analysis. | Case management workflow PEP. |

## Forensic Impact Analysis

A Forensic Impact Analysis must be completed before local LLM-assisted DFIR workflow execution when evidence, timeline construction, report drafting, or tool-assisted artifact processing is in scope.

| If Workflow Involves | Forensic Impact Analysis Must Identify |
|---|---|
| Evidence ingestion | Evidence type, source system, collection method, hash status, chain-of-custody reference, and authorized use. |
| Timeline construction | Evidence objects used, derived artifacts, timestamp normalization, timezone assumptions, and unresolved gaps. |
| Artifact parsing or transformation | Parser/tool version, source evidence, derived output location, before/after state where applicable, and risk of evidence alteration. |
| Local RAG or vector indexing | Namespace, evidence scope, embedding model/version, retention path, deletion path, and cross-case retrieval risk. |
| Model-generated interpretation | Whether output is observation, derived fact, hypothesis, analyst note, or unsupported inference. |
| Report drafting | Intended audience, output destination, review requirement, customer authorization requirement, and unsupported-claim risk. |
| Evidence export or transfer | Destination, customer authorization, legal/contractual constraints, custody impact, and audit reference. |

The workflow must fail closed or return for clarification if the Forensic Impact Analysis cannot identify case scope, evidence scope, custody status, output destination, or review requirement.

## Human Review Gates

| If This Occurs | Then Require |
|---|---|
| Timeline output is generated by local LLM. | Analyst review before use in findings or reports. |
| Model output contains forensic interpretation. | Analyst validation and evidence reference check. |
| Timeline entry lacks evidence reference. | Reject entry or return for correction. |
| Model suggests causality, attribution, exfiltration, or compromise conclusion. | DFIR lead review before use. |
| Report text is customer-facing. | Report review and customer authorization where required. |
| Evidence export or transfer is requested. | Evidence custodian approval and customer authorization where required. |
| Tool may alter source evidence. | Evidence-handling approval and before/after state audit. |
| Persistent memory write is requested. | Policy approval, owner, retention, and review required. |
| Case closure is proposed. | Human-controlled closure decision with audit-linked rationale. |

## Customer Authorization Gates

| Customer Authorization Required When | Enforcement Requirement |
|---|---|
| Evidence leaves approved customer-controlled or local environment. | Evidence movement PEP must verify authorization reference. |
| Customer-facing report is released. | Output PEP must block release without review and authorization where required. |
| Third-party sharing is requested. | Evidence/data transfer workflow must verify authorization and legal scope. |
| Case data is retained beyond standard retention. | Retention policy must reflect customer or legal authorization. |
| Local analysis environment changes trust boundary. | Workflow must verify customer-approved processing boundary. |
| Production response action is recommended from DFIR findings. | Response workflow must route through customer authorization and service model approval. |

## Evidence Boundary Enforcement

| Evidence Boundary | Required Control |
|---|---|
| Tenant | Requests must carry `tenant_id`; missing or mismatched tenant fails closed. |
| Customer | Requests must carry `customer_id`; cross-customer retrieval is denied and audited. |
| Case / Incident / Engagement | Workflows must carry case, incident, or engagement identifier before evidence is accessed. |
| Evidence Object | Timeline entries and findings must reference evidence object identifiers. |
| Original Evidence | Original evidence remains read-only where required. |
| Derived Artifact | Derived artifacts must reference source evidence and parser/transformation version. |
| Chain of Custody | Required when evidence is used for formal DFIR, legal-sensitive review, or customer-facing findings. |
| Output Destination | Destination must be declared before timeline, report, export, or transfer. |
| Classification | Data classification and sensitivity label must persist through the workflow. |

## Evidence Format Requirements

Private / Local LLM-assisted DFIR workflows must preserve and validate evidence format handling before AI-assisted analysis uses evidence or derived artifacts.

| Evidence Format / Artifact Type | Required Control |
|---|---|
| E01 / Ex01 forensic image | Validate image metadata, hash, segment integrity, mount/read-only handling, and tool compatibility before derived analysis. |
| AFF4 image | Validate container metadata, stream integrity, hash references, and parser/tool version. |
| RAW / DD image | Validate size, hash, source device metadata, and read-only working-copy handling. |
| Memory image | Validate source host, acquisition tool, hash, timestamp, and malware-safe handling path. |
| EVTX / Windows logs | Preserve source host, channel, time range, parser version, and timestamp normalization. |
| Cloud audit export | Preserve source cloud account/subscription/project, query or export method, time range, and output hash where applicable. |
| EDR / XDR export | Preserve source system, export filter, alert/event identifiers, and transformation version. |
| PCAP / network capture | Preserve capture interface/source, time range, hash, and parser version. |
| Derived artifact | Reference original evidence object, parser/transformation version, output path, hash, and creation timestamp. |

Agents and local LLM workflows may assist with format-aware summarization, but they must not treat unsupported, unvalidated, or partially parsed evidence formats as reliable sources for findings.

## Local RAG and Memory Rules

| If | Then |
|---|---|
| Local RAG is used. | Restrict retrieval to case-scoped evidence, derived artifacts, and approved reference material. |
| Vector index is created. | Record namespace, embedding model, embedding version, source documents, retention policy, and deletion path. |
| Chunk or embedding is created from evidence. | Preserve source evidence object identifier and transformation version. |
| Retrieved context influences timeline output. | Log retrieved context identifiers and scope result. |
| Memory read is requested. | Validate case, customer, workflow, and freshness before prompt assembly. |
| Persistent memory write is requested. | Deny by default unless policy, owner, purpose, retention, and approval exist. |
| Cross-case context is returned. | Deny, quarantine, and audit. |
| Stale context influences output. | Mark stale, route for analyst review, or return for clarification. |
| Case closes. | Delete, archive, or transfer local indexes and memory according to retention policy. |

## Forensic Tool Use Rules

| If Tool Is Used For | Then Require |
|---|---|
| Parsing logs or artifacts | Record parser name, parser version, source evidence, output path, and hash where applicable. |
| Timeline generation | Record source artifacts, transformation version, timestamp normalization, and timezone handling. |
| Scripted analysis | Review script or notebook before use if it can alter evidence or produce reportable findings. |
| Evidence transformation | Preserve original evidence and store derived artifact separately. |
| Malware or suspicious artifact handling | Use malware-safe environment and record tool version and handling path. |
| Evidence-changing operation | Require approval, before-state reference, after-state reference, and audit event. |
| External tool dependency | Verify tool is approved for the isolated environment and does not create unauthorized egress. |

## Timeline and Finding Controls

| If Timeline Output Includes | Then Require |
|---|---|
| Observed event | Evidence object reference and source timestamp. |
| Derived fact | Source artifact and parser/transformation reference. |
| Model interpretation | Label as interpretation or hypothesis. |
| Causal relationship | Analyst validation and evidence support. |
| Attribution statement | DFIR lead approval and strong evidence support. |
| Exfiltration claim | Evidence support for access, volume, transfer, and destination where applicable. |
| Missing evidence or uncertainty | Explicit unresolved-question entry. |
| Customer-facing conclusion | Report review and customer authorization where required. |

## Sensitive DFIR Action Handling

Private / Local LLM-assisted DFIR workflows may recommend evidence-sensitive or release-sensitive actions, but they must not execute them without approval and enforcement.

An **authorized forensic action path** means the action is executed only through a documented, approved, and replayable workflow. For enterprise use, the action path should be represented as an **idempotent workflow** or **signed playbook** that defines the allowed evidence action, case scope, required approvals, customer authorization requirements, PEP enforcement point, before/after state reference where applicable, and audit fields.

| Sensitive DFIR Action | Local LLM Output Allowed | Execution Allowed? |
|---|---:|---:|
| Evidence export | Recommendation only | Only after evidence custodian approval and customer authorization where required. |
| Evidence transformation | Recommendation and tool plan | Only through approved tool path with provenance and derived artifact record. |
| Source evidence modification | Not allowed by default | Only through explicit evidence-handling exception and audit. |
| Timeline release | Draft only | Only after analyst review and release approval. |
| Customer-facing report | Draft only | Only after report review and customer authorization where required. |
| Persistent case memory write | Recommendation only | Only after policy approval, owner, retention, and deletion path. |
| Case closure | Draft recommendation only | Human-controlled decision with audit-linked rationale. |
| Final forensic conclusion | Draft support only | Analyst/DFIR lead validated conclusion required. |

## Local Model Runtime Controls

| Control Area | Required Behavior |
|---|---|
| Model selection | Use only approved local/private model profile. |
| Model version | Record model identifier and version in output and audit artifacts. |
| Prompt template | Use governed prompt templates for timeline, summary, and report tasks. |
| Network egress | Deny unauthorized outbound access. |
| Training | Do not train on customer evidence unless separately authorized. |
| Prompt logging | Log full prompt where allowed; otherwise preserve redacted prompt, metadata, and source references. |
| Output logging | Preserve output identifier, source references, review status, and release status. |
| Runtime update | Model/runtime/prompt updates require governed change control. |

## Prompt Template Governance

Governed prompt templates are controlled DFIR workflow artifacts.

| Prompt Template Activity | Required Control |
|---|---|
| New prompt template is created. | Prompt Governance Owner, DFIR Lead, and assurance reviewer must approve intended use, allowed evidence scope, output type, and review requirement. |
| Existing template is modified. | Change must include version update, rationale, reviewer sign-off, test evidence, and rollback path. |
| Template is used for evidence analysis. | Template identifier and version must be recorded in timeline, report, review, and audit artifacts. |
| Template changes output classification or release behavior. | PDP policy and output PEP must be reviewed before use. |
| Template includes tool instructions. | Tool owner and evidence custodian must validate that instructions cannot alter source evidence without approval. |
| Template is retired. | Retirement must preserve version history and prevent use in new workflows. |
| Template fails validation. | Block use and route to prompt governance review. |

Prompt changes must not be made by the local LLM, agent, or analyst ad hoc inside an active evidence workflow unless routed through the approved prompt governance process.

## Report and Release Controls

| If Output Is | Then Require |
|---|---|
| Internal working note | Case scope, analyst review status, and audit reference. |
| Internal timeline | Evidence references and analyst review. |
| Draft report section | Evidence-backed claims and review status. |
| Customer-facing report | Release approval and customer authorization where required. |
| Executive summary | Review for unsupported claims and sensitive data exposure. |
| Legal-sensitive output | Legal or authorized review path where required. |
| Final forensic finding | Evidence support, analyst validation, DFIR lead approval, and audit linkage. |

## Escalation Paths

| Condition | Escalate To | Reason |
|---|---|---|
| Evidence scope is unclear | Evidence custodian / DFIR lead | Evidence handling authority required. |
| Chain of custody is missing or incomplete | Evidence custodian | Custody gap must be resolved before findings. |
| Local model output suggests unsupported conclusion | DFIR lead | Finding must be validated or rejected. |
| Evidence export is requested | Customer approver / evidence custodian | Authorization and transfer control required. |
| Malware handling is required | Malware analysis specialist | Specialized controlled environment required. |
| Production response action is required | MDR / Cloud IR / SOC Incident Lead | Response action belongs in response operating model. |
| Customer-facing report is requested | Report reviewer / customer approver | Release approval required. |
| Local environment boundary changes | Security owner / customer approver | Trust boundary and authorization must be revalidated. |

## Audit and Replay Requirements

Private / Local LLM-assisted DFIR workflows should emit or preserve:

- request identifier;
- correlation identifier;
- audit reference identifier — this **MUST** match the audit reference identifier used in the related `example-audit-event.json` structure so evidence, model output, review, enforcement, and final workflow state remain linked;
- tenant and customer identifiers;
- case, incident, and engagement identifiers;
- evidence manifest identifier;
- evidence object identifiers;
- derived artifact identifiers;
- chain-of-custody reference;
- analyst and reviewer identifiers;
- model identifier and version;
- prompt template identifier and prompt template version;
- prompt governance approval or change reference where applicable;
- retrieved context identifiers;
- knowledge or memory scope result;
- evidence format and validation result where applicable;
- forensic impact analysis identifier where applicable;
- parser or transformation versions;
- timeline output identifier;
- review record identifier;
- accepted, corrected, or rejected entries;
- approval or customer authorization references where required;
- output destination;
- final workflow state;
- deny, clarification, quarantine, or escalation reason where applicable.

## Fail-Closed Rules

| Failure Condition | Required Behavior |
|---|---|
| Missing `tenant_id`, `customer_id`, or `case_id` | Fail closed. |
| Evidence object identifier missing for timeline entry | Reject entry or return for correction. |
| Evidence format is unsupported or unvalidated | Block use in findings until validated or converted through approved process. |
| Chain-of-custody reference missing where required | Block formal finding or release. |
| Forensic Impact Analysis is missing where required | Block workflow start or return for clarification. |
| Prompt template is unapproved or version is missing | Block local model execution. |
| Retrieval returns cross-case or cross-customer context | Deny, quarantine result, and audit. |
| Unapproved local model runtime | Block model execution. |
| Unauthorized external network access attempted | Block, alert, and audit. |
| Persistent memory write attempted without approval | Deny and audit. |
| Source evidence modification attempted | Block unless explicit evidence-handling exception exists. |
| Customer release attempted without review | Block release. |
| Evidence export attempted without authorization | Block export and audit. |
| Output contains unsupported conclusion | Reject, correct, or route to DFIR lead. |
| Policy unavailable | Fail closed. |

## Relationship to Examples

| Example | Private / Local LLM-assisted DFIR Relevance |
|---|---|
| [`local-llm-forensic-timeline`](../examples/local-llm-forensic-timeline/) | Primary example for local LLM-assisted timeline drafting, analyst review, and auditability. |
| [`cloud-iam-compromise`](../examples/cloud-iam-compromise/) | Applies if cloud evidence escalates into local/private forensic analysis. |
| [`alert-triage-to-recommendation`](../examples/alert-triage-to-recommendation/) | Applies only if alert triage escalates into evidence handling or local/private DFIR. |

## Relationship to Patterns

| Pattern | Private / Local LLM-assisted DFIR Usage |
|---|---|
| [`private-local-llm-dfir-pattern.md`](../patterns/private-local-llm-dfir-pattern.md) | Baseline pattern for local/private LLM-assisted forensic analysis. |
| [`tenant-safe-rag-memory-pattern.md`](../patterns/tenant-safe-rag-memory-pattern.md) | Applies to local RAG, vector stores, case memory, evidence retrieval, and memory controls. |
| [`human-approved-sensitive-action-pattern.md`](../patterns/human-approved-sensitive-action-pattern.md) | Applies to evidence export, report release, final findings, and other sensitive DFIR actions. |
| [`policy-enforced-tool-use-pattern.md`](../patterns/policy-enforced-tool-use-pattern.md) | Applies to forensic parsers, scripts, notebooks, artifact tools, and controlled tool use. |
| [`governed-agentic-security-operations-pattern.md`](../patterns/governed-agentic-security-operations-pattern.md) | Baseline for scoped, policy-gated, auditable agentic security operations. |

Service owners must map these pattern requirements to deployment-specific local runtime controls, evidence stores, retrieval gateways, forensic tool wrappers, approval workflows, retention processes, and audit pipelines before implementation.

## Acceptance Criteria

A Private / Local LLM-assisted DFIR workflow is acceptable when:

- every workflow is bound to tenant, customer, case, incident or engagement, workflow, analyst, and evidence scope;
- original evidence is preserved and protected;
- evidence object identifiers are used in timeline entries and findings;
- chain of custody is preserved where required;
- local model runtime is approved, versioned, and controlled;
- governed prompt templates have owner, version, validation, sign-off, and audit linkage;
- Forensic Impact Analysis is completed before evidence, timeline, report, or tool-assisted workflows begin where required;
- evidence formats are validated or explicitly marked unsupported before use in findings;
- unauthorized network egress is blocked;
- retrieval is case-scoped and auditable;
- persistent memory is denied by default;
- parser and transformation versions are recorded;
- model-generated interpretation is labeled;
- observed facts are separated from hypotheses;
- analyst review occurs before findings or report use;
- unsupported inferences are rejected, corrected, or marked unresolved;
- customer-facing release requires review and authorization where required;
- evidence export requires approval and authorization;
- audit records support reconstruction.

## Non-Goals

This operating model does not:

- claim that local or private LLM execution is automatically safe;
- replace trained DFIR analysts;
- replace evidence handling or chain-of-custody requirements;
- require LLM use in every DFIR case;
- define a specific forensic tool, model, vector database, or runtime;
- allow model-generated conclusions to become findings without review;
- permit evidence export without authorization;
- replace customer contracts, legal requirements, or DFIR lead authority;
- authorize containment or remediation actions outside MDR, Cloud IR, or SOC / IR controls.

## Summary

The Private / Local LLM-assisted DFIR operating model defines how local or isolated AI assistance can support forensic analysis while preserving evidence integrity, case scope, analyst accountability, customer authorization, and auditability.

The core principle is:

> Private or local LLMs may assist DFIR, but forensic conclusions must remain evidence-backed, analyst-reviewed, case-scoped, policy-controlled, and auditable.
