import json
from pathlib import Path

from gaso.cli import main

ROOT = Path(__file__).resolve().parents[1]


def test_cli_success_exit_and_json_output(capsys, monkeypatch):
    monkeypatch.chdir(ROOT)
    exit_code = main(["validate", "templates/agent-card.yaml", "--format", "json"])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload["status"] == "PASS"
    assert payload["external_action_executed"] is False


def test_cli_conformance_block_uses_exit_one(capsys, monkeypatch):
    monkeypatch.chdir(ROOT)
    exit_code = main(
        [
            "evaluate-policy",
            "walkthroughs/artifacts/mssp-endpoint-isolation/negative/request-target-mismatch.yaml",
            "--policy",
            "walkthroughs/artifacts/mssp-endpoint-isolation/policy.yaml",
            "--format",
            "json",
        ]
    )
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 1
    assert payload["status"] == "FAIL_CLOSED"
    assert payload["external_action_executed"] is False


def test_cli_usage_or_configuration_error_uses_exit_two(capsys, monkeypatch):
    monkeypatch.chdir(ROOT)
    exit_code = main(["validate", "missing-artifact.yaml", "--format", "json"])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 2
    assert payload["status"] == "ERROR"
    assert payload["external_action_executed"] is False
