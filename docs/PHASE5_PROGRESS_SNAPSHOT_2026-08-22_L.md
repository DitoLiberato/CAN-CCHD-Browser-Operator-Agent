# CAN-CCHD Phase 5 — Progress Snapshot L

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 13**

## Binding state

Phase 5 continues exclusively from the 76 frozen Phase 4.5 quantitative units. The restart legacy-data firewall remains binding. No legacy Browser Agent/database value may supply membership, denominator, numerator, diagnosis, target mapping, actionability, overlap, PRISMA count or meta-analysis weight.

## Current extraction counts

After Blocks 01–13:

- frozen units: **76**
- structurally extracted: **51/76**
- `PRIMARY_POOLABLE`: **19**
- `SENSITIVITY_ONLY`: **29**
- `HOLD_PENDING_QA`: **2**
- `NOT_POOLABLE`: **1**
- not yet structurally extracted: **25**

Block 13 created no new unresolved hold.

## Block 13 additions

### U_R041 — Zhao 2014, China

- 120,707 asymptomatic newborns in the analytic cohort;
- pulse-ox final positives = 516;
- source critical-CHD true positives = 122; source false positives = 394;
- source critical definition requires death or intervention before 28 days;
- lesion-level harmonization removes 104 cases and returns truncus2 + single ventricle8 + DORV8 to the harmonized-negative denominator;
- harmonized denominator = **412**;
- among the 394 source false positives, 180 required medical intervention or further monitoring -> `CAN-AB180`;
- the 18 re-entered source-critical structural cases are `CAN-U18` because the source qualifier is death OR intervention and participant-level intervention is not separable;
- residual source true-false-positive group = `NON_CAN214`;
- Strict = **180/412**;
- Expanded = **198/412**;
- ascertainment = 100%;
- mixed/inseparable nursery-NICU setting prevents principal pooling;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

Important correction preserved: an early provisional interpretation considered the 18 re-entered critical structural cases Strict, but the final coding correctly leaves them CAN-U because severity/death-or-intervention status does not prove participant-specific actionability.

### U_R135 — Salih 2018, Sulaimany/Iraq

- 2,181 newborns; screening at 3–6 h;
- final positives = 100;
- major CHD12, minor CHD33, no-intracardiac-CHD55;
- detailed same-cohort 2014 report was independently recovered during Phase 5 and treated as post-freeze companion/provenance only, with no new quantitative weight;
- definite harmonized CCHD = standalone TGA2 + HLHS1;
- pulmonary atresia2 lacks septal anatomy, giving CCHD3–5 and denominator **95–97**;
- no diagnosis-specific qualifying management consequence -> Strict0;
- CAN-U = **37–39** depending PA mapping;
- NON_CAN31; explicitly healthy27;
- ascertainment = 100%;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

The detailed 2014 source was an actual PDF. Screenshot calls were attempted as required but returned cache-miss errors; accessible text extraction was used and the limitation is documented in the Block 13 audit.

### U_R125_ROSARIO_AR — SIBEN Rosario

- apparently healthy rooming-in newborns;
- 28 failed first test, 25 passed repeat, 3 required another repeat;
- only **1 final positive**;
- no CCHD;
- severe transient tachypnea, NICU admission and supplemental O2 for five days;
- denominator1;
- `CAN-A1`;
- Strict = Expanded = **1/1**;
- ascertainment = 100%;
- `PRIMARY_POOLABLE / QA_COMPLETE`.

This unit is a strong demonstration that repeat-normalized infants are PASS and must not inflate the final-failed-screen denominator.

### U_R125_GUADALAJARA_MX — SIBEN Guadalajara

- >1,000 newborns screened; final fails6;
- diagnoses: TGA1, pulmonary valve atresia1, PPHN2, source true false positives2;
- standalone TGA1 is definite harmonized CCHD;
- pulmonary-atresia septal anatomy is not reported, so harmonized CCHD =1–2 and denominator = **4–5**;
- PPHN2 were promptly treated -> `CAN-A2`;
- if pulmonary atresia remains denominator -> `CAN-U1`;
- NON_CAN2;
- Strict = **2** across admissible mappings;
- Expanded = **2–3**;
- ascertainment =100%;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

## Current status lists

### PRIMARY_POOLABLE = 19

U_R009, U_R017, U_R018, U_R019, U_R020, U_R024, U_R025, U_R031, U_R043, U_R049, U_R071, U_R072, U_R089, U_R093, U_R099, U_R100, U_R108, U_R109, U_R125_ROSARIO_AR.

### SENSITIVITY_ONLY = 29

U_R007, U_R015, U_R021, U_R022, U_R023, U_R029, U_R030, U_R032, U_R034, U_R035, U_R039, U_R041, U_R053, U_R068, U_R069, U_R076, U_R077, U_R086, U_R087, U_R104, U_R125_SAN_LUIS_AR, U_R125_GUADALAJARA_MX, U_R126, U_R127, U_R128, U_R130, U_R135, U_NR007, U_NR008.

### HOLD_PENDING_QA = 2

- U_R033 — Qatar: internal source inconsistency between narrative CCHD/false-positive split and diagnostic table.
- U_R102 — Turkey 2025: cardiac-target grouping and category exclusivity/exhaustiveness unresolved.

### NOT_POOLABLE = 1

- U_R105 — Jain 2022: final-failed-screen denominator cannot be reconstructed because repeat-normalized infants are included in the source positive group, with an additional internal cardiac-count conflict and inseparable mixed NICU/postnatal population.

## Outstanding retrospective target audit before final primary-pool freeze

The harmonized-target audit remains mandatory for early units extracted before restoration of the exact lesion lock, especially:

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
- U_R042
- U_R066
- U_R067

These units remain part of the frozen 76. They were not dropped and no legacy source may be used to resolve them.

## Post-freeze provenance amendment

A detailed 2014 Sattar/Salih/Hamawandi report was independently recovered during extraction of U_R135. It has the same investigators and exact quantitative signature as the frozen R135 cohort and is treated as a **same-cohort companion/provenance source only**. It does not change the frozen report count, quantitative-unit count, participant count or meta-analysis weight.

## Canonical Block 13 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_13.csv` — commit `1fcfc55aa5304ad3c97ddf903bbd71fe11dbb05e`
- `docs/PHASE5_EXTRACTION_BLOCK_13_AUDIT.md` — commit `35710d245c0a0a4c6559f5abe4fbe249305a0328`

## Exact resume point

Proceed to **Phase 5 Extraction Block 14** from the remaining **25** frozen units.

Continue enforcing:

1. final-failed-screen denominator;
2. lesion-level harmonized CCHD target;
3. Strict vs Expanded diagnosis-based actionability;
4. >=90% ascertainment threshold;
5. no diagnosis-as-actionability inference;
6. no normal-echo-as-healthy inference;
7. no death-or-intervention aggregate treated as intervention without participant linkage;
8. no full-cohort event assignment to a positive subgroup without participant linkage;
9. setting/altitude/timing heterogeneity;
10. program/report clustering and no duplicate weights;
11. post-freeze companions may improve provenance only, not membership or weight;
12. no forced arithmetic reconciliation.

Snapshot L supersedes Snapshot K as the safe resume point.
