# Case Report + Review — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR THIS BRANCH**

Last updated: **2026-09-03**  
Branch: **`case-report-01`**  
Parent architecture: **`phase11-writing`**  
Current status: **PHASE 0 LOCKED; PHASE 0.5 PRIVATE CASE CORE IN PROGRESS; PHASE 1 SEARCH CALIBRATION IN PROGRESS**

## Privacy boundary

This repository is public. Patient-level source documents and potentially identifying clinical details must remain outside this branch until explicit privacy/consent clearance.

The branch may contain:

- generic methodology;
- de-identification-safe templates;
- systematic-review search/screening/extraction artifacts;
- privacy-safe project-state summaries;
- later manuscript material only after privacy review.

The branch must not contain direct patient identifiers, original source PDFs, clinical images, or a detailed rare-case Case Core before consent/privacy clearance.

## Start here

Read in this order:

1. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
2. `docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`
3. `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.1.md`
4. `docs/PHASE0_05_PROGRESS_SNAPSHOT_2026-09-03.md`
5. `docs/PROJECT_DECISION_RECORD_v0.2.md`
6. `docs/CASE_REPORT_REVIEW_HANDOFF.md`
7. `case/CASE_CORE_TEMPLATE.md`

## Scientific architecture

Two streams remain separate until verification and freeze:

- **CASE STREAM** — what actually happened to the index patient;
- **LITERATURE STREAM** — what has actually been published.

Literature cannot retrospectively rewrite case facts. Case features cannot determine which literature findings are accepted.

## Phase 0 — CLOSED

`docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md` is physician-approved.

Planned article:

> **Case report with an embedded systematic review of reported cases.**

Primary review question:

> Among published human cases with Tetralogy of Fallot and Morgagni diaphragmatic hernia in the same patient, what presentation, diagnostic pathway, intervention sequence, palliation strategy, hernia management, definitive repair and outcomes have been reported?

The publication endpoint is locked to the **full staged clinical course through definitive diaphragmatic and cardiac correction plus an initial postoperative/early follow-up endpoint**.

Changing to an earlier bridge-only endpoint requires an explicit Phase 0 protocol amendment.

## Phase 0.5 — IN PROGRESS, PRIVATE SIDE

A de-identified private Case Core has been initiated from available primary clinical sources and clinician updates. It remains intentionally outside this public repository.

The Case Core remains open until the definitive surgical course and early outcome are available.

## Phase 1 — IN PROGRESS

Initial search calibration and sentinel recall are documented in:

`docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.1.md`

Initial direct candidate registry:

`review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.1.csv`

Current calibration suggests a small enumerable direct-case literature, with four direct candidates identified so far through PubMed-indexed and scholarly-web discovery.

The central association is therefore not novel. The likely teaching contribution lies in **different management routes, competing cardiorespiratory physiology, response-guided palliation, and the eventual staged/combined course**.

Balloon pulmonary/RVOT palliation is already established in TOF generally. Any novelty must be narrower than balloon dilation itself.

## Gate 1 remains open

Before Phase 1 closes:

- run source-native PubMed count/export;
- run Europe PMC count/export;
- reconcile PubMed/Europe PMC;
- enrich with OpenAlex/Crossref;
- complete supplementary scholarly-web/Google Scholar searching;
- run backward/forward citation chasing;
- perform a noise audit;
- freeze the raw candidate registry for Phase 2 deduplication.

## One-line handoff

**Continue on `case-report-01`; Phase 0 is locked, the private Case Core remains open through definitive surgery, and Phase 1 is actively building an exhaustive direct TOF–Morgagni reported-case corpus plus a separate contextual palliation literature.**
