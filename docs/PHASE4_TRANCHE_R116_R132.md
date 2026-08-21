# Phase 4 tranche R116–R132

Date: 2026-08-21
Branch: `phase4-consolidation`

See `PHASE4_CONSOLIDATION_LEDGER_v0.1.md` for governance and global counts.

R116 EXCLUDE PRIMARY / retain program context — Ma 2023 Shanghai, 801,831 newborns, 16,489 dual-index positives. Screening positive is POX + auscultation and the report does not provide diagnosis/outcome classification among POX-only CCHD-negative failed screens. Major overlap with Shanghai program reports including R117 and earlier Shanghai cohorts.
R117 EXCLUDE PRIMARY / overlap-context — Tian 2025 South Shanghai, 198,606 screened, 3,299 dual-index positives. POX-only performance is reported, but clinical outcomes of POX-only CCHD-negative failures are not classified. Overlaps R116 during 2019–2021 and shares program/investigators.
R118 EXCLUDE PRIMARY / RETAIN NICU / canonical ID assigned — Hu 2016, 4,128 consecutive NICU admissions; NICU-only cohort already represented in master ledger.
R119 EXCLUDE PRIMARY / citation chasing — Jullien 2021 review/evidence summary.
R120 EXCLUDE PRIMARY — Mawson 2018 known antenatally diagnosed CHD cohort; not routine screening of undiagnosed newborns.
R121 EXCLUDE PRIMARY — Vega Amenábar 2017 Guatemala. Positive-screen cohort with 60 positive tests; substantial loss to echocardiographic follow-up (~48% did not attend), preventing complete diagnosis/outcome/no-diagnosis ascertainment across CCHD-negative failed screens. Preserve regional context.
R122 EXCLUDE PRIMARY / citation chasing — Castañeda-Jinete 2024 systematic review.
R123 EXCLUDE PRIMARY / citation chasing — Ramírez-Escobar 2019 narrative review.
R124 EXCLUDE PRIMARY — de Lira Albuquerque 2015 Brazil. 4,027 newborns and 9 CHD reported, but no extractable clinical classification of CCHD-negative failed pulse-ox screens sufficient for CAN-CCHD outcome.
R125 INCLUDE / MULTI-SITE IMPLEMENTATION REPORT — Sola/SIBEN 2020 contains directly extractable routine screening units that must be treated separately, not as one pooled cohort. San Luis: >1,400 infants screened; 4 hypoxemic infants detected, none CCHD, all required supplemental oxygen. Rosario: 28 failed first test, 25 passed repeat, 3 required further repeat; one final positive had normal echo, severe transient tachypnea, NICU admission and supplemental oxygen for 5 days. Extract site-level denominators independently and audit for overlap with separate publications before pooling.
R126 INCLUDE / QA FLAG — Atitlán-Gil 2020 Hidalgo, Mexico. 1,748 screened; 29 positive screens underwent echocardiography. Detailed text reports 14 simple/noncritical CHD and 3 CCHD among screen positives, with 12 remaining without CHD on echo. Primary CCHD-negative failed denominator = 26 using detailed text; noncritical CHD = 14; remaining 12 require diagnosis-not-ascertained coding rather than assuming healthy. Abstract reports 13.8% CCHD, inconsistent with detailed 3/29 and likely incorporating another clinically detected CCHD; use detailed screen-positive flow and retain QA flag.
R127 INCLUDE / HIGH-ALTITUDE FLAG — González-Andrade 2018 Quito. 963 term newborns; 53 positive pulse-ox screens; no CCHD. At least 23 ASD and 6 PDA+ASD identified; remaining positive-screen diagnoses require fuller classification. High-altitude physiology (2,820 m) requires sensitivity/subgroup flag.
R128 INCLUDE — Witkowski 2024 Brazil. 5,667 asymptomatic newborns; 10 positive pulse-ox screens; no CCHD. Echocardiography: 1 ostium secundum ASD/interatrial communication, 7 PFO, 2 normal. Preserve ASD as noncritical CHD; PFO as likely transitional/non-actionable unless protocol actionability rule states otherwise; two explicitly normal echo but not automatically equivalent to broader clinical healthy status.
R129 EXCLUDE PRIMARY — Medeiros 2015 provider survey/interviews; not newborn cohort.
R130 INCLUDE / EARLY-SCREEN + ACTIONABILITY FLAG — Rendón Díez 2025 Colombia. 609 neonates; 42 (6.9%) pulse-ox positive; no CCHD. Exploratory analysis reports 29 noncritical CHD detected by pulse-ox screening. Echo findings across the broader echo group include ASD, VSD, partial anomalous pulmonary venous connection, PFO, PDA and pulmonary hypertension; 12 infants were hospitalized for noncardiac conditions, but those noncardiac events are not isolated to the 42 positive screens. Use CCHD-negative failed denominator 42; do not assign all 29 noncritical echo findings as clinically actionable until lesion-level actionability is frozen. Early screening median 15.4 h is a heterogeneity flag.
R131 EXCLUDE PRIMARY / context — Moreno 2024 Peru position/implementation paper; no original cohort.
R132 EXCLUDE PRIMARY / citation chasing — Balseca Artos 2026 narrative review.

Count impact: R118 was already represented under a dash ID and only receives its canonical ID; the other 16 reports are newly nominally represented. New decisions among those 16: 5 INCLUDE reports (R125,R126,R127,R128,R130) and 11 EXCLUDE PRIMARY/context reports. Global working state after this tranche: 119/156 reports represented; 57 INCLUDE/INCLUDE-with-flag; 57 EXCLUDE PRIMARY/context/NICU; 4 companion/no independent cohort; 1 conditional/supporting; 0 MAYBE among adjudicated; 37 unreconciled.

New overlap/QA flags:
- Shanghai R116/R117 overlap each other and earlier Shanghai program reports; neither contributes to primary CAN-CCHD denominator because POX-only failed-screen outcomes are not separable.
- R125 SIBEN must be extracted as site-level study units (San Luis, Rosario) and checked against any independent publication from those sites.
- R126 abstract/detail discrepancy for number of CCHD among positive screens; use detailed flow unless later source resolves.
- R127 high-altitude subgroup.
- R128 PFO/transitional physiology coding.
- R130 lesion-level actionability and early-screen timing.
