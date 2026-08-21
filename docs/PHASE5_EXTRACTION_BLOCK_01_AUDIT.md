# CAN-CCHD Phase 5 — Extraction Block 01 Audit

Date: 2026-08-21  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_01.csv`

## Purpose

This is the first primary-source extraction block after the Phase 4.5 freeze. It intentionally starts with units whose source material permits an explicit test of the locked distinction between **diagnosis** and **actionability**.

No value in this block came from the legacy Browser Agent/database.

## Units

### U_R017 — Jawin 2015, Malaysia

**Primary source:** Jawin V, Ang H-L, Omar A, Thong M-K. *Beyond Critical Congenital Heart Disease: Newborn Screening Using Pulse Oximetry for Neonatal Sepsis and Respiratory Diseases in a Middle-Income Country.* PLoS One. 2015;10:e0137580. PMID 26360420; PMCID PMC4567069; DOI 10.1371/journal.pone.0137580.

Primary-source extraction:
- 5,247 newborns analyzed;
- 15 final screen positives;
- 2 lesion-level CCHD cases (pulmonary atresia with VSD; pulmonary atresia + TGA + DORV);
- harmonized-CCHD-negative denominator = 13;
- 13/13 had significant noncardiac disease requiring hospitalization and treatment;
- diagnostic distribution: sepsis 2; congenital pneumonia 2; PPHN 2; meconium aspiration syndrome 2; lung hypoplasia/VACTERL 1; TTN 4;
- treatment evidence includes antibiotics, oxygen support, ventilation/iNO, partial exchange transfusion and respiratory support depending on diagnosis.

**Phase 5 terminal classification:**
- CAN-A = 13;
- Strict CAN-CCHD = 13/13;
- Expanded CAN-CCHD = 13/13;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

Incidental VSD/PFO/PDA findings in some infants are retained as overlapping lesion detail and are not double-counted as participant-level endpoints.

## U_R018 — Özalkaya 2016, Turkey

**Primary source:** Özalkaya E et al. *Early screening for critical congenital heart defects in asymptomatic newborns in Bursa province.* J Matern Fetal Neonatal Med. 2016;29:1105-1107. PMID 25902399; DOI 10.3109/14767058.2015.1035642.

Primary-source raw extraction:
- 8,208 term newborns screened;
- 7 final positives;
- authors report 6 CCHD true positives and 1 false positive with PFO;
- PFO has no qualifying management consequence in the source and maps to `NON_CAN` under the locked Protocol Core.

However, Phase 5 does **not** automatically substitute the authors' six `CCHD` labels for the harmonized review target. The individual lesions of those six screen-positive CCHD cases have not yet been fully re-mapped in this extraction pass.

**Phase 5 status:**
- raw data extracted;
- PFO = transitional/non-actionable;
- harmonized primary denominator not yet released;
- `HOLD_PENDING_MAPPING`;
- `EXTRACTED_PENDING_TARGET_QA`.

This is deliberately stricter than simply importing `study false-positive = 1` into the primary denominator.

## U_R019 — van Niekerk / POPSICLe 2016, South Africa

**Primary source:** van Niekerk AM et al. *Feasibility of Pulse Oximetry Pre-discharge Screening Implementation for detecting Critical Congenital heart Lesions in newborns in a secondary-level maternity hospital in the Western Cape, South Africa: The 'POPSICLe' study.* S Afr Med J. 2016;106(8). DOI 10.7196/SAMJ.2016.v106i8.10071.

Primary-source extraction:
- 1,001 babies screened at sea level;
- 2 final failed screens;
- 1 TGA/CCHD;
- 1 CCHD-negative infant with respiratory distress and elevated septic markers;
- that infant was admitted to NICU, received nCPAP for 3 days and IV antibiotics for 7 days; echocardiogram was normal.

**Phase 5 terminal classification:**
- harmonized-CCHD-negative denominator = 1;
- CAN-A = 1;
- Strict CAN-CCHD = 1/1;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

The normal echocardiogram is not used as a `healthy` classification because the primary source explicitly documents the noncardiac illness and treatment.

## U_R025 — Flórez-Muñoz 2021, Colombia

**Primary source:** Flórez-Muñoz SL et al. *Tamizaje con oximetría de pulso en el diagnóstico de cardiopatías congénitas críticas en recién nacidos.* Rev Colomb Cardiol. 2021;28(6):583-589. DOI 10.24875/rccar.m21000100.

Primary-source extraction:
- 438 term asymptomatic newborns;
- 4 positive screens;
- 1 TGA with associated VSD/ASD = harmonized CCHD;
- 1 moderate pulmonary hypertension;
- 2 explicitly healthy infants discharged;
- pulmonary-hypertension infant required transfer to neonatal intermediate care, supplemental oxygen, and repeat echocardiography at 24 hours.

**Phase 5 terminal classification:**
- harmonized-CCHD-negative denominator = 3;
- CAN-A = 1;
- explicitly healthy/no diagnosis = 2;
- Strict CAN-CCHD = 1/3;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

## Block-level result

Four frozen units have undergone structured Phase 5 extraction:

- **3 QA-complete and primary-poolable:** U_R017, U_R019, U_R025;
- **1 extracted but held for harmonized target mapping:** U_R018.

No imputation was performed. No diagnosis was promoted to Strict CAN-CCHD without primary-source management evidence. No `normal echo` was converted to healthy.

## Important methodological consequence for subsequent blocks

Phase 4 labels such as `sepsis`, `PPHN`, `respiratory disease` or even a working note saying `actionable` must be re-tested against the primary source during Phase 5. If the diagnosis is clinically relevant but qualifying actionability is not documented, it will be coded `CAN-U`, not Strict CAN-CCHD.

This rule will be applied prospectively to the remaining frozen units.
