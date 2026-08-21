# CAN-CCHD Phase 5 — Extraction Block 03 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_03.csv`

## Purpose

Block 03 tests three different failure modes that could otherwise bias the primary meta-analysis:

1. a clinically actionable alternative diagnosis with explicit disposition consequence;
2. a study that reports clinically significant non-CCHD disease without documenting the actionability consequence required by the locked Protocol Core;
3. a study whose target is broad CHD rather than harmonized CCHD and whose population mixes Well Baby Unit and NICU.

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

**Terminal Phase 5 classification:**
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
- 77,148 term newborns screened;
- 34 final failed screens;
- 1 true-positive TAPVR;
- harmonized-CCHD-negative denominator = 33;
- 10/33 false positives had significant non-CCHD disease;
- the remaining 23 did not have the study's significant non-CCHD outcome.

The accessible primary text does not document specific treatment, escalation, altered disposition, or required follow-up for those 10 infants. Under the locked Protocol Core, lack of actionability evidence is handled by `CAN-U`, not by a study-level hold.

**Terminal Phase 5 classification:**
- denominator = 33;
- CAN-U = 10;
- aggregate NON_CAN = 23;
- Strict CAN-CCHD = 0/33;
- Expanded CAN-CCHD = 10/33;
- `PRIMARY_POOLABLE`;
- `QA_COMPLETE`.

The 23 are not relabeled as healthy or transitional; they remain the study-defined aggregate remainder without significant non-CCHD disease.

## U_R076 — Mohsin 2019, Pakistan

**Primary source:** Mohsin M et al. *Clinical Screening for Congenital Heart Disease in Newborns at a Tertiary Care Hospital of a Developing Country.* Cureus. 2019;11(6):e4808. PMID 31403007; PMCID PMC6682379; DOI 10.7759/cureus.4808.

Primary-source extraction:
- 1,650 newborns;
- inseparable mixture of Well Baby Unit and NICU;
- 16 final pulse-positive infants;
- study target = CHD broadly, not harmonized CCHD;
- 8 pulse-positive structural-CHD infants;
- 8 study-defined non-CHD false positives: PPHN n=6, congenital pneumonia n=2.

Raw pulse-positive structural lesions recovered from the diagnostic flow figure:
1. TGA;
2. PA/IVS;
3. TOF;
4. PA/IVS;
5. DORV/VSD;
6. ASD/CAVSD/pulmonary stenosis/PDA;
7. CAVSD/DORV/pulmonary atresia;
8. critical pulmonary stenosis.

### Harmonized CCHD mapping

Under the locked Phase 0.4/Cochrane target:
- PA/IVS x2 = definite harmonized CCHD;
- DORV/VSD is not automatically harmonized CCHD;
- TGA is not explicitly characterized as `simple`;
- TOF, pulmonary stenosis, PA with non-intact septal anatomy, and critical pulmonary stenosis require death or surgery/catheterization within 28 days;
- the article reports none of those qualifying 28-day outcomes.

No parallel report or Aga Khan institutional version provides the missing timing.

Therefore the harmonized CCHD-negative denominator is not point-identifiable but is bounded:

> **9 to 14**

### CAN-CCHD mapping

The article does not document specific treatment, escalation, disposition change, or required diagnosis-specific follow-up for the PPHN, pneumonia, or structural non-CCHD cases. Generic counselling regarding appropriate management is insufficient for Strict actionability.

Accordingly:
- Strict CAN-CCHD = **0% across every admissible denominator mapping**;
- Expanded CAN-CCHD = **100% across every admissible denominator mapping**, because every infant remaining in the denominator has a clinically relevant diagnosis.

For a study-defined sensitivity representation only:
- denominator = 8;
- PPHN 6 + pneumonia 2;
- Strict = 0/8;
- Expanded = 8/8.

### Poolability

Mohsin is excluded from the principal well-baby meta-analysis independently of the denominator uncertainty because Well Baby Unit and NICU outcomes are not separable.

**Terminal Phase 5 classification:**
- `entry_hold_flag = NO`;
- `poolability_status = SENSITIVITY_ONLY`;
- `qa_status = QA_COMPLETE_SENSITIVITY_ONLY`;
- no primary meta-analysis weight;
- no remaining Mohsin-specific hold.

Detailed resolution: `docs/PHASE5_R076_MOHSIN_RESOLUTION.md`.

## Block-level result

After final QA of Blocks 01–03:
- structurally extracted = **11/76**;
- QA-complete `PRIMARY_POOLABLE` = **10**;
- `SENSITIVITY_ONLY` = **1** (U_R076);
- unresolved holds among extracted units = **0**;
- not yet structurally extracted = **65**.

## Methodological conclusion

Block 03 confirms that Phase 5 must validate three independent layers:

1. who belongs in the harmonized CCHD-negative denominator;
2. what diagnosis/outcome is present;
3. whether that diagnosis is demonstrably actionable.

When a point denominator cannot be recovered and the study is already excluded from the principal population because of inseparable mixed setting, interval mapping plus sensitivity-only retention is preferable to inventing a value or leaving the entire extraction pipeline blocked.
