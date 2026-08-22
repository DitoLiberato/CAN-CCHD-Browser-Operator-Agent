# CAN-CCHD Phase 5 — Extraction Block 13 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 13 COMPLETE / QA-CLOSED**

## Scope

Block 13 contains four frozen quantitative units:

- `U_R041` — Zhao 2014, China
- `U_R135` — Salih 2018, Iraq/Sulaimany
- `U_R125_ROSARIO_AR` — SIBEN Rosario, Argentina
- `U_R125_GUADALAJARA_MX` — SIBEN Guadalajara, Mexico

The initially proposed R042/R066/R067 units were not used in this block because the currently accessible canonical restart-native artifacts do not expose their exact bibliographic identities with enough direct provenance for source-level extraction. They remain frozen units and are moved to the identity-reconciliation queue. No legacy database was consulted.

Binding rules applied:

1. only final failed screens enter the analytic flow;
2. harmonized CCHD is lesion-level and governed by the locked Cochrane-derived definition;
3. conditional lesions require the <=28-day qualifying event;
4. diagnosis or source severity labels do not by themselves establish Strict CAN-CCHD;
5. treatment/monitoring evidence must be explicitly linked;
6. mixed well-baby/NICU populations remain sensitivity-only when outcomes are inseparable;
7. report companions may add provenance/detail but never independent quantitative weight.

---

## U_R041 — Zhao 2014, China

Primary source: Zhao QM et al. *Pulse oximetry with clinical assessment to screen for congenital heart disease in neonates in China: a prospective study.* Lancet. 2014;384:747-754. PMID 24768155. DOI 10.1016/S0140-6736(14)60198-7.

### Population and final-fail flow

The large prospective multicentre study screened 120,707 asymptomatic newborns. The symptomatic cohort was analysed separately. Prenatally diagnosed major CHD was excluded from the screening analysis.

Pulse oximetry alone produced:

- final positive screens = **516**;
- source critical-CHD true positives = **122**;
- source critical-CHD false positives = **394**.

The protocol used repeat measurements four hours apart for borderline results, so the 516 are final pulse-ox positive results rather than unconfirmed first-test abnormalities.

### Source critical definition

The study explicitly defines critical CHD as defects **causing death or requiring intervention before 28 days of age**. Thus the source timing is aligned with the review lock, but the review's lesion list still governs membership.

Pulse-ox detected source-critical lesions:

- critical pulmonary stenosis 10;
- TOF 9;
- truncus arteriosus 2;
- single ventricle 8;
- pulmonary atresia 30;
- TGA 32;
- DORV 8;
- HLHS 3;
- coarctation 3;
- interrupted aortic arch 2;
- critical aortic stenosis 1;
- TAPVC 14.

Total = 122.

### Harmonized CCHD mapping

Removed as harmonized CCHD:

- critical PS10 — conditional lesion with source <=28-day critical qualifier;
- TOF9 — conditional with source qualifier;
- PA30 — if PA/IVS unconditional; if PA/VSD-type, source <=28-day qualifier satisfies the conditional rule; either route qualifies;
- TGA32 — treated as standalone/simple TGA because the source separately tabulates DORV and single-ventricle anatomy;
- HLHS3 — unconditional;
- CoA3 — conditional with source qualifier;
- IAA2 — unconditional;
- critical AS1 — conditional with source qualifier;
- TAPVC14 — conditional with source qualifier.

Total harmonized CCHD removed = **104**.

Re-enter/stay in harmonized-CCHD-negative denominator:

- truncus arteriosus2;
- single ventricle8;
- DORV8.

Total re-entered = **18**.

Therefore:

`516 - 104 = 412 harmonized-CCHD-negative final failed screens`.

### CAN classification

The primary report states that among the 394 source critical-CHD false positives, **180 required medical intervention or further monitoring**:

- other CHD90;
- PPHN41;
- lung problem23;
- preterm birth16;
- infection10.

These categories sum exactly to 180. Because the report explicitly links all 180 participants to intervention/monitoring, they are `CAN-AB=180` and therefore Strict.

The 18 source-critical structural cases that re-enter the review denominator are certainly clinically relevant. However, the source critical definition is `death OR intervention before 28 days`; it does not identify participant-by-participant whether these 18 qualified by intervention or by death. They are therefore conservatively `CAN-U=18`, not automatically Strict.

The remaining 214/394 are the source's residual `true false positives` after removal of the 180 medically consequential cases. They are retained as aggregate `NON_CAN=214` rather than being called healthy.

Final:

- denominator = **412**;
- Strict = **180/412**;
- Expanded = **198/412**;
- NON_CAN = 214;
- ascertainment = 100%.

### Setting

The screening cohort was consecutive and the study/Cochrane characterization permits newborns irrespective of NICU status; gestational ages <35 weeks were present. The asymptomatic cohort is not separable into well-baby versus higher-acuity/NICU subgroups for these outcomes.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

The unit is exceptionally informative and large, but the mixed/inseparable setting prevents principal-pool entry under the pre-specified rule.

---

## U_R135 — Salih 2018 / Sulaimany, Iraq

Primary report identity: Salih AF et al. *Role of Pulse Oximetry Screening for Detection of Life Threatening Congenital Heart Detects in Newborn.* Kurdistan Journal of Applied Research. 2018. DOI 10.24017/science.2018.2.22.

### Post-freeze same-cohort companion recovered during Phase 5

A detailed earlier report was independently recovered:

Sattar RA, Salih AF, Hamawandi AM. *Role of pulse oximetry screening for detection of life threatening congenital heart defects in newborn.* Merit Res J Med Med Sci. 2014;2(2):54-60.

The 2014 report has the same investigators and reproduces the exact quantitative signature used by R135:

- N=2,181;
- positive POS=100;
- CHD=45;
- major CHD=12;
- minor CHD=33;
- no-CHD false positives=55;
- 28/55 with other pathology.

It is therefore treated as a **post-freeze companion/provenance report of the same quantitative cohort**, not as a new bibliographic discovery capable of creating a new unit or weight. It supplies lesion-level and false-positive detail. The web PDF screenshot was attempted after opening the PDF and returned a cache-miss error; text extraction remained available.

### Screening population

- 2,181 enrolled newborns;
- premature newborns excluded;
- screening at 3–6 hours;
- three repeated borderline-positive measurements before echo;
- final POS-positive infants = 100.

### Raw diagnoses

Major CHD12:

- TGA2;
- TOF2;
- tricuspid atresia1;
- HLHS1;
- pulmonary atresia2;
- AVSD2;
- CoA2.

Minor CHD33:

- isolated PDA5;
- mixed PDA8;
- VSD8;
- ASD10;
- pulmonary stenosis2.

No intracardiac CHD55:

- healthy27;
- PPHN6;
- sepsis13;
- RDS4;
- birth asphyxia5.

### Harmonized target

Definite harmonized CCHD:

- standalone TGA2;
- HLHS1.

Pulmonary atresia2 has no septal-anatomy description. If PA/IVS, both are unconditional target cases; otherwise a PA/VSD-type interpretation would require a documented <=28-day event, which is absent. Therefore:

- harmonized CCHD = **3–5**;
- denominator = **95–97**.

TOF2 and CoA2 remain in the denominator because no <=28-day qualifying event is reported. Tricuspid atresia1 and AVSD2 are not automatic target lesions.

### CAN classification

No participant-specific treatment/escalation/disposition/follow-up consequence is documented for the alternative pathologies. Diagnosis alone cannot establish Strict.

`CAN-U` consists of:

- noncardiac pathology28;
- minor PS2;
- major structural diagnoses re-entering the denominator: TOF2 + tricuspid atresia1 + AVSD2 + CoA2 =7;
- plus PA2 if they remain harmonized-negative.

Thus:

- if PA2 qualify as PA/IVS: denominator95, CAN-U37;
- if PA2 remain denominator: denominator97, CAN-U39.

The remaining minor PDA/ASD/VSD combinations total NON_CAN31. Healthy27 is explicit.

Final bound:

- Strict = **0**;
- Expanded = **37–39 / 95–97**;
- ascertainment = 100% in either mapping.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

Reason: pulmonary-atresia anatomy prevents a unique harmonized denominator. Very-early screening (3–6 h) is an additional heterogeneity flag.

---

## U_R125_ROSARIO_AR — SIBEN Rosario

Primary source: Sola A et al. *CCHD Screening Implementation Efforts in Latin American Countries by the Ibero American Society of Neonatology (SIBEN).* Int J Neonatal Screen. 2020;6(1):21. PMCID PMC7422978. DOI 10.3390/ijns6010021.

### Final-fail reconstruction

During intermittent implementation:

- 28 newborns failed the first screen;
- 25 passed repeat testing;
- 3 required an additional repeat;
- only **one infant had a final positive POS**.

The 27 who normalized are PASS and do not enter the review denominator.

The sole final-positive infant:

- had a normal echocardiogram;
- had **severe transient tachypnea**;
- was admitted to NICU;
- required supplemental oxygen for **five days**.

No CCHD was detected in the screened period.

### CAN classification

The diagnosis and acute consequence are directly linked:

- `CAN-A=1`.

Therefore:

- denominator = 1;
- Strict = Expanded = **1/1**;
- ascertainment = 100%.

### Decision

**PRIMARY_POOLABLE / QA_COMPLETE.**

The infant entered NICU as a consequence of the screen-detected illness; this does not make the screening population a baseline NICU cohort. The source describes apparently healthy newborns in rooming-in.

---

## U_R125_GUADALAJARA_MX — SIBEN Guadalajara private hospital

Primary source: same Sola/SIBEN 2020 implementation report.

### Flow

A private hospital screened >1,000 newborns during February 2019–January 2020. Six infants failed POS and all received pediatric-cardiology evaluation with echocardiography.

Diagnoses:

- TGA1;
- pulmonary valve atresia1;
- PPHN2;
- source `true false positives`2.

The two PPHN infants were **promptly treated**.

### Harmonized target

- standalone TGA1 = definite harmonized CCHD;
- pulmonary valve atresia lacks septal anatomy.

If the pulmonary-atresia case is PA/IVS, it is harmonized CCHD. If it is a PA/VSD-type anatomy, the source does not document the required <=28-day death/intervention event.

Therefore:

- harmonized CCHD = 1–2;
- denominator = **4–5**.

### CAN classification

- PPHN2 with prompt treatment -> `CAN-A=2`;
- if pulmonary atresia remains denominator -> `CAN-U=1`;
- two source true false positives -> aggregate `NON_CAN=2`.

Thus:

- denominator4 scenario: Strict2, Expanded2;
- denominator5 scenario: Strict2, Expanded3.

Ascertainment is 100% in both scenarios.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

The only barrier to a principal weight is the unresolved pulmonary-atresia anatomy. The unit remains linked to the `R125_SIBEN_2020` program cluster.

---

## Block 13 summary

| Unit | Status | Harmonized denominator | Strict | Expanded | Main reason |
|---|---|---:|---:|---:|---|
| U_R041 China | SENSITIVITY_ONLY | 412 | 180 | 198 | mixed nursery/NICU setting inseparable |
| U_R135 Iraq | SENSITIVITY_ONLY | 95–97 | 0 | 37–39 | PA anatomy prevents point target mapping |
| U_R125_ROSARIO_AR | PRIMARY_POOLABLE | 1 | 1 | 1 | clean diagnosis + acute management consequence |
| U_R125_GUADALAJARA_MX | SENSITIVITY_ONLY | 4–5 | 2 | 2–3 | PA anatomy prevents point target mapping |

Block-level disposition:

- new PRIMARY_POOLABLE = **1**;
- new SENSITIVITY_ONLY = **3**;
- new HOLD_PENDING_QA = **0**;
- new NOT_POOLABLE = **0**.

## Methodological conclusions reinforced

1. A very large, completely classified study can remain outside the principal pool solely because of inseparable mixed setting.
2. A source critical definition aligned to <=28 days does not override the locked lesion list.
3. `death OR intervention` cannot be silently converted to intervention for Strict CAN-CCHD when participant linkage is absent.
4. Initial failed screens that normalize on repeat are PASS, as illustrated dramatically by Rosario (28 first fails -> 1 final fail).
5. A post-freeze companion publication may improve provenance and lesion-level extraction but never increases the frozen quantitative-unit count.
6. Pulmonary atresia without septal anatomy remains a recurring bounded-mapping problem and should be handled consistently across all units.

Block 13 is QA-closed.
