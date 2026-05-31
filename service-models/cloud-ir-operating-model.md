# Cloud IR Operating Model

## Purpose

This file defines the **Cloud Incident Response (Cloud IR) operating model** for the **Agentic MSSP / MDR / DFIR Security Operations Architecture**.

The Cloud IR operating model describes how agentic assistance can support cloud incident investigation, identity compromise response, workload containment, cloud control-plane analysis, approval package preparation, and evidence-aware escalation without granting agents autonomous authority over customer cloud environments.

This file is an operating model, not a vendor-specific engineering design.

## Service Scope

The Cloud IR service model supports cloud-focused incident response across cloud identity, cloud control plane, workloads, SaaS integrations, storage, logging, and cloud-native security telemetry.

| Area | In Scope |
|---|---|
| Cloud IAM compromise | Investigation and response preparation for suspicious sign-ins, token misuse, OAuth abuse, privilege escalation, role changes, or administrative activity. |
| Cloud workload compromise | Investigation and response preparation for compromised compute, containers, serverless workloads, images, keys, secrets, or workloads. |
| Cloud control-plane abuse | Review of suspicious API activity, policy changes, audit logs, resource creation, data access, and privilege changes. |
| Cloud containment preparation | Approval package preparation for session revocation, credential reset, key rotation, resource quarantine, network restriction, role removal, or policy rollback. Approval package must include blast-radius analysis before human review. |
| Cloud evidence handling | Preservation and review of logs, snapshots, audit trails, configuration state, cloud metadata, and derived timeline artifacts where applicable. |
| Escalation | Handoff to DFIR or Private / Local LLM-assisted DFIR when evidence preservation, forensic timeline reconstruction, or local analysis is required. |

## Out of Scope

| Area | Out-of-Scope Boundary |
|---|---|
| Autonomous cloud response | Agents must not revoke sessions, reset credentials, disable identities, delete resources, rotate keys, change policy, isolate workloads, or modify customer environments without approved authority. |
| Unscoped cloud access | Agents must not retrieve or act outside authorized tenant, customer, cloud account/subscription/project, incident, workload, identity, or evidence scope. |
| Broad cloud policy changes | Agents may draft recommendations, but broad IAM, network, logging, or security policy changes require review and approved change path. |
| Final customer communication | Agents may draft customer summaries, but release requires review and customer authorization where required. |
| Final forensic conclusion | Cloud IR workflows must not make final forensic conclusions unless escalated into DFIR with evidence handling controls. |
| Local/private forensic AI analysis | Private / Local LLM-assisted DFIR applies only when cloud evidence or artifacts are analyzed in a local, isolated, or customer-controlled AI environment. |

## Operating Principles

| Principle | Required Behavior |
|---|---|
| Cloud account scope | Every workflow must be bound to customer, tenant, cloud account/subscription/project, incident, and workflow scope. |
| Identity-first control | Privileged identity and token actions require explicit approval and enforcement. |
| Agent as assistant | Agents may investigate, summarize, recommend, and prepare approval context, but must not execute cloud response actions. |
| Policy before response | Cloud API calls, tool execution, account changes, output release, or workflow state changes must pass policy where required. |
| PEP at cloud boundary | Enforcement must occur at cloud API gateways, tool wrappers, workflow orchestrators, retrieval gateways, and output publishing controls. |
| Customer authorization | Customer-impacting cloud changes require customer authorization where required by service agreement or impact. |
| Evidence-aware response | If cloud logs, snapshots, images, or audit data become evidence, preserve provenance and escalate to DFIR where required. |
| Fail closed | Missing scope, policy, approval, customer authorization, or output destination must block execution or return for clarification. |
| Audit and replay | Requests, context, policy decisions, approvals, cloud actions, and results must be reconstructable. |

## Cloud IR Workflow Classes

| Workflow Class | Agentic Assistance Allowed | Approval Required? | Notes |
|---|---|---|---|
| Cloud alert investigation | Yes | Usually no for read-only scoped analysis | Must remain customer and cloud-account scoped. |
| Cloud IAM risk assessment | Yes | No for recommendation; yes before action | Identity actions require approval before execution. |
| Cloud audit log review | Yes | Usually no if read-only and scoped | Retrieval must preserve source and time scope. |
| Session or token revocation preparation | Yes | Yes | Requires approval and authorized response path. |
| Credential reset or key rotation preparation | Yes | Yes | Customer authorization may be required. |
| OAuth grant or app consent removal preparation | Yes | Yes | Scope must be limited to approved grant or application. |
| Workload isolation preparation | Yes | Yes | May affect production systems; recommendation must include blast-radius analysis. |
| Cloud policy rollback recommendation | Yes | Yes before change | Requires change authority and rollback path. |
| Cloud evidence preservation | Yes | Yes if evidence workflow begins | Escalate to DFIR if chain of custody applies. |
| Customer report draft | Yes | Yes before release | Customer-facing output requires review and authorization where required. |

## Roles and Responsibilities

| Role | Responsibility | Must Not Do |
|---|---|---|
| Cloud IR Analyst | Validate cloud context, review recommendations, approve scoped actions within authority, and escalate when required. | Execute high-impact response solely from agent output. |
| Cloud IR Lead | Own response coordination, cloud containment decisioning, customer authorization path, and escalation to DFIR. | Bypass customer, policy, or evidence controls. |
| Agentic Workflow | Summarize cloud signals, correlate identity/resource activity, draft recommendations, identify uncertainty, and prepare approval packages. | Execute cloud API changes, approve itself, notify customers, or access unrelated customer environments. |
| Agent Orchestrator | Route agent requests through workflow policy, retrieve short-lived credentials from a policy-scoped credential broker, and bind execution to tenant, customer, cloud account, incident, and approval scope. | Store persistent static cloud keys, bypass credential broker, reuse credentials across customers, or inject credentials without PDP/PEP authorization. |
| PDP | Decide whether cloud action is allowed, denied, restricted, approval-required, clarification-required, or escalation-required. | Enforce directly without a PEP. |
| PEP | Enforce decisions at workflow, cloud API, tool, retrieval, evidence, ticketing, and output boundaries. | Permit execution if scope, approval, or customer authorization is missing. |
| Customer Approver | Authorize customer-impacting cloud actions where required. | Be bypassed by internal approval. |
| DFIR Lead | Own evidence handling if cloud response becomes formal forensic investigation. | Treat Cloud IR triage output as final forensic conclusion. |
| Audit / Assurance | Preserve traceability, evaluate enforcement, and support replay. | Depend only on narrative notes without structured identifiers. |

## Agentic Assistance Boundaries

| Agent May | Agent Must Not |
|---|---|
| Summarize cloud IAM and workload signals. | Execute cloud response actions. |
| Correlate cloud logs, identity activity, workload events, and threat context. | Retrieve data across unrelated customers or cloud accounts. |
| Draft response recommendations. | Revoke sessions, reset credentials, rotate secrets, or remove grants. |
| Prepare approval packages. | Approve or reuse approvals. |
| Identify uncertainty and missing context. | Present hypotheses as confirmed findings. |
| Suggest DFIR escalation. | Start evidence transfer or preservation without approved workflow. |
| Draft customer summary. | Release customer-facing communication. |

## Blast-Radius Analysis Requirement

Cloud IR containment recommendations must include a blast-radius analysis before human review.

| If Agent Recommends | Then Output Must Include |
|---|---|
| Identity action | Affected identity, role, session, token, OAuth grant, downstream access impact, and customer scope based on current `tenant_id` and cloud account scope. |
| Workload action | Target workload, resource group/project/subscription, dependent services, production impact, recovery path, and customer scope based on current `tenant_id`. |
| Data access or export action | Data classification, sensitivity label, storage location, residency constraint, evidence impact, and transfer authorization requirement. |
| Policy or configuration change | Target policy, affected resources, rollback path, owner approval, and multi-tenant or multi-customer impact check. |
| Customer-facing communication | Audience, release destination, customer authorization requirement, and unsupported-claim check. |

Blast-radius analysis must categorize impact as one or more of: **identity**, **data**, **workload**, **network**, **policy/configuration**, **customer communication**, or **evidence**. Missing blast-radius analysis must route the workflow to clarification or fail closed.

## Policy and Enforcement Points

Service owners must map the PDP / PEP boundaries defined in this operating model to specific infrastructure components in their deployment guide, such as cloud API gateways, workflow orchestrators, tool wrappers, retrieval gateways, evidence stores, ticket connectors, approval systems, and output publishing controls.

| Boundary | PDP Decision Required When | PEP Enforcement Location |
|---|---|---|
| Cloud telemetry retrieval | Cloud logs, identity data, audit records, resource metadata, or SaaS context are retrieved. | Retrieval gateway or cloud telemetry connector. |
| Cloud tool use | Agent or workflow requests a cloud API, script, connector, CLI, automation, or playbook. | Cloud tool wrapper, API gateway, or orchestrator. |
| Identity action | Session revocation, credential reset, account disablement, role removal, OAuth grant removal, or token action is proposed. | Identity API gateway or IAM tool PEP. |
| Workload action | Isolation, quarantine, snapshot, network restriction, shutdown, image capture, or tag change is proposed. | Cloud workload tool PEP. |
| Policy or configuration change | IAM, network, logging, security, storage, or detection configuration change is proposed. | Change workflow, CI/CD gate, or policy deployment PEP. |
| Evidence preservation | Logs, snapshots, exports, or artifacts are preserved or transferred. | Evidence store, data movement PEP, or DFIR handoff workflow. |
| Customer-facing output | Report, recommendation, notification, or summary may be released externally. | Output publishing layer. |
| Escalation | Workflow moves to DFIR, Private / Local LLM-assisted DFIR, MDR, or incident command. | Workflow orchestrator. |

## Credential Brokerage Requirements

Cloud IR workflows must not rely on persistent static keys for agent or tool execution.

| If Credentialed Cloud Access Is Required | Then Require |
|---|---|
| Agent or workflow needs cloud API access. | Retrieve short-lived credentials from a policy-scoped credential broker. |
| Customer-specific access is required. | Bind credential issuance to `tenant_id`, `customer_id`, cloud account/subscription/project, workflow, approval record, and expiration. |
| Privileged action is requested. | Credential broker must verify PDP decision, approval record, customer authorization where required, and PEP enforcement path. |
| Credential scope cannot be proven. | Deny credential issuance and emit audit event. |
| Credential is issued. | Record broker reference, credential scope, expiration, requester, approval record, and audit reference. |

Acceptable broker patterns include a dedicated secrets broker, short-lived cloud-native role assumption, managed identity, workload identity federation, or vault-backed credential issuance. Static long-lived cloud keys are not an authorized response path.

## Human Approval Gates

| If This Occurs | Then Require |
|---|---|
| Recommendation includes session revocation, credential reset, account disablement, token revocation, key rotation, or OAuth grant removal. | Human approval before execution; customer authorization where required. |
| Recommendation changes IAM, network, logging, storage, detection, or cloud security policy. | Human approval, change owner review, and approved response path. |
| Recommendation may disrupt production workloads. | Human approval and customer authorization assessment. |
| Recommendation involves snapshot, image capture, evidence export, or log preservation. | DFIR/evidence handling review where required. |
| Cloud evidence is needed for formal findings or legal-sensitive review. | Escalation to DFIR operating model. |
| Local/private analysis of cloud evidence is required. | Escalation to Private / Local LLM-assisted DFIR operating model. |
| Customer-facing communication is drafted. | Review and release approval before publication. |
| Incident closure is proposed. | Human-controlled closure decision with audit-linked rationale. |
| Scope is ambiguous across tenant, customer, cloud account, identity, resource, or incident. | Return for clarification or fail closed. |

## Customer Authorization Gates

| Customer Authorization Required When | Enforcement Requirement |
|---|---|
| Cloud identity state changes. | IAM tool PEP must verify authorization and scope. |
| Cloud workload state changes. | Workload PEP must verify customer authorization and impact assessment. |
| Cloud policy or configuration changes. | Change workflow must include customer authorization where required. |
| Customer notification is sent. | Output PEP must block release without authorization reference. |
| Evidence, logs, snapshots, or cloud artifacts are exported or transferred. | Evidence/data movement PEP must verify authorization. |
| Customer contract defines response authority. | Workflow must enforce contract-specific authorization path. |
| Production-impacting containment is recommended. | Workflow PEP must require authorization before action. |

## Cloud Data Boundary Enforcement

| Boundary | Required Control |
|---|---|
| Tenant | Requests must carry `tenant_id`; missing or mismatched tenant fails closed. |
| Customer | Requests must carry `customer_id`; cross-customer access is denied and audited. |
| Cloud account / subscription / project | Requests must identify the exact cloud scope; broad cloud access is denied by default. |
| Region / data residency | Workflows must preserve customer-approved region and data residency constraints. |
| Identity | Identity actions must name target identity and approved action scope. |
| Workload / resource | Workload actions must name target resource and approved action scope. |
| Incident / case | Incident and case identifiers must be present for incident-scoped workflows. |
| Evidence | Evidence object identifiers are required when evidence preservation or DFIR handling begins. |
| Output destination | Destination must be declared before write, release, export, or transfer. |
| Classification | Data classification and sensitivity label must persist through workflow state. |

## Retrieval and Memory Rules

| If | Then |
|---|---|
| Cloud logs are retrieved. | Restrict retrieval to customer, cloud account, incident, and time window. |
| IAM context is retrieved. | Restrict to affected identities, roles, applications, sessions, and approved scope. |
| Resource context is retrieved. | Restrict to affected resource group, project, account, workload, or asset scope. |
| Case memory influences recommendation. | Validate customer, cloud account, incident, and freshness before prompt assembly. |
| Shared threat context is retrieved. | Confirm it is approved reference context and not customer data from another tenant. |
| Persistent memory write is requested. | Deny by default unless policy, owner, retention, and approval are present. |
| Retrieved context crosses customer or cloud account boundary. | Deny, quarantine, and audit. |
| Retrieval supports customer-facing output. | Preserve source references and require release review. |

## Cloud Sensitive Action Handling

Cloud IR workflows may recommend sensitive response actions, but they must not execute them without approval and enforcement.

An **authorized response path** means the response action is executed only through a documented, approved, and replayable workflow. For enterprise use, the response path should be represented as an **idempotent workflow** or **signed playbook** that defines the allowed action, target cloud scope, required approvals, customer authorization requirements, PEP enforcement point, rollback or recovery expectation where applicable, and audit fields.

Every state-changing cloud action must record a **before-state reference** and **after-state reference** in the audit log. The before-state reference must capture the relevant identity, workload, policy, grant, key, session, or resource state before execution. The after-state reference must confirm the resulting state after execution or record partial failure.

| Sensitive Action | Cloud IR Agent Output Allowed | Execution Allowed? |
|---|---:|---:|
| Session revocation | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| Credential reset | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| Account disablement | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| OAuth grant removal | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| Key or secret rotation | Recommendation and approval package | Only after approval, impact review, and authorized response path. |
| Workload isolation | Recommendation and approval package | Only after approval, customer authorization where required, and authorized response path. |
| Cloud policy rollback | Draft change only | Only through change owner review and deployment gate. |
| Snapshot or evidence preservation | Recommendation only | Requires evidence handling approval and audit linkage. |
| Customer notification | Draft only | Only after release approval and customer authorization where required. |
| Incident closure | Draft recommendation only | Human-controlled workflow decision required with audit-linked closure rationale. |

## Cloud Evidence Handling

| If This Occurs | Then Require |
|---|---|
| Cloud logs are preserved for investigation. | Record source, time range, export method, hash where applicable, and custody reference. |
| Snapshot, disk image, memory artifact, or workload image is captured. | Escalate to DFIR or evidence-handling workflow. |
| Cloud audit logs are exported. | Preserve source system, query, time range, output destination, and audit reference. |
| Evidence leaves customer-controlled environment. | Customer authorization and evidence transfer record required. |
| Timeline reconstruction begins. | Use DFIR operating model and evidence manifest if formal forensic timeline is required. |
| Local/private AI analysis is used over evidence. | Use Private / Local LLM-assisted DFIR operating model. |
| Agent produces forensic interpretation. | Require analyst validation before findings or report use. |

## Cloud Policy and Configuration Changes

| If Agent Proposes | Then Require |
|---|---|
| IAM policy change | Cloud owner review, impact assessment, approval, and rollback plan. |
| Conditional access or access policy change | Identity owner approval and staged deployment path. |
| Network security rule change | Cloud/network owner approval and impact review. |
| Logging configuration change | Security logging owner approval; ensure no audit gap is introduced. |
| Storage access change | Data owner approval and sensitivity review. |
| Detection or alert rule change | Detection owner review, test evidence, and deployment gate. |
| Multi-customer policy change | Service lead approval and tenant impact review. |

## Escalation Paths

| Condition | Escalate To | Reason |
|---|---|---|
| Active identity compromise requiring response coordination | MDR / SOC Incident Lead | Response coordination and containment approval required. |
| Cloud resource compromise with production impact | Cloud IR Lead / customer approver | Cloud containment may disrupt business operations. |
| Evidence preservation, snapshot, forensic timeline, malware analysis, or chain-of-custody required | DFIR | Formal forensic workflow required. |
| Cloud evidence cannot leave customer-controlled environment | Private / Local LLM-assisted DFIR | Local/private forensic AI workflow required. |
| Customer-impacting action required | Customer approver / service lead | Customer authority or contract-specific approval required. |
| Broad cloud policy or architecture risk found | Cloud security owner / governance approver | Risk may require architecture or configuration change. |
| Policy exception required | Governance approver / service owner | Exception must be explicitly approved and logged. |

## Audit and Replay Requirements

Cloud IR workflows should emit or preserve:

- request identifier;
- correlation identifier;
- audit reference identifier — this **MUST** match the audit reference identifier used in the related `example-audit-event.json` structure so the request, decision, approval, enforcement, execution result, and final workflow state remain linked;
- tenant and customer identifiers;
- cloud account, subscription, or project identifier;
- incident and case identifiers where applicable;
- identity, workload, resource, or policy identifiers where applicable;
- workflow identifier;
- agent identifier;
- requester identity;
- retrieved context references where used;
- cloud query or export scope where applicable;
- proposed action;
- policy decision;
- approval record where required;
- customer authorization reference where required;
- tool invocation record where applicable;
- execution result where action is authorized;
- before-state reference for every state-changing cloud action;
- after-state reference for every state-changing cloud action;
- evidence object identifiers where evidence handling begins;
- output destination;
- final workflow state;
- deny, clarification, escalation, or fail-closed reason where applicable.

## Fail-Closed Rules

| Failure Condition | Required Behavior |
|---|---|
| Missing `tenant_id` or `customer_id` | Fail closed. |
| Missing cloud account, subscription, project, or environment scope | Return for clarification or fail closed. |
| Affected identity or resource missing for response action | Return for clarification before action. |
| Customer context mismatch | Deny and audit. |
| Retrieval returns cross-customer or cross-cloud-account context | Deny, quarantine result, and audit. |
| Policy unavailable | Fail closed. |
| Approval required but missing | Block action and route for approval. |
| Customer authorization required but missing | Block customer-impacting action. |
| Output destination missing or unauthorized | Block write or release. |
| Agent requests prohibited cloud API action | Deny and audit. |
| Evidence handling begins without evidence scope | Escalate to DFIR or fail closed. |
| Cloud policy change lacks owner approval | Block deployment. |
| Evidence export lacks authorization | Block export and audit. |

## Relationship to Examples

| Example | Cloud IR Relevance |
|---|---|
| [`cloud-iam-compromise`](../examples/cloud-iam-compromise/) | Primary Cloud IR example for IAM compromise, approval-controlled response, customer authorization, and PEP enforcement. |
| [`alert-triage-to-recommendation`](../examples/alert-triage-to-recommendation/) | Applies when alert triage escalates into cloud-specific incident response. |
| [`local-llm-forensic-timeline`](../examples/local-llm-forensic-timeline/) | Applies when cloud incident response escalates into DFIR timeline work or local/private forensic analysis. |

## Relationship to Patterns

| Pattern | Cloud IR Usage |
|---|---|
| [`governed-agentic-security-operations-pattern.md`](../patterns/governed-agentic-security-operations-pattern.md) | Baseline for scoped, policy-gated, auditable Cloud IR workflows. |
| [`policy-enforced-tool-use-pattern.md`](../patterns/policy-enforced-tool-use-pattern.md) | Applies to cloud APIs, IAM tools, scripts, connectors, response automation, and output writes. |
| [`human-approved-sensitive-action-pattern.md`](../patterns/human-approved-sensitive-action-pattern.md) | Applies to cloud containment, IAM actions, policy changes, evidence export, customer notification, and incident closure. |
| [`tenant-safe-rag-memory-pattern.md`](../patterns/tenant-safe-rag-memory-pattern.md) | Applies to cloud logs, identity context, resource context, case memory, and retrieved cloud evidence support. |
| [`private-local-llm-dfir-pattern.md`](../patterns/private-local-llm-dfir-pattern.md) | Applies only when cloud evidence is analyzed in local/private forensic environments. |

Service owners must map these pattern requirements to deployment-specific cloud controls, policies, tests, tool wrappers, approval workflows, and runbooks before implementation.

## Acceptance Criteria

A Cloud IR agentic operating workflow is acceptable when:

- every workflow is bound to tenant, customer, cloud account/subscription/project, incident, and workflow scope;
- target identity, workload, resource, or policy scope is present before response action;
- agent output is treated as recommendation or approval support, not execution authority;
- policy is evaluated before cloud API calls, tool use, response action, ticket write, evidence export, or output release where required;
- PEP enforcement exists at the actual cloud, workflow, retrieval, evidence, or output boundary;
- sensitive cloud actions require human approval;
- customer-impacting actions require customer authorization where applicable;
- response actions execute only through authorized response paths;
- containment recommendations include blast-radius analysis before human review;
- credentialed tool execution uses policy-scoped, short-lived credential brokerage rather than persistent static keys;
- state-changing cloud actions record before-state and after-state references;
- retrieval and memory are scoped and auditable where used;
- cloud evidence preservation escalates to DFIR when required;
- customer-facing outputs are reviewed before release;
- denied or uncertain workflows fail closed or return for clarification;
- audit records support reconstruction.

## Non-Goals

This operating model does not:

- define a specific cloud provider implementation;
- replace customer cloud operations authority;
- require every Cloud IR workflow to be agentic;
- allow agents to perform autonomous cloud containment or remediation;
- replace human analysts, cloud incident leads, service owners, or customer authority;
- replace customer contracts or authorization requirements;
- replace DFIR evidence handling;
- claim that AI recommendations are authoritative without review;
- permit final forensic conclusions without DFIR controls.

## Summary

The Cloud IR operating model defines how agentic assistance can support cloud incident investigation and response preparation while preserving customer scope, cloud account boundaries, policy enforcement, human approval, customer authorization, evidence integrity where applicable, and auditability.

The core principle is:

> Cloud IR agents may investigate, correlate, summarize, recommend, and prepare approval packages, but they must not execute cloud response actions, alter customer environments, release customer-facing outputs, or handle evidence outside governed scope.
