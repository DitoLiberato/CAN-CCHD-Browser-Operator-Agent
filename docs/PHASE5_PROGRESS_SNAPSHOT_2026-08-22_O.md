# CAN-CCHD Phase 5 — Progress Snapshot O

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 16**

## Binding state

Phase 5 continues exclusively from the 76 frozen Phase 4.5 quantitative units. The restart legacy-data firewall remains binding. No legacy Browser Agent/database value may supply membership, identity reconstruction, denominator, numerator, diagnosis, target mapping, actionability, overlap, PRISMA count or meta-analysis weight.

## Current extraction counts

After Blocks 01–16:

- frozen units: **76**
- structurally extracted: **63/76**
- `PRIMARY_POOLABLE`: **23**
- `SENSITIVITY_ONLY`: **35**
- `HOLD_PENDING_QA`: **2**
- `NOT_POOLABLE`: **3**
- not yet structurally extracted: **13**

Block 16 created no new unresolved hold.

These poolability counts remain **provisional pending the mandatory retrospective harmonized-target audit**, especially the expanded simple-TGA consistency audit described below.

## Block 16 additions

### U_NR050 — Neelannavar/Bagalkot

- 400 asymptomatic term/late-preterm newborns; postnatal ward;
- screening >24 h with repeat 6–12 h for borderline values;
- final positives7;
- diagnoses: TAPVC1, TGA1, DORV2, ASD2, structurally normal echo1;
- strict current lock does **not** infer simple TGA from the isolated TGA label;
- TAPVC lacks a qualifying <=28-day event; DORV is off-list;
- harmonized CCHD0; denominator7;
- CAN-U4; NON_CAN2; UNKNOWN1;
- Strict0/7; Expanded4/7;
- ascertainment85.7%;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

Source QA: the article explicitly gives CCHD-positive4/CCHD-negative3 among seven pulse-positive babies while also printing `False positive=0` in its diagnostic-accuracy table. The explicit participant diagnosis counts govern; no arithmetic repair is invented.

### U_NR058 — Reddy & Devaraj 2018

- 800 asymptomatic hospital-born newborns;
- screening at12 h;
- one final positive;
- ASD + VSD + pulmonary stenosis;
- no cyanosis, oedema or tachypnoea;
- pulmonary stenosis is conditional and no <=28-day qualifying event is documented;
- harmonized CCHD0; denominator1;
- CAN-U1;
- Strict0/1; Expanded1/1;
- ascertainment100%;
- `PRIMARY_POOLABLE / QA_COMPLETE`.

Early 12-h timing is retained as a heterogeneity covariate.

### U_NR062 — Ahmed/Nellore

- 1000 term newborns; respiratory disorders/prematurity/ELBW excluded;
- screening within4 h and again48–72 h;
- final 48–72 h failures7;
- source outcomes: cyanotic/CCHD5 + acyanotic CHD with severe PPHN1 + severe PPHN1;
- lesion identities for the five source-CCHD cases are unavailable at participant level;
- harmonized CCHD0–5; denominator2–7;
- no diagnosis-specific qualifying actionability consequence recovered;
- Strict0 throughout;
- CAN-U2–7;
- Expanded=2–7/2–7, proportionally invariant at100%;
- diagnostic ascertainment100%, but target denominator not point-identifiable;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

NR063 is same-cohort companion and creates no weight.

### U_NR064 — Lanker 2014

- 1200 asymptomatic newborns;
- single postductal screen >24 h;
- final positives3;
- TGA1, truncus arteriosus1, structurally normal echo1;
- strict current lock does not infer simple TGA; truncus is off-list;
- harmonized CCHD0; denominator3;
- CAN-U2; UNKNOWN1;
- Strict0/3; Expanded2/3;
- ascertainment66.7%;
- `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

This is an explicit normal-echo-not-healthy safeguard.

## Current status lists

### PRIMARY_POOLABLE =23

U_R009, U_R010, U_R017, U_R018, U_R019, U_R020, U_R024, U_R025, U_R031, U_R043, U_R049, U_R071, U_R072, U_R089, U_R093, U_R099, U_R100, U_R101, U_R108, U_R109, U_R125_ROSARIO_AR, U_NR044, U_NR058.

### SENSITIVITY_ONLY =35

U_R007, U_R015, U_R021, U_R022, U_R023, U_R026, U_R029, U_R030, U_R032, U_R034, U_R035, U_R039, U_R041, U_R053, U_R068, U_R069, U_R076, U_R077, U_R086, U_R087, U_R104, U_R125_SAN_LUIS_AR, U_R125_GUADALAJARA_MX, U_R126, U_R127, U_R128, U_R130, U_R135, U_NR002, U_NR007, U_NR008, U_NR050, U_NR059, U_NR062, U_NR064.

### HOLD_PENDING_QA =2

- U_R033 — Qatar source-internal CCHD/diagnostic-table inconsistency.
- U_R102 — Turkey 2025 cardiac-target grouping and category exclusivity/exhaustiveness unresolved.

### NOT_POOLABLE =3

- U_R105 — Jain 2022: final-failed-screen denominator not reconstructable.
- U_NR009 — Tekgündüz 2021: combined SpO2/perfusion-index positivity not POX-separable.
- U_BIRMINGHAM_R027_MAIN — Henderson 2022: outcome-selected admitted-positive subcohort; all final positives not enumerated.

## Remaining 13 frozen units

### Restart-native identity-reconciliation queue =9

- U_R001
- U_R002
- U_R003
- U_R006
- U_R008
- U_R013
- U_R042
- U_R066
- U_R067

They remain part of the frozen76 and are not excluded. Legacy sources are prohibited for resolving them.

### Directly identified unextracted units =4

- U_R036
- U_R037
- U_R125_BARRANQUILLA_CO
- U_R125_SONORA_MX

The identity queue must not block extraction of these four.

## Expanded retrospective harmonized-target audit — mandatory before primary-pool freeze

Block16 applies the strict rule that only **sufficiently established simple TGA** is unconditional CCHD. An isolated source label `TGA` or `d-TGA` is insufficient by itself. This exposes inconsistent permissive handling in earlier blocks.

At minimum, the retrospective audit must now re-check all extracted units in which TGA/d-TGA was removed or materially affected target mapping, including:

- U_R017 — complex PA/VSD + TGA/DORV anatomy;
- U_R019 — TGA/simple-status question;
- U_R023 — d-TGA and DORV+TGA+PS;
- U_R024 — TGA/IVS wording and PA anatomy;
- U_R025 — TGA+VSD/ASD complex anatomy;
- U_R031 — standalone TGA17 previously removed;
- U_R035 — standalone d-TGA previously removed;
- U_R041 — standalone TGA category previously treated as simple;
- U_R053 — standalone TGA previously removed;
- U_R068 — standalone TGA previously removed;
- U_R077 — d-TGA2 previously removed;
- U_R104 — standalone TGA previously removed;
- U_R108 — TGA mapping;
- U_R125_GUADALAJARA_MX — standalone TGA mapping;
- U_R135 — standalone TGA2 mapping;
- U_NR044 — standalone TGA3 mapping.

Units already using the strict interpretation, such as U_R086, U_R109, U_NR050, U_NR059 and U_NR064, serve as consistency anchors.

The previously planned conditional-lesion audit remains binding as well, especially for TAPVR/TAPVC, PA anatomy, pulmonary stenosis, TOF and CoA cases where <=28-day qualifying events were not documented.

**No final primary meta-analysis may be run until this target audit is complete and any affected block rows are amended.**

## Block16 methodological conclusions

1. Isolated TGA/d-TGA labels do not prove simple TGA.
2. Historical source-CCHD labels never substitute for locked lesion-level mapping.
3. Conditional pulmonary stenosis/TAPVC without a qualifying <=28-day event remains harmonized-negative.
4. DORV and truncus are not automatic locked target lesions.
5. Normal echo without noncardiac ascertainment remains UNKNOWN.
6. Diagnostic ascertainment and target identifiability are separate dimensions.
7. Early screening is a heterogeneity flag, not an automatic exclusion.
8. Explicit diagnosis counts may remain usable despite a source metric-label error; no forced correction is allowed.

## Canonical Block16 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_16.csv` — commit `bba350e180a7e53a43a87ec8e1b0b22d27751473`
- `docs/PHASE5_EXTRACTION_BLOCK_16_AUDIT.md` — commit `547188b244e31f726e718fb1694833d122c53e4f`

## Exact resume point

Proceed to **Phase 5 Extraction Block17** using the four directly identified remaining units, ideally grouping the two standard R units and the two remaining SIBEN sites:

- U_R036;
- U_R037;
- U_R125_BARRANQUILLA_CO;
- U_R125_SONORA_MX.

After those four are structurally extracted, the only unextracted frozen units will be the nine-unit restart-native identity-reconciliation queue. The next major task will then be identity reconstruction plus the mandatory retrospective harmonized-target audit.

Snapshot O supersedes Snapshot N as the safe resume point.
