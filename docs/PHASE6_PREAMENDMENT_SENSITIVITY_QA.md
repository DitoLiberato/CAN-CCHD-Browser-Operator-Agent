# CAN-CCHD Phase 6 — Pre-amendment TGA Sensitivity Database QA

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **SENSITIVITY DATABASE QA PASSED AFTER PROVENANCE CORRECTION**

## 1. Scope

This audit addresses Gate H of `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md` for:

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

The locked SAP defines S2 as a repeat analysis under the **original pre-amendment Phase 5 / Snapshot R-S framework**. This dataset is sensitivity-only and must never replace the amended 28-unit primary database.

## 2. Problem found in the candidate sensitivity file

The original candidate committed as `60b3fe2bc4b6153a5a5099ffe89f99f453beca6b` contained **23 rows**.

Database-readiness QA showed that this file was a hybrid rather than a reproducible historical framework:

- it excluded the five units promoted into the final primary pool after the target rerun;
- it also excluded U_R020, U_R024, and U_R043, which were still `PRIMARY_POOLABLE` in the preserved pre-rerun Snapshot R/S state and were downgraded only during the later conditional-lesion audit;
- several rows used post-rerun conditional-lesion values rather than the preserved pre-amendment structural-extraction values.

Thus the 23-row candidate could not be described accurately as the preserved Snapshot R-S framework.

No pooled result had been calculated, so this was corrected during the database-readiness gate rather than carried into analysis.

## 3. Binding interpretation of S2

The canonical sensitivity file now represents the **historical pre-rerun/pre-amendment Phase 5 analytic framework preserved at Snapshot R/S**.

This is an audit-preserving historical sensitivity, not a retrospectively manufactured one-variable counterfactual in which every later QA correction is held fixed except TGA ontology.

That distinction matters because the subsequent all-76 rerun did two things before final pool freeze:

1. implemented the d-TGA amendment;
2. independently corrected conditional-lesion/anatomy mappings.

Therefore S2 must be interpreted as a robustness analysis against the preserved earlier framework, not as a causal estimate of the d-TGA amendment alone.

A future pure `TGA-only` counterfactual would require a separate explicit protocol definition because the old simple-TGA rule left several generic TGA labels genuinely non-point-identifiable. It is not silently substituted for the locked S2.

## 4. Corrected sensitivity membership

**PASS.**

Corrected rows: **26**  
Unique `unit_id`: **26**  
Duplicates: **0**.

This exactly reconstructs the provisional `PRIMARY_POOLABLE = 26` framework preserved in Snapshot R/S.

### Present in the current 28-unit primary pool but absent from historical S2

These five units were not point-primary under the preserved pre-rerun framework and were promoted only after target adjudication/rerun:

- U_R006
- U_R008
- U_R013
- U_R023
- U_R036

### Present in historical S2 but absent from the current 28-unit primary pool

These three units were primary before the later conditional-lesion/anatomy audit and were subsequently downgraded to sensitivity-only:

- U_R020
- U_R024
- U_R043

Thus the membership transition is transparent:

`26 historical primary units - 3 later downgrades + 5 later promotions = 28 final primary units`.

## 5. Historical numerical provenance

The corrected sensitivity file uses the latest frozen structural-extraction values that existed in the preserved pre-rerun framework, not the later post-rerun overlay.

Row provenance:

- Block 01: U_R017, U_R018, U_R019, U_R025
- Block 02: U_R009, U_R024, U_R089, U_R093
- Block 03: U_R071, U_R072
- Block 04: U_R020, U_R043, U_R099
- Block 05: U_R100
- Block 06: U_R108
- Block 07: U_R049
- Block 09: U_R031
- Block 11: U_R109
- Block 13: U_R125_ROSARIO_AR
- Block 14: U_R101
- Block 15: U_R010, U_NR044
- Block 16: U_NR058
- Block 17: U_R125_BARRANQUILLA_CO
- Block 19: U_R067
- Block 20: U_R066

The historical framework is also documented by:

- `docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_R.md`;
- `docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_S.md`.

Those snapshots explicitly preserve `PRIMARY_POOLABLE = 26` before the all-76 target/conditional rerun and preserve the original `simple TGA` target rule as the sensitivity framework.

## 6. Arithmetic QA

**PASS — 26/26 rows.**

For every sensitivity row:

- `denominator = final_failed - target`;
- `strict + can_u + noncan + healthy + unknown = denominator`;
- `expanded = strict + can_u`;
- `0 <= strict <= expanded <= denominator`.

No integer arithmetic failure was found.

`strict_prop` and `expanded_prop` were recomputed from integer counts and stored only as descriptive row-level proportions.

## 7. R125 cluster metadata

**PASS.**

Historical S2 retains:

- U_R125_BARRANQUILLA_CO;
- U_R125_ROSARIO_AR;

with `program_cluster = R125_SIBEN_2020` for both, matching the preserved overlap/non-independence resolution. They remain separate rows in this input; any later cluster aggregation is governed by the locked SAP sensitivity specification.

## 8. Sensitivity-only safeguard

This corrected file is explicitly **SENSITIVITY ONLY**.

It must not:

- alter the final 28-unit primary membership;
- overwrite post-rerun primary values;
- be used as the authoritative current target mapping;
- weaken the amended d-TGA rule;
- restore historical values into `PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`.

## 9. Correction record

Rejected candidate sensitivity version:

- commit `60b3fe2bc4b6153a5a5099ffe89f99f453beca6b` — 23-row hybrid.

Canonical corrected sensitivity version:

- commit `cd2940a1b7712b46d580957f8d3687674b728ad9`;
- blob SHA `61e8ff9f3bb875fbc30f3964ee2e72a448cc94f2`;
- rows **26**.

The correction occurred before any authoritative meta-analysis result.

## 10. Gate H conclusion

Gate H: **PASS AFTER CORRECTION**.

The pre-amendment sensitivity input is now arithmetically closed, membership-reconciled, historically traceable, explicitly sensitivity-only, and suitable for later use under the locked SAP with the interpretation caveat above.
