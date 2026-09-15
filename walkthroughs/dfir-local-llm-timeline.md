# Walkthrough: DFIR Local-Model Timeline

## Scenario

A forensic examiner uses a synthetic, isolated local-model workflow to draft a timeline from a declared event-log object. The timeline is derived material and cannot replace or modify the source evidence.

## Governed Path

1. Authorize the case, evidence access, processing purpose, and isolated environment.
2. Register the source object, acquisition context, and integrity value in the evidence manifest.
3. Verify the externally preserved original and provide a controlled read-only analysis view.
4. Produce the draft timeline within declared model, storage, retrieval, telemetry, and egress boundaries.
5. Store the output separately and record lineage to source evidence.
6. Review timestamps, source support, contrary evidence, and limitations.
7. Approve only the stated investigative use; handle external report release separately.
8. Audit stable references and hashes without duplicating protected evidence into the general log.

## Run the Gates

The complete synthetic set is under [`artifacts/dfir-local-llm-timeline/`](artifacts/dfir-local-llm-timeline/). It includes evidence and lineage, assurance limitations, policy and decision, human approval, validate-only case-record request/result, audit events, and expected replay.

```bash
gaso validate profiles/dfir.yaml \
  walkthroughs/artifacts/dfir-local-llm-timeline/*.yaml \
  walkthroughs/artifacts/dfir-local-llm-timeline/expected-replay.json

gaso verify-tenant-scope \
  walkthroughs/artifacts/dfir-local-llm-timeline/evidence-manifest.yaml \
  walkthroughs/artifacts/dfir-local-llm-timeline/timeline-lineage.yaml

gaso verify-evidence-manifest \
  walkthroughs/artifacts/dfir-local-llm-timeline/evidence-manifest.yaml \
  --lineage walkthroughs/artifacts/dfir-local-llm-timeline/timeline-lineage.yaml

gaso evaluate-policy \
  walkthroughs/artifacts/dfir-local-llm-timeline/request.yaml \
  --policy walkthroughs/artifacts/dfir-local-llm-timeline/policy.yaml \
  --approvals walkthroughs/artifacts/dfir-local-llm-timeline/human-approval.yaml

gaso verify-audit-chain \
  walkthroughs/artifacts/dfir-local-llm-timeline/audit-events.jsonl
gaso replay \
  walkthroughs/artifacts/dfir-local-llm-timeline/audit-events.jsonl
```

Expected result: all commands pass and replay reports `external_action_executed: false`. Removing the source evidence reference or changing the lineage scope must fail.

The negative lineage names an evidence object absent from the manifest. This must return `FAIL_CLOSED` with exit `1`:

```bash
gaso verify-evidence-manifest \
  walkthroughs/artifacts/dfir-local-llm-timeline/evidence-manifest.yaml \
  --lineage \
  walkthroughs/artifacts/dfir-local-llm-timeline/negative/timeline-lineage-unknown-source.yaml
```

The automated assertion is in [`../tests/test_walkthroughs.py`](../tests/test_walkthroughs.py).

## Production Boundary

The declared hashes are synthetic. The repository does not read the evidence object, run a model, prove isolation, establish chain of custody, or decide forensic/legal sufficiency. Those require the organization's evidence repository, access controls, isolated compute and network enforcement, qualified reviewers, case procedure, and durable audit system.

Related controls: `GASO-EVD-001` through `003`, `GASO-LLM-001` through `003`, `GASO-AUD-003`. Profile: [`../profiles/dfir.yaml`](../profiles/dfir.yaml).
