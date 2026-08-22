# CAN-CCHD Phase 5 — Extraction Block 11 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 11 COMPLETE / QA-CLOSED**

## Scope

Block 11 contains four frozen Phase 4.5 quantitative units:

- `U_R105` — Jain 2022, India
- `U_R109` — Murni 2022, Indonesia
- `U_NR007` — Williams 2021, planned out-of-hospital births, United States
- `U_NR008` — Narayen 2016, POLS pilot, Netherlands

All extraction obeys the restart legacy-data firewall. No legacy Browser Agent/database value was used.

Binding rules applied:

1. analytic denominator = unique newborn after the **final** failed screening sequence;
2. initial/borderline screens that normalize on protocol-defined repeat are PASS, not denominator;
3. source CCHD labels do not override the locked lesion-level 28-day target;
4. diagnosis alone does not establish Strict CAN-CCHD;
5. publisher/source arithmetic conflicts are preserved, never repaired by assumption;
6. out-of-hospital cohorts remain extractable but timing/setting are retained as heterogeneity variables;
7. `NOT_POOLABLE` is used when the analytic denominator is intrinsically unreconstructable, rather than creating a permanent pseudo-hold.

---

## U_R105 — Jain 2022, India

Primary source:

Jain D, Jain M, Lamture Y. *Pulse Oximetry Screening for Detecting Critical Congenital Heart Disease in Neonates.* Cureus. 2022;14(12):e32852. PMID 36699784; PMCID PMC9870300; DOI 10.7759/cureus.32852.

### Population / setting

- 5,874 neonates studied.
- Hospital-born neonates from both the postnatal ward **and NICU** were included.
- Screening began at approximately 4 h of life and was repeated on subsequent days.
- Prenatally diagnosed duct-dependent circulation was excluded.

This is an inseparable mixed postnatal-ward/NICU cohort and therefore would already be outside the principal well-baby pool.

### Why the final-failed denominator cannot be reconstructed

The source reports 164 neonates with hypoxemia who underwent echocardiographic evaluation. However:

- 144 had saturations of 90–95%;
- after a 6-hour repeat, only 78 remained hypoxemic;
- therefore 66 normalized on repeat and are PASS under the locked Phase 5 final-fail rule;
- the source nevertheless includes these infants in its echocardiographic/hypoxemia reporting.

The remaining immediate-fail components (<90% and/or >3% limb difference) are not reported in a participant-disjoint way sufficient to reconstruct the final-fail cohort.

Therefore **164 cannot be used as the Phase 5 denominator**.

### Internal cardiac arithmetic conflict

The article states:

- CHD detected = 44;
- subdivided into major/critical = 12 and minor = 32.

But Table 1 reports:

- critical = 12;
- noncritical = 34;
- total implied = 46.

The source also reports rich alternative-diagnosis information among echo-negative/false-positive infants:

- severe birth asphyxia 9;
- meconium aspiration 14;
- sepsis 67;
- PPHN 16;
- pneumothorax 2;
- normal 12;
- these sum to 120.

These data are clinically informative but cannot be linked to a reconstructable final-failed-screen denominator.

### Decision

**NOT_POOLABLE / QA_COMPLETE_NOT_POOLABLE.**

This is not a pending QA hold. The published report itself lacks the information needed to reconstruct the locked analytic denominator and contains irreconcilable cardiac arithmetic. The alternative-diagnosis distribution is retained for narrative/descriptive evidence only.

---

## U_R109 — Murni 2022, Indonesia

Primary source:

Murni IK et al. *Feasibility of screening for critical congenital heart disease using pulse oximetry in Indonesia.* BMC Pediatr. 2022;22:369. PMID 35761296; PMCID PMC9235153; DOI 10.1186/s12887-022-03404-0.

### Population / screening

- 1,452 newborns screened.
- Seemingly healthy newborns were eligible.
- <35 weeks, prenatal CHD, dysmorphic features, cyanosis, murmur and abnormal vital signs were exclusion criteria.
- Symptomatic infants requiring oxygen for asphyxia/PPHN/pulmonary disease were not enrolled in screening.
- Actual timing was mixed: 59% <=24 h and 41% >24 h.
- Ten infants ultimately had positive screening and were referred for echocardiography.

### Raw diagnoses among all 10 final positives

Source-defined `CCHD` = 8:

1. Ebstein anomaly x2;
2. pulmonary atresia + VSD + vertical PDA x1;
3. tricuspid atresia + pulmonary atresia + small secundum ASD x1;
4. mitral atresia + TGA + severe pulmonary stenosis + single ventricle + hypoplastic LV x1;
5. tricuspid atresia + inlet VSD + moderate ASD + small RV + pulmonary stenosis x1;
6. DORV + TGA + VSD x1;
7. unbalanced AVSD + moderate PDA x1.

Source-defined non-CCHD = 2:

- small secundum ASD x1;
- PFO x1.

### Harmonized CCHD mapping

None of the eight source-CCHD cases can be removed automatically under the locked target:

- Ebstein is not an automatic target lesion;
- PA+VSD is conditional and lacks a documented <=28-day intervention/death;
- the PA in the tricuspid-atresia complex is not explicitly PA/IVS;
- TGA occurs only in complex anatomy, not as simple TGA;
- pulmonary stenosis is conditional and lacks the <=28-day qualifier;
- DORV, tricuspid atresia and unbalanced AVSD are not automatic target lesions.

Therefore:

- definite harmonized CCHD = **0**;
- harmonized-CCHD-negative denominator = **10**.

### CAN-CCHD coding

The eight severe structural diagnoses are clearly clinically relevant, but the primary report does not provide participant-specific treatment, escalation, altered disposition or required follow-up beyond diagnostic referral/echo. Diagnostic referral alone is insufficient for Strict.

Thus:

- `CAN-U = 8`;
- small ASD + PFO without qualifying consequence = `NON_CAN = 2`;
- Strict = **0/10**;
- Expanded = **8/10**;
- ascertainment = **100%**.

### Decision

**PRIMARY_POOLABLE / QA_COMPLETE.**

Early screening is retained as a heterogeneity flag. This unit illustrates why source-defined severe/CCHD labels cannot substitute for the locked harmonized target.

---

## U_NR007 — Williams 2021, planned out-of-hospital births

Primary source:

Williams KB et al. *Newborn Pulse Oximetry for Infants Born Out-of-Hospital.* Pediatrics. 2021;148(4):e2020048785. PMID 34531289; DOI 10.1542/peds.2020-048785.

### Population / design

- 3,019 newborns, predominantly Amish/Mennonite Plain communities.
- Early screen at 1–4 h and late screen at 24–48 h.
- Follow-up to 6 weeks.
- Results were deliberately analyzed under two definitions:
  - strict algorithm interpretation;
  - midwife field interpretation.

The article explicitly states that these interpretations did not always correspond.

### Denominator-convention reconstruction

The accessible primary report gives:

- three CCHD detected overall;
- combined field sensitivity 100% and PPV 8.8%;
- combined strict-algorithm sensitivity 66.7% and PPV 5.4%.

These reported values are arithmetically consistent with:

- field: 3 TP / 34 total positives -> approximately **31 source-defined CCHD-negative positives**;
- strict algorithm: 2 TP / 37 total positives -> approximately **35 source-defined CCHD-negative positives**.

Because the study itself treats the two interpretations separately, Phase 5 does not choose one by fiat.

In addition, lesion identities for the three source-CCHD cases were not recoverable in the accessible primary text, so the harmonized target count cannot be established lesion-by-lesion.

### Alternative pathology

The report states that **12 false-positive cases** had other pathology, including:

- noncritical CHD;
- pulmonary disease;
- infection.

No sufficiently linked treatment/escalation/disposition consequence is available in the accessible primary evidence for Strict coding.

Thus, within the source-defined sensitivity frame:

- Strict lower/identified count = **0**;
- CAN-U lower bound = **12**;
- Expanded lower-bound estimate = **12/31 to 12/35** depending denominator convention;
- remaining false-positive cases are clinically incompletely characterized.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

Reasons:

1. field-versus-algorithm denominator convention;
2. source-CCHD lesions unavailable for harmonized mapping;
3. low alternative-outcome classification of the CCHD-negative positive group.

Out-of-hospital setting itself is preserved as heterogeneity, not used as the sole exclusion reason.

---

## U_NR008 — Narayen 2016, POLS pilot, Netherlands

Primary source:

Narayen IC et al. *Pulse Oximetry Screening for Critical Congenital Heart Disease after Home Birth and Early Discharge.* J Pediatr. 2016;170:188-192.e1. PMID 26746119; DOI 10.1016/j.jpeds.2015.12.004.

Same-investigator later program summary used for discrepancy audit:

Narayen IC, Blom NA, te Pas AB. *Pulse Oximetry Screening Adapted to a System with Home Births: The Dutch Experience.* Int J Neonatal Screen. 2018;4:11.

### Population / independence

- 3,625 eligible births;
- 3,090 consented;
- 3,059 actually screened;
- median first screen 1.8 h;
- median second screen 37 h;
- home birth and early hospital discharge setting;
- no CCHD detected;
- 32 false-positive/final positive screens.

The pilot ran October 2013–October 2014. The later POLAR R020 cohort begins July 2015, so there is no temporal participant overlap. Both retain `program_cluster_id = DUTCH_POLS_POLAR`.

### Numerator discrepancy

The primary article states that important noncritical cardiac or noncardiac pathology was found in **62% of false-positive screenings**. With denominator 32 this corresponds to approximately 20 infants.

However, a later same-investigator Dutch-program summary gives the pilot distribution:

- respiratory pathology 8;
- infection/sepsis 3;
- noncritical CHD 3;
- other pathology 2;
- healthy 16.

These categories sum exactly to 32 but identify pathology in only **16/32 = 50%**, not 62%.

This discrepancy was already flagged in Phase 4.5 and remains unresolved. No forced reconciliation is permitted.

### CAN-CCHD coding

The primary article establishes referral and clinically important alternative pathology, but does not provide diagnosis-linked treatment/escalation/disposition evidence sufficient for Strict classification.

Therefore:

- Strict = **0/32** on recovered linked actionability evidence;
- clinically relevant diagnosis burden / CAN-U is bounded **16–20**;
- Expanded = **16–20/32**;
- denominator ascertainment = 100%;
- the uncertainty is a numerator discrepancy, not participant missingness.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

The unit is highly informative for the Dutch sequential-program and very-early-screen sensitivity analyses, but should not receive a single primary effect estimate while the 50% versus 62% pathology discrepancy remains unresolved.

---

## Block 11 summary

| Unit | Status | Harmonized denominator | Strict | Expanded | Main reason |
|---|---|---:|---:|---:|---|
| U_R105 Jain | NOT_POOLABLE | not reconstructable | — | — | initial-pass/final-fail mixing + internal cardiac arithmetic + mixed NICU setting |
| U_R109 Murni | PRIMARY_POOLABLE | 10 | 0 | 8 | complete lesion-level classification and 100% ascertainment |
| U_NR007 Williams | SENSITIVITY_ONLY | source-defined ~31 field / ~35 algorithm; harmonized unresolved | 0 on linked evidence | >=12 | dual denominator convention + unavailable CCHD lesions + low classification |
| U_NR008 POLS pilot | SENSITIVITY_ONLY | 32 | 0 | 16–20 | primary 62% pathology versus later same-investigator 50% table discrepancy |

### Block-level effect

- new `PRIMARY_POOLABLE` = **1**
- new `SENSITIVITY_ONLY` = **2**
- new `NOT_POOLABLE` = **1**
- new unresolved `HOLD_PENDING_QA` = **0**

## Methodological signals reinforced

1. `Initial positive` and `final failed screen` are not interchangeable; a study can have rich alternative-diagnosis data and still be quantitatively unusable if those populations are mixed.
2. A source-CCHD label can collapse to zero definite harmonized CCHD when lesion-level anatomy does not satisfy the locked 28-day target.
3. Denominator-convention uncertainty and numerator-discrepancy uncertainty are different phenomena and should remain separately coded.
4. Out-of-hospital cohorts are not automatically excluded; they can contribute to sensitivity/heterogeneity analyses when denominators and outcomes are sufficiently characterized.
5. `NOT_POOLABLE` is preferable to an indefinite hold when the source publication cannot, even in principle from its reported data, reconstruct the locked analytic unit.

Block 11 is QA-closed.