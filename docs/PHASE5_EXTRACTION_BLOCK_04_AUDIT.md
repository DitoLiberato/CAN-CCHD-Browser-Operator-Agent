# CAN-CCHD Phase 5 — Extraction Block 04 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_04.csv`

## Purpose

Block 04 applies the stabilized Phase 5 rules to four high-information cohorts with different evidence patterns:

- a large community/home-birth implementation cohort with aggregate treatment/referral evidence (POLAR);
- a well-baby cohort with complete diagnoses but an irreducible harmonized-target interval (Morocco);
- a complete diagnostic cohort lacking specific management evidence (Oakley);
- a high-altitude cohort with detailed participant-level management (Tekleab).

No scientific value was imported from the legacy Browser Agent/database.

---

## U_R020 — Narayen / POLAR 2018, Netherlands

**Primary source:** Narayen IC et al. *Accuracy of Pulse Oximetry Screening for Critical Congenital Heart Defects after Home Birth and Early Postnatal Discharge.* J Pediatr. 2018;197:29-35.e1. PMID 29580679; DOI 10.1016/j.jpeds.2018.01.039.

**Supporting same-cohort author summary:** Narayen IC, Blom NA, te Pas AB. *Pulse Oximetry Screening Adapted to a System with Home Births: The Dutch Experience.* Int J Neonatal Screen. 2018;4:11. PMCID PMC7510226.

Primary facts:
- 23,959 newborns screened after exclusion of prenatally diagnosed and immediately symptomatic CCHD;
- screening at >=1 h and again on day 2 or 3;
- 5 pulse-oximetry-detected CCHD;
- 221 CCHD false-positive final screens;
- primary paper reports 134 infants with significant alternative pathology and explicitly states that detection led to early recognition and referral for treatment.

The same-cohort author summary decomposes all 221 CCHD-negative final failed screens:
- respiratory pathology = 88;
- infection/sepsis = 31;
- non-critical CHD = 3;
- other pathology = 12;
- healthy = 87.

These sum exactly to 221. The disease categories sum to 134.

### CAN-CCHD coding

The primary report links the **noncardiac disease groups** to early recognition and referral for treatment. Therefore:

- respiratory 88 + infection/sepsis 31 + other pathology 12 = **131 CAN-AB**;
- non-critical CHD 3 = **CAN-U**, because the subgroup is clinically significant but no concrete treatment/follow-up consequence is reported for those three infants;
- healthy = 87.

Thus:
- Strict CAN-CCHD = **131/221**;
- Expanded CAN-CCHD = **134/221**;
- explicitly healthy = **87/221**;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

The same-cohort author review is used only to decompose the already established 221-infant primary cohort and does not create independent weight.

---

## U_R023 — El Idrissi Slitine 2020, Morocco

**Primary source:** El Idrissi Slitine N et al. *Pulse Oximetry and Congenital Heart Disease Screening: Results of the First Pilot Study in Morocco.* Int J Neonatal Screen. 2020;6(3):53. PMID 33123634; PMCID PMC7570348; DOI 10.3390/ijns6030053.

Primary facts:
- 8,013 asymptomatic newborns screened;
- 15 final failed screens;
- study-defined groups: 5 CCHD, 5 non-critical CHD, 5 false positives.

### Raw lesion/outcome detail

Study-defined CCHD:
- D-TGA 1 — operated with good result;
- DORV + TGA + pulmonary stenosis 1 — stable, waiting for surgery;
- coarctation + PDA 1 — waiting for surgery;
- HLHS 2 — died.

Non-critical CHD:
- single atrium 1 — stable, waiting for surgery;
- hypertrophic myocardium 2 — outcome `normal heart`;
- large ASD 1 — stable, waiting for surgery;
- AV canal 1 — stable, waiting for surgery.

Other CCHD-negative outcomes:
- PPHN 1 — outcome `normal`;
- sepsis 2 — recovered; article states both were diagnosed and treated early;
- normal findings 2.

### Harmonized-target problem

Under `PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`:
- D-TGA = definite harmonized CCHD;
- HLHS x2 = definite harmonized CCHD;
- DORV+TGA+PS is not simple TGA and cannot be promoted automatically;
- coarctation is conditional and requires death or surgery/catheterization within 28 days;
- the article does not establish the required <=28-day intervention timing for the two uncertain cases.

Therefore:
- definite harmonized CCHD = 3;
- possible harmonized CCHD = 3-5;
- harmonized-CCHD-negative denominator = **10-12**.

No timing is inferred from lesion severity or from the phrase `waiting for surgery`.

### CAN-CCHD coding across the admissible denominator interval

Fixed CCHD-negative cases:
- sepsis treated early = CAN-A 2;
- single atrium + large ASD + AV canal with planned surgery = CAN-B 3;
- PPHN without a specific documented treatment consequence = CAN-U 1;
- hypertrophic-myocardium findings resolving to `normal heart` = NON_CAN 2;
- normal findings = explicitly healthy/no diagnosis 2.

If either/both of the two target-uncertain cardiac cases remain in the harmonized-CCHD-negative denominator, they are CAN-B because the source documents a planned surgical pathway.

Therefore:
- denominator = **10-12**;
- Strict CAN-CCHD = **5-7**;
- Expanded CAN-CCHD = **6-8**;
- Strict proportion range = **50.0%-58.3%**;
- Expanded proportion range = **60.0%-66.7%**.

Because a unique primary meta-analysis weight cannot be assigned without inventing 28-day timing, terminal status is:

`SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

This is a resolved bounded estimate, not an unresolved hold.

---

## U_R043 — Oakley 2015, United Kingdom

**Primary source:** Oakley JL, Soni NB, Wilson D, Sen S. *Effectiveness of pulse-oximetry in addition to routine neonatal examination in detection of congenital heart disease in asymptomatic newborns.* J Matern Fetal Neonatal Med. 2015;28(14):1736-1739. PMID 25241768; DOI 10.3109/14767058.2014.967674.

**Harmonized-target validation:** Plana MN et al. Cochrane Database Syst Rev. 2018;CD011912. PMID 29494750.

Primary facts:
- 6,329 newborns screened;
- mean screening age 28 h, range 6-72 h;
- 14 final failed screens;
- Cochrane extraction under the pre-specified harmonized target confirms TP=7 and FP=7;
- among 7 harmonized-CCHD-negative final failed screens: 3 non-critical but significant CHD and 4 respiratory illness/sepsis;
- all low-saturation infants had identifiable pathology.

The accessible primary report does **not** specify treatment, escalation, altered disposition, or required follow-up for these seven infants.

Therefore:
- CAN-U = 7;
- Strict CAN-CCHD = **0/7**;
- Expanded CAN-CCHD = **7/7**;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

The words `significant` and `unwell` are not substituted for the locked specific-actionability requirement.

---

## U_R099 — Tekleab 2019, Ethiopia

**Primary source:** Tekleab AM, Sewnet YC. *Role of pulse oximetry in detecting critical congenital heart disease among newborns delivered at a high altitude setting in Ethiopia.* Pediatr Health Med Ther. 2019;10:83-88. PMID 31616201; PMCID PMC6699584; DOI 10.2147/PHMT.S217987.

Primary facts:
- 941 apparently healthy term newborns;
- Addis Ababa altitude approximately 2,600 m;
- median screening age 8 h; 67.3% screened <24 h;
- 56 persistent final failed screens;
- all 56 received echocardiography;
- no CCHD detected.

Diagnostic distribution:
- PPHN = 10, including 2 later diagnosed with sepsis;
- PDA = 11;
- ASD = 2;
- no echocardiographic abnormality = 33.

### Participant-level actionability

PPHN:
- all 10 admitted to NICU;
- all treated according to hospital guideline;
- 2 also had sepsis and were managed accordingly;
- PPHN resolved.

These 10 are **CAN-A**. Sepsis is an etiologic overlap and does not create extra participants.

PDA/ASD:
- other causes of hypoxemia were ruled out;
- the 13 infants were monitored until SpO2 normalized;
- they were discharged with explicit advice for follow-up.

Under the locked rule that ordinarily minor lesions may become actionable when qualifying management/follow-up is documented, these 13 are **CAN-B**.

Echo-negative group:
- all 33 were carefully re-evaluated by a pediatrician;
- all had unremarkable clinical findings;
- SpO2 normalized;
- they were sent home with advice.

This affirmative clinical reassessment supports `explicitly_healthy_no_diagnosis = 33` rather than merely `normal echo`.

Therefore:
- denominator = 56;
- CAN-A = 10;
- CAN-B = 13;
- Strict CAN-CCHD = **23/56**;
- Expanded CAN-CCHD = **23/56**;
- explicitly healthy/no diagnosis = 33;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`.

High altitude and predominantly <24-h timing remain mandatory subgroup/heterogeneity flags.

---

## Block-level result

Four additional frozen units were structurally extracted.

### Block 04 disposition

`PRIMARY_POOLABLE`:
- U_R020 POLAR
- U_R043 Oakley
- U_R099 Tekleab

`SENSITIVITY_ONLY`:
- U_R023 Morocco

Unresolved holds created by this block: **0**.

## Cumulative Phase 5 state after Block 04

- frozen units = **76**;
- structurally extracted = **15/76**;
- `PRIMARY_POOLABLE` = **13**;
- `SENSITIVITY_ONLY` = **2** (U_R076 Mohsin + U_R023 Morocco);
- unresolved holds among extracted units = **0**;
- not yet structurally extracted = **61**.

## Methodological signal

Block 04 confirms three important properties of the locked taxonomy:

1. an aggregate consequence such as referral for treatment can support Strict CAN-CCHD when the affected subgroup is numerically identifiable;
2. clinically important disease without documented management remains CAN-U rather than being discarded;
3. traditionally minor cardiac lesions can enter CAN-B when the primary source documents a real monitoring/follow-up pathway attributable to the finding.

None of these rules alters Phase 4.5 study membership; they only determine the downstream quantitative endpoint and poolability.
