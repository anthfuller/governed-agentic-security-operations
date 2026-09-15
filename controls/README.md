# Normative Control Catalog

The canonical catalog is [`control-catalog.yaml`](control-catalog.yaml). It turns the repository's governance principles into reviewable requirements with stable identifiers, accountable roles, required inputs, expected evidence, failure behavior, verification methods, and implementation references.

The catalog is normative for this repository. Narrative documents are informative unless they cite a `GASO-*` control identifier or explicitly state a normative requirement.

## Identifier Format

Control identifiers use `GASO-<DOMAIN>-NNN`. Domain abbreviations are defined in the catalog and correspond to governance, identity, tenant isolation, policy, approval, tools, evidence, audit, fleet, local-LLM, ingestion, and assurance concerns.

## Validation

```bash
gaso validate controls/control-catalog.yaml
```

Validation confirms schema conformance, unique IDs, valid profile names, and locally resolvable references. It does not prove that an external platform enforces a control.

## Tailoring

Organizations select controls through an implementation profile. Tailoring decisions should be recorded rather than silently deleting requirements. A control that depends on an external product must identify that dependency and the organization must verify it separately.
