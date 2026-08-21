# CAN-CCHD Phase 4.5 — Recent Wave A + Typo/Grey-Literature Reconciliation

Date: 2026-08-21
Status: COMPLETE / SATURATION COUNTER RESET TO ZERO
Branch: `phase4-consolidation`

## Purpose

After Closing Wave 4 found NR044 Kishore Kumar 2017, Phase 4.5 required two independent zero-new-primary waves before freeze. The first attempted recent/current wave (2024–2026) did **not** produce zero. It also revealed a search-recall vulnerability to nonstandard spelling (`oxymetry`) and poorly indexed/grey-literature reports. Therefore the wave was deliberately expanded to typo variants, regional journals, theses and backward references before restarting the saturation counter.

`RESTART_LEGACY_DATA_FIREWALL.md` applies. No legacy app/database data were used.

## New report identities

### NR049 — Nathawani et al. 2024 — EXCLUDE PRIMARY / criterion 6

**Citation:** Nathawani RR, Chandra NS, Abhijith YV, Ramesh AC, Ramesh M. *Role of Pulse Oximetry as a Screening Tool for the Detection of Congenital Heart Disease in Newborn Babies.* Apollo Medicine. 2024;21(1):19–21. DOI 10.4103/am.am_55_23. First online 2023-08-07.

- 1,333 births; 1,117 eligible neonates.
- 259 were considered suspicious by the study's SpO2 pathway and evaluated by echocardiography.
- Six had CHD.
- No usable clinical diagnosis/outcome/no-diagnosis distribution is supplied for the large POX-positive/CHD-negative group.

**Decision:** EXCLUDE PRIMARY / RETAIN ACCURACY CONTEXT — criterion 6.

### NR050 — Neelannavar et al. 2024 — INCLUDE; representative report for `NEELANNAVAR_BAGALKOT_400`

**Citation:** Neelannavar R, Talawar K, Vinaykumar, Mirji G. *Pulse Oximetry Screening For Critical Congenital Heart Defects In Asymptomatic Newborn Babies.* Journal of Cardiovascular Disease Research. 2024;15(6):741–744. DOI 10.48047/jcdr.2024.15.06.74.

Underlying cohort, confirmed by the 2017 thesis and companion reports:
- 400 asymptomatic newborns screened after 24 h.
- 7 final hypoxemic/positive screens.
- 4 diagnosed as CCHD by the authors (TGA, TAPVC, DORV cluster).
- 2 ASD.
- 1 reported as normal.

Thus the report provides three author-defined CCHD-negative failed screens (2 ASD, 1 normal), subject to locked lesion/actionability coding.

**Decision:** INCLUDE / lesion-actionability + target-definition flag.

### NR051 — Talawar et al. 2024 — COMPANION / SAME COHORT AS NR050

**Citation:** Talawar K, Vinaykumar, Mirji G, Neelannavar R. *A study on critical congenital heart defects in asymptomatic newborn babies.* Journal of Cardiovascular Disease Research. 2024;15(6):738–740. DOI 10.48047/jcdr.2024.15.06.73.

Same authors, institution, issue, screening method and N=400 program as NR050.

**Decision:** COMPANION / NO INDEPENDENT COHORT CONTRIBUTION.

### NR052 — Mirji et al. 2024 — COMPANION / SAME COHORT AS NR050

**Citation:** Mirji G, Neelannavar R, Talawar K, Vinaykumar. *Clinical Parameters of New Born Subjected for Detection of Critical Congenital Heart Disease at a Tertiary Care Hospital.* Research Journal of Medical Sciences. 2024;18(7):144–147. DOI 10.36478/makrjms.2024.7.144.147.

- Explicitly reports the same N=400 newborn program.
- Same institution/authors/screening rules as NR050.

**Decision:** COMPANION / NO INDEPENDENT COHORT CONTRIBUTION.

### NR053 — Vinaykumar et al. 2024 — COMPANION / SAME COHORT AS NR050

**Citation:** Vinaykumar, Mirji G, Neelannavar R, Talawar K. *Correlates of Pulse Oximetry Saturation in Asymptomatic Newborn Babies.* Research Journal of Medical Sciences. 2024;18(7):160–163.

Same four-author Bagalkot research program and same issue/program as NR050/NR052.

**Decision:** COMPANION / NO INDEPENDENT COHORT CONTRIBUTION.

### NR054 — Neelannavar 2017 thesis — COMPANION / GREY-SOURCE PROVENANCE FOR NR050

**Identity:** Ramesh Neelannavar. *Pulse Oximetry Screening For Critical Congenital Heart Defects In Asymptomatic Newborn.* BLDE University/Vijayapur thesis, 2017.

- Provides the clearest underlying cohort description: N=400, seven hypoxemic, four CCHD, two ASD, one normal.
- This is source/provenance for the later publication cluster, not an independent cohort.

**Decision:** COMPANION / GREY-LITERATURE PROVENANCE; no independent pooling.

### NR055 — Bhojak et al. 2024 — EXCLUDE PRIMARY / criterion 6

**Citation:** Bhojak RD, Chaurasia S, Raina R, Chaudhari C. *A Prospective Study on Pulse Oximetry as a Tool for Early Detection of Congenital Heart Diseases.* Journal of Cardiovascular Disease Research. 2024;15(3):127–135. DOI 10.48047/jcdr.2024.15.03.16.

- Prospective newborn POX/clinical-parameter study.
- Accessible reporting identifies abnormal saturations/CHD detection but does not provide a defensible clinical-outcome distribution specifically among CCHD-negative failed screens.

**Decision:** EXCLUDE PRIMARY / RETAIN ACCURACY CONTEXT — criterion 6.

### NR056 — Soni et al. 2025 — EXCLUDE PRIMARY / criterion 6

**Citation:** Soni T, Pol VS, Takalkar AA. *Prevalence of Suspected Congenital Cardiac Disease Using Pulse Oxymeter: A Descriptive Observational Study from Maharashtra.* Journal of Chemical Health Risks. 2025;15(5).

- N=100.
- Four failed POX screens.
- The article reports a 4% suspected CHD prevalence from POX but does not provide echocardiographic/clinical disposition of the four failures.

**Decision:** EXCLUDE PRIMARY — criterion 6.

### NR057 — Santosh Kumar & Jaiswal 2021 — EXCLUDE PRIMARY / criterion 6 + derivative-text QA

**Citation:** Santosh Kumar, Bir Prakash Jaiswal. *A Prospective Study to evaluate the Validity of Pulse Oxymeter Screening for early detection of Congenital heart disease.* International Journal of Health and Clinical Research. 2021;4(19):140–143.

- Abstract describes a 12-month term-newborn study with POX within 4 h and at 48–72 h.
- Reports sensitivity 26% and specificity 99.8% for POX, but no patient-level failed-screen clinical distribution.
- Methods/results wording and summary metrics are strikingly similar to Ahmed 2019 despite different authors/institution; no cohort identity is assumed without evidence.

**Decision:** EXCLUDE PRIMARY — criterion 6; retain `possible derivative-content / provenance QA` flag. Do not pool as companion unless identity is proven.

### NR058 — Reddy & Devaraj 2018 — INCLUDE / lesion-level mapping flag

**Citation:** Reddy GC, Devaraj KN. *Can pulse oxymetry be used as a routine screening tool in early diagnosis of critical congenital heart diseases in newborns?* International Journal of Contemporary Pediatrics. 2018;5(3):867–872. DOI 10.18203/2349-3291.ijcp20181504.

- 800 newborns.
- One persistent positive screen: SpO2 88% right thumb, 90% left thumb, 92% left great toe.
- Echocardiography: ASD + VSD + pulmonary stenosis.
- No cyanosis, oedema or tachypnoea reported.

**Decision:** INCLUDE / locked CCHD-target mapping + noncritical-lesion actionability flag. Do not assume pulmonary stenosis is critical without source-supported severity.

### NR059 — John et al. 2016, West Virginia — INCLUDE / high-value nominal table

**Citation:** John C, Phillips J, Hamilton C, Lastliger A. *Implementing Universal Pulse Oximetry Screening in West Virginia: Findings from Year One.* West Virginia Medical Journal. 2016;112(4):42–46. PMID 27491102.

- 20,115 infants entered Birth Score database; 19,283 screened.
- 19 failed.
- 17/19 had TTE reports available; 7/17 were CCHD.
- Two failed screens had no TTE and remain unascertained.
- The 10 confirmed CCHD-negative failures have nominal diagnoses:
  1. ASD + low-normal heart function
  2. mild Ebstein anomaly/TR + PFO
  3. ASD + PDA
  4. PPHN + PDA
  5. VSD + PFO
  6. ASD with L→R shunt
  7. PFO with L→R shunt
  8. pulmonary hypertension + bidirectional PDA
  9. PFO with L→R shunt
  10. ASD + low-normal heart function

**Decision:** INCLUDE / confirmed primary denominator 10; incomplete-ascertainment flag for two failed screens without TTE; lesion/actionability mapping required.

### NR060 — Mouledoux et al. 2017 — EXCLUDE PRIMARY / criterion 6

**Citation:** Mouledoux J, Guerra S, Ballweg J, Li Y, Walsh W. *A novel, more efficient, staged approach for critical congenital heart disease screening.* Journal of Perinatology. 2017;37:288–290. PMID 27831548. DOI 10.1038/jp.2016.204.

- Tennessee 2013–2014 state program; 163,699 screening records submitted.
- 232 failed the staged algorithm.
- 51 were true-positive CCHD.
- Clinical diagnoses/outcomes of the CCHD-negative failed screens are not reported.

**Decision:** EXCLUDE PRIMARY / RETAIN ALGORITHM-IMPLEMENTATION CONTEXT — criterion 6.

### NR061 — Polanki et al. 2022 — EXCLUDE PRIMARY / criterion 6

**Citation:** Polanki R, Bolishetti KK, Shanigaram K, Pallee S, Babjian S, Sreeramdasu LD. *Neonatal Pulse Oxymetry Screening for Detection of Congenital Heart Disease in Asymptomatic Newborns: A Cross-sectional Study from a Tertiary Care Hospital.* Journal of Clinical and Diagnostic Research. 2022;16(5):SC11–SC14. DOI 10.7860/JCDR/2022/55706.16364.

- 14,400 term asymptomatic newborns.
- 45 POX positive.
- 30 CHD on echo, 15 false positives.
- No clinical diagnosis/outcome distribution for the 15 false-positive/CCHD-negative infants.

**Decision:** EXCLUDE PRIMARY / RETAIN ACCURACY CONTEXT — criterion 6.

### NR062 — Ahmed 2019 observational report — INCLUDE

**Citation:** Ahmed SN. *Effectiveness of a Pulse Oximetric Screening for the Detection of Congenital Heart Disease in Asymptomatic New-Borns — An Observational Study.* Asian Journal of Clinical Pediatrics and Neonatology. 2019;7(1):46–50. DOI 10.21276/ajcpn.2019.7.1.11.

- N=1,000 term newborns.
- POX within 4 h and at 48–72 h.
- At 48–72 h, seven infants had SpO2 <95%.
- Five had cyanotic heart disease described by the paper as CCHD/cyanotic disease.
- One had acyanotic CHD with severe PPHN.
- One had severe PPHN without reported CHD.

**Decision:** INCLUDE / target-definition and lesion-level mapping flag. The paper provides explicit non-CCHD/PPHN information, but final denominator must follow the review's locked CCHD lesion definition rather than the authors' broad labels.

### NR063 — Ahmed 2019 comparative report — COMPANION / SAME COHORT AS NR062

**Citation:** Ahmed SN. *A Comparative Study of Pulse Oximetry Screening and Clinical Examination in Diagnosis of Congenital Heart Disease.* Asian Journal of Clinical Pediatrics and Neonatology. 2019;7(2):1–5.

Same author, institution (Narayana Medical College, Nellore), 12-month period, February 2018–January 2019, same POX timings and same clinical-examination protocol as NR062.

**Decision:** COMPANION / NO INDEPENDENT COHORT CONTRIBUTION vs NR062.

### NR064 — Lanker et al. 2014 — INCLUDE / echo-normal, not healthy

**Citation:** Lanker AM, Chowdhary J, Jeelani N, Jeelani S, Hassan AU, Wani N. *Effectiveness of pulse oximetry screening for congenital heart disease in asymptomatic new-borns.* International Journal of Research in Medical Sciences. 2014;2(3):1112–1116. DOI 10.5455/2320-6012.ijrms20140894.

- 1,200 asymptomatic newborns screened >24 h.
- Three had SpO2 ≤95%.
- TGA in one; truncus arteriosus in one; third had structurally normal heart on echocardiography.

**Decision:** INCLUDE. The single CCHD-negative failed screen is `echo-normal / alternative diagnosis not reported`; **do not code as healthy** merely because the heart was structurally normal.

### NR065 — Shah et al. 2015, Pravara/Loni — ZERO CCHD-NEGATIVE DENOMINATOR

**Citation:** Shah F, Chatterjee R, Patel PC, Kunkulol RR. *Early detection of critical congenital heart disease in newborns using pulse oximetry screening.* International Journal of Medical Research & Health Sciences. 2015;4(1):78–83. DOI 10.5958/2319-5886.2015.00013.2.

- 700 intramural neonates screened within 24 h.
- Four final/persistent positives underwent echo.
- Final diagnoses: complete AVSD, TGA, supracardiac TAPVC, preductal coarctation.
- Under the source's target all four were treated as CCHD; locked lesion mapping should confirm this, but no obvious CCHD-negative failed screen is reported.

**Decision:** EXCLUDE FROM PRIMARY CAN-CCHD PROPORTION / ZERO ELIGIBLE CCHD-NEGATIVE DENOMINATOR; retain screening context and lesion-definition QA.

### NR066 — Siva et al. 2016 — ZERO CCHD-NEGATIVE DENOMINATOR

**Citation:** Siva P, Senthilvelan B, Gopalakrishnan H, Subramanian S. *Role of pulse oximetry in screening newborns for congenital heart disease at 1 hour and 24 hours after birth.* International Journal of Contemporary Pediatrics. 2016;3(2):631–634. DOI 10.18203/2349-3291.ijcp20161053.

- 430 asymptomatic newborns.
- Five positive at 1 h.
- Echo: 3 HLHS, 1 TGA, 1 truncus arteriosus.
- No CCHD-negative failed screen reported among the positives.

**Decision:** EXCLUDE FROM PRIMARY CAN-CCHD PROPORTION / ZERO ELIGIBLE CCHD-NEGATIVE DENOMINATOR; retain early-screen context.

## New cohort clusters created

### `NEELANNAVAR_BAGALKOT_400`
- NR050 representative quantitative report
- NR051 companion
- NR052 companion
- NR053 companion
- NR054 thesis/grey-source provenance

Only one cohort contribution may enter any quantitative synthesis.

### `AHMED_NELLORE_1000`
- NR062 representative quantitative report
- NR063 companion

Only NR062 contributes independently.

### Tennessee program context
- NR045 Walsh 2011 Middle Tennessee (earlier local implementation report)
- NR060 Mouledoux 2017 statewide 2013–2014 staged-algorithm study

Do not assume cohort overlap solely from state/program lineage; neither currently contributes a CAN-CCHD numerator because criterion 6 is not met.

## Wave result

New report identities added in this reconciliation: **18 (NR049–NR066)**.

New independent reports currently eligible to contribute CAN-CCHD information:
- NR050 Neelannavar/Bagalkot
- NR058 Reddy & Devaraj
- NR059 John/West Virginia
- NR062 Ahmed/Nellore
- NR064 Lanker/Srinagar

New zero-CCHD-negative-denominator screening reports:
- NR065 Shah/Pravara
- NR066 Siva/Chennai

Because multiple new independent primary reports were found, **saturation counter = 0**.

## Next step

1. Incorporate NR049–NR066 into report master v0.4.
2. Restart saturation only after this expanded delta set is fixed.
3. Run Zero Wave 1 using broad typo/grey/regional variants that are independent of the queries that found these reports.
4. Run Zero Wave 2 using backward/forward citation chasing from NR050, NR058, NR059, NR062, NR064 and high-yield anchors.
5. Any newly discovered independent primary report resets the counter again.
6. Make a final direct attempt to identify native PMID 22984710 before Phase 4.5 freeze.