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
- `PHASE4_TRANCHE_R116_R132.md`

## Current nominal Phase 4 status through R145, with R116-R132 now adjudicated
- INCLUDE / INCLUDE-with-flag reports: 57
- EXCLUDE PRIMARY / RETAIN CONTEXT or NICU reports: 57
- COMPANION / NO INDEPENDENT COHORT reports: 4
- CONDITIONAL / SUPPORTING reports: 1
- MAYBE among adjudicated reports: 0
- Total nominal reports represented: 119 / 156
- Remaining unreconciled reports: 37

These are report-level counts, not unique quantitative cohort counts. Site-level units within a multi-site implementation report (e.g., R125 SIBEN) are tracked separately for quantitative extraction but do not increase the report count.

## Canonical-ID assignments completed
- R101 = Singh & Chen 2022
- R104 = Gaonkar 2024
- R105 = Jain 2022
- R106 = Eltahlawi 2025
- R109 = Murni 2022
- R118 = Hu 2016 NICU-only

## High-information additions from R097-R115
- R099 Tekleab 2019: 56 persistent failed screens, no CCHD; 10 PPHN (2 also sepsis), 11 PDA, 2 ASD, 33 clinically unremarkable after negative echo.
- R100 Cloete/New Zealand 2019: 16,644 screened; 48 failed; 37 significant pathology, 11 no pathology; national report indicates 33 respiratory/infectious and one SVT, with cardiac classification to reconcile before freezing exact CCHD-negative denominator.
- R101 Singh & Chen 2022: 23,614 screened; 360 protocol-positive after second screen, 171 reclassified clinically well/normal on repeat, 189 study-defined true positive; 156 significant non-cardiac diagnoses. Denominator-definition flag remains active.
- R102 Sero et al. 2025: 301 positive; 101 sepsis, 16 congenital pneumonia, 32 polycythaemia, 52 TTN; mutual exclusivity must be verified.
- R108 Shah 2026: 6 persistent failures at 6 h; 2 CCHD, 4 early PDA/transitional cardiac findings without follow-up.

## High-information additions from R116-R132
- R125 Sola/SIBEN 2020 contains directly extractable site-level implementation units. San Luis: >1,400 screened, 4 hypoxemic screen-detected infants, none CCHD, all required supplemental oxygen. Rosario: one final positive after repeat testing, normal echo, severe TTN, NICU admission and supplemental oxygen for 5 days. Treat site units separately and audit overlap before pooling.
- R126 Atitlán-Gil 2020 Hidalgo: 1,748 screened; 29 positive; detailed flow reports 14 simple/noncritical CHD + 3 CCHD among screen positives, leaving 12 without CHD on echo. Use detailed screen-positive flow; abstract/detail discrepancy flag active.
- R127 González-Andrade 2018 Quito: 963 term newborns; 53 positive; no CCHD; at least 23 ASD and 6 PDA+ASD. High-altitude subgroup flag (2,820 m).
- R128 Witkowski 2024 Brazil: 5,667 screened; 10 positive; no CCHD; 1 ostium secundum ASD, 7 PFO, 2 normal echo. Actionability coding for PFO/transitional physiology pending.
- R130 Rendón Díez 2025 Colombia: 609 neonates; 42 pulse-ox positive; no CCHD; exploratory analysis reports 29 noncritical CHD detected by screening. Early-screen median 15.4 h and lesion-level actionability flags active.

## Cohort-overlap register
- Birmingham: Singh 2014 and Henderson 2022 have partial temporal overlap; resolve unique cohort contribution before pooling.
- PulseOx: Ewer 2011 and Ewer 2012 are companion reports of the same cohort.
- Meberg: 2008 and 2009 are companion/overlap reports.
- Saxena/Arvind: Arvind 2022 re-analyses the 19,009-newborn Saxena 2015 cohort.
- Taksande: 2013 and 2017 same-centre update cluster; possible cumulative extension.
- El Bakry Egypt/UAE: R141 and R145 same 2014-2016 enriched cohort.
- R101 Singh & Chen is a distinct Cambridge/Rosie cohort, not the Birmingham R014/R027 cohort.
- Shanghai: R116 Ma 2023 (2017-2021, whole Shanghai) and R117 Tian 2025 (2019-2023, south Shanghai) overlap during 2019-2021 and share program/investigators; neither currently contributes to the primary CAN-CCHD denominator because POX-only CCHD-negative outcomes are not separable.
- R125 SIBEN contains multiple site-level implementation units; check each against separate publications before pooling.

## Active QA flags before pooling
1. R101 denominator convention: 360 algorithm-positive vs 189 clinician-confirmed true-positive.
2. R099 PPHN/sepsis overlap.
3. R100 lesion-level cardiac classification before exact CCHD-negative denominator.
4. R102 mutual exclusivity of non-cardiac categories.
5. R108 transitional PDA findings without follow-up.
6. R125 site-level extraction and overlap audit.
7. R126 abstract/detail discrepancy in CCHD count among positives.
8. R127 altitude heterogeneity.
9. R128 PFO/transitional physiology coding.
10. R130 lesion-level actionability and early-screen timing.
11. Continue strict criterion-6 QA on older INCLUDE rows; Huang 2022 and Nuntnarumit 2018 were already corrected to EXCLUDE PRIMARY during R077-R085.

## Next reconciliation tasks
1. Reconstruct the remaining 37 reports, prioritising unreconciled earlier IDs and any post-R145 additions that formed the historical 156-report Phase 4 universe.
2. Assign canonical corpus IDs to any remaining dash-ID rows.
3. Resolve overlap clusters before any pooled estimates.
4. Freeze actionability coding for non-critical CHD, transitional physiology, and management-only outcomes.
5. Convert ledger/tranches to structured extraction table after nominal Phase 4 saturation.
