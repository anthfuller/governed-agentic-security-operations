# Human Approval Record Template

Use this record for formal human authorization after review. A review note, analyst recommendation, model result, or assurance result is not an approval.

The record must bind the approver, role, request, policy decision, exact actions, scope, conditions, and validity period. The approver must be a human identity with authority for the requested action. `request_digest` is the SHA-256 value of the canonical request body (UTF-8 JSON with sorted keys and compact separators), so an allowed parameter or other request field cannot change after approval.

Validate [`human-approval-record.yaml`](human-approval-record.yaml) with `gaso validate`. Use `gaso evaluate-policy` to confirm that required approval types and scope match the request.

The record is a synthetic reference. Production approval identity, authorization, revocation, and non-repudiation require an external approval system.
