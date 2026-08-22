# CAN-CCHD Phase 5 — Progress Snapshot H

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 09**

## Binding state

Phase 5 continues exclusively from the 76 frozen unique quantitative units created at Phase 4.5 closure. The restart legacy-data firewall remains binding. No legacy Browser Agent/database value may supply membership, denominator, numerator, diagnosis, actionability, overlap, PRISMA count or meta-analysis weight.

## Current extraction counts

After Blocks 01–09:

- frozen Phase 5 units: **76**
- structurally extracted: **35/76**
- `PRIMARY_POOLABLE`: **17**
- `SENSITIVITY_ONLY`: **16**
- `HOLD_PENDING_QA`: **2**
- not yet structurally extracted: **41**

No new unresolved hold was created in Block 09.

## PRIMARY_POOLABLE = 17

- U_R009
- U_R017
- U_R018
- U_R019
- U_R020
- U_R024
- U_R025
- U_R031
- U_R043
- U_R049
- U_R071
- U_R072
- U_R089
- U_R093
- U_R099
- U_R100
- U_R108

## SENSITIVITY_ONLY = 16

- U_R007
- U_R015
- U_R021
- U_R022
- U_R023
- U_R032
- U_R034
- U_R035
- U_R039
- U_R068
- U_R069
- U_R076
- U_R077
- U_R086
- U_R087
- U_R128

## HOLD_PENDING_QA = 2

- U_R033 — Qatar: internal source inconsistency between narrative CCHD/false-positive split and diagnostic table.
- U_R102 — Turkey 2025: cardiac target grouping and diagnostic-category exclusivity/exhaustiveness unresolved.

## Block 09 additions

### U_R031 — Jordan / Abu Lehyah 2025

- screened = 20,482;
- final failed screens = 752;
- direct NICU admissions excluded;
- early-screen predominant, median 20 h;
- definite harmonized CCHD = HLHS23 + standalone TGA17 = 40;
- harmonized-CCHD-negative denominator = **712**;
- 247 unique babies with PPHN/sepsis/congenital pneumonia explicitly requiring increased monitoring or treatment -> `CAN-AB=247`;
- 98 cardiac diagnoses re-enter/stay in denominator under the locked target but lack subgroup-specific qualifying actionability -> `CAN-U=98`;
- explicit no ultimate diagnosis = 367;
- Strict = **247/712**;
- Expanded = **345/712**;
- ascertainment = 100%;
- `PRIMARY_POOLABLE / QA_COMPLETE`.

Source-count nuance: source narrative/cardio totals are not used as a shortcut. The complete raw table is reconstructed directly under the harmonized lesion lock.

### U_R032 — Tanzania / Majani 2025

- screened = 10,630;
- final failed screens = 51;
- 49 underwent echo;
- two final-positive infants died before echo and remain unascertained in Phase 5;
- among the 49 evaluated: source CCHD15 and author-defined false positives34;
- 34 confirmed source-defined CCHD-negative cases = urgent-intervention condition26 + normal8;
- lesion identities for the 15 source-CCHD cases were not recovered from the accessible main article;
- harmonized denominator therefore cannot be point-identified;
- study-defined sensitivity estimate = Strict **26/34**;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_R077 — Taipei pilot / Tsao 2016

- screened = 6,296;
- final failed screens = 16;
- mixed well-baby/intermediate/special-care/NICU setting inseparable;
- source CCHD5 = d-TGA2, HLHS1, Ebstein1, DORV+single ventricle+TAPVR1;
- definite harmonized CCHD = d-TGA2 + HLHS1 = 3;
- harmonized denominator = 13;
- among 11 source false positives, diagnoses = respiratory10 + PDA1; 8/11 required further management;
- Strict = **8/13 exact**;
- Expanded = **12–13/13 bounded** because the source does not identify whether PDA was among the eight managed infants;
- ascertainment = 100%;
- pilot ends 2014-03-31 and later R029 begins 2014-04-01 -> sequential, non-overlapping, shared `TAIPEI_POX_PROGRAM` cluster;
- `SENSITIVITY_ONLY` because of mixed setting.

### U_R087 — Minnesota / Kochilas 2013

- screened = 7,549;
- reported final failures = 6;
- one source-CCHD = TOF with pulmonary atresia; no locked <=28-day qualifying event recovered -> remains harmonized-negative;
- PPHN3 + re-entered TOF/PA1 = `CAN-U4` because no specific treatment/escalation/disposition/follow-up consequence was recovered;
- two failed screens remain UNKNOWN;
- denominator = 6;
- Strict = **0/6**;
- Expanded = **4/6**;
- ascertainment = 66.7%;
- implementation/interpretation errors retained as design flag;
- R088 companion creates no independent weight;
- `SENSITIVITY_ONLY`.

## Block 09 methodological conclusions

1. Jordan demonstrates that a large study can be primary-poolable after lesion-level harmonization even when the source's own CCHD aggregate labels are imperfect, provided the raw table permits complete reconstruction.
2. Two Tanzanian infants who died before echo remain in the final-fail flow; source analytic exclusion does not authorize Phase 5 deletion.
3. Exact actionable counts do not authorize diagnosis-specific assignment when management linkage is absent; hence Taipei Strict is exact while Expanded is bounded.
4. Mixed setting, low ascertainment and implementation error are distinct sensitivity mechanisms and must remain distinguishable.

## Outstanding cross-block QA before final pooling

A retrospective target-mapping audit remains mandatory for early extracted units that were initially coded before full restoration of the exact Cochrane lesion lock, especially:

- U_R017
- U_R019 if TGA complexity remains unclear
- U_R024 pulmonary-atresia anatomy
- U_R025 complex TGA anatomy
- U_R071 TAPVR
- U_R072 TAPVR
- U_R020 lesion-level validation if needed

This audit must occur before final primary-pool freeze; it does not prevent continued extraction.

## Identity-reconciliation queue

The following frozen units were not extracted in Block 07 because exact restart-native bibliographic identity was not sufficiently preserved in currently accessible canonical artifacts:

- U_R001
- U_R002
- U_R003
- U_R006

They remain part of the frozen 76 and require independent restart-native identity reconstruction. Legacy data must not be used to resolve them.

## Canonical Block 09 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_09.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_09_AUDIT.md`

## Exact resume point

Proceed to **Phase 5 Extraction Block 10** from the remaining 41 frozen units. Continue enforcing:

1. final-failed-screen denominator;
2. lesion-level harmonized CCHD target;
3. Strict vs Expanded actionability;
4. >=90% ascertainment threshold;
5. no diagnosis-as-actionability inference;
6. no normal-echo-as-healthy inference;
7. participant-level overlap control;
8. setting, altitude and screening-timing heterogeneity flags.

Snapshot H supersedes Snapshot G as the current safe resume point.