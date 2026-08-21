# CAN-CCHD Phase 4.5 — Overlap and Non-Independence Resolution

Date: 2026-08-21
Status: TERMINAL COHORT-RELATIONSHIP AUDIT

Scope: the 73 reports with terminal status `INCLUDE_PRIMARY` in `PHASE45_TERMINAL_REPORT_STATUS_REGISTRY.md`.

This audit resolves bibliographic/report eligibility separately from quantitative independence. A report can remain eligible while not contributing a distinct main-analysis unit if its participants overlap another report.

## 1. Birmingham program — R014 Singh 2014 + R027 Henderson 2022

### Evidence

R014 Singh 2014:
- Birmingham Women's Hospital.
- Study period: **1 April 2010 to 31 July 2013**.
- 25,859 screened in the underlying screening cohort; 208 neonatal-unit admissions caused by positive pulse-ox screening.
- Detailed alternative-diagnosis information is available.

R027 Henderson 2022:
- Same Birmingham regional neonatal unit/program.
- Study period: **1 April 2013 to 31 March 2019**.
- 49,375 live births; 253 admissions caused by positive pulse-ox screening.
- 247/253 had a significant diagnosis requiring intervention; 6/253 were healthy/transitional; 22 CHD including 8 CCHD.

There is therefore **four months of participant-period overlap: April–July 2013**.

### Decision

Define one main-analysis program unit:

`U_BIRMINGHAM_R027_MAIN`

- Representative report: **R027 Henderson 2022**.
- Supporting/overlap report: **R014 Singh 2014**.
- R014 remains `INCLUDE_PRIMARY` at report level because it is clinically informative, but it does not create a second independent weight in the main synthesis.
- Sensitivity analysis: replace R027 with R014 to test dependence on representative-report choice.
- Do **not** sum R014 + R027 raw counts.

Reason for representative choice: R027 covers a longer/later period, explicitly evaluates the evolved routine program, and provides a nearly complete clinical outcome classification. Using both as independent estimates would double-count infants from April–July 2013.

## 2. Taipei program — R077 Tsao 2016 + R029 Tsao 2023

### Evidence

R077 pilot:
- 12 Taipei birthing facilities.
- **1 October 2013 to 31 March 2014**.
- 6,296 newborns screened; 16 failed; 5 CCHD.
- CCHD-negative failed screens include PDA, TTN, RDS and PPHN.

R029 extended program:
- Expanded Taipei program, 30 birthing facilities.
- **1 April 2014 to 30 June 2017**.
- 93,058 screened after prenatal-suspicion exclusions; 156 referred.

The extended program begins the day after the pilot period ends. There is **no temporal participant overlap**.

### Decision

Retain as two independent participant cohorts:

- `U_R077_TAIPEI_PILOT_2013_2014`
- `U_R029_TAIPEI_EXTENDED_2014_2017`

Assign a common `program_cluster_id = TAIPEI_POX_PROGRAM` for later sensitivity/cluster-robust analysis because protocol, investigators and facilities overlap institutionally, even though participants do not overlap.

## 3. Dutch home-birth / early-discharge program — NR008 + R020

### Evidence

NR008 POLS/Leiden feasibility cohort:
- Leiden region.
- **October 2013 to October 2014**.
- 3,059 screened.

R020 POLAR accuracy cohort:
- Larger Leiden–Amsterdam and surrounding regions.
- **July 2015 to December 2016**.
- 23,959 screened.

There is a clear temporal gap and the later cohort is an expanded implementation rather than the same participant set.

### Decision

Retain as two independent participant cohorts:

- `U_NR008_POLS_2013_2014`
- `U_R020_POLAR_2015_2016`

Assign common `program_cluster_id = DUTCH_POLS_POLAR` for sensitivity analysis. NR067–NR070 remain satellite/companion reports and create no additional quantitative unit.

## 4. R125 SIBEN multisite implementation report — full site-level audit

R125 is one bibliographic report containing direct primary program data from multiple geographically distinct implementations. It must **not** be represented by one pooled report-level row, because the source mixes different countries, hospitals, periods, algorithms and outcome ascertainment.

Five blocks meet the threshold for a quantitative extraction unit. Other country descriptions are retained as context only.

### 4.1 San Luis, Argentina

`U_R125_SAN_LUIS_AR`

- >1,400 infants screened during approximately six months of systematic implementation.
- 4 hypoxemic infants detected.
- No CCHD among the four.
- All required supplemental oxygen and had good outcomes.

Coding note:
- CCHD-negative failed-screen denominator = 4.
- Specific diagnoses are not reported; therefore these infants cannot automatically be counted as confirmed actionable **diagnoses** despite clinically meaningful management.
- Preserve as `diagnosis_not_reported + treatment_required` until Phase 5 coding.

### 4.2 Rosario Provincial Hospital, Argentina

`U_R125_ROSARIO_AR`

- Initial/intermittent implementation from 2016–2018, improving into 2019.
- 28 infants failed the first test; 25 passed repeat; 3 required a further repeat.
- One infant had final positive POS, normal echocardiogram, severe transient tachypnea, NICU admission and supplemental oxygen for five days.
- No CCHD was diagnosed in this screened period.

Coding note:
- Final CCHD-negative failed-screen denominator = 1.
- Actionable alternative diagnosis = severe TTN n=1.

### 4.3 Hospital Niño Jesús / MACSA, Barranquilla, Colombia

`U_R125_BARRANQUILLA_CO`

- Program fully implemented 1 January 2016 through 31 December 2019.
- 9,241 newborns screened.
- 38 positive tests.
- Table reports 8 hypoxemic conditions/PPHN and 12 structural cardiac diagnoses plus 18 study-defined true false positives.
- Cardiac table includes ASD, ASD+pulmonary stenosis, VSD+PDA, VSD+PPHN, TOF, TAPVR, single-ventricle lesions, septal hypertrophy and tricuspid atresia/hypoplastic RV.

Coding note:
- This is a high-value unit but the final CCHD-negative denominator must be derived using the review's locked CCHD lesion definition, not the article's broad `true positive` terminology.
- The 18 true false positives are not automatically `healthy`; clinical meaning must follow the source wording.

### 4.4 Sonora, Mexico

`U_R125_SONORA_MX`

- 9,181 apparently healthy newborns screened.
- 22 reported positive tests.
- Source reports 11 duct-dependent cardiac lesions, 8 pulmonary hypertension, 3 early sepsis and 2 study-defined true false positives with skin conditions (one generalized melanosis).
- The eight PPHN cases were echo-confirmed and treated early.

Critical arithmetic QA:
- Reported categories sum to 24 despite only 22 positive tests (11+8+3+2).
- Therefore this unit is **eligible for extraction but HOLD_FROM_PRIMARY_POOLING until category overlap/count discrepancy is resolved**.
- Do not force mutual exclusivity in Phase 4.5.

### 4.5 Guadalajara, Mexico — private hospital

`U_R125_GUADALAJARA_MX`

- >1,000 infants analyzed in 2/2019–1/2020.
- 6 failed POS.
- 2 CCHD: TGA and pulmonary valve atresia.
- 2 respiratory-condition positives, both PPHN, promptly treated.
- 2 study-defined true false positives.

Coding note:
- Confirmed CCHD-negative failed-screen denominator = 4.
- Confirmed actionable PPHN = 2.
- Remaining two retain study-defined false-positive/no qualifying condition status; do not call healthy unless explicitly supported.

### R125 country/program descriptions NOT promoted to quantitative units

- Costa Rica: 33,804 births; 16 CCHD and `a similar number` of other hypoxemic conditions, mainly PPHN/sepsis. The non-CCHD count is approximate and total positive-screen denominator is not exact → descriptive only.
- Honduras: 1,221 newborns with 7 CCHD detected; no extractable CCHD-negative failed-screen denominator → descriptive only.
- Paraguay: implementation protocol described without extractable outcome denominator → descriptive only.
- Other countries/cities in the implementation manuscript lack sufficiently exact failed-screen clinical outcome data for this review.

### R125 decision

R125 contributes **five site/program quantitative extraction units**, not one report-level quantitative row.

These five units remain linked by `report_cluster_id = R125_SIBEN_2020`; later meta-analysis should consider sensitivity to treating multiple units from one implementation report as a cluster.

## 5. Already-resolved non-independent clusters — no new action

The following are already represented correctly in the terminal report registry and create no second quantitative weight:

- R010/R011 PulseOx cohort — R011 companion.
- R006/R075 Meberg — R075 companion.
- R087/R088 Minnesota — R088 reanalysis companion.
- R032/NR034 Tanzania — NR034 preliminary/protocol companion.
- R053/NR048 Ghana — NR048 implementation companion.
- NR050/NR051–NR054 Bagalkot — NR050 representative.
- NR062/NR063 Nellore — NR062 representative.
- NR005/NR006 Hainan — both excluded from primary; NR006 companion.
- R141/R145 enriched El Bakry cluster — excluded/companion; no primary weight.
- R116/R117 Shanghai overlap — both excluded from primary.
- R048/R055 Taksande same-center lineage — both excluded after strict QA.

## 6. Wisconsin / out-of-hospital context

- R045 Miller/Wisconsin is excluded primary under criterion 6, so it cannot create duplicate weight.
- NR007 Williams out-of-hospital cohort is eligible and remains independent in the primary extraction set.
- NR008 is a Netherlands cohort and is geographically/temporally unrelated to Wisconsin.

No active primary double counting remains in this cluster.

## Quantitative-unit arithmetic after overlap resolution

Starting terminal eligible reports: **73 INCLUDE_PRIMARY reports**.

Adjustments:
- Birmingham R014 + R027: 2 reports → 1 main-analysis unit = **−1**.
- R125 SIBEN: 1 report → 5 site/program units = **+4**.

Therefore the frozen Phase 4.5 **eligible quantitative extraction-unit inventory = 76 units**.

Important: `76` means unique/non-overlapping **extraction units**, not necessarily 76 immediately poolable effect estimates. Units with unresolved target mapping, missingness, category overlap or count inconsistency may be held from the primary meta-analysis during Phase 5.

## Closure conclusion

No unresolved participant-level overlap remains that requires merging before extraction. Program-level relatedness without participant overlap (e.g. Taipei and Dutch sequential cohorts) is retained via cluster IDs for sensitivity/robust analyses.

Phase 4.5 may now hand off to the final frozen study-selection/unit dataset and then Phase 5 structured extraction.