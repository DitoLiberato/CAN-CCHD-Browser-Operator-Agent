# CAN-CCHD Phase 6 — Statistical Analysis Plan Lock

Date: 2026-08-22
Branch: `phase6-analysis`
Status: **LOCKED BEFORE ANY META-ANALYTIC POOLED RESULT**

## 1. Purpose and provenance

This document locks the quantitative synthesis method after Phase 5 was frozen and after the canonical 28-unit primary analysis dataset was constructed, but **before any pooled meta-analytic result was calculated or inspected**.

Binding scientific inputs:

- `docs/PROTOCOL_CORE_v1.0_RESTART_LOCK_RECONSTRUCTED.md`
- `docs/PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`
- `docs/PHASE5_PROTOCOL_AMENDMENT_2026-08-22_D_TGA_TARGET_RULE.md`
- `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`
- `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`
- `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

The older `docs/08_ANALYSIS_AND_WRITING.md` prespecified a random-effects proportional meta-analysis if meta-analysis was stable enough to implement, but did not lock a transformation or heterogeneity estimator. The choices below therefore complete the statistical specification prospectively, before viewing a pooled result.

## 2. Review estimands

### Primary estimand — Strict CAN-CCHD

For each PRIMARY_POOLABLE unit:

`Strict proportion = Strict CAN-CCHD / harmonized-CCHD-negative final failed screens`

where:

`Strict CAN-CCHD = CAN-A + CAN-B + CAN-AB`.

Clinical interpretation:

> Among newborns who complete a pulse-oximetry screening/repeat pathway with a final failed screen and do not have harmonized target CCHD, what proportion have a documented clinically actionable non-CCHD diagnosis/outcome?

### Secondary estimand — Expanded CAN-CCHD

`Expanded proportion = (Strict CAN-CCHD + CAN-U) / harmonized-CCHD-negative final failed screens`.

This estimates the broader burden of clinically relevant non-CCHD diagnoses whether or not qualifying actionability was directly demonstrated.

## 3. Primary analysis set

Primary analysis uses the **28 frozen PRIMARY_POOLABLE units** in:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

The analytic denominator is the final harmonized-CCHD-negative failed-screen count, not the total screened population.

No HOLD_PENDING_QA, NOT_POOLABLE, or SENSITIVITY_ONLY unit receives a primary meta-analysis weight.

## 4. Why a one-stage binomial model is required

The primary dataset contains both zero-event and all-event studies and several very small denominators. A conventional transformed inverse-variance analysis would require arbitrary continuity corrections for boundary proportions and can behave poorly when proportions are 0 or 1.

Therefore the primary model is a **one-stage binomial-normal generalized linear mixed model (GLMM)** with a logit link and a random study/unit intercept.

For unit `i`:

`Y_i ~ Binomial(n_i, p_i)`

`logit(p_i) = mu + u_i`

`u_i ~ Normal(0, tau^2)`

where:

- `Y_i` is the Strict CAN-CCHD numerator;
- `n_i` is the harmonized-CCHD-negative final-failed-screen denominator;
- `mu` is the average latent log-odds across study units;
- `tau` is the between-study standard deviation on the logit scale.

The same model is fit separately for the Expanded endpoint.

No continuity correction is used in the primary GLMM.

## 5. Primary pooled quantity

The primary reported pooled proportion is:

`inverse_logit(mu)`

This is the proportion for the median study/unit under the logit-normal random-effects distribution and is the conventional direct back-transformation of the GLMM intercept.

Also report as a supportive quantity the **marginal mean probability**:

`E[inverse_logit(mu + U)]`, where `U ~ Normal(0, tau^2)`.

The two quantities must be labelled distinctly if heterogeneity makes them meaningfully different.

## 6. Estimation and uncertainty

Fit by maximum likelihood using numerical integration of the exact binomial-logistic-normal likelihood.

Implementation target:

- adaptive or sufficiently high-order Gauss-Hermite quadrature;
- numerical optimization with multiple starting values;
- convergence and Hessian checks.

Report:

- pooled median-study proportion with 95% confidence interval;
- marginal mean probability as supportive estimate;
- `tau` and `tau^2` on the logit scale;
- 95% prediction interval for the distribution of true study-level proportions.

Confidence intervals for the main GLMM parameters should preferentially use profile likelihood. If profile likelihood is numerically unstable, a clearly labelled likelihood/Hessian-based interval may be used and checked by bootstrap sensitivity.

## 7. Study-level intervals and forest plots

For display only, study-level observed proportions receive exact binomial 95% confidence intervals (Clopper-Pearson or an equivalently explicit exact-binomial method).

Forest plots must display raw `events / denominator` alongside the observed percentage.

Study-level display intervals do not determine the GLMM weights.

## 8. Heterogeneity

Primary heterogeneity reporting:

- `tau` and `tau^2` from the GLMM;
- 95% prediction interval on the probability scale;
- visual distribution of study-specific observed proportions.

A conventional `I^2` is not treated as the principal heterogeneity measure for the exact one-stage binomial GLMM because within-study variance is not represented by one common normal-approximation variance. If an `I^2` value is reported, it must come from a clearly labelled conventional two-stage sensitivity model and must not replace the GLMM prediction interval.

## 9. Prespecified sensitivity analyses

### S1 — Expanded endpoint

Repeat the primary GLMM using Expanded CAN-CCHD numerator.

### S2 — Original pre-amendment TGA mapping

Repeat the synthesis under the original Cochrane-literal/simple-TGA mapping preserved by the pre-amendment Phase 5 extraction/Snapshot R-S framework.

This analysis assesses the impact of the formal d-TGA amendment on pooled results and pool membership.

### S3 — R125/SIBEN report-cluster sensitivity

Primary analysis treats Barranquilla and Rosario as distinct site/program units because participants are geographically distinct and non-overlapping.

Sensitivity analysis replaces the two site estimates with one report-cluster aggregate:

- denominator = `38 + 1 = 39`;
- Strict numerator = `0 + 1 = 1`;
- Expanded numerator = `18 + 1 = 19`.

This tests whether allowing two independent weights from one implementation report materially changes the pooled estimate.

### S4 — Leave-one-out influence analysis

Refit the primary GLMM after excluding each primary unit in turn. Report the range of pooled estimates and identify any unit whose exclusion produces a conspicuous change in pooled estimate or heterogeneity.

No unit is excluded from the main model solely because it is influential.

### S5 — Alternative random-effects distribution

Fit a beta-binomial random-effects model as a distributional sensitivity analysis. This provides a marginal mean proportion under a beta mixing distribution and handles 0/n and n/n studies without continuity corrections.

The beta-binomial result is supportive; the logit-normal binomial GLMM remains primary.

### S6 — Conventional two-stage model for comparability only

If computationally stable, fit a conventional random-effects meta-analysis on a logit scale with REML estimation of between-study variance and small-sample-adjusted inference. Boundary studies require an explicitly documented continuity correction and therefore this model is **not** the primary analysis.

Its purpose is comparison with conventional meta-analysis output and, if useful, conventional `I^2` reporting.

Freeman-Tukey double-arcsine pooling is not a primary method because of known back-transformation pathologies for single-proportion meta-analysis.

## 10. Subgroup and meta-regression policy

The dataset retains screening timing, setting, altitude and program-cluster metadata.

Formal subgroup/meta-regression will only be attempted when a subgroup contains enough independent units to avoid a manifestly unstable model. As an operational minimum:

- at least 4 independent units per categorical subgroup for a descriptive subgroup GLMM;
- preferably >=10 units per fitted meta-regression coefficient for inferential modelling.

Sparse categories are reported descriptively, not forced into inferential subgroup estimates.

Candidate prespecified heterogeneity dimensions:

- predominantly <24 h versus predominantly >=24 h versus mixed/uncertain timing;
- well-baby hospital versus community/out-of-hospital versus other eligible setting;
- altitude where enough independent data exist;
- implementation/report cluster sensitivity.

## 11. Small-study/publication-bias analyses

Because the endpoint is a single proportion rather than a comparative treatment effect, with strong genuine clinical/design heterogeneity and many boundary proportions, funnel-plot asymmetry tests are not treated as definitive evidence of publication bias.

A conventional funnel/transform-based exploratory assessment may be shown if technically interpretable, but it must be labelled exploratory and must not drive inclusion/exclusion or the primary conclusion.

## 12. Descriptive quantities

In addition to the random-effects meta-analysis, report simple descriptive totals across the primary dataset:

- number of contributing units;
- total harmonized-CCHD-negative final failed screens;
- total Strict CAN-CCHD outcomes;
- total Expanded CAN-CCHD outcomes;
- distribution/range of study denominators.

The crude pooled numerator/denominator ratio is a descriptive aggregate only and must **not** be presented as the random-effects meta-analytic estimate.

## 13. Reproducibility outputs required

Phase 6 should create:

- `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
- `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`
- `analysis/phase6/run_phase6_meta.py`
- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_study_results.csv`
- `analysis/phase6/results/phase6_sensitivity_results.csv`
- `analysis/phase6/figures/` forest and diagnostic figures
- a Phase 6 audit/interpretation document before manuscript drafting.

## 14. Statistical lock conclusion

The statistical method is now fixed before pooled results are viewed:

**Primary:** one-stage random-effects binomial-logistic-normal GLMM, exact binomial likelihood, no continuity correction.

**Primary outcome:** Strict CAN-CCHD.

**Secondary outcome:** Expanded CAN-CCHD.

**Core robustness:** original TGA mapping, R125 report-cluster aggregation, leave-one-out analysis, beta-binomial distributional sensitivity, and a conventional two-stage comparison.

No result-driven change to this plan is permitted without a dated, explicit statistical protocol amendment documenting the reason and preserving the original analysis as a sensitivity analysis.
