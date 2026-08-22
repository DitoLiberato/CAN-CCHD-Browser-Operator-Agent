# CAN-CCHD Phase 6 — Progress Snapshot: Database Ready

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **SAFE RESUME POINT — DATABASE FROZEN / READY FOR META-ANALYSIS / META-ANALYSIS NOT YET RUN**

## 1. Exact scientific state

The database-readiness gate defined in `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md` has been completed.

Final gate result: **PASS**.

The restart-native analysis database is now formally frozen for the locked Phase 6 meta-analysis.

No authoritative pooled result has been calculated or inspected in reaching this state.

## 2. Frozen primary input

Canonical file:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

State:

- 28 rows;
- 28 unique `unit_id` values;
- exact final `PRIMARY_POOLABLE` membership;
- zero duplicates;
- integer arithmetic closed 28/28;
- proportions independently reproduced;
- post-rerun overlay precedence verified;
- unchanged-row provenance verified;
- target ontology verified;
- ascertainment threshold verified;
- metadata and R125 cluster handling verified.

The primary file required **no data correction** during Phase 6 QA and is frozen in place as v1.0.

## 3. Frozen historical pre-amendment sensitivity input

Canonical file:

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

Blob SHA:

`61e8ff9f3bb875fbc30f3964ee2e72a448cc94f2`

Rows: **26**.

The original 23-row candidate was rejected during Gate H because it mixed post-rerun values with a pre-amendment label. The corrected file now reconstructs the preserved Snapshot R/S pre-rerun primary framework exactly and is explicitly sensitivity-only.

Membership difference versus the final 28-unit primary set:

- current-only after rerun/promotions: U_R006, U_R008, U_R013, U_R023, U_R036;
- historical-only before later downgrades: U_R020, U_R024, U_R043.

Interpret S2 as a **historical framework sensitivity**, not as a pure one-variable causal contrast of d-TGA ontology.

## 4. Frozen Phase 5 disposition

Unchanged:

- total quantitative units: **76**;
- `PRIMARY_POOLABLE`: **28**;
- `SENSITIVITY_ONLY`: **40**;
- `HOLD_PENDING_QA`: **3**;
- `NOT_POOLABLE`: **5**.

HOLD and NOT_POOLABLE units remain quarantined from the primary analysis.

## 5. QA artifacts created in the readiness closeout

- `docs/PHASE6_PRIMARY_DATABASE_QA.md` — primary gates A-G passed;
- `docs/PHASE6_PREAMENDMENT_SENSITIVITY_QA.md` — Gate H passed after correction;
- `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md` — formal freeze declaration.

Relevant commits:

- sensitivity correction: `cd2940a1b7712b46d580957f8d3687674b728ad9`;
- primary QA: `14c9ff8e6001192310f14622dd3903ae328caef1`;
- sensitivity QA: `e2c69830b976b399163c44b83cee39764f154491`;
- database freeze: `9a5c127cf324e652bb38b099889de84473ff3009`.

## 6. Mandatory reading order from this safe point

A new chat or agent must read, in order:

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

Do not restore older numerical values over the frozen Phase 6 input.

## 7. Exact next movement

The next phase may now execute the prospectively locked statistical analysis plan in `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`.

The analysis must begin from the frozen integer counts, not from legacy databases or reconstructed proportions.

Required sequence when analysis starts:

1. build/review the reproducible Phase 6 analysis script;
2. validate model implementation on the frozen primary integers;
3. run the locked Strict primary GLMM;
4. run the locked Expanded and prespecified sensitivity analyses, including the corrected historical S2 input and R125 cluster sensitivity;
5. write machine-readable results and figures;
6. create a separate analysis audit/interpretation artifact before manuscript drafting.

No result-driven database edits are allowed after this freeze without a formal database amendment.

## 8. Legacy firewall

Still binding.

Do not use the old Browser Agent, old app databases, `can_cchd.db`, `data/processed/can_cchd_agent.db`, or any other legacy data artifact to resolve scientific values or analysis weights.

## 9. One-line handoff

**Database-readiness gate PASSED. Primary v1.0 is frozen at 28 unique units; the corrected historical pre-amendment sensitivity input is frozen at 26 units; all A-H gates are closed; no meta-analysis has yet been run. The next chat may execute the locked Phase 6 SAP from these frozen restart-native inputs.**
