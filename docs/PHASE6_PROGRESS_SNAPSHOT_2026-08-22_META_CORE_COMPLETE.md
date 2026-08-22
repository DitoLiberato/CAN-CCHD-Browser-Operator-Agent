# CAN-CCHD Phase 6 — Progress Snapshot: Core Meta-analysis Complete

Date: 2026-08-22
Branch: `phase6-analysis`
Status: **SAFE RESUME POINT — DATABASE FROZEN / CORE META-ANALYSIS + S1-S6 COMPLETE**

## Canonical scientific state

The restart-native analysis database remains frozen and unchanged after quantitative results were viewed.

Primary analysis set:

- 28 PRIMARY_POOLABLE units;
- 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD outcomes;
- 1,015 Expanded CAN-CCHD outcomes.

The database-readiness freeze remains binding. No HOLD_PENDING_QA, NOT_POOLABLE, or SENSITIVITY_ONLY unit was given a primary weight.

## Authoritative core results

### Strict CAN-CCHD

Locked one-stage binomial-logistic-normal GLMM:

- median-study pooled proportion: **17.0%**;
- 95% profile-likelihood CI: **3.1% to 46.8%**;
- marginal mean probability: **33.8%**;
- tau: **3.369**;
- 95% prediction interval: approximately **0.03% to 99.34%**.

Interpretation: extreme between-study heterogeneity. The 17.0% pooled median-study probability must never be presented without the heterogeneity measures and marginal mean.

### Expanded CAN-CCHD

- median-study pooled proportion: **69.4%**;
- 95% profile-likelihood CI: **57.7% to 81.4%**;
- marginal mean probability: **65.8%**;
- tau: **1.110**;
- 95% prediction interval: **20.4% to 95.2%**.

Interpretation: clinically relevant alternative diagnoses are common after harmonized-CCHD-negative final failed pulse-oximetry screens, although the magnitude remains heterogeneous.

## Robustness completed

Prespecified core sensitivity framework is complete:

- S1 Expanded endpoint;
- S2 corrected historical pre-amendment/pre-rerun 26-unit framework;
- S3 R125/SIBEN report-cluster aggregation;
- S4 leave-one-out influence analysis;
- S5 beta-binomial random-effects sensitivity;
- S6 conventional logit REML/Hartung-Knapp comparison.

None reverses the core interpretation.

Notable robustness values:

- historical S2 Strict: 18.4%; Expanded: 69.7%;
- R125 aggregation Strict: 17.2%; Expanded: 69.0%;
- Strict leave-one-out pooled range: 14.8%-21.1%;
- Expanded leave-one-out pooled range: 65.3%-70.9%;
- beta-binomial marginal means: Strict 33.5%, Expanded 66.3%.

## Numerical QA

The authoritative GLMM implementation was validated with:

- adaptive Gauss-Hermite quadrature;
- q=21,31,41,61 stability checks;
- multiple optimization starting values;
- positive-definite Hessian checks;
- profile-likelihood confidence intervals.

No numerical instability was found in the full 28-unit Strict or Expanded models.

## Binding interpretation artifact

Read next:

`docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`

Machine-readable results:

`analysis/phase6/results/phase6_primary_results.json`

## Exact next movement

Phase 6 is not yet fully closed. Next:

1. subgroup/meta-regression feasibility audit;
2. descriptive timing/setting/altitude summaries;
3. prespecified etiologic secondary proportions where reproducible from the frozen extraction evidence;
4. exploratory publication-bias assessment only if technically interpretable;
5. manuscript-ready tables and figure captions;
6. final Phase 6 closeout;
7. Phase 11 SHA abstract and manuscript drafting.

Do not edit frozen database values during this work. Any genuine scientific correction discovered after freeze requires an explicit database amendment before result rerun.

## One-line handoff

**The database is frozen; the authoritative Strict and Expanded GLMMs and core S1-S6 sensitivities are complete. Strict actionability is extremely heterogeneous (median-study 17.0%, marginal 33.8%), while Expanded clinically relevant disease is common (median-study 69.4%, marginal 65.8%). Finish secondary/subgroup/reporting analyses before closing Phase 6 and drafting the manuscript.**
