# CAN-CCHD Phase 5 — Extraction Block 08 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_08.csv`

## Purpose

Block 08 applies the locked Phase 5 rules to four restart-native units with different limitations: a persistent early false-positive with normal echocardiography, a low-risk nursery study dominated by PFO, a lesion-mapping/missingness case from Panama, and a statewide mixed-setting implementation cohort with participant-level plus aggregate outcome data.

No scientific value was imported from the legacy Browser Agent/database.

## U_R007 — Sendelbach 2008, Dallas, United States

**Primary source:** Sendelbach DM et al. *Pulse oximetry screening at 4 hours of age to detect critical congenital heart defects.* Pediatrics. 2008;122(4):e815-e820. PMID 18762486; DOI 10.1542/peds.2008-0781.

Primary extraction:
- 15,233 stable newborn-nursery infants were screened at 4 hours;
- infants admitted to NICU or with respiratory distress/cyanosis before 4 hours were excluded;
- 859 had SpO2 <96% initially;
- 768 were rescreened before discharge and 767 normalized;
- only one infant remained persistently <96% and underwent echocardiography;
- the echocardiogram was normal;
- no alternative noncardiac diagnosis or management consequence was reported.

The locked analytic unit is the **final failed screen**, not an initial low reading. Therefore 859 is not the denominator. The eligible denominator is one.

A normal echocardiogram excludes structural cardiac findings at that assessment but does not establish that the infant was clinically healthy or identify the cause of persistent hypoxemia. The single case is therefore `UNKNOWN`, not `healthy` and not `NON_CAN`.

**Terminal Phase 5 classification:**
- harmonized CCHD = 0;
- denominator = 1;
- Strict = 0/1;
- Expanded = 0/1;
- UNKNOWN = 1;
- terminal clinical ascertainment = 0/1 = 0%;
- `SENSITIVITY_ONLY`;
- `QA_COMPLETE_SENSITIVITY_ONLY`.

This unit also retains a very-early-screening flag (4 hours).

## U_R015 — Zuppa 2015, Rome, Italy

**Primary source:** Zuppa AA et al. *Clinical examination and pulse oximetry as screening for congenital heart disease in low-risk newborn.* J Matern Fetal Neonatal Med. 2015;28(1):7-11. PMID 24588079; DOI 10.3109/14767058.2014.899573.

Primary extraction:
- 5,750 asymptomatic low-risk nursery newborns;
- screening at 48–72 hours;
- three pulse-oximetry-positive infants;
- all three had negative cardiovascular physical examinations;
- echocardiography found PFO in two and no structural CHD in the third;
- no screen-positive CCHD was identified.

The primary report does **not** support the historical secondary interpretation that all three false positives had PPHN. That interpretation remains rejected.

Coding:
- PFO x2 = `NON_CAN` because no qualifying clinical consequence is documented;
- the third infant has a structurally normal echocardiogram but no noncardiac clinical outcome = `UNKNOWN`.

**Terminal Phase 5 classification:**
- denominator = 3;
- Strict = 0/3;
- Expanded = 0/3;
- NON_CAN = 2;
- UNKNOWN = 1;
- ascertainment = 2/3 = 66.7%;
- `SENSITIVITY_ONLY`.

## U_R021 — Miranda Peralta, Panama

**Primary source:** Miranda Peralta AL. *Tamizaje de cardiopatías congénitas en el neonato mediante oximetría de pulso en el Hospital Materno Infantil José Domingo de Obaldía. Agosto 2014-febrero 2015.* Pediatr Panamá. 2018;47(1):13-19. DOI 10.37980/im.journal.rspp.20181608.

Source-level QA:
- abstract reports 2,236 screened; discussion gives 2,235;
- eligibility language describes screening at 24–48 hours, whereas results state 86.6% were screened within the first 24 hours;
- these discrepancies are preserved rather than silently harmonized.

Final failed screens = 16.

Reported echocardiographic/clinical findings:
- six structurally normal hearts;
- six PDA with hemodynamic repercussion;
- three anomalous pulmonary venous connections;
- one complex right-heart lesion described as hypoplastic RV + hypoplastic tricuspid valve + pulmonary atresia **versus** critical domed pulmonary stenosis, with a large tortuous PDA and suspected ventriculo-coronary fistulas.

### Harmonized target mapping

The complex lesion cannot be forced into a single anatomy:
- if it represents PA/IVS, it is unconditional harmonized CCHD -> denominator = 15;
- if it represents critical pulmonary stenosis, the source does not document death or surgery/catheterization within 28 days -> it remains harmonized-CCHD-negative -> denominator = 16.

The three anomalous pulmonary venous connections are not specified as total anomalous return and lack the locked 28-day qualifying outcome; they remain in the harmonized-negative denominator.

### Actionability

The source specifies that two of the six hemodynamically significant PDA cases required medical closure. These are `CAN-A=2`.

The remaining four PDA cases had hemodynamic repercussion but lack a specific qualifying management consequence in the report -> `CAN-U=4`.

The three anomalous pulmonary venous connections are clinically relevant structural diagnoses but lack qualifying actionability -> `CAN-U=3`.

If the complex lesion remains in the denominator, it adds one further `CAN-U` case.

The six structurally normal echoes do not establish noncardiac health -> `UNKNOWN=6`.

**Bounded terminal classification:**
- scenario PA/IVS: denominator 15; Strict 2/15; Expanded 9/15; UNKNOWN 6; ascertainment 60.0%;
- scenario critical PS retained: denominator 16; Strict 2/16; Expanded 10/16; UNKNOWN 6; ascertainment 62.5%.

Because both harmonized target membership and ascertainment prevent a defensible principal weight, the unit is `SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY`.

## U_R086 — Garg 2013, New Jersey statewide program

**Primary source:** Garg LF et al. *Results From the New Jersey Statewide Critical Congenital Heart Defects Screening Program.* Pediatrics. 2013;132(2):e314-e323. PMID 23858425; PMCID PMC4471476; DOI 10.1542/peds.2013-0269.

Program facts:
- 75,324 live births during the implementation period;
- 73,320 were eligible for screening;
- 99.1% of eligible newborns were screened;
- the exact integer screened count is not reconstructed by multiplying these rounded values;
- the statewide program included WBN and NICU/special-care nursery locations;
- 49 failed screens were reported.

The report provides unusually detailed information for 30/49 failed screens whose diagnostic evaluation was attributable solely to the pulse-oximetry failure, while the remaining 19 already had clinical indicators that independently justified evaluation.

### Harmonized CCHD mapping

The authors classified seven failed-screen infants as CCHD. Under the locked lesion target, only two are definite harmonized CCHD from the reported information:
- HLHS;
- interrupted aortic arch.

Five author-CCHD cases remain in the harmonized-negative denominator:
- d-TGA: not assumed to be `simple TGA` without explicit anatomy;
- another TGA: same rule;
- coarctation: no documented <=28-day death/surgery/catheterization;
- TAPVR: no documented <=28-day qualifying event;
- tricuspid atresia: not an unconditional lesion in the locked target.

Thus:
- harmonized CCHD = 2;
- harmonized-CCHD-negative denominator = 47.

### Actionability and missingness

Among the 30 screen-attributable evaluations:
- the reclassified d-TGA, tricuspid-atresia and coarctation cases were transferred out after screening -> `CAN-A=3`;
- seven specifically described alternative diagnoses/findings are clinically relevant but lack sufficiently specific qualifying management evidence -> `CAN-U=7`;
- ten specifically described minor/resolved findings are `NON_CAN=10`;
- ten had no identified diagnosis.

Among the 19 infants with prior clinical indicators:
- reclassified TGA and TAPVR are clinically relevant but screening did not create the already-indicated management pathway -> `CAN-U=2`;
- 13 remaining cases are reported only in a broad aggregate of other CHD/echo findings/noncardiac diagnoses, insufficient to distinguish CAN-U from NON_CAN -> `UNKNOWN=13`;
- two had no identified diagnosis.

The 12 explicit no-diagnosis infants are preserved as such; they are not used to infer a specific etiology.

Reconciliation of the 47 denominator infants:
- CAN-A = 3;
- CAN-U = 9;
- NON_CAN = 10;
- explicit no diagnosis = 12;
- UNKNOWN = 13;
- total = 47.

**Terminal Phase 5 classification:**
- Strict = 3/47;
- Expanded = 12/47;
- ascertainment = 34/47 = 72.3%;
- `SENSITIVITY_ONLY` because ascertainment is below 90% **and** the WBN/NICU/SCN population is not separable;
- `QA_COMPLETE_SENSITIVITY_ONLY`.

## Block-level result

Four additional frozen units have undergone structured extraction.

Block 08 disposition:
- PRIMARY_POOLABLE = 0;
- SENSITIVITY_ONLY = 4;
- new unresolved holds = 0.

Cumulative Phase 5 state after Blocks 01–08:
- structurally extracted = **31/76**;
- PRIMARY_POOLABLE = **16**;
- SENSITIVITY_ONLY = **13**;
- HOLD_PENDING_QA = **2**;
- not yet extracted = **45**.

## Methodological conclusion

Block 08 reinforces four safeguards:

1. an initial abnormal pulse-oximetry reading that normalizes on protocol repeat is not a failed-screen denominator event;
2. normal echocardiography is not equivalent to healthy/noncardiac ascertainment;
3. source labels such as `CCHD` do not override the lesion-level harmonized target;
4. rich implementation data can remain sensitivity-only when setting mixing or terminal CAN classification falls below the locked >=90% threshold.
