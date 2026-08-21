# Phase 4 tranche R038–R047

Date: 2026-08-21
Branch: `phase4-consolidation`

Governance follows `PHASE4_CONSOLIDATION_LEDGER_v0.1.md`.

R038 EXCLUDE PRIMARY — Vaidyanathan 2011, Kerala. Prospective newborn cohort using combined clinical examination + lower-extremity pulse oximetry, with universal/near-universal echocardiographic ascertainment. The report evaluates predictors of CHD but does not provide an isolated failed-POX CCHD-negative cohort with diagnosis/outcome/no-diagnosis classification suitable for the CAN-CCHD denominator.

R039 INCLUDE / ASCERTAINMENT-INCOMPLETE FLAG — Bradshaw 2012. 6,745 screened; 9 positive POX screens. One CCHD; four noncritical CHD (dextrocardia with lobar pneumonia requiring NICU, dilated ascending aorta, two ASDs); one confirmed no CHD after evaluation; three additional positives had no further testing/consultation. CCHD-negative denominator = 8, but 3/8 are diagnosis-not-ascertained. Preserve categories; do not assume those three were healthy.

R040 EXCLUDE PRIMARY / RETAIN DETECTION CONTEXT — Prudhoe 2013. 29,925 screened in North-East UK historical cohort; strong CCHD/serious-CHD detection data but no defensibly extractable final failed-POX CCHD-negative denominator with clinical outcome classification for CAN-CCHD. Possible historical overlap/context relation with Richmond/North-East UK work remains flagged.

R043 INCLUDE — Oakley 2015. 6,329 screened; 14 saturation <95%; 7 CCHD. Among 7 CCHD-negative positives: 3 significant noncritical CHD and 4 previously undiagnosed respiratory illness or sepsis. All low-saturation infants had identifiable pathology. Highly informative.

R044 EXCLUDE PRIMARY / QA CORRECTION — Saxena 2015. 19,009 newborns, major/critical CHD accuracy study with low specificity. Authors attribute low specificity partly to infections/respiratory issues and lack of repeat testing, but do not classify the CCHD-negative pulse-ox positives sufficiently to derive a defensible CAN-CCHD numerator/no-diagnosis distribution. Previous permissive INCLUDE status is corrected under strict criterion 6.

R045 EXCLUDE PRIMARY / RETAIN OVERLAP-CONTEXT — Miller 2016 Wisconsin out-of-hospital cohort. 1,616 with detailed POS; 16 failed, 3 CCHD detected by POS. The report does not clinically classify all remaining CCHD-negative failed screens. It overlaps a 2013 SHINE/J Pediatr report in which 3 failures included 2 sepsis and 1 CHD; partial companion information is insufficient for a complete 2013–2014 CAN-CCHD numerator. Do not pool as independent outcome cohort until report-cluster reconstruction.

R046 EXCLUDE PRIMARY — Patriciu 2017. 5,406 infants assessed at first hour and 24 h; study reports sensitivity/specificity for CHD and 14 critical CHD identified, but does not provide a final failed-screen CCHD-negative cohort with diagnosis/outcome/no-diagnosis classification.

R047 EXCLUDE PRIMARY — Shahzad 2017. Cross-sectional diagnostic study, 138 neonates with echocardiography of all enrolled participants; POX test-performance data are reported, but clinical diagnoses/outcomes among CCHD-negative test positives are not presented in a way that supports the CAN-CCHD numerator.

Count impact versus prior master ledger: R041 and R042 were already represented; newly reconciled reports in this gap block = 8 (R038,R039,R040,R043,R044,R045,R046,R047). New decisions: 2 INCLUDE (R039,R043), 6 EXCLUDE PRIMARY. Updated working total = 137/156 represented; 68 INCLUDE; 64 EXCLUDE primary/context/NICU; 4 companion; 1 conditional/supporting; 0 MAYBE among adjudicated; 19 unreconciled.

QA/overlap additions:
- R039: three positive screens lacked further work-up; diagnosis-not-ascertained, not healthy.
- R040: North-East UK historical overlap/context flag.
- R044: strict criterion-6 correction from prior permissive inclusion.
- R045: Wisconsin SHINE 2013–2014 overlaps earlier 2013 J Pediatr report; reconstruct cluster before any use.
