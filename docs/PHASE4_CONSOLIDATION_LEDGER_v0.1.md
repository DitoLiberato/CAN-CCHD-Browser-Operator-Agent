# CAN-CCHD Phase 4 Consolidation Ledger v0.1

Status: WORKING / NEAR NOMINAL SATURATION
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
- Reports with zero CCHD-negative failed screens are retained for PRISMA/accounting but cannot contribute to the CAN-CCHD proportion.

## Historical Phase 4 checkpoint
Historical universe = 156 reports (49 initially `include`, 107 `maybe`). A prior anonymous checkpoint of 18 eligible reports is not mechanically added; all current totals derive from named reports.

## Canonical tranche files
- `PHASE4_TRANCHE_R016_R025.md`
- `PHASE4_TRANCHE_R033_R052_R065.md`
- `PHASE4_TRANCHE_R038_R047.md`
- `PHASE4_TRANCHE_R077_R085.md`
- `PHASE4_TRANCHE_R086_R096.md`
- `PHASE4_TRANCHE_R097_R115.md`
- `PHASE4_TRANCHE_R116_R132.md`

## Current nominal Phase 4 status
- INCLUDE / INCLUDE-with-flag reports: 70
- EXCLUDE PRIMARY / RETAIN CONTEXT or NICU reports: 74
- COMPANION / NO INDEPENDENT COHORT reports: 4
- CONDITIONAL / SUPPORTING reports: 1
- MAYBE among adjudicated reports: 0
- Total nominal reports represented: 149 / 156 (95.5%)
- Remaining unreconciled reports: 7

These are report-level counts, not unique quantitative cohort counts. Site-level units within multi-site reports are tracked separately for extraction without inflating report counts.

## Newly consolidated residual block R033 + R052-R065
- R033 Abu Jarir 2026 Qatar: INCLUDE. 68,150 live births; 8 screen-detected CCHD and 26 CCHD-false-positive infants with non-cardiac diagnoses; PPHN most frequent. Exact mutually exclusive diagnostic subcategories pending.
- R052 Bulbul 2024 Lebanon: EXCLUDE PRIMARY / ZERO ELIGIBLE DENOMINATOR. 900 term well-babies; no positive POS at birth or 24 h.
- R053 Yao 2026 Ghana: INCLUDE / INCOMPLETE-ASCERTAINMENT FLAG. 5,725 screened; 29 failed; two died before echo. Among 27 evaluated: 9 CCHD, 10 non-CCHD CHD, 8 no CHD on echo. Confirmed CCHD-negative denominator = 18; lesion-level actionability pending; two deaths remain unclassified.
- R057 Thangaratinam 2012: EXCLUDE PRIMARY / systematic review.
- R058 Plana/Cochrane 2018: EXCLUDE PRIMARY / systematic review.
- R059 2013 review: EXCLUDE PRIMARY.
- R060 Canadian position statement: EXCLUDE PRIMARY / guidance.
- R061 van Vliet 2023 review: EXCLUDE PRIMARY.
- R062 2024 systematic review: EXCLUDE PRIMARY.
- R063 Kumar 2025 review: EXCLUDE PRIMARY.
- R064 Ting 2026 US impact study: EXCLUDE PRIMARY / RETAIN POLICY CONTEXT; no failed-screen clinical-yield cohort.
- R065 Studer 2014 provider survey: EXCLUDE PRIMARY / clearly ineligible.

## High-information primary-study anchors already consolidated
- R009 Riede 2010: 40 CCHD false positives = 15 PPHN, 13 sepsis, 12 healthy.
- R017 Jawin 2015: 13/13 CCHD-negative positives had significant non-cardiac disease (2 sepsis, 11 respiratory).
- R019 POPSICLe: 1 CCHD-negative final fail = neonatal sepsis.
- R020 POLAR: 221 CCHD false positives; 134 noncardiac illness.
- R023 Morocco: 10 CCHD-negative failures = 5 noncritical CHD, 1 PPHN, 2 sepsis, 2 normal.
- R024 Gopalakrishnan: 13 CCHD-negative = 8 sepsis/congenital pneumonia, 2 PPHN, 3 transitional circulation.
- R025 Flórez-Muñoz: 3 CCHD-negative = 1 pulmonary hypertension, 2 healthy/discharged.
- R039 Bradshaw: 8 CCHD-negative; 4 noncritical CHD, one confirmed no CHD, three not fully ascertained.
- R043 Oakley: 7 CCHD-negative = 3 significant noncritical CHD + 4 respiratory/sepsis.
- R099 Tekleab: 56 persistent fails, no CCHD; 10 PPHN (2 also sepsis), 11 PDA, 2 ASD, 33 clinically unremarkable.
- R100 New Zealand: 48 failed; 37 significant pathology, 11 no pathology.
- R101 Singh & Chen: 360 algorithm-positive vs 189 study-defined true-positive; 156 significant noncardiac diagnoses.
- R102 Turkey 2025: 301 positive; 101 sepsis, 16 pneumonia, 32 polycythaemia, 52 TTN; mutual-exclusivity flag.
- R125 SIBEN: directly extractable site units (San Luis 4/4 CCHD-negative required O2; Rosario final positive severe TTN, NICU, O2 5 days).
- R128 Brazil: 10 positive, no CCHD; 1 ASD, 7 PFO, 2 normal.
- R130 Colombia 2025: 42 positive, no CCHD; 29 noncritical CHD detected; early-screen/actionability flags.
- R135 Salih 2018: 55 CCHD false positives; 28 had other pathology.

## Cohort-overlap register
- Birmingham: Singh 2014 / Henderson 2022 partial temporal overlap.
- PulseOx: Ewer 2011 / Ewer 2012 companion reports.
- Meberg 2008 / 2009 companion/overlap.
- Saxena / Arvind same 19,009-newborn cohort; Saxena now excluded primary under strict criterion 6, Arvind companion/non-independent.
- Taksande 2013 / 2017 possible cumulative extension.
- El Bakry R141 / R145 same enriched cohort.
- R101 Cambridge/Rosie distinct from Birmingham.
- Shanghai R116 / R117 overlap 2019-2021; neither contributes primary denominator because POX-only CCHD-negative outcomes are not separable.
- R125 SIBEN site units require overlap audit against separate publications.
- R040 Prudhoe belongs to North-East UK historical program context.
- R045 Miller 2016 overlaps earlier Wisconsin SHINE 2013 report; do not pool blindly.

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
15. R020 disposition of remaining false positives not characterized as noncardiac illness.
16. R039 three failed screens without further diagnostic work-up.
17. R043 actionability of significant noncritical CHD lesions.
18. R045 Wisconsin SHINE report-cluster reconstruction.
19. R033 exact alternative-diagnosis breakdown among 26 Qatar false positives.
20. R053 Ghana: actionability of 10 non-CCHD CHD; 8 echo-negative infants clinically unclassified; two pre-echo deaths excluded from confirmed CCHD-negative denominator.
21. Continue strict criterion-6 QA on older INCLUDE rows.

## Next reconciliation tasks
1. Identify and adjudicate the final 7 reports by set difference between the historical 156-report Phase 4 universe and this ledger/tranche set; likely post-R145/unmapped additions.
2. Assign canonical IDs to any remaining dash-ID rows/post-R145 records.
3. Resolve overlap clusters before pooled estimates.
4. Freeze actionability coding for non-critical CHD, transitional physiology, management-only outcomes, and diagnosis-not-ascertained.
5. Convert ledger/tranches to a structured extraction table after nominal Phase 4 saturation.
