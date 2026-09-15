import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
import pytest

from gaso.errors import ConformanceError
from gaso.schema_store import SchemaStore

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path):
    return json.loads(path.read_text()) if path.suffix == ".json" else yaml.safe_load(path.read_text())


def test_all_schemas_are_valid():
    for path in (ROOT / "schemas").glob("*.schema.json"):
        Draft202012Validator.check_schema(json.loads(path.read_text()))


def test_all_machine_readable_repository_artifacts_validate():
    store = SchemaStore(ROOT / "schemas")
    paths = [ROOT / "controls" / "control-catalog.yaml"]
    paths.extend((ROOT / "profiles").glob("*.yaml"))
    paths.extend((ROOT / "templates").glob("*.yaml"))
    paths.extend((ROOT / "policies").glob("*.yaml"))
    paths.extend((ROOT / "examples").rglob("*.json"))
    paths.extend((ROOT / "walkthroughs" / "artifacts").rglob("*.yaml"))
    paths.extend((ROOT / "walkthroughs" / "artifacts").rglob("*.json"))
    for path in paths:
        store.validate(load(path), str(path.relative_to(ROOT)))


def test_every_registered_schema_exists():
    index = json.loads((ROOT / "schemas" / "index.json").read_text())
    for schema_name in set(index.values()):
        assert (ROOT / "schemas" / schema_name).is_file()


def test_malformed_artifact_fails_closed():
    store = SchemaStore(ROOT / "schemas")
    artifact = load(ROOT / "templates" / "governed-action-request.yaml")
    del artifact["scope"]
    with pytest.raises(ConformanceError, match="scope"):
        store.validate(artifact, "malformed request")
