import json
from pathlib import Path
import shutil
import tomllib

import yaml
from jsonschema import Draft202012Validator
import pytest

from gaso.errors import ConformanceError, UsageError
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


def test_profile_validation_fails_when_catalog_is_not_installed(tmp_path):
    installed_schemas = tmp_path / "share" / "gaso" / "schemas"
    shutil.copytree(ROOT / "schemas", installed_schemas)
    profile = load(ROOT / "profiles" / "mssp.yaml")

    with pytest.raises(UsageError, match="control catalog"):
        SchemaStore(installed_schemas).validate(profile, "installed MSSP profile")


def test_installed_layout_profile_references_are_checked_against_catalog(tmp_path):
    installed_root = tmp_path / "share" / "gaso"
    shutil.copytree(ROOT / "schemas", installed_root / "schemas")
    (installed_root / "controls").mkdir()
    shutil.copy2(ROOT / "controls" / "control-catalog.yaml", installed_root / "controls" / "control-catalog.yaml")
    profile = load(ROOT / "profiles" / "mssp.yaml")
    profile["applicable_controls"].append("GASO-POL-999")

    with pytest.raises(ConformanceError, match="GASO-POL-999"):
        SchemaStore(installed_root / "schemas").validate(profile, "installed MSSP profile")


def test_distribution_declares_control_catalog_data_file():
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())
    assert project["tool"]["setuptools"]["data-files"]["share/gaso/controls"] == ["controls/control-catalog.yaml"]
