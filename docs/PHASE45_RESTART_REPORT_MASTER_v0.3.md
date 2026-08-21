# CAN-CCHD Phase 4.5 Restart-Native Report Master v0.3

Date: 2026-08-21
Status: WORKING MASTER / CITATION-CHASING WAVE INCORPORATED / SATURATION NOT YET ACHIEVED
Branch: `phase4-consolidation`

## Scope and firewall

This master contains only evidence identities from the August 2026 restarted systematic review or independently reverified citation-chasing sources. The legacy Browser Agent/database is `LEGACY_HISTORICAL_ONLY` under `RESTART_LEGACY_DATA_FIREWALL.md` and contributes no study membership, eligibility decision, numerator, denominator, diagnosis, overlap, PRISMA count, or meta-analysis value.

## Current resolved bibliographic inventory

- Restart public-corpus reports: **R001–R145 = 145 reports**.
- Restart-native non-R reports before Closing Wave 4: **NR001–NR043 = 43 reports**.
- Closing Wave 4 citation-chasing additions: **NR044–NR048 = 5 reports**.
- **Current resolved bibliographic inventory = 193 reports**.
- Additional unresolved native PubMed occurrence: **PMID 22984710 = 1**, not assigned an NR ID and not counted among the 193.

`193` is a bibliographic report-inventory count. It is not an eligible-primary-study count and not a unique quantitative-cohort count.

## Inherited report identities

All R001–R145 and NR001–NR043 identities, dispositions and QA flags from `PHASE45_RESTART_REPORT_MASTER_v0.2.md` are carried forward unchanged unless explicitly amended below.

Canonical supporting files:
- `PHASE45_NATIVE_PUBMED_81_RECON.md`
- `PHASE45_CLOSING_WAVE1_REVIEW_RECON.md`
- `PHASE45_CLOSING_WAVE3_REGIONAL_RECON.md`
- `PHASE45_CLOSING_WAVE4_CITATION_CHASE.md`
- `PHASE4_CONSOLIDATION_LEDGER_v0.1.md`
- `RESTART_LEGACY_DATA_FIREWALL.md`

## NR044–NR048 — Closing Wave 4 additions

| ID | Identity | Phase 4 disposition | Core note |
|---|---|---|---|
| NR044 | Kishore Kumar et al. 2017 — Bangalore, *Neonatology Today* | **INCLUDE / target-definition + lesion-mapping flag** | 22,601 well newborns; 14 persistent failed screens; 3 pulmonary diagnoses requiring treatment (PPHN, TTN, congenital pneumonia + sepsis); remaining cardiac lesions require re-mapping to locked CCHD definition. |
| NR045 | Walsh 2011 — Middle Tennessee | **EXCLUDE PRIMARY / RETAIN IMPLEMENTATION CONTEXT** | 14,564 asymptomatic infants; 112 conventional false positives, but no complete clinical outcome distribution for the 112 CCHD-negative positives. Criterion 6 not met. |
| NR046 | Song et al. 2021 — POX + cardiac auscultation, CHD target | **EXCLUDE PRIMARY / RETAIN COMBINED-SCREEN CONTEXT** | 3,327 neonates; 276 abnormal POX results; clinical outcomes among POX-positive/CHD-negative infants not extractable for CAN-CCHD. |
| NR047 | Bin-Nun et al. 2021 — Israel historical/embedded Shaare Zedek cohort | **EXCLUDE PRIMARY / RETAIN IMPLEMENTATION CONTEXT** | 19,763 screened; 48 positive; 1 true-positive CCHD; 47 CCHD-negative positives not clinically classified. Criterion 6 not met. |
| NR048 | Adaboh et al. 2026 — Ghana implementation report | **COMPANION / NO INDEPENDENT COHORT** | Same Ghana program as quantitative R053 Yao 2026; implementation report explicitly points to separate quantitative manuscript. |

## Saturation state

Closing Wave 4 found a new independent primary report (NR044). Therefore the saturation counter was reset.

**Current saturation counter: 0 consecutive zero-new-independent-primary waves after the latest new primary discovery.**

Phase 4.5 cannot be frozen yet.

## Required next two independent saturation waves

### Wave A — Recent/current 2024–2026 literature

Search specifically for newborn CCHD pulse-ox screening reports with failed-screen/false-positive/non-CCHD/secondary-diagnosis language, emphasizing newly published, ahead-of-print, regional and non-PubMed reports.

A report counts as a new independent primary only if it contains a distinct screening population/cohort and is not already represented by R001–R145 or NR001–NR048.

### Wave B — Seed/author/backward-forward citation chasing

Use independent seed families:
- NR044 Kishore Kumar/Bangalore;
- NR007 Williams out-of-hospital;
- NR008 Narayen/home birth;
- NR009 Tekgündüz/altitude;
- high-yield anchors such as R009 Riede, R010 Ewer, R017 Jawin, R020 POLAR, R024 Gopalakrishnan, R029 Tsao, R099 Tekleab, R101 Singh & Chen and R102 Turkey 2025.

Backward/forward chasing should prioritize direct primary reports and not recursively add reviews/guidelines merely because they cite the topic.

## Saturation rule

- If Wave A finds **zero** new independent primary reports, counter = 1.
- If Wave B independently finds **zero** new independent primary reports, counter = 2 and the bibliographic master may be frozen, subject to the unresolved PMID handling below.
- If either wave finds a new independent primary report, assign the next NR ID, adjudicate it, incorporate it into the master, reset counter to 0, and repeat two independent zero waves.

## Unresolved PMID 22984710

This occurrence remains in the restart-native 81-PMID export but its bibliographic identity has not been safely recovered. It must not be guessed.

Before final freeze, make one final direct NCBI/PubMed identity attempt. If still unrecoverable, preserve it as `UNRESOLVED_NATIVE_EXPORT_OCCURRENCE` and explicitly state that it is not counted as a resolved bibliographic report. It may be classified as an export/identifier anomaly only with evidence.

## Freeze requirements after saturation

Once the two-zero-wave rule is achieved:

1. freeze the report master version;
2. recompute report-level Phase 4 dispositions from the master, not from historical `156` counts;
3. reconcile all companion/overlap clusters separately;
4. derive the **unique quantitative cohort** list;
5. perform strict criterion-6 QA on all INCLUDE rows;
6. create the structured Phase 5 extraction dataset.

## Important cohort/overlap clusters already requiring resolution

- Birmingham: Singh 2014 / Henderson 2022 partial temporal overlap.
- PulseOx: Ewer 2011 / Ewer 2012 companion reports.
- Meberg 2008 / 2009 companion/overlap.
- Taksande 2013 / 2017 possible cumulative extension.
- Saxena / Arvind same 19,009-newborn cohort; no independent double counting.
- El Bakry R141 / R145 same enriched cohort.
- Shanghai R116 / R117 overlap 2019–2021.
- R125 SIBEN site-level units require overlap audit.
- Wisconsin/out-of-hospital cluster: Miller 2016 and related SHINE reports; Williams/Narayen require program/date comparison but are not automatically companions.
- Majani R032 definitive / NR034 preliminary protocol report.
- Ghana R053 Yao definitive / NR048 Adaboh implementation companion.

This v0.3 supersedes v0.2 for current report-inventory accounting while retaining v0.2 as audit history.