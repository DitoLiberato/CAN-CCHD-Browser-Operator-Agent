#!/usr/bin/env python3
"""Create an empty research workspace; no network, approvals or scientific defaults."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys

# Hosts may regenerate these presentation-only files when installing a skill.
# Project locks still hash the complete installed snapshot, including these files.
HOST_METADATA = {"agents/openai.yaml", "assets/icon.svg"}

PHASES = [
    "Question, feasibility and protocol", "Search/source planning and collection",
    "Normalization and identity reconciliation", "Preliminary relevance screening",
    "Full source retrieval", "Final eligibility and corpus adjudication",
    "Structured extraction and appraisal", "Human verification",
    "Mapping and harmonization", "Scientific QA and data lock",
    "Synthesis and analysis", "Manuscript and publication QA",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files_under(root):
    return sorted(p for p in root.rglob("*") if p.is_file()
                  and "__pycache__" not in p.parts and p.suffix != ".pyc")


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bootstrap(destination, title, language="en", skill_root=None):
    skill = Path(skill_root or Path(__file__).resolve().parents[1]).resolve()
    manifest = json.loads((skill / "manifest.json").read_text(encoding="utf-8"))
    expected = manifest.get("content_sha256", {})
    if not expected:
        raise ValueError("Skill manifest has no integrity inventory; use a built distribution.")
    actual = {p.relative_to(skill).as_posix(): digest(p) for p in files_under(skill)
              if p.relative_to(skill).as_posix() not in HOST_METADATA | {"manifest.json"}}
    if any(p.is_symlink() for p in skill.rglob("*")) or actual != expected:
        raise ValueError("Skill bundle differs from its manifest; obtain/validate the intended version.")
    root = Path(destination).expanduser()
    if root.is_symlink():
        raise ValueError("Destination must not be a symbolic link.")
    if root.exists() and (not root.is_dir() or any(root.iterdir())):
        raise ValueError("Destination must be absent or empty; existing projects are never overwritten.")
    root = root.resolve()
    if root == skill or skill in root.parents or root in skill.parents:
        raise ValueError("Create the research project outside the installed skill.")
    root.mkdir(parents=True, exist_ok=True)
    template = skill / "assets" / "project-template"
    shutil.copytree(template, root, dirs_exist_ok=True)
    snapshot = root / "_pipeline" / "skill"
    shutil.copytree(skill, snapshot, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    now = datetime.now(timezone.utc).isoformat()
    lock = {
        "schema_version": 1, "tool": manifest["name"], "version": manifest["version"],
        "upstream": manifest["upstream"], "snapshot": "_pipeline/skill",
        "created_at": now,
        "files": {p.relative_to(snapshot).as_posix(): digest(p) for p in files_under(snapshot)},
    }
    write_json(root / "PIPELINE_LOCK.json", lock)
    project = {
        "schema_version": 1, "title": title, "language": language, "created_at": now,
        "lead_author": None, "design": {"label": None, "rationale": None},
        "protocol": {"version": "draft-0.1", "status": "draft",
                     "path": "protocol/PROTOCOL.md", "approval_id": None},
        "capabilities": {k: "unknown" for k in ["web", "files", "python", "github_read", "github_write"]},
        "repository": {"owner": None, "name": None, "url": None,
                       "visibility": "private_recommended", "remote_verified": False},
        "current_phase": 0,
        "phases": [{"id": i, "name": name, "status": "in_progress" if i == 0 else "locked",
                    "applicability": "undecided", "gate_evidence": [],
                    "closure_approval_id": None, "closure_note": None,
                    "not_applicable_reason": None} for i, name in enumerate(PHASES)],
        "data_freeze": None,
        "release": {"status": "draft", "approval_id": None, "artifacts": []},
    }
    write_json(root / "project.json", project)
    return root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination")
    parser.add_argument("--title", required=True)
    parser.add_argument("--language", default="en")
    args = parser.parse_args()
    try:
        root = bootstrap(args.destination, args.title, args.language)
    except (OSError, ValueError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created local project: {root}")
    print("Phase 0 only. No human approvals, searches, GitHub repository or remote synchronization created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
