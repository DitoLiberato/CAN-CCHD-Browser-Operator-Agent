"""Synthetic integrity scenarios; no actual scientific/human approval is represented."""
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import shutil
import unittest
import zipfile

BASE = Path(__file__).resolve().parents[1]
SKILL = BASE / "skills" / "research-assistant-pipeline"


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


BOOT = module("bootstrap", SKILL / "scripts/bootstrap_project.py")
CHECK = module("validator", SKILL / "scripts/validate_project.py")


class IntegrityScenarios(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = BOOT.bootstrap(Path(self.tmp.name) / "project", "Synthetic fixture", skill_root=SKILL)
        self.project = json.loads((self.root / "project.json").read_text())
        self.approvals = []

    def tearDown(self):
        self.tmp.cleanup()

    def artifact(self, path):
        return {"path": path, "sha256": hashlib.sha256((self.root / path).read_bytes()).hexdigest()}

    def approve(self, key, kind, paths, phase=None, **extra):
        record = {"id": key, "kind": kind, "decision": "approved", "actor_role": "human",
                  "actor_name": "SYNTHETIC TEST ACTOR", "decided_at": "2026-10-15T20:00:00Z",
                  "source_ref": "synthetic-test-fixture-only", "scope": "Synthetic integrity fixture",
                  "protocol_version": "v1", "phase_id": phase,
                  "artifacts": [self.artifact(p) for p in paths], **extra}
        self.approvals.append(record)
        return record

    def save(self):
        (self.root / "project.json").write_text(json.dumps(self.project))
        (self.root / "audit/approvals.jsonl").write_text("".join(json.dumps(a) + "\n" for a in self.approvals))

    def check(self):
        self.save()
        return CHECK.validate(self.root)[0]

    def approve_protocol(self):
        paths = ["protocol/PROTOCOL.md", "protocol/RULES.csv", "protocol/EXECUTION_PLAN.md"]
        self.approve("P0", "protocol", paths, 0)
        self.project["protocol"].update(version="v1", status="approved", approval_id="P0")
        self.project["phases"][0].update(status="completed", applicability="applicable",
                                          closure_approval_id="P0", gate_evidence=paths)

    def complete_through(self, last):
        self.approve_protocol()
        for i in range(1, last + 1):
            path = f"qa/gate-{i}.md"
            (self.root / path).write_text("Synthetic structural fixture; not scientific evidence.\n")
            paths = [path]
            if i == 11:
                paths.append("publication/PUBLICATION_QA.md")
            self.approve(f"P{i}", "phase_close", paths, i)
            self.project["phases"][i].update(status="completed", applicability="applicable",
                                            closure_approval_id=f"P{i}", gate_evidence=paths)
        self.project["current_phase"] = last
        if last >= 9:
            paths = ["evidence/extraction.csv"]
            self.approve("F", "data_freeze", paths)
            self.project["data_freeze"] = {"approval_id": "F", "protocol_version": "v1",
                                            "artifacts": [self.artifact(p) for p in paths]}

    def test_empty_scaffold_is_valid_but_unapproved(self):
        self.assertEqual(self.check(), [])
        self.assertIsNone(self.project["protocol"]["approval_id"])
        self.assertEqual(self.project["current_phase"], 0)

    def test_bootstrap_never_overwrites_existing_work(self):
        (self.root / "my-notes.txt").write_text("retain")
        with self.assertRaises(ValueError):
            BOOT.bootstrap(self.root, "replacement", skill_root=SKILL)
        self.assertEqual((self.root / "my-notes.txt").read_text(), "retain")

    def test_snapshot_tampering_is_detected(self):
        (self.root / "_pipeline/skill/references/core.md").write_text("changed")
        self.assertTrue(any("snapshot changed" in e for e in self.check()))

    def test_newest_installed_skill_does_not_replace_project_snapshot(self):
        original = (self.root / "_pipeline/skill/SKILL.md").read_bytes()
        self.assertEqual(original, (SKILL / "SKILL.md").read_bytes())
        self.assertEqual(self.check(), [])

    def test_host_metadata_can_be_generated_at_install_but_snapshot_stays_locked(self):
        installed = Path(self.tmp.name) / "host-installed-skill"
        shutil.copytree(SKILL, installed)
        (installed / "agents/openai.yaml").write_text("interface:\n  display_name: Host title\n")
        (installed / "assets/icon.svg").write_text("Synthetic host presentation fixture")
        project = BOOT.bootstrap(Path(self.tmp.name) / "host-project", "Synthetic host fixture", skill_root=installed)
        self.assertEqual(CHECK.validate(project)[0], [])
        (project / "_pipeline/skill/assets/icon.svg").write_text("Changed after project lock")
        self.assertTrue(any("snapshot changed" in e for e in CHECK.validate(project)[0]))

    def test_formal_work_without_protocol_is_rejected(self):
        self.project["phases"][1]["status"] = "in_progress"
        self.assertTrue(any("before approved protocol" in e for e in self.check()))

    def test_approved_protocol_can_open_collection(self):
        self.approve_protocol()
        self.project["phases"][1]["status"] = "in_progress"
        self.project["current_phase"] = 1
        self.assertEqual(self.check(), [])

    def test_ai_cannot_be_recorded_as_human_approver(self):
        self.approve_protocol()
        self.approvals[0]["actor_role"] = "assistant"
        self.assertTrue(any("actual approving human" in e for e in self.check()))

    def test_changed_approved_protocol_requires_new_decision(self):
        self.approve_protocol()
        (self.root / "protocol/PROTOCOL.md").write_text("different question")
        self.assertTrue(any("artifact changed" in e for e in self.check()))

    def test_wrong_version_approval_is_rejected(self):
        self.approve_protocol()
        self.project["protocol"]["version"] = "v2"
        self.assertTrue(any("version mismatch" in e for e in self.check()))

    def test_missing_phase_cannot_be_skipped(self):
        self.approve_protocol()
        self.project["phases"][3]["status"] = "in_progress"
        self.project["current_phase"] = 3
        self.assertTrue(any("predecessor" in e for e in self.check()))

    def test_not_applicable_requires_a_human_scope_and_reason(self):
        self.approve_protocol()
        self.project["phases"][1].update(status="not_applicable", applicability="not_applicable")
        self.project["current_phase"] = 1
        self.assertTrue(any("rationale" in e for e in self.check()))

    def test_open_high_qa_blocks_synthesis(self):
        self.complete_through(9)
        (self.root / "qa/findings.json").write_text(json.dumps([
            {"id": "Q1", "severity": "high", "status": "open", "description": "Synthetic conflict"}]))
        self.project["phases"][10]["status"] = "in_progress"
        self.project["current_phase"] = 10
        self.assertTrue(any("block lock/synthesis" in e for e in self.check()))

    def test_lock_artifact_must_be_covered_by_approval(self):
        self.complete_through(9)
        self.project["data_freeze"]["artifacts"] = [self.artifact("evidence/source_registry.csv")]
        self.assertTrue(any("Data freeze: artifact outside" in e for e in self.check()))

    def write_extraction(self, status="ai_suggested"):
        source = self.root / "evidence/source_registry.csv"
        with source.open(encoding="utf-8", newline="") as handle:
            columns = next(csv.reader(handle))
        with source.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns)
            writer.writeheader()
            writer.writerow({"source_id": "S1", "stream": "synthetic", "location": "fixture", "status": "available"})
        path = self.root / "evidence/extraction.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            keys = next(csv.reader(handle))
        row = dict(zip(keys, ["U1", "events", "3", "persons", "S1", "table 1", status, "X1", "true"]))
        with path.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerow(row)
        return row

    def test_ai_only_data_cannot_enter_analysis(self):
        self.approve_protocol()
        self.write_extraction()
        self.assertTrue(any("Unverified analytic field" in e for e in self.check()))

    def test_unrelated_extraction_approval_cannot_authorize_a_field(self):
        self.approve_protocol()
        self.write_extraction("verified")
        self.approve("X1", "extraction", ["evidence/extraction.csv"], verified_fields=[])
        self.assertTrue(any("Analytic field outside" in e for e in self.check()))

    def test_verified_field_is_bound_to_exact_content(self):
        self.approve_protocol()
        row = self.write_extraction("verified")
        self.approve("X1", "extraction", ["evidence/extraction.csv"], verified_fields=[row])
        self.assertEqual(self.check(), [])
        self.approvals[-1]["verified_fields"][0]["value"] = "4"
        self.assertTrue(any("Analytic field outside" in e for e in self.check()))

    def test_path_traversal_is_rejected(self):
        self.approve_protocol()
        self.approvals[0]["artifacts"].append({"path": "../outside", "sha256": "0" * 64})
        self.assertTrue(any("unsafe" in e for e in self.check()))

    def test_extraction_requires_valid_schema_even_without_rows(self):
        for content in ["", "arbitrary,headers\nx,y\n"]:
            (self.root / "evidence/extraction.csv").write_text(content)
            self.assertTrue(any("CSV columns" in e for e in self.check()))

    def test_inclusion_whitespace_cannot_bypass_verification(self):
        self.approve_protocol()
        self.write_extraction()
        p = self.root / "evidence/extraction.csv"
        p.write_text(p.read_text().replace("true", "true "))
        self.assertTrue(any("Unverified analytic field" in e for e in self.check()))
        p.write_text(p.read_text().replace("true ", "maybe"))
        self.assertTrue(any("explicit boolean" in e for e in self.check()))

    def test_source_registry_must_resolve_included_sources(self):
        self.approve_protocol()
        self.write_extraction("verified")
        p = self.root / "evidence/source_registry.csv"
        p.write_text(p.read_text().replace("S1,", "S2,"))
        self.assertTrue(any("does not resolve" in e for e in self.check()))
        p.unlink()
        self.assertTrue(any("Missing required file" in e for e in self.check()))

    def test_phase9_closure_requires_data_lock(self):
        self.complete_through(9)
        self.project["data_freeze"] = None
        self.assertTrue(any("Completed scientific QA" in e for e in self.check()))

    def test_any_freeze_requires_severe_findings_resolved(self):
        self.complete_through(9)
        self.project["phases"][9]["status"] = "in_progress"
        (self.root / "qa/findings.json").write_text('[{"severity":"critical","status":"open"}]')
        self.assertTrue(any("block lock/synthesis" in e for e in self.check()))

    def test_unknown_qa_severity_or_status_cannot_silently_pass(self):
        p = self.root / "qa/findings.json"
        p.write_text('[{"severity":"High","status":"open"}]')
        self.assertTrue(any("invalid severity" in e for e in self.check()))
        p.write_text('[{"severity":"high","status":"ignored"}]')
        self.assertTrue(any("invalid status" in e for e in self.check()))

    def test_snapshot_manifest_must_match_even_if_lock_is_refreshed(self):
        p = self.root / "_pipeline/skill/references/core.md"
        p.write_text("modified")
        path = self.root / "PIPELINE_LOCK.json"
        lock = json.loads(path.read_text())
        lock["files"]["references/core.md"] = hashlib.sha256(p.read_bytes()).hexdigest()
        path.write_text(json.dumps(lock))
        self.assertTrue(any("distribution manifest" in e for e in self.check()))

    def test_escaping_required_symlink_returns_error_without_crash(self):
        outside = Path(self.tmp.name) / "outside.txt"
        outside.write_text("synthetic")
        p = self.root / "CURRENT_STATE.md"
        p.unlink()
        p.symlink_to(outside)
        self.assertTrue(any("escapes project" in e for e in self.check()))

    def test_current_phase_uses_blocked_instead_of_locked(self):
        self.project["phases"][0]["status"] = "locked"
        self.assertTrue(any("Current phase cannot be locked" in e for e in self.check()))
        self.project["phases"][0]["status"] = "blocked"
        self.assertEqual(self.check(), [])

    def test_exploratory_inputs_cannot_be_accepted_before_protocol(self):
        self.write_extraction("verified")
        self.assertTrue(any("Accepted analytic inputs" in e for e in self.check()))

    def test_complete_synthetic_release_requires_scoped_approval(self):
        self.complete_through(11)
        path = "publication/manuscript.md"
        (self.root / path).write_text("Synthetic artifact; no study results.")
        self.approve("R", "release", [path])
        self.project["release"] = {"status": "release_candidate", "approval_id": "R",
                                   "artifacts": [self.artifact(path)]}
        self.assertEqual(self.check(), [])
        self.project["release"]["artifacts"] = [self.artifact("publication/PUBLICATION_QA.md")]
        self.assertTrue(any("Release: artifact outside" in e for e in self.check()))

    def test_archive_contains_only_standalone_skill(self):
        archive = next((BASE / "dist").glob("*.zip"))
        with zipfile.ZipFile(archive) as z:
            names = z.namelist()
            self.assertTrue(all(n.startswith("research-assistant-pipeline/") for n in names))
            self.assertIn("research-assistant-pipeline/SKILL.md", names)
            self.assertFalse(any("can_cchd.db" in n or ".git/" in n for n in names))
            self.assertIsNone(z.testzip())

    def test_distributed_zip_bootstraps_and_validates_without_original_repo(self):
        install = Path(self.tmp.name) / "isolated installation"
        with zipfile.ZipFile(next((BASE / "dist").glob("*.zip"))) as archive:
            archive.extractall(install)
        skill = install / "research-assistant-pipeline"
        project = Path(self.tmp.name) / "new independent project"
        boot = subprocess.run([sys.executable, str(skill / "scripts/bootstrap_project.py"),
                               str(project), "--title", "Synthetic ZIP test", "--language", "pt-BR"],
                              capture_output=True, text=True)
        self.assertEqual(boot.returncode, 0, boot.stderr)
        check = subprocess.run([sys.executable, str(project / "_pipeline/skill/scripts/validate_project.py"),
                                str(project), "--json"], capture_output=True, text=True)
        self.assertEqual(check.returncode, 0, check.stderr)
        self.assertEqual(json.loads(check.stdout)["status"], "STRUCTURAL_PASS")


if __name__ == "__main__":
    unittest.main()
