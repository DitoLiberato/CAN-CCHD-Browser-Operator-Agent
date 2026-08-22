# CAN-CCHD Phase 5 — Progress Snapshot M

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 14**

## Binding state

Phase 5 continues exclusively from the 76 frozen Phase 4.5 quantitative units. The restart legacy-data firewall remains binding. No legacy Browser Agent/database value may supply membership, denominator, numerator, diagnosis, target mapping, actionability, overlap, PRISMA count or meta-analysis weight.

## Current extraction counts

After Blocks 01–14:

- frozen units: **76**
- structurally extracted: **55/76**
- `PRIMARY_POOLABLE`: **20**
- `SENSITIVITY_ONLY`: **30**
- `HOLD_PENDING_QA`: **2**
- `NOT_POOLABLE`: **3**
- not yet structurally extracted: **21**

Block 14 created no new unresolved hold.

## Block 14 additions

### U_R101 — Singh & Chen 2022, Cambridge

- 23,614 screened in a postnatal-ward population; antenatal CHD and NICU admission before 4 h excluded.
- screening at 4–12 h.
- 1,393 abnormal first screens; 1,033 normalized on the protocol repeat -> PASS.
- **360 remained abnormal on the second protocol screen and are the locked final failed screens**.
- the source's later clinician reclassification into 189 `true positives` +171 clinically well is downstream evaluation and does not redefine screening positivity.
- among the 189: CHD21 + significant noncardiac156 with overlap11 -> unique disease union166.
- source critical CHD6 = HLHS1, hypoplastic aortic arch1, IAA1, CoA1, critical PS2.
- harmonized CCHD =5: HLHS1 +IAA1 +CoA1 +critical PS2; isolated hypoplastic aortic arch re-enters.
- harmonized denominator = **355**.
- `CAN-AB161`; `CAN-U2`; `NON_CAN23`; explicit clinically-well/no-later-diagnosis169.
- Strict = **161/355**.
- Expanded = **163/355**.
- ascertainment =100%.
- inherited 360-vs189 denominator convention flag resolved.
- `PRIMARY_POOLABLE / QA_COMPLETE`.

### U_NR009 — Tekgündüz 2021, Erzurum

- 501 neonates >35 weeks at high altitude.
- screening at 24–48 h used **combined SpO2 + peripheral perfusion index**.
- combined positives21; no CCHD.
- PDA9 among the combined-positive group; remaining12 not sufficiently clinically characterized.
- accessible source does not separate POX-positive from perfusion-index-positive infants.
- a POX final-fail denominator therefore cannot be constructed.
- `NOT_POOLABLE / QA_COMPLETE_NOT_POOLABLE`.

### U_NR059 — John 2016, West Virginia

- statewide well-baby program; NICU infants in first24 h excluded.
- detailed primary flow governs: 19,283 eligible/data-frame infants but **17,120 actually screened with a classified result** =17,101 pass +19 fail.
- final fails19; TTE17; no TTE2.
- source CCHD7 uses a first-year intervention definition broader than the locked 28-day target.
- definite harmonized CCHD among evaluated = HLHS2 +IAA-containing case1 =3.
- pulmonary-atresia anatomy, conditional CoA/TAPVR mapping and two no-TTE failures create a total target range3–6.
- harmonized denominator = **13–16**.
- Strict=0 throughout.
- Expanded=`CAN-U6–7`.
- NON_CAN7; UNKNOWN0–2.
- ascertainment approximately86.7–100% depending admissible mapping.
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_BIRMINGHAM_R027_MAIN — Henderson 2022 + R014 support

- R027 remains representative; R014 overlaps April–July2013 and is never separately summed.
- routine program screened >34-week infants; pre-screen NNU admission excluded.
- published research cohort consists only of **positive-screen infants admitted because further investigation/treatment was required**.
- all final positive screens were not enumerated.
- selected admitted subset253: CCHD8, other significant condition239, transitional/no pathology6 after harmonized target removal.
- descriptive selected-subset Strict yield =239/245.
- this cannot estimate CAN-CCHD among all final failed screens because cohort inclusion was conditioned on an outcome closely aligned with treatment/investigation need.
- full final-fail denominator unavailable.
- `NOT_POOLABLE / QA_COMPLETE_NOT_POOLABLE`.

## Current status lists

### PRIMARY_POOLABLE = 20

U_R009, U_R017, U_R018, U_R019, U_R020, U_R024, U_R025, U_R031, U_R043, U_R049, U_R071, U_R072, U_R089, U_R093, U_R099, U_R100, U_R101, U_R108, U_R109, U_R125_ROSARIO_AR.

### SENSITIVITY_ONLY = 30

U_R007, U_R015, U_R021, U_R022, U_R023, U_R029, U_R030, U_R032, U_R034, U_R035, U_R039, U_R041, U_R053, U_R068, U_R069, U_R076, U_R077, U_R086, U_R087, U_R104, U_R125_SAN_LUIS_AR, U_R125_GUADALAJARA_MX, U_R126, U_R127, U_R128, U_R130, U_R135, U_NR007, U_NR008, U_NR059.

### HOLD_PENDING_QA = 2

- U_R033 — Qatar: internal source inconsistency between narrative CCHD/false-positive split and diagnostic table.
- U_R102 — Turkey 2025: cardiac-target grouping and category exclusivity/exhaustiveness unresolved.

### NOT_POOLABLE = 3

- U_R105 — Jain 2022: protocol final-fail denominator not reconstructable; repeat-normalized infants mixed into source positive group, internal cardiac-count conflict, mixed NICU/postnatal population.
- U_NR009 — Tekgündüz 2021: combined SpO2/perfusion-index positive group cannot be separated into POX final failures.
- U_BIRMINGHAM_R027_MAIN — Henderson 2022: published subcohort selected after positive screening by admission/investigation/treatment requirement; full final-fail denominator not enumerated.

## Block 14 methodological conclusions

1. Protocol repeat logic, not downstream clinician adjudication, defines final failure.
2. Explicit participant overlap permits exact union reconstruction; Cambridge uses `156 + 21 - 11 = 166`.
3. A source <=28-day critical definition does not expand the review's lesion list; off-list lesions still re-enter the denominator.
4. Combined-test cohorts cannot supply a pulse-ox denominator unless the POX component is separable.
5. First-year source CCHD definitions are too broad for the review's conditional <=28-day target.
6. Final failures without TTE remain in the flow and generate uncertainty bounds.
7. Outcome-selected subcohorts cannot estimate a population proportion even when internally well classified.
8. Detailed source flow governs when abstract wording compresses or mislabels the screened count.
9. Program/report overlap remains controlled; no duplicate R014/R027 weight.

## Outstanding retrospective target audit before final primary-pool freeze

Still mandatory for early extracted units that predate complete restoration of the exact lesion lock, especially:

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

These remain part of the frozen 76 and have not been dropped. Legacy sources are prohibited for identity resolution.

## Canonical Block 14 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_14.csv` — corrected West Virginia screened count commit `301dc7fbd0bb97dd5d60ad41f2031fe7b829e704`
- `docs/PHASE5_EXTRACTION_BLOCK_14_AUDIT.md` — commit `f1ab54219cf1270681bfa81aee2a11dcf9e82395`

## Exact resume point

Proceed to **Phase 5 Extraction Block 15** from the remaining **21** frozen units.

Continue enforcing:

1. final-failed-screen denominator;
2. lesion-level harmonized CCHD target;
3. Strict vs Expanded actionability;
4. >=90% ascertainment for the principal fully classified analysis;
5. no diagnosis-as-actionability inference;
6. no normal-echo-as-healthy inference;
7. no downstream clinical reclassification substituted for protocol screening failure;
8. no outcome-selected subcohort used as the full failed-screen denominator;
9. combined-test membership must be POX-separable;
10. setting/altitude/timing heterogeneity;
11. overlap/program clustering and no duplicate weights;
12. no forced arithmetic reconciliation.

Snapshot M supersedes Snapshot L as the safe resume point.