# CAN-CCHD Phase 4.5 Restart-Native Report Master v0.2

Date: 2026-08-21
Status: WORKING MASTER / PUBMED NATIVE WAVE INCORPORATED / REGIONAL CLOSING WAVE PENDING
Branch: `phase4-consolidation`

## Scope and firewall

This master contains only evidence identities recovered from the **August 2026 restarted systematic review**. The legacy Browser Agent SQLite database is excluded by `RESTART_LEGACY_DATA_FIREWALL.md` and contributes no scientific membership, eligibility decision, numerator, denominator or diagnosis.

## Current resolved bibliographic inventory

- Restart public-corpus reports: **R001–R145 = 145 reports**.
- Verified restart-native non-R reports: **NR001–NR043 = 43 reports**.
- **Resolved report master v0.2 = 188 bibliographic reports**.
- Additional unresolved native PubMed occurrence: **PMID 22984710 = 1**, not assigned a report ID and not included in the 188 until its identity is recovered.

`188` is a report-inventory count. It is not an eligible-study count and not a unique quantitative-cohort count.

## NR001–NR006 — review/reference and non-PubMed reconciliation deltas

| ID | Identity | Phase 4 disposition |
|---|---|---|
| NR001 | Donia & Tolba 2016 — *Use of early pulse oximetry in the detection of cardiac lesions among asymptomatic term newborns* | CONDITIONAL / SUPPORTING |
| NR002 | Gamhewage et al. 2021 — Sri Lanka tertiary-hospital POX screening cohort, N=8,718 | INCLUDE |
| NR003 | Zayachnikova et al. 2020 — Volgograd/Russia POX accuracy cohort, N=20,527 | EXCLUDE PRIMARY / RETAIN ACCURACY CONTEXT |
| NR004 | Gunaratne et al. 2021 — Sri Lanka POX vs clinical examination cohort, N=5,435 | EXCLUDE PRIMARY / RETAIN ACCURACY CONTEXT |
| NR005 | Chen et al. 2023 — English-language Hainan dual-index provincial program report | EXCLUDE PRIMARY / RETAIN PROGRAM CONTEXT |
| NR006 | Zhang et al. 2023 — Chinese-language Hainan program report | COMPANION / NO INDEPENDENT COHORT vs NR005 |

Gamhewage and Gunaratne are distinct reports/cohorts and must never be bibliographically merged.

## NR007–NR043 — native PubMed 81-PMID deltas

These 37 identities were absent from R001–R145 but were recovered from the restart-native PubMed PMID export. Full occurrence-level reconciliation is stored in `PHASE45_NATIVE_PUBMED_81_RECON.md`.

| ID | PMID | Identity | Phase 4 disposition |
|---|---:|---|---|
| NR007 | 34531289 | Williams et al. 2021 — *Newborn Pulse Oximetry for Infants Born Out-of-Hospital* | INCLUDE / denominator-convention flag |
| NR008 | 26746119 | Narayen et al. 2016 — *Pulse Oximetry Screening for Critical Congenital Heart Disease after Home Birth and Early Discharge* | INCLUDE / numerator-discrepancy QA flag |
| NR009 | 32504134 | Tekgündüz et al. 2021 — high-altitude oxygen saturation/perfusion-index screening; PDA prediction | INCLUDE / altitude + partial ascertainment + PDA actionability flags |
| NR010 | 33605861 | Taksande & Jameel 2021 CCHD review | EXCLUDE PRIMARY / citation context |
| NR011 | 39477714 | 2024 NICU cardiac stabilization/resuscitation review | EXCLUDE PRIMARY |
| NR012 | 27530240 | Ismail, Cawsey & Ewer 2017 — *Newborn pulse oximetry screening in practice* | EXCLUDE PRIMARY / context |
| NR013 | 27603536 | Ewer 2016 — POX screening medical-aspects review | EXCLUDE PRIMARY / context |
| NR014 | 32499387 | Martin et al. 2020 — updated POX screening strategies/expert panel | EXCLUDE PRIMARY / context |
| NR015 | 30733239 | Methemoglobinemia identified by POX screening — case report | EXCLUDE PRIMARY |
| NR016 | 33073011 | Saudi national CCHD screening implementation/program report | EXCLUDE PRIMARY / RETAIN CONTEXT |
| NR017 | 29404717 | Antenatally diagnosed/known-CCHD neonatal cohort | EXCLUDE PRIMARY |
| NR018 | 24877491 | Single CCHD case report | EXCLUDE PRIMARY |
| NR019 | 26369369 | van Vliet et al. 2016 newborn CCHD screening review | EXCLUDE PRIMARY |
| NR020 | 27468253 | Engel & Kochilas 2016 POX screening review | EXCLUDE PRIMARY |
| NR021 | 26800085 | POX performance/accuracy study in infants with known CCHD | EXCLUDE PRIMARY |
| NR022 | 29379160 | Paranka et al. 2018 — altitude impact on CCHD screening | EXCLUDE PRIMARY / RETAIN ALTITUDE CONTEXT |
| NR023 | 35244731 | Provider attitudes to proposed CCHD screening algorithm changes | EXCLUDE PRIMARY |
| NR024 | 23381095 | Ewer 2013 POX/CCHD screening review | EXCLUDE PRIMARY |
| NR025 | 25601984 | Pflugeisen et al. 2015 — POX newborn heart-screening QI time series | EXCLUDE PRIMARY / RETAIN IMPLEMENTATION-QI CONTEXT |
| NR026 | 34150354 | CCHD detection in screening era — case report | EXCLUDE PRIMARY |
| NR027 | 40792335 | 2025 neonatal oxygen-saturation/altitude reference-values study | EXCLUDE PRIMARY |
| NR028 | 41540907 | POX vs arterial saturation bias by race/ethnicity in neonatal/cardiac ICU | EXCLUDE PRIMARY |
| NR029 | 20523077 | Hoffman 2011 rationale/advocacy article | EXCLUDE PRIMARY / context |
| NR030 | 41553481 | Cor triatriatum dexter neonatal hypoxemia case series | EXCLUDE PRIMARY |
| NR031 | 32985395 | Rao et al. 2020 Albuquerque altitude screening cohort | EXCLUDE PRIMARY / RETAIN ALTITUDE CONTEXT |
| NR032 | 36580978 | CCHD screening state-mandate / nurse-supervisor implementation survey | EXCLUDE PRIMARY |
| NR033 | 23918890 | US CCHD POX cost-effectiveness model | EXCLUDE PRIMARY |
| NR034 | 35837363 | Majani et al. 2022 Tanzania Pulse Oximetry Study protocol/preliminary results | COMPANION / NO INDEPENDENT COHORT vs R032 |
| NR035 | 33072951 | POX values in newborns with known CCHD on ICU admission at altitude | EXCLUDE PRIMARY |
| NR036 | 37918940 | Hasan et al. 2023 broader at-risk-neonate/ML prospective cohort | EXCLUDE PRIMARY / context |
| NR037 | 28149925 | ML/echocardiography method study for coarctation detection | EXCLUDE PRIMARY |
| NR038 | 32411491 | Hemoglobin Sunshine Seth case report | EXCLUDE PRIMARY |
| NR039 | 17015513 | Tennessee Task Force / implementation strategy report | EXCLUDE PRIMARY |
| NR040 | 23298328 | Healthy-newborn altitude oxygen-saturation reference-value study | EXCLUDE PRIMARY |
| NR041 | 41994208 | Optical cerebral hemodynamics in neonates with known CHD | EXCLUDE PRIMARY |
| NR042 | 23594685 | Georgia hospital practices/feasibility survey | EXCLUDE PRIMARY |
| NR043 | 28285866 | TAPVR neonatal case report | EXCLUDE PRIMARY |

## PubMed native-wave outcome

Native PubMed export: **81 occurrences**.

- 43 mapped to existing Rxxx reports.
- 37 mapped to new resolved NR007–NR043 reports.
- 1 remains `UNRESOLVED_NATIVE_PMID_IDENTITY`: PMID **22984710**.

No scientific disposition is assigned to PMID 22984710 until identity verification. It is not counted in the 188-report master.

## New high-value primary reports from the native PubMed wave

### NR007 Williams 2021

3,019 newborns; 3 CCHD detected; 12 false-positive cases had other pathologies. Retain field-vs-algorithm denominator flag and perform overlap audit against other out-of-hospital programs.

### NR008 Narayen 2016

3,059 screened; 32 false-positive screens; clinically important alternate conditions reported. Retain numerator-discrepancy flag. Current study dates precede the later POLAR cohort and do not show temporal overlap.

### NR009 Tekgündüz 2021

501 neonates at high altitude; 21 positive screens; no CCHD; 9 PDA among positives. Remaining 12 are not fully characterized. Retain altitude, partial-ascertainment and PDA-actionability flags.

## Completed independent closing wave

`PHASE45_CLOSING_WAVE1_REVIEW_RECON.md` documents completion of the Cochrane 2018, Saganski 2024 and van Vliet 2024 reference reconciliation with no remaining unresolved primary bibliographic identity from those sources.

## Remaining Phase 4.5 work before master freeze

1. Run independent LILACS/BVS + SciELO + IMEMR/regional reconciliation against R001–R145 + NR001–NR043.
2. Audit any Google Scholar/citation-chasing identities documented after v0.7 but not yet assigned R/NR IDs.
3. Attempt recovery of PubMed identity `22984710`; if impossible, document whether it is an export corruption/invalid identifier rather than a report.
4. Require a final zero-new-primary closing wave after all source-specific reconciliations.
5. Only then freeze the bibliographic report master and recompute final Phase 4 dispositions.
6. Resolve cohort non-independence separately before quantitative pooling.

## Canonical files

- `RESTART_LEGACY_DATA_FIREWALL.md`
- `PHASE45_CLOSING_WAVE1_REVIEW_RECON.md`
- `PHASE45_NATIVE_PUBMED_81_RECON.md`
- `PHASE4_CONSOLIDATION_LEDGER_v0.1.md`

This v0.2 supersedes v0.1 for current report-master accounting while preserving v0.1 as audit history.