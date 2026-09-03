# Case Report 01 — Handoff

**Branch:** `case-report-01`  
**Last updated:** 2026-09-03  
**Status:** **Pipeline v1.0 frozen; Phase 0 protocol drafted; Phase 0.5 private Case Core in progress.**

## Read first

1. `CURRENT_STATE.md`
2. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
3. `docs/PHASE0_05_PROGRESS_SNAPSHOT_2026-09-03.md`
4. `docs/PHASE0_CASE_REVIEW_PROTOCOL_v0.1.md`
5. `docs/PROJECT_DECISION_RECORD_v0.2.md`
6. `case/CASE_CORE_TEMPLATE.md`

## Scientific architecture

Two independent streams remain firewalled until Phase 7:

- **CASE STREAM** — verified facts of the index case from primary clinical sources;
- **LITERATURE STREAM** — verified published evidence from reproducible search and review.

Literature cannot rewrite historical case facts. Case features may motivate search sensitivity analyses but cannot determine which published evidence is accepted.

## What is already decided

- article design: case report + embedded systematic review of reported cases;
- the core anatomic association itself is not presumed novel because direct precedent exists;
- no `first`, `unique`, or strong novelty claim before Phase 10;
- primary direct-analog corpus: unique published human patients with TOF + Morgagni hernia;
- trisomy 21 is a comparison/modifier axis rather than an inclusion criterion;
- broader diaphragmatic/catheter/syndromic literature may be retained only as explicitly labeled contextual evidence;
- management sequencing is a central review outcome;
- the management hypothesis now includes response-guided transcatheter palliation, not only preplanned device implantation;
- detailed patient-level procedure facts, chronology, source PDFs and images remain outside the public GitHub branch until consent/privacy clearance;
- multimodality imaging exists privately and may later support a high-value figure set after consent/de-identification;
- the project remains viable and should continue.

## Phase 0 state

`docs/PHASE0_CASE_REVIEW_PROTOCOL_v0.1.md` has been drafted.

It defines:

- primary and secondary review questions;
- direct-analog eligibility;
- contextual evidence boundary;
- comparison axes;
- high-recall search framework;
- systematic-review synthesis limits;
- CARE/PRISMA/JBI reporting/appraisal plan;
- imaging strategy;
- consent/ethics/privacy gate;
- amendment rules.

**Gate 0 remains OPEN until physician approval.**

After approval, promote to `PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md` before formal Phase 1 collection.

## Phase 0.5 state

A private de-identified artifact has been created outside GitHub:

`CASE_CORE_PRIVATE_v0.1.md`

It currently records:

- minimum scientifically necessary baseline;
- pre-intervention cardiac anatomy;
- competing cardiorespiratory physiology;
- intended vs actually completed intervention distinction;
- early post-intervention course;
- current growth/discharge strategy;
- imaging inventory;
- observed fact vs contemporaneous interpretation vs later-author-interpretation firewall;
- explicit missing-data list.

**Gate 0.5 remains IN PROGRESS.**

Priority private sources still desired when available:

- full catheterization report;
- invasive/procedural measurements and technical details;
- early discharge documentation;
- early outpatient follow-up;
- later definitive surgical documentation if the manuscript endpoint includes it.

## Publication endpoint decision still open

Two acceptable endpoints remain:

1. **Early bridge-to-growth endpoint** — manuscript freezes after a stable early follow-up period, before definitive surgery.
2. **Full staged-course endpoint** — manuscript waits for definitive cardiac/diaphragmatic surgery and postoperative outcome.

This endpoint must be deliberately selected before Case Core freeze.

## Privacy rule

The repository is public. Until explicit consent/privacy clearance:

- no original patient PDF;
- no direct identifiers;
- no detailed rare-case chronology in public GitHub;
- no clinical images;
- no public Case Core.

Public branch may contain methodology, review artifacts and privacy-safe project-state summaries.

## Immediate next actions

1. Physician review of `PHASE0_CASE_REVIEW_PROTOCOL_v0.1.md`.
2. Incorporate any amendments and lock Phase 0 v1.0.
3. Continue private Phase 0.5 verification as primary clinical documents become available.
4. Decide minimum follow-up required for Case Core freeze.
5. Clarify guardian publication-consent pathway and institutional ethics/IRB determination.
6. Start Phase 1 calibrated high-recall searches only after Gate 0 lock.

## One-line resume prompt

**Continue Case Report 01 on branch `case-report-01`. Read the Phase 0/0.5 snapshot and protocol draft. Keep all patient-level clinical material private, approve/lock Gate 0, continue the private Case Core, then begin the systematic reported-case review with sentinel-recall calibration.**
