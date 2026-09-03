# Case Report + Review — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR THIS BRANCH**

Last updated: **2026-09-03**  
Branch: **`case-report-01`**  
Parent architecture: **`phase11-writing`**  
Current status: **PHASE 0 LOCKED; PHASE 0.5 PRIVATE CASE CORE IN PROGRESS; PHASE 1 SCIENTIFIC DISCOVERY CLOSED AT SATURATION; FORMAL GATE 1 OPEN FOR NATIVE COUNT/EXPORT BACKFILL ONLY**

## Privacy boundary

This repository is public. Patient-level source documents and potentially identifying clinical details remain outside this branch until explicit privacy/consent clearance.

The branch may contain methodology, de-identification-safe templates, systematic-review artifacts, privacy-safe project-state summaries, and later manuscript material only after privacy review.

The branch must not contain direct patient identifiers, original patient source PDFs, clinical images, or a detailed rare-case Case Core before consent/privacy clearance.

## Start here

Read in this order:

1. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
2. `docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`
3. `docs/PHASE1_SCIENTIFIC_SEARCH_CLOSEOUT_v1.0.md`
4. `docs/PHASE1_SATURATION_AUDIT_v1.0.md`
5. `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.3_SATURATION.csv`
6. `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.2.md`
7. `docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md`
8. `docs/PHASE0_05_PROGRESS_SNAPSHOT_2026-09-03.md`
9. `docs/PROJECT_DECISION_RECORD_v0.2.md`
10. `docs/CASE_REPORT_REVIEW_HANDOFF.md`
11. `case/CASE_CORE_TEMPLATE.md`

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

## Phase 1 — SCIENTIFIC DISCOVERY CLOSED AT SATURATION

Canonical closeout artifacts:

- `docs/PHASE1_SCIENTIFIC_SEARCH_CLOSEOUT_v1.0.md`
- `docs/PHASE1_SATURATION_AUDIT_v1.0.md`
- `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.3_SATURATION.csv`

Earlier Phase 1 logs/registries remain provenance history.

### Saturation decision

**DISCOVERY / CITATION SATURATION = PASS.**

Independent discovery pathways included modern direct terminology, historical/subcostosternal terminology, broad TOF + CDH sensitivity, Cantrell/anterior-midline searches, hidden-case mining inside Morgagni series, adult/repaired-TOF searches, multilingual searches, recent/grey literature, backward/forward citation chasing, large-series anomaly mining and final exact/semantic plateau checks.

After the final productive hidden-series/adult waves, multiple conceptually independent late waves produced no additional individually extractable direct patient.

### Raw literature signal at saturation

The current registry contains:

- **8 individually identifiable direct candidate records/patient-level reports** with explicit or historically equivalent TOF + Morgagni signal, pending Phase 2 identity reconciliation and Phase 5 eligibility;
- **2 additional aggregate TOF-associated Morgagni patients** reported in the Ortiz 2025 55-patient series, without sufficient patient-level mapping for individual extraction;
- additional aggregate/unresolved cardiac-series signals preserved without inflating direct patient counts;
- one high-value TOF + large-CDH management analog whose Morgagni anatomy remains unresolved;
- explicit non-Morgagni negative/anatomic controls.

Publication count is not patient count. No final unique-case number is frozen in Phase 1.

### Important late recoveries

- Johnson & Mangiardi 1952 — historical subcostosternal/Morgagni-equivalent TOF case.
- Sönmez et al. 2006 — TOF patient hidden inside a Morgagni case-series table.
- Rao et al. 2014 — repaired-TOF adult with large Morgagni and competing-physiology/conservative management route.
- Veejeyahshegarun et al. 2024 — hernia-first Pentalogy/Morgagni + TOF case-level abstract.
- Ortiz et al. 2025 — two TOF patients embedded at aggregate level within 55 Morgagni cases.

These findings validate the decision to search beyond exact case-report titles.

### Scientific framing after saturation

The association itself is not novel. The literature is rare but sufficiently diverse to support the intended educational framing: **different practical routes through a rare combined cardiorespiratory problem**.

TOF balloon pulmonary/RVOT palliation is established generally. The saturated direct search did not identify a patient-level TOF–Morgagni report clearly matching the narrower pattern of satisfactory balloon response leading to intentional omission of a planned RVOT stent. This is a provisional search finding, not a final novelty claim.

No management route is currently claimed superior.

## Formal Gate 1 — TECHNICAL SUBGATE OPEN ONLY

The scientific search should **not** be broadened further merely to generate more records.

The only remaining Phase 1 requirement is reproducibility backfill:

1. obtain exact source-native PubMed counts/exports for the locked calibrated families;
2. obtain exact Europe PMC counts/exports;
3. reconcile those exports against the saturated registry;
4. freeze the raw Phase 1 collection for Phase 2 normalization/deduplication.

The current access route has not exposed trustworthy machine-readable source-native custom-query counts. None have been fabricated or inferred.

## One-line handoff

**Continue on `case-report-01`; Phase 0 is locked, the private Case Core remains open through definitive surgery, and Phase 1 scientific discovery has passed saturation. Do not expand searching further without a new signal; complete only PubMed/Europe PMC native count/export backfill, reconcile, freeze the raw collection, then proceed to Phase 2.**
