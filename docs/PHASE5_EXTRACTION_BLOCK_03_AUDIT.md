# CAN-CCHD Phase 5 — Extraction Block 03 Audit

Date: 2026-08-21  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_03.csv`

## Purpose

Block 03 tests three different failure modes that could otherwise bias the primary meta-analysis:

1. a clinically actionable alternative diagnosis with explicit disposition consequence;
2. a study that reports `significant non-CCHD disease` without documenting the actionability consequence required by the locked Protocol Core;
3. a study whose reported `true-positive` target is broad CHD rather than harmonized CCHD and therefore requires lesion-level denominator remapping.

No value in this block came from the legacy Browser Agent/database.

## U_R071 — Cubells 2018, Valencia, Spain

**Primary source:** Cubells E et al. *Congenital Critical Heart Defect Screening in a Health Area of the Community of Valencia (Spain): A Prospective Observational Study.* Int J Neonatal Screen. 2018;4(1):3. PMID 33072929; PMCID PMC7548888; DOI 10.3390/ijns4010003.

Primary-source extraction:
- 8,856 newborns screened across 12 hospitals;
- 5 positive screens;
- 3 CCHD cases: total anomalous pulmonary venous return;
- 2 harmonized-CCHD-negative failed screens;
- both CCHD-negative infants had respiratory distress secondary to early-onset sepsis;
- the report states that these infants would otherwise have been discharged home, but the positive pulse-oximetry screen led to neonatal intensive care admission.

This is direct evidence of an acute change in disposition/escalation attributable to the screening pathway.

**Phase 5 terminal classification:**
- denominator = 2;
- CAN-A = 2;
- Strict CAN-CCHD = 2/2;
- Expanded CAN-CCHD = 2/2;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`;
- `QA_COMPLETE`.

## U_R072 — Diller 2018, United States

**Primary source:** Diller CL et al. *A Modified Algorithm for Critical Congenital Heart Disease Screening Using Pulse Oximetry.* Pediatrics. 2018;141(5):e20174065. PMID 29691284; DOI 10.1542/peds.2017-4065.

Primary-source extraction:
- 77,148 term newborns screened at or near 24 hours;
- 34 final failed screens under the AAP algorithm;
- 1 true-positive TAPVR;
- harmonized-CCHD-negative denominator = 33;
- 10/33 false positives had `significant non-CCHD disease`;
- the remaining 23 did not have the study's significant non-CCHD outcome.

The accessible primary text does **not** provide the individual diagnoses of those 10 infants or document specific treatment, escalation, altered disposition, or required follow-up.

Therefore the Phase 4.5 working note `exact actionable numerator 10/33` is **not inherited into Phase 5 as a Strict numerator**. Phase 5 must follow the locked actionability rule rather than a pre-extraction shorthand.

**Provisional Phase 5 classification:**
- denominator = 33;
- CAN-U = 10;
- aggregate NON_CAN = 23;
- provisional Strict CAN-CCHD = 0/33;
- Expanded CAN-CCHD = 10/33;
- ascertainment for the broad significant-disease endpoint = 100%;
- `HOLD_PENDING_ACTIONABILITY_QA`.

The 23 remaining false positives are **not** labeled healthy and are **not** presumed transitional. In matrix v0.1 they occupy the aggregate `transitional_nonactionable_n`/NON_CAN field under `PHASE5_SCHEMA_CLARIFICATION_01_NONCAN_FIELD.md`.

If full primary text later supplies qualifying management evidence, the 10 cases may be promoted to the appropriate Strict class. They must not be promoted from the word `significant` alone.

## U_R076 — Mohsin 2019, Pakistan

**Primary source:** Mohsin M et al. *Pulse Oximetry Screening for Critical Congenital Heart Disease in Newborns.* Cureus. 2019;11(6):e4808. PMID 31403007; PMCID PMC6682379; DOI 10.7759/cureus.4808.

Primary-source extraction:
- 1,650 newborns enrolled;
- population included both the Well Baby Unit and NICU, with very sick/mechanically ventilated infants excluded;
- pulse oximetry was performed at birth, 24 hours and 48 hours;
- 16 pulse-oximetry-positive infants;
- the authors use **CHD broadly** as the diagnostic target rather than the review's harmonized CCHD target;
- 8 pulse-positive infants had structural CHD and 8 had no study-defined CHD;
- among the 8 without study-defined CHD: PPHN = 6; congenital pneumonia = 2.

The article's diagnostic flow figure permits raw lesion recovery among the eight pulse-positive structural-CHD infants:
- pulse-only detections: TGA; pulmonary atresia with intact ventricular septum;
- pulse + clinical examination detections: TOF; pulmonary atresia with intact ventricular septum; DORV/VSD; ASD/CAVSD/pulmonary stenosis/PDA; CAVSD/DORV/pulmonary atresia; critical pulmonary stenosis.

This resolves the **raw lesion identities**, but it does not by itself resolve the review denominator because the exact locked harmonized CCHD lesion mapping must still be applied lesion by lesion. The article's `8 true positives` cannot simply be subtracted from 16 as if `CHD = harmonized CCHD`.

The source also does not document diagnosis-specific treatment, escalation, disposition change, or required follow-up for the 6 PPHN and 2 congenital-pneumonia cases. Generic counselling/appropriate-management wording does not satisfy the Protocol Core's specific-actionability requirement.

Finally, the mixed Well Baby Unit/NICU population is a prespecified heterogeneity concern and may require sensitivity-only handling unless the relevant subgroup can be separated.

**Phase 5 status:**
- raw screening and lesion data extracted;
- harmonized denominator = not yet frozen;
- Strict numerator = not yet frozen;
- `HOLD_PENDING_MAPPING`;
- `EXTRACTED_PENDING_TARGET_QA`.

## Block-level result

Three additional frozen units have undergone structured extraction.

Cumulative Phase 5 status after Blocks 01–03:
- structurally extracted = **11/76**;
- QA-complete `PRIMARY_POOLABLE` = **7**;
- extracted but held = **4**:
  - U_R018 — harmonized target mapping;
  - U_R024 — generic actionability wording;
  - U_R072 — `significant disease` without demonstrated management consequence;
  - U_R076 — broad CHD target / harmonized lesion mapping + mixed setting;
- not yet structurally extracted = **65**.

## Methodological conclusion

Block 03 confirms that Phase 5 must independently validate three layers for every unit:

1. **who is in the harmonized CCHD-negative denominator;**
2. **what diagnosis/outcome is present;**
3. **whether that diagnosis is demonstrably actionable.**

A study may be highly informative at one layer and still require a hold at another. This is expected and is preferable to forcing apparently complete but methodologically incompatible estimates into the primary meta-analysis.
