# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> Before interpreting any Phase file, CSV, snapshot, extraction block, database, result file, or historical note, **read this file first**.

Last updated: **2026-08-22**  
Current scientific branch: **`phase6-analysis`**  
Current safe-resume snapshot: **`docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_META_CORE_COMPLETE.md`**  
Snapshot creation commit: **`b8aebdf79afc261f454b354612607183e29e5934`**  
Current phase status: **PHASE 6 — CORE META-ANALYSIS COMPLETE / SECONDARY & REPORTING QA NEXT**

---

## 1. Mandatory new-chat procedure

Read, in order:

1. `CURRENT_STATE.md`
2. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_META_CORE_COMPLETE.md`
3. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
4. `analysis/phase6/results/phase6_primary_results.json`
5. `analysis/phase6/results/phase6_sensitivity_results.csv`
6. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
7. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`
8. `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
9. `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`
10. `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`

The database-readiness gate passed before any authoritative result was calculated. The core authoritative meta-analysis has now been executed from the frozen inputs.

---

## 2. Frozen database state

Unchanged after viewing results:

- total quantitative units: **76**;
- `PRIMARY_POOLABLE`: **28**;
- `SENSITIVITY_ONLY`: **40**;
- `HOLD_PENDING_QA`: **3**;
- `NOT_POOLABLE`: **5**.

Canonical primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

Primary analysis totals:

- 28 unique units;
- 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD outcomes;
- 1,015 Expanded CAN-CCHD outcomes.

No scientific database field was changed after meta-analysis results were inspected.

---

## 3. Authoritative core meta-analysis

Binding model remains the prospectively locked one-stage random-effects binomial-logistic-normal GLMM with exact binomial likelihood and no continuity correction.

### Strict CAN-CCHD — primary endpoint

- median-study pooled probability: **17.0%**;
- 95% profile-likelihood CI: **3.1% to 46.8%**;
- marginal mean probability: **33.8%**;
- tau: **3.369**;
- 95% prediction interval: approximately **0.03% to 99.34%**.

Interpretation: **extreme between-study heterogeneity**. The 17.0% median-study probability must not be reported as a universal rate or without the marginal mean, tau, and prediction interval.

### Expanded CAN-CCHD — secondary endpoint

- median-study pooled probability: **69.4%**;
- 95% profile-likelihood CI: **57.7% to 81.4%**;
- marginal mean probability: **65.8%**;
- tau: **1.110**;
- 95% prediction interval: **20.4% to 95.2%**.

Interpretation: clinically relevant alternative diagnoses are common among harmonized-CCHD-negative final failed screens, although heterogeneity remains substantial.

Canonical interpretation/audit:

`docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`

---

## 4. Core robustness complete

The prespecified core S1-S6 framework has been run:

- S1 Expanded endpoint;
- S2 corrected historical pre-amendment/pre-rerun 26-unit framework;
- S3 R125/SIBEN report-cluster aggregation;
- S4 leave-one-out influence analysis;
- S5 beta-binomial sensitivity;
- S6 conventional two-stage REML/Hartung-Knapp comparison.

None reverses the core interpretation.

Key checks:

- historical S2: Strict 18.4%, Expanded 69.7%;
- R125 aggregation: Strict 17.2%, Expanded 69.0%;
- Strict leave-one-out pooled range: 14.8%-21.1%;
- Expanded leave-one-out range: 65.3%-70.9%;
- beta-binomial marginal means: Strict 33.5%, Expanded 66.3%.

The historical S2 is a pre-amendment/pre-rerun framework sensitivity, not a pure causal one-variable d-TGA contrast.

---

## 5. Reproducibility outputs

Authoritative implementation and outputs:

- `analysis/phase6/run_phase6_meta.py`
- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_study_results.csv`
- `analysis/phase6/results/phase6_sensitivity_results.csv`
- `analysis/phase6/results/phase6_leave_one_out.csv`
- `analysis/phase6/figures/forest_strict.svg`
- `analysis/phase6/figures/forest_expanded.svg`

The GLMM solution was validated across adaptive quadrature orders 21/31/41/61, multiple starting values, positive-definite Hessian checks, and profile-likelihood confidence intervals.

---

## 6. Exact next movement — remaining Phase 6

The core meta-analysis is complete, but Phase 6 is not closed yet.

Next tasks:

1. **Subgroup/meta-regression feasibility audit** — timing, setting, altitude; do not force unstable inferential models.
2. **Descriptive heterogeneity summaries** — especially predominantly <24 h vs >=24 h vs mixed/uncertain screening timing.
3. **Etiologic secondary outcomes** where participant-level numerators are reproducible from frozen extraction: PPHN/pulmonary hypertension, respiratory disease, infection/sepsis, noncritical CHD, and no actionable diagnosis.
4. **Publication-bias/small-study assessment** only if technically interpretable; exploratory only.
5. **Manuscript-ready tables and figure captions** plus a final Phase 6 results summary.
6. **Final Phase 6 closeout/snapshot.**
7. Then proceed to **Phase 11 — SHA abstract and manuscript drafting**.

No database editing may be mixed silently into secondary analysis. Any genuine scientific correction requires an explicit dated `PHASE6_DATABASE_AMENDMENT` before rerunning results.

---

## 7. Overall review progress

Completed:

- protocol/restart methodological lock;
- public/regional search and corpus construction;
- normalization/deduplication/identity reconstruction;
- title/abstract/full-text screening and terminal eligibility;
- overlap/non-independence resolution;
- structured extraction of all 76 units;
- harmonized target and d-TGA rerun across all 76;
- conditional-lesion <=28-day audit;
- final pool freeze;
- Phase 6 database-readiness gates A-H;
- primary Strict GLMM;
- Expanded GLMM;
- core S1-S6 sensitivity framework;
- study-level exact-binomial results and core forest plots.

Pending before the scientific review is analysis-complete:

- secondary/subgroup/etiologic analysis package;
- final Phase 6 reporting QA and closeout;
- manuscript/SHA abstract drafting and human review.

---

## 8. Critical legacy firewall

The systematic review was rebuilt from scratch.

The old Browser Agent, old application databases, `can_cchd.db`, `data/processed/can_cchd_agent.db`, and related legacy artifacts remain **historical only** and must never be used to alter current scientific values or analysis weights.

Use only restart-native frozen scientific artifacts.

---

## 9. One-line handoff

**DATABASE FROZEN; CORE META-ANALYSIS COMPLETE. Strict CAN-CCHD is extremely heterogeneous (median-study 17.0%, marginal mean 33.8%), while Expanded clinically relevant disease is common (median-study 69.4%, marginal mean 65.8%). S1-S6 robustness is complete and does not reverse the interpretation. Finish subgroup/etiologic/reporting analyses, close Phase 6, then move to the SHA abstract and manuscript.**
