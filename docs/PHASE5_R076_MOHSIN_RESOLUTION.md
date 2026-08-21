# CAN-CCHD Phase 5 — Terminal Resolution of U_R076 / Mohsin 2019

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **RESOLVED — SENSITIVITY ONLY / NO PRIMARY META-ANALYSIS WEIGHT**

## Primary report

Mohsin M, Humayun KN, Atiq M. *Clinical Screening for Congenital Heart Disease in Newborns at a Tertiary Care Hospital of a Developing Country.* Cureus. 2019;11(6):e4808. PMID 31403007; PMCID PMC6682379; DOI 10.7759/cureus.4808.

## 1. Why the unit was held

Mohsin enrolled an inseparable mixture of newborns from the **Well Baby Unit and NICU** and used **congenital heart disease broadly** as the target rather than the review's harmonized CCHD definition.

Among 1,650 newborns:
- 16 had a final positive pulse-oximetry screen;
- 8 had study-defined structural CHD;
- 8 had no study-defined CHD: PPHN n=6 and congenital pneumonia n=2.

The article does not report lesion-specific surgery, catheter intervention, or death within 28 days. Therefore conditional lesions cannot be promoted to harmonized CCHD by assumption.

## 2. Raw pulse-positive structural lesions recovered

The article's diagnostic flow figure gives the eight pulse-positive structural-CHD infants:

1. TGA
2. pulmonary atresia with intact ventricular septum (PA/IVS)
3. TOF
4. PA/IVS
5. DORV/VSD
6. ASD/CAVSD/pulmonary stenosis/PDA
7. CAVSD/DORV/pulmonary atresia
8. critical pulmonary stenosis

The remaining eight pulse-positive infants were:
- PPHN n=6;
- congenital pneumonia n=2.

## 3. Application of the locked harmonized CCHD definition

Under `PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`:

### Definite harmonized CCHD

- PA/IVS x2 = unconditional harmonized CCHD.

### Not automatically harmonized CCHD

- DORV/VSD = not listed as an automatic CCHD lesion and no equivalence/early-intervention evidence is provided.

### Potential/conditional but unresolved

- TGA is reported simply as `TGA`; the report does not explicitly establish the review's `simple TGA` anatomical criterion.
- TOF requires death or surgery/catheterization within 28 days; not reported.
- pulmonary stenosis in the ASD/CAVSD/PS/PDA combination requires qualifying 28-day outcome; not reported.
- pulmonary atresia in the CAVSD/DORV/PA combination has non-intact septal anatomy and therefore follows the conditional PA/VSD-type rule; qualifying 28-day outcome not reported.
- critical pulmonary stenosis remains a conditional pulmonary-valve-stenosis lesion despite the adjective `critical`; qualifying 28-day outcome not reported.

No parallel report or institutional version was found with additional 28-day outcome data. The Aga Khan repository reproduces the same article.

## 4. Harmonized denominator bounds

With 16 final positive pulse-oximetry screens:

- minimum definite harmonized CCHD = 2 (PA/IVS x2);
- maximum plausible harmonized CCHD under the reported anatomy = 7 if TGA and all four conditional lesions meet the missing qualifying criteria;
- therefore the harmonized-CCHD-negative denominator is **bounded from 9 to 14**.

A single harmonized denominator is not point-identifiable from the report.

This uncertainty affects meta-analysis precision/weight and must not be replaced by an invented value.

## 5. CAN-CCHD consequences

### Strict CAN-CCHD

The article does not document a specific treatment, escalation, altered disposition, or required diagnosis-specific follow-up for the PPHN, congenital-pneumonia, or structural non-CCHD cases. It states only that abnormalities were recorded and parents were counseled regarding appropriate management.

Therefore:

> **Strict CAN-CCHD = 0 across all admissible harmonized denominator mappings.**

### Expanded CAN-CCHD

Every infant who can remain in the harmonized-CCHD-negative denominator has a clinically relevant diagnosis:
- PPHN;
- congenital pneumonia; or
- structural CHD not demonstrated to meet the locked CCHD target.

Therefore:

> **Expanded CAN-CCHD = 100% across the full harmonized denominator range 9–14.**

The exact event count/denominator pair varies with lesion mapping, so no harmonized meta-analysis weight is assigned.

## 6. Study-defined sensitivity representation

For a transparent study-defined sensitivity analysis only:

- study-defined non-CHD false-positive denominator = 8;
- PPHN = 6;
- congenital pneumonia = 2;
- Strict CAN-CCHD = 0/8;
- Expanded CAN-CCHD = 8/8.

This representation must be labeled **study-defined target**, not harmonized primary denominator.

## 7. Poolability decision

Independent of the target-mapping uncertainty, Mohsin is not eligible for the principal well-baby meta-analysis because the source mixes **Well Baby Unit + NICU** and does not provide separable outcome data.

Binding Phase 5 status:

- `entry_hold_flag = NO`
- `poolability_status = SENSITIVITY_ONLY`
- `qa_status = QA_COMPLETE_SENSITIVITY_ONLY`
- no primary meta-analysis weight
- no further Mohsin-specific hold required

## 8. Final resolution

**U_R076 is no longer a Phase 5 blocker.**

The unit is fully resolved for the purposes of this review:
- raw diagnoses preserved;
- harmonized denominator uncertainty bounded rather than imputed;
- Strict and Expanded directional results characterized;
- mixed-setting limitation enforced;
- retained for sensitivity/context only.
