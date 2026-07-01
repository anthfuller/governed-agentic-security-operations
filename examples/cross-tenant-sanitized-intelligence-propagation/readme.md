# Cross-Tenant Sanitized Intelligence Propagation

This example models a governed release path for sanitized defensive intelligence derived from one tenant-bound cloud identity investigation and delivered only to eligible recipient tenant scopes.

The records show how a release request, sanitization review, policy decision, and release audit event preserve source boundaries while allowing reusable defensive intelligence to move through approved tenant-scoped security operations channels. The released package excludes raw evidence, source customer identifiers, source tenant and case context, secrets, tenant-specific values, model prompts, and agent memory.

## Files

| File | Purpose |
| --- | --- |
| [`example-sanitized-intelligence-release-request.json`](./example-sanitized-intelligence-release-request.json) | Candidate release request for policy evaluation. Records the source investigation reference, candidate recipients, sanitized package references, required downstream gates, boundary expectations, and actions not authorized by the request. |
| [`example-sanitization-review-record.json`](./example-sanitization-review-record.json) | Sanitization review record. Validates that the candidate package and manifest passed required absence checks before policy evaluation and records review attestations used by the release path. |
| [`example-release-policy-decision.json`](./example-release-policy-decision.json) | Policy decision record. Records the policy decision point result, allowed recipient scope, excluded recipients, authorized channels, release conditions, fail-closed requirements, and actions denied by policy. |
| [`example-release-audit-event.json`](./example-release-audit-event.json) | Final release audit event. Records release execution, recipient delivery results, boundary validation, evidence preservation, denied actions, and replayable outcome facts. |

## Scenario summary

A cloud identity investigation in `tenant-alpha-prod` produces a generalized behavioral pattern for OAuth consent abuse, token replay, directory enumeration, and service principal credential manipulation. The intelligence package is prepared as sanitized defensive intelligence for evaluation against candidate recipients.

The release request includes `tenant-bravo-prod`, `tenant-charlie-prod`, and `tenant-delta-prod` as candidate recipients. Candidate scope is not approval. The policy decision reduces the recipient set to eligible tenants only: `tenant-bravo-prod` and `tenant-charlie-prod`. `tenant-alpha-prod` is excluded because it is the originating tenant, and `tenant-delta-prod` is denied because the required service exposure eligibility check fails.

Authorized release channels are limited to:

- `tenant_scoped_intelligence_feed`
- `tenant_scoped_detection_content_queue`
- `soc_triage_context_enrichment_feed`

The release does not authorize customer notification, raw evidence release, source context release, source identifier release, recipient access to the source case, recipient-to-recipient data sharing, automated customer-environment containment or remediation, policy exceptions, scope expansion, model training, or model fine-tuning.

## Governed sequence

1. `example-sanitized-intelligence-release-request.json` records the candidate release request. The request state is `approved_for_policy_evaluation`; it does not authorize delivery.
2. `example-sanitization-review-record.json` records sanitization review results for the candidate package. The review verifies package and manifest hashes, confirms required fields were removed or generalized, and verifies that recipient adaptation cannot reintroduce source values.
3. `example-release-policy-decision.json` records an `allow_with_conditions` decision from the cross-tenant intelligence policy decision point. The decision locks allowed recipients, authorized channels, release conditions, and fail-closed behavior.
4. `example-release-audit-event.json` records release execution after the required policy and human review gates. It records evidence preservation, immutable package commitment, delivery to approved tenant-scoped feeds, detection-content queueing, sanitized context update, and release receipts.

## Boundary model

The source investigation remains internal to the originating tenant scope. Source evidence is referenced for audit and replay but is not copied into the release package. Recipient tenants receive only approved sanitized payload references and tenant-adaptable detection content.

The release request includes expected memory boundary references for the source case and all candidate recipients because recipient eligibility has not yet been decided at request time. The policy decision and final audit event narrow memory and delivery scope to the approved recipient tenants only.

Recipient adaptation must use recipient-local values only. Recipient agent context is limited to sanitized intelligence and cannot retrieve source case memory. Source tenant, source customer, source case, raw logs, case notes, tokens, secrets, prompts, tool-call arguments, and agent runtime memory are excluded from the payload.

## Policy controls represented

| Control area | Representation |
| --- | --- |
| Sanitization before policy | The policy decision requires a passed sanitization review for the reviewed package and manifest hashes. |
| Candidate scope versus approved scope | The request lists candidate tenants; the policy decision locks approved tenants and excludes ineligible tenants. |
| Policy decision versus enforcement | The policy decision record captures the decision point outcome. The release audit event records enforcement, delivery, and receipt results. |
| Human oversight | Human release review is required before delivery and is reflected through review attestations and approval references in the release path. |
| Fail-closed behavior | Missing correlation fields, failed sanitization, payload mismatch, source identifiers, secrets, model memory, expired decisions, unavailable audit logging, or scope expansion deny release progression or delivery. |
| Evidence handling | Evidence is preserved by immutable reference only; audit records are append-only and retained under the declared security audit retention class. |

## Recipient and memory scope

| Stage | Scope result |
| --- | --- |
| Release request | Bravo, Charlie, and Delta are candidate recipients only. The request does not decide eligibility. |
| Request memory boundary expectation | Source case boundary plus Bravo, Charlie, and Delta candidate recipient boundaries are expected. |
| Policy decision | Bravo and Charlie are allowed. Alpha is excluded as the source tenant. Delta is denied because the service exposure eligibility check fails. |
| Release audit event | Delivery occurs only to Bravo and Charlie. Alpha and Delta receive no release package. |

## Replay expectations

Together, the JSON records allow deterministic reconstruction of:

- why the sanitized intelligence release was requested;
- which source tenant, customer, case, workflow, and detection produced the candidate intelligence;
- which package, payload, and manifest hashes were reviewed and released;
- which fields were removed or generalized before release;
- which recipients were requested, approved, denied, or excluded;
- which policy decision and review gates controlled delivery;
- which release actions executed and which actions were explicitly denied;
- whether source identifiers, raw evidence, secrets, tenant-specific values, and model memory were excluded from the released payload;
- whether tenant, customer, evidence, and memory boundaries held during delivery.

## Key identifiers

| Identifier | Value |
| --- | --- |
| Correlation ID | `corr-cross-tenant-sanitized-intel-0001` |
| Release request ID | `release-req-sanitized-intel-0001` |
| Sanitization review record ID | `sanitization-review-record-0001` |
| Policy decision ID | `release-policy-decision-0001` |
| Release package ID | `sanitized-intel-package-cloud-iam-oauth-abuse-0001` |
| Release execution ID | `release-execution-sanitized-intel-0001` |
| Source case ID | `case-cloud-iam-0031` |
| Source workflow ID | `workflow-cloud-iam-investigation-0031` |
| Source detection ID | `detection-cloud-iam-oauth-abuse-0007` |

## Integrity invariants

| Invariant | Expected result |
| --- | --- |
| Release request authorizes delivery | `false` |
| Sanitization review required before policy decision | `true` |
| Policy decision required before delivery | `true` |
| Human review required before delivery | `true` |
| Raw evidence released | `false` |
| Source identifiers visible to recipients | `false` |
| Secrets or token material released | `false` |
| Model prompt or agent memory released | `false` |
| Recipient access to source case allowed | `false` |
| Customer notification authorized | `false` |
| Automated customer-environment action authorized | `false` |
| Model training or fine-tuning authorized | `false` |
| Recipient scope expansion allowed without new policy decision | `false` |
| Audit records append-only | `true` |

Each JSON record uses `json_sorted_keys_compact` canonicalization and excludes only `record_hash_reference` from its declared record hash scope. Correlation IDs, artifact filenames, package identifiers, payload hashes, manifest hashes, recipient scope, and audit references are intentionally repeated across records so replay can detect missing, mismatched, or tampered inputs.
