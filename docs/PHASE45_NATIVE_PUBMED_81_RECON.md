# CAN-CCHD Phase 4.5 — Native PubMed 81-PMID Reconciliation

Date: 2026-08-21
Status: COMPLETE EXCEPT ONE UNRESOLVED NATIVE PMID IDENTITY
Source file: `pmid-criticalco-set (1).txt` (restart-native PubMed export)

## Summary

- Native PMID occurrences audited: **81/81**.
- Already represented by restart-native Rxxx reports: **43**.
- Newly resolved non-R PubMed bibliographic reports: **37**.
- New primary reports meeting Phase 4 clinical-yield eligibility: **3**.
- New primary/method/context reports excluded from primary CAN-CCHD synthesis: **11**.
- New secondary/review/survey/case-report records: **22**.
- New companion/preliminary report: **1**.
- Unresolved native PMID identity: **1** (`22984710`).

The counts above are bibliographic reconciliation counts, not unique quantitative cohorts.

## Reconciliation table

| PMID | Master ID | Native-wave class | Reconciliation note |
|---:|---|---|---|
| 33605861 | NR010 | `new_secondary_or_case` | Taksande & Jameel 2021 — Critical Congenital Heart Disease in Neonates: A Review Article. EXCLUDE PRIMARY / citation context. |
| 29494750 | R058 | `represented_R` |  |
| 39477714 | NR011 | `new_secondary_or_case` | Special considerations for stabilization/resuscitation of neonates with cardiac disease in NICU (2024). EXCLUDE PRIMARY. |
| 34531289 | NR007 | `new_primary_include` | Williams et al. 2021 — Newborn Pulse Oximetry for Infants Born Out-of-Hospital. INCLUDE / denominator-convention flag. |
| 34496777 | R119 | `represented_R` |  |
| 36815269 | R029 | `represented_R` |  |
| 27530240 | NR012 | `new_secondary_or_case` | Ismail, Cawsey & Ewer 2017 — Newborn pulse oximetry screening in practice. EXCLUDE PRIMARY / context. |
| 27603536 | NR013 | `new_secondary_or_case` | Ewer 2016 — Screening for Critical Congenital Heart Defects with Pulse Oximetry: Medical Aspects. EXCLUDE PRIMARY / context. |
| 39411017 | R131 | `represented_R` | Metadata correction: R131 PMID=39411017. |
| 34429338 | R026 | `represented_R` |  |
| 36699784 | R105 | `represented_R` |  |
| 32499387 | NR014 | `new_secondary_or_case` | Martin et al. 2020 — Updated Strategies for Pulse Oximetry Screening for Critical Congenital Heart Disease. EXCLUDE PRIMARY / context. |
| 27073996 | R077 | `represented_R` |  |
| 30733239 | NR015 | `new_secondary_or_case` | Ward 2019 — Congenital Methemoglobinemia Identified by Pulse Oximetry Screening. EXCLUDE PRIMARY. |
| 38308011 | R110 | `represented_R` |  |
| 33073011 | NR016 | `new_secondary_or_case` | Saudi Arabia national CCHD screening implementation/program article (2020). EXCLUDE PRIMARY / retain context. |
| 28939700 | R080 | `represented_R` |  |
| 33073018 | R125 | `represented_R` |  |
| 28672762 | R049 | `represented_R` |  |
| 29404717 | NR017 | `new_primary_exclude` | Antenatally diagnosed CCHD neonatal cohort. EXCLUDE PRIMARY. |
| 24877491 | NR018 | `new_secondary_or_case` | Single CCHD case report (2014). EXCLUDE PRIMARY. |
| 26369369 | NR019 | `new_secondary_or_case` | van Vliet et al. 2016 — review of newborn screening for CCHD. EXCLUDE PRIMARY. |
| 27468253 | NR021 | `new_secondary_or_case` | Engel & Kochilas 2016 — Pulse Oximetry Screening: A Review of Diagnosing Critical Congenital Heart Disease in Newborns. EXCLUDE PRIMARY. |
| 26800085 | NR022 | `new_primary_exclude` | Pulse oximetry performance/accuracy in infants with known CCHD. EXCLUDE PRIMARY. |
| 32504134 | NR009 | `new_primary_include` | Tekgündüz et al. 2021 — Oxygen saturation and perfusion index screening in neonates at high altitudes: can PDA be predicted? INCLUDE / altitude + partial-ascertainment + PDA-actionability flags. |
| 29379160 | NR023 | `new_primary_exclude` | Paranka et al. 2018 — The impact of altitude on screening for critical congenital heart disease. EXCLUDE PRIMARY / retain altitude context. |
| 23958775 | R087 | `represented_R` |  |
| 35244731 | NR024 | `new_secondary_or_case` | Providers' Attitudes to Proposed Changes in the Critical Congenital Heart Disease Screening Algorithm. EXCLUDE PRIMARY. |
| 23381095 | NR025 | `new_secondary_or_case` | Ewer 2013 — newborn pulse oximetry/CCHD screening review. EXCLUDE PRIMARY. |
| 39957234 | R106 | `represented_R` |  |
| 25601984 | NR026 | `new_primary_exclude` | Pflugeisen et al. 2015 — Quality improvement measures in pulse-oximetry newborn heart screening: a time series analysis. EXCLUDE PRIMARY / implementation-QI context. |
| 24037922 | R069 | `represented_R` |  |
| 31686645 | R034 | `represented_R` |  |
| 34150354 | NR028 | `new_secondary_or_case` | Critical Congenital Heart Disease Detection in the Screening Era: Do Not Neglect the Examination! EXCLUDE PRIMARY. |
| 29691284 | R072 | `represented_R` |  |
| 40792335 | NR029 | `new_primary_exclude` | Neonatal oxygen saturation/altitude reference-values study (2025). EXCLUDE PRIMARY. |
| 26746119 | NR008 | `new_primary_include` | Narayen et al. 2016 — Pulse Oximetry Screening for Critical Congenital Heart Disease after Home Birth and Early Discharge. INCLUDE / numerator-discrepancy QA flag. |
| 41540907 | NR030 | `new_primary_exclude` | Pulse oximetry and arterial saturation bias in neonates: retrospective analysis by race & ethnicity. EXCLUDE PRIMARY. |
| 22984710 | UNRESOLVED | `unresolved_identity` | Present in native PMID list; identity not recoverable from available native text/search. Do not guess or count as resolved report. |
| 20523077 | NR031 | `new_secondary_or_case` | Hoffman 2011 — rationale/advocacy for routine CCHD screening. EXCLUDE PRIMARY / context. |
| 25287457 | R089 | `represented_R` |  |
| 42299162 | R108 | `represented_R` |  |
| 41553481 | NR032 | `new_secondary_or_case` | Cor triatriatum dexter neonatal hypoxemia/failure case series (2026). EXCLUDE PRIMARY. |
| 41890244 | R033 | `represented_R` | Metadata correction: R033 PMID=41890244. |
| 32985395 | NR033 | `new_primary_exclude` | Rao et al. 2020 — Pulse oximetry screening for detection of congenital heart defects at 1646 m in Albuquerque, NM. EXCLUDE PRIMARY / altitude context. |
| 30332903 | R051 | `represented_R` |  |
| 36580978 | NR034 | `new_secondary_or_case` | Nurse supervisor/state mandate CCHD screening implementation survey. EXCLUDE PRIMARY. |
| 23677390 | R090 | `represented_R` |  |
| 23858425 | R086 | `represented_R` |  |
| 28043739 | R060 | `represented_R` |  |
| 23918890 | NR035 | `new_secondary_or_case` | US cost-effectiveness model for CCHD pulse-ox screening. EXCLUDE PRIMARY. |
| 35837363 | NR036 | `companion` | Majani et al. 2022 — Tanzania Pulse Oximetry Study research protocol and preliminary results. COMPANION / no independent cohort vs R032. |
| 19581492 | R111 | `represented_R` |  |
| 25058746 | R074 | `represented_R` |  |
| 38756257 | R104 | `represented_R` |  |
| 29580679 | R020 | `represented_R` |  |
| 33072951 | NR037 | `new_primary_exclude` | Pulse Oximetry Values in Newborns with Critical Congenital Heart Disease upon ICU Admission at Altitude. EXCLUDE PRIMARY. |
| 37918940 | NR038 | `new_primary_exclude` | Hasan et al. 2023 — machine learning identification of at-risk neonates in low-resource settings. EXCLUDE PRIMARY / context. |
| 16238542 | R005 | `represented_R` |  |
| 28149925 | NR039 | `new_primary_exclude` | Machine-learning/echocardiography method for coarctation detection. EXCLUDE PRIMARY. |
| 32411491 | NR040 | `new_secondary_or_case` | Hemoglobin Sunshine Seth case report. EXCLUDE PRIMARY. |
| 33072929 | R071 | `represented_R` |  |
| 17015513 | NR041 | `new_secondary_or_case` | Tennessee Task Force / implementation strategy report. EXCLUDE PRIMARY. |
| 23298328 | NR042 | `new_primary_exclude` | Healthy newborn altitude oxygen saturation reference-value study. EXCLUDE PRIMARY. |
| 31616201 | R099 | `represented_R` |  |
| 41101352 | R102 | `represented_R` |  |
| 28749481 | R070 | `represented_R` |  |
| 24768155 | R041 | `represented_R` |  |
| 41994208 | NR043 | `new_primary_exclude` | Optical cerebral hemodynamics in neonates with known CHD. EXCLUDE PRIMARY. |
| 28917066 | R068 | `represented_R` |  |
| 39997630 | R031 | `represented_R` |  |
| 28264208 | R091 | `represented_R` |  |
| 23594685 | NR044 | `new_secondary_or_case` | Georgia hospital practices/feasibility survey for CCHD screening. EXCLUDE PRIMARY. |
| 26360420 | R017 | `represented_R` |  |
| 27540721 | R118 | `represented_R` |  |
| 20195633 | R009 | `represented_R` |  |
| 19581259 | R112 | `represented_R` |  |
| 25241768 | R043 | `represented_R` |  |
| 31945047 | R100 | `represented_R` |  |
| 27499412 | R019 | `represented_R` |  |
| 28285866 | NR045 | `new_secondary_or_case` | TAPVR neonatal case report. EXCLUDE PRIMARY. |

## New primary inclusions

### NR007 — Williams et al. 2021

*Newborn Pulse Oximetry for Infants Born Out-of-Hospital* (PMID 34531289; DOI 10.1542/peds.2020-048785).

- 3,019 newborns, predominantly Plain (Amish/Mennonite) communities.
- Early 1–4 h and late 24–48 h screens.
- 3 CCHD detected.
- Twelve false-positive cases had other pathologies (including noncritical CHD, pulmonary disease or infection).
- **INCLUDE with denominator-convention flag** because field interpretation and strict algorithm interpretation differed.
- Cohort overlap with other out-of-hospital reports must be checked; do not automatically treat as Miller 2016 companion.

### NR008 — Narayen et al. 2016

*Pulse Oximetry Screening for Critical Congenital Heart Disease after Home Birth and Early Discharge* (PMID 26746119; DOI 10.1016/j.jpeds.2015.12.004).

- 3,625 eligible births; 3,090 consented; 3,059 screened.
- No CCHD detected by the screening cohort.
- 32 false-positive screens.
- Secondary extraction reports respiratory disease, infection/sepsis, noncritical CHD, other pathology and healthy infants among false positives.
- **INCLUDE**, but retain a numerator-discrepancy QA flag because later summary percentages do not perfectly reconcile with the category counts.
- Pilot dates Oct 2013–Oct 2014; later POLAR cohort dates Jul 2015–Dec 2016, so current evidence supports program lineage without temporal cohort overlap.

### NR009 — Tekgündüz et al. 2021

*Oxygen saturation and perfusion index screening in neonates at high altitudes: can PDA be predicted?* (PMID 32504134; DOI 10.1007/s00431-020-03698-1).

- 501 neonates >35 weeks.
- 21 positive screening tests; no CCHD.
- 9 screen-positive infants had PDA.
- The remaining 12 CCHD-negative positives are not sufficiently characterized in the abstract.
- **INCLUDE with altitude, partial-ascertainment and PDA-actionability flags**; the 12 uncharacterized infants remain diagnosis-not-reported unless full text resolves them.

## Important new exclusions / context reports

- **Paranka 2018 (PMID 29379160):** 6,109 infants; 65 positive screens; altitude-focused; no complete clinical classification of CCHD-negative failed screens → EXCLUDE PRIMARY / RETAIN ALTITUDE CONTEXT.
- **Pflugeisen 2015 (PMID 25601984):** 18,363 newborns; time-series/QI study; false-positive trend but no alternative-diagnosis classification → EXCLUDE PRIMARY / RETAIN IMPLEMENTATION-QI CONTEXT.
- **Rao 2020 (PMID 32985395):** 3,548 infants; 93 false positives at altitude; no clinical diagnosis/outcome distribution for those 93 → EXCLUDE PRIMARY / RETAIN ALTITUDE CONTEXT.
- **Majani 2022 (PMID 35837363):** research protocol/preliminary results of Tanzania Pulse Oximetry Study → COMPANION / PRELIMINARY REPORT relative to definitive R032 Majani 2025.

## Metadata corrections

- **R131**: PMID `39411017` (PMCID PMC11473077; DOI 10.47487/apcyccv.v5i3.366).
- **R033 Abu Jarir/Qatar**: PMID `41890244`.

## Unresolved native occurrence

### PMID 22984710

The PMID occurs in the native 81-PMID list, but its PubMed bibliographic identity could not be recovered from the currently accessible restart-native full-text export, File Library indexing, or external exact-PMID search. Search-engine hits for the number are unrelated identifiers and are not evidence of PubMed identity.

**Binding treatment:** retain as `UNRESOLVED_NATIVE_PMID_IDENTITY`; do not assign an NR ID, do not include or exclude scientifically, and do not count it as a resolved bibliographic report until identity is recovered from PubMed/NCBI or a verified native export.

## Closure rule for this source

The native PubMed 81-PMID reconciliation is scientifically complete for **80 resolved identities + 1 explicitly unresolved occurrence**. The source is not declared zero-pending until PMID 22984710 is resolved or formally documented as an export error/invalid identifier.

Next: incorporate NR007–NR045 into restart-native report master v0.2, then run the independent regional/LILACS/SciELO/IMEMR closing wave.