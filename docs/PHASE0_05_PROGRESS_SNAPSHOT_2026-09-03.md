# Case Report 01 — Phase 0 / 0.5 Progress Snapshot

**Date:** 2026-09-03  
**Branch:** `case-report-01`  
**Status:** **PHASE 0 PROTOCOL DRAFTED; PHASE 0.5 PRIVATE CASE CORE IN PROGRESS**

## Purpose

This snapshot preserves the project state after review of the initial clinical source and a subsequent treating-clinician update, while respecting the public-repository privacy firewall.

Detailed patient-level chronology and procedure-specific facts remain in a private, de-identified Case Core outside GitHub.

## Decisions now established

### 1. Article architecture

The project remains a **case report with an embedded systematic review of reported cases**.

CASE and LITERATURE streams remain independent until Phase 7 Dual Freeze.

### 2. Novelty framing

The core anatomic association itself is not presumed novel.

The preliminary probe identified direct precedent, so the article must not be framed as a first association.

Potential contribution will instead be tested across:

- competing cardiorespiratory physiology;
- diagnostic pathway;
- intervention sequencing;
- response-guided catheter palliation;
- bridge-to-growth strategy;
- definitive cardiac/diaphragmatic surgical planning;
- clinical outcome.

No `first`, `unique`, or equivalent claim is allowed before Phase 10 novelty adjudication.

### 3. Review scope

Primary direct-analog corpus:

> unique published human patients with both Tetralogy of Fallot and Morgagni diaphragmatic hernia.

Secondary contextual evidence may include broader diaphragmatic-hernia management analogs, transcatheter RVOT bridge strategies, trisomy-21/Morgagni diagnostic context, and relevant surgical/physiologic literature, but these sources remain analytically separate from direct analogs.

### 4. Management question refined

The project question is no longer limited to a preplanned device strategy.

Phase 0 now explicitly asks how prior cases handled:

- cardiac-first vs diaphragmatic-first vs simultaneous/combined treatment;
- staged approaches;
- bridge palliation;
- balloon-based RVOT intervention;
- RVOT/device stenting or shunt strategies;
- response-guided decisions during catheterization;
- timing of definitive repair after stabilization/growth.

Patient-specific procedural details supporting this refinement remain private until consent/privacy clearance.

### 5. Imaging potential

The private Case Stream has access to multimodality imaging capable of supporting the manuscript, including radiography, thoracic CT, echocardiography and angiography.

Final figure selection is deferred until consent/privacy clearance and manuscript-level teaching points are known.

### 6. Case maturity

The case has progressed beyond a merely planned intervention and now has an early post-intervention clinical endpoint sufficient to continue the project.

However, Phase 0.5 remains open because the final Case Core still requires selected primary documentation and at least an early discharge/follow-up endpoint before freeze.

The definitive surgical course may later strengthen the paper but is not automatically required if the final publication endpoint is explicitly defined as a successful/unsuccessful bridge-to-growth period and the limitations are transparent.

### 7. Privacy

The repository is public.

Therefore:

- original source PDFs remain off-repository;
- direct identifiers remain off-repository;
- detailed rare-case chronology remains off-repository;
- clinical images remain off-repository until publication consent and de-identification review;
- the public branch stores methodology, literature-review artifacts and privacy-safe project state only.

## Artifacts

### Public branch

- `CURRENT_STATE.md`
- `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
- `docs/PHASE0_CASE_REVIEW_PROTOCOL_v0.1.md`
- `docs/PROJECT_DECISION_RECORD_v0.1.md`
- `docs/CASE_REPORT_REVIEW_HANDOFF.md`
- `case/CASE_CORE_TEMPLATE.md`

### Private/off-repository

- `CASE_CORE_PRIVATE_v0.1.md`
- source clinical documents;
- patient-level imaging;
- detailed timeline and procedure-specific source data.

## Current gates

### Gate 0 — Protocol

**OPEN.** Protocol v0.1 has been drafted and awaits physician approval/edits before lock.

### Gate 0.5 — Case Core

**IN PROGRESS.** Private Case Core v0.1 has been reconstructed from the available referral source plus treating-clinician update. It is not frozen.

## Required next actions

1. Physician review/approve or amend `PHASE0_CASE_REVIEW_PROTOCOL_v0.1.md`.
2. Promote approved protocol to v1.0 LOCKED.
3. Continue private Case Core verification with catheterization report and early discharge documentation when available.
4. Decide the minimum follow-up endpoint required before Case Core freeze.
5. Document guardian consent pathway and institutional ethics/IRB determination.
6. Only after Gate 0 lock, begin Phase 1 calibrated literature collection.

## One-line resume

**Resume Case Report 01 on `case-report-01`: review and lock the Phase 0 protocol, continue the private de-identified Phase 0.5 Case Core, keep detailed patient data and images off the public repository, then proceed to calibrated high-recall literature collection only after Gate 0 is closed.**
