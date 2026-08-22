# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> Read this file before interpreting any Phase file, CSV, snapshot, extraction block, database, result file, or historical note.

Last updated: **2026-08-22**  
Current scientific branch: **`phase6-analysis`**  
Current safe-resume snapshot: **`docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`**  
Snapshot creation commit: **`7d28a261999e5fd0f3872343b93c7e4ceea48b4b`**  
Current phase status: **PHASE 6 ANALYSIS COMPLETE / PHASE 11 WRITING NEXT**

---

## 1. Mandatory new-chat procedure

Read, in order:

1. `CURRENT_STATE.md`
2. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
3. `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
4. `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
5. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
6. `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
7. `docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`
8. `analysis/phase6/results/phase6_primary_results.json`
9. `analysis/phase6/results/phase6_secondary_results.json`
10. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
11. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`

Do not reopen extraction or change frozen scientific values by default.

---

## 2. Frozen scientific database

Primary canonical input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

Primary analysis set:

- 28 unique PRIMARY_POOLABLE units;
- 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD outcomes;
- 1,015 Expanded CAN-CCHD outcomes.

Whole Phase 5 disposition remains:

- 76 quantitative units total;
- 28 PRIMARY_POOLABLE;
- 40 SENSITIVITY_ONLY;
- 3 HOLD_PENDING_QA;
- 5 NOT_POOLABLE.

No scientific database field was changed after quantitative results were inspected. Any genuine later correction requires an explicit dated `PHASE6_DATABASE_AMENDMENT` and controlled rerun.

---

## 3. Authoritative core meta-analysis

Primary model: one-stage random-effects binomial-logistic-normal GLMM with exact binomial likelihood, logit link, no continuity correction.

### Strict CAN-CCHD

- median-study probability: **17.0%**;
- 95% profile-likelihood CI: **3.1%-46.8%**;
- marginal mean probability: **33.8%**;
- tau: **3.369**;
- 95% prediction interval: approximately **0.03%-99.34%**.

Interpretation: **extreme between-study heterogeneity**. Never report 17.0% as a universal patient-level frequency or without the marginal mean/tau/prediction interval.

### Expanded CAN-CCHD

- median-study probability: **69.4%**;
- 95% CI: **57.7%-81.4%**;
- marginal mean probability: **65.8%**;
- tau: **1.110**;
- 95% prediction interval: **20.4%-95.2%**.

Core S1-S6 robustness is complete and does not reverse the interpretation.

---

## 4. Secondary etiologic analysis complete

Audited derivation:

`data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`

Binding rule: an etiologic category that is not point-identifiable is **missing for that outcome, never zero**. Etiologic categories may overlap and must not be summed.

Random-effects GLMM results:

- PPHN/pulmonary hypertension: **10.3%** (95% CI **4.7%-16.3%**), k=22;
- respiratory disease: **8.7%** (**1.6%-23.0%**), k=22;
- infection/sepsis: **16.7%** (**9.4%-24.2%**), k=22;
- other/non-target structural cardiac diagnosis: **26.6%** (**14.4%-43.0%**), k=26.

All four etiologic solutions were stable across quadrature 21/31/41/61.

---

## 5. Subgroup/meta-regression audit complete

Timing groups:

- predominantly <24 h: 13 units;
- predominantly >=24 h: 6 units;
- mixed/uncertain: 9 units.

Timing omnibus diagnostic:

- Strict p=**0.263**;
- Expanded p=**0.493**.

No clear timing-group effect is demonstrated; this is not evidence of equivalence.

The >=24 h Strict subgroup has only **3 events/97**, extreme tau and non-reproducible profile-likelihood bracketing. No authoritative pooled Strict estimate is promoted for that subgroup.

Setting and altitude meta-regression are infeasible because covariate structure is too sparse/unbalanced.

---

## 6. Small-study/reporting-bias decision

Formal Egger/Begg tests, trim-and-fill and conventional funnel inference are not promoted for this single-proportion meta-analysis with boundary estimates and strong genuine heterogeneity.

Reporting bias cannot be excluded statistically. See:

`docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`.

No funnel-derived adjusted pooled estimate belongs in the manuscript.

---

## 7. Reproducibility outputs

Scripts:

- `analysis/phase6/run_phase6_meta.py`
- `analysis/phase6/run_phase6_secondary.py`

Machine-readable results:

- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_secondary_results.json`
- `analysis/phase6/results/phase6_study_results.csv`
- `analysis/phase6/results/phase6_etiology_study_results.csv`
- `analysis/phase6/results/phase6_sensitivity_results.csv`
- `analysis/phase6/results/phase6_leave_one_out.csv`
- `analysis/phase6/results/phase6_subgroup_results.csv`

Figures:

- `analysis/phase6/figures/forest_strict.svg`
- `analysis/phase6/figures/forest_expanded.svg`

Manuscript-ready table/caption/wording package:

`docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`.

---

## 8. Phase 6 closeout

Canonical closeout:

`docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`

**Phase 6 is analysis-complete.** The restart-native Analysis phase corresponds functionally to legacy workflow Phase 10. The next movement is **Phase 11 — Writing**.

Recommended order:

1. SHA abstract;
2. manuscript Results;
3. Methods/statistical analysis;
4. Discussion/limitations;
5. PRISMA/search-flow assembly;
6. journal-specific tables/figures/supplement formatting;
7. human scientific review.

---

## 9. Critical legacy firewall

The systematic review was rebuilt from scratch.

The old Browser Agent, old application databases, `can_cchd.db`, `data/processed/can_cchd_agent.db`, and related legacy artifacts are **historical only** and must never be used to alter current scientific values, eligibility decisions, diagnoses, denominators, numerators or weights.

Use only restart-native frozen scientific artifacts.

---

## 10. One-line handoff

**PHASE 6 ANALYSIS COMPLETE. Database frozen and unchanged; Strict median-study 17.0% with extreme heterogeneity, Expanded 69.4%; S1-S6, etiologic outcomes, subgroup feasibility, reporting-bias decision, tables/captions and reporting QA complete. Start Phase 11 from `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`.**
