# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> Before interpreting any Phase file, CSV, snapshot, extraction block, database, or historical note, **read this file first**.

Last updated: **2026-08-22**  
Current scientific branch: **`phase6-analysis`**  
Current safe-resume snapshot: **`docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_DATABASE_READY.md`**  
Snapshot creation commit: **`fab26aa6261de33d5cc5862f432bef564d5d4999`**  
Current phase status: **PHASE 6 — DATABASE FROZEN / READY FOR META-ANALYSIS**

---

## 1. Mandatory new-chat procedure

Read, in order:

1. `CURRENT_STATE.md`
2. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_DATABASE_READY.md`
3. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`
4. `docs/PHASE6_PRIMARY_DATABASE_QA.md`
5. `docs/PHASE6_PREAMENDMENT_SENSITIVITY_QA.md`
6. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
7. `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
8. `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`
9. `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`
10. `docs/PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`

The database-readiness gate has passed. The next chat may execute the locked meta-analysis from these frozen inputs.

No authoritative meta-analysis has yet been run.

---

## 2. Database-readiness result

The Phase 6 database-readiness gates A-H are formally closed.

Overall result: **PASS**.

Formal freeze artifact:

`docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`

Primary QA:

`docs/PHASE6_PRIMARY_DATABASE_QA.md`

Sensitivity QA:

`docs/PHASE6_PREAMENDMENT_SENSITIVITY_QA.md`

---

## 3. Frozen primary database

Canonical primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

State:

- rows: **28**;
- unique units: **28**;
- duplicates: **0**;
- exact match to final `PRIMARY_POOLABLE` membership;
- all integer arithmetic closed;
- all row proportions independently reproduced;
- 11 post-rerun overlay rows verified;
- 17 unchanged rows verified against frozen extraction provenance;
- all primary units satisfy the required outcome-ascertainment threshold;
- ontology, terminal-state, cluster, and descriptive metadata gates passed.

No primary value changed during Phase 6 QA, so no `v1.1` primary file was created. **v1.0 is the frozen canonical primary input.**

---

## 4. Frozen historical pre-amendment sensitivity database

Canonical S2 input:

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

Frozen corrected blob SHA:

`61e8ff9f3bb875fbc30f3964ee2e72a448cc94f2`

Rows: **26**.

The original 23-row candidate was rejected during Gate H because it was a hybrid of post-rerun values and a pre-amendment label.

The corrected file reconstructs the preserved Snapshot R/S pre-rerun `PRIMARY_POOLABLE = 26` framework and is **sensitivity-only**.

Membership difference versus the final 28-unit primary database:

- current-only after rerun/promotions: U_R006, U_R008, U_R013, U_R023, U_R036;
- historical-only before later downgrades: U_R020, U_R024, U_R043.

Interpret this S2 as a **historical pre-amendment/pre-rerun framework sensitivity**, not as a pure one-variable causal contrast of the d-TGA ontology change.

---

## 5. Frozen Phase 5 scientific disposition

Unchanged by Phase 6 readiness QA:

- total unique quantitative units: **76**;
- `PRIMARY_POOLABLE`: **28**;
- `SENSITIVITY_ONLY`: **40**;
- `HOLD_PENDING_QA`: **3**;
- `NOT_POOLABLE`: **5**.

The canonical Phase 5 closeout remains:

- `docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_T.md`
- `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`

HOLD and NOT_POOLABLE units remain quarantined from primary meta-analysis weights.

---

## 6. Binding numerical precedence after freeze

For the primary analysis:

1. `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv` — **frozen canonical input**;
2. Phase 6 QA/freeze artifacts for audit;
3. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv` for provenance of affected rows;
4. target-rerun audits and binding ontology documents;
5. latest frozen Phase 5 extraction blocks for provenance of unchanged rows.

Do not restore stale block values over the frozen primary file.

For the pre-amendment historical sensitivity, use only the corrected 26-row Phase 6 S2 input and its QA note.

---

## 7. Locked analysis boundary

Primary endpoint:

`Strict CAN-CCHD / harmonized-CCHD-negative final failed screens`

Secondary endpoint:

`Expanded CAN-CCHD / harmonized-CCHD-negative final failed screens`

Primary model:

one-stage random-effects binomial-logistic-normal GLMM using exact binomial likelihood and no continuity correction.

Binding method document:

`docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`

The statistical plan was locked before pooled results. No result-driven change is permitted without a dated explicit statistical amendment preserving the locked analysis.

---

## 8. Exact next movement

The next chat may now begin quantitative synthesis, but must start from the frozen Phase 6 integers.

Recommended sequence:

1. implement/review the reproducible Phase 6 analysis script;
2. validate the locked model implementation;
3. run the Strict primary GLMM;
4. run Expanded and all prespecified sensitivities, including corrected historical S2 and R125 cluster aggregation;
5. write machine-readable results and figures;
6. create a Phase 6 analysis audit/interpretation artifact before manuscript drafting.

No database editing should be mixed silently into analysis. Any new scientific correction requires a formal `PHASE6_DATABASE_AMENDMENT` before rerunning results.

---

## 9. Critical legacy firewall

The systematic review was rebuilt from scratch.

The old Browser Agent, old application databases, `can_cchd.db`, `data/processed/can_cchd_agent.db`, and related legacy artifacts are **historical only**.

They must not be used to resolve scientific values, including identity, eligibility, numerator, denominator, diagnosis, target mapping, actionability, missingness, overlap, PRISMA counts, or analysis weights.

Use only restart-native frozen scientific artifacts.

---

## 10. One-line handoff

**DATABASE-READINESS GATE PASSED. The canonical primary database is frozen at 28 unique units in `PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`; the corrected historical pre-amendment sensitivity database is frozen at 26 units; all A-H gates are closed; no authoritative meta-analysis has yet been run. Read the database-ready snapshot and locked SAP, then begin Phase 6 quantitative synthesis from the frozen restart-native inputs.**
