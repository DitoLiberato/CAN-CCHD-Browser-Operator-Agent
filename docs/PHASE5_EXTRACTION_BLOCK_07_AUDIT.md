# CAN-CCHD Phase 5 — Extraction Block 07 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_07.csv`

## Scope and identity safeguard

Block 07 was initially going to contain U_R001, U_R002, U_R003 and U_R006. Their R-identities are frozen as eligible quantitative units, but the currently accessible restart-native repository artifacts do not preserve enough bibliographic identity detail to reconstruct those four rows without guessing. The legacy Browser Agent/database is prohibited by `RESTART_LEGACY_DATA_FIREWALL.md` and was not consulted.

Therefore those units remain queued for a dedicated restart-native identity reconciliation. They were **not** assigned identities by inference.

Block 07 instead extracts four unambiguously identified frozen units:

- U_R035 — Hoke 2002;
- U_R049 — Hamilcikan 2018;
- U_R068 — Almawazini 2017;
- U_R069 — Andrews 2014.

No scientific value in this block came from the legacy app/database.

## U_R035 — Hoke 2002, United States

**Primary:** Hoke TR et al. *Oxygen saturation as a screening test for critical congenital heart disease: a preliminary study.* Pediatr Cardiol. 2002;23(4):403-409. PMID 12170356; DOI 10.1007/s00246-002-1482-8.

Primary report:
- 2,876 well-baby nursery newborns;
- screening before 24 h;
- 57 abnormal tests;
- study authors classified 4 as critical CHD.

Independent historical CCHD evidence summaries identify the four screen-positive cardiac lesions as:
- d-TGA x1;
- TOF x1;
- coarctation x1;
- pulmonary stenosis x1.

Under the locked harmonized target:
- standalone d-TGA is treated as simple TGA and is harmonized CCHD;
- TOF, coarctation and pulmonary stenosis are **conditional** lesions;
- no death/surgery/catheterization within the first 28 days was recovered for those three conditional lesions;
- therefore they remain in the harmonized-CCHD-negative denominator rather than being removed merely because the historical paper called them critical.

Thus:
- harmonized CCHD = 1;
- harmonized denominator = 56.

A later detailed pulse-oximetry evidence synthesis reports, among the paper's conventional 53 false positives:
- PPHN = 1;
- healthy = 39;
- unknown = 13.

When the three conditional cardiac lesions are returned to the review denominator:
- CAN-U = 4 (PPHN + TOF + CoA + PS);
- Strict = 0/56;
- Expanded = 4/56;
- explicitly healthy = 39;
- UNKNOWN = 13;
- terminal ascertainment = 43/56 = 76.8%.

No qualifying participant-level management consequence was recovered for the four CAN-U diagnoses. The PPHN/healthy/unknown split is **secondary-supported rather than directly recovered from accessible primary full text**, and this is retained explicitly in provenance.

**Terminal Phase 5 status:** `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY` because ascertainment is below the locked >=90% principal threshold.

## U_R049 — Hamilcikan 2018, Turkey

**Primary:** Hamilcikan S, Can E. *Critical congenital heart disease screening with a pulse oximetry in neonates.* J Perinat Med. 2018;46(2):203-207. PMID 28672762; DOI 10.1515/jpm-2017-0006.

Primary full-text reconstruction corrects an abstract-level denominator ambiguity:
- original cohort = 4,518;
- 282 excluded before screening (226 not approached for consent; 56 refused);
- **4,236 actually screened**;
- 4,109 screened >24 h;
- 127 screened <24 h;
- 3 final failures in the >24-h group;
- 6 final failures in the <24-h group;
- total final failed screens = **9**;
- no CCHD detected.

The study explicitly states that infants admitted to NICU or continuously pulse-ox monitored were ineligible. Therefore this is a well-baby/late-preterm screening cohort for primary setting purposes, despite the institution being a tertiary neonatal center.

Terminal diagnoses among the nine failures:
- AVSD x2;
- VSD x3;
- PDA x1;
- TTN x2;
- early neonatal sepsis x1.

Actionability coding:
- TTN x2 + sepsis x1 were described as requiring intensive-care follow-up -> CAN-A = 3;
- AVSD x2 are clinically relevant structural diagnoses, but only generic monitoring is reported -> CAN-U = 2;
- VSD x3 + PDA x1 have no reported size, haemodynamic consequence, specific treatment, or required follow-up -> NON_CAN = 4 under the locked incidental/minor-lesion rule;
- pediatric-cardiology referral and echocardiography alone are diagnostic ascertainment, not actionability.

Therefore:
- denominator = 9;
- Strict = 3/9;
- Expanded = 5/9;
- NON_CAN = 4/9;
- ascertainment = 100%.

The mixed early/post-24-h timing remains a heterogeneity flag but does not remove the unit from primary pooling.

**Terminal Phase 5 status:** `PRIMARY_POOLABLE / QA_COMPLETE`.

## U_R068 — Almawazini 2017, Saudi Arabia

**Primary:** Almawazini AM et al. *Effectiveness of the critical congenital heart disease screening program for early diagnosis of cardiac abnormalities in newborn infants.* Saudi Med J. 2017;38(10):1019-1024. PMID 28917066; PMCID PMC5694635; DOI 10.15537/smj.2017.10.20295.

Primary source:
- 3,300 live births;
- 197 NICU admissions;
- 3,103 observational-nursery newborns;
- 2,961 screened;
- 114 final positive screens;
- 7 cardiac lesions called critical by the paper;
- 13 severe pulmonary hypertension;
- 45 PFO without PH;
- 5 stable VSD;
- 44 large symptomatic PDA.

The seven study-defined critical cardiac lesions were:
- HLHS x2;
- TGA x1;
- pulmonary atresia x1;
- pulmonary stenosis x1;
- AV canal x1;
- truncus arteriosus x1.

Harmonized target mapping:
- HLHS x2 = definite harmonized CCHD;
- standalone TGA x1 = definite simple-TGA mapping;
- pulmonary stenosis is conditional, and the required <=28-day surgery/catheterization/death is not documented -> remains in denominator;
- AV canal and truncus are not automatically part of the locked CCHD target -> remain in denominator;
- pulmonary atresia is reported without septal anatomy. If PA/IVS, it is unconditional harmonized CCHD; if not, it is not automatically removable. This single anatomical ambiguity prevents a point denominator.

Therefore:
- harmonized CCHD = 3-4;
- harmonized denominator = 110-111.

CAN coding:
- severe PH x13 = CAN-U (serious diagnosis, but no diagnosis-specific treatment/escalation consequence reported);
- large symptomatic PDA x44 = CAN-U;
- AV canal x1 + truncus x1 + pulmonary stenosis x1 = CAN-U;
- pulmonary atresia x1 contributes an additional CAN-U only if it remains in the denominator;
- PFO x45 + stable VSD x5 = NON_CAN;
- Strict = 0 throughout the admissible mapping;
- Expanded = 60/110 or 61/111 (54.5%-55.0%).

The paper states that prostaglandin was started and urgent transfer arranged for ductus-dependent patients, but does not identify the affected individuals/lesions. That aggregate statement is not used to assign a participant-level Strict numerator among harmonized-CCHD-negative cases.

Al-Baha is retained as a high-altitude **external geographic context** flag; altitude was not reported as a study variable in the article.

**Terminal Phase 5 status:** `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY` because the denominator cannot be point-weighted without inventing PA septal anatomy.

## U_R069 — Andrews 2014, Arkansas, United States

**Primary:** Andrews JP et al. *Smooth implementation of critical congenital heart defect screening in a newborn nursery.* Clin Pediatr (Phila). 2014;53(2):173-176. PMID 24037922; DOI 10.1177/0009922813502850.

Primary source:
- 1,905 screened;
- 3 failed screens;
- ASD x2;
- PFO x1.

The authors' implementation target treated the two ASDs as true-positive structural heart disease. Under the review's harmonized target, neither ASD nor PFO is CCHD, so:
- harmonized CCHD = 0;
- denominator = 3.

Actionability:
- ASD x2 = CAN-U because the lesions are clinically relevant structural diagnoses but no specific treatment/escalation/disposition/follow-up consequence is documented;
- PFO x1 = NON_CAN;
- Strict = 0/3;
- Expanded = 2/3;
- ascertainment = 100%.

Setting QA is decisive. The study excluded newborns with prior echocardiography, death/transfer, and infants >7 days old with continuous NICU monitoring. It did **not** exclude all short intermediate/NICU stays, and the authors explicitly refer to their cohort as a `high-risk population`. The failed-screen outcomes are not separable by nursery versus higher-acuity setting.

Under the locked rule that mixed nursery/NICU cohorts are sensitivity-only unless separable, this unit cannot receive a primary weight.

**Terminal Phase 5 status:** `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

## Block-level result

Block 07 adds four structurally extracted units:

- PRIMARY_POOLABLE: 1
  - U_R049
- SENSITIVITY_ONLY: 3
  - U_R035
  - U_R068
  - U_R069
- new unresolved holds: 0

Cumulative Phase 5 state:
- structurally extracted = **27/76**;
- PRIMARY_POOLABLE = **16**;
- SENSITIVITY_ONLY = **9**;
- HOLD_PENDING_QA = **2**;
- not yet structurally extracted = **49**.

## Methodological conclusion

Block 07 validates four safeguards simultaneously:

1. historical study labels such as `critical CHD` cannot override the harmonized lesion target;
2. a conditional lesion without the required <=28-day event belongs in the harmonized-negative denominator;
3. generic monitoring/referral/echo cannot be upgraded into Strict actionability;
4. mixed/high-risk setting rules apply even when diagnostic ascertainment itself is complete.

The unresolved identity of U_R001/U_R002/U_R003/U_R006 is now a documented identity-reconciliation task and not a reason to guess or consult the legacy database.
