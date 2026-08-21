# CAN-CCHD Phase 4 Consolidation Ledger v0.1

Status: WORKING / NOT YET FINAL
Date: 2026-08-21
Branch: `phase4-consolidation`

## Purpose
This ledger is the canonical reconstruction point for Phase 4 full-text adjudication after work was split across chats. It must supersede free-text chat counts once every report is reconciled by canonical corpus ID.

## Governance rules
- Unit of tracking: report, linked to canonical `raw_record_id` whenever available.
- Quantitative unit: unique cohort; companion/overlapping reports are linked and never blindly summed.
- Primary outcome denominator: CCHD-negative failed screens.
- Primary outcome: any clinically actionable non-CCHD diagnosis among CCHD-negative failed screens.
- Preserve separate categories: actionable CAN-CCHD; transitional/non-actionable physiology; explicitly healthy/no diagnosis; diagnosis not reported.
- NICU-only cohorts are excluded from the primary meta-analysis per protocol, but retained for possible secondary/sensitivity analysis.
- Mixed nursery/NICU cohorts are flagged for sensitivity analysis unless a separable well-baby denominator is available.
- Absence of reported alternative diagnosis is not equivalent to healthy.

## Historical Phase 4 checkpoint
The prior chat established a Phase 4 universe of 156 reports: 49 initially routed as `include` and 107 as `maybe`. A historical checkpoint recorded 18 reports already adjudicated as eligible, but their complete nominal list was not preserved. Therefore this ledger will rebuild the exact nominal count and must not mechanically add post-checkpoint decisions to the number 18.

## Recovered / re-adjudicated reports

| Corpus ID | Report | Decision | Key Phase 4 note |
|---|---|---|---|
| R007 | Sendelbach 2008 | INCLUDE | 1 persistent failed screen; echocardiogram normal; no actionable diagnosis. |
| R042 | Bhola 2014 | INCLUDE | 11 CCHD-negative; 6 respiratory disease. |
| R036 | Arlettaz 2006 | INCLUDE | 24 persistent failures; 17 CHD; among remaining 7, 5 PPHN. |
| R066 | Jones 2016 | INCLUDE | 21 CCHD-negative; 16 alternative diagnoses. |
| R034 | Havelund 2019 | INCLUDE | 59 evaluated; 1 CCHD; 14 TTN/respiratory and 10 other treated conditions. |
| R026 | Schwartz 2021 | INCLUDE | 31 failures; 12 CCHD; remaining 19 all had diagnoses (9 noncritical CHD, 10 noncardiac). |
| R072 | Diller 2018 | INCLUDE | 33 CCHD false positives; 10 significant non-CCHD disease. |
| R037 | Tautz 2010 | INCLUDE | 18 persistent failures; 9 CHD; 2 persistent fetal circulation/PPHN; 7 neonatal infections. |
| R009 | Riede 2010 | INCLUDE | 54 positive; 14 CCHD; among 40 non-CCHD: 15 PPHN, 13 sepsis, 12 healthy. |
| R010 | Ewer/PulseOx 2011 | INCLUDE | 169 false positives for major/CCHD; 6 significant non-major CHD and 40 other urgent diseases. |
| R001 | Richmond 2002 | INCLUDE | 13 infants with noncardiac disease initially revealed by low saturation; denominator reconciliation required. |
| R014 | Singh 2014 | INCLUDE | Birmingham cohort; 55 pneumonia, 30 sepsis, 12 PPHN among clinically significant POS admissions. Partial temporal overlap with Henderson 2022. |
| R027 | Henderson 2022 | INCLUDE | Birmingham later cohort; 253 POS admissions, 247 significant diagnoses, 6 transitional/healthy. Partial overlap with Singh 2014. |
| — | Singh & Chen 2022 | INCLUDE | Distinct Cambridge/Rosie cohort; 189 true POS; 156 significant noncardiac conditions; overlap audit required against local companion reports. |
| — | Gamhewage 2021 | INCLUDE | 8,718 screened; 19 positive; 18 CHD, 14 CCHD; 1 positive without CHD, diagnosis not reported. |
| R030 | Pico Mawyin 2025 | INCLUDE | 4,897 screened; 626 positive; 497 structural defects, 129 normal echo; alternative diagnoses not ascertained/reported. |
| — | Donia & Tolba 2016 | CONDITIONAL / SUPPORTING | Selected persistent-low-SpO2 cohort (120), not full screened denominator; may inform positive-screen composition but not population failure incidence unless source denominator recovered. |
| R002 | Koppel 2003 | INCLUDE | One false positive described as delayed transition with self-limited pulmonary hypertension. |
| R003 | Reich 2003 | INCLUDE | Two CCHD false positives, both significant PDA. |
| R004 | Bakr 2005 | INCLUDE | Two CCHD-negative positives: one noncritical CHD and one other condition. |
| R005 | Rosati 2005 | INCLUDE | One CCHD false positive; alternative etiology incompletely reported. |
| R006 | Meberg 2008 | INCLUDE | 281 non-CHD positives: 55 pneumonia/septicemia, 54 TTN, 6 PPHN, 6 pneumothorax, 5 aspiration, 8 miscellaneous, 147 transitional. |
| R008 | de-Wahl Granelli 2009 | INCLUDE | 69 CCHD false positives: 4 other CCHD, 10 mild CHD, 6 PPHN, 8 transition, 10 infection, 7 pulmonary, 24 normal. |
| R035 | Hoke 2002 | INCLUDE | 53 CCHD-negative abnormal screens; at least 1 PPHN, 39 healthy and 13 insufficiently described in recovered extraction. |
| R012 | Ruangritnamchai 2007 | INCLUDE | 3 SpO2<95; 2 CCHD, 1 CCHD-negative; alternative diagnosis not reported. |
| R013 | Turska-Kmiec 2012 | INCLUDE | 14 non-CCHD positives: 8 transition, 1 ASD, 2 intrauterine infection, 3 pneumonia. |
| — | Kochilas 2013 | INCLUDE | Failed-screen cohort eligible; clinical breakdown of remaining non-CCHD failures insufficiently reported. |
| R015 | Zuppa 2015 | INCLUDE | 3 PO positives; individual alternative diagnoses not adequately resolved. |
| R041 | Zhao 2014 | INCLUDE | Large Chinese cohort; reported extraction: 41 PPHN, 23 pulmonary disease, 10 infection, 106 noncritical CHD, 214 healthy among pulse-ox CCHD false positives. |
| R029 | Tsao 2023 | INCLUDE | 114 CCHD false positives: 58 respiratory, 41 other CHD, 2 sepsis, 3 other disease, 10 no disease. |
| R032 | Majani 2025 | INCLUDE | 34 CCHD false positives: 5 noncritical CHD, 10 respiratory, 11 infection, 8 normal. |
| — | Gaonkar 2024 | INCLUDE | 65 positive; 4 CCHD, 26 RDS, 9 PPHN, 26 study-defined false positives/no qualifying diagnosis. |
| — | Jain 2022 | INCLUDE | 120 without cardiac defect among hypoxemic infants: 67 sepsis, 16 PPHN, 14 MAS, 9 severe asphyxia, 2 pneumothorax, 12 normal. |
| — | Murni 2022 | INCLUDE | 10 positive; 8 CCHD; 1 small ASD and 1 PFO among CCHD-negative. |
| R028 | Janjua/Study authors 2022 | INCLUDE | Population eligible; CAN-CCHD breakdown incomplete. |
| R031 | Abu Lehyah 2025 | INCLUDE | 20,482 screened; 752 failed; 102 PPHN and 145 noncardiac abnormalities reported; internal-category overlap flag. |
| — | Huang 2022 | INCLUDE | 44,147 births; 27 POX-positive, 20 CHD; 7 non-CHD without adequate diagnosis breakdown. |
| — | Nuntnarumit 2018 | INCLUDE | 10,603 healthy newborns; approximately 1 false positive; alternative diagnosis not reported. |
| — | Garg 2013 | INCLUDE | New Jersey program; 49 failed; among 30 investigations triggered solely by POX, 3 CCHD and 17 other diagnoses/findings. |
| — | Eltahlawi 2025 | EXCLUDE PRIMARY / RETAIN CONTEXT | Mixed/enriched tertiary population without separable routine well-baby denominator: includes neonates born in or transferred to 10 university hospitals and emergency-incubator screening; 23% failed screens and 42% mortality among positives. Rich descriptive data, but incompatible with primary population denominator. |
| — | Minocha 2018 | EXCLUDE PRIMARY | Referral/enriched population: neonates already referred for suspected CHD, not a screening denominator. |
| R070 | Van Naarden Braun 2017 | EXCLUDE PRIMARY / RETAIN NICU | NICU-only cohort. |
| R074 | Manja 2015 | EXCLUDE PRIMARY / RETAIN NICU | NICU-only cohort. |
| — | Hu 2016 | EXCLUDE PRIMARY / RETAIN NICU | NICU-only cohort. |
| — | Uygur 2019 | EXCLUDE PRIMARY | Eligible newborn population and valid POX screening, but full-text review does not provide an extractable diagnosis/outcome/no-diagnosis numerator among CCHD-negative failed POX screens. |
| R049 | Hamilcikan 2018 | INCLUDE | 4,518 newborns; 9 CCHD false positives in post-24h group; 6 noncritical CHD and 3 significant noncardiac pathology. |
| R055 | Taksande 2013 | INCLUDE / MIXED-POPULATION FLAG | 2,110 newborns from postnatal ward and NICU; at least 1 CCHD-negative failure plus noncritical CHD after repeat; sensitivity flag. |
| R048 | Taksande 2017 | INCLUDE REPORT / OVERLAP PENDING | Same-centre update; 4,926 newborns; possible cumulative extension of R055. Do not pool independently until dates resolved. |
| R051 | Banait 2020 | EXCLUDE PRIMARY | Regional CCHD registry/era comparison; cannot identify extractable CCHD-negative failed-screen denominator/outcomes. |
| R056 | de-Wahl Granelli 2005 | EXCLUDE PRIMARY | Case-control/method-development sample assembled from normal newborns and referred CCHD cases; not screening cohort. |
| R054 | Arvind 2022 | COMPANION / NO INDEPENDENT COHORT | Reanalysis of same 19,009-newborn cohort reported by Saxena 2015; retain companion information but no independent denominator. |
| R050 | Dilli 2019 | EXCLUDE PRIMARY | 4,888 multicentre newborns; 42 POX positives and 5 screen-detected CCHD (PPV 11.9%), yielding 37 CCHD-negative failed screens. Full text reports overall echo categories but not their distribution within failed screens, so the CAN-CCHD numerator/no-diagnosis category cannot be extracted. |

## Current nominal ledger status
This is a report-level working count, not yet a count of unique quantitative cohorts.
- INCLUDE or INCLUDE-with-flag reports: 41
- EXCLUDE PRIMARY or EXCLUDE PRIMARY / RETAIN CONTEXT reports: 9
- EXCLUDE PRIMARY / RETAIN NICU reports: 3
- MAYBE reports: 0
- CONDITIONAL / SUPPORTING reports: 1
- COMPANION / NO INDEPENDENT COHORT reports: 1
- Total nominal reports represented in ledger: 55

These counts intentionally do not add the historical anonymous checkpoint of 18; all totals must be derived only from named rows in this ledger. `MAYBE = 0` refers only to the 55 nominal reports currently reconstructed, not to the unreconciled remainder of the historical 156-report Phase 4 universe.

## Cohort-overlap register
- Birmingham: Singh 2014 and Henderson 2022 have partial temporal overlap (approximately Apr-Jul 2013); retain both reports but resolve unique cohort contribution before pooling.
- PulseOx: Ewer 2011 and Ewer 2012 are companion reports of the same cohort; primary quantitative contribution should come from the best report while companion data may supplement extraction.
- Meberg: 2008 and 2009 reports require companion/overlap adjudication.
- Saxena/Arvind: Arvind 2022 explicitly re-analyses the 19,009-newborn Saxena 2015 cohort; do not count as independent cohorts.
- Taksande: 2013 (n=2,110) and 2017 (n=4,926) originate from the same centre with near-identical methods; 2017 is an “update work”. Treat as potential cumulative extension until study dates prove independence.

## Next reconciliation tasks
1. Reconstruct the remaining 101 reports from the historical 156-report Phase 4 universe into this nominal ledger; do not infer their status from the old aggregate counts.
2. Assign canonical corpus IDs to every dash-ID row above.
3. Recover the nominal identities of the historical 18-study checkpoint and deduplicate against this ledger.
4. Resolve all overlap clusters before any pooled denominator/numerator is produced.
5. Convert this markdown ledger to a structured extraction table once Phase 4 nominal reconciliation reaches saturation.
