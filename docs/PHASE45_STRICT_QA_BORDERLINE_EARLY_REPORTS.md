# CAN-CCHD Phase 4.5 — Strict QA of Borderline Early Reports

Date: 2026-08-21
Status: TERMINAL QA / CORRECTIVE

## Purpose

Re-audit older permissive INCLUDE decisions under the final protocol criterion 6:

> A calculable CCHD false-positive count alone is insufficient. The CCHD-negative failed-screen group must contain diagnosis, clinical outcome, management, or explicit no-diagnosis information sufficient to support CAN-CCHD classification. `Normal echo` is not automatically `healthy`, and secondary summaries must not override contradictory primary-report evidence.

This audit uses restart-native records and independently reverified primary/full-text sources only. Legacy Browser Agent data are prohibited by `RESTART_LEGACY_DATA_FIREWALL.md`.

## Decisions

### R004 — Bakr 2005 — EXCLUDE PRIMARY / QA CORRECTION

**Report:** Bakr AF, Habib HS. *Combining pulse oximetry and clinical examination in screening for congenital heart disease.* Pediatr Cardiol. 2005;26(6):832–835. PMID 16088415.

Primary-report evidence:
- 5,211 asymptomatic newborns screened.
- Echocardiography was triggered by low pulse oximetry in five infants and by significant murmur in ten others.
- Primary abstract reports screening performance but does not give a complete clinical diagnosis/outcome distribution specifically for the CCHD-negative pulse-ox failed screens.

QA conflict:
- Later secondary sources disagree on the number/composition of CCHD false positives (e.g. one vs two depending on target definition) and one review table labels an event only as `other`.
- Because the primary source does not provide a stable, clinically classifiable CCHD-negative failed-screen cohort, the CAN-CCHD denominator/numerator cannot be reconstructed defensibly without relying on conflicting secondary reinterpretation.

**Terminal decision:** EXCLUDE PRIMARY — criterion 6 / target-definition discrepancy. Retain historical accuracy/context.

### R005 — Rosati 2005 — EXCLUDE PRIMARY / QA CORRECTION

**Report:** Rosati E, Chitano G, Dipaola L, De Felice C, Latini G. *Indications and limitations for a neonatal pulse oximetry screening of critical congenital heart disease.* J Perinat Med. 2005;33(5):455–457. PMID 16238542.

Primary-report evidence:
- 5,292 apparently healthy newborns screened at median 72 h.
- Primary report: 2 true positives, 1 false negative and 1 false positive for the authors' critical-CCVM target.
- The primary abstract/full accessible record does not clinically classify the false-positive infant beyond absence of the target CCVM.

QA conflict:
- A later review table reports two CCHD false positives with one `other` and one `healthy`, whereas the primary study reports one false positive under its target definition.
- This mismatch strongly suggests target-definition reclassification and cannot be imported into CAN-CCHD without lesion-level primary evidence.

**Terminal decision:** EXCLUDE PRIMARY — criterion 6 / target-definition discrepancy. Retain accuracy context.

### R012 — Ruangritnamchai 2007 — EXCLUDE PRIMARY / QA CORRECTION

**Report:** Ruangritnamchai C, Bunjapamai W, Pongpanich B. *Pulse oximetry screening for clinically unrecognized critical congenital heart disease in the newborns.* Images Paediatr Cardiol. 2007;9(1):10–15. PMID 22368668; PMCID PMC3232575.

Full-text evidence:
- 1,847 clinically normal newborns screened at 24–48 h.
- Three infants had SpO2 <95%.
- Two had CCHD (TGA; complete AV canal with moderate TR).
- The third CCHD-negative failed screen is not given a diagnosis, clinical outcome, management category, or explicit healthy/no-diagnosis classification in the primary full text.

**Terminal decision:** EXCLUDE PRIMARY — criterion 6. A denominator of one CCHD-negative failed screen is calculable, but the CAN-CCHD clinical category is not ascertainable.

### R015 — Zuppa 2015 — INCLUDE / QA CORRECTION OF DIAGNOSTIC INTERPRETATION

**Report:** Zuppa AA, Riccardi R, Catenazzi P, et al. *Clinical examination and pulse oximetry as screening for congenital heart disease in low-risk newborn.* J Matern Fetal Neonatal Med. 2015;28(1):7–11. PMID 24588079.

Primary full-text evidence:
- 5,750 low-risk/asymptomatic nursery newborns screened at 48–72 h.
- Three newborns were positive on pulse oximetry and had negative cardiovascular physical examination.
- Echocardiography was negative for structural CHD; PFO was present in two of the three.
- No CCHD was detected among the three pulse-ox positive infants.

Critical correction:
- A secondary review table has been read as if all three false positives had PPHN. The primary full text does **not** support that interpretation. The primary source takes precedence.

Primary CAN-CCHD coding:
- CCHD-negative failed-screen denominator = 3.
- PFO = 2, to be coded transitional/non-actionable unless the final lesion rule states otherwise.
- One infant had structurally normal echocardiography; do not automatically label globally healthy beyond the cardiac evaluation.
- Actionable CAN-CCHD numerator = 0 on currently available primary evidence.

**Terminal decision:** INCLUDE / transitional-nonactionable flag.

### R028 — Janjua 2022 — EXCLUDE PRIMARY / QA CORRECTION

**Report:** Janjua D, Singh J, Agrawal A. *Pulse oximetry as a screening test for congenital heart disease in newborns.* J Mother Child. 2022;26:1–9. PMID 35853444; PMCID PMC10032324.

Primary-report evidence:
- 1,082 asymptomatic term neonates aged 2–24 h.
- Five critical CHD cases were confirmed by echocardiography.
- Pulse oximetry alone detected 80% of those critical CHD cases; clinical examination detected 60%; combined screening detected all five.
- The report does not provide a complete count and clinical classification of pulse-ox positive / CCHD-negative infants suitable for a CAN-CCHD denominator.

**Terminal decision:** EXCLUDE PRIMARY — criterion 6 / accuracy-only outcome for the review question.

### R030 — Pico Mawyin 2025 — INCLUDE / TARGET-DEFINITION + TRANSITIONAL-PERIOD + PARTIAL-ASCERTAINMENT FLAGS

**Report:** Pico Mawyin T, Vargas-Vera RM, Viteri Gómez G, et al. *La pulsioximetría como estrategia de tamizaje de las cardiopatías congénitas.* Horizonte Médico. 2025;25(1):e3068.

Primary-report evidence:
- 4,897 term newborns in rooming-in, screened during the transitional period before discharge.
- 626 positive pulse-ox screens.
- Echocardiography: 497 with reported findings and 129 echo-negative.
- Reported findings among the 497: PDA 127; VSD 34; ASD 25; secondary pulmonary hypertension 23; PFO 272; aortic aneurysm 4; coarctation 8; rhythm disorders 4.

CAN-CCHD implications:
- Criterion 6 **is satisfied** because the positive-screen cohort has a detailed diagnostic distribution, including a clinically actionable non-CCHD category (secondary pulmonary hypertension) and multiple noncritical/transitional cardiac findings.
- The final CCHD-negative denominator cannot yet be frozen because the authors call aortic aneurysm and coarctation `critical malformations`, whereas the review's locked CCHD target requires lesion-level remapping rather than accepting the article's terminology automatically.
- The 129 echo-negative infants are `diagnosis not ascertained beyond cardiac echo`, not automatically healthy.
- PFO and much early PDA are likely transitional/non-actionable; VSD/ASD/PDA actionability requires the frozen lesion rule; pulmonary hypertension is potentially actionable.

**Terminal report-level decision:** INCLUDE. Do not enter the quantitative meta-analysis until target-definition mapping and lesion-level actionability are frozen.

### R030 duplicate-publication alert — 2024 RCCSH article

During this QA, an earlier 2024 article was identified with the same Guayaquil cohort, same authors, same N=4,897, same 626 positive screens and same diagnostic counts:

- *Tamizaje de cardiopatías congénitas con el uso de la pulsioximetría.* Revista Científica en Ciencias de la Salud Humana (RCCSH). 2024;3(1). DOI 10.56274/rcs.2024.3.1.38.

This is **not a new quantitative cohort**. Treat as DUPLICATE/COMPANION publication of R030 pending final bibliographic-dedup labeling. Its discovery after the bibliographic freeze does not reset cohort saturation because it contains no independent cohort.

## Net strict-QA changes from older permissive handling

- R004 Bakr: permissive/uncertain → **EXCLUDE PRIMARY**.
- R005 Rosati: permissive/uncertain → **EXCLUDE PRIMARY**.
- R012 Ruangritnamchai: previously treated as potentially includable → **EXCLUDE PRIMARY**.
- R015 Zuppa: **INCLUDE retained**, but primary diagnosis interpretation corrected; no evidence for 3 PPHN.
- R028 Janjua: older include/uncertain → **EXCLUDE PRIMARY**.
- R030 Pico Mawyin: **INCLUDE retained/confirmed**, with target-definition and lesion-actionability gate before pooling.

## Next QA step

Apply the same strict criterion-6 audit to the remaining older/regional INCLUDE rows that have incomplete outcome descriptions or depend on secondary extraction. Then build one terminal status registry for all frozen-master reports and derive unique quantitative cohorts.