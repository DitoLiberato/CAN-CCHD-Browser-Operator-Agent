# CAN-CCHD Phase 5 — Extraction Block 06 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Block file: `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_06.csv`

## Purpose

Block 06 tests four recurrent Phase 5 problems without altering the locked protocol:

1. minor cardiac findings that become actionable only when a specific follow-up consequence is documented;
2. a conditional harmonized-CCHD lesion whose <=28-day intervention/death status is unavailable;
3. very-early transitional screening with physiologic PDA findings;
4. the rule that a normal echocardiogram is not equivalent to an ascertained healthy/noncardiac outcome.

No scientific value was imported from the legacy Browser Agent/database.

## U_R022 — Soto Torselli 2020, Guatemala

Primary source: Soto Torselli AS, Orellana Morales SM. *Detección temprana de cardiopatías congénitas en neonatos sanos con oximetría de pulso.* Rev Fac Med Guatemala. 2020;1(28):31-40. DOI 10.37345/23045329.v1i28.62.

Primary-source facts:
- 376 clinically healthy newborns screened with the American pre/postductal algorithm;
- 11 final positive screens;
- 10 echocardiograms completed because one infant did not attend the echocardiography appointment;
- of the 10 echocardiograms, one was structurally normal and nine showed noncritical cardiac abnormalities;
- reported findings overlap across infants: PFO 7, small ASD 2, PDA 1, biventricular hypertrophy 1, dilated coronary sinus 1;
- no important cyanotic lesion or important hemodynamic/clinical compromise was found;
- the report states that follow-up would continue through the IGSS pediatric-cardiology outpatient clinic.

Harmonized target:
- no reported lesion meets the locked harmonized-CCHD target;
- denominator = 11.

CAN coding:
- the nine abnormal-echo infants receive `CAN-B`, not because PFO/ASD/PDA are inherently actionable, but because a specific cardiology follow-up consequence is documented for the abnormal cardiac findings;
- the structurally normal echo is not called healthy because no noncardiac cause/outcome is reported;
- the infant lost before echo is `UNKNOWN`.

Terminal classification:
- CAN-B = 9;
- Strict = Expanded = 9/11;
- UNKNOWN = 2;
- terminal ascertainment = 9/11 = 81.8%;
- `SENSITIVITY_ONLY` because ascertainment is below the locked >=90% threshold.

This is a direct demonstration that the same lesion (for example PFO) may be NON_CAN in one report and CAN-B in another depending on documented management/follow-up consequence.

## U_R034 — Havelund 2019, Denmark

Primary source: Havelund KW et al. *Implementation of pulse oximetry screening in a Danish maternity ward.* Dan Med J. 2019;66(11):A5576. PMID 31686645.

Primary-source facts:
- 2,855 apparently healthy newborns screened;
- median first screening time 2.5 h after birth (range 0.5-7.5 h);
- 59 non-approved final screens required paediatric assessment;
- 16 remained with their mother after assessment because no further treatment was required;
- 18 were admitted to NICU for observation until saturation normalized, without treatment;
- 25 required treatment;
- within the treated group were 14 transitory tachypnoea, 10 other treatment-requiring conditions, and one pulmonary stenosis classified by the authors as CCHD.

Actionability:
- NICU observation is a qualifying acute disposition consequence even without pharmacologic treatment;
- therefore the 18 observation-only infants are CAN-A;
- the 24 non-pulmonary-stenosis treated infants are also CAN-A;
- if pulmonary stenosis remains in the harmonized-CCHD-negative denominator, it is also CAN-A because treatment was required;
- the 16 assessment-only infants are aggregate NON_CAN; they are not relabeled as explicitly healthy without a more specific terminal diagnosis statement.

Harmonized target problem:
- pulmonary valve stenosis is a conditional locked-target lesion;
- the report does not document death or surgery/catheterization within 28 days;
- therefore the review cannot point-identify whether this infant is harmonized CCHD.

Bounded terminal classification:
- harmonized CCHD = 0-1;
- denominator = 58-59;
- CAN-A / Strict / Expanded = 42-43;
- NON_CAN = 16;
- ascertainment = 100% within either admissible mapping;
- `SENSITIVITY_ONLY` because a single primary-analysis weight cannot be assigned without inventing <=28-day timing.

The implied Strict proportion is stable: 42/58 = 72.4% versus 43/59 = 72.9%. The uncertainty is principally a weighting/target-membership issue, not a substantive reversal of the clinical-yield estimate.

## U_R108 — Shah 2026, India

Primary source: Shah H et al. *Role of Pulse Oximetry Screening for Term Healthy Newborns During Transitional Period to Detect Critical Congenital Heart Disease (CCHD): A Prospective Observational Study in a Tertiary Care Hospital.* Cureus. 2026;18(5):e108873. PMID 42299162; PMCID PMC13264696; DOI 10.7759/cureus.108873.

Primary-source facts:
- 530 healthy term newborns >=2.5 kg;
- saturation measured at 15 min and 6 h;
- 81 were low at 15 min, but 75 normalized by 6 h and are PASS under the review's final-failed-screen rule;
- six remained abnormal and underwent echocardiography;
- findings: TGA with severe PAH; tricuspid atresia with moderate PAH; four PDA/PFO patterns;
- the authors explicitly state that the PDA findings may be physiologic transitional findings and that follow-up echocardiography was not part of the protocol.

Harmonized target:
- TGA without reported structural complexity is mapped as simple TGA and therefore unconditional harmonized CCHD;
- tricuspid atresia is not an automatic lesion in the locked target, and no early-course equivalence is documented;
- harmonized CCHD = 1;
- denominator = 5.

CAN coding:
- four early PDA/PFO findings = NON_CAN transitional physiology;
- tricuspid atresia = CAN-U because it is clinically relevant but no specific treatment, escalation, altered disposition, or required follow-up is reported;
- diagnosis severity alone is not substituted for actionability.

Terminal classification:
- Strict = 0/5;
- Expanded = 1/5;
- NON_CAN = 4/5;
- ascertainment = 100%;
- `PRIMARY_POOLABLE`, with mandatory very-early-screening/transitional-period sensitivity flag.

## U_R128 — Witkowski et al. 2024, southern Brazil

Primary source: Witkowski SM et al. *Prevalence of Critical Congenital Heart Disease Detected in the Pulse Oximetry Test in Asymptomatic Newborns, >=35 Gestational Weeks, in a Maternity in Southern Brazil.* Int J Cardiovasc Sci. 2024;37:e20230065. DOI 10.36660/ijcs.20230065.

Primary-source facts:
- 5,667 asymptomatic newborns >=35 weeks included;
- tests performed before 24 h were excluded;
- 10 persistent positive screens;
- no screen-positive CCHD;
- echocardiography: normal 2; PFO 7; ostium-secundum interatrial communication 1;
- five CCHD infants born during the same period became symptomatic before the screening window and were not participants in the failed-screen cohort.

CAN coding:
- PFO 7 and the single incidental ASD/IAC have no documented qualifying management consequence and are NON_CAN under the locked minor-lesion rule;
- the two normal echocardiograms cannot be reclassified as healthy because no noncardiac diagnosis/outcome ascertainment is reported.

Terminal classification:
- denominator = 10;
- Strict = Expanded = 0/10;
- NON_CAN = 8;
- UNKNOWN = 2;
- terminal ascertainment = 80%;
- `SENSITIVITY_ONLY` because the unit fails the >=90% fully-classified threshold.

## Block-level result

Four additional frozen units were structurally extracted.

Block 06 dispositions:
- PRIMARY_POOLABLE: U_R108;
- SENSITIVITY_ONLY: U_R022, U_R034, U_R128;
- new unresolved holds: none.

Cumulative Phase 5 state after Blocks 01-06:
- extracted = 23/76;
- PRIMARY_POOLABLE = 15;
- SENSITIVITY_ONLY = 6;
- HOLD_PENDING_QA = 2 (U_R033, U_R102);
- unextracted = 53.

## Methodological conclusion

Block 06 reinforces three binding principles:

1. actionability is a consequence-of-care construct, not a lesion-name construct;
2. normal echocardiography does not provide noncardiac outcome ascertainment;
3. conditional harmonized-CCHD lesions remain bounded/sensitivity-only when the required <=28-day course is unavailable rather than being forced into a point denominator.
