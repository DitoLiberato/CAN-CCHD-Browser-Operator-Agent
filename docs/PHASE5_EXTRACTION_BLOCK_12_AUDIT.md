# CAN-CCHD Phase 5 — Extraction Block 12 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 12 COMPLETE / QA-CLOSED**

## Scope

Block 12 contains four frozen units:

- `U_R104` — Gaonkar 2024, India
- `U_R126` — Atitlán-Gil 2020, Hidalgo/Mexico
- `U_R127` — González-Andrade 2018, Quito/Ecuador
- `U_R130` — Rendón Díez 2025, Medellín/Colombia

All extraction used restart-native artifacts and independently reverified primary sources only. Legacy Browser Agent/database data were not used.

Binding rules remained unchanged: final-failed-screen denominator, lesion-level harmonized CCHD mapping, diagnosis-based Strict/Expanded CAN taxonomy, no normal-echo-as-healthy inference, >=90% terminal ascertainment for the principal fully classified analysis, and no forced participant-level reconstruction from aggregate/overlapping categories.

---

## U_R104 — Gaonkar 2024, India

Primary source: Gaonkar PM, Mutha SR, Sanghani IM. *Enhancing Neonatal Care: The Vital Role of Pulse Oximetry in the Early Screening of Critical Congenital Heart Diseases and Respiratory Diseases in Rural Areas.* Cureus. 2024;16(4):e58398. PMID 38756257; PMCID PMC11097288; DOI 10.7759/cureus.58398.

### Population / final-fail flow

- 440 hospital-born newborns.
- Postnatal ward **and NICU** infants included; results inseparable by setting.
- <32-week unstable infants excluded; moderate/late preterm included.
- Screening at <24 h and again >24 h; persistent abnormality after the >24 h/recheck sequence defined final positivity.
- Final positives = **65**.

### Source diagnoses

Among 65 final positives:

- CCHD 4: TOF2, standalone TGA1, TAPVR1;
- PPHN9;
- RDS26;
- source false positives26.

### Harmonized target

- standalone TGA1 = definite harmonized CCHD -> removed;
- TOF2 and TAPVR1 are conditional target lesions; no participant-level <=28-day surgery/catheterization/death qualifier is documented -> remain harmonized-negative.

Harmonized denominator = **64**.

### CAN mapping

The primary report ties management directly to diagnosed groups:

- source-CCHD and PPHN cases were promptly referred to higher medical centers for further treatment;
- persistently positive RDS cases received immediate NICU admission followed by humidified oxygen or CPAP.

Thus, among harmonized-negative infants:

- re-entered TOF2 + TAPVR1 = actionable3;
- PPHN9 = actionable9;
- RDS26 = actionable26;
- total `CAN-A = 38`.

The 26 source false positives are not given a diagnostic/outcome category adequate for CAN-CCHD classification -> `UNKNOWN=26`.

Result:

- Strict = **38/64**;
- Expanded = **38/64**;
- ascertainment = **38/64 = 59.4%**.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

Reasons: mixed postnatal/NICU population is inseparable and terminal classification is <90%.

PDF screenshot attempts were made as required, but the remote PDF cache returned a retrieval error. The machine-readable primary full-text PDF content remained available and was used for extraction.

---

## U_R126 — Atitlán-Gil 2020, Hidalgo/Mexico

Primary source: Atitlán-Gil A et al. *Implementation of diagnostic screening for congenital heart disease in Hidalgo, Mexico.* Arch Cardiol Mex. 2020;90(1):35-41. DOI 10.24875/ACM.M20000084.

### Resolution of the inherited discrepancy

The source gives:

- 1,748 screened;
- 29 screen-positive infants undergoing echocardiographic evaluation;
- among screen positives: simple CHD14 + source CCHD3 + 12 without CHD on echo.

A fourth CCHD is described elsewhere in the article, explaining the abstract's 13.8% CCHD figure. The full text explicitly states that this fourth infant was **clinically identified and did not undergo screening** because severe hypoxemia prompted immediate cardiology evaluation.

Therefore the Phase 4 entry discrepancy is resolved rather than held:

- screen-positive CCHD = 3;
- separate clinically detected/non-screened CCHD = outside the final-fail analytic flow.

### Screen-positive CCHD mapping

The three screen-positive complex cases are reproducibly interpreted as:

1. LV hypoplasia + mitral atresia + aortic atresia + hypoplastic aortic arch + severe TR — anatomy equivalent to HLHS -> definite harmonized CCHD;
2. tricuspid atresia + ASD — not an automatic harmonized target lesion;
3. TOF — conditional lesion; palliative surgery is documented, but the source does not explicitly establish surgery within <=28 days.

Thus:

- definite harmonized CCHD removed = **1**;
- harmonized denominator = **29 - 1 = 28**.

The non-screened fourth CCHD (PA + PDA + severe TR) is never introduced into this denominator.

### CAN mapping

- tricuspid-atresia and TOF cases both underwent palliative operation -> `CAN-AB=2`;
- the 14 simple-CHD cases are explicitly maintained by the program in cardiology follow-up -> `CAN-B=14`;
- the remaining 12 are only documented as no CHD/echo-negative, without noncardiac outcome ascertainment -> `UNKNOWN=12`.

Result:

- Strict = **16/28**;
- Expanded = **16/28**;
- ascertainment = **16/28 = 57.1%**.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

The inherited hold is cleared because the 3-versus-4 CCHD discrepancy is now source-resolved. The unit remains outside the principal pool solely because terminal ascertainment is below 90%.

---

## U_R127 — González-Andrade 2018, Quito/Ecuador

Primary source: González-Andrade F, Echeverría D, López V, Arellano M. *Is pulse oximetry helpful for the early detection of critical congenital heart disease at high altitude?* Congenit Heart Dis. 2018;13(6):911-918. PMID 30095227; DOI 10.1111/chd.12654.

Same-cohort primary supporting source: Echeverría Espinosa DO, López Izquierdo LV, Arellano Reinoso MA. Universidad Central del Ecuador thesis, 2014, with González-Andrade as methodological adviser.

### Population / flow

- Quito altitude = **2,820 m**.
- 963 term newborns screened at 24-48 h.
- final positive screens = **53**.
- no CCHD found.
- published full text states echocardiography was performed in **49/53 (92.5%)**, with 4 not imaged.

This resolves the apparent earlier 53-versus-49 discrepancy: 53 were positive, 49 underwent echo.

### Detailed echo findings among 49

The same-cohort detailed table gives mutually exclusive primary echo labels:

- normal9;
- PFO2;
- PFO + mild pulmonary insufficiency1;
- PDA3;
- ASD23;
- ASD + PDA6;
- ASD + rhythm disorder2;
- ASD + false LV tendon2;
- minimal mitral regurgitation1.

### CAN mapping

- no harmonized CCHD;
- minor/incidental ASD/PDA/PFO, minimal regurgitation, mild PI and false-tendon findings without qualifying management consequence -> `NON_CAN=38`;
- ASD + unspecified rhythm disorder2 are clinically relevant but lack demonstrated actionability -> `CAN-U=2`;
- normal echo9 is not a global healthy/no-diagnosis classification -> UNKNOWN9;
- no echo4 -> UNKNOWN4.

Thus:

- denominator = **53**;
- Strict = **0/53**;
- Expanded = **2/53**;
- NON_CAN = 38;
- UNKNOWN = 13;
- terminal ascertainment = **40/53 = 75.5%**.

The publication states generally that noncyanotic CHD merits follow-up, but does not document qualifying participant-level follow-up/treatment for these screen-positive infants; this statement is not used to promote lesions into Strict.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

High altitude is a major heterogeneity flag, but the immediate reason for exclusion from the principal fully classified pool is ascertainment <90%.

Published-PDF screenshot retrieval was attempted; the remote host timed out. The published full-text search result plus independently reverified same-cohort primary thesis supplied the detailed flow/table.

---

## U_R130 — Rendón Díez 2025, Medellín/Colombia

Primary source: Rendón Díez M et al. *Tamizaje temprano con oximetría de pulso para la detección de cardiopatías congénitas críticas cianóticas. Estudio de pruebas diagnósticas.* Andes Pediatr. 2025;96(2):200-208. DOI 10.32641/andespediatr.v96i2.5374.

### Population / flow

- 609 consecutive newborns >34 weeks and >2,000 g;
- rooming-in or basic neonatal-care service;
- prenatal CCHD excluded;
- screening 6-48 h, median 15.4 h;
- 42 final positive screens;
- all 42 underwent inpatient echo;
- no CCHD detected.

Harmonized denominator = **42**.

### Why the CAN numerator is not point-identifiable

The authors report 29/42 pulse-positive infants as having `noncritical CHD`, but define that outcome as **any abnormal echocardiogram**. Across the 53 total echocardiograms in the study, findings overlap and include:

- ASD3;
- VSD1;
- partial anomalous pulmonary venous connection1;
- PFO36;
- PDA24;
- pulmonary hypertension5.

The report does not provide the participant-level lesion composition of the 29 pulse-positive abnormal echos. Therefore the locked CAN taxonomy cannot determine how many of those 29 represent clinically relevant CAN-U versus transitional/incidental NON_CAN.

Separately, 12/609 infants were hospitalized for sepsis/sepsis risk, hypoglycemia or hyperbilirubinemia, but the report does **not** isolate these 12 to the pulse-positive group. Likewise, later telephone follow-up reports noncardiac hospitalizations but not their original screen status.

Consequently:

- exact denominator = 42;
- harmonized CCHD = 0;
- Strict is not point-identifiable; a purely structural maximum from the birth hospitalization count is 0-12, but this is **not** treated as an event estimate;
- Expanded is also not point-identifiable because the 29 abnormal-echo positives mix physiologic and potentially relevant lesions and overlap linkage is unavailable.

The authors' phrase `falsos positivos rentables` is preserved as source interpretation only and is **not** converted into a CAN category.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

This unit is retained for bounded/structural sensitivity analysis and the early-screening subgroup, but contributes no point CAN-CCHD proportion to the principal pool.

Publisher PDF access was blocked by anti-bot validation; primary SciELO HTML full text was independently verified and sufficient for the extraction.

---

## Block 12 summary

| Unit | Status | Harmonized denominator | Strict | Expanded | Key reason |
|---|---|---:|---:|---:|---|
| U_R104 Gaonkar | SENSITIVITY_ONLY | 64 | 38 | 38 | mixed NICU/ward + 59.4% ascertainment |
| U_R126 Hidalgo | SENSITIVITY_ONLY | 28 | 16 | 16 | source discrepancy resolved; 57.1% ascertainment |
| U_R127 Quito | SENSITIVITY_ONLY | 53 | 0 | 2 | high altitude + 75.5% ascertainment |
| U_R130 Medellín | SENSITIVITY_ONLY | 42 | not point-identifiable | not point-identifiable | positive-subgroup actionability cannot be reconstructed |

Block effect:

- new PRIMARY_POOLABLE = 0
- new SENSITIVITY_ONLY = 4
- new HOLD_PENDING_QA = 0
- new NOT_POOLABLE = 0

## Methodological conclusions reinforced

1. A source-level CCHD count may reconcile once clinically detected but non-screened infants are separated from the pulse-positive analytic flow.
2. A documented therapeutic consequence can make a harmonized-negative structural lesion Strict CAN even when that lesion fails the review's CCHD target.
3. High-altitude physiology is a heterogeneity covariate, not by itself an exclusion rule; missing clinical ascertainment can independently drive sensitivity-only status.
4. `Any abnormal echo` is not a valid synonym for CAN-U because it mixes physiologic/incidental and clinically relevant lesions.
5. Full-cohort hospitalization counts cannot be assigned to the positive-screen subgroup without participant linkage.
6. Normal echo remains UNKNOWN when noncardiac outcome is not ascertained.

Block 12 is QA-closed.