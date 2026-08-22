# CAN-CCHD Phase 5 — All-76 Target Rerun — Batch 01: TGA Sweep

Date: 2026-08-22
Branch: `phase5-extraction`
Parent safe point: Snapshot S, commit `b833bd0ffaa49dc311e12d2d1a48b94a5694554f`
Status: **BATCH 01 COMPLETE / ALL 76 CHECKED FOR TGA TERMINOLOGY / CONDITIONAL-LESION PASS CONTINUES**

## Purpose

Apply the frozen d-TGA protocol amendment systematically across all 76 structurally extracted quantitative units before final pool freezing.

Binding rule:

- d-TGA is an unconditional harmonized CCHD target whether anatomically simple or complex;
- unqualified `TGA` in neonatal CCHD/POS context maps to d-TGA unless the source indicates corrected/l-TGA anatomy;
- explicit ccTGA/l-TGA is not automatically promoted;
- associated VSD/ASD/CoA/PS/PA/DORV/etc. does not negate d-TGA target status;
- a participant with multiple qualifying components is counted once;
- historical block CSVs and Snapshots R/S remain unchanged for provenance.

The companion conditional-lesion audit remains governed by the existing lock: CoA, AS, PS, TOF, PA/VSD and TAPVC/TAPVR require actual death, cardiac surgery, or catheter intervention <=28 days. Missing timing is not affirmative evidence.

## Sweep completeness

All **76/76** frozen quantitative units were checked against their latest structural-extraction record (Blocks 01-17 plus the superseding reconstruction Blocks 19-21).

- units with explicit TGA/d-TGA/ccTGA terminology in the frozen analytic evidence: **34**;
- units without explicit TGA terminology in the frozen analytic evidence: **42**;
- analytic units with a numerical denominator/CAN change from the d-TGA amendment: **13**;
- additional TGA-containing units with no numerical primary-estimand change: retained below for audit completeness;
- explicit ccTGA within a final-positive analytic cohort: **U_R013 only**; it remains non-target under this amendment.

## Numerical changes closed in Batch 01

| Unit | Pre-amendment state | Amended state | CAN consequence | Pool consequence at this stage |
|---|---|---|---|---|
| U_R006 Meberg 2008 | target 0-11; denom 313-324 | **target 11; denom 313** | Strict **32**; Expanded **166** | target uncertainty removed; candidate PRIMARY pending closing conditional-pass QA |
| U_R008 de-Wahl Granelli 2009 | target 5-7; denom 81-83 | **target 11; denom 77** | Strict **42**; CAN-U **8**; Expanded **50** | target uncertainty removed; candidate PRIMARY pending closing conditional-pass QA |
| U_R010 Ewer 2011 | target 17; denom 178 | **target 18; denom 177** | Strict **46** unchanged; CAN-U 9->8; Expanded **54** | remains PRIMARY_POOLABLE |
| U_R013 Turska-Kmiec 2012 | target 2-5; denom 24-27 | **target 5; denom 24** | Strict **0**; Expanded **15**; NON_CAN 9 | isolated ccTGA remains denominator; candidate PRIMARY pending closing conditional-pass QA |
| U_R023 Morocco | target 3-5; denom 10-12 | **target 4; denom 11** | CoA without <=28d event remains denominator/CAN-B; Strict **6**; Expanded **7** | candidate PRIMARY pending closing conditional-pass QA |
| U_R036 Arlettaz 2006 | target 3-5; denom 19-21 | **target 5; denom 19** | Strict **0**; Expanded **18**; UNKNOWN 1 | target uncertainty removed; candidate PRIMARY pending closing conditional-pass QA |
| U_R053 Ghana/Yao | 2 definite targets + 2 pre-echo deaths unresolved; denom 25-27 | **3 definite targets**; denom **24-26** | complex TGA+VSD+PS removed; Strict 0; Expanded lower bound **18** | remains SENSITIVITY_ONLY (mixed setting + pre-echo deaths/missing outcomes) |
| U_R076 Mohsin | 2 definite targets with TGA/conditional bounds | **target 3; denom 13** | TGA + PA/IVSx2 target; no <=28d event for conditional lesions; Strict **0**; Expanded **13** | remains SENSITIVITY_ONLY (mixed Well Baby/NICU) |
| U_R086 New Jersey | target 2; denom 47 | **target 4; denom 45** | d-TGA + generic TGA removed; Strict **2**; CAN-U **8**; Expanded **10**; ascertained 32/45 | remains SENSITIVITY_ONLY (mixed setting + incomplete ascertainment) |
| U_R109 Yogyakarta | target 0; denom 10 | **target 2; denom 8** | both complex TGA-containing cases removed; Strict **0**; CAN-U **6**; Expanded **6** | remains PRIMARY_POOLABLE |
| U_NR050 Bagalkot | target 0; denom 7 | **target 1; denom 6** | TGA removed from CAN-U; Expanded **3**; ascertained 5/6 | remains SENSITIVITY_ONLY (<90% ascertainment) |
| U_NR059 West Virginia | target 3-6; denom 13-16 | **target 4-7; denom 12-15** | TGA+VSD removed; CAN-U **5-6** before no-TTE unknowns | remains SENSITIVITY_ONLY (PA anatomy + 2 no-TTE final fails) |
| U_NR064 Srinagar | target 0; denom 3 | **target 1; denom 2** | TGA removed from CAN-U; Expanded **1**; UNKNOWN 1; ascertainment 50% | remains SENSITIVITY_ONLY |

### Important correction — U_R008 de-Wahl Granelli

Snapshot S correctly identified the two isolated `TGA` rows as an immediate minimum rerun trigger, but the systematic all-76 sweep recovered the full participant table from the primary BMJ report. Among the 19 pulse-positive duct-dependent cases there are **seven TGA-bearing participants**:

1. TGA;
2. TGA;
3. TGA + PA + DILV;
4. TGA + DILV;
5. TGA + CoA + VSD;
6. TGA + DILV + CoA;
7. IAA + TGA + DILV.

The seventh overlaps an already-unconditional IAA case. Therefore the amended target union is:

- HLHS x3;
- IAA x2;
- TGA-bearing x7;
- one IAA/TGA overlap;
- **unique harmonized target = 11**.

Thus `88 - 11 = 77` is the amended CCHD-negative denominator. The 69 source false positives still contribute Strict 42 + NON_CAN 3 + explicit healthy 24; the remaining 8 non-target duct-dependent structural cases are CAN-U. Arithmetic closes exactly: `42 + 8 + 3 + 24 = 77`.

Primary verification used de-Wahl Granelli et al., BMJ 2009;338:a3037, PMCID PMC2627280, Table 1.

## TGA-containing units with no new numerical effect

These units contain TGA terminology but their current analytic count does not change because the TGA-bearing participant was already removed as target through explicit simple/d-TGA wording or through another independently qualifying component, or because the unit is not numerically poolable:

- U_R001 Richmond — simple TGA present, but terminal denominator is unreconstructable; NOT_POOLABLE.
- U_R017 Jawin — PA/VSD case has PDA stent at 1 week; second case contains TGA and remains target; target count remains 2.
- U_R019 South Africa — TGA already target.
- U_R024 Gopalakrishnan — two TGA/IVS cases already target; pulmonary-atresia anatomy remains for the conditional/anatomy pass.
- U_R025 Colombia — TGA+VSD+ASD already target.
- U_R029 Taipei extended — aggregate TGA x8 now unconditionally qualifies, but six multi-diagnosis source-CCHD participants prevent unique participant-level target de-duplication; no point denominator can yet be manufactured.
- U_R031 Jordan — TGA x17 already target.
- U_R035 Hoke — explicit d-TGA already target.
- U_R041 China multicentre — TGA x32 already target; conditional source-critical lesions are independently <=28-day qualified by the source definition.
- U_R066 Northwick Park — TGA+VSD+ASD+CoA participant already target through documented CoA repair day 7 (and arterial switch day 21); no numeric change.
- U_R068 Saudi Arabia — TGA already target; pulmonary-atresia anatomy remains unresolved separately.
- U_R077 Taipei pilot — d-TGA x2 already target.
- U_R100 New Zealand — d-TGA-containing participants already target.
- U_R104 Baramati — standalone TGA already target.
- U_R105 Wardha — TGA/TGA+VSD present, but final-fail denominator is unreconstructable; NOT_POOLABLE.
- U_R108 India — TGA already target.
- U_R135 Iraq — TGA x2 already target; pulmonary-atresia anatomy remains unresolved separately.
- U_NR002 Sri Lanka — standalone TGA already target; residual PA anatomy requires separate audit.
- U_NR044 Bangalore — TGA x3 already target.
- U_BIRMINGHAM_R027_MAIN — TGA x2 appears in the selected admitted-positive subset, but full final-positive denominator is absent; NOT_POOLABLE.
- U_R125_GUADALAJARA_MX — TGA already target; pulmonary-valve-atresia anatomy remains unresolved.

## ccTGA safeguard

U_R013 contains one explicit **congenitally corrected TGA** in addition to three conventional TGA cases. The three conventional TGA cases are now target. The ccTGA participant is **not** promoted by the d-TGA amendment and remains a harmonized-CCHD-negative structural diagnosis unless another qualifying component/event is demonstrated.

No other final-positive analytic unit contains an explicit ccTGA/l-TGA label in the frozen extraction evidence.

## Conditional-lesion findings already closed while applying the TGA rerun

The following conditional decisions are already sufficiently supported and do not need to remain as artificial ranges:

- U_R017 PA/VSD: PDA stenting at 1 week -> qualifies <=28d.
- U_R041 conditional PS/TOF/PA/CoA/AS/TAPVC cases: source critical classification explicitly requires death/intervention within 28 days -> qualifies.
- U_R066 TAPVC: repair day 14 -> qualifies; CoA in TGA complex: repair day 7 -> qualifies.
- U_R100 source target framework: intervention/death <=28d; current mapped conditional target remains qualified.
- U_R101 source critical cases: source definition is intervention/death within 28 days; mapped CoA/critical PS remain qualified.
- U_R023 CoA: no <=28d death/surgery/catheterization documented -> does **not** qualify as target.
- U_R076 TOF/PS/PA-non-IVS possibilities: exhaustive primary/parallel-source search found no lesion-specific <=28d death/surgery/catheterization -> do **not** qualify as conditional target.
- U_R086 CoA/TAPVR: no participant-level <=28d qualifying event documented in the extracted primary evidence -> remain denominator.
- U_R109 PA/VSD and PS components: no <=28d qualifying event documented; only d-TGA components create target status.
- U_NR050 TAPVC: no <=28d qualifying event documented -> remains denominator.
- U_NR059 CoA/TAPVR: source uses a first-year intervention definition and does not establish <=28d events -> remain denominator.

## Still open for the dedicated conditional/anatomy pass

These are not d-TGA questions and must not be silently resolved by the amendment:

- generic/unspecified pulmonary atresia where PA/IVS versus PA/VSD anatomy is not established: U_R021, U_R024, U_R068, U_R135, U_NR002, U_NR059, U_R125_GUADALAJARA_MX;
- participant-level lesion de-duplication/target mapping in U_R029;
- source-CCHD lesion identities unavailable in U_R026, U_R032, U_R037, U_R042, U_R102, U_NR062 and U_R125_SONORA_MX;
- no-TTE final failed screens: U_R053 and U_NR059;
- remaining conditional-lesion timing checks in units whose extraction currently relied on a source target label rather than explicit participant-level <=28-day evidence.

## Batch 01 conclusion

The d-TGA amendment has now been rerun systematically across all 76 frozen extraction units rather than only the Block 21 trigger cases.

No historical block CSV or Snapshot R/S was overwritten. The next movement is the **conditional-lesion/anatomy closure pass**, using this Batch 01 document as the first post-Snapshot-S checkpoint. Final pool counts are intentionally not frozen yet.
