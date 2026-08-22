# CAN-CCHD Phase 5 — Progress Snapshot D

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT**

## Current state

Phase 5 continues exclusively from the 76 frozen unique quantitative units created at Phase 4.5 closure. No scientific value is imported from the legacy Browser Agent/database.

Nineteen units have now been structurally extracted across Blocks 01–05.

## Current QA disposition

### PRIMARY_POOLABLE = 14

- U_R009
- U_R017
- U_R018
- U_R019
- U_R020
- U_R024
- U_R025
- U_R043
- U_R071
- U_R072
- U_R089
- U_R093
- U_R099
- U_R100

### SENSITIVITY_ONLY = 3

- U_R023 — Morocco; harmonized denominator bounded 10-12, Strict 5-7, Expanded 6-8.
- U_R039 — Bradshaw; harmonized denominator 9, Strict 2/9, Expanded 3/9, only 55.6% sufficiently classified.
- U_R076 — Mohsin; mixed Well Baby/NICU and non-point-identifiable harmonized target; Strict 0% and Expanded 100% invariant across admissible denominator mapping.

### HOLD_PENDING_QA = 2

- U_R033 — Qatar Abu Jarir 2026. Primary source conflict: narrative says 8 CCHD + 26 false positives, while Table 2 lists d-TGA1, Ebstein1, HLHS1, PPHN28, TAPVR1, non-CCHD2. No forced reconciliation; harmonized denominator not frozen.
- U_R102 — Sero 2025 Turkey. 301 positives; 23 CCHD/significant CHD not lesion-separated; named noncardiac categories are not proven mutually exclusive or exhaustive; full text unavailable in current pass. Do not derive an unreported remainder by subtraction.

## Block 05 key results

### U_R100 — Cloete 2020, New Zealand

- screened = 16,644;
- final failed screens = 48;
- study definition of critical cardiac defect matches the locked <=28-day intervention/death target;
- harmonized CCHD = 3;
- denominator = 45;
- 34 had identified non-CCHD pathology and were admitted because of the failed screen -> CAN-A = 34;
- 11 had no identified pathology/slow transition;
- Strict = 34/45;
- Expanded = 34/45;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

### U_R039 — Bradshaw 2012

- screened = 6,745;
- final failed screens = 9;
- source-defined anomalous SVC-to-left-atrium CCHD does not meet an automatic locked harmonized target category and no <=28-day equivalence is established;
- harmonized CCHD = 0; denominator = 9;
- CAN-A = 2;
- CAN-U = 1;
- NON_CAN = 2;
- UNKNOWN = 4;
- Strict = 2/9;
- Expanded = 3/9;
- sufficiently classified = 5/9 = 55.6%;
- `SENSITIVITY_ONLY`.

### U_R033 — Abu Jarir 2026

- 34 POCC-positive infants;
- source narrative and Table 2 are internally incompatible;
- no defensible point harmonized denominator;
- `HOLD_PENDING_QA`.

### U_R102 — Sero 2025

- 29,840 documented POS results;
- 301 positive screens;
- 23 cardiac cases combine CCHD and significant CHD;
- noncardiac diagnoses include sepsis101, congenital pneumonia16, polycythaemia32, TTN52;
- exclusivity/exhaustiveness not established;
- no point denominator/numerator frozen;
- `HOLD_PENDING_QA`.

## Counts

- Frozen Phase 5 units: **76**
- Structurally extracted: **19/76**
- QA-complete primary-poolable: **14**
- Sensitivity-only: **3**
- Unresolved extracted holds: **2**
- Not yet structurally extracted: **57**

## Canonical Block 05 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_05.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_05_AUDIT.md`

## Exact resume point

Proceed to Block 06 from the remaining 57 frozen units. Do not let R033 or R102 block forward extraction. They remain explicit QA holds and can be revisited if a clearer source, supplementary material, full text, erratum, author report or reproducible explanation becomes available.

Continue applying prospectively:
1. locked harmonized CCHD target mapping;
2. final-failed-screen denominator;
3. Strict versus Expanded actionability;
4. >=90% ascertainment;
5. no forced arithmetic reconciliation;
6. no diagnosis-as-actionability inference;
7. participant-level overlap control;
8. timing, altitude and setting heterogeneity flags.

This snapshot supersedes Snapshot C as the current safe resume point.
