# CAN-CCHD Phase 5 — Extraction Block 02 Audit

Date: 2026-08-21  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_02.csv`

## Purpose

Block 02 stress-tests the locked distinction between **clinically relevant diagnosis** and **demonstrated actionability**. The central rule is prospective and binding: a diagnostic label alone does not enter Strict CAN-CCHD unless the primary source documents a qualifying treatment, escalation, disposition change, management change, or required follow-up pathway.

No value in this block came from the legacy Browser Agent/database.

## U_R009 — Riede 2010, Germany

**Primary source:** Riede FT, Wörner C, Dähnert I, Möckel A, Kostelka M, Schneider P. *Effectiveness of neonatal pulse oximetry screening for detection of critical congenital heart disease in daily clinical routine—results from a prospective multicenter study.* Eur J Pediatr. 2010;169:975-981. PMID 20195633; PMCID PMC2890074; DOI 10.1007/s00431-010-1160-4.

Primary-source extraction:
- 41,445 screened;
- 54 final positive screens;
- 14 true-positive CCHD;
- 40 CCHD-negative final failed screens;
- 15 PPHN;
- 13 sepsis;
- 12 explicitly healthy.

The report gives a complete and mutually exclusive clinical classification, but it does **not** document treatment, escalation, altered disposition, or diagnosis-specific follow-up among the 15 PPHN or 13 sepsis infants. Its discussion states that earlier recognition of illnesses such as neonatal sepsis is beneficial, but that is not participant-level actionability evidence.

**Phase 5 classification:**
- CAN-U = 28;
- Strict CAN-CCHD = 0/40;
- Expanded CAN-CCHD = 28/40;
- explicitly healthy = 12;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

This is a deliberate correction to any earlier shorthand that treated PPHN or sepsis as automatically actionable.

## U_R024 — Gopalakrishnan 2021, India

**Primary source:** Gopalakrishnan S et al. *Pulse oximetry screening to detect critical congenital heart diseases in asymptomatic neonates.* Med J Armed Forces India. 2021;77:214-219. PMCID PMC8042503; DOI 10.1016/j.mjafi.2020.01.007.

Primary-source extraction:
- 1,855 asymptomatic neonates;
- 16 final positive screens;
- 3 CCHD: TGA with intact ventricular septum x2; pulmonary atresia x1;
- harmonized-CCHD-negative denominator = 13;
- 8 early-onset sepsis/congenital pneumonia;
- 2 PPHN;
- 3 transitional circulation.

The source states that the false-positive cases with early-onset sepsis/congenital pneumonia, PPHN and transitional circulation were “managed as per standard guidelines.” This is stronger than diagnosis-only evidence, but it does not specify the treatment, escalation, disposition, or follow-up consequence for the 10 clinically relevant disease cases.

Because the locked Protocol Core requires a **specific clinically meaningful consequence**, this block does not force those 10 into Strict CAN-CCHD.

**Provisional Phase 5 classification:**
- CAN-U = 10;
- NON_CAN/transitional = 3;
- provisional Strict CAN-CCHD = 0/13;
- Expanded CAN-CCHD = 10/13;
- ascertainment = 100%;
- `HOLD_PENDING_ACTIONABILITY_QA`.

A later protocol-level QA must decide whether the generic phrase “managed as per standard guidelines” is sufficient to demonstrate actionability. Until that decision is frozen, the Strict numerator is not released.

## U_R089 — Johnson 2014, United States

**Primary source:** Johnson LC, Lieberman E, O'Leary E, Geggel RL. *Prenatal and newborn screening for critical congenital heart disease: findings from a nursery.* Pediatrics. 2014;134:916-922. PMID 25287457; DOI 10.1542/peds.2014-1461.

Primary-source extraction:
- 6,838 infants with complete pulse-oximetry data;
- 35 failed the first screen;
- 34 passed the repeat sequence;
- one infant failed all three screens;
- the sole final failed screen underwent echocardiography and had PPHN;
- no screen-positive CCHD.

Under the locked final-failed-screen rule, denominator = 1, not 35.

The accessible primary report documents PPHN and echocardiographic ascertainment but not treatment, escalation, disposition change, or diagnosis-specific follow-up. Echocardiography is the diagnostic work-up after a failed screen and is not itself sufficient actionability evidence.

**Phase 5 classification:**
- CAN-U = 1;
- Strict CAN-CCHD = 0/1;
- Expanded CAN-CCHD = 1/1;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

## U_R093 — Cawsey 2016, United Kingdom

**Primary source:** Cawsey MJ, Noble S, Cross-Sudworth F, Ewer AK. *Feasibility of pulse oximetry screening for critical congenital heart defects in homebirths.* Arch Dis Child Fetal Neonatal Ed. 2016;101:F349-F351. PMID 26915671; DOI 10.1136/archdischild-2015-309936.

Primary-source extraction:
- 90 babies underwent routine pulse-oximetry screening within two hours following homebirth;
- 2 positive screens;
- no CCHD;
- both positive-screen infants had significant respiratory illness;
- both were admitted to the neonatal unit.

The source therefore supports both a clinical diagnosis category and an acute escalation/disposition consequence.

**Phase 5 classification:**
- CAN-A = 2;
- Strict CAN-CCHD = 2/2;
- Expanded CAN-CCHD = 2/2;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`;
- retain early-screen and out-of-hospital heterogeneity flags.

## Block-level result

Four additional frozen units have undergone structured extraction:

- **3 QA-complete and primary-poolable:** U_R009, U_R089, U_R093;
- **1 fully diagnosed but held for actionability-threshold adjudication:** U_R024.

Across Blocks 01–02:
- units structurally extracted = **8/76**;
- QA-complete primary-poolable units = **6**;
- held after extraction = **2** (U_R018 target mapping; U_R024 actionability wording);
- remaining not yet extracted = **68**.

## Methodological signal

The first eight units confirm that the Phase 5 taxonomy materially changes the analysis compared with diagnosis-only summaries. Studies can be fully informative for the Expanded outcome while contributing zero events to the Strict numerator when management/actionability is not demonstrated. That behavior is intended by the pre-specified CAN-U category and must be applied consistently to the remaining 68 units.
