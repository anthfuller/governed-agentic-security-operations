from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from gaso.errors import ConformanceError
from gaso.schema_store import SchemaStore

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    return yaml.safe_load((ROOT / "templates" / name).read_text())


def test_release_and_recall_records_validate():
    store = SchemaStore(ROOT / "schemas")
    store.validate(load("fleet-release-manifest.yaml"), "release")
    store.validate(load("fleet-recall-record.yaml"), "recall")


def test_release_without_rollback_target_is_rejected():
    release = deepcopy(load("fleet-release-manifest.yaml"))
    del release["rollback_target"]
    with pytest.raises(ConformanceError, match="rollback_target"):
        SchemaStore(ROOT / "schemas").validate(release, "release without rollback")


def test_recall_scope_cannot_be_empty():
    recall = deepcopy(load("fleet-recall-record.yaml"))
    recall["scope"] = {}
    with pytest.raises(ConformanceError):
        SchemaStore(ROOT / "schemas").validate(recall, "unbounded recall")
