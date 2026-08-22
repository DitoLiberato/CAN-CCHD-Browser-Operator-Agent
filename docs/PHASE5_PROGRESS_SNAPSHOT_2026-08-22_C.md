# CAN-CCHD Phase 5 — Progress Snapshot C

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT**

## Current state

Phase 5 continues exclusively from the 76 frozen unique quantitative units created at Phase 4.5 closure. No scientific value is imported from the legacy Browser Agent/database.

## Completed structured extraction

Fifteen units have now been structurally extracted across Blocks 01–04.

### PRIMARY_POOLABLE = 13

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

### SENSITIVITY_ONLY = 2

- U_R076 Mohsin 2019 — mixed Well Baby/NICU plus non-point-identifiable harmonized target; Strict 0% and Expanded 100% invariant across admissible mapping.
- U_R023 Morocco 2020 — harmonized denominator bounded 10-12 because two study-defined CCHD cases lack required <=28-day intervention/death timing; Strict 5-7 and Expanded 6-8.

### Unresolved holds among extracted units = 0

## Block 04 additions

### U_R020 — POLAR, Netherlands
- denominator = 221;
- respiratory pathology 88;
- infection/sepsis 31;
- other pathology 12;
- non-critical CHD 3;
- healthy 87;
- primary paper links noncardiac illness detection to early recognition and referral for treatment;
- CAN-AB = 131;
- CAN-U = 3;
- Strict = 131/221;
- Expanded = 134/221;
- `PRIMARY_POOLABLE`.

### U_R023 — Morocco
- 15 final fails;
- definite harmonized CCHD = D-TGA 1 + HLHS 2;
- DORV+TGA+PS and CoA+PDA cannot be point-classified without <=28-day intervention timing;
- harmonized denominator = 10-12;
- Strict = 5-7;
- Expanded = 6-8;
- bounded estimate only;
- `SENSITIVITY_ONLY`.

### U_R043 — Oakley, UK
- harmonized denominator = 7, validated by Cochrane 2018 TP=7/FP=7;
- 3 significant non-critical CHD + 4 respiratory illness/sepsis;
- no specific management consequence available in accessible primary report;
- Strict = 0/7;
- Expanded = 7/7;
- `PRIMARY_POOLABLE`.

### U_R099 — Tekleab, Ethiopia
- altitude approximately 2,600 m;
- denominator = 56;
- PPHN 10, including sepsis overlap in 2: all NICU-admitted/treated -> CAN-A=10;
- PDA 11 + ASD 2: monitored until saturation normalized and explicit follow-up advised -> CAN-B=13;
- 33 negative echo + normal pediatric reassessment -> explicitly healthy/no diagnosis=33;
- Strict = 23/56;
- Expanded = 23/56;
- `PRIMARY_POOLABLE`, with mandatory altitude/early-screen subgroup flags.

## Current counts

- Frozen Phase 5 units: **76**
- Structurally extracted: **15/76**
- QA-complete primary-poolable: **13**
- Sensitivity-only: **2**
- Unresolved holds among extracted units: **0**
- Not yet structurally extracted: **61**

## Canonical Block 04 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_04.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_04_AUDIT.md`

## Exact resume point

Proceed to Block 05 from the remaining 61 frozen units. Continue prioritizing units with complete diagnostic distributions while carrying forward:

1. harmonized CCHD lesion mapping;
2. final-failed-screen denominator;
3. Strict versus Expanded CAN-CCHD;
4. >=90% ascertainment;
5. no diagnosis-as-actionability inference;
6. participant-level overlap control;
7. altitude, timing and setting heterogeneity flags.

This snapshot supersedes Snapshot B as the current safe resume point.
