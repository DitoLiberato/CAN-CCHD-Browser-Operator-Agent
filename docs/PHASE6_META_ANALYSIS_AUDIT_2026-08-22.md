# CAN-CCHD Phase 6 — Meta-analysis Audit and Interpretation Lock

Date: 2026-08-22
Branch: `phase6-analysis`
Status: **AUTHORITATIVE CORE QUANTITATIVE SYNTHESIS COMPLETE**

## 1. Scientific boundary

This analysis was run only after the Phase 6 database-readiness gate had passed and the restart-native primary database was frozen.

Primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen primary population:

- 28 unique PRIMARY_POOLABLE units;
- 1,999 harmonized-CCHD-negative final failed screens;
- no HOLD_PENDING_QA, NOT_POOLABLE, or SENSITIVITY_ONLY unit received a primary weight.

No scientific database value was modified after inspecting the meta-analytic results.

Binding statistical method:

`docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`

Primary model: one-stage random-effects binomial-logistic-normal GLMM with exact binomial likelihood, logit link, no continuity correction.

## 2. Numerical implementation and validation

The authoritative implementation is:

`analysis/phase6/run_phase6_meta.py`

The main GLMM used adaptive Gauss-Hermite quadrature with 41 points. Numerical stability was checked at 21, 31, 41, and 61 points.

For both Strict and Expanded endpoints:

- multiple starting values converged to the same optimum;
- the observed Hessian was positive definite;
- likelihood and parameter estimates were stable across quadrature orders;
- profile-likelihood 95% confidence intervals were successfully obtained.

For Strict, the pooled probability across q=21/31/41/61 was 0.17019 / 0.17008 / 0.17009 / 0.17009.

For Expanded, it was effectively invariant at 0.69356 across the same quadrature checks.

## 3. Primary outcome — Strict CAN-CCHD

Definition:

`Strict CAN-CCHD / harmonized-CCHD-negative final failed screens`

Observed totals:

- events: **638**;
- denominator: **1,999**;
- crude aggregate ratio: **31.9%** — descriptive only, not the random-effects estimate.

Primary GLMM:

- median-study pooled probability: **17.0%**;
- 95% profile-likelihood CI: **3.1% to 46.8%**;
- tau: **3.369** on the logit scale;
- tau^2: **11.349**;
- marginal mean probability: **33.8%**;
- 95% prediction interval for true study-level proportions: approximately **0.03% to 99.34%**.

Boundary structure is substantial:

- 11/28 units had zero Strict events;
- 5/28 units had Strict events in every denominator participant.

### Interpretation

Strict actionability is **extremely heterogeneous** across programs. The 17.0% value is the prespecified back-transformed GLMM intercept and represents the median-study true probability under the logit-normal random-effects distribution. It must not be interpreted as a universally applicable rate.

The large separation between the median-study probability (17.0%) and the marginal mean probability (33.8%), together with tau=3.369 and the very wide prediction interval, reflects a highly dispersed distribution of true study-level Strict proportions.

Therefore reporting Strict requires the pooled median-study estimate, marginal mean, tau, and prediction interval together.

## 4. Secondary outcome — Expanded CAN-CCHD

Definition:

`(Strict CAN-CCHD + CAN-U) / harmonized-CCHD-negative final failed screens`

Observed totals:

- events: **1,015**;
- denominator: **1,999**;
- crude aggregate ratio: **50.8%** — descriptive only.

GLMM:

- median-study pooled probability: **69.4%**;
- 95% profile-likelihood CI: **57.7% to 81.4%**;
- tau: **1.110**;
- tau^2: **1.233**;
- marginal mean probability: **65.8%**;
- 95% prediction interval: **20.4% to 95.2%**.

There were no Expanded zero-event units and 9/28 units had Expanded events in every denominator participant.

### Interpretation

Clinically relevant non-target diagnoses are common among CCHD-negative final failed pulse-oximetry screens. Heterogeneity remains important but is substantially less extreme than for Strict actionability.

The difference between Strict and Expanded is scientifically informative rather than merely statistical: the literature much more consistently reports the presence of clinically relevant alternative disease than it documents the specific management consequence required by the locked Strict actionability definition.

## 5. Prespecified robustness analyses

### S2 — historical pre-amendment/pre-rerun framework

Corrected 26-unit historical sensitivity input:

- Strict median-study probability: **18.4%**; 95% CI **1.9% to 59.5%**; tau **4.026**;
- Expanded median-study probability: **69.7%**; 95% CI **56.0% to 83.7%**; tau **1.229**.

This historical framework does not reverse the core conclusions. As frozen during database QA, it is not interpreted as a pure one-variable causal contrast of the d-TGA amendment because membership and later conditional-lesion adjudications also differ.

### S3 — R125/SIBEN report-cluster aggregation

Replacing Barranquilla and Rosario by one 39-participant report-cluster row gave:

- Strict: **17.2%**, 95% CI **3.8% to 43.8%**, tau **3.037**;
- Expanded: **69.0%**, 95% CI **57.2% to 81.0%**, tau **1.104**.

The two-site representation does not materially drive the principal estimates.

### S4 — leave-one-out influence

Strict pooled estimate range across 28 leave-one-out refits:

- **14.8% to 21.1%**;
- tau range **2.848 to 3.621**.

Lowest pooled estimate occurred after omitting U_R017 Jawin 2015; highest after omitting U_R009 Riede 2010.

Expanded pooled estimate range:

- **65.3% to 70.9%**;
- tau range **0.912 to 1.175**.

No single study eliminates the heterogeneity or reverses the clinical conclusion.

### S5 — beta-binomial distributional sensitivity

Marginal mean probabilities:

- Strict: **33.5%**;
- Expanded: **66.3%**.

These closely track the corresponding GLMM marginal means (33.8% and 65.8%). This supports the distinction between the median-study and population-of-studies marginal estimands rather than indicating failure of the primary model.

### S6 — conventional two-stage comparison

Logit random-effects REML/Hartung-Knapp model with Jeffreys 0.5 correction applied uniformly to all units, explicitly supportive only:

- Strict pooled probability: **29.9%**, 95% CI **16.8% to 47.4%**, I^2 **85.9%**;
- Expanded pooled probability: **60.4%**, 95% CI **51.1% to 69.0%**, I^2 **73.5%**.

These estimates are not substituted for the locked exact-binomial GLMM.

## 6. Forest plots and study-level intervals

Study-level display intervals use exact binomial confidence intervals and do not determine GLMM weights.

Generated figures:

- `analysis/phase6/figures/forest_strict.svg`
- `analysis/phase6/figures/forest_expanded.svg`

Machine-readable study results:

`analysis/phase6/results/phase6_study_results.csv`

## 7. Subgroup/meta-regression status

Timing metadata in the primary database currently group into:

- predominantly <24 h: 13 units;
- predominantly >=24 h: 6 units;
- mixed/uncertain: 9 units.

An initial stability diagnostic showed that forcing a formal Strict GLMM in the >=24 h subset is numerically fragile because the subgroup is small and boundary-heavy. In accordance with the locked SAP, no unstable subgroup estimate is promoted into the authoritative core results.

Setting and altitude categories are also sparse/unbalanced for inferential modelling. A dedicated subgroup-feasibility audit remains a Phase 6 secondary task. Descriptive subgroup summaries may be reported even when formal meta-regression is not defensible.

## 8. Interpretation lock

The core synthesis supports two simultaneous conclusions:

1. **Documented actionable alternatives (Strict) are real but highly variable across studies/programs.** A single pooled percentage is insufficient without explicit heterogeneity reporting.
2. **Clinically relevant alternative diagnoses (Expanded) are common.** The median-study estimate is approximately 69%, with a marginal mean near 66%.

The sharp Strict-versus-Expanded contrast is consistent with substantial heterogeneity in disease mix, screening timing, care pathways, documentation, and the extent to which primary reports link diagnoses to concrete management consequences.

No result-driven change to the CAN taxonomy, target definition, frozen membership, or statistical model is permitted after this analysis without an explicit dated amendment.

## 9. Remaining Phase 6 work

Before Phase 6 is fully closed:

1. complete the subgroup/meta-regression feasibility audit and descriptive timing/setting/altitude summaries;
2. extract/synthesize prespecified etiologic secondary proportions where the frozen data permit reproducible participant-level numerators: PPHN/pulmonary hypertension, respiratory disease, infection/sepsis, noncritical CHD, and no actionable diagnosis;
3. decide whether a publication-bias/funnel display is technically interpretable; any such analysis remains exploratory;
4. create manuscript-ready tables, figure captions, and the final Phase 6 results summary;
5. then hand off to Phase 11 manuscript/SHA abstract drafting.

## 10. Reproducibility outputs

Core Phase 6 outputs now present:

- `analysis/phase6/run_phase6_meta.py`
- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_study_results.csv`
- `analysis/phase6/results/phase6_sensitivity_results.csv`
- `analysis/phase6/results/phase6_leave_one_out.csv`
- `analysis/phase6/figures/forest_strict.svg`
- `analysis/phase6/figures/forest_expanded.svg`

**Core meta-analysis and prespecified S1-S6 robustness framework are complete. Phase 6 remains open only for secondary/subgroup/reporting work before manuscript drafting.**
