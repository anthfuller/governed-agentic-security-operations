from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def catalog():
    return yaml.safe_load((ROOT / "controls" / "control-catalog.yaml").read_text())


def test_control_ids_are_unique_and_complete():
    controls = catalog()["controls"]
    ids = [item["id"] for item in controls]
    assert len(ids) == len(set(ids))
    assert len(ids) == 36
    for item in controls:
        assert item["accountable_role"]
        assert item["required_inputs"]
        assert item["expected_evidence"]
        assert item["verification"]


def test_control_local_references_exist():
    controls = catalog()["controls"]
    known_ids = {control["id"] for control in controls}
    for control in controls:
        assert control["related"]["controls"]
        assert set(control["related"]["controls"]) <= known_ids
        for category, paths in control["related"].items():
            if category == "controls":
                continue
            for relative in paths:
                assert (ROOT / relative).exists(), f"{control['id']} {category} missing: {relative}"


def test_profile_control_selection_matches_catalog_applicability():
    controls = {item["id"]: item for item in catalog()["controls"]}
    for profile_path in (ROOT / "profiles").glob("*.yaml"):
        profile = yaml.safe_load(profile_path.read_text())
        profile_name = profile["profile_id"].removeprefix("GASO-PROFILE-")
        selected = set(profile["applicable_controls"])
        expected = {control_id for control_id, control in controls.items() if profile_name in control["profiles"]}
        assert selected == expected
        assert all(item["control_id"] in controls for item in profile["conditional_controls"])


def test_controls_do_not_claim_unimplemented_automation():
    controls = {item["id"]: item for item in catalog()["controls"]}
    assert {item["type"] for item in controls["GASO-POL-003"]["verification"]} == {"automated", "external"}
    assert {item["type"] for item in controls["GASO-TOL-001"]["verification"]} == {"automated", "external"}
    assert {item["type"] for item in controls["GASO-TOL-003"]["verification"]} == {"automated", "external"}
    assert {item["type"] for item in controls["GASO-FLT-002"]["verification"]} == {"manual", "external"}
    for control_id in ("GASO-POL-003", "GASO-TOL-001", "GASO-TOL-003", "GASO-FLT-002"):
        assert controls[control_id]["external_dependencies"], control_id
