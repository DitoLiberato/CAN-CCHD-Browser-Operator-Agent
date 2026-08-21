# CAN-CCHD Phase 4 Consolidation Ledger v0.1

Status: WORKING / NOT YET FINAL
Date: 2026-08-21
Branch: `phase4-consolidation`

## Purpose
Canonical reconstruction point for Phase 4 full-text adjudication after work was split across chats. Free-text chat counts are superseded by named reports in this ledger and tranche files.

## Governance rules
- Unit of tracking: report, linked to canonical `raw_record_id` whenever available.
- Quantitative unit: unique cohort; companion/overlapping reports are linked and never blindly summed.
- Primary denominator: CCHD-negative failed screens.
- Primary outcome: any clinically actionable non-CCHD diagnosis among CCHD-negative failed screens.
- Preserve separate categories: actionable CAN-CCHD; transitional/non-actionable physiology; explicitly healthy/no diagnosis; diagnosis not reported.
- NICU-only cohorts are excluded from primary meta-analysis, retained for secondary/sensitivity.
- Mixed nursery/NICU cohorts are sensitivity-flagged unless separable.
- Absence of reported alternative diagnosis is not equivalent to healthy.
- A calculable CCHD false-positive count alone is insufficient unless diagnosis, outcome, management, or explicit no-diagnosis information is available in that group.

## Historical Phase 4 checkpoint
Historical universe = 156 reports (49 initially `include`, 107 `maybe`). A prior anonymous checkpoint of 18 eligible reports is not mechanically added; all current totals derive from named reports.

## Canonical tranche files
- `PHASE4_TRANCHE_R016_R025.md`
- `PHASE4_TRANCHE_R038_R047.md`
- `PHASE4_TRANCHE_R077_R085.md`
- `PHASE4_TRANCHE_R086_R096.md`
- `PHASE4_TRANCHE_R097_R115.md`
- `PHASE4_TRANCHE_R116_R132.md`

## Current nominal Phase 4 status
- INCLUDE / INCLUDE-with-flag reports: 68
- EXCLUDE PRIMARY / RETAIN CONTEXT or NICU reports: 64
- COMPANION / NO INDEPENDENT COHORT reports: 4
- CONDITIONAL / SUPPORTING reports: 1
- MAYBE among adjudicated reports: 0
- Total nominal reports represented: 137 / 156 (87.8%)
- Remaining unreconciled reports: 19

These are report-level counts, not unique quantitative cohort counts. Site-level units within multi-site reports are tracked separately for extraction without inflating report counts.

## High-information gap-tranche additions R016-R025
- R017 Jawin 2015: 15 positive; 2 CCHD; all 13 CCHD-negative positives had significant non-cardiac disease requiring hospitalisation/treatment (2 sepsis, 11 respiratory).
- R018 Özalkaya 2016: 7 positive; 6 CCHD; 1 CCHD-negative = PFO, transitional/non-actionable flag.
- R019 POPSICLe 2016: 2 failed; 1 CCHD, 1 neonatal sepsis.
- R020 POLAR 2018: 221 CCHD false positives; 134 noncardiac illness (31 infections, 88 respiratory pathology).
- R021 Panama: 16 positive; 1 CCHD; remaining 15 = 6 normal echo, 6 PDA, 3 anomalous pulmonary venous connections; lesion-classification flag.
- R022 Soto Torselli 2020: 11 positive; 10 echoes, 1 lost; no CCHD; mainly PFO/small noncritical findings, no important haemodynamic/clinical compromise.
- R023 Morocco 2020: 15 failed; 5 CCHD, 5 noncritical CHD, 5 false positives = 1 PPHN, 2 sepsis, 2 normal.
- R024 Gopalakrishnan 2021: 16 positive; 3 CCHD; CCHD-negative 13 = 8 sepsis/congenital pneumonia, 2 PPHN, 3 transitional circulation.
- R025 Flórez-Muñoz 2021: 4 positive; 1 TGA/CCHD; remaining 3 = 1 moderate pulmonary hypertension, 2 healthy/discharged.
- R016 Gómez-Rodríguez excluded under strict criterion 6: CCHD false-positive count is inferable but clinical classification of that group is not defensibly extractable.

## Gap-tranche additions R038-R047
- R039 Bradshaw 2012: 6,745 screened; 9 positive. One CCHD; four noncritical CHD (including dextrocardia with lobar pneumonia requiring NICU); one confirmed no CHD after evaluation; three positives had no further work-up. CCHD-negative denominator = 8, with diagnosis-not-ascertained flag for 3.
- R043 Oakley 2015: 6,329 screened; 14 low-saturation; 7 CCHD; among remaining 7, 3 significant noncritical CHD and 4 respiratory illness/sepsis. All low-saturation infants had identifiable pathology.
- R038 Vaidyanathan 2011 excluded: combined clinical + POX strategy, no isolated CCHD-negative failed-POX outcome cohort.
- R040 Prudhoe 2013 excluded from primary CAN-CCHD synthesis: strong detection study but no extractable final CCHD-negative failed-screen outcome denominator; North-East UK historical overlap/context flag.
- R044 Saxena 2015 QA-corrected to EXCLUDE PRIMARY under strict criterion 6: low specificity is discussed, but CCHD-negative POX positives are not clinically classified sufficiently for a defensible CAN-CCHD numerator.
- R045 Miller 2016 excluded primary / retain overlap context: 2013–2014 Wisconsin SHINE cohort has 16 failed, 3 CCHD detected; remaining failures incompletely classified. Overlaps earlier 2013 J Pediatr SHINE report with 2 sepsis + 1 CHD among 3 failures.
- R046 Patriciu 2017 excluded: CHD accuracy study without CCHD-negative failed-screen outcome classification.
- R047 Shahzad 2017 excluded: all-enrollee echo diagnostic study without usable clinical outcome classification among CCHD-negative test positives.

## Canonical-ID assignments completed
- R101 = Singh & Chen 2022
- R104 = Gaonkar 2024
- R105 = Jain 2022
- R106 = Eltahlawi 2025
- R109 = Murni 2022
- R118 = Hu 2016 NICU-only

## Other high-information recent additions
- R099 Tekleab: 56 persistent fails, no CCHD; 10 PPHN (2 also sepsis), 11 PDA, 2 ASD, 33 clinically unremarkable.
- R100 New Zealand: 48 failed; 37 significant pathology, 11 no pathology.
- R101 Singh & Chen: denominator-definition flag 360 algorithm-positive vs 189 study-defined true-positive; 156 significant noncardiac.
- R102 Turkey 2025: 301 positive; 101 sepsis, 16 pneumonia, 32 polycythaemia, 52 TTN; mutual-exclusivity flag.
- R125 SIBEN: site-level units. San Luis 4/4 CCHD-negative hypoxemic infants required O2; Rosario final positive = severe TTN, NICU, O2 5 days.
- R126 Hidalgo: 29 positive; detailed flow 14 noncritical CHD + 3 CCHD, 12 remaining no CHD on echo; abstract/detail discrepancy.
- R127 Quito: 53 positive, no CCHD; high-altitude flag.
- R128 Brazil: 10 positive, no CCHD; 1 ASD, 7 PFO, 2 normal.
- R130 Colombia 2025: 42 positive, no CCHD; 29 noncritical CHD detected; early-screen/actionability flags.

## Cohort-overlap register
- Birmingham: Singh 2014 / Henderson 2022 partial temporal overlap.
- PulseOx: Ewer 2011 / Ewer 2012 companion reports.
- Meberg 2008 / 2009 companion/overlap.
- Saxena / Arvind same 19,009-newborn cohort; R044 now excluded from primary CAN-CCHD synthesis and R054 remains companion/non-independent.
- Taksande 2013 / 2017 possible cumulative extension.
- El Bakry R141 / R145 same enriched cohort.
- R101 Cambridge/Rosie is distinct from Birmingham.
- Shanghai R116 / R117 overlap 2019-2021; neither contributes primary denominator because POX-only CCHD-negative outcomes are not separable.
- R125 SIBEN contains multiple site-level units; audit each against separate publications.
- R040 Prudhoe belongs to North-East UK historical program context and requires overlap audit against earlier Richmond-region work before any secondary use.
- R045 Miller 2016 overlaps earlier Wisconsin SHINE 2013 J Pediatr report; do not pool blindly.

## Active QA flags before pooling
1. R101 denominator convention.
2. R099 PPHN/sepsis overlap.
3. R100 lesion-level cardiac classification.
4. R102 mutual exclusivity.
5. R108 transitional PDA without follow-up.
6. R125 site-level overlap audit.
7. R126 abstract/detail discrepancy.
8. R127 altitude heterogeneity.
9. R128 PFO/transitional coding.
10. R130 lesion-level actionability/early timing.
11. R018 PFO/transitional coding.
12. R021 PDA/anomalous pulmonary venous connection classification.
13. R022 one lost-to-echo positive and predominantly non-actionable findings.
14. R023 noncritical-CHD actionability.
15. R020 disposition of 87 CCHD false positives without noncardiac illness reported in abstract.
16. R039 three failed screens without further diagnostic work-up.
17. R043 actionability of the three significant noncritical CHD lesions.
18. R045 Wisconsin SHINE report-cluster reconstruction.
19. Continue strict criterion-6 QA on older INCLUDE rows.

## Next reconciliation tasks
1. Reconstruct the remaining 19 reports. Known gaps now include R033, R052-R065 plus post-R145/unmapped reports; verify exact difference before adjudication.
2. Assign canonical IDs to remaining dash-ID rows/post-R145 records.
3. Resolve overlap clusters before pooled estimates.
4. Freeze actionability coding for non-critical CHD, transitional physiology, and management-only outcomes.
5. Convert ledger/tranches to structured extraction table after nominal Phase 4 saturation.
