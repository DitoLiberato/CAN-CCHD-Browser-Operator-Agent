# CAN-CCHD Phase 4.5 — Strict QA of Borderline Primary Reports, Set 2

Date: 2026-08-21
Status: TERMINAL QA / CORRECTIVE

Governance: `01_RESEARCH_PLAN_AND_PROTOCOL.md` + `RESTART_LEGACY_DATA_FIREWALL.md` + strict criterion 6.

## R007 — Sendelbach 2008 — INCLUDE retained / outcome-limited

- 15,233 stable newborn-nursery infants screened at 4 h.
- 859 had SpO2 <96% at the first screen; 768 were rescreened before discharge and 767 normalized.
- One infant remained persistently <96% and underwent echocardiography; echocardiography was normal.
- No CCHD was detected by the screening pathway.

**CAN-CCHD coding:** final CCHD-negative failed-screen denominator = 1. Actionable CAN-CCHD = 0 on available evidence. The infant is `echo-normal / alternative diagnosis not ascertained`, **not explicitly healthy**.

**Decision:** INCLUDE. Relevant failed-screen outcome exists (normal cardiac evaluation), but retain `outcome-limited / diagnosis-not-ascertained-beyond-echo` flag.

## R035 — Hoke 2002 — INCLUDE retained / partial ascertainment

- 2,876 well-baby nursery newborns screened.
- 57 abnormal screening tests; 4 target CCHD true positives, leaving 53 conventional CCHD false positives.
- Later detailed evidence synthesis of the study reports among the 53 false positives: PPHN n=1 and explicitly healthy n=39; the remaining 13 are not clinically classified in the available extraction.

**CAN-CCHD coding:** denominator = 53; confirmed actionable = at least 1 (PPHN); explicitly healthy = 39; diagnosis/outcome not fully ascertained = 13.

**Decision:** INCLUDE / partial-outcome-ascertainment flag. Do not treat the 13 missing classifications as healthy or non-actionable.

## R068 — Almawazini 2017 — INCLUDE retained / highly classifiable

- 2,961 nursery infants screened; 114 positive.
- All positive infants underwent pediatric-cardiology evaluation and echocardiography.
- Seven had critical cardiac defects.
- Thirteen had severe pulmonary hypertension.
- The remaining 94 CCHD-negative positives were classified as 45 PFO without pulmonary hypertension (echo considered normal for age), 5 VSD, and 44 large symptomatic PDA.

**CAN-CCHD coding:** CCHD-negative failed denominator = 107. PPHN n=13 is actionable. PFO n=45 is transitional/non-actionable unless final lesion rule states otherwise. VSD n=5 and especially large symptomatic PDA n=44 require lesion/actionability coding rather than automatic classification.

**Decision:** INCLUDE / lesion-actionability flag. Criterion 6 strongly satisfied.

## R069 — Andrews 2014 — INCLUDE retained

- 1,905 infants screened in the Arkansas implementation program.
- Three failed screening.
- Diagnoses: ASD n=2 and PFO n=1; no CCHD among the three.

**CAN-CCHD coding:** denominator = 3. ASD n=2 requires actionability coding; PFO n=1 is transitional/non-actionable unless final rule states otherwise.

**Decision:** INCLUDE / lesion-actionability flag.

## R071 — Cubells 2018, Valencia — INCLUDE retained / clean actionable outcome

- 8,856 eligible newborns screened.
- Five positive pulse-ox screens.
- Three had severe cardiac malformation (TAPVR/CCHD).
- Two CCHD-negative positive screens had respiratory distress secondary to early-onset sepsis and were admitted to NICU rather than discharged.

**CAN-CCHD coding:** confirmed CCHD-negative failed denominator = 2; actionable CAN-CCHD = 2 early-onset sepsis.

**Decision:** INCLUDE / highly informative.

## R072 — Diller 2018 — INCLUDE retained / significant-disease classification

- 77,148 term newborns screened at/near 24 h using the AAP algorithm.
- One CCHD true positive and 33 false positives.
- The report explicitly states that 10/33 (31.3%) false positives had significant non-CCHD disease.

**CAN-CCHD coding:** denominator = 33; actionable significant non-CCHD disease = 10. The complement (23) is not assigned a specific diagnosis category in the abstract and should not be re-labelled as healthy; however, the study-level statement that 10/33 had significant non-CCHD disease provides an exact numerator for the actionable endpoint.

**Decision:** INCLUDE / diagnosis-subtype-limited flag. Criterion 6 satisfied for the primary actionable proportion.

## R049 — Hamilçıkan 2018 — INCLUDE retained

- 4,518 newborns; the clinically relevant after-24-h screening subgroup contained 4,109 infants.
- No CCHD detected during study period.
- Nine CCHD false-positive screens after 24 h.
- Six had noncritical cardiac diagnoses: AVSD n=2, VSD n=3, PDA n=1.
- Three had other significant non-cardiac pathology.

**CAN-CCHD coding:** denominator = 9; confirmed significant non-cardiac pathology = 3; six cardiac findings require locked CCHD-target/actionability mapping.

**Decision:** INCLUDE / lesion-actionability flag.

## R055 — Taksande 2013 — EXCLUDE PRIMARY / QA CORRECTION

- 2,110 clinically normal newborns; inclusion explicitly allowed postnatal ward **and NICU** infants.
- Screening occurred within the first 4 h using a very low <90% threshold.
- Eight infants had SpO2 <90%; seven had CCHD.
- The single CCHD-negative low-SpO2 infant is not given a diagnosis, clinical outcome, management outcome, or explicit no-diagnosis classification.

**Decision:** EXCLUDE PRIMARY — criterion 6, with an additional mixed-population/NICU concern. The calculable denominator of one CCHD-negative failed screen is insufficient without a clinical outcome.

## R048 — Taksande 2017 — EXCLUDE PRIMARY / QA CORRECTION

- 4,926 liveborn neonates; inclusion again explicitly covered postnatal ward and NICU.
- Twelve had SpO2 <90%; nine had CCHD.
- The three CCHD-negative infants in this primary threshold-positive group are not clinically classified.
- A separate 90–95% saturation group underwent repeat measurement; among persistent low saturations, VSD and AVSD were found, but this is not the report's <90% positive-screen definition and cannot be used to repair the unclassified primary false-positive subgroup.

**Decision:** EXCLUDE PRIMARY — criterion 6 + mixed ward/NICU population. Preserve as accuracy/method context. Potential same-center lineage with R055 remains a non-independence note but does not affect pooling because both are excluded primary.

## R031 — Abu Lehyah 2025, Jordan — INCLUDE retained / highly informative

- 20,482 nursery neonates screened; infants directly admitted to NICU were excluded.
- 752 failed the protocol and underwent echocardiography/additional evaluation.
- The paper reports 138 CCHD/cardiac target cases and explicitly identifies non-CCHD conditions among failed screens.
- PPHN n=102, neonatal sepsis n=85, congenital pneumonia n=60.
- The authors state that 247 additional babies had diseases requiring increased monitoring or treatment.
- Their false-positive analysis distinguishes all CCHD-negative screen positives from those with no ultimate diagnosis: treating PPHN/sepsis/pneumonia as clinically meaningful reduces the false-positive rate from 3.0% to 1.8%.

**CAN-CCHD framework:** approximately 614 CCHD-negative failed screens under the authors' CCHD count (752-138), with actionable non-CCHD pathology n=247 and approximately 367 without an ultimate diagnosis under their false-positive convention. Exact CCHD lesion count must be cross-checked against Table 2 before numerical pooling because the table contains a small number of non-CCHD cardiac findings and source target definitions.

**Decision:** INCLUDE / highly informative; retain early-screen timing and target-definition QA flags.

## R032 — Majani 2025, Tanzania — INCLUDE retained / highly informative

- 10,630 newborns screened; 51 POX positive.
- Echocardiographic evaluation relevant to the primary analysis was available for 49 positive infants.
- CCHD confirmed in 15.
- Among the 34 confirmed CCHD-negative false positives: 8 (23.5%) were normal and 26 (76.5%) had conditions requiring urgent medical intervention: noncritical CHD n=5, respiratory disorders n=10, infections n=11.
- Two of the 51 screen-positive newborns are not part of the 49 with the reported echo classification and should remain unascertained rather than silently added to the confirmed CCHD-negative denominator.

**CAN-CCHD coding:** confirmed CCHD-negative denominator = 34; actionable/urgent other condition = 26; normal = 8. Noncritical CHD lesion-level actionability remains to be frozen.

**Decision:** INCLUDE / highly informative / incomplete-positive-screen-ascertainment flag for the two unclassified screen positives.

## Net QA effect of Set 2

Retained INCLUDE:
- R007 Sendelbach
- R035 Hoke
- R068 Almawazini
- R069 Andrews
- R071 Cubells
- R072 Diller
- R049 Hamilçıkan
- R031 Abu Lehyah
- R032 Majani

Corrected to EXCLUDE PRIMARY:
- R055 Taksande 2013
- R048 Taksande 2017

## Next step

Audit the remaining INCLUDE/CONDITIONAL reports not already covered by strict-QA tranche files or Sets 1–2. Then construct one terminal report-status registry for the frozen 219-report master, incorporating post-freeze companion-only amendments without increasing independent cohort count.