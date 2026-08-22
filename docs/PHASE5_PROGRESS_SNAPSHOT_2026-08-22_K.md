# CAN-CCHD Phase 5 — Progress Snapshot K

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 12**

## Binding state

Phase 5 continues exclusively from the 76 frozen Phase 4.5 quantitative units. The restart legacy-data firewall remains binding: no legacy Browser Agent/database value may supply scientific membership, denominators, numerators, diagnoses, target mapping, actionability, overlap resolution, PRISMA counts or meta-analysis weights.

## Current extraction counts

After Blocks 01–12:

- frozen units: **76**
- structurally extracted: **47/76**
- `PRIMARY_POOLABLE`: **18**
- `SENSITIVITY_ONLY`: **26**
- `HOLD_PENDING_QA`: **2**
- `NOT_POOLABLE`: **1**
- not yet structurally extracted: **29**

Block 12 created no new unresolved hold.

## Block 12 additions

### U_R104 — Gaonkar 2024, India

- 440 hospital-born neonates, mixed postnatal ward/NICU;
- final positives65;
- source CCHD4 = TOF2 + TGA1 + TAPVR1;
- definite harmonized CCHD = standalone TGA1;
- denominator64;
- re-entered TOF/TAPVR3 + PPHN9 + RDS26 have direct referral/treatment/NICU evidence -> CAN-A38;
- source false positives26 clinically unclassified -> UNKNOWN26;
- Strict38/64; Expanded38/64; ascertainment59.4%;
- `SENSITIVITY_ONLY`.

### U_R126 — Atitlán-Gil 2020, Hidalgo

- 1,748 screened; 29 screen positives;
- detailed screen-positive flow = simple CHD14 + CCHD3 + echo-no-CHD12;
- source fourth CCHD was clinically detected and explicitly not screened, resolving the inherited discrepancy;
- one screen-positive HLHS-equivalent complex removed as harmonized CCHD;
- denominator28;
- re-entered tricuspid-atresia and TOF cases had palliative operations -> CAN-AB2;
- simple CHD14 maintained in cardiology follow-up -> CAN-B14;
- echo-negative12 -> UNKNOWN12;
- Strict16/28; Expanded16/28; ascertainment57.1%;
- inherited entry hold cleared;
- `SENSITIVITY_ONLY`.

### U_R127 — González-Andrade 2018, Quito

- 963 term newborns at 2,820 m;
- 53 final positives, no CCHD;
- published full text explicitly reports echo in 49/53, resolving the apparent 53-versus-49 issue;
- detailed same-cohort table: normal9; PFO2; PFO+mild PI1; PDA3; ASD23; ASD+PDA6; ASD+rhythm disorder2; ASD+false tendon2; minimal MR1;
- CAN-U2 = unspecified rhythm disorders;
- NON_CAN38 = incidental/minor/transitional structural findings without qualifying consequence;
- UNKNOWN13 = normal echo9 + no echo4;
- Strict0/53; Expanded2/53; ascertainment75.5%;
- `SENSITIVITY_ONLY`.

### U_R130 — Rendón Díez 2025, Medellín

- 609 newborns >34 weeks and >2,000g, rooming-in/basic neonatal care;
- screening median15.4h;
- final positive42; no CCHD;
- authors call 29/42 noncritical-CHD positives but define the outcome as any abnormal echo, mixing PFO/PDA/PH and structural lesions;
- participant-level composition of the 29 is unavailable;
- 12 full-cohort noncardiac hospitalizations are not linked to the 42 pulse-positive infants;
- denominator42 exact, but Strict and Expanded CAN numerators are not point-identifiable;
- retain only for bounded/structural sensitivity and early-screen subgroup;
- `SENSITIVITY_ONLY`.

## Current status lists

### PRIMARY_POOLABLE = 18

U_R009, U_R017, U_R018, U_R019, U_R020, U_R024, U_R025, U_R031, U_R043, U_R049, U_R071, U_R072, U_R089, U_R093, U_R099, U_R100, U_R108, U_R109.

### HOLD_PENDING_QA = 2

- U_R033 — Qatar source-internal CCHD/diagnostic-table inconsistency.
- U_R102 — Turkey 2025 cardiac-target grouping and category exclusivity/exhaustiveness unresolved.

### NOT_POOLABLE = 1

- U_R105 — Jain 2022: final-failed-screen denominator cannot be reconstructed; repeat-normalized infants included in source positive group plus internal cardiac-count conflict and mixed NICU/postnatal setting.

### SENSITIVITY_ONLY = 26

U_R007, U_R015, U_R021, U_R022, U_R023, U_R029, U_R030, U_R032, U_R034, U_R035, U_R039, U_R053, U_R068, U_R069, U_R076, U_R077, U_R086, U_R087, U_R104, U_R125_SAN_LUIS_AR, U_R126, U_R127, U_R128, U_R130, U_NR007, U_NR008.

## Outstanding cross-block QA before final primary-pool freeze

Retrospective harmonized-target audit remains mandatory for early units extracted before restoration of the exact lesion lock, especially:

- U_R017
- U_R019 if TGA complexity remains unclear
- U_R024 pulmonary-atresia anatomy
- U_R025 complex TGA anatomy
- U_R071 TAPVR
- U_R072 TAPVR
- U_R020 lesion-level validation if needed

This does not block continued extraction.

## Identity-reconciliation queue

Exact restart-native bibliographic identity still requires independent reconstruction for:

- U_R001
- U_R002
- U_R003
- U_R006

They remain part of the frozen 76. Legacy data must not be used.

## Canonical Block 12 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_12.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_12_AUDIT.md`

## Exact resume point

Proceed to **Phase 5 Extraction Block 13** from the remaining 29 frozen units.

Continue enforcing:

1. final-failed-screen denominator;
2. lesion-level harmonized CCHD target;
3. Strict vs Expanded diagnosis-based actionability;
4. >=90% ascertainment threshold;
5. no diagnosis-as-actionability inference;
6. no normal-echo-as-healthy inference;
7. no full-cohort event assignment to a positive subgroup without participant linkage;
8. setting/altitude/timing heterogeneity;
9. management-only evidence remains distinct from diagnosis-based CAN-CCHD;
10. no forced arithmetic reconciliation.

Snapshot K supersedes Snapshot J as the safe resume point.