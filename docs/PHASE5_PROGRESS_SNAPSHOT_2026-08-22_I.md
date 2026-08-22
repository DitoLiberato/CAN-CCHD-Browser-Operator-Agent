# CAN-CCHD Phase 5 — Progress Snapshot I

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 10**

## Binding state

Phase 5 continues exclusively from the 76 frozen unique quantitative units created at Phase 4.5 closure. The restart legacy-data firewall remains binding. No legacy Browser Agent/database value may supply membership, denominator, numerator, diagnosis, actionability, overlap, PRISMA count or meta-analysis weight.

## Current extraction counts

After Blocks 01–10:

- frozen Phase 5 units: **76**
- structurally extracted: **39/76**
- `PRIMARY_POOLABLE`: **17**
- `SENSITIVITY_ONLY`: **20**
- `HOLD_PENDING_QA`: **2**
- not yet structurally extracted: **37**

No new unresolved hold was created in Block 10.

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

## SENSITIVITY_ONLY = 20

- U_R007
- U_R015
- U_R021
- U_R022
- U_R023
- U_R029
- U_R030
- U_R032
- U_R034
- U_R035
- U_R039
- U_R053
- U_R068
- U_R069
- U_R076
- U_R077
- U_R086
- U_R087
- U_R125_SAN_LUIS_AR
- U_R128

## HOLD_PENDING_QA = 2

- U_R033 — Qatar: internal source inconsistency between narrative CCHD/false-positive split and diagnostic table.
- U_R102 — Turkey 2025: cardiac target grouping and diagnostic-category exclusivity/exhaustiveness unresolved.

## Block 10 additions

### U_R029 — Taipei extended program / Tsao 2023

- 93,058 screened; 156 final failed/referral assessments.
- source-defined CCHD false positives = 114.
- source-defined false-positive distribution: respiratory58 + other CHD41 + sepsis2 + other noncardiac3 + no disease10.
- explicit noncardiac illness = 63.
- source CCHD table contains aggregate lesion counts across 42 cases, with six cases carrying >=2 diagnoses.
- unconditional target diagnoses appear in the table, but participant-level combinations are not reconstructable and TGA simplicity / conditional <=28-day qualifiers are unavailable.
- harmonized denominator therefore is not point-identifiable.
- recovered evidence does not link qualifying management to the 63 noncardiac cases sufficiently for Strict coding.
- source-defined sensitivity subset: Strict0/114 on recovered linked evidence; Expanded lower bound63/114.
- extended cohort begins 2014-04-01, one day after R077 pilot ends; sequential/non-overlapping; common `TAIPEI_POX_PROGRAM` cluster.
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_R030 — Pico Mawyin 2025, Ecuador

- 4,897 term rooming-in newborns; 626 final positives.
- 497 diagnostic echocardiographic findings +129 echo-negative =626.
- diagnoses: PDA127; VSD34; ASD25; secondary PH23; PFO272; aortic aneurysm4; CoA8; rhythm disorder4.
- no unconditional harmonized CCHD lesion among listed diagnoses; CoA remains conditional without <=28-day event.
- harmonized CCHD=0; denominator=626.
- CAN-U39 = secondary PH23 + CoA8 + aortic aneurysm4 + rhythm disorder4.
- NON_CAN458 = PFO272 + early PDA127 + VSD34 + ASD25 without qualifying consequence.
- UNKNOWN129 = echo-negative without noncardiac outcome ascertainment.
- Strict0/626; Expanded39/626.
- ascertainment=79.4%, below principal threshold.
- duplicate 2024 RCCSH publication creates no additional weight.
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_R053 — Ghana / Yao 2026

- 5,725 screened; 29 final failed screens; 2 died before echo; 27 imaged.
- mixed well-baby/NICU population inseparable; 74% screened before 24 h.
- participant-level cardiac table permits exact review of imaged cases.
- definite harmonized CCHD among imaged cases = standalone TGA1 + HLHS1 =2.
- known imaged harmonized-negative denominator=25.
- two pre-echo deaths can be CCHD or CCHD-negative -> final denominator 25-27.
- CAN-U lower bound19 = 17 cardiac cases re-entering/staying in denominator + myocarditis1 + PPHN1.
- six recovered source false positives lack etiologic classification; UNKNOWN rises to 8 if both deaths are harmonized-negative.
- Strict0 across admissible mappings; Expanded >=19/25-27.
- ascertainment 70.4%-76.0%.
- R053/NR048 form one Ghana cohort; companion adds no weight.
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_R125_SAN_LUIS_AR — SIBEN San Luis

- >1,400 screened in approximately six months of systematic implementation.
- four final-positive hypoxemic infants; no CCHD.
- all four required supplemental oxygen and had good outcomes.
- etiologic diagnoses are not reported.
- harmonized denominator=4.
- locked CAN diagnosis endpoint: Strict0, Expanded0, UNKNOWN4.
- management-only consequence = oxygen treatment4/4 is preserved separately and may inform a broader clinical-consequence sensitivity analysis.
- does not become Strict CAN solely because treatment occurred without a reported diagnosis.
- `program_cluster_id=R125_SIBEN_2020`.
- `SENSITIVITY_ONLY / QA_COMPLETE_MANAGEMENT_ONLY_SENSITIVITY`.

## Block 10 methodological conclusions

1. Large source-defined CCHD-false-positive samples do not authorize a harmonized denominator when participant-level target mapping is not reproducible.
2. Echo-negative status is not equivalent to healthy/no-diagnosis after complete clinical evaluation.
3. Conditional lesions remain in the harmonized-negative denominator unless the <=28-day qualifying event is documented.
4. Pre-echo deaths remain in the final-fail flow and create denominator bounds when CCHD status is unresolved.
5. Treatment without a reported etiologic diagnosis is clinically meaningful but is not automatically a CAN-CCHD diagnosis.
6. Program-related sequential cohorts remain independent participant cohorts but retain cluster IDs for robust/sensitivity analyses.

## Outstanding cross-block QA before final pooling

A retrospective target-mapping audit remains mandatory for early extracted units initially coded before full restoration of the exact Cochrane lesion lock, especially:

- U_R017
- U_R019 if TGA complexity remains unclear
- U_R024 pulmonary-atresia anatomy
- U_R025 complex TGA anatomy
- U_R071 TAPVR
- U_R072 TAPVR
- U_R020 lesion-level validation if needed

This audit must occur before final primary-pool freeze but does not block continued extraction.

## Identity-reconciliation queue

Exact restart-native identities still require reconstruction for:

- U_R001
- U_R002
- U_R003
- U_R006

They remain part of the frozen 76. Legacy data must not be used to resolve them.

## Canonical Block 10 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_10.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_10_AUDIT.md`

## Exact resume point

Proceed to **Phase 5 Extraction Block 11** from the remaining 37 frozen units.

Continue enforcing:

1. final-failed-screen denominator;
2. lesion-level harmonized CCHD target;
3. Strict vs Expanded actionability;
4. >=90% ascertainment threshold;
5. no diagnosis-as-actionability inference;
6. no normal-echo-as-healthy inference;
7. participant-level overlap control;
8. setting, altitude and screening-timing heterogeneity flags;
9. management-only evidence kept distinct from diagnosis-based CAN-CCHD.

Snapshot I supersedes Snapshot H as the current safe resume point.
