# Evidence Manifest Template

Use the manifest to identify evidence objects without embedding evidence in the repository. Record object type, source, SHA-256 value, acquisition time, and custodian role. Bind the manifest to the applicable customer, tenant, case, and environment.

Derived material must be listed separately and documented with a derived-artifact lineage record. A manifest does not prove that acquisition was forensically sound or that an object is admissible.

Validate [`evidence-manifest.yaml`](evidence-manifest.yaml) with:

```bash
gaso verify-evidence-manifest templates/evidence-manifest.yaml
```
