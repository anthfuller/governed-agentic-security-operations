# Implementation Profiles

Profiles select and specialize the shared control catalog for a service context. They do not copy the full text of each control.

- [`mssp.yaml`](mssp.yaml) covers multi-tenant managed security operations.
- [`mdr.yaml`](mdr.yaml) covers managed detection and response.
- [`dfir.yaml`](dfir.yaml) covers digital forensics and incident response, including conditional private/local-LLM use.

Validate a profile with:

```bash
gaso validate profiles/mssp.yaml
```

A valid profile states which controls apply, who is accountable, which actions are prohibited, which approvals and artifacts are required, what conformance tests must pass, and which external systems must enforce behavior beyond this repository.
