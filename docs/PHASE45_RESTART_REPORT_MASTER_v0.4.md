# CAN-CCHD Phase 4.5 Restart-Native Report Master v0.4

Date: 2026-08-21
Status: WORKING MASTER / RECENT + TYPO/GREY EXPANSION INCORPORATED / SATURATION COUNTER 0
Branch: `phase4-consolidation`

## Scope and firewall

This master contains only reports from the August 2026 restarted systematic review or independently reverified restart-era citation/grey-literature chasing. `RESTART_LEGACY_DATA_FIREWALL.md` remains binding: the abandoned Browser Agent/database contributes no scientific membership, decision, numerator, denominator, diagnosis, overlap, PRISMA count or quantitative value.

## Current resolved bibliographic inventory

- Restart public-corpus reports: **R001–R145 = 145 reports**.
- Non-R reports through Closing Wave 4: **NR001–NR048 = 48 reports**.
- Recent/typo/grey expansion: **NR049–NR066 = 18 reports**.
- **Resolved restart-native bibliographic inventory = 211 reports.**
- Additional unresolved native PubMed occurrence: **PMID 22984710 = 1**, not assigned an NR ID and not counted among the 211.

`211` is a bibliographic report count. It is not an eligible-primary-study count and not a unique quantitative-cohort count.

## Inherited identities

All R001–R145 and NR001–NR048 identities, dispositions and QA flags from `PHASE45_RESTART_REPORT_MASTER_v0.3.md` remain in force unless explicitly amended by later QA.

## NR049–NR066 additions

| ID | Report / identity | Disposition | Key note |
|---|---|---|---|
| NR049 | Nathawani et al. 2024, Apollo Medicine | EXCLUDE PRIMARY / criterion 6 | 1,117 eligible; 259 study-defined suspected by SpO2 pathway; only 6 CHD; CCHD-negative clinical outcomes not classified. |
| NR050 | Neelannavar et al. 2024, JCDR 15(6):741–744 | **INCLUDE** | Representative `NEELANNAVAR_BAGALKOT_400`; 400 screened, 7 positive, authors report 4 CCHD, 2 ASD, 1 normal. Lesion/actionability flag. |
| NR051 | Talawar et al. 2024, JCDR 15(6):738–740 | COMPANION | Same `NEELANNAVAR_BAGALKOT_400` cohort. |
| NR052 | Mirji et al. 2024, Research Journal of Medical Sciences 18(7):144–147 | COMPANION | Same N=400 Bagalkot cohort. |
| NR053 | Vinaykumar et al. 2024, *Correlates of Pulse Oximetry Saturation in Asymptomatic Newborn Babies* | COMPANION | Same N=400 Bagalkot research program. |
| NR054 | Neelannavar 2017 BLDE thesis | COMPANION / GREY PROVENANCE | Source-level description of same 400 cohort; four CCHD, two ASD, one normal among 7 positives. |
| NR055 | Bhojak et al. 2024, JCDR 15(3):127–135 | EXCLUDE PRIMARY / criterion 6 | Clinical/POX accuracy report; no defensible CCHD-negative failed-screen outcome distribution recovered. |
| NR056 | Soni et al. 2025, Maharashtra | EXCLUDE PRIMARY / criterion 6 | N=100, four POX fails, but no clinical/echo disposition of failures. |
| NR057 | Santosh Kumar & Jaiswal 2021 | EXCLUDE PRIMARY / criterion 6 + derivative-text QA | No extractable failed-screen outcome distribution; wording/summary metrics strikingly duplicate Ahmed 2019 but cohort identity not assumed. |
| NR058 | Reddy & Devaraj 2018, Hyderabad | **INCLUDE** | N=800; one positive; ASD + VSD + pulmonary stenosis. Locked target/lesion mapping required. |
| NR059 | John et al. 2016, West Virginia | **INCLUDE** | 19 fails; 17 TTE; 7 CCHD; 10 confirmed CCHD-negative failures with nominal diagnoses; 2 failures without TTE unascertained. |
| NR060 | Mouledoux et al. 2017, Tennessee | EXCLUDE PRIMARY / criterion 6 | 232 failed staged algorithm, 51 true-positive CCHD; CCHD-negative outcomes not classified. |
| NR061 | Polanki et al. 2022, Tirupathi | EXCLUDE PRIMARY / criterion 6 | 14,400 screened, 45 positive, 30 CHD, 15 false positives without clinical diagnosis distribution. |
| NR062 | Ahmed 2019, Nellore observational report | **INCLUDE** | N=1,000; seven positive at 48–72 h; five cyanotic/CCHD-labelled, one acyanotic CHD + severe PPHN, one severe PPHN. Target mapping required. |
| NR063 | Ahmed 2019 comparative report | COMPANION | Same `AHMED_NELLORE_1000` study period/method as NR062. |
| NR064 | Lanker et al. 2014, Srinagar | **INCLUDE** | N=1,200; 3 fails; TGA, truncus, and one structurally normal heart. Echo-normal case is **not coded healthy**; alternative diagnosis not reported. |
| NR065 | Shah et al. 2015, Pravara/Loni | ZERO CCHD-NEGATIVE DENOMINATOR / retain context | N=700; four persistent positives: complete AVSD, TGA, TAPVC, coarctation. |
| NR066 | Siva et al. 2016, Chennai | ZERO CCHD-NEGATIVE DENOMINATOR / retain context | N=430; five positives: 3 HLHS, TGA, truncus. |

Full source-level details and decisions: `PHASE45_SATURATION_WAVE_A_AND_TYPO_GREY_RECON.md`.

## New cohort clusters

### `NEELANNAVAR_BAGALKOT_400`
- NR050 representative quantitative report
- NR051 companion
- NR052 companion
- NR053 companion
- NR054 thesis/grey provenance

One cohort contribution only.

### `AHMED_NELLORE_1000`
- NR062 representative quantitative report
- NR063 companion

One cohort contribution only.

## High-value new extraction anchors

### NR059 West Virginia
Confirmed CCHD-negative failed-screen denominator currently **10**, with nominal diagnoses including ASD, mild Ebstein/TR, VSD/PFO, PFO, PPHN + PDA, and pulmonary hypertension + bidirectional PDA. Two additional failed screens had no available TTE and remain unascertained, not silently added to the confirmed denominator.

### NR050 Bagalkot
Authors report seven positive screens: four CCHD, two ASD and one normal. Locked CCHD lesion definition and actionability rules govern the final numerator/denominator.

### NR062 Nellore
The final 48–72 h screen gives seven positives, including severe PPHN in two infants (one with acyanotic CHD). Do not rely on the paper's broad cyanotic/CCHD labels without lesion-level target reconciliation.

### NR064 Srinagar
One CCHD-negative failed screen had a structurally normal heart. This supports an `alternative diagnosis not reported / echo-normal` category, **not explicit healthy**.

## Saturation state

The attempted recent 2024–2026 wave and the typo/grey-literature expansion found multiple new independent primary reports.

**Current saturation counter = 0 consecutive zero-new-independent-primary waves after the latest discovery.**

Phase 4.5 is not frozen.

## Required restart of saturation test

### Zero Wave 1
Run a broad independent recall search using spelling variants, regional/grey sources, and diagnosis-oriented terms different from the searches that generated NR049–NR066. Reconcile every candidate against R001–R145 + NR001–NR066.

### Zero Wave 2
If Zero Wave 1 finds no new independent primary report, run independent backward/forward citation chasing from the new anchors NR050, NR058, NR059, NR062, NR064 plus established high-yield anchors. If it also finds zero new independent primary reports, counter reaches 2 and the bibliographic master may be frozen subject to final PMID handling.

Any new independent primary report resets the counter to 0.

## Outstanding native PMID

`PMID 22984710` remains `UNRESOLVED_NATIVE_EXPORT_OCCURRENCE` pending one final direct identity attempt before freeze. Do not guess or assign a scientific disposition without verified identity.

## Freeze sequence after two zero waves

1. Freeze the bibliographic report master.
2. Recompute report-level Phase 4 dispositions from the frozen master.
3. Apply strict criterion-6 QA to all INCLUDE rows.
4. Resolve companions and temporal/cohort overlaps.
5. Derive unique quantitative cohorts.
6. Start Phase 5 structured extraction.

## Canonical supporting files

- `RESTART_LEGACY_DATA_FIREWALL.md`
- `PHASE45_CLOSING_WAVE1_REVIEW_RECON.md`
- `PHASE45_NATIVE_PUBMED_81_RECON.md`
- `PHASE45_CLOSING_WAVE3_REGIONAL_RECON.md`
- `PHASE45_CLOSING_WAVE4_CITATION_CHASE.md`
- `PHASE45_SATURATION_WAVE_A_AND_TYPO_GREY_RECON.md`
- `PHASE4_CONSOLIDATION_LEDGER_v0.1.md`

This v0.4 supersedes v0.3 for current report-master accounting while preserving all prior versions as audit history.