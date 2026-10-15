#!/usr/bin/env python3
"""Check recorded project integrity. This cannot authenticate humans or validate science."""
import argparse
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path
import re

TERMINAL = {"completed", "completed_with_note", "not_applicable"}
STATUSES = TERMINAL | {"locked", "available", "in_progress", "blocked", "awaiting_human"}
HOST_METADATA = {"agents/openai.yaml", "assets/icon.svg"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root):
    root = Path(root).resolve()
    errors, warnings = [], []

    def fail(message):
        errors.append(message)

    def local(path):
        if not isinstance(path, str) or not path or Path(path).is_absolute():
            raise ValueError("Expected a nonempty project-relative path")
        value = (root / path).resolve()
        if not value.is_relative_to(root):
            raise ValueError("Artifact path escapes project")
        return value

    def read_json(path):
        return json.loads(local(path).read_text(encoding="utf-8"))

    def artifact_list(items, label, required=True):
        if not isinstance(items, list) or (required and not items):
            fail(f"{label}: nonempty artifact list required")
            return
        for item in items:
            try:
                p = local(item["path"])
                digest = item["sha256"]
                if not re.fullmatch(r"[a-f0-9]{64}", digest) or sha(p) != digest:
                    fail(f"{label}: artifact changed or invalid hash: {item['path']}")
            except (OSError, ValueError, TypeError, KeyError):
                fail(f"{label}: missing, unsafe or invalid artifact")

    def read_csv(path, columns):
        with local(path).open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, strict=True)
            headers = reader.fieldnames or []
            if len(headers) != len(set(headers)) or not set(columns).issubset(headers):
                fail(f"{path}: missing/duplicate required CSV columns")
                return []
            rows = list(reader)
            for row in rows:
                if None in row or any(value is None for value in row.values()):
                    fail(f"{path}: malformed CSV row")
            return rows

    required = ["START_HERE.md", "CURRENT_STATE.md", "PIPELINE_LOCK.json", "project.json",
                "protocol/PROTOCOL.md", "protocol/RULES.csv", "protocol/EXECUTION_PLAN.md",
                "protocol/STANDARDS.md", "audit/approvals.jsonl", "audit/decisions.jsonl",
                "audit/amendments.jsonl", "audit/tool_use.csv", "handoff/LATEST.md",
                "qa/findings.json", "evidence/extraction.csv", "evidence/source_registry.csv"]
    try:
        for path in required:
            if not local(path).is_file():
                fail(f"Missing required file: {path}")
        if errors:
            return errors, warnings
        project, lock = read_json("project.json"), read_json("PIPELINE_LOCK.json")
        if project.get("schema_version") != 1 or lock.get("schema_version") != 1:
            fail("Unsupported schema version")
        snapshot = local(lock["snapshot"])
        if not snapshot.is_dir() or not isinstance(lock.get("files"), dict) or not lock["files"]:
            fail("Missing pipeline snapshot/inventory")
        else:
            actual = {}
            for p in snapshot.rglob("*"):
                if p.is_symlink():
                    fail("Pipeline snapshot contains symbolic link")
                if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
                    actual[p.relative_to(snapshot).as_posix()] = sha(p)
            if actual != lock["files"]:
                fail("Pipeline snapshot changed from PIPELINE_LOCK.json")
            manifest = json.loads((snapshot / "manifest.json").read_text(encoding="utf-8"))
            content = {name: digest for name, digest in actual.items()
                       if name not in HOST_METADATA | {"manifest.json"}}
            if content != manifest.get("content_sha256"):
                fail("Pipeline snapshot differs from its distribution manifest")
            if manifest.get("version") != lock.get("version"):
                fail("Pipeline version differs from lock")
        approvals = {}
        for line_no, line in enumerate(local("audit/approvals.jsonl").read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
                key = record["id"]
                if not key or key in approvals:
                    fail(f"Approval line {line_no}: missing/duplicate ID")
                approvals[key] = record
            except (ValueError, KeyError, TypeError):
                fail(f"Invalid approval JSON at line {line_no}")

        protocol = project["protocol"]
        if protocol.get("status") not in {"draft", "approved"}:
            fail("Protocol status must be draft or approved")

        def approval(key, kinds, phase=None):
            record = approvals.get(key)
            if not record:
                fail(f"Missing human approval: {key}")
                return None
            for field in ["actor_name", "decided_at", "source_ref", "scope", "protocol_version"]:
                if not isinstance(record.get(field), str) or not record[field].strip():
                    fail(f"Approval {key}: missing {field}")
            if record.get("actor_role") != "human" or record.get("decision") != "approved":
                fail(f"Approval {key}: must record an actual approving human decision")
            if record.get("kind") not in kinds:
                fail(f"Approval {key}: incorrect decision kind")
            if record.get("protocol_version") != protocol.get("version"):
                fail(f"Approval {key}: protocol version mismatch; review amendment impact")
            if phase is not None and record.get("phase_id") != phase:
                fail(f"Approval {key}: phase scope mismatch")
            try:
                datetime.fromisoformat(record.get("decided_at", "").replace("Z", "+00:00"))
            except (ValueError, TypeError):
                fail(f"Approval {key}: invalid decision date")
            artifact_list(record.get("artifacts"), f"Approval {key}")
            return record

        def check_covered(items, record, label):
            covered = {(a.get("path"), a.get("sha256")) for a in (record or {}).get("artifacts", [])}
            for item in items or []:
                if (item.get("path"), item.get("sha256")) not in covered:
                    fail(f"{label}: artifact outside human approval scope: {item.get('path')}")

        if protocol["status"] == "approved":
            record = approval(protocol.get("approval_id"), {"protocol"})
            covered = {a.get("path") for a in (record or {}).get("artifacts", [])}
            for path in [protocol["path"], "protocol/RULES.csv", "protocol/EXECUTION_PLAN.md"]:
                if path not in covered:
                    fail(f"Protocol approval does not cover {path}")
        phases = project["phases"]
        if not isinstance(phases, list) or [p.get("id") for p in phases] != list(range(12)):
            fail("Exactly twelve ordered phase IDs 0–11 are required")
            return errors, warnings
        current = project.get("current_phase")
        if type(current) is not int or current not in range(12):
            fail("Invalid current_phase")
        for phase in phases:
            i, status = phase["id"], phase.get("status")
            if status not in STATUSES:
                fail(f"Phase {i}: invalid status")
            if phase.get("applicability") not in {"undecided", "applicable", "not_applicable"}:
                fail(f"Phase {i}: invalid applicability")
            if i > 0 and status != "locked":
                if protocol["status"] != "approved":
                    fail(f"Phase {i}: formal work before approved protocol")
                if any(p.get("status") not in TERMINAL for p in phases[:i]):
                    fail(f"Phase {i}: predecessor gate remains open")
            if status in TERMINAL:
                if phase.get("applicability") == "undecided":
                    fail(f"Phase {i}: closure without decided applicability")
                kind = {"protocol"} if i == 0 else {"phase_close"}
                if status == "not_applicable":
                    kind = {"not_applicable"}
                    if i == 0 or not phase.get("not_applicable_reason"):
                        fail(f"Phase {i}: invalid/missing non-applicability rationale")
                    if phase.get("applicability") != "not_applicable":
                        fail(f"Phase {i}: applicability contradicts status")
                elif phase.get("applicability") != "applicable":
                    fail(f"Phase {i}: completed phase must be applicable")
                record = approval(phase.get("closure_approval_id"), kind, i)
                evidence = phase.get("gate_evidence")
                if not isinstance(evidence, list) or not evidence:
                    fail(f"Phase {i}: gate evidence required")
                else:
                    covered = {a.get("path") for a in (record or {}).get("artifacts", [])}
                    for path in evidence:
                        if not local(path).is_file() or path not in covered:
                            fail(f"Phase {i}: evidence missing or outside approval scope: {path}")
                if status == "completed_with_note" and not phase.get("closure_note"):
                    fail(f"Phase {i}: closure note required")
        if type(current) is int and current in range(12):
            if phases[current]["status"] == "locked":
                fail("Current phase cannot be locked; use blocked for a paused phase")
            if any(p["status"] not in TERMINAL for p in phases[:current]):
                fail("current_phase advances beyond an open predecessor")
            if any(p["status"] != "locked" for p in phases[current + 1:]):
                fail("Phases after current_phase must remain locked")

        findings = read_json("qa/findings.json")
        if not isinstance(findings, list):
            fail("QA findings must be a list")
            findings = []
        for finding in findings:
            if finding.get("severity") not in {"info", "low", "medium", "high", "critical", "scientific_stop"}:
                fail("QA finding: invalid severity")
            if finding.get("status") not in {"open", "in_progress", "resolved"}:
                fail("QA finding: invalid status")
        severe = [f for f in findings if f.get("severity") in {"high", "critical", "scientific_stop"}
                  and f.get("status") != "resolved"]
        synthesis_started = phases[10]["status"] != "locked"
        qa_closed = phases[9]["status"] in TERMINAL
        freeze = project.get("data_freeze")
        if severe and (qa_closed or synthesis_started or freeze):
            fail("Open high/critical scientific QA findings block lock/synthesis")
        if phases[9]["status"] in {"completed", "completed_with_note"} and not freeze:
            fail("Completed scientific QA requires a human-approved data freeze")
        if freeze:
            record = approval(freeze.get("approval_id"), {"data_freeze"})
            artifact_list(freeze.get("artifacts"), "Data freeze")
            check_covered(freeze.get("artifacts"), record, "Data freeze")
            if freeze.get("protocol_version") != protocol.get("version"):
                fail("Data freeze protocol version mismatch")
        if synthesis_started and not freeze:
            fail("Synthesis requires a human-approved data freeze")
        sources = read_csv("evidence/source_registry.csv", ["source_id", "stream", "location", "status"])
        source_ids = [r.get("source_id", "") for r in sources]
        if any(not s or not s.strip() for s in source_ids) or len(source_ids) != len(set(source_ids)):
            fail("Source registry requires nonempty unique source IDs")
        keys = ("item_id", "field", "value", "unit", "source_id", "source_location", "status")
        rows = read_csv("evidence/extraction.csv", [*keys, "human_approval_id", "analysis_included"])
        for row in rows:
            inclusion = (row.get("analysis_included") or "").strip().lower()
            if inclusion not in {"true", "1", "yes", "false", "0", "no"}:
                fail("Extraction row: analysis_included must be an explicit boolean")
            if row.get("status") not in {"ai_suggested", "verified", "corrected", "rejected", "unavailable_with_note", "needs_review"}:
                fail("Extraction row: invalid verification status")
            if inclusion not in {"true", "1", "yes"}:
                continue
            if protocol["status"] != "approved":
                fail("Accepted analytic inputs require an approved protocol")
            if row.get("status") not in {"verified", "corrected"}:
                fail(f"Unverified analytic field: {row.get('item_id')}/{row.get('field')}")
            if not row.get("source_id") or not row.get("source_location"):
                fail("Analytic field lacks source identity/location")
            if row.get("source_id") not in source_ids:
                fail("Analytic source ID does not resolve in source registry")
            if not row.get("item_id") or not row.get("field"):
                fail("Analytic field lacks item/field identity")
            record = approval(row.get("human_approval_id"), {"extraction", "mapping"})
            verified = (record or {}).get("verified_fields", [])
            if not any(all(field.get(k) == row.get(k, "") for k in keys) for field in verified):
                fail(f"Analytic field outside approval scope: {row.get('item_id')}/{row.get('field')}")

        release = project["release"]
        if release.get("status") not in {"draft", "release_candidate"}:
            fail("Invalid release status")
        if release.get("status") == "release_candidate":
            record = approval(release.get("approval_id"), {"release"})
            artifact_list(release.get("artifacts"), "Release")
            check_covered(release.get("artifacts"), record, "Release")
            if any(p["status"] not in TERMINAL for p in phases):
                fail("Release requires closure of all applicable phases")
            if phases[11]["status"] == "not_applicable":
                fail("Publication QA cannot be not applicable for a release")
            if "publication/PUBLICATION_QA.md" not in phases[11].get("gate_evidence", []):
                fail("Release requires publication QA evidence in the approved scope")
            if severe:
                fail("Open high/critical findings block release")
        if protocol["status"] == "draft":
            warnings.append("Draft protocol: no formal downstream scientific execution authorized.")
        warnings.append("Structural checks cannot authenticate human approvals or establish scientific validity.")
    except (OSError, ValueError, TypeError, KeyError, AttributeError, csv.Error) as exc:
        fail(f"Invalid project structure: {exc}")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors, warnings = validate(args.project)
    result = {"status": "FAIL" if errors else "STRUCTURAL_PASS", "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["status"])
        for message in errors:
            print(f"ERROR: {message}")
        for message in warnings:
            print(f"NOTE: {message}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
