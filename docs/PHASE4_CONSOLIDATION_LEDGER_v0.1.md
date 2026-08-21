# CAN-CCHD Phase 4 Consolidation Ledger v0.1

Status: WORKING / RESTART-NATIVE MASTER RECONCILIATION
Date: 2026-08-21
Branch: `phase4-consolidation`

## Binding provenance boundary

This Phase 4 ledger belongs exclusively to the **August 2026 restarted systematic review**.

The pre-existing CAN-CCHD Browser Agent application, including `data/processed/can_cchd_agent.db`, legacy `records`, `studies`, `screening_decisions`, `eligibility_decisions`, and any other historical app tables, is `LEGACY_HISTORICAL_ONLY` and cannot supply scientific membership or adjudication data to this ledger.

Binding firewall: `RESTART_LEGACY_DATA_FIREWALL.md`.

Current restart report inventory: `PHASE45_RESTART_REPORT_MASTER_v0.1.md`.

Membership/reconstruction method: `PHASE4_MEMBERSHIP_RECONCILIATION.md`.

## Provenance audit result

The Rxxx lineage is restart-native:

- R001–R132 were already present in the restart public-corpus workbooks through `CAN-CCHD_Public_Corpus_v0.6.xlsx`.
- The restart v0.7 manifest explicitly states base v0.6 = 132 raw reports and adds R133–R145 as 13 new regional reports, for a logical total of 145.
- Those artifacts predate the later diagnostic inspection of the legacy SQLite database.
- Therefore the later SQLite inspection did not introduce any Rxxx report identity into the restarted review.
- Independently verified non-R additions are tracked as NRxxx in `PHASE45_RESTART_REPORT_MASTER_v0.1.md` with explicit restart-native provenance.

A temporary diagnostic workflow read the legacy SQLite only to determine whether it contained the missing restart corpus artifact. It did not. No exported legacy data were committed or merged. The workflow was removed, temporary PR #4 was closed without merge, and the local exported ZIP was deleted.

## Historical count correction

The earlier working statements based on a historical `156 Nxxx` Phase 4 queue are retained only as historical audit context. They are not used as the binding denominator for closing the restarted review because the exact normalization artifact behind those IDs is unavailable and cannot be safely reconstructed from the legacy app database.

No future `x/156` claim should be used as the primary completion metric unless the restart-native artifact itself is recovered and independently validated.

## Governance rules

- Bibliographic membership must originate from restart-native search/export/reconciliation artifacts or independently reverified citation chasing.
- Unit of report-level tracking: unique bibliographic report.
- Quantitative unit: unique cohort; companion/overlapping reports are linked and never blindly summed.
- Primary denominator: CCHD-negative failed screens.
- Primary outcome: clinically actionable non-CCHD diagnosis among CCHD-negative failed screens.
- Preserve separate categories: actionable CAN-CCHD; transitional/non-actionable physiology; explicitly healthy/no diagnosis; diagnosis not reported/not ascertained.
- NICU-only cohorts are excluded from the primary meta-analysis and retained for secondary/sensitivity analysis.
- Mixed nursery/NICU cohorts are sensitivity-flagged unless separable.
- Absence of reported alternative diagnosis is not equivalent to healthy.
- A calculable CCHD false-positive count alone is insufficient unless diagnosis, outcome, management, or explicit no-diagnosis information is available in that group.
- Reports with zero CCHD-negative failed screens may remain in study-selection accounting but cannot contribute to the CAN-CCHD proportion.

## Canonical tranche files

- `PHASE4_TRANCHE_R016_R025.md`
- `PHASE4_TRANCHE_R033_R052_R065.md`
- `PHASE4_TRANCHE_R038_R047.md`
- `PHASE4_TRANCHE_R077_R085.md`
- `PHASE4_TRANCHE_R086_R096.md`
- `PHASE4_TRANCHE_R097_R115.md`
- `PHASE4_TRANCHE_R116_R132.md`

Other report-level decisions are preserved in this branch history and the restart report master.

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
- R101 Singh & Chen: denominator-definition flag; 156 significant noncardiac diagnoses among study-defined true positives.
- R102 Turkey 2025: 301 positive; sepsis, pneumonia, polycythaemia and TTN categories require mutual-exclusivity QA.
- R125 SIBEN: extractable site-level units; site overlap audit required.
- R128 Brazil: 10 positive, no CCHD; 1 ASD, 7 PFO, 2 normal.
- R130 Colombia 2025: 42 positive, no CCHD; 29 noncritical CHD detected; early-screen/actionability flags.
- R135 Salih 2018: 55 CCHD false positives; 28 had other pathology.

## Cohort-overlap register

- Birmingham: Singh 2014 / Henderson 2022 partial temporal overlap.
- PulseOx: Ewer 2011 / Ewer 2012 companion reports.
- Meberg 2008 / 2009 companion/overlap.
- Saxena / Arvind same 19,009-newborn cohort; Saxena excluded primary under strict criterion 6; Arvind companion/non-independent.
- Taksande 2013 / 2017 possible cumulative extension.
- El Bakry R141 / R145 same enriched cohort.
- R101 Cambridge/Rosie distinct from Birmingham.
- Shanghai R116 / R117 overlap 2019–2021; neither contributes primary denominator because POX-only CCHD-negative outcomes are not separable.
- R125 SIBEN site units require overlap audit against separate publications.
- R040 Prudhoe belongs to North-East UK historical program context.
- R045 Miller 2016 overlaps earlier Wisconsin SHINE 2013 report.
- NR005 / NR006 represent the same Hainan 2019–2021 provincial program and are not independent quantitative cohorts.

## Active QA flags before pooling

1. Complete the restart-native report-master closing reconciliation waves.
2. Resolve R101 denominator convention.
3. Resolve R099 PPHN/sepsis overlap.
4. Complete R100 cardiac lesion classification.
5. Verify R102 mutual exclusivity.
6. Resolve R108 transitional PDA coding.
7. Audit R125 site-level overlap.
8. Resolve R126 abstract/detail discrepancy.
9. Preserve R127 altitude heterogeneity.
10. Freeze R128 PFO/transitional coding.
11. Freeze R130 lesion-level actionability/early timing.
12. Freeze R018 PFO/transitional coding.
13. Resolve R021 PDA/anomalous pulmonary venous connection classification.
14. Preserve R022 lost-to-echo / non-actionable distinctions.
15. Freeze R023 noncritical-CHD actionability.
16. Resolve incomplete classifications in R020 and R039 without equating missing diagnosis to healthy.
17. Reconstruct R045 Wisconsin SHINE report cluster.
18. Continue strict criterion-6 QA on all older INCLUDE reports.

## Next step

Continue the report-master completeness audit using **restart-native sources only**:

1. reconcile the native PubMed PMID export against R001–R145 + NRxxx;
2. reconcile Cochrane/Saganski/van Vliet primary references;
3. reconcile regional/LILACS/SciELO/IMEMR ledgers;
4. identify any post-v0.7 citation-chasing reports not yet assigned R/NR identity;
5. freeze the bibliographic report master after two independent zero-new-report closing waves;
6. recompute terminal Phase 4 decisions from that master;
7. proceed to structured Phase 5 extraction.