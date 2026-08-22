# CAN-CCHD Phase 5 — Progress Snapshot F

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT**

## Current Phase 5 state

Phase 5 continues exclusively from the 76 frozen unique quantitative extraction units created at Phase 4.5 closure. The legacy Browser Agent/database remains prohibited as a scientific source under `RESTART_LEGACY_DATA_FIREWALL.md`.

## Completed structured extraction

After Blocks 01–07:

- Frozen units: **76**
- Structurally extracted: **27/76**
- PRIMARY_POOLABLE: **16**
- SENSITIVITY_ONLY: **9**
- HOLD_PENDING_QA: **2**
- Not yet structurally extracted: **49**

Existing unresolved holds remain:
- U_R033 — Qatar Abu Jarir 2026: source internal inconsistency between narrative 8 CCHD +26 false positives and Table 2 categories.
- U_R102 — Sero 2025 Turkey: broad cardiac target plus diagnostic-category exclusivity/remainder unresolved.

Block 07 created no new unresolved hold.

## Block 07 units

### U_R035 — Hoke 2002

- 2,876 well-baby newborns;
- 57 final abnormal screens;
- historical four screen-positive cardiac lesions: d-TGA, TOF, CoA, PS;
- exact harmonized mapping removes only standalone/simple d-TGA;
- TOF/CoA/PS are conditional and no <=28-day death/surgery/catheterization evidence was recovered, so they re-enter the review denominator;
- harmonized denominator = **56**;
- PPHN1 + TOF/CoA/PS = CAN-U4;
- healthy39;
- UNKNOWN13;
- Strict = **0/56**;
- Expanded = **4/56**;
- ascertainment = **43/56 = 76.8%**;
- `SENSITIVITY_ONLY`.

Important: the PPHN/healthy/unknown breakdown is supported by a later detailed evidence-synthesis table rather than directly recovered accessible primary full text; provenance is explicit.

### U_R049 — Hamilcikan 2018

Primary full text corrects the screening flow:
- original cohort 4,518;
- 282 excluded before screening;
- **4,236 actually screened**;
- 4,109 >24 h + 127 <24 h;
- 3 failures >24 h + 6 failures <24 h = **9 final failed screens**;
- NICU/continuously monitored infants explicitly ineligible;
- no CCHD.

Terminal diagnoses:
- AVSD2;
- VSD3;
- PDA1;
- TTN2;
- early neonatal sepsis1.

Coding:
- TTN2 + sepsis1 required intensive-care follow-up -> CAN-A3;
- AVSD2 -> CAN-U2;
- VSD3 + PDA1 -> NON_CAN4 because no size/hemodynamic significance or qualifying management/follow-up consequence is documented;
- diagnostic cardiology referral/echo alone is not actionability.

Result:
- denominator9;
- Strict **3/9**;
- Expanded **5/9**;
- ascertainment100%;
- `PRIMARY_POOLABLE`, with early-screen timing heterogeneity flag.

### U_R068 — Almawazini 2017, Al-Baha Saudi Arabia

- 2,961 observational-nursery newborns screened;
- 114 final positives;
- raw cardiac lesions: HLHS2, TGA1, PA1, PS1, AV canal1, truncus1;
- severe PH13;
- PFO45;
- stable VSD5;
- large symptomatic PDA44.

Harmonized target:
- definite CCHD = HLHS2 + standalone/simple TGA1;
- PS is conditional and lacks the required <=28-day invasive intervention/death evidence -> denominator;
- AV canal and truncus -> denominator;
- PA septal anatomy is not reported, so it can only be bounded as PA/IVS versus non-PA/IVS.

Result:
- harmonized CCHD = **3-4**;
- denominator = **110-111**;
- Strict = **0 throughout**;
- CAN-U = **60-61**;
- NON_CAN = 50 (PFO45 + stable VSD5);
- Expanded = **60/110 to 61/111 (54.5%-55.0%)**;
- terminal diagnosis ascertainment =100%;
- `SENSITIVITY_ONLY` because no exact denominator weight can be assigned.

The paper reports PGE/urgent transfer for ductus-dependent patients but does not identify which denominator-relevant lesions received that management; it is not converted into participant-level Strict events.

Al-Baha altitude is retained only as external geographic context, not as a study-reported variable.

### U_R069 — Andrews 2014, Arkansas

- 1,905 screened;
- 3 final failed screens;
- ASD2 + PFO1;
- harmonized CCHD=0;
- denominator=3;
- ASD2 = CAN-U2 because structural diagnosis is reported but no qualifying management consequence;
- PFO1 = NON_CAN;
- Strict **0/3**;
- Expanded **2/3**;
- ascertainment100%.

Setting rule:
- exclusion applied only to age >7 days with continuous NICU monitoring rather than all NICU/intermediate-care exposure;
- authors call cohort `high-risk population`;
- nursery versus short higher-acuity participants are not separable;
- therefore `SENSITIVITY_ONLY` despite complete outcome ascertainment.

## Identity-reconciliation queue created during Block 07

U_R001, U_R002, U_R003 and U_R006 remain frozen eligible extraction units, but their exact bibliographic identities are not sufficiently preserved in currently accessible restart-native repository artifacts to support Phase 5 extraction without guessing.

Binding rule:
- do not infer their article identities;
- do not query the legacy database to recover them;
- resolve later through a dedicated restart-native identity reconstruction from surviving corpus/search artifacts or independent bibliographic reconciliation.

This identity task does **not** alter the frozen 76-unit inventory and does not block extraction of other identifiable units.

## Canonical Block 07 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_07.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_07_AUDIT.md`

## Exact next step

Proceed to Block 08 from the remaining identifiable frozen units, while preserving:

1. exact harmonized CCHD mapping;
2. final-failed-screen denominator;
3. Strict versus Expanded actionability distinction;
4. >=90% terminal ascertainment threshold;
5. well-baby versus mixed/NICU setting rule;
6. no diagnosis-as-actionability inference;
7. explicit provenance when only secondary evidence can supply a clinical subclassification;
8. separate identity-reconciliation queue for U_R001/U_R002/U_R003/U_R006.

This snapshot supersedes Snapshot E as the current safe resume point.
