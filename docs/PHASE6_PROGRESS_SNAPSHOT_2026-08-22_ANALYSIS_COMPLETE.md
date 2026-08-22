# CAN-CCHD Phase 6 — Safe Resume Snapshot — Analysis Complete

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **SAFE RESUME POINT — PHASE 6 ANALYSIS COMPLETE / PHASE 11 WRITING NEXT**

## Canonical state

The restart-native scientific database is frozen and unchanged after quantitative results were viewed.

Primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob: `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

Primary set:

- 28 PRIMARY_POOLABLE units;
- denominator 1,999 harmonized-CCHD-negative final failed screens;
- Strict events 638;
- Expanded events 1,015.

Whole 76-unit disposition remains 28 PRIMARY_POOLABLE / 40 SENSITIVITY_ONLY / 3 HOLD_PENDING_QA / 5 NOT_POOLABLE.

No database amendment occurred during Phase 6 analysis.

## Authoritative core results

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

S1-S6 robustness is complete and does not reverse the interpretation.

## Secondary etiologic results

Outcome-specific exact-reporting GLMMs:

- PPHN/pulmonary hypertension: **10.3%** (95% CI 4.7%-16.3%), k=22;
- respiratory disease: **8.7%** (1.6%-23.0%), k=22;
- infection/sepsis: **16.7%** (9.4%-24.2%), k=22;
- other/non-target structural cardiac diagnosis: **26.6%** (14.4%-43.0%), k=26.

Rule: non-point-identifiable diagnosis categories are missing for that outcome, never zero. Etiologic categories may overlap and must not be summed.

## Subgroup audit

Timing groups: 13 predominantly <24 h / 6 predominantly >=24 h / 9 mixed-uncertain.

Strict timing omnibus p=0.263; Expanded p=0.493. No clear timing-group effect is demonstrated, but no equivalence claim is permitted.

The >=24 h Strict subgroup has 3 events/97 and a numerically unstable/boundary-heavy GLMM; no authoritative pooled Strict estimate is promoted.

Setting and altitude meta-regression are infeasible because of sparse/unbalanced covariate structure.

## Reporting-bias decision

No inferential Egger/Begg/trim-and-fill or conventional funnel analysis is promoted for this single-proportion synthesis with boundary observations and strong genuine heterogeneity.

Read:

`docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`.

## Manuscript-ready package

Read:

`docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`.

Main quantitative presentation is locked to:

- Table 1: primary + etiologic random-effects results;
- Table 2: robustness/sensitivity;
- Table 3: timing subgroup audit;
- Figure 1: Strict forest;
- Figure 2: Expanded forest;
- PRISMA figure assembled during writing.

No main-paper funnel plot is planned.

## Reproducibility inventory

Inputs:

- `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
- `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`
- `data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`

Scripts:

- `analysis/phase6/run_phase6_meta.py`
- `analysis/phase6/run_phase6_secondary.py`

Results:

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

## Mandatory reading order for a new chat

1. `CURRENT_STATE.md`
2. this snapshot
3. `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
4. `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
5. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
6. `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
7. `docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`
8. `analysis/phase6/results/phase6_primary_results.json`
9. `analysis/phase6/results/phase6_secondary_results.json`
10. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
11. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`

## Exact next movement

Do not reopen extraction or alter frozen values by default.

Proceed to **Phase 11 — writing**, preferably:

1. SHA abstract;
2. manuscript Results;
3. Methods/statistical analysis;
4. Discussion/limitations;
5. PRISMA/search-flow assembly;
6. journal-specific formatting and human scientific review.

## Legacy firewall

The old Browser Agent/app databases remain historical only and may not contribute scientific values, denominators, numerators, diagnoses, eligibility decisions or weights.

## One-line handoff

**PHASE 6 ANALYSIS COMPLETE. Database frozen and unchanged; Strict 17.0% median-study with extreme heterogeneity, Expanded 69.4%; S1-S6, etiologic outcomes, subgroup feasibility and reporting-bias decision complete. Start Phase 11 from the manuscript-ready results package.**
