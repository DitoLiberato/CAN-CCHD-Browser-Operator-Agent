# Case Report 01 — Handoff

**Branch:** `case-report-01`  
**Last updated:** 2026-09-03  
**Status:** **Pipeline v1.0 frozen; Phase 0 locked; Phase 0.5 private Case Core in progress; Phase 1 active — sensitivity wave 2 complete, Gate 1 open.**

## Read first

1. `CURRENT_STATE.md`
2. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
3. `docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`
4. `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.2.md`
5. `docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md`
6. `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.2.csv`
7. `docs/PHASE0_05_PROGRESS_SNAPSHOT_2026-09-03.md`
8. `docs/PROJECT_DECISION_RECORD_v0.2.md`
9. `case/CASE_CORE_TEMPLATE.md`

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

## Phase 1 — ACTIVE

Current Phase 1 source-of-truth:

- `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.2.md`
- `docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md`
- `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.2.csv`

### Candidate registry — current raw signal

Six records currently have explicit or historically equivalent Morgagni/subcostosternal signal, plus one high-value anatomy-pending Pentalogy/CDH case.

1. **Johnson & Mangiardi, 1952** — `Subcostosternal diaphragmatic hernia` — abstract explicitly reports coexistence with TOF. Historical terminology is anatomically equivalent to Morgagni-type defect; full-text confirmation required.
2. **Goldstein et al., 2006, Eurorad** — bilateral Morgagni + Down syndrome + TOF; modified BT shunt in infancy and later definitive TOF repair before/around later hernia recognition.
3. **Kumar et al., 2015, Ann Thorac Surg** — PMID 25639421 — TOF + Morgagni + Down syndrome.
4. **Aironi et al., 2015, J Card Surg** — PMID 25976041 — TOF + Morgagni.
5. **Venugopal et al., 2016, Chirurgia** — TOF + Morgagni with reported successful surgical outcome.
6. **Veejeyahshegarun et al., 2024 conference abstract** — Pentalogy of Cantrell with operative Morgagni repair and postoperative TOF diagnosis; hernia-first pathway and poor neonatal outcome.
7. **Zhu et al., Epub 2025 / issue 2026** — TOF + large CDH in Pentalogy of Cantrell, RVOT stent first, then definitive combined cardiac/diaphragmatic repair; direct-set status waits for full-text confirmation of Morgagni anatomy. At minimum this is a high-value management analog.

This is **not** the frozen corpus and these are not yet frozen unique-patient counts.

### Important calibration findings

- association itself is not novel;
- direct literature remains small enough to enumerate;
- historical `subcostosternal` terminology is essential and must be explicitly searched;
- broad TOF + CDH queries are necessary but produce anatomic noise;
- Pentalogy of Cantrell is a necessary sensitivity route but does not automatically prove Morgagni anatomy;
- multilingual modern-term sweep has not added further direct cases so far;
- Hatherley 1950 is confirmed posterolateral and therefore contextual, not direct;
- balloon pulmonary/RVOT dilation is established palliation in TOF generally;
- current literature already displays different management routes, which supports the intended educational framing rather than a novelty-by-association framing.

### Working teaching angle — not yet manuscript conclusion

The article is increasingly positioned as a comparison of **different legitimate routes through a rare combined cardiorespiratory problem**:

- cardiac palliation/repair before hernia recognition;
- hernia-first management;
- direct/combined repair pathways;
- RVOT-stent bridge to later repair;
- index-case response-guided balloon-only palliation with planned growth before definitive correction.

No route is claimed superior.

### Gate 1 remaining work

1. Source-native PubMed exact counts/export for calibrated query families.
2. Europe PMC exact counts/export.
3. PubMed/Europe PMC reconciliation.
4. OpenAlex/Crossref metadata enrichment and citation-link recovery.
5. Continued scholarly-web/Google Scholar sensitivity searching.
6. Backward citation chase of all direct candidates, especially Johnson 1952.
7. Forward citation chase of all direct candidates.
8. Full-text anatomy adjudication for anatomy-pending candidates.
9. Provenance/eligibility adjudication of clinical repository and conference-abstract formats at Phase 5.
10. Raw collection freeze for Phase 2 normalization/deduplication.

The current browser-access route has not exposed reliable machine-readable custom-query counts from PubMed/Europe PMC. No count has been guessed. This keeps Gate 1 open but is not a scientific stop condition.

## Privacy rule

Until explicit consent/privacy clearance:

- no original patient PDF;
- no direct identifiers;
- no detailed rare-case chronology in public GitHub;
- no clinical images;
- no public Case Core.

## One-line resume prompt

**Continue Case Report 01 on `case-report-01`. Phase 0 is locked to the full staged-course endpoint; keep the Case Core private through definitive surgery and continue Phase 1 source-native collection, historical/citation saturation and anatomy adjudication using the v0.2 candidate registry.**
