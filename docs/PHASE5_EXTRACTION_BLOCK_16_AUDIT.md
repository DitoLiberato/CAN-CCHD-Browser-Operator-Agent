# CAN-CCHD Phase 5 — Extraction Block 16 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **QA COMPLETE**

## Scope

Block 16 extracted four frozen Phase 4.5 quantitative units with restart-native identities already preserved:

- `U_NR050` — Neelannavar/Bagalkot 400 cohort;
- `U_NR058` — Reddy & Devaraj 2018;
- `U_NR062` — Ahmed/Nellore 1000 cohort;
- `U_NR064` — Lanker et al. 2014.

The restart legacy-data firewall remained binding. No legacy Browser Agent/database value was used for identity, eligibility, numerator, denominator, diagnosis, target mapping, actionability, ascertainment or pooling status.

## Cross-block target rule applied

This block applies the stricter target interpretation established during later Phase 5 QA:

> A report label `TGA`/`d-TGA` is not sufficient by itself to establish the unconditional locked lesion **simple TGA**.

Accordingly, isolated TGA labels in NR050 and NR064 remain in the harmonized-CCHD-negative denominator unless simple anatomy is explicitly established. This is deliberately stricter than several earlier blocks and further strengthens the need for the already-planned retrospective TGA/simple-TGA audit before the final primary-pool freeze.

Conditional lesions remain harmonized-negative unless the required <=28-day death/surgery/catheterization event is documented. Off-list diagnoses such as DORV and truncus arteriosus are not automatically harmonized CCHD.

---

## U_NR050 — Neelannavar et al. / Bagalkot

### Primary-source reconstruction

Primary publication and same-cohort thesis establish:

- 400 asymptomatic term/late-preterm newborns;
- screening after 24 h;
- right-hand + foot SpO2;
- 90–95% repeated after 6–12 h;
- seven final hypoxemic/positive screens;
- diagnoses among the seven:
  - TAPVC1;
  - TGA1;
  - DORV2;
  - ASD2;
  - structurally normal heart1.

The 2024 publication gives the lesion counts explicitly: TAPVC1, TGA1 and DORV2 among the four source-labeled CCHD cases.

### Harmonized target

- TGA1: `simple TGA` not established -> stays in denominator.
- TAPVC1: conditional lesion; no <=28-day qualifying event reported -> stays.
- DORV2: not an automatic target lesion -> stays.

Therefore:

- harmonized CCHD = **0**;
- denominator = **7**.

### CAN coding

- TGA/TAPVC/DORV group4 -> `CAN-U4`: clinically relevant diagnoses, but no participant-specific qualifying management consequence recovered;
- ASD2 -> aggregate `NON_CAN2`;
- structurally normal echo1 -> `UNKNOWN1`, not healthy.

Results:

- Strict = **0/7**;
- Expanded = **4/7**;
- ascertainment = **6/7 = 85.7%**;
- `SENSITIVITY_ONLY`.

### Source QA note

The publication's diagnostic-accuracy table explicitly shows CCHD-positive4 / CCHD-negative3 among seven pulse-positive babies, but also prints `False positive = 0`. This metric-label/arithmetic inconsistency is not used to overwrite the explicit participant diagnosis distribution. No forced reconciliation is performed.

### Provenance / PDF handling

The JCDR 2024 primary PDF was opened in the web source and supplied the full lesion table. PDF screenshot calls were attempted on the relevant pages as required, but the source returned cache-miss errors. The machine-readable primary PDF text remained accessible and the failed screenshot attempts are retained as a tooling limitation. The BLDE 2017 thesis is same-cohort companion/provenance only and creates no additional quantitative weight.

---

## U_NR058 — Reddy & Devaraj 2018

### Primary-source reconstruction

- 800 hospital-born newborns;
- study framed as screening asymptomatic newborns;
- screening at 12 h;
- one positive infant;
- SpO2: right thumb88%, left thumb90%, left great toe92%;
- no cyanosis, oedema or tachypnoea;
- echocardiography: ASD + VSD + pulmonary stenosis in the same infant.

### Harmonized target

Pulmonary stenosis is conditional and no <=28-day qualifying invasive event/death is documented. ASD/VSD are off-target.

Therefore:

- harmonized CCHD =0;
- denominator=1.

### CAN coding

The composite structural diagnosis is clinically relevant but the primary report provides no specific treatment, escalation, disposition change or required follow-up consequence attributable to the screening pathway.

- `CAN-U1`;
- Strict **0/1**;
- Expanded **1/1**;
- ascertainment100%.

### Pooling decision

`PRIMARY_POOLABLE`.

Reason: exact final-fail denominator, exact diagnosis, 100% classification and an asymptomatic screening population. Screening at 12 h is retained as a timing heterogeneity flag but does not by itself preclude principal pooling.

Primary publisher HTML was independently reverified. A separate PDF mirror was identified but could not be reopened because of source cache limitations; the publisher HTML contains the decisive methods and outcome data.

---

## U_NR062 — Ahmed 2019 / Nellore

### Primary-source reconstruction

The final 48–72 h measurement, not the earlier <4 h measurement, governs the review's final-fail denominator.

At 48–72 h:

- 1000 term newborns screened;
- seven remained SpO2<95%;
- diagnoses:
  - source cyanotic/CCHD5;
  - acyanotic CHD with severe PPHN1;
  - severe PPHN without reported CHD1.

The paper reports two antenatally detected diagnoses elsewhere (severe pulmonary stenosis; DORV with pulmonary atresia), but does not provide participant-level linkage proving that these correspond to particular members of the five final-positive cyanotic cases. They are therefore not used to force target assignment.

### Harmonized target

The lesion identities of the five source-CCHD final positives are unavailable. Any number from zero to five can qualify under the locked target.

Therefore:

- harmonized CCHD = **0–5**;
- denominator = **2–7**.

### CAN coding

All harmonized-negative cases in every admissible scenario have a clinically relevant diagnosis. However, the primary report does not link those final-positive diagnoses to a specific treatment/escalation/disposition/follow-up consequence. The word `severe` in severe PPHN is not treated as actionability evidence by itself.

Thus:

- Strict = **0** throughout;
- `CAN-U = 2–7`;
- Expanded = **2–7 / 2–7**, proportionally invariant at100%;
- diagnostic ascertainment =100%, but the harmonized denominator is not point-identifiable.

### Pooling decision

`SENSITIVITY_ONLY` because no single harmonized denominator/weight is defensible.

### PDF handling

The primary article was independently reverified from the full-text journal/ResearchGate-indexed PDF text. Direct PDF reopen/screenshot attempts failed because the journal source returned cache-miss/non-PDF errors in the web layer. No OCR or secondary reconstruction was substituted for the readable primary text.

NR063 remains same-cohort companion and creates no independent weight.

---

## U_NR064 — Lanker et al. 2014

### Primary-source reconstruction

- 1200 asymptomatic newborns;
- single postductal screen >24 h;
- three final positive screens;
- TGA1;
- truncus arteriosus1;
- structurally normal heart1.

### Harmonized target

- TGA1: source does not establish `simple TGA` -> remains denominator;
- truncus arteriosus1: not an automatic locked target lesion -> remains denominator.

Therefore:

- harmonized CCHD=0;
- denominator=3.

### CAN coding

- TGA1 + truncus1 -> `CAN-U2`: clinically relevant structural diagnoses without specific qualifying actionability evidence;
- structurally normal echo1 -> `UNKNOWN1`, because normal echo does not establish absence of noncardiac disease.

Results:

- Strict = **0/3**;
- Expanded = **2/3**;
- ascertainment = **66.7%**;
- `SENSITIVITY_ONLY`.

This unit is a direct test of two binding safeguards: source-defined cardiac target labels do not override the harmonized lesion lock, and normal echo is not equivalent to healthy.

---

## Block 16 methodological conclusions

1. `TGA` without sufficiently established simple anatomy is retained in the harmonized-negative denominator.
2. Historical `CCHD` labels never substitute for lesion-level mapping.
3. Pulmonary stenosis without a documented <=28-day qualifying event remains harmonized-negative.
4. Off-list DORV and truncus arteriosus remain harmonized-negative unless anatomy/course independently establishes a locked target component.
5. Normal echocardiography alone remains `UNKNOWN` for the noncardiac CAN outcome.
6. A study can have 100% diagnostic ascertainment but still be sensitivity-only when the harmonized target denominator is not point-identifiable.
7. Early screening is a heterogeneity variable, not an automatic exclusion when the final-fail cohort is otherwise valid.
8. Source arithmetic/metric-label errors are preserved and bypassed only when explicit participant-level diagnosis counts independently establish the analysis; no invented correction is allowed.

## Block 16 disposition

- `PRIMARY_POOLABLE`: **1** — U_NR058.
- `SENSITIVITY_ONLY`: **3** — U_NR050, U_NR062, U_NR064.
- new `HOLD_PENDING_QA`: **0**.
- new `NOT_POOLABLE`: **0**.

## Remaining extraction inventory after Block 16

Block 16 reduces the unextracted frozen inventory from17 to **13 units**.

Four have usable identities and remain suitable for direct extraction:

- U_R036;
- U_R037;
- U_R125_BARRANQUILLA_CO;
- U_R125_SONORA_MX.

Nine remain in restart-native identity reconciliation:

- U_R001;
- U_R002;
- U_R003;
- U_R006;
- U_R008;
- U_R013;
- U_R042;
- U_R066;
- U_R067.

No legacy source may be used to resolve this queue.
