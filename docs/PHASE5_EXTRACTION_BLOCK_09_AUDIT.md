# CAN-CCHD Phase 5 — Extraction Block 09 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 09 COMPLETE / QA-CLOSED**

## Scope

Block 09 contains four frozen Phase 4.5 quantitative units:

- `U_R031` — Abu Lehyah 2025, Jordan
- `U_R032` — Majani 2025, Tanzania
- `U_R077` — Tsao 2016, Taipei pilot
- `U_R087` — Kochilas 2013, Minnesota

All extraction obeys the restart legacy-data firewall. No legacy Browser Agent/database value was used.

Binding rules applied prospectively:

1. analytic denominator = harmonized-CCHD-negative **final** failed screens;
2. conditional lesions require documented death/surgery/catheterization within 28 days;
3. diagnosis alone does not establish Strict CAN-CCHD;
4. normal echocardiography alone does not establish global health;
5. missing final-fail outcomes are preserved as UNKNOWN;
6. >=90% terminal ascertainment is required for the principal fully classified analysis;
7. mixed well-baby/NICU cohorts without separable results are sensitivity-only.

---

## U_R031 — Abu Lehyah 2025, Jordan

Primary source: Abu Lehyah NAA et al. *Prospective Evaluation of Pulse Oximetry Screening for Critical Congenital Heart Disease in a Jordanian Tertiary Hospital: High Incidence and Early Detection Challenges.* Pediatr Rep. 2025;17(1):23. PMID 39997630; PMCID PMC11858587; DOI 10.3390/pediatric17010023.

### Population and screening

- 20,482 newborn-nursery infants screened.
- Direct NICU admissions and infants <35 weeks were excluded.
- Median first screening age 20 h (IQR 15–24 h); only 35.4% were screened at or after 24 h.
- Final failed screens = 752.
- All final failures underwent echocardiography/additional evaluation.

### Raw source accounting

The echocardiographic table reconciles all 752 final failures:

- normal echo / no ultimate diagnosis pathway accounting = source complement after cardiac/noncardiac diagnoses;
- PPHN 102;
- HLHS 23;
- TOF 18;
- TGA 17;
- single ventricle 16;
- DORV 12;
- pulmonary atresia 12;
- critical pulmonary stenosis 11;
- coarctation 9;
- TAPVR 9;
- truncus arteriosus 5;
- cardiac mass 2;
- tricuspid atresia 2;
- restrictive cardiomyopathy 1;
- subvalvular aortic stenosis 1.

The article additionally identifies a unique group of 247 babies with PPHN, neonatal sepsis or congenital pneumonia requiring increased monitoring or treatment:

- PPHN 102;
- neonatal sepsis 85;
- congenital pneumonia 60;
- total = 247.

The source definitions strengthen actionability: neonatal sepsis includes antibiotic treatment for >=5 days; congenital pneumonia includes antibiotics >=5 days plus oxygen supplementation >=2 h.

### Harmonized CCHD mapping

The source definition is conceptually close to the review lock because it references life-threatening duct-dependent disease leading to death or intervention in the first 28 days. However, the review lock requires participant/lesion-level evidence for conditional lesions and does not accept the source label alone.

Definite harmonized CCHD removed:

- HLHS 23;
- standalone TGA 17.

Total definite harmonized CCHD = **40**.

The following source cardiac diagnoses remain in the harmonized-CCHD-negative denominator because the required case-level qualifier is absent or the lesion is not automatically in the target:

- TOF 18;
- single ventricle 16;
- DORV 12;
- pulmonary atresia 12 — septal anatomy unspecified;
- critical pulmonary stenosis 11;
- coarctation 9;
- TAPVR 9;
- truncus 5;
- cardiac mass 2;
- tricuspid atresia 2;
- restrictive cardiomyopathy 1;
- subvalvular aortic stenosis 1.

These sum to **98** cardiac diagnoses remaining in the denominator.

Thus:

`752 - 40 = 712 harmonized-CCHD-negative final failed screens`.

### CAN-CCHD coding

- `CAN-AB = 247`: the source explicitly ties this unique noncardiac group to increased monitoring/treatment. The exact acute-versus-management subtype is not separable for all 247, so the group is Strict without forcing A/B subclassification.
- `CAN-U = 98`: clinically relevant cardiac diagnoses remain in the denominator, but subgroup-specific treatment/escalation/disposition/follow-up evidence is not provided sufficiently to promote them to Strict.
- explicit no ultimate diagnosis = 367.

Arithmetic:

`247 + 98 + 367 = 712`.

Therefore:

- Strict = **247/712**;
- Expanded = **345/712**;
- ascertainment = **100%**.

### Source-count QA

The narrative sometimes refers to 138 CCHD/cardiac cases, whereas the unstarred table categories sum to 135. Adding cardiac mass 2 + restrictive cardiomyopathy 1 yields 138 total cardiac anomalies. The Phase 5 extraction does **not** use the narrative 138 as a shortcut; it reconstructs the denominator directly from the complete raw table and locked lesion mapping.

### Decision

**PRIMARY_POOLABLE / QA_COMPLETE.**

This is currently a major addition to the primary evidence base because it supplies a large, fully classified harmonized denominator while preserving early-screen timing as a heterogeneity covariate.

---

## U_R032 — Majani 2025, Tanzania

Primary source: Majani NG et al. PLOS Glob Public Health. 2025;5(7):e0004904. PMID 40674358; PMCID PMC12270164; DOI 10.1371/journal.pgph.0004904.

### Population and flow

- 10,630 newborns screened.
- Regular newborn-nursery population >35 weeks; severe illness/malformation requiring NICU excluded.
- Median screening age 24 h (IQR 18–37 h).
- Final positive screens = 51.
- 49 underwent echocardiography.
- **Two final-positive infants died before echocardiography.**

These two deaths are retained in the Phase 5 final-fail flow. They may not be deleted, assumed CCHD, or assumed CCHD-negative.

### Source-defined evaluated subset

Among the 49 evaluated positives:

- source-defined CCHD = 15;
- source-defined CCHD-negative false positives = 34.

The 34 are fully clinically classified:

- conditions requiring urgent medical intervention = 26;
  - noncritical CHD 5;
  - respiratory disorders 10;
  - infections 11;
- normal = 8.

Thus the author-defined evaluated CCHD-negative subset yields a valid sensitivity estimate:

- Strict = **26/34**;
- normal = **8/34**.

### Why it is not primary-poolable

The accessible main article does not provide the individual lesions for the 15 source-defined CCHD cases. Under the locked harmonized target, the source label cannot substitute for lesion-level mapping. Some of those 15 may qualify as harmonized CCHD and some may re-enter the denominator.

In addition, the two babies who died before echocardiography have unresolved CCHD status.

Therefore neither the harmonized CCHD count nor the harmonized-CCHD-negative denominator is point-identifiable from the currently recovered primary data.

The supporting-material inventory identifies raw/supplemental data, but the lesion-level cases required for a reproducible harmonized reconstruction were not recovered in this extraction pass. No assumption is made to repair that absence.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

No unresolved methodological hold is necessary: the usable author-defined subset and the reason it cannot enter the harmonized primary pool are both explicit. If lesion-level raw data are later recovered, this unit can be re-adjudicated without changing the protocol.

---

## U_R077 — Tsao 2016, Taipei pilot

Primary source: Tsao PC et al. *Pulse Oximetry Screening for Critical Congenital Heart Disease in Newborns: Experience in a Single Institution in Taiwan.* PLoS One. 2016;11(4):e0153407. PMID 27073996; PMCID PMC4830600; DOI 10.1371/journal.pone.0153407.

### Independence / program cluster

Pilot period:

- 1 October 2013 through 31 March 2014.

The later Taipei R029 cohort begins 1 April 2014. Therefore the two cohorts are sequential rather than participant-overlapping. Both retain:

`program_cluster_id = TAIPEI_POX_PROGRAM`.

### Population

- 6,296 newborns screened.
- All live newborns were eligible regardless of health status/location.
- Well-baby nursery, intermediate/special care and NICU infants are not separable for the outcome.
- Final failed screens = 16.
- Median screening age = 25 h; 89.8% screened at 24–36 h.

The mixed setting independently mandates sensitivity-only treatment.

### Harmonized target

Five cases were source-defined CCHD:

- d-TGA 2;
- HLHS 1;
- Ebstein anomaly 1;
- DORV + single ventricle + TAPVR 1.

Definite harmonized CCHD:

- standalone d-TGA 2;
- HLHS 1.

Total removed = **3**.

Ebstein anomaly is not automatically harmonized CCHD. The complex DORV/single-ventricle/TAPVR case contains a conditional TAPVR component but no participant-level <=28-day death/intervention qualifier is reported. Both therefore remain in the denominator.

Harmonized denominator:

`16 - 3 = 13`.

### CAN-CCHD coding

Among the authors' 11 CCHD false positives:

- PDA 1;
- respiratory problems 10, including TTN/RDS/PPHN;
- 8/11 required further management including oxygen/ventilatory support.

Coding:

- `CAN-AB = 8` — exact actionable infant count with specific management consequence, although diagnosis-specific A/B subclassification is not fully separable;
- `CAN-U = 2` — two respiratory diagnoses without qualifying management evidence among the nonmanaged remainder;
- `NON_CAN = 1` — PDA without documented consequence.

The two source-CCHD cases that re-enter the harmonized denominator are clinically relevant but lack qualifying participant-level actionability evidence:

- additional `CAN-U = 2`.

Final:

- Strict = **8/13**;
- CAN-U = 4;
- Expanded = **12/13**;
- NON_CAN = 1;
- ascertainment = 100%.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY** because the cohort mixes well-baby and higher-acuity/NICU populations without separable outcomes. The unit remains valuable for mixed-setting and program-cluster sensitivity analyses.

---

## U_R087 — Kochilas 2013, Minnesota

Primary source: Kochilas LK et al. Pediatrics. 2013;132(3):e587–e594. PMID 23958775; DOI 10.1542/peds.2013-0803.

Companion/reanalysis: R088. R088 supplies no independent quantitative weight.

### Population and implementation

- 7,549 screened in six normal newborn nurseries.
- Six reported failed screens.
- The implementation publication documents interpretation/reporting errors in the screening algorithm; this is retained as a mandatory methodological flag rather than silently reconstructing an idealized denominator.

### Harmonized target

The one source-defined CCHD case is TOF with pulmonary atresia. Under the locked target this behaves as a PA/VSD-type conditional lesion; no participant-level <=28-day death/surgery/catheterization qualifier was recovered in the current primary/restart-native evidence.

Therefore it remains in the harmonized-CCHD-negative denominator.

Harmonized denominator = **6**.

### CAN-CCHD classification

Restart-native primary QA establishes:

- neonatal pulmonary hypertension = 3 among the source CCHD-negative failures;
- TOF/PA case re-entered by harmonization = 1 clinically relevant cardiac diagnosis;
- two remaining reported failed screens = clinically unclassified.

No specific treatment, escalation, disposition change or required follow-up consequence was recovered for the PPHN cases or the re-entered cardiac case. Diagnosis alone cannot be promoted to Strict.

Thus:

- Strict = **0/6**;
- CAN-U = 4;
- Expanded = **4/6**;
- UNKNOWN = 2;
- ascertainment = **4/6 = 66.7%**.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

Reasons:

1. terminal clinical ascertainment <90%; and
2. documented implementation/interpretation errors.

R088 remains companion-only and must never add an independent weight.

---

## Block 09 summary

| Unit | Status | Harmonized denominator | Strict | Expanded | Main reason |
|---|---|---:|---:|---:|---|
| U_R031 Jordan | PRIMARY_POOLABLE | 712 | 247 | 345 | complete table-level reconstruction, 100% ascertainment |
| U_R032 Tanzania | SENSITIVITY_ONLY | not point-identifiable | study-defined 26/34 | at least 26/34 | source-CCHD lesions unavailable + 2 pre-echo deaths |
| U_R077 Taipei pilot | SENSITIVITY_ONLY | 13 | 8 | 12 | mixed well-baby/NICU population |
| U_R087 Minnesota | SENSITIVITY_ONLY | 6 | 0 | 4 | 66.7% ascertainment + implementation errors |

### Block-level poolability effect

- new PRIMARY_POOLABLE = 1
- new SENSITIVITY_ONLY = 3
- new unresolved holds = 0

## Methodological signals reinforced

1. A source definition may be conceptually aligned with the review but still fail lesion-level conditional mapping if <=28-day events are not documented per case/category.
2. Complete raw tables can support a harmonized denominator even when source narrative CCHD totals are internally awkward, provided no arithmetic is invented.
3. Final-fail infants who die before diagnostic evaluation remain in the flow and cannot be silently excluded.
4. An exact actionable count inside a source-defined CCHD-negative subset is valid for sensitivity but does not repair an unidentified harmonized denominator.
5. Mixed NICU/well-baby setting can independently exclude a fully classified unit from the principal pool.
6. Historical implementation errors are preserved as design heterogeneity; Phase 5 does not retroactively substitute an ideal algorithm.

Block 09 is QA-closed.