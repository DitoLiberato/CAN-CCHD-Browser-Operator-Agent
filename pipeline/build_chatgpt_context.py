#!/usr/bin/env python3
"""Export the existing workflow as one Markdown context file for manual project use."""
import argparse
import hashlib
import json
from pathlib import Path
import re

from build_distribution import inventory

NAME = "research-assistant-pipeline"


def build(source, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    if output == source or source in output.parents:
        raise ValueError("Context output must be outside the skill distribution")
    if any(p.is_symlink() for p in source.rglob("*")):
        raise ValueError("Skill source must not contain symlinks")
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    if inventory(source) != manifest.get("content_sha256"):
        raise ValueError("Source differs from its distribution manifest")
    version = manifest["version"]
    if not re.fullmatch(r"[A-Za-z0-9._-]+", version):
        raise ValueError("Invalid version")
    files = [source / "SKILL.md", *sorted((source / "references").glob("*.md")),
             source / "CITATION.cff", source / "LICENSE"]
    header = [
        "# Research Assistant Pipeline — manual project context\n",
        f"Tool version: **{version}**. This is a context export, not a new workflow version.\n",
        "This file contains the full SKILL.md instructions, all bundled methodological references,",
        "citation metadata and the license notice. Use it as project context when native installation is unavailable.",
        "Attaching it does not install a skill or grant tools. Python scripts and empty project",
        "templates remain in the [original ZIP](research-assistant-pipeline-" + version + ".zip).\n",
        "Respond in the researcher's language. For an existing project, follow that project's",
        "pinned snapshot and approval records; do not overwrite its rules with this export.",
        "If a referenced local file or tool is unavailable, say so and request the actual file",
        "or use the documented manual fallback. Never claim a script or check ran without execution.\n",
        "Generated with `python3 pipeline/build_chatgpt_context.py`. The source hashes below",
        "identify the original files; relative links are adjusted for this export's location.\n",
        "## Source inventory\n",
        "| Source | SHA-256 |", "|---|---|",
    ]
    for path in files:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        header.append(f"| `{path.relative_to(source).as_posix()}` | `{digest}` |")
    sections = ["\n".join(header)]
    for path in files:
        text = path.read_text(encoding="utf-8")

        def link(match):
            target = match.group(1)
            if ":" in target or target.startswith("#"):
                return match.group(0)
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(source) or not resolved.is_file():
                raise ValueError(f"Invalid bundled reference: {target}")
            return f"](../skills/{NAME}/{resolved.relative_to(source).as_posix()})"

        text = re.sub(r"\]\(([^)]+)\)", link, text)
        if path.name == "CITATION.cff":
            text = "```yaml\n" + text.rstrip() + "\n```\n"
        elif path.name == "LICENSE":
            text = "```text\n" + text.rstrip() + "\n```\n"
        elif text.startswith("---\n"):
            _, metadata, body = text.split("---", 2)
            text = "```yaml\n" + metadata.strip() + "\n```\n" + body
        sections.append(f"\n---\n\n## Source: {path.relative_to(source).as_posix()}\n\n{text.rstrip()}\n")
    output.mkdir(parents=True, exist_ok=True)
    context = output / f"{NAME}-{version}-context.md"
    context.write_text("\n".join(sections), encoding="utf-8")
    digest = hashlib.sha256(context.read_bytes()).hexdigest()
    checksum = context.with_suffix(".sha256")
    checksum.write_text(f"{digest}  {context.name}\n", encoding="utf-8")
    return context, checksum, len(files)


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=str(here / "skills" / NAME))
    parser.add_argument("--output", default=str(here / "dist"))
    args = parser.parse_args()
    context, checksum, count = build(args.source, args.output)
    print(f"Built {context.name} from {count} source files; checksum in {checksum.name}")


if __name__ == "__main__":
    main()
