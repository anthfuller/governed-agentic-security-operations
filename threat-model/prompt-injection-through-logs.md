# Prompt Injection Through Logs

Logs, alerts, tickets, emails, case notes, command output, and evidence are untrusted data even when collected from an internal system. Embedded text may attempt to redirect an agent, reveal data, or request tools.

## Required Controls

- label source content as data and keep it separate from system and workflow instructions;
- preserve source provenance, tenant scope, and parser version;
- minimize retrieved content and use structured fields where possible;
- never translate free-form content directly into a tool call;
- validate proposed actions through policy, approval, and the external PEP;
- treat generated claims as derived and require source support.

## Fail-Closed Conditions

Block progression when source scope or provenance is missing, instruction and data boundaries cannot be established, output requests an undeclared tool or target, or material claims lack evidence references.

Negative tests should insert hostile instructions into every supported input type and confirm they cannot alter policy, approval, tenant scope, tool parameters, or output destination.

Related controls: `GASO-ING-001`, `GASO-TOL-002`, `GASO-TOL-003`, `GASO-ASR-002`.
