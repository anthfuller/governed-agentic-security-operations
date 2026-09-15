# Local LLM Forensic Timeline Example

## Purpose

This example demonstrates how a **Private / Local LLM-assisted DFIR** workflow can support forensic timeline development while preserving evidence integrity, case scope, human validation, and auditability.

The example supports the **Agentic MSSP / MDR / DFIR Security Operations Architecture** where applicable by showing how local AI assistance can help organize forensic events into a timeline without allowing the model to become the authority for forensic conclusions.

The core purpose is to show a governed workflow where a local or isolated LLM assists with timeline construction, but final findings remain evidence-backed, analyst-reviewed, and auditable.

## Scenario

A DFIR analyst is working in a local or isolated forensic workspace. The analyst has approved evidence artifacts from a specific customer incident, including parsed logs, endpoint activity, authentication events, process execution records, cloud activity, or derived forensic artifacts.

A local LLM-assisted workflow is used to help organize approved evidence into a draft timeline.

The local LLM may summarize, group, normalize, and explain events, but it must not:

- alter original evidence;
- retrieve unrelated cases;
- write persistent memory by default;
- produce final forensic findings without review;
- publish customer-facing conclusions;
- export evidence without authorization;
- treat inferred activity as observed fact.

## Service Model Applicability

| Service Model | Applicability |
|---|---|
| DFIR | Primary use case. Applies to forensic timeline support, evidence review, artifact correlation, analyst validation, and report preparation. |
| Private / Local LLM-assisted DFIR | Primary use case. Applies when local, isolated, air-gapped, or customer-controlled LLMs assist with forensic timeline analysis. |
| SOC / Incident Response | Applies when incident response escalates into evidence review or timeline reconstruction. |
| MDR | Applies when MDR workflows require forensic triage, timeline assistance, or escalation into DFIR. |
| MSSP | Applies only when managed service delivery includes or hands off to customer-scoped DFIR timeline support. |

This example should not be forced into standard alert triage or basic MDR workflows unless evidence handling or timeline analysis is actually in scope.

## Example Files

| File | Purpose |
|---|---|
| `README.md` | Explains the scenario, workflow, controls, review path, auditability, failure paths, and related patterns. |
| `example-evidence-manifest.json` | Describes the approved evidence set, provenance, hashes, case scope, parser outputs, and chain-of-custody references. |
| `example-timeline-output.json` | Shows the local LLM-assisted draft timeline with event references, confidence, evidence links, and distinction between observed facts and interpretations. |
| `example-review-record.json` | Shows analyst review, validation decisions, corrections, rejected inferences, and approval status for timeline use. |
| `example-audit-event.json` | Shows the audit event correlating evidence manifest, local model runtime, retrieval context, timeline output, review record, and final workflow state. |

## Actors and Components

| Actor or Component | Role |
|---|---|
| DFIR analyst | Reviews evidence, validates model-assisted timeline output, and remains accountable for findings. |
| Local LLM runtime | Assists with summarization, grouping, normalization, and timeline drafting inside an approved local or isolated environment. |
| Forensic workspace | Holds case-scoped evidence, derived artifacts, local indexes, working notes, and timeline outputs. |
| Evidence store | Preserves original evidence and derived artifacts with provenance, hashes, timestamps, and chain-of-custody references. |
| Local retrieval layer | Retrieves only approved case-scoped evidence and derived artifacts for the local model. |
| Policy and enforcement controls | Enforce case scope, evidence scope, output destination, tool use, and retention controls. |
| Review workflow | Records analyst validation, corrections, rejected inferences, and approval status. |
| Audit layer | Records evidence access, model runtime metadata, timeline generation, review, and final workflow state. |

## Preconditions

Before this workflow runs, the system should have:

- a valid `tenant_id`;
- a valid `customer_id`;
- a valid `case_id`;
- a valid `incident_id` or engagement reference;
- a valid `workflow_id`;
- an identified analyst;
- an approved local or private LLM runtime;
- an evidence manifest with evidence object identifiers;
- original evidence preserved in read-only form where required;
- hashes and provenance recorded for evidence objects;
- chain-of-custody references where applicable;
- approved parser or transformation outputs;
- case-scoped local retrieval or index namespace;
- defined output destination;
- retention and deletion handling;
- review and audit requirements.

## Example Flow

1. **Case-scoped evidence is registered**  
   Evidence objects are added to the evidence manifest with source, hash, provenance, collection time, custodian, classification, and chain-of-custody reference.

2. **Derived artifacts are produced**  
   Approved tools or parsers generate derived artifacts such as parsed logs, timeline fragments, process execution records, authentication events, or cloud activity summaries.

3. **Local retrieval context is prepared**  
   Only approved case-scoped evidence and derived artifacts are indexed or made available to the local LLM workflow.

4. **Analyst requests timeline assistance**  
   The analyst asks the local LLM-assisted workflow to organize approved events into a draft timeline.

5. **Local LLM generates draft timeline**  
   The model creates a structured timeline output using only approved case-scoped context.

6. **Timeline output distinguishes evidence from interpretation**  
   The output separates observed evidence, derived facts, analyst notes, model-generated interpretation, hypotheses, and unresolved questions.

7. **Analyst review is performed**  
   A qualified analyst validates, corrects, rejects, or approves timeline entries before they are used in findings or reports.

8. **Review record is created**  
   The review record documents accepted entries, rejected inferences, required corrections, confidence, limitations, and release status.

9. **Audit event is emitted**  
   The audit event correlates evidence manifest, model runtime, retrieval scope, timeline output, review record, and final workflow state.

10. **Case retention or closure handling applies**  
   Local indexes, derived artifacts, prompts, outputs, and working files are retained, archived, deleted, or transferred according to case and customer policy.

## Local LLM Controls

The local LLM runtime should enforce:

- approved model selection;
- model version tracking;
- prompt template control;
- case-scoped input;
- no unauthorized network egress;
- no training on customer evidence;
- no persistent memory write by default;
- local storage controls;
- analyst access controls;
- prompt and output logging where policy allows;
- metadata logging where full prompt logging is restricted;
- governed model, prompt, and workflow updates.

Local execution is not sufficient by itself. The workflow still requires case scope, evidence references, review, and auditability.

## Evidence and Timeline Controls

The timeline workflow must preserve forensic integrity.

Required controls include:

- original evidence preserved in read-only form where required;
- evidence object identifiers for timeline entries;
- evidence hash references;
- provenance and collection metadata;
- parser or transformation versioning;
- separation of original evidence from derived artifacts;
- distinction between observed facts and model interpretation;
- timestamp normalization with source timezone retained where applicable;
- analyst validation before use in findings;
- chain-of-custody references where applicable.

## RAG, Retrieval, and Memory Controls

If local RAG or retrieval is used, the workflow must enforce:

- case-specific namespace;
- customer and tenant scope;
- evidence object scope;
- approved ingestion sources;
- parser or transformation version tracking;
- no unrelated case retrieval;
- no cross-customer retrieval;
- no persistent memory write by default;
- retention and deletion handling for indexes, chunks, embeddings, summaries, and memory records;
- audit of retrieved context used in timeline generation.

Persistent memory should not be used unless there is explicit purpose, owner, retention rule, approval, and audit trail.

## Tool Use Controls

If forensic tools, scripts, notebooks, parsers, or timeline utilities are used, the workflow should enforce:

- approved tool registry;
- tool owner;
- tool version;
- source evidence identifiers;
- destination or output location;
- read-only default for source evidence;
- parameter logging;
- parser or transformation version tracking;
- output validation;
- failure logging;
- analyst review before outputs support conclusions.

Tools should not modify source evidence unless explicitly approved through a separate sensitive-action path.

## Review Requirements

Analyst review is required before timeline output is used in:

- forensic findings;
- customer-facing reports;
- incident summaries;
- attribution statements;
- containment recommendations;
- legal, regulatory, or executive communications;
- case closure decisions.

The review should identify:

- accepted timeline entries;
- corrected entries;
- rejected entries;
- unsupported inferences;
- missing evidence;
- timestamp or timezone concerns;
- confidence and limitations;
- whether additional evidence is needed.

## Evidence, Audit, and Traceability

The example should preserve enough information to reconstruct how the timeline was produced.

Audit and traceability should include:

- evidence manifest reference;
- evidence object identifiers;
- evidence hashes where applicable;
- parser or transformation versions;
- model identifier and version;
- prompt template identifier;
- retrieval context identifiers;
- timeline output identifier;
- analyst review record;
- accepted and rejected timeline entries;
- output destination;
- retention policy;
- audit and correlation identifiers.

Where full prompt or response logging is restricted, metadata and references should still support review and reconstruction.

## Failure and Deny Paths

The workflow should deny, fail closed, quarantine, or return for clarification when:

- case scope is missing;
- evidence scope is missing;
- evidence hash or provenance is missing where required;
- chain-of-custody reference is missing where required;
- retrieval returns unrelated case or customer context;
- local model attempts network egress without authorization;
- output includes unsupported forensic conclusions;
- timeline entries lack evidence references;
- timestamps cannot be normalized or source timezone is unclear;
- persistent memory write is attempted without approval;
- source evidence modification is attempted without approval;
- customer-facing release is attempted without review;
- evidence export or transfer is requested without authorization.

## What This Example Should Not Do

This example should not:

- treat local LLM output as a final forensic finding;
- allow model-generated interpretation to replace evidence;
- modify original evidence;
- blend unrelated cases or customers;
- write persistent memory by default;
- export evidence without authorization;
- release customer-facing reports without analyst review;
- claim that local execution alone makes the workflow trustworthy;
- bypass policy, review, or audit requirements because the model runs locally.

## Expected Control Outcome

A successful run should produce:

- a scoped evidence manifest;
- a local LLM-assisted draft timeline;
- evidence references for timeline entries;
- clear distinction between observed facts and interpretations;
- analyst review record;
- accepted, corrected, or rejected timeline entries;
- audit event supporting reconstruction;
- final workflow state showing whether the timeline is draft, analyst-validated, or approved for limited use.

## Acceptance Criteria

This example is acceptable when:

- the workflow is scoped to a specific tenant, customer, case, incident, and evidence set;
- original evidence is preserved;
- evidence provenance and hashes are captured where applicable;
- chain of custody is preserved where required;
- local model runtime is identified and controlled;
- retrieval is case-scoped and auditable;
- timeline entries reference evidence objects;
- model-generated interpretations are separated from observed facts;
- analyst review is required before findings or reports use the timeline;
- rejected or corrected model outputs are recorded;
- customer-facing release is not allowed without review and authorization;
- audit records allow the workflow to be reconstructed.

## Related Patterns

This example maps to:

- [`private-local-llm-dfir-pattern.md`](../../patterns/private-local-llm-dfir-pattern.md)
- [`tenant-safe-rag-memory-pattern.md`](../../patterns/tenant-safe-rag-memory-pattern.md)
- [`human-approved-sensitive-action-pattern.md`](../../patterns/human-approved-sensitive-action-pattern.md)
- [`policy-enforced-tool-use-pattern.md`](../../patterns/policy-enforced-tool-use-pattern.md)
- [`governed-agentic-security-operations-pattern.md`](../../patterns/governed-agentic-security-operations-pattern.md)
- [`control-loop.md`](../../architecture/control-loop.md)
- [`layered-architecture.md`](../../architecture/layered-architecture.md)

## Summary

This example shows how a local LLM can assist DFIR timeline development without becoming the authority for forensic conclusions.

The core principle is:

> A local LLM may help organize forensic events, but timeline entries and conclusions must remain case-scoped, evidence-backed, analyst-reviewed, and auditable.
