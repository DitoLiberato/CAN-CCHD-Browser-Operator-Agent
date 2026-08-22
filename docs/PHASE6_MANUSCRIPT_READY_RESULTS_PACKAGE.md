# CAN-CCHD Phase 6 — Manuscript-ready Results Package

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **TABLES / FIGURE STRATEGY / RESULTS WORDING LOCKED FOR DRAFTING**

## 1. Primary quantitative table

**Table 1. Random-effects proportional synthesis among harmonized-CCHD-negative final failed pulse-oximetry screens**

| Outcome | k | Observed events / denominator* | Median-study pooled probability, % (95% CI) | Marginal mean, % | tau | 95% prediction interval, % |
|---|---:|---:|---:|---:|---:|---:|
| Strict CAN-CCHD | 28 | 638 / 1,999 | **17.0 (3.1-46.8)** | **33.8** | **3.369** | **0.03-99.34** |
| Expanded CAN-CCHD | 28 | 1,015 / 1,999 | **69.4 (57.7-81.4)** | **65.8** | **1.110** | **20.4-95.2** |
| PPHN / pulmonary hypertension | 22 | 148 / 1,071 | **10.3 (4.7-16.3)** | **12.5** | **0.790** | **2.4-35.1** |
| Respiratory disease | 22 | 126 / 1,063 | **8.7 (1.6-23.0)** | **20.3** | **2.220** | **0.12-88.1** |
| Infection / sepsis | 22 | 212 / 1,063 | **16.7 (9.4-24.2)** | **18.9** | **0.720** | **4.7-45.1** |
| Other/non-target structural cardiac diagnosis | 26 | 280 / 1,952 | **26.6 (14.4-43.0)** | **33.0** | **1.556** | **1.7-88.4** |

\*Observed event/denominator totals are descriptive aggregates, not the random-effects estimates. Etiologic outcomes have outcome-specific reporting subsets; categories can overlap and must not be summed.

### Interpretation lock for Table 1

- The **17.0% Strict estimate is the median-study true probability**, not a universal patient-level rate.
- Because Strict heterogeneity is extreme, the manuscript must report the marginal mean, tau and prediction interval alongside the pooled median-study probability.
- Expanded CAN-CCHD is substantially more consistent and shows that clinically relevant non-target disease is common even when strict actionability documentation is unavailable.
- The respiratory outcome shows a particularly large separation between the median-study and marginal mean estimands, reflecting strong heterogeneity and the influence of high-yield programs.

## 2. Robustness table

**Table 2. Core sensitivity and robustness analyses**

| Analysis | Endpoint | k | Estimate, % (95% CI where applicable) | tau / heterogeneity | Interpretation |
|---|---|---:|---:|---:|---|
| Historical pre-amendment/pre-rerun framework | Strict | 26 | 18.4 (1.9-59.5) | 4.026 | Historical framework; not a pure one-variable d-TGA causal contrast |
| Historical pre-amendment/pre-rerun framework | Expanded | 26 | 69.7 (56.0-83.7) | 1.229 | No reversal |
| R125/SIBEN report-cluster aggregation | Strict | 27 | 17.2 (3.8-43.8) | 3.037 | No material change |
| R125/SIBEN report-cluster aggregation | Expanded | 27 | 69.0 (57.2-81.0) | 1.104 | No material change |
| Beta-binomial random-effects sensitivity | Strict | 28 | 33.5 marginal mean | — | Closely matches GLMM marginal mean 33.8% |
| Beta-binomial random-effects sensitivity | Expanded | 28 | 66.3 marginal mean | — | Closely matches GLMM marginal mean 65.8% |
| Conventional logit REML/Hartung-Knapp | Strict | 28 | 29.9 (16.8-47.4) | tau 1.439; I² 85.9% | Supportive only; continuity-corrected two-stage model |
| Conventional logit REML/Hartung-Knapp | Expanded | 28 | 60.4 (51.1-69.0) | tau 0.677; I² 73.5% | Supportive only |
| Leave-one-out | Strict | 28 refits | pooled range 14.8-21.1 | tau 2.85-3.62 | No single unit reverses conclusion |
| Leave-one-out | Expanded | 28 refits | pooled range 65.3-70.9 | tau 0.91-1.18 | No single unit reverses conclusion |

The exact-binomial one-stage GLMM remains authoritative. Conventional two-stage results are comparability analyses only.

## 3. Timing/subgroup table

**Table 3. Prespecified screening-timing subgroup audit**

| Timing group | Endpoint | k | Observed events / denominator | Median-study estimate, % (95% CI) | Marginal mean, % | tau |
|---|---|---:|---:|---:|---:|---:|
| Predominantly <24 h | Strict | 13 | 564 / 1,733 | 28.4 (5.0-67.7) | 37.9 | 2.444 |
| Predominantly <24 h | Expanded | 13 | 842 / 1,733 | 62.6 (45.9-80.4) | 60.4 | 1.035 |
| Predominantly >=24 h | Strict | 6 | **3 / 97** | **Not promoted: numerically fragile** | — | approximately 6-7 |
| Predominantly >=24 h | Expanded | 6 | 61 / 97 | 80.8 (50.1-99.2) | 74.7 | 1.341 |
| Mixed/uncertain | Strict | 9 | 71 / 169 | 26.7 (0.7-90.4) | 39.5 | 3.371 |
| Mixed/uncertain | Expanded | 9 | 112 / 169 | 73.3 (52.2-91.0) | 70.0 | 0.975 |

Timing meta-regression omnibus diagnostic:

- Strict: LR chi-square(2) = 2.67, **p=0.263**, residual tau approximately 3.06.
- Expanded: LR chi-square(2) = 1.41, **p=0.493**, residual tau approximately 1.07.

Interpretation: no clear timing-group effect was demonstrated, but this is not evidence of equivalence. The >=24 h Strict subgroup is weakly identified. Setting and altitude meta-regression were judged infeasible because of sparse/unbalanced covariate structure.

## 4. Reporting-bias decision

No inferential Egger/Begg/trim-and-fill or conventional funnel-plot analysis is promoted. See:

`docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`

A funnel-derived bias-adjusted pooled estimate must not appear in the manuscript.

## 5. Main figure strategy

### Figure 1 — Strict CAN-CCHD forest plot

File:

`analysis/phase6/figures/forest_strict.svg`

**Caption:**

> **Figure 1. Study-level Strict CAN-CCHD proportions among harmonized-CCHD-negative final failed pulse-oximetry screens.** Points show observed study/unit proportions and horizontal lines show exact binomial 95% confidence intervals; event counts and denominators are displayed for each unit. The authoritative random-effects synthesis used a one-stage binomial-logistic-normal GLMM without continuity correction. The pooled median-study probability was 17.0% (95% profile-likelihood CI 3.1%-46.8%), with marginal mean 33.8%, tau 3.369, and a 95% prediction interval of approximately 0.03%-99.34%, indicating extreme between-study heterogeneity.

### Figure 2 — Expanded CAN-CCHD forest plot

File:

`analysis/phase6/figures/forest_expanded.svg`

**Caption:**

> **Figure 2. Study-level Expanded CAN-CCHD proportions among harmonized-CCHD-negative final failed pulse-oximetry screens.** Expanded CAN-CCHD includes Strict CAN-CCHD plus clinically relevant diagnoses for which qualifying actionability was not directly demonstrated. Points show observed study/unit proportions and exact binomial 95% confidence intervals. The one-stage random-effects GLMM yielded a median-study probability of 69.4% (95% CI 57.7%-81.4%), marginal mean 65.8%, tau 1.110, and 95% prediction interval 20.4%-95.2%.

### Figure 3 — PRISMA flow diagram

The PRISMA diagram belongs in the main manuscript but is a review-flow/reporting figure rather than a Phase 6 statistical output. It should be finalized during manuscript assembly from the frozen search/screening counts.

## 6. Supplementary material strategy

Recommended supplementary items:

- study-level Strict/Expanded result table: `analysis/phase6/results/phase6_study_results.csv`;
- leave-one-out table: `analysis/phase6/results/phase6_leave_one_out.csv`;
- full sensitivity table: `analysis/phase6/results/phase6_sensitivity_results.csv`;
- audited etiologic derivation table: `data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`;
- study-level etiologic results: `analysis/phase6/results/phase6_etiology_study_results.csv`;
- timing subgroup output: `analysis/phase6/results/phase6_subgroup_results.csv`.

Four separate etiologic forest plots are **not required for the main manuscript**. They can be generated for the supplement if requested by reviewers or if the target journal's figure allowance permits them.

## 7. Manuscript-ready Results wording

A defensible first-pass Results summary is:

> Twenty-eight independent primary units contributed 1,999 harmonized-CCHD-negative final failed screens. There were 638 Strict CAN-CCHD outcomes and 1,015 Expanded CAN-CCHD outcomes; the corresponding crude aggregate ratios (31.9% and 50.8%) are descriptive only. In the prespecified one-stage random-effects binomial-logistic-normal GLMM, the Strict median-study probability was 17.0% (95% CI 3.1%-46.8%), while the marginal mean was 33.8%. Between-study heterogeneity was extreme (tau=3.369), with a 95% prediction interval spanning approximately 0.03%-99.34%. The Expanded endpoint was substantially higher and less heterogeneous: median-study probability 69.4% (95% CI 57.7%-81.4%), marginal mean 65.8%, tau=1.110, and prediction interval 20.4%-95.2%. Core sensitivity analyses, including the historical target framework, report-cluster aggregation, leave-one-out analyses, beta-binomial modelling and a conventional two-stage comparison, did not reverse the interpretation.

> In outcome-specific etiologic syntheses, PPHN/pulmonary hypertension occurred with a median-study probability of 10.3% (95% CI 4.7%-16.3%), infection/sepsis 16.7% (9.4%-24.2%), respiratory disease 8.7% (1.6%-23.0%), and other structural cardiac diagnoses outside the harmonized target 26.6% (14.4%-43.0%). Etiologic categories were allowed to overlap, and studies in which a category was not point-identifiable were treated as missing for that outcome rather than as zero. Timing did not demonstrate a clear omnibus association with Strict or Expanded outcomes, although the >=24-hour Strict subgroup was too sparse and boundary-heavy for a stable inferential pooled estimate.

## 8. Interpretation guardrails for drafting

Do not write:

- “17% of babies have actionable disease” without qualifying the estimand and heterogeneity;
- “screening before 24 h is better/worse” based on the subgroup diagnostic;
- “absence of publication bias” based on the decision not to run funnel tests;
- etiologic percentages as mutually exclusive components that sum to Expanded CAN-CCHD;
- crude 638/1,999 or 1,015/1,999 ratios as the random-effects pooled result.

Preferred core message:

> A failed CCHD pulse-oximetry screen that is negative for harmonized target CCHD frequently identifies other clinically relevant neonatal disease. The fraction for which a specific qualifying management consequence is documented is highly heterogeneous across programs and reports, while the broader presence of clinically relevant alternative disease is consistently common.
