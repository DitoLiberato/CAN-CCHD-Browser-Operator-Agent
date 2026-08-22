# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> Read this file before interpreting any Phase file, CSV, snapshot, database, result file, draft, or historical note.

Last updated: **2026-08-22**  
Current scientific/writing branch: **`phase11-writing`**  
Frozen analysis branch: **`phase6-analysis`**  
Current safe-resume snapshot: **`docs/PHASE11_PROGRESS_SNAPSHOT_2026-08-22_SHA_DRAFT_STARTED.md`**  
Snapshot creation commit: **`fd15b2ad273d71758400d52e58d57a6b10775b80`**  
Current phase status: **PHASE 11 — SHA ABSTRACT DRAFTING STARTED / PHASE 6 FROZEN**

---

## 1. Mandatory new-chat procedure

Read, in order:

1. `CURRENT_STATE.md`
2. `docs/PHASE11_PROGRESS_SNAPSHOT_2026-08-22_SHA_DRAFT_STARTED.md`
3. `docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.1.md`
4. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
5. `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
6. `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
7. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
8. `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
9. `analysis/phase6/results/phase6_primary_results.json`
10. `analysis/phase6/results/phase6_secondary_results.json`

Do not reopen extraction or alter frozen scientific values during writing.

---

## 2. Phase 6 frozen scientific state

Phase 6 closed on branch `phase6-analysis` at commit `310487b2c2795bcb070ed1b4c138f394e16cab52`.

Canonical primary input remains:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA: `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

Primary set:

- 28 PRIMARY_POOLABLE units;
- 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD outcomes;
- 1,015 Expanded CAN-CCHD outcomes.

Whole 76-unit disposition remains 28 PRIMARY_POOLABLE / 40 SENSITIVITY_ONLY / 3 HOLD_PENDING_QA / 5 NOT_POOLABLE.

No scientific database amendment occurred during Phase 6.

---

## 3. Authoritative results available for writing

Strict CAN-CCHD:

- median-study probability **17.0%**;
- 95% CI **3.1%-46.8%**;
- marginal mean **33.8%**;
- tau **3.369**;
- prediction interval approximately **0.03%-99.34%**.

Expanded CAN-CCHD:

- median-study probability **69.4%**;
- 95% CI **57.7%-81.4%**;
- marginal mean **65.8%**;
- tau **1.110**;
- prediction interval **20.4%-95.2%**.

Etiologic median-study estimates:

- PPHN/pulmonary hypertension **10.3%**;
- respiratory disease **8.7%**;
- infection/sepsis **16.7%**;
- other/non-target structural cardiac diagnosis **26.6%**.

S1-S6 robustness is complete. Timing did not demonstrate a clear omnibus subgroup effect; the >=24 h Strict subgroup is too sparse and unstable for a promoted inferential estimate. Setting/altitude meta-regressions are infeasible. No inferential funnel/trim-and-fill result is promoted.

---

## 4. Current Phase 11 artifact

SHA abstract draft:

`docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.1.md`

Status: **draft_requires_human_review**.

Proposed title:

`Clinically Actionable Non-CCHD Diagnoses After Failed Newborn Pulse Oximetry Screening: A Systematic Review and Meta-analysis`

Current abstract body: **248 words** by repository whitespace count.

Current SHA37 requirements checked 2026-08-22:

- English;
- title <=40 words;
- abstract <=300 words including Introduction, Methodology, Results and Conclusion;
- original unpublished contribution;
- one optional figure/table;
- published deadline 31 August 2026.

Conference requirements must be rechecked immediately before portal submission.

---

## 5. Exact next movement

Review and refine SHA abstract v0.1 into v0.2, focusing on:

1. title/central framing: `Clinically Actionable` versus broader `Beyond False Positives` message;
2. whether all four etiologic outcomes justify abstract space;
3. how much statistical-estimand detail is needed for a conference audience while preserving the extreme-heterogeneity warning;
4. final portal word count and submission metadata.

After locking the SHA abstract, proceed to manuscript Results, Methods/statistical analysis, Discussion/limitations, PRISMA/search-flow and journal-specific formatting.

---

## 6. Critical legacy firewall

The old Browser Agent/app/database artifacts remain historical only and must never be used to alter current scientific values, eligibility decisions, diagnoses, denominators, numerators or weights.

Any genuine scientific correction during writing requires a formal dated Phase 6 database amendment and controlled rerun before prose is updated.

---

## 7. One-line handoff

**PHASE 11 STARTED on `phase11-writing`. Phase 6 remains frozen; SHA abstract v0.1 exists within the current 300-word SHA limit. Review/lock the abstract next without reopening analysis.**
