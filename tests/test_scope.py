from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from gaso.errors import ConformanceError
from gaso.scope import verify_scopes

ROOT = Path(__file__).resolve().parents[1]


def artifact(name: str):
    return yaml.safe_load((ROOT / "templates" / name).read_text())


def test_matching_request_and_approvals_pass():
    values = [("request", artifact("governed-action-request.yaml")), ("human", artifact("human-approval-record.yaml")), ("customer", artifact("customer-approval-record.yaml"))]
    scope = verify_scopes(values)
    assert scope["tenant_id"] == "tenant-example-001"


def test_cross_tenant_approval_fails_closed():
    request = artifact("governed-action-request.yaml")
    approval = deepcopy(artifact("human-approval-record.yaml"))
    approval["scope"]["tenant_id"] = "tenant-example-002"
    with pytest.raises(ConformanceError, match="scope differs"):
        verify_scopes([("request", request), ("approval", approval)])


def test_target_must_be_declared_in_scope():
    request = artifact("governed-action-request.yaml")
    request["target_id"] = "host-example-999"
    with pytest.raises(ConformanceError, match="target_id"):
        verify_scopes([("request", request)])
