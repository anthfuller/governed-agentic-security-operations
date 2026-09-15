import json
from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def test_no_unfinished_stub_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in {".git", ".venv", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        unfinished_marker = "place" + "holder"
        assert path.read_text(errors="ignore").strip().lower() != unfinished_marker, path


def test_machine_readable_files_parse():
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in {".git", ".venv", "__pycache__"} for part in path.parts):
            continue
        if path.suffix == ".json":
            json.loads(path.read_text())
        elif path.suffix in {".yaml", ".yml"}:
            yaml.safe_load(path.read_text())
        elif path.suffix == ".jsonl":
            for line in path.read_text().splitlines():
                if line.strip():
                    json.loads(line)


def test_internal_markdown_links_resolve_case_sensitively():
    failures = []
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv"} for part in path.parts):
            continue
        for raw_target in MARKDOWN_LINK.findall(path.read_text()):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (path.parent / relative).resolve().exists():
                failures.append(f"{path.relative_to(ROOT)} -> {relative}")
    assert not failures, "Broken local links:\n" + "\n".join(failures)
