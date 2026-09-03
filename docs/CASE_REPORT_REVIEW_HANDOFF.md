# Case Report 01 — Handoff

**Branch:** `case-report-01`  
**Last updated:** 2026-09-03  
**Status:** **Pipeline v1.0 frozen; Phase 0 locked; Phase 0.5 private Case Core in progress; Phase 1 scientific discovery CLOSED AT SATURATION; formal Gate 1 open only for native PubMed/Europe PMC count/export backfill.**

## Read first

1. `CURRENT_STATE.md`
2. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
3. `docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`
4. `docs/PHASE1_SCIENTIFIC_SEARCH_CLOSEOUT_v1.0.md`
5. `docs/PHASE1_SATURATION_AUDIT_v1.0.md`
6. `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.3_SATURATION.csv`
7. `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.2.md`
8. `docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md`
9. `docs/PHASE0_05_PROGRESS_SNAPSHOT_2026-09-03.md`
10. `docs/PROJECT_DECISION_RECORD_v0.2.md`
11. `case/CASE_CORE_TEMPLATE.md`

## Scientific architecture

Two independent streams remain firewalled until Phase 7:

- **CASE STREAM** — verified facts of the index case from primary clinical sources;
- **LITERATURE STREAM** — verified published evidence from reproducible search and review.

Literature cannot rewrite historical case facts. Case features may motivate sensitivity searches but cannot determine which published evidence is accepted.

## Phase 0 — CLOSED

The locked source is:

`docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`

Article design:

> **Case report with an embedded systematic review of reported cases.**

Direct set:

> unique published human patients with coexisting TOF and Morgagni-type anterior/subcostosternal diaphragmatic hernia.

Trisomy 21 is a comparison/modifier axis, not an inclusion criterion.

Publication endpoint:

> **full staged clinical course through definitive correction of the diaphragmatic lesion and cardiac defect, with initial postoperative/early follow-up.**

An earlier bridge-only endpoint requires explicit Phase 0 amendment.

## Phase 0.5 — PRIVATE / IN PROGRESS

Private artifact outside GitHub:

`CASE_CORE_PRIVATE_v0.1.md`

The Case Core remains open through definitive surgery and early outcome.

Priority future sources:

- complete catheterization report/measurements and balloon details;
- ward/discharge documentation;
- outpatient symptom and growth trajectory;
- definitive diaphragmatic and cardiac operative documentation;
- early postoperative outcome;
- guardian publication consent;
- institutional ethics/IRB determination.

## Phase 1 — SCIENTIFIC DISCOVERY CLOSED

Canonical search closeout:

- `docs/PHASE1_SCIENTIFIC_SEARCH_CLOSEOUT_v1.0.md`
- `docs/PHASE1_SATURATION_AUDIT_v1.0.md`
- `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.3_SATURATION.csv`

### Saturation

**PASS.**

The search moved beyond title-driven case finding and covered:

- modern TOF + Morgagni terminology;
- historical `subcostosternal`/Larrey/anterior terminology;
- broad TOF + congenital diaphragmatic hernia sensitivity;
- Pentalogy of Cantrell/anterior-midline pathways;
- hidden cases in Morgagni case series;
- adult/repaired-TOF presentations;
- multilingual searching;
- recent/grey literature;
- backward and forward citation chasing;
- large-series anomaly mining;
- final exact/semantic plateau waves.

After the last productive late waves, multiple independent searches produced no new individually extractable direct patient.

### Saturation registry — raw signal

The v0.3 registry currently preserves:

- **8 individually identifiable direct candidate records/patient-level reports**, pending Phase 2 report-to-patient reconciliation and Phase 5 eligibility;
- **2 additional TOF-associated Morgagni patients at aggregate level** in Ortiz et al. 2025, without enough individual mapping for extraction;
- unresolved aggregate cardiac signals that must not be converted into case counts;
- one anatomy-pending TOF + large-CDH case retained at least as a management analog;
- non-Morgagni negative/anatomic controls.

Do not report these as a final number of unique patients until Phase 2/5 resolve independence and eligibility.

### Most important late Phase 1 discoveries

1. **Sönmez et al. 2006** — a direct TOF patient hidden inside a Morgagni case-series table; this would have been missed by title-only searching.
2. **Rao et al. 2014** — repaired TOF + large Morgagni in adulthood, with the clinical team attributing symptoms primarily to noncardiac/respiratory physiology and managing the hernia conservatively.
3. **Ortiz et al. 2025** — a 55-patient pediatric Morgagni series containing two TOF patients, currently only aggregate-level.
4. Historical and Cantrell pathways retained Johnson 1952 and the 2024 hernia-first case.

### Working teaching angle after saturation

The literature now supports the planned educational framing more strongly than a rarity-only narrative:

> **different routes through a rare combined cardiorespiratory problem.**

The direct/context corpus contains cardiac-first, hernia-first, staged/combined, conservative and device-bridge patterns.

Balloon pulmonary/RVOT palliation is not novel in TOF generally. The saturated direct search did **not identify** a patient-level TOF–Morgagni report clearly matching the narrower pattern of a planned RVOT stent being intentionally omitted after a satisfactory balloon-only response. This is only a provisional search finding; full-text extraction and Phase 10 must adjudicate any novelty language.

No route is claimed superior.

## Formal Gate 1 — ONLY REPRODUCIBILITY BACKFILL REMAINS

Do **not** restart or broaden discovery searching solely to increase record numbers.

Remaining controlled tasks:

1. run the already locked calibrated families natively in PubMed and preserve exact hit counts/export;
2. run them natively in Europe PMC and preserve exact hit counts/export;
3. reconcile these source-native exports against the saturated registry;
4. freeze the raw Phase 1 collection;
5. then begin Phase 2 normalization/deduplication.

The current access route did not provide trustworthy source-native custom-query counts. None have been guessed or retrofitted.

## Privacy rule

Until explicit consent/privacy clearance:

- no original patient PDF;
- no direct identifiers;
- no detailed rare-case chronology in public GitHub;
- no clinical images;
- no public Case Core.

## One-line resume prompt

**Continue Case Report 01 on `case-report-01`. Phase 0 is locked to the full staged-course endpoint, the Case Core remains private through definitive surgery, and Phase 1 scientific discovery has reached saturation. Complete only the native PubMed/Europe PMC count/export reproducibility backfill, reconcile and freeze the raw collection, then proceed to Phase 2.**
