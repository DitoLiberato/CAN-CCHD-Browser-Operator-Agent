# CAN-CCHD Phase 5 — Progress Snapshot T

Date: 2026-08-22
Branch: `phase5-extraction`
Status: **SAFE RESUME POINT — PHASE 5 FROZEN / READY FOR QUANTITATIVE SYNTHESIS**

## Canonical state

Phase 5 is complete and frozen after the all-76 post-amendment target rerun.

- frozen quantitative units: **76**
- structurally extracted: **76/76**
- d-TGA/TGA/ccTGA rerun: **76/76**
- conditional <=28-day lesion audit: **76/76**
- final hold resolution attempt: complete
- post-rerun numerical overlay: complete
- final pool registry: complete

## Final frozen analysis membership

- PRIMARY_POOLABLE: **28**
- SENSITIVITY_ONLY: **40**
- HOLD_PENDING_QA: **3**
- NOT_POOLABLE: **5**
- total: **76**

## Binding post-Snapshot-S artifacts

1. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH01_TGA_SWEEP.md`
2. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH02_CONDITIONAL_LESIONS.md`
3. `docs/PHASE5_FINAL_HOLD_RESOLUTION_ATTEMPT.md`
4. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`
5. `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`

The harmonized target lock and d-TGA protocol amendment remain methodologically superior to all historical extraction shorthand.

Historical Blocks 01-21 and Snapshots R/S remain immutable provenance records and preserve the pre-amendment sensitivity framework.

## Important rerun effects

The d-TGA amendment and conditional-lesion audit changed numerical values in **20 units**.

Five units moved from SENSITIVITY_ONLY to PRIMARY_POOLABLE after TGA uncertainty was eliminated:

- U_R006
- U_R008
- U_R013
- U_R023
- U_R036

Three previously primary units moved to SENSITIVITY_ONLY after the strict <=28-day / lesion-identity audit showed that no point harmonized target count can be supported:

- U_R020 POLAR
- U_R024 Gopalakrishnan
- U_R043 Oakley

Several primary units retained poolability but received corrected target/denominator values, notably U_R009 Riede, U_R018 Özalkaya, U_R071 Cubells and U_R072 Diller.

## Holds

The three remaining holds were rechecked and remain unresolved evidence limitations:

- U_R033 Qatar
- U_R102 Turkey 2025
- U_R125_SONORA_MX

They are no longer an active search queue and receive no primary weight.

## Exact next movement

Begin quantitative synthesis by building a canonical 28-row PRIMARY_POOLABLE analysis-input dataset using:

- the post-rerun numeric overlay for affected units;
- the latest historical block extraction for unaffected units.

Then run the prespecified Strict primary analysis, followed by Expanded and sensitivity/robustness analyses.

Snapshot T supersedes Snapshot S as the canonical safe resume point.
