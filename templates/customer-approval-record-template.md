# Customer Approval Record Template

Use this record when a service agreement or action class retains customer authorization. Customer approval is separate from internal MSSP or MDR review and approval.

The record must bind the customer approver, canonical request digest, policy decision, exact action and target, customer and tenant scope, conditions, and validity period. It must not be reused for another customer, tenant, target, request body, or policy version.

Validate [`customer-approval-record.yaml`](customer-approval-record.yaml) with `gaso validate`. The repository does not verify that the named approver has real contractual authority; that remains an external control.
