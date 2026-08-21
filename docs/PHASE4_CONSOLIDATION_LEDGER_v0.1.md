# CAN-CCHD Phase 4 Consolidation Ledger v0.1

Status: WORKING / NORMALIZED-MEMBERSHIP RECONCILIATION REQUIRED
Date: 2026-08-21
Branch: `phase4-consolidation`

## Critical QA amendment — 2026-08-21

The previous report-level countdown `149/156 (95.5%); 7 remaining` is **withdrawn as a formal Phase 4 closure metric**.

Reason: the historical Phase 4 universe of 156 was created after normalization/deduplication of the 327-record raw corpus and is tracked by normalized IDs (`Nxxx`). This ledger was reconstructed primarily from raw/public report IDs (`Rxxx`) plus non-PubMed reports. Rxxx membership is not one-to-one with the Nxxx Phase 4 universe, and several initially no-ID reports were later assigned Rxxx IDs. Therefore raw-report counts can both include records outside the historical 156 and double-count identity-reconciled reports.

The individual study adjudications below and in tranche files remain valid report-level evidence. Global Phase 4 counts will be frozen only after completion of `PHASE4_MEMBERSHIP_RECONCILIATION.md`, which creates a one-row-per-Nxxx crosswalk.

## Historical normalized Phase 4 facts

- Raw corpus before normalization: 327 records.
- Phase 3 routing: 49 `include`, 111 `maybe`, 9 `separate_analysis`.
- Active Phase 4 full-text universe: 49 `include` + 107 `maybe` = **156 normalized records**.
- Four maybe-routed normalized records not in the active FT-resolvable queue: `N228`, `N265`, `N298`, `N299`.
- Nine `separate_analysis` records remain outside the primary 156.

## Governance rules

- Formal Phase 4 accounting unit: normalized Phase 4 member (`Nxxx`).
- Report-level provenance unit: source report, linked to `raw_record_id` (`Rxxx`) whenever available.
- Quantitative unit: unique cohort; companion/overlapping reports are linked and never blindly summed.
- Primary denominator: CCHD-negative failed screens.
- Primary outcome: any clinically actionable non-CCHD diagnosis among CCHD-negative failed screens.
- Preserve separate categories: actionable CAN-CCHD; transitional/non-actionable physiology; explicitly healthy/no diagnosis; diagnosis not reported/not ascertained.
- NICU-only cohorts are excluded from primary meta-analysis and retained for secondary/sensitivity analysis.
- Mixed nursery/NICU cohorts are sensitivity-flagged unless separable.
- Absence of reported alternative diagnosis is not equivalent to healthy.
- A calculable CCHD false-positive count alone is insufficient unless diagnosis, outcome, management, or explicit no-diagnosis information is available in that group.
- Reports with zero CCHD-negative failed screens may remain in study-selection accounting but cannot contribute to the CAN-CCHD proportion.

## Canonical reconciliation file

- `PHASE4_MEMBERSHIP_RECONCILIATION.md` — binding gate before Phase 4 closure.

## Canonical tranche files

- `PHASE4_TRANCHE_R016_R025.md`
- `PHASE4_TRANCHE_R033_R052_R065.md`
- `PHASE4_TRANCHE_R038_R047.md`
- `PHASE4_TRANCHE_R077_R085.md`
- `PHASE4_TRANCHE_R086_R096.md`
- `PHASE4_TRANCHE_R097_R115.md`
- `PHASE4_TRANCHE_R116_R132.md`

## Report-level adjudication progress

Extensive report-level full-text adjudication has been completed across the Rxxx corpus and non-PubMed reports. These decisions are retained in tranche files and prior ledger history. They are not converted into a formal x/156 completion percentage until mapped to the normalized Nxxx universe.

Examples of raw-ID reconciliation already completed:
- Garg 2013 = R086.
- Kochilas/Minnesota 2013 = R087; R088 is companion/reanalysis.
- Singh & Chen 2022 = R101.
- Gaonkar 2024 = R104.
- Jain 2022 = R105.
- Eltahlawi 2025 = R106.
- Murni 2022 = R109.
- Hu 2016 NICU = R118.

## High-information primary-study anchors already adjudicated

- R009 Riede 2010: 40 CCHD false positives = 15 PPHN, 13 sepsis, 12 healthy.
- R017 Jawin 2015: 13/13 CCHD-negative positives had significant non-cardiac disease (2 sepsis, 11 respiratory).
- R019 POPSICLe: 1 CCHD-negative final fail = neonatal sepsis.
- R020 POLAR: 221 CCHD false positives; 134 noncardiac illness.
- R023 Morocco: 10 CCHD-negative failures = 5 noncritical CHD, 1 PPHN, 2 sepsis, 2 normal.
- R024 Gopalakrishnan: 13 CCHD-negative = 8 sepsis/congenital pneumonia, 2 PPHN, 3 transitional circulation.
- R025 Flórez-Muñoz: 3 CCHD-negative = 1 pulmonary hypertension, 2 healthy/discharged.
- R039 Bradshaw: 8 CCHD-negative; 4 noncritical CHD, one confirmed no CHD, three not fully ascertained.
- R043 Oakley: 7 CCHD-negative = 3 significant noncritical CHD + 4 respiratory/sepsis.
- R086 Garg/New Jersey: 49 failed; among 30 evaluations attributable solely to POX, 3 CCHD and 17 other diagnoses/findings.
- R089 Johnson: sole final CCHD-negative failed screen had PPHN.
- R093 Cawsey: 2/2 CCHD-negative failed homebirth screens had significant respiratory disease.
- R099 Tekleab: 56 persistent fails, no CCHD; 10 PPHN (2 also sepsis), 11 PDA, 2 ASD, 33 clinically unremarkable.
- R100 New Zealand: 48 failed; 37 significant pathology, 11 no pathology.
- R101 Singh & Chen: 360 algorithm-positive vs 189 study-defined true-positive; 156 significant noncardiac diagnoses.
- R102 Turkey 2025: 301 positive; 101 sepsis, 16 pneumonia, 32 polycythaemia, 52 TTN; mutual-exclusivity flag.
- R125 SIBEN: directly extractable site units (San Luis 4/4 CCHD-negative required O2; Rosario final positive severe TTN, NICU, O2 5 days).
- R128 Brazil: 10 positive, no CCHD; 1 ASD, 7 PFO, 2 normal.
- R130 Colombia 2025: 42 positive, no CCHD; 29 noncritical CHD detected; early-screen/actionability flags.
- R133 Abu Jarir/Qatar: 26 CCHD false positives with noncardiac diagnoses; PPHN predominant.
- R135 Salih 2018: 55 CCHD false positives; 28 had other pathology.

## Cohort-overlap register

- Birmingham: Singh 2014 / Henderson 2022 partial temporal overlap.
- PulseOx: Ewer 2011 / Ewer 2012 companion reports.
- Meberg 2008 / 2009 companion/overlap.
- Saxena / Arvind same 19,009-newborn cohort; Saxena excluded primary under strict criterion 6; Arvind companion/non-independent.
- Taksande 2013 / 2017 possible cumulative extension.
- El Bakry R141 / R145 same enriched cohort.
- R101 Cambridge/Rosie distinct from Birmingham.
- Shanghai R116 / R117 overlap 2019-2021; neither contributes primary denominator because POX-only CCHD-negative outcomes are not separable.
- R125 SIBEN site units require overlap audit against separate publications.
- R040 Prudhoe belongs to North-East UK historical program context.
- R045 Miller 2016 overlaps earlier Wisconsin SHINE 2013 report.

## Active QA flags before pooling

1. Reconstruct the exact 156-row Nxxx membership crosswalk before any final Phase 4 count.
2. R101 denominator convention.
3. R099 PPHN/sepsis overlap.
4. R100 lesion-level cardiac classification.
5. R102 mutual exclusivity.
6. R108 transitional PDA without follow-up.
7. R125 site-level overlap audit.
8. R126 abstract/detail discrepancy.
9. R127 altitude heterogeneity.
10. R128 PFO/transitional coding.
11. R130 lesion-level actionability/early timing.
12. R018 PFO/transitional coding.
13. R021 PDA/anomalous pulmonary venous connection classification.
14. R022 one lost-to-echo positive and predominantly non-actionable findings.
15. R023 noncritical-CHD actionability.
16. R020 disposition of remaining false positives not characterized as noncardiac illness.
17. R039 three failed screens without further diagnostic work-up.
18. R043 actionability of significant noncritical CHD lesions.
19. R045 Wisconsin SHINE report-cluster reconstruction.
20. R133 exact alternative-diagnosis breakdown among 26 Qatar false positives.
21. R053 Ghana: actionability of non-CCHD CHD; echo-negative infants clinically unclassified; two pre-echo deaths outside confirmed CCHD-negative denominator.
22. Continue strict criterion-6 QA on older INCLUDE rows.

## Next step

Recover/reconstruct the normalized Phase 4 membership list and populate `PHASE4_MEMBERSHIP_RECONCILIATION.md`. Only then identify genuinely unmatched terminal records, adjudicate them, recompute INCLUDE/EXCLUDE/other counts from the 156 Nxxx rows, and close Phase 4.