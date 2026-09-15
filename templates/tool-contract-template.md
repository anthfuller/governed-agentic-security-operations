# Tool Contract Template

Use a tool contract to register the allowed operations and parameters for one versioned tool interface.

For each operation, record its risk class, required approvals, and allowed parameter names. Record the scope dimensions and prohibited uses. The external-enforcement field must identify where authorization and parameter enforcement actually occur.

Validate [`tool-contract.yaml`](tool-contract.yaml) with `gaso validate`. Registration means the tool is known; it does not authorize any invocation.
