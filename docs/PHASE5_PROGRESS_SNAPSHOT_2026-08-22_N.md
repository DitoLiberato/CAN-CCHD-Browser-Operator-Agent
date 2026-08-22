# CAN-CCHD Phase 5 — Progress Snapshot N

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 15**

## Binding state

Phase 5 continues exclusively from the 76 frozen Phase 4.5 quantitative units. The restart legacy-data firewall remains binding. No legacy Browser Agent/database value may supply membership, identity reconstruction, denominator, numerator, diagnosis, target mapping, actionability, overlap, PRISMA count or meta-analysis weight.

## Current extraction counts

After Blocks 01–15:

- frozen units: **76**
- structurally extracted: **59/76**
- `PRIMARY_POOLABLE`: **22**
- `SENSITIVITY_ONLY`: **32**
- `HOLD_PENDING_QA`: **2**
- `NOT_POOLABLE`: **3**
- not yet structurally extracted: **17**

Block 15 created no new unresolved hold.

## Block 15 additions

### U_R010 — Ewer/PulseOx 2011

- 20,055 asymptomatic newborns >34 weeks;
- median screening age12.4h;
- final positives195;
- 17/18 source-critical cases satisfy the exact locked target; one TGA+VSD case re-enters because the lock specifies simple TGA;
- harmonized denominator178;
- CAN-A40 respiratory/infective conditions requiring intervention;
- CAN-B6 significant CHD with continuing monitoring/drug-treatment definition;
- CAN-U9 = serious CHD8 + re-entered complex TGA/VSD1, conservatively not promoted to Strict because screening-attributable actionability is not participant-level separable;
- NON_CAN123;
- Strict **46/178**;
- Expanded **55/178**;
- ascertainment100%;
- `PRIMARY_POOLABLE / QA_COMPLETE`.

QA correction: a provisional Strict54/178 was rejected before freeze; final Strict is46/178.

### U_R026 — Schwartz 2021, Maryland

- 64,780 well-infant nursery screens;
- final failed screens31;
- all31 have source clinical categories: CCHD12, non-CCHD requiring further follow-up9, noncardiac disorders10;
- lesion identities for source-CCHD12 unavailable;
- harmonized denominator therefore19–31;
- Strict9 throughout;
- CAN-U10–22;
- Expanded19–31;
- source diagnostic ascertainment100%;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_NR002 — Gamhewage 2021, Sri Lanka

- 8,718 healthy term newborns screened at24–48h; prenatal CHD/NICU-before-screen excluded;
- final positives19;
- source CCHD14 plus noncritical CHD4 and one normal echo;
- lesion/event harmonization establishes CCHD8–11 and denominator8–11;
- re-entered source-CCHD cases with explicit surgery/follow-up/palliation pathway -> CAN-AB3–6;
- noncritical CHD4 -> CAN-U4;
- normal echo1 -> UNKNOWN1;
- Strict3–6; Expanded7–10;
- ascertainment87.5%–90.9%;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

### U_NR044 — Kumar 2017, Bangalore

- 22,601 well newborns >36 weeks; NICU excluded;
- final persistent failures14;
- treated pulmonary disease3;
- echo11: minor lesions2 + authors' CCCHD group9;
- diagnostic labels for the nine-case group sum10, preserved as overlap/count inconsistency rather than repaired;
- standalone TGA3 removed as harmonized CCHD;
- remaining six participants from the nine-case source group -> CAN-U6;
- treated pulmonary disease -> CAN-A3;
- minor PDA/VSD+PDA findings -> NON_CAN2;
- denominator11;
- Strict **3/11**; Expanded **9/11**;
- ascertainment100%;
- `PRIMARY_POOLABLE / QA_COMPLETE`.

## Current status lists

### PRIMARY_POOLABLE =22

U_R009, U_R010, U_R017, U_R018, U_R019, U_R020, U_R024, U_R025, U_R031, U_R043, U_R049, U_R071, U_R072, U_R089, U_R093, U_R099, U_R100, U_R101, U_R108, U_R109, U_R125_ROSARIO_AR, U_NR044.

### SENSITIVITY_ONLY =32

U_R007, U_R015, U_R021, U_R022, U_R023, U_R026, U_R029, U_R030, U_R032, U_R034, U_R035, U_R039, U_R041, U_R053, U_R068, U_R069, U_R076, U_R077, U_R086, U_R087, U_R104, U_R125_SAN_LUIS_AR, U_R125_GUADALAJARA_MX, U_R126, U_R127, U_R128, U_R130, U_R135, U_NR002, U_NR007, U_NR008, U_NR059.

### HOLD_PENDING_QA =2

- U_R033 — Qatar source-internal CCHD/diagnostic-table inconsistency.
- U_R102 — Turkey 2025 cardiac-target grouping and category exclusivity/exhaustiveness unresolved.

### NOT_POOLABLE =3

- U_R105 — Jain 2022: final-failed-screen denominator not reconstructable.
- U_NR009 — Tekgündüz 2021: combined SpO2/perfusion-index positivity not POX-separable.
- U_BIRMINGHAM_R027_MAIN — Henderson 2022: outcome-selected admitted-positive subcohort; all final positives not enumerated.

## Remaining 17 frozen units

### Restart-native identity-reconciliation queue =9

Exact bibliographic identity is not sufficiently preserved in currently accessible canonical artifacts for direct extraction without independent reconstruction:

- U_R001
- U_R002
- U_R003
- U_R006
- U_R008
- U_R013
- U_R042
- U_R066
- U_R067

These units remain in the frozen 76 and are not excluded. Legacy data are prohibited for resolving them.

### Identified units still available for direct extraction =8

- U_R036
- U_R037
- U_R125_BARRANQUILLA_CO
- U_R125_SONORA_MX
- U_NR050 — Bagalkot representative cohort; NR051–NR054 companions only
- U_NR058
- U_NR062 — Nellore representative; NR063 companion only
- U_NR064

The identity queue must not block continued extraction of these eight units.

## Outstanding retrospective target audit before final primary-pool freeze

Still mandatory for early extracted units that predate complete restoration of the exact lesion lock, especially:

- U_R017
- U_R019 if TGA complexity remains unclear
- U_R024 pulmonary-atresia anatomy
- U_R025 complex TGA anatomy
- U_R071 TAPVR
- U_R072 TAPVR
- U_R020 lesion-level validation if needed

This audit does not block continued structural extraction.

## Block 15 methodological conclusions

1. Source false-positive terminology based on absence of major CHD cannot substitute for the harmonized denominator.
2. Complex TGA must not be silently mapped as simple TGA.
3. Clinical seriousness/future intervention does not prove screening-attributable Strict actionability.
4. Target uncertainty can persist despite 100% source diagnostic ascertainment.
5. Participant-level class arithmetic may remain usable when diagnostic-label overlap is explicit and no overlap is guessed.
6. Normal echo without noncardiac ascertainment remains UNKNOWN.
7. Companion reports may refine lesion/outcome detail but never add a quantitative weight.
8. Identity uncertainty is handled by a dedicated restart-native reconstruction queue and never by legacy lookup.

## Canonical Block 15 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_15.csv` — commit `53df042bcd6774cbd0c6be1caa6f16ae5bb1d0ec`
- `docs/PHASE5_EXTRACTION_BLOCK_15_AUDIT.md` — commit `4af1ee0b19707b631fb2bdaba22ff6b9de218df2`

## Exact resume point

Proceed to **Phase 5 Extraction Block 16** from the eight directly identifiable unextracted units, preferably prioritizing NR050, NR058, NR062 and NR064 or the SIBEN Barranquilla/Sonora units.

Continue enforcing:

1. final-failed-screen denominator;
2. exact lesion-level harmonized target;
3. Strict vs Expanded actionability;
4. >=90% ascertainment for the principal fully classified analysis;
5. no diagnosis-as-actionability inference;
6. no normal-echo-as-healthy inference;
7. no source CCHD label substituted for locked target;
8. no diagnostic-overlap repair by guesswork;
9. no companion/cluster duplicate weight;
10. no legacy identity reconstruction or scientific data leakage;
11. no forced arithmetic reconciliation.

Snapshot N supersedes Snapshot M as the safe resume point.