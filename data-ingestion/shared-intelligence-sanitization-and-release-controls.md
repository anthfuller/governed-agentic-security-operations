# Shared Intelligence Sanitization and Release Controls

## Purpose

This file defines controls for converting ingestion-derived security observations into sanitized, approved, versioned, and scoped shared intelligence.

Shared intelligence may include reusable detection patterns, enrichment context, threat-hunting hypotheses, TTP summaries, ATT&CK or ATLAS mappings, indicator packages, agent context packages, report guidance, and operational lessons derived from governed ingestion workflows.

The goal is to let security knowledge improve future Managed SOC / MSSP, MDR, cloud incident response, detection engineering, threat hunting, and private/local LLM-assisted DFIR workflows without redistributing raw tenant data, raw customer data, raw evidence, case details, secrets, or customer-specific operational context.

This file defines sanitization and release governance expectations. It does not define production content pipelines, legal determinations, customer contract terms, external intelligence-sharing agreements, detection-rule syntax, or platform-specific release automation.

## Scope

This file applies to shared intelligence created from or influenced by:

- SIEM, XDR, EDR, NDR, firewall, identity, email, cloud, SaaS, ticketing, case-management, vulnerability, asset, and business-application telemetry;
- normalized records, enrichment records, correlation results, detection outcomes, and investigation timelines;
- agent-generated summaries, analyst notes, Agent Judge findings, and review records that depend on ingested data;
- private/local LLM-assisted DFIR extraction, parsing, summarization, and timeline reconstruction output;
- evidence-derived metadata used to create reusable detection or threat-hunting knowledge;
- customer-approved intelligence intended for controlled reuse;
- curated external threat intelligence combined with tenant, customer, case, or evidence-derived context;
- release packages distributed to eligible tenants, customers, agents, detection repositories, enrichment stores, knowledge stores, vector indexes, report workflows, or playbook libraries.

This file does not authorize cross-tenant reuse, customer-facing release, evidence release, sensitive disclosure, containment, remediation, access change, or case closure. Those decisions remain governed by policy, approval, evidence, tenant-isolation, tool-access, and human-oversight controls.

## Core Principles

- Raw tenant data, raw customer data, raw evidence, and raw case content MUST NOT be redistributed as shared intelligence.
- Sanitization is not approval.
- De-identification is not sufficient unless release scope, allowed use, retention, provenance, approval, and audit requirements are also satisfied.
- Shared intelligence MUST remain distinguishable from source records, evidence records, analyst notes, model output, and customer-facing reports.
- Tenant identity and customer identity MUST remain separate in internal provenance and release-control records.
- Release packages MUST define eligible consumers, allowed use, version, owner, expiration or revalidation expectations, rollback path, recall path, and audit references.
- Agent-generated candidate intelligence MUST be reviewed before release.
- Shared intelligence MUST NOT authorize tool execution, response action, customer notification, evidence disclosure, or cross-boundary access.
- Knowledge stores, vector indexes, shared memory, case memory, and agent context packages MUST NOT receive shared intelligence unless destination, retention, and reuse controls are approved.
- Missing, ambiguous, stale, unauthorized, or unauditable sanitization or release context MUST fail closed.

## Shared Intelligence Types

| Type | Description | Release Control Requirement |
|---|---|---|
| Detection pattern | Reusable logic, condition, behavior, or correlation pattern derived from observed activity. | Requires source support, sanitization, test context, owner, version, allowed use, and release approval. |
| Indicator package | Domains, IPs, URLs, file hashes, certificate attributes, sender traits, process traits, or infrastructure indicators. | Requires sensitivity review, source permission, confidence, expiration, and destination scope. |
| TTP summary | Generalized adversary behavior, technique sequence, tool behavior, or tradecraft description. | Requires removal of customer, case, asset, user, and evidence details. |
| Threat-hunting hypothesis | Reusable hunt question, analytic angle, or investigative hypothesis. | Requires scoped use, source limitations, and validation status. |
| Enrichment package | Reusable enrichment context for identity, asset, cloud, SaaS, vulnerability, campaign, or infrastructure interpretation. | Requires source attribution, freshness, allowed use, retention, and boundary checks. |
| Agent context package | Sanitized context supplied to agents for triage, enrichment, investigation, drafting, or prioritization. | Requires approved destination, retrieval scope, version, and policy constraints. |
| Playbook or workflow guidance | Generalized investigation steps, escalation criteria, or analyst guidance. | Requires removal of customer-specific actions, approvals, credentials, and environment assumptions. |
| Report guidance | Reusable wording, structure, explanation, or evidence-support guidance. | Requires confirmation that no customer-specific facts or evidence content are embedded. |
| ATT&CK or ATLAS mapping | Technique, tactic, or AI-system risk mapping derived from investigation or assurance findings. | Requires source support and clear confidence or limitation notes. |
| Sanitized lessons learned | Generalized operational learning from incidents, failures, exceptions, or reviews. | Requires de-identification, owner review, approval, and release scope. |

## Content That Must Not Be Released as Shared Intelligence

Shared intelligence packages MUST NOT include:

- raw logs, raw alerts, raw packets, raw memory content, raw disk artifacts, raw files, raw emails, or raw evidence content;
- customer names, tenant names, internal aliases, organization identifiers, customer contract details, or customer-specific service details;
- tenant IDs, customer IDs, subscription IDs, account IDs, project IDs, workspace IDs, directory IDs, mailbox IDs, user IDs, device IDs, hostnames, internal IPs, case IDs, ticket IDs, incident IDs, or evidence object IDs unless explicitly approved for the specific release path;
- credentials, secrets, API keys, tokens, private keys, session identifiers, authentication material, or privileged access details;
- personal data, regulated data, legal-sensitive material, protected communications, or privacy-sensitive details unless the governed release path explicitly permits the specific disclosure;
- customer-specific containment steps, remediation steps, vulnerabilities, architecture details, control weaknesses, business context, or response decisions;
- chain-of-custody records, examiner notes, legal hold details, or forensic conclusions intended for a specific matter;
- unreviewed model output, unsupported claims, hallucinated details, or inferred facts without source support;
- data from a failed, quarantined, disputed, expired, recalled, or unauditable ingestion path.

Customer-derived indicators, hashes, domains, IP addresses, infrastructure traits, malware traits, or behavioral patterns MAY be released only when source permission, sensitivity handling, allowed use, approval, retention, and destination controls permit that release.

## Sanitization Lifecycle

| Stage | Purpose | Required Outcome |
|---|---|---|
| Candidate identification | Identify reusable knowledge from ingestion, investigation, DFIR, enrichment, assurance, or analyst review. | Candidate record with source, owner, scope, and reason for reuse. |
| Source and scope review | Determine source systems, tenants, customers, cases, evidence references, workflow context, and allowed use. | Source lineage and boundary context are known. |
| Classification review | Assign data classification, sensitivity label, retention, legal/privacy flags where applicable, and release risk. | Handling requirements are known before transformation. |
| Sanitization | Remove, transform, generalize, aggregate, or suppress sensitive source details. | Sanitized candidate that no longer exposes raw tenant, customer, case, or evidence data. |
| Boundary validation | Validate tenant, customer, case, evidence, retrieval, retention, and destination boundaries. | Release candidate is either valid, blocked, or routed for review. |
| Quality and support review | Validate evidence support, enrichment source, confidence, limitations, false-positive risk, and operational usefulness. | Candidate is ready for approval, rejected, or returned for correction. |
| Approval | Obtain required internal, customer, legal/privacy, or release-owner approval where policy requires it. | Scoped approval record linked to the release candidate. |
| Packaging | Assign release identifier, version, allowed use, eligible consumers, destination, expiration, rollback, and recall conditions. | Release package is versioned and ready for controlled distribution. |
| Distribution | Release only to approved destinations and eligible consumers through governed routing. | Distribution record identifies who or what received the package. |
| Monitoring | Monitor for misuse, boundary issues, false positives, drift, stale context, or customer impact. | Monitoring signals drive correction, rollback, recall, or revalidation. |
| Correction, rollback, or recall | Update, withdraw, revoke, quarantine, or supersede released intelligence when needed. | Affected consumers and downstream uses are auditable. |

## Sanitization Requirements

| Area | Requirement |
|---|---|
| Identifier removal | Customer, tenant, account, project, subscription, workspace, user, host, mailbox, ticket, incident, and case identifiers MUST be removed, transformed, or suppressed unless explicitly approved for the release scope. |
| Evidence boundary | Raw evidence and evidence object identifiers MUST NOT be released as shared intelligence unless the evidence-release path explicitly permits it. |
| Source attribution | Internal release records MUST preserve source lineage without exposing raw source material to unauthorized consumers. |
| Generalization | Customer-specific observations SHOULD be generalized into reusable behavior, logic, conditions, TTPs, or lessons learned. |
| Aggregation | Aggregated patterns MUST avoid exposing a single customer, tenant, case, asset, user, or evidence set by inference. |
| Time handling | Exact timestamps SHOULD be generalized or removed when they could identify a customer, incident, case, activity window, or evidence object. |
| Volume handling | Counts and frequencies SHOULD be rounded, banded, or suppressed when exact values create customer or case exposure. |
| Location handling | Regions, geographies, business units, and environment labels MUST be removed or generalized when they expose customer or case identity. |
| Vulnerability handling | Customer-specific vulnerabilities, missing controls, architecture weaknesses, or exposure details MUST NOT be included in shared packages. |
| Indicator handling | Indicators MUST be evaluated for source permission, sensitivity, confidence, expiration, false-positive risk, and allowed use before release. |
| Prompt and context handling | Prompts, agent context packages, RAG content, vector entries, and shared memory MUST NOT embed raw source records, customer details, evidence content, or unapproved case facts. |
| Enrichment handling | Enrichment values MUST preserve source, freshness, confidence, and limitations and MUST NOT overwrite source meaning. |
| Unsupported claims | Claims without source support MUST be removed or routed for review. |
| Destination control | Sanitized output MUST be checked against destination, retention, reuse, and consumer eligibility controls before release. |

## Required Sanitization Record

A governed sanitization workflow SHOULD produce a structured record with the following fields where applicable.

| Field | Requirement | Purpose |
|---|---|---|
| `sanitization_record_id` | MUST | Unique identifier for the sanitization record. |
| `shared_intelligence_candidate_id` | MUST | Links sanitization to the candidate intelligence item. |
| `candidate_type` | MUST | Identifies detection pattern, indicator package, TTP summary, hunt hypothesis, enrichment package, agent context package, playbook guidance, report guidance, mapping, or lesson learned. |
| `originating_workflow_id` | MUST when created from a governed workflow | Links the candidate to the workflow that produced it. |
| `source_system_ids` | MUST when source systems influenced the candidate | Identifies systems that contributed source records or enrichment. |
| `source_ingestion_record_refs` | SHOULD | References source ingestion records without exposing raw source content to release consumers. |
| `normalization_record_refs` | SHOULD when normalized records influenced the candidate | Links to normalization outputs used during derivation. |
| `enrichment_record_refs` | SHOULD when enrichment influenced the candidate | Links to enrichment context and freshness. |
| `evidence_refs_internal` | MUST when evidence influenced the candidate | Preserves internal evidence traceability without releasing raw evidence. |
| `tenant_ids_internal` | MUST when tenant-scoped data influenced the candidate | Preserves internal tenant provenance. |
| `customer_ids_internal` | MUST when customer-scoped data influenced the candidate | Preserves internal customer provenance separately from tenant identity. |
| `case_ids_internal` | MUST when case-bound data influenced the candidate | Preserves internal case provenance. |
| `data_classification` | MUST | Defines handling requirements. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity and handling context. |
| `allowed_use` | MUST | Defines permitted uses such as detection, enrichment, triage, threat hunting, reporting support, agent context, or assurance. |
| `disallowed_use` | SHOULD | Defines prohibited uses such as customer notification, action authorization, evidence disclosure, or legal conclusion. |
| `retention_policy_id` | MUST when retention applies | Preserves retention and disposal expectations. |
| `sanitization_method` | MUST | Identifies removal, generalization, aggregation, hashing, masking, suppression, transformation, or rewriting method. |
| `removed_or_transformed_elements_ref` | MUST | References what was removed or transformed without re-exposing sensitive values. |
| `residual_reidentification_risk` | MUST | Records low, moderate, high, unknown, or review-required residual risk. |
| `sanitization_validation_result` | MUST | Records pass, fail, partial, review-required, or blocked result. |
| `quality_validation_result` | SHOULD | Records usefulness, confidence, false-positive risk, limitations, and test status where applicable. |
| `review_record_id` | MUST when human review is required | Links to review of sanitization quality and boundary handling. |
| `policy_context_id` | MUST when policy affects release, routing, retention, or allowed use | Links sanitization to applicable policy context. |
| `approval_record_id` | MUST when release requires formal approval | Links to scoped approval. |
| `audit_reference_id` | MUST | Supports replay and accountability. |
| `correlation_ids` | MUST when available | Links ingestion, normalization, enrichment, evidence, policy, approval, release, and audit records. |

## Required Release Package Record

A shared intelligence release package MUST define the release scope and downstream handling requirements.

| Field | Requirement | Purpose |
|---|---|---|
| `shared_intelligence_release_id` | MUST | Unique identifier for the release. |
| `release_package_id` | MUST | Identifies the packaged content. |
| `release_version` | MUST | Supports versioning, rollback, recall, and replay. |
| `release_owner` | MUST | Identifies accountable owner. |
| `release_type` | MUST | Identifies detection package, indicator package, enrichment package, hunt package, agent context package, report guidance, playbook guidance, or mapping package. |
| `sanitization_record_id` | MUST | Links release to sanitization validation. |
| `release_state` | MUST | Records candidate, review-required, approved, released, blocked, deprecated, corrected, rolled back, recalled, or revoked. |
| `release_scope` | MUST | Defines eligible tenants, customers, services, roles, workflows, environments, or internal destinations. |
| `eligible_consumer_types` | MUST | Defines analysts, agents, Agent Judges, detection engineering workflows, enrichment stores, hunt workflows, report workflows, or governance workflows allowed to consume the package. |
| `distribution_destinations` | MUST | Identifies detection repository, knowledge store, vector index, case workflow, enrichment store, report workflow, agent package, or other approved destination. |
| `allowed_use` | MUST | Defines what the release may be used for. |
| `disallowed_use` | SHOULD | Defines what the release must not be used for. |
| `data_classification` | MUST | Preserves release handling requirements. |
| `sensitivity_label` | MUST when applicable | Preserves sensitivity handling. |
| `confidence_level` | SHOULD | Communicates confidence without implying correctness or authorization. |
| `limitations` | SHOULD | Records known gaps, false-positive risk, stale-source risk, or conditions of use. |
| `effective_time_utc` | MUST when release is active | Defines when the release becomes usable. |
| `expiration_time_utc` | SHOULD when intelligence can age out | Supports revalidation and stale-content prevention. |
| `revalidation_interval` | SHOULD | Defines when the release must be reviewed again. |
| `rollback_conditions` | MUST for operational content | Defines when release must be reverted to a prior version. |
| `recall_conditions` | MUST | Defines when release must be withdrawn or quarantined. |
| `policy_context_id` | MUST | Links release to applicable policy. |
| `approval_record_id` | MUST when required | Links release to approval authority and scope. |
| `release_audit_reference_id` | MUST | Supports audit replay. |
| `correlation_ids` | MUST when available | Links related candidate, sanitization, review, approval, release, distribution, rollback, recall, and audit records. |

## Review and Approval Gates

Shared intelligence release MUST preserve separation between review and approval.

| Gate | Purpose | Required Outcome |
|---|---|---|
| Source lineage review | Confirm that source, ingestion, normalization, enrichment, evidence, and workflow lineage are known. | Candidate is supported or rejected. |
| Boundary review | Confirm tenant, customer, case, evidence, retention, and allowed-use boundaries. | Boundary status is pass, fail, or review-required. |
| Sanitization review | Confirm sensitive identifiers, raw records, evidence content, customer context, and restricted details have been removed or transformed. | Sanitization result is recorded. |
| Quality review | Confirm usefulness, confidence, limitations, false-positive risk, and operational fit. | Candidate is ready for release approval or correction. |
| Policy decision | Determine whether release is allowed, denied, approval-required, or failed closed. | PDP decision reference is recorded where applicable. |
| Formal approval | Authorize release for the defined scope where policy requires approval. | Approval record identifies authority, scope, expiration, and conditions. |
| Distribution enforcement | Enforce release scope and destination restrictions. | PEP or equivalent enforcement result is recorded. |
| Post-release monitoring | Monitor release impact, misuse, drift, stale context, false positives, and boundary concerns. | Correction, rollback, recall, or revalidation is triggered when required. |

Human review MAY validate sanitization, quality, and boundary handling. Formal approval MAY authorize a scoped release. Neither review nor approval authorizes unrelated tool execution, response action, evidence release, customer notification, or cross-boundary access.

## Release States

| State | Meaning | Allowed Handling |
|---|---|---|
| `CANDIDATE` | Potential shared intelligence has been identified. | Internal review only. |
| `SANITIZATION_IN_PROGRESS` | Sensitive content is being removed, transformed, or generalized. | No distribution. |
| `REVIEW_REQUIRED` | Human or specialized review is required. | Hold until review completes. |
| `APPROVAL_REQUIRED` | Formal approval is required before release. | Hold until approval is granted. |
| `APPROVED` | Release has been approved for a defined scope. | Distribution may occur only through approved destinations. |
| `RELEASED` | Package has been distributed to eligible consumers. | Monitor, audit, and enforce allowed use. |
| `BLOCKED` | Candidate failed sanitization, policy, approval, quality, or boundary checks. | Do not distribute. Preserve audit record. |
| `CORRECTED` | Released package has been superseded by a corrected version. | Preserve prior version and correction record. |
| `DEPRECATED` | Package remains referenceable but should not be used for new workflows. | Restrict new use and preserve replayability. |
| `ROLLED_BACK` | Distribution reverted to a prior approved version. | Notify affected systems and audit impact. |
| `RECALLED` | Package is withdrawn because it is unsafe, unauthorized, incorrect, stale, or boundary-violating. | Remove from active destinations and quarantine downstream use. |
| `REVOKED` | Approval or authorization was withdrawn. | Stop use and preserve revocation record. |

## Allowed Use and Destination Controls

Shared intelligence MUST be released only for approved uses and destinations.

| Destination | Control Requirement |
|---|---|
| Detection repository | Release package MUST define detection scope, version, test status, owner, rollback path, and eligible tenants or environments. |
| Enrichment store | Release package MUST preserve source, freshness, confidence, expiration, allowed use, and retention. |
| Knowledge store or vector index | Package MUST be sanitized, scoped, versioned, retention-bound, and retrievable only by approved workflows or agents. |
| Agent context package | Package MUST include allowed use, limitations, source-support references, and policy constraints. |
| Threat-hunting workflow | Package MUST define hypothesis scope, confidence, limitations, and customer or tenant eligibility. |
| Report workflow | Package MUST be reusable guidance only unless specific customer-facing content has separate review and approval. |
| Playbook library | Package MUST avoid customer-specific authority, credentials, environment details, or action authorization. |
| Governance or assurance workflow | Package MUST be traceable to source, sanitization, release, and audit records. |

Destination approval MUST be evaluated before distribution. A package approved for detection use MUST NOT automatically be approved for reporting, customer communication, agent memory, evidence handling, or response action.

## Agent Use of Shared Intelligence

Agents MAY:

- identify candidate reusable patterns from scoped ingestion outputs;
- draft sanitized summaries for review;
- propose TTP mappings, hunt hypotheses, enrichment candidates, or detection-pattern candidates;
- compare a candidate against known shared intelligence packages;
- prepare release packages, review packets, limitations, and audit references;
- consume approved shared intelligence within assigned workflow, tenant, customer, case, retrieval, retention, and allowed-use scope.

Agents MUST NOT:

- approve shared intelligence release;
- bypass sanitization, review, policy, approval, or destination controls;
- route raw customer, tenant, case, or evidence data into shared knowledge stores, vector indexes, shared memory, or agent context packages;
- treat shared intelligence as proof of incident truth, evidence completeness, customer approval, or action authorization;
- expand release scope beyond the approved consumers, destinations, workflows, tenants, or customers;
- reuse stale, revoked, recalled, or expired intelligence without revalidation;
- convert customer-specific findings into generalized claims without source support and review.

## Private/Local LLM-Assisted DFIR Requirements

Private/local LLM-assisted DFIR workflows MAY produce candidate intelligence such as artifact patterns, timeline observations, malware behavior summaries, detection ideas, or report guidance.

Local execution does not authorize sharing.

DFIR-derived shared intelligence MUST satisfy these requirements:

- raw evidence, raw artifacts, chain-of-custody details, examiner notes, legal hold context, and case-specific findings remain inside the approved case and evidence boundary;
- extracted indicators or behaviors are reviewed for sensitivity, source permission, customer scope, confidence, and release eligibility;
- evidence references are preserved internally for audit without exposing evidence content to release consumers;
- examiner review is required before DFIR-derived intelligence is released beyond the original case scope;
- customer-facing DFIR conclusions remain governed by evidence validation, examiner review, and approval paths separate from shared intelligence release.

## Policy Enforcement Boundary

Shared intelligence release MUST preserve separation between sanitization, review, approval, PDP, PEP, agents, tools, and audit.

| Component | Responsibility |
|---|---|
| Ingestion workflow | Provides source records, metadata, normalization, enrichment, and provenance. |
| Sanitization workflow | Removes, transforms, suppresses, or generalizes sensitive content. |
| Agent | May propose or consume shared intelligence within governed scope. |
| Human reviewer | Reviews source support, quality, boundary handling, and sanitization results. |
| Formal approver | Approves scoped release where policy requires approval. |
| PDP | Produces governed authorization decisions where policy gating is required. |
| PEP | Enforces release, destination, eligibility, and allowed-use constraints. |
| Audit system | Records source lineage, sanitization, review, approval, release, distribution, correction, rollback, recall, and downstream use. |

A sanitization result MUST NOT be treated as a PDP decision. A release approval MUST NOT be treated as authorization for unrelated tools, actions, customer notifications, or evidence release.

## Fail-Closed Conditions

Shared intelligence release MUST fail closed, quarantine, or route to governed review when:

- source lineage is missing, ambiguous, stale, unauthorized, inconsistent, or unauditable;
- tenant, customer, case, workspace, account, project, subscription, evidence, retention, or allowed-use scope is missing or inconsistent;
- source ingestion, parsing, normalization, enrichment, or audit records are quarantined, disputed, failed, recalled, or incomplete;
- raw tenant data, raw customer data, raw evidence, personal data, secrets, credentials, customer identifiers, or case details remain in the release candidate;
- residual re-identification risk is high, unknown, or unresolved;
- required sanitization validation, quality review, human review, policy decision, approval, destination authorization, or release audit record is missing;
- release destination, eligible consumer, allowed use, retention, expiration, rollback, or recall path is undefined;
- candidate intelligence includes unsupported claims, unresolved conflicts, stale enrichment, or unverified model-generated content;
- a knowledge store, vector index, shared memory, case memory, or agent context package would receive unapproved or unscoped content;
- customer-derived indicators would be shared without source permission, sensitivity review, allowed-use constraints, and approval;
- audit logging fails where release audit is required.

Fail-closed handling MUST preserve the candidate record, source references, sanitization record, failure reason, affected scope, review route, policy context, approval context where available, and audit references.

## Audit and Replay Requirements

Audit replay MUST be able to reconstruct:

- which source systems, ingestion records, normalized records, enrichment records, evidence references, workflows, and cases influenced the candidate;
- which tenants and customers contributed source material, while preserving access controls over provenance details;
- what content was removed, generalized, transformed, suppressed, or retained during sanitization;
- who or what proposed the candidate;
- which agent, analyst, examiner, reviewer, approver, PDP, PEP, and workflow participated;
- which data classification, sensitivity label, allowed use, retention policy, expiration, release scope, and destination applied;
- which release version was approved and distributed;
- which consumers, agents, stores, indexes, workflows, tenants, or customers received the release;
- which monitoring signals, corrections, rollbacks, recalls, revocations, or exceptions occurred after release;
- which downstream workflows consumed the intelligence before and after correction, rollback, or recall.

Audit records SHOULD reference source and evidence records rather than copying raw source data or raw evidence into release audit logs.

## Rollback, Recall, Correction, and Revocation

Shared intelligence packages MUST support controlled rollback, recall, correction, and revocation.

| Action | Use When | Required Handling |
|---|---|---|
| Correction | Released content contains an error, stale context, unsupported claim, confidence change, or incomplete limitation. | Publish a corrected version, preserve prior version, and audit affected consumers. |
| Rollback | A new version causes operational issues, false positives, policy conflicts, or unexpected downstream impact. | Revert to prior approved version where available and record affected destinations. |
| Recall | Content is unsafe, unauthorized, boundary-violating, contaminated, disputed, or derived from invalid source data. | Withdraw from active use, quarantine downstream consumption, notify accountable owners, and audit impact. |
| Revocation | Approval, authorization, source permission, or allowed use is withdrawn. | Stop use, mark release revoked, preserve revocation reason, and evaluate downstream use. |
| Deprecation | Content is obsolete but not unsafe. | Prevent new use while preserving replay references. |

Rollback or recall MUST evaluate detection repositories, enrichment stores, knowledge stores, vector indexes, shared memory, agent context packages, report workflows, case workflows, and any downstream package that consumed the release.

## Relationship to Other Data-Ingestion Files

| File | Relationship |
|---|---|
| [`data-ingestion-model.md`](data-ingestion-model.md) | Defines the broader ingestion model and how sanitized intelligence enters governed workflows. |
| [`source-system-metadata.md`](source-system-metadata.md) | Defines source metadata required to understand provenance, owner, classification, and allowed use. |
| [`normalization-and-enrichment.md`](normalization-and-enrichment.md) | Defines normalized and enriched records that may support candidate shared intelligence. |
| [`ingestion-failure-handling.md`](ingestion-failure-handling.md) | Defines failure handling that must block release when source, sanitization, or routing context is invalid. |
| [`ingestion-audit-replay.md`](ingestion-audit-replay.md) | Defines replay requirements for source-to-release reconstruction. |

## Relationship to Other Control Areas

- [`../tenant-isolation/readme.md`](../tenant-isolation/readme.md) defines tenant, customer, case, and cross-tenant boundary controls.
- [`../policy-enforcement/readme.md`](../policy-enforcement/readme.md) defines PDP, PEP, policy decisions, approval requirements, and fail-closed behavior.
- [`../human-oversight/readme.md`](../human-oversight/readme.md) defines review, formal approval, customer approval, escalation, and review records.
- [`../tool-access/readme.md`](../tool-access/readme.md) defines tool registration, scoped execution, restricted tool use, and tool execution audit.
- [`../evidence-traceability/readme.md`](../evidence-traceability/readme.md) defines evidence references, finding support, and DFIR evidence handling.
- [`../local-llm-dfir/readme.md`](../local-llm-dfir/readme.md) defines local/private LLM-assisted DFIR evidence and review boundaries.
- [`../audit-replay/readme.md`](../audit-replay/readme.md) defines repository-wide audit event, replayability, correlation, failure audit, and immutable audit expectations.
- [`../agent-governance/readme.md`](../agent-governance/readme.md) defines agent lifecycle, package rollout, rollback, recall, and fleet monitoring expectations.

## Operational Anti-Patterns

Avoid the following:

- routing raw tenant, customer, case, or evidence data into shared intelligence packages;
- treating de-identification as approval;
- treating a sanitized detection pattern, indicator, or agent context package as authorization to execute tools or actions;
- allowing agents to release, widen, or recall shared intelligence without governed workflow controls;
- storing customer-specific context in shared memory, shared vector indexes, shared knowledge stores, prompt packages, or agent packages;
- distributing shared intelligence without owner, version, allowed use, eligible consumer, expiration, rollback, recall, and audit context;
- allowing a package approved for one use to be reused for another use without policy validation;
- publishing customer-derived indicators without source permission, sensitivity review, approval, and expiration handling;
- using intelligence derived from failed, quarantined, disputed, expired, or unauditable ingestion paths;
- deleting or silently overwriting recalled or corrected release records;
- failing open when sanitization, approval, destination, or audit context is missing.

## Acceptance Criteria

This file is acceptable when:

- shared intelligence is clearly separated from raw source records, customer data, tenant data, case records, evidence, analyst notes, and model output;
- sanitization, review, formal approval, policy decision, enforcement, and audit responsibilities remain separate;
- tenant identity and customer identity remain separate in internal provenance records;
- shared intelligence release records define owner, version, allowed use, disallowed use, eligible consumers, destination, retention, expiration, rollback, recall, approval, and audit references;
- customer-derived indicators and patterns cannot be released without source permission, sensitivity handling, allowed-use controls, approval where required, and replayable provenance;
- knowledge stores, vector indexes, shared memory, case memory, and agent context packages cannot receive unapproved or unscoped content;
- agents may propose and consume shared intelligence only within governed scope and may not approve or distribute it independently;
- private/local LLM-assisted DFIR output cannot be released as shared intelligence without examiner review, evidence-aware provenance, sanitization, and approval where required;
- failed, quarantined, disputed, expired, recalled, or unauditable ingestion paths block shared intelligence release;
- audit replay can reconstruct source lineage, sanitization, review, approval, release, distribution, downstream use, correction, rollback, recall, and revocation without exposing raw source data to unauthorized consumers.
