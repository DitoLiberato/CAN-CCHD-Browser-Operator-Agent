# CAN-CCHD Phase 6 — Safe Resume Snapshot — Secondary Analysis Complete

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **SAFE RESUME POINT — CORE + SECONDARY QUANTITATIVE ANALYSIS COMPLETE / REPORTING QA NEXT**

## Frozen scientific state

The restart-native scientific database remains unchanged and frozen:

- 76 quantitative units total;
- 28 PRIMARY_POOLABLE;
- 40 SENSITIVITY_ONLY;
- 3 HOLD_PENDING_QA;
- 5 NOT_POOLABLE.

Primary canonical input: `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`.

Historical S2 input: `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`.

Any new scientific-value correction requires a formal dated `PHASE6_DATABASE_AMENDMENT`.

## Core meta-analysis complete

Strict:
- median-study **17.0%**;
- 95% CI **3.1%-46.8%**;
- marginal mean **33.8%**;
- tau **3.369**.

Expanded:
- median-study **69.4%**;
- 95% CI **57.7%-81.4%**;
- marginal mean **65.8%**;
- tau **1.110**.

S1-S6 robustness is complete.

## Secondary etiologic analysis complete

Audited derivation: `data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`.

Outcome-specific exact-reporting GLMMs:

- PPHN/pulmonary hypertension: **10.3%** (95% CI **4.7%-16.3%**), k=22;
- respiratory disease: **8.7%** (**1.6%-23.0%**), k=22, extreme heterogeneity;
- infection/sepsis: **16.7%** (**9.4%-24.2%**), k=22;
- other/non-target structural cardiac diagnosis: **26.6%** (**14.4%-43.0%**), k=26.

Never treat a non-reported etiologic category as zero. Etiologic categories can overlap and must not be summed.

## Subgroup audit complete

Timing groups:

- <24 h predominant: 13 units;
- >=24 h predominant: 6 units;
- mixed/uncertain: 9 units.

The >=24 h Strict subgroup is numerically fragile: 3 events/97, extreme tau, and no reproducible profile-likelihood CI. No authoritative Strict pooled estimate is promoted for that subgroup.

Expanded timing subgroup fits are stable.

Three-level timing meta-regression diagnostic:

- Strict omnibus p=0.263;
- Expanded omnibus p=0.493.

No timing effect is demonstrated, but no equivalence/no-effect claim is permitted.

Setting meta-regression: **infeasible**.  
Altitude meta-regression: **infeasible**.

## Mandatory reading order for a new chat

1. `CURRENT_STATE.md`
2. this snapshot
3. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
4. `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
5. `analysis/phase6/results/phase6_primary_results.json`
6. `analysis/phase6/results/phase6_secondary_results.json`
7. `analysis/phase6/results/phase6_sensitivity_results.csv`
8. `data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`
9. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
10. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`

## Reproducibility files

Core:

- `analysis/phase6/run_phase6_meta.py`
- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_study_results.csv`
- `analysis/phase6/results/phase6_sensitivity_results.csv`
- `analysis/phase6/results/phase6_leave_one_out.csv`
- core forest plots.

Secondary:

- `analysis/phase6/run_phase6_secondary.py`
- `analysis/phase6/results/phase6_secondary_results.json`
- `analysis/phase6/results/phase6_etiology_study_results.csv`
- `analysis/phase6/results/phase6_subgroup_results.csv`
- `data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`.

## Exact next movement

Do **not** reopen extraction or rerun the database by default.

Next:

1. publication-bias/small-study interpretability decision;
2. manuscript-ready tables;
3. figure and figure-caption finalization;
4. final Phase 6 reporting QA and analysis-complete freeze;
5. SHA abstract and manuscript drafting.

## Legacy firewall

Legacy Browser Agent/app databases remain historical only and cannot be used to alter any scientific value, denominator, numerator, eligibility decision, diagnosis, or weight.

## One-line handoff

**Core and secondary quantitative synthesis are complete from the frozen restart-native database. Etiologic outcomes and subgroup feasibility have been audited; timing does not show a demonstrable group effect but Strict remains highly heterogeneous and the >=24 h Strict subgroup is numerically fragile. Finish reporting QA, freeze Phase 6 analysis-complete, then draft the SHA abstract/manuscript.**
