# CAN-CCHD Phase 6 — Analysis Closeout

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **PHASE 6 ANALYSIS COMPLETE / FROZEN FOR WRITING**

## 1. Closeout decision

Phase 6 quantitative analysis is complete.

No scientific database amendment occurred after the Phase 6 database freeze. The 28-unit primary membership, denominators, Strict numerators and Expanded numerators remain unchanged.

The next scientific movement is manuscript/abstract writing, not further default analysis.

Any later correction to a scientific value requires an explicit dated `PHASE6_DATABASE_AMENDMENT` followed by a controlled rerun. Exploratory manuscript requests must not silently mutate the frozen analysis.

## 2. Frozen primary state

Canonical primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA: `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

Primary set:

- 28 PRIMARY_POOLABLE units;
- 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD outcomes;
- 1,015 Expanded CAN-CCHD outcomes.

Whole Phase 5 disposition remains:

- 76 quantitative units;
- 28 PRIMARY_POOLABLE;
- 40 SENSITIVITY_ONLY;
- 3 HOLD_PENDING_QA;
- 5 NOT_POOLABLE.

No HOLD, SENSITIVITY_ONLY or NOT_POOLABLE unit received a primary weight.

## 3. Authoritative primary results

### Strict CAN-CCHD

One-stage random-effects binomial-logistic-normal GLMM:

- median-study probability: **17.0%**;
- 95% profile-likelihood CI: **3.1%-46.8%**;
- marginal mean probability: **33.8%**;
- tau: **3.369**;
- 95% prediction interval: approximately **0.03%-99.34%**.

Interpretation is locked as extreme heterogeneity. The 17.0% estimate must not be presented as a universal patient-level frequency.

### Expanded CAN-CCHD

- median-study probability: **69.4%**;
- 95% CI: **57.7%-81.4%**;
- marginal mean probability: **65.8%**;
- tau: **1.110**;
- 95% prediction interval: **20.4%-95.2%**.

## 4. Core robustness complete

S1-S6 are complete:

- Expanded endpoint;
- corrected historical pre-amendment/pre-rerun framework;
- R125/SIBEN report-cluster aggregation;
- leave-one-out influence analysis;
- beta-binomial random-effects sensitivity;
- conventional two-stage logit REML/Hartung-Knapp comparison.

None reverses the scientific interpretation.

Key robustness checks:

- historical Strict 18.4%; Expanded 69.7%;
- R125 aggregation Strict 17.2%; Expanded 69.0%;
- leave-one-out Strict range 14.8%-21.1%; Expanded 65.3%-70.9%;
- beta-binomial marginal means Strict 33.5%, Expanded 66.3%.

## 5. Secondary etiologic outcomes complete

Audited derivation:

`data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`

Binding missingness rule:

> A non-reported or non-point-identifiable etiologic category is missing for that outcome, not zero.

Etiologic categories may overlap and are never summed to recreate Expanded CAN-CCHD.

Outcome-specific GLMMs:

- PPHN/pulmonary hypertension: **10.3%** (95% CI **4.7%-16.3%**), k=22, marginal mean 12.5%, tau 0.790;
- respiratory disease: **8.7%** (**1.6%-23.0%**), k=22, marginal mean 20.3%, tau 2.220;
- infection/sepsis: **16.7%** (**9.4%-24.2%**), k=22, marginal mean 18.9%, tau 0.720;
- other/non-target structural cardiac diagnosis: **26.6%** (**14.4%-43.0%**), k=26, marginal mean 33.0%, tau 1.556.

All four solutions were stable across quadrature orders 21/31/41/61.

## 6. Subgroup/meta-regression audit complete

Timing distribution:

- predominantly <24 h: 13 units;
- predominantly >=24 h: 6 units;
- mixed/uncertain: 9 units.

The >=24 h Strict subgroup contains only 3 events/97, has extreme estimated tau and lacks reproducible profile-likelihood bracketing. **No authoritative pooled Strict estimate is promoted for this subgroup.**

Timing omnibus GLMM meta-regression diagnostic:

- Strict: LR chi-square(2)=2.67, p=0.263, residual tau approximately 3.06;
- Expanded: LR chi-square(2)=1.41, p=0.493, residual tau approximately 1.07.

No clear timing effect is demonstrated; this is not evidence of equivalence.

Setting and altitude meta-regressions were formally judged infeasible because of sparse/unbalanced covariate structure.

## 7. Small-study / reporting-bias decision complete

Formal Egger/Begg tests, trim-and-fill and conventional funnel inference are **not promoted** for this single-proportion synthesis with boundary estimates and strong genuine heterogeneity.

Canonical decision:

`docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`

Reporting bias cannot be statistically excluded; it will be addressed as a limitation and through the broad search/retrieval strategy, not via a funnel-derived adjusted estimate.

## 8. Reporting QA completed

The closeout QA verified:

1. the frozen primary input was not edited after results were seen;
2. all 28 primary unit IDs and denominators remain canonical;
3. primary Strict/Expanded values in narrative documents agree with machine-readable results;
4. sensitivity values agree with `phase6_sensitivity_results.csv`;
5. etiologic study subsets agree with the audited derivation table;
6. `NOT_POINT_IDENTIFIABLE` etiologic fields are never converted to zero;
7. etiologic overlap is explicitly preserved;
8. the fragile >=24 h Strict model is not promoted;
9. setting/altitude inference is not forced;
10. crude aggregate ratios are labelled descriptive only;
11. study-level display intervals are exact binomial intervals and do not define GLMM weights;
12. no legacy Browser Agent/app database contributed a scientific value;
13. the secondary reproducibility script and machine-readable outputs now physically exist in the repository;
14. no formal publication-bias statistic is interpreted as evidence of absence of bias.

## 9. Reproducibility inventory

### Frozen inputs

- `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
- `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`
- `data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`

### Executable analysis

- `analysis/phase6/run_phase6_meta.py`
- `analysis/phase6/run_phase6_secondary.py`

### Machine-readable results

- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_secondary_results.json`
- `analysis/phase6/results/phase6_study_results.csv`
- `analysis/phase6/results/phase6_etiology_study_results.csv`
- `analysis/phase6/results/phase6_sensitivity_results.csv`
- `analysis/phase6/results/phase6_leave_one_out.csv`
- `analysis/phase6/results/phase6_subgroup_results.csv`

### Figures

- `analysis/phase6/figures/forest_strict.svg`
- `analysis/phase6/figures/forest_expanded.svg`

### Interpretation/reporting locks

- `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
- `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
- `docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`
- `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
- this closeout document.

## 10. Main-paper figure/table decision

Main manuscript quantitative presentation:

- Table 1: primary + etiologic random-effects estimates;
- Table 2: robustness/sensitivity analyses;
- Table 3: timing subgroup audit;
- Figure 1: Strict forest plot;
- Figure 2: Expanded forest plot;
- PRISMA flow diagram during manuscript assembly.

No main-paper funnel plot. Four separate etiologic forest plots are not required; they may be generated for supplementary material only if the journal/review process benefits from them.

Canonical captions and manuscript-ready results wording are in:

`docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`.

## 11. Phase transition

**PHASE 6 IS CLOSED AS ANALYSIS-COMPLETE.**

The next phase is manuscript/abstract writing. In the older workflow nomenclature this corresponds to moving from Analysis (legacy Phase 10) to Writing (Phase 11).

Recommended writing order:

1. SHA abstract;
2. manuscript Results using the locked results package;
3. Methods/statistical analysis section;
4. Discussion and limitations;
5. PRISMA/search-flow assembly;
6. tables/figures/supplement final formatting;
7. human scientific review and journal-specific adaptation.

## 12. One-line closeout

**The restart-native database is frozen and unchanged; primary, sensitivity, etiologic, subgroup and reporting-bias decisions are complete and reproducible. Phase 6 analysis is closed. Begin Phase 11 writing from the manuscript-ready results package without reopening extraction or changing scientific values unless a formal amendment is justified.**
