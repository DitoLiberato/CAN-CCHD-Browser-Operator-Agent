# Case Report + Review — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR THIS BRANCH**

Last updated: **2026-09-03**  
Branch: **`case-report-01`**  
Parent architecture: **`phase11-writing`**  
Current status: **PHASE 0 LOCKED; PHASE 0.5 PRIVATE CASE CORE IN PROGRESS; PHASE 1 ACTIVE — CALIBRATION/SENSITIVITY WAVE 2 COMPLETE, GATE 1 OPEN**

## Privacy boundary

This repository is public. Patient-level source documents and potentially identifying clinical details must remain outside this branch until explicit privacy/consent clearance.

The branch may contain methodology, de-identification-safe templates, systematic-review artifacts, privacy-safe project-state summaries, and later manuscript material only after privacy review.

The branch must not contain direct patient identifiers, original patient source PDFs, clinical images, or a detailed rare-case Case Core before consent/privacy clearance.

## Start here

Read in this order:

1. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
2. `docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`
3. `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.2.md`
4. `docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md`
5. `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.2.csv`
6. `docs/PHASE0_05_PROGRESS_SNAPSHOT_2026-09-03.md`
7. `docs/PROJECT_DECISION_RECORD_v0.2.md`
8. `docs/CASE_REPORT_REVIEW_HANDOFF.md`
9. `case/CASE_CORE_TEMPLATE.md`

## Scientific architecture

Two streams remain separate until verification and freeze:

- **CASE STREAM** — what actually happened to the index patient;
- **LITERATURE STREAM** — what has actually been published.

Literature cannot retrospectively rewrite case facts. Case features cannot determine which literature findings are accepted.

## Phase 0 — CLOSED

`docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md` is physician-approved.

Planned article:

> **Case report with an embedded systematic review of reported cases.**

Primary direct-review question:

> Among published human cases with Tetralogy of Fallot and Morgagni diaphragmatic hernia in the same patient, what presentation, diagnostic pathway, intervention sequence, palliation strategy, hernia management, definitive repair and outcomes have been reported?

Publication endpoint is locked to the **full staged clinical course through definitive diaphragmatic and cardiac correction plus an initial postoperative/early-follow-up endpoint**.

Changing to an earlier bridge-only endpoint requires an explicit Phase 0 protocol amendment.

## Phase 0.5 — IN PROGRESS, PRIVATE SIDE

A de-identified private Case Core exists outside the public repository. It remains open until the definitive surgical course and early outcome are available.

## Phase 1 — ACTIVE

Current source-of-truth:

- `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.2.md`
- `docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md`
- `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.2.csv`

### Current candidate signal

The raw registry now contains:

- **6 records with explicit or historically equivalent Morgagni/subcostosternal signal**, pending final eligibility and report-to-patient reconciliation;
- **1 additional high-value anatomy-pending Pentalogy/CDH case**, guaranteed to remain useful as a management analog even if the diaphragmatic defect proves non-Morgagni.

Important newly recovered signals:

- a 1952 `subcostosternal diaphragmatic hernia` report explicitly coexisting with TOF; modern and historical literature equates anteromedial subcostosternal defects with Morgagni-type defects, so this is a direct candidate pending full text;
- a 2024 Pentalogy of Cantrell case-level abstract explicitly documenting operative Morgagni hernia plus TOF, providing a hernia-first route with poor neonatal outcome;
- a 2025/2026 Pentalogy case with TOF + large CDH, RVOT stent first, then definitive combined cardiac/diaphragmatic repair; anatomy remains pending for direct-set status.

### Search calibration conclusion

- modern `Morgagni` terminology alone is too narrow historically;
- `subcostosternal` / foramen-of-Morgagni terminology is mandatory for recall;
- broad TOF + CDH searches are necessary but anatomically noisy;
- Pentalogy of Cantrell is a required sensitivity pathway;
- multilingual modern-term sweep has not yet added a new direct case;
- Down syndrome terms remain sensitivity/comparison terms only, never mandatory.

### Scientific framing

The central association is not novel. Current evidence strengthens the intended teaching angle: **different routes through the same rare combined problem**.

Routes already visible in the candidate literature include cardiac palliation/repair before hernia recognition, hernia-first management, direct combined/surgical approaches, and a modern RVOT-stent bridge before definitive combined repair.

Balloon pulmonary/RVOT palliation is established in TOF generally. Any defensible novelty in the index case must therefore be narrower: response-guided balloon-only palliation sufficient to omit a planned stent, interaction with the diaphragmatic lesion, growth-to-repair strategy, and the later definitive course.

No route is currently claimed superior.

## Gate 1 remains open

Outstanding before Phase 1 closure:

- source-native PubMed exact counts/export for all calibrated families;
- Europe PMC exact counts/export;
- PubMed/Europe PMC reconciliation;
- OpenAlex/Crossref enrichment/citation links;
- continued scholarly-web/Google Scholar sensitivity work;
- backward and forward citation saturation;
- full-text anatomy adjudication for anatomy-pending candidates;
- final raw collection freeze for Phase 2 normalization/deduplication.

The current browser-access route has not provided trustworthy machine-readable source-native custom-query counts; none have been fabricated. This is a reproducibility task still to close, not a scientific reason to stop the review.

## One-line handoff

**Continue on `case-report-01`; Phase 0 is locked, the private Case Core remains open through definitive surgery, and Phase 1 has expanded the direct-candidate literature through historical subcostosternal and Pentalogy sensitivity searches while keeping source-native reproducibility and citation saturation open.**
