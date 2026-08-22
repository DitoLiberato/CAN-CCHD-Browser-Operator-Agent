# CAN-CCHD Phase 5 — Extraction Block 05 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Block: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_05.csv`

## Purpose

Block 05 deliberately tests four distinct Phase 5 problems: source-level inconsistency, incomplete ascertainment, a clean fully actionable cohort, and a report whose diagnostic categories cannot yet support a harmonized denominator. All values were extracted from restart-native or independently reverified primary sources; the legacy Browser Agent/database was not used.

## U_R033 — Abu Jarir 2026, Qatar

Primary source: Abu Jarir R et al. *Pulse Oximetry Screening for Critical Congenital Heart Disease: A Four-Year Experience in Qatar.* Cureus. 2026;18(3):e105810. PMID 41890244; PMCID PMC13014115; DOI 10.7759/cureus.105810.

The report states 68,150 live births and 34 POCC-positive infants. Its narrative/abstract describes the 34 as 8 CCHD and 26 false-positive/non-cardiac cases, with PPHN the commonest alternative diagnosis.

However, the article's Table 2 PO2 column lists d-TGA 1, Ebstein anomaly 1, HLHS 1, PPHN 28, TAPVR 1 and non-CCHD 2, which also totals 34. This representation contains only four named structural cardiac lesions and 30 PPHN/non-CCHD entries, and therefore cannot be reconciled with the narrative 8/26 split without inventing information.

Under the locked harmonized target, d-TGA and HLHS are definite CCHD. TAPVR is conditional on death or invasive intervention within 28 days, which the accessible report does not establish. Ebstein anomaly is not automatically harmonized CCHD. The additional cardiac lesions required to make the narrative count of eight are not identifiable from the table representation.

The source calls false-positive illnesses clinically significant, but does not supply diagnosis-specific treatment, escalation, altered disposition or required follow-up sufficient for Strict CAN-CCHD.

**Terminal Phase 5 status:**
- harmonized denominator: not point-identifiable;
- Strict/Expanded numerator: not frozen;
- `HOLD_PENDING_QA`;
- `EXTRACTED_HOLD_SOURCE_INCONSISTENCY`.

No arithmetic reconciliation by subtraction is permitted.

## U_R039 — Bradshaw 2012, United States

Primary source: Bradshaw EA et al. *Feasibility of implementing pulse oximetry screening for congenital heart disease in a community hospital.* J Perinatol. 2012;32:710-715. PMID 22282131; PMCID PMC3432220; DOI 10.1038/jp.2011.179.

Among 6,745 screened well-baby nursery infants, 9 failed the screening pathway. The authors historically label one case — anomalous drainage of the SVC to the left atrium — as CCHD. This lesion is not one of the locked harmonized target lesions, and the report does not establish a reproducible duct-dependent/first-28-day invasive-intervention equivalence. Therefore it cannot simply be removed from the review denominator because the source called it CCHD.

The harmonized CCHD count is consequently 0 and the harmonized-CCHD-negative failed-screen denominator is 9.

Clinical classification:
- anomalous SVC-to-left-atrium with NICU transfer: CAN-A = 1;
- mirror-image dextrocardia with lobar pneumonia and NICU transfer: CAN-A = 1;
- dilated ascending aorta with diagnostic cardiology evaluation but no qualifying management consequence: CAN-U = 1;
- PFO and PFO-versus-small-ASD: NON_CAN = 2;
- one evaluated no-CHD infant without adequate noncardiac outcome ascertainment: UNKNOWN = 1;
- three positive screens with no further testing/consultation: UNKNOWN = 3.

Thus:
- Strict = 2/9;
- Expanded = 3/9;
- NON_CAN = 2/9;
- UNKNOWN = 4/9;
- sufficiently classified = 5/9 = 55.6%.

This is below the locked >=90% threshold. The unit is therefore `SENSITIVITY_ONLY`, not primary-poolable. Importantly, the echo/no-CHD infant is not relabeled healthy.

## U_R100 — Cloete 2020, New Zealand

Primary source: Cloete E et al. *Pulse oximetry screening in a midwifery-led maternity setting with high antenatal detection of congenital heart disease.* Acta Paediatr. 2020;109:100-108. PMID 31298757; PMCID PMC6972617; DOI 10.1111/apa.14934.

This is a particularly clean unit because the study itself defines a critical congenital cardiac defect by cardiac intervention and/or cardiac-related death within the first 28 days, matching the locked harmonized target.

Among 16,644 screened newborns, 48 failed:
- 3 harmonized CCHD;
- 45 harmonized-CCHD-negative failed screens.

The 45 comprise:
- PPHN 3;
- respiratory pathology 27 — pneumonia 13, TTN 8, meconium exposure 4, pneumothorax 1, ongoing unexplained oxygen requirement 1;
- sepsis 3;
- supraventricular tachycardia 1;
- no identifiable pathology/slow birth transition 11.

All 34 CCHD-negative infants with identified pathology were admitted to a newborn unit as a consequence of the failed screen. This is direct acute disposition/escalation evidence and supports CAN-A = 34. The other 11 were explicitly reported as having no identified pathology/slow transition and are not promoted to CAN merely because four underwent short observation admissions.

**Terminal classification:**
- denominator = 45;
- CAN-A = 34;
- Strict = 34/45;
- Expanded = 34/45;
- explicit no-pathology/slow-transition = 11/45;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`;
- `QA_COMPLETE`.

Early screening timing remains a heterogeneity flag.

## U_R102 — Sero 2025, Turkey

Primary source: Sero L, Tuncel D, Akdeniz O, Okur N. *What is the role of pulse oximetry screening in identifying neonatal morbidities other than critical heart diseases?* Klin Padiatr. 2025. PMID 41101352; DOI 10.1055/a-2695-8865.

The accessible primary abstract reports 29,840 documented POS results and 301 positive screens. It reports 23 infants jointly as `CCHD and significant congenital heart disease`, without separating harmonized CCHD from broader cardiac disease. It also names sepsis 101, congenital pneumonia 16, polycythaemia 32 and TTN 52.

Three problems prevent quantitative harmonization:
1. the 23 cardiac cases are not lesion-separated;
2. mutual exclusivity of the noncardiac categories is not established;
3. the listed noncardiac diagnoses are introduced as examples and are not demonstrated to be exhaustive.

Therefore the apparent remainder of 77 infants must **not** be generated by subtraction. The accessible abstract also provides diagnoses rather than specific treatment/escalation/disposition/follow-up evidence, so it cannot supply a Strict numerator.

The full article was not accessible in the current retrieval pass. The Phase 4.5 mutual-exclusivity hold therefore remains active and is strengthened by the unresolved target mapping.

**Terminal current status:**
- denominator: not point-identifiable;
- Strict/Expanded numerator: not frozen;
- `HOLD_PENDING_QA`;
- `EXTRACTED_HOLD_PENDING_FULLTEXT_QA`.

## Block-level QA result

Block 05 adds four structurally extracted units:
- U_R100 -> `PRIMARY_POOLABLE`;
- U_R039 -> `SENSITIVITY_ONLY` because ascertainment is 55.6%;
- U_R033 -> `HOLD_PENDING_QA` because the primary source is internally inconsistent;
- U_R102 -> `HOLD_PENDING_QA` because target mapping, category exclusivity and outcome exhaustiveness remain unresolved.

Cumulative Phase 5 state after Block 05:
- structurally extracted = **19/76**;
- `PRIMARY_POOLABLE` = **14**;
- `SENSITIVITY_ONLY` = **3**;
- unresolved extracted holds = **2**;
- not yet structurally extracted = **57**.

## Methodological lesson

Block 05 confirms that the >=90% rule, harmonized target definition and no-forced-reconciliation rule are doing distinct jobs. A study can have an apparently simple published false-positive count and still be unusable for a point estimate if the lesion target or participant outcomes are not reproducibly identifiable. Conversely, a high-yield unit such as Cloete can enter the primary analysis because denominator, terminal classification and management consequence all align cleanly.
