# CAN-CCHD Phase 4 Consolidation Ledger v0.1

Status: WORKING / NOT YET FINAL
Date: 2026-08-21
Branch: `phase4-consolidation`

## Purpose
This ledger is the canonical reconstruction point for Phase 4 full-text adjudication after work was split across chats. It supersedes free-text chat counts once reports are reconciled by canonical corpus ID.

## Governance rules
- Unit of tracking: report, linked to canonical `raw_record_id` whenever available.
- Quantitative unit: unique cohort; companion/overlapping reports are linked and never blindly summed.
- Primary denominator: CCHD-negative failed screens.
- Primary outcome: any clinically actionable non-CCHD diagnosis among CCHD-negative failed screens.
- Preserve separate categories: actionable CAN-CCHD; transitional/non-actionable physiology; explicitly healthy/no diagnosis; diagnosis not reported.
- NICU-only cohorts are excluded from the primary meta-analysis per protocol, but retained for possible secondary/sensitivity analysis.
- Mixed nursery/NICU cohorts are flagged for sensitivity analysis unless a separable well-baby denominator is available.
- Absence of reported alternative diagnosis is not equivalent to healthy.
- A calculable CCHD false-positive count alone is insufficient for inclusion unless diagnosis, outcome, management, or explicit no-diagnosis information is available in that group.

## Historical Phase 4 checkpoint
The prior chat established a Phase 4 universe of 156 reports: 49 initially routed as `include` and 107 as `maybe`. A historical checkpoint recorded 18 reports already adjudicated as eligible, but their complete nominal list was not preserved. Therefore all current totals are derived only from named reports reconstructed in this ledger/tranche files; the historical 18 are never mechanically added.

## Canonical tranche files
- `PHASE4_TRANCHE_R077_R085.md`
- `PHASE4_TRANCHE_R086_R096.md`
- `PHASE4_TRANCHE_R097_R115.md`

These tranche files preserve report-level adjudication and QA details. Earlier rows R001-R076 and R133-R145 were reconstructed in this master ledger during prior passes.

## Current nominal Phase 4 status through R115 plus regional R133-R145
Report-level count, not yet unique quantitative cohorts:
- INCLUDE / INCLUDE-with-flag reports: 52
- EXCLUDE PRIMARY / RETAIN CONTEXT or NICU reports: 46
- COMPANION / NO INDEPENDENT COHORT reports: 4
- CONDITIONAL / SUPPORTING reports: 1
- MAYBE among adjudicated reports: 0
- Total nominal reports represented: 103 / 156
- Remaining unreconciled reports: 53

## Important canonical-ID assignments completed in R097-R115
The following reports were already represented under dash IDs and have now been mapped to corpus IDs without increasing the nominal count:
- R101 = Singh & Chen 2022
- R104 = Gaonkar 2024
- R105 = Jain 2022
- R106 = Eltahlawi 2025
- R109 = Murni 2022

## High-information additions from R097-R115
- R099 Tekleab 2019: 56 persistent failed screens, no CCHD; 10 PPHN (2 also sepsis), 11 PDA, 2 ASD, 33 clinically unremarkable after negative echo.
- R100 Cloete/New Zealand 2019: 16,644 screened; 48 failed; 37 significant pathology, 11 no pathology; national report indicates 33 respiratory/infectious and one SVT, with cardiac classification to reconcile before freezing the exact CCHD-negative denominator.
- R101 Singh & Chen 2022: 23,614 screened; 360 protocol-positive after second screen, 171 reclassified clinically well/normal on repeat, 189 study-defined true positive; 156 significant non-cardiac diagnoses. Denominator-definition flag remains active.
- R102 Sero et al. 2025: 301 positive; non-cardiac morbidities include 101 sepsis, 16 congenital pneumonia, 32 polycythaemia, 52 TTN; mutual exclusivity must be verified.
- R108 Shah 2026: 6 persistent failures at 6 h; 2 CCHD, 4 early PDA/transitional cardiac findings without follow-up. Include with transitional-period/actionability flag.

## Cohort-overlap register
- Birmingham: Singh 2014 and Henderson 2022 have partial temporal overlap (approximately Apr-Jul 2013); retain both reports but resolve unique cohort contribution before pooling.
- PulseOx: Ewer 2011 and Ewer 2012 are companion reports of the same cohort; use the best report for quantitative contribution and companion data only to supplement extraction.
- Meberg: 2008 and 2009 are companion/overlap reports; no blind summation.
- Saxena/Arvind: Arvind 2022 re-analyses the 19,009-newborn Saxena 2015 cohort; no independent denominator.
- Taksande: 2013 and 2017 same-centre update cluster; potential cumulative extension until dates prove independence.
- El Bakry Egypt/UAE: R141 and R145 same 2014-2016 enriched cohort; no independent pooling.
- R101 Singh & Chen is a distinct Cambridge/Rosie cohort, not the Birmingham R014/R027 cohort; retain local-companion audit only.

## Active QA flags before pooling
1. R101: pre-specify denominator convention (360 algorithm-positive vs 189 clinician-confirmed true-positive) before meta-analysis.
2. R099: PPHN/sepsis overlap; do not add overlapping diagnoses.
3. R100: lesion-level cardiac classification needed to freeze exact CCHD-negative denominator.
4. R102: verify whether non-cardiac categories are mutually exclusive.
5. R108: four PDA findings are transitional-period findings without follow-up; do not automatically classify as definite actionable non-critical CHD.
6. Revisit all older INCLUDE rows under the strict criterion-6 rule where only false-positive counts, but no clinical outcome/no-diagnosis data, had originally been available. Huang 2022 and Nuntnarumit 2018 were already corrected to EXCLUDE PRIMARY during the R077-R085 QA pass.

## Next reconciliation tasks
1. Reconstruct the remaining 53 reports from the 156-report Phase 4 universe, beginning with R116 onward and any unreconciled earlier IDs.
2. Assign canonical corpus IDs to any remaining dash-ID rows.
3. Resolve overlap clusters before generating any pooled denominator/numerator.
4. Freeze an actionability coding dictionary for non-critical CHD, transitional physiology, and management-only outcomes before final extraction.
5. Convert the markdown ledger/tranches into a structured extraction table after nominal Phase 4 saturation.
