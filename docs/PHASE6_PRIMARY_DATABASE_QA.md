# CAN-CCHD Phase 6 — Primary Database Readiness QA

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **PRIMARY DATABASE QA PASSED / v1.0 FORMALLY FROZEN**

## 1. Scope

This audit implements the database-readiness gates in `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md` before any authoritative meta-analysis is run.

Primary candidate audited:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA at audit: `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

No legacy Browser Agent/application database was used. Scientific reconciliation used only restart-native frozen Phase 5/6 artifacts and primary-source-derived extraction records.

## 2. Gate A — Primary membership

**PASS.**

- rows: **28**;
- unique `unit_id`: **28**;
- duplicate `unit_id`: **0**;
- membership equals exactly the 28 `PRIMARY_POOLABLE` units frozen in `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`;
- no `SENSITIVITY_ONLY`, `HOLD_PENDING_QA`, or `NOT_POOLABLE` unit is present.

## 3. Gate B — Integer arithmetic and proportions

**PASS — 28/28 rows.**

For every primary row the following identities were recomputed from the stored integer counts:

- `denominator = final_failed - target`;
- `strict + can_u + noncan + healthy + unknown = denominator`;
- `expanded = strict + can_u`;
- `0 <= strict <= expanded <= denominator`.

There were **0 arithmetic failures**.

`strict_prop` and `expanded_prop` were independently recalculated from the integer counts. All 56 stored proportions agree with the recalculated value to the expected 8-decimal rounding precision. Maximum absolute discrepancy was < `5e-9`.

No proportion was used to repair an integer count.

## 4. Gate C — Value-source precedence and provenance

**PASS.**

### Post-rerun overlay rows

Exactly **11** primary units are tagged `POST_RERUN_OVERLAY`, and every current integer value matches `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`:

- U_R006
- U_R008
- U_R009
- U_R010
- U_R013
- U_R018
- U_R023
- U_R036
- U_R071
- U_R072
- U_R109

No stale pre-rerun block value overrides the overlay for these units.

### Unchanged frozen-extraction rows

Exactly **17** rows are tagged `LATEST_FROZEN_EXTRACTION_BLOCK`. Their current counts and metadata were reconciled against their latest frozen extraction records:

- Block 01: U_R017, U_R019, U_R025
- Block 02: U_R089, U_R093
- Block 04: U_R099
- Block 05: U_R100
- Block 06: U_R108
- Block 07: U_R049
- Block 09: U_R031
- Block 13: U_R125_ROSARIO_AR
- Block 14: U_R101
- Block 15: U_NR044
- Block 16: U_NR058
- Block 17: U_R125_BARRANQUILLA_CO
- Block 19: U_R067
- Block 20: U_R066

All 17 reconcile without correction.

For overlay rows, descriptive metadata were also checked against the latest frozen extraction records; the overlay remains authoritative only for the post-rerun numerical fields it supersedes.

## 5. Gate D — Harmonized target ontology

**PASS.**

The frozen primary values are consistent with:

- `docs/PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`;
- `docs/PHASE5_PROTOCOL_AMENDMENT_2026-08-22_D_TGA_TARGET_RULE.md`;
- `docs/PHASE5_ALL76_TARGET_RERUN_BATCH01_TGA_SWEEP.md`;
- `docs/PHASE5_ALL76_TARGET_RERUN_BATCH02_CONDITIONAL_LESIONS.md`;
- the final post-rerun numerical overlay.

Binding safeguards remain intact:

- d-TGA is unconditional target disease whether simple or complex;
- unqualified neonatal TGA maps to d-TGA unless the source indicates corrected/l-TGA;
- ccTGA/l-TGA is not automatically promoted;
- CoA, aortic stenosis, pulmonary stenosis, TOF, PA/VSD, and TAPVC/TAPVR require actual death/surgery/catheterization <=28 days;
- PA/IVS is unconditional;
- generic pulmonary atresia is not silently converted to PA/IVS;
- study labels such as `CCHD`, `critical`, or `major` do not substitute for the locked lesion/event rule.

No new target adjudication was introduced during Phase 6 QA.

## 6. Gate E — Ascertainment and terminal-state integrity

**PASS.**

All 28 primary units satisfy the principal ascertainment requirement.

- **27/28** have 100% terminal ascertainment in the frozen Phase 5 evidence;
- **U_R036** has 18/19 classifiable harmonized-CCHD-negative final failed screens = **94.7%**, with one explicit `UNKNOWN`;
- no primary unit is below 90%.

The terminal categories remain mutually exclusive at the analytic level:

`Strict / CAN-U / NON_CAN / explicitly healthy-no-diagnosis / UNKNOWN`.

`UNKNOWN` was not redistributed by subtraction. `Normal echo` was not recoded as globally healthy unless the source affirmatively supported a healthy/no-diagnosis state.

## 7. Gate F — Non-independence / R125 cluster

**PASS.**

The primary database contains two active R125/SIBEN site units:

- `U_R125_BARRANQUILLA_CO`;
- `U_R125_ROSARIO_AR`.

Both retain `program_cluster = R125_SIBEN_2020`.

Per `docs/PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`, these are geographically distinct, non-overlapping site/program cohorts and remain separate primary analytic units. They must not be summed in the primary database. The locked SAP retains report-cluster aggregation only as a later sensitivity analysis.

## 8. Gate G — Metadata

**PASS.**

Country, setting, timing, altitude, and program-cluster fields were checked against the frozen extraction provenance. No metadata were invented to fill an unknown value.

`total_screened` remains descriptive and is not the meta-analytic denominator. Missing `total_screened` is therefore permitted when the source does not support a point value; the blank value for `U_R125_ROSARIO_AR` is intentional.

## 9. Gate H linkage — pre-amendment sensitivity

The sensitivity database was audited separately in `docs/PHASE6_PREAMENDMENT_SENSITIVITY_QA.md`.

That audit identified and corrected a provenance problem in the original 23-row candidate sensitivity file. This correction does **not** alter the 28-row primary database.

## 10. Primary freeze decision

No correction or normalization was required in `PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`.

Therefore:

> **`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv` is formally frozen as the canonical primary meta-analysis input.**

A `v1.1` primary file is intentionally **not** created because it would duplicate an unchanged dataset and weaken provenance clarity.

Any later change to a primary integer count, membership assignment, target mapping, terminal category, or denominator requires a dated explicit database amendment and must preserve this frozen version for audit.

## 11. Primary database-readiness conclusion

Primary gates A-G: **PASS**.

Primary database status: **FROZEN / READY**, conditional only on successful completion of the separately audited sensitivity-readiness Gate H. No meta-analysis was executed during this audit.
