#!/usr/bin/env python3
"""Build an allowlisted, self-contained Agent Skill distribution."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

NAME = "research-assistant-pipeline"
HOST_METADATA = {"agents/openai.yaml", "assets/icon.svg"}


def inventory(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()
            and "__pycache__" not in p.parts and p.suffix != ".pyc"
            and p.relative_to(root).as_posix() not in HOST_METADATA | {"manifest.json"}}


def build(source, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    if any(p.is_symlink() for p in source.rglob("*")):
        raise ValueError("Skill source must not contain symlinks")
    required = ["SKILL.md", "LICENSE", "CITATION.cff", "manifest.json",
                "scripts/bootstrap_project.py", "scripts/validate_project.py"]
    for name in required:
        if not (source / name).is_file():
            raise ValueError(f"Missing required skill file: {name}")
    allowed_roots = {"SKILL.md", "LICENSE", "CITATION.cff", "manifest.json",
                     "agents", "references", "scripts", "assets"}
    if {p.name for p in source.iterdir()} - allowed_roots:
        raise ValueError("Unexpected files at skill root")
    manifest_path = source / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["host_metadata_excluded"] = sorted(HOST_METADATA)
    manifest["content_sha256"] = inventory(source)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    target = output / "skills" / NAME
    if target != source:
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    dist = output / "dist"
    dist.mkdir(parents=True, exist_ok=True)
    archive = dist / f"{NAME}-{manifest['version']}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(target.rglob("*")):
            if not p.is_file() or "__pycache__" in p.parts or p.suffix == ".pyc":
                continue
            entry = zipfile.ZipInfo(f"{NAME}/{p.relative_to(target).as_posix()}", (2026, 10, 15, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            z.writestr(entry, p.read_bytes())
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None or f"{NAME}/SKILL.md" not in z.namelist():
            raise ValueError("Invalid distribution archive")
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    (dist / "SHA256SUMS").write_text(f"{checksum}  {archive.name}\n", encoding="utf-8")
    shutil.copy2(target / "CITATION.cff", output / "CITATION.cff")
    shutil.copy2(target / "LICENSE", output / "LICENSE")
    return archive, checksum


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument("--source", default=str(here / "skills" / NAME))
    parser.add_argument("--output", default=str(here))
    args = parser.parse_args()
    archive, checksum = build(args.source, args.output)
    print(f"Built {archive.name}; SHA256 {checksum}")


if __name__ == "__main__":
    main()
