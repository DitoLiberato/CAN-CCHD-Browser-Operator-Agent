# CAN-CCHD Phase 5 — Progress Snapshot J

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 11**

## Binding state

Phase 5 continues exclusively from the **76 frozen unique quantitative units** created at Phase 4.5 closure. The restart legacy-data firewall remains binding. No legacy Browser Agent/database value may supply membership, denominator, numerator, diagnosis, actionability, overlap, PRISMA count, meta-analysis weight, or resolve a scientific discrepancy.

## Current extraction counts

After Blocks 01–11:

- frozen Phase 5 units: **76**
- structurally extracted: **43/76**
- `PRIMARY_POOLABLE`: **18**
- `SENSITIVITY_ONLY`: **22**
- `HOLD_PENDING_QA`: **2**
- `NOT_POOLABLE`: **1**
- not yet structurally extracted: **33**

Block 11 created no new unresolved hold.

## PRIMARY_POOLABLE = 18

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
- **U_R109**

## SENSITIVITY_ONLY = 22

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
- **U_NR007**
- **U_NR008**

## HOLD_PENDING_QA = 2

- U_R033 — Qatar: internal source inconsistency between narrative CCHD/false-positive split and diagnostic table.
- U_R102 — Turkey 2025: cardiac target grouping and diagnostic-category exclusivity/exhaustiveness unresolved.

## NOT_POOLABLE = 1

- **U_R105 — Jain 2022, India:** final failed-screen denominator cannot be reconstructed from the publication because protocol-defined repeat-normalizers are mixed into the reported hypoxemic/echo-evaluated group; source cardiac counts are internally inconsistent; mixed NICU/postnatal-ward population is inseparable. This is a terminal quantitative limitation, not a pending hold.

## Block 11 additions

### U_R105 — Jain 2022, India

- 5,874 neonates studied from postnatal ward and NICU.
- Screening began at approximately 4 h.
- Source reports 164 hypoxemic/echo-evaluated infants, but 66 borderline infants normalized on the protocol-defined 6-h repeat and therefore are PASS under the locked final-fail rule.
- The remaining immediate/persistent positive components cannot be reconstructed as a participant-disjoint final-failed cohort.
- Narrative says CHD44 = major12 + minor32, while Table 1 implies CHD46 = critical12 + noncritical34.
- Rich alternative-diagnosis data are preserved descriptively: severe birth asphyxia9, meconium aspiration14, sepsis67, PPHN16, pneumothorax2, normal12.
- No CAN-CCHD effect estimate is created.
- `NOT_POOLABLE / QA_COMPLETE_NOT_POOLABLE`.

### U_R109 — Murni 2022, Indonesia

- 1,452 seemingly healthy newborns screened; 10 final positives.
- Source-defined CCHD8 comprises Ebstein/complex PA-VSD/tricuspid-atresia/TGA-PS/DORV/unbalanced-AVSD anatomies.
- Under the locked target, none can be removed automatically as harmonized CCHD: no simple TGA, no explicitly established PA/IVS, and conditional PA-VSD/PS lesions lack a documented <=28-day qualifying event.
- harmonized CCHD = 0; denominator = **10**.
- eight severe structural diagnoses lack participant-specific qualifying management consequences -> `CAN-U8`.
- small ASD1 + PFO1 without consequence -> `NON_CAN2`.
- Strict = **0/10**; Expanded = **8/10**; ascertainment = 100%.
- mixed early/post-24-h timing retained as heterogeneity.
- `PRIMARY_POOLABLE / QA_COMPLETE`.

### U_NR007 — Williams 2021, US out-of-hospital

- 3,019 newborns; early 1–4 h plus late 24–48 h screening.
- Study explicitly analyzes both strict-algorithm and midwife-field interpretations because they do not always agree.
- Reported performance is consistent with approximately 34 field-positive versus 37 algorithm-positive combined screens, corresponding to approximately 31 versus 35 source-defined CCHD-negative positives.
- three source-CCHD cases were detected overall, but lesion identities were not recovered sufficiently for harmonized target mapping.
- 12 false-positive cases had other pathology; treatment/escalation linkage insufficient for Strict coding.
- Strict = 0 on recovered linked evidence; Expanded lower bound = 12, with denominator convention dependent.
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_NR008 — Narayen 2016 POLS pilot, Netherlands

- 3,059 screened; no CCHD; 32 final false-positive screens.
- very early/community pathway: median first test 1.8 h, second approximately 37 h.
- primary article reports important pathology in 62% of false positives (~20/32).
- later same-investigator Dutch-program summary gives respiratory8 + infection/sepsis3 + noncritical CHD3 + other pathology2 + healthy16 = pathology16/32.
- no forced reconciliation between 20/32 and 16/32.
- Strict = 0 on recovered diagnosis-linked actionability evidence; Expanded = **16–20/32 bounded**.
- denominator ascertainment = 100%; uncertainty is a numerator discrepancy, not participant missingness.
- pilot and later POLAR R020 are temporally non-overlapping but share `DUTCH_POLS_POLAR` cluster.
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

## Block 11 methodological conclusions

1. Initial/borderline positives that normalize on a protocol-defined repeat cannot be retained in the final-failed denominator.
2. `NOT_POOLABLE` is distinct from `HOLD_PENDING_QA`: it denotes a terminal limitation of the published quantitative structure rather than a potentially resolvable pending discrepancy.
3. Source-defined CCHD may collapse to zero definite harmonized CCHD when lesion anatomy and <=28-day qualifiers do not satisfy the locked target.
4. Out-of-hospital setting itself is not a reason for exclusion; denominator convention and clinical ascertainment govern poolability.
5. A numerator discrepancy between a primary report and a later same-investigator summary is preserved as a bound rather than arbitrarily resolved.

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

Exact restart-native identities still require independent reconstruction for:

- U_R001
- U_R002
- U_R003
- U_R006

They remain part of the frozen 76. Legacy data must not be used to resolve them.

## Canonical Block 11 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_11.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_11_AUDIT.md`

## Exact resume point

Proceed to **Phase 5 Extraction Block 12** from the remaining **33** frozen units.

Continue enforcing:

1. final-failed-screen denominator;
2. lesion-level harmonized CCHD target;
3. Strict vs Expanded actionability;
4. >=90% ascertainment threshold;
5. no diagnosis-as-actionability inference;
6. no normal-echo-as-healthy inference;
7. participant-level overlap control;
8. setting, altitude and screening-timing heterogeneity flags;
9. management-only evidence kept distinct from diagnosis-based CAN-CCHD;
10. `NOT_POOLABLE` separated from resolvable QA holds.

Snapshot J supersedes Snapshot I as the current safe resume point.