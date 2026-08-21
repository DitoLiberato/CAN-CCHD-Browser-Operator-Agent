# CAN-CCHD Phase 4.5 — Frozen Unique Quantitative Extraction Units

Date: 2026-08-21
Status: **FROZEN EXTRACTION-UNIT INVENTORY**

Source registries:
- `PHASE45_RESTART_REPORT_MASTER_v0.5_FROZEN.md`
- `PHASE45_TERMINAL_REPORT_STATUS_REGISTRY.md`
- `PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`

## Counts

- Frozen resolved bibliographic reports: **219**
- Terminal INCLUDE_PRIMARY reports: **73**
- Terminal EXCLUDE_PRIMARY reports: **129**
- COMPANION_NONINDEPENDENT reports: **16**
- CONDITIONAL_SUPPORTING reports: **1**
- Frozen unique/non-overlapping quantitative extraction units derived from INCLUDE_PRIMARY reports: **76**

`76` is the number of extraction units. It is **not** a promise that 76 effect estimates will enter the primary meta-analysis. Phase 5 may hold units from primary pooling because of unresolved target mapping, missing diagnostic ascertainment, arithmetic inconsistency, or inability to derive the locked actionable numerator.

## Unit construction rules

- One eligible report normally creates one extraction unit.
- Actual participant overlap is collapsed.
- Distinct non-overlapping temporal cohorts from the same program may remain separate but receive a shared program-cluster ID for sensitivity/robust analysis.
- Multisite reports may create multiple units when site-level failed-screen denominators/outcomes are independently extractable.
- Companion reports create no additional unit.

## Frozen unit list

### Standard one-report units — R lineage

| Unit ID | Source report | Core Phase 5 note |
|---|---|---|
| U_R001 | R001 | standard extraction |
| U_R002 | R002 | standard extraction |
| U_R003 | R003 | standard extraction |
| U_R006 | R006 | R075 companion excluded from extra weight |
| U_R007 | R007 | echo-normal; diagnosis not ascertained beyond echo |
| U_R008 | R008 | standard extraction |
| U_R009 | R009 | clean detailed classification |
| U_R010 | R010 | R011 companion; PulseOx cohort |
| U_R013 | R013 | standard extraction |
| U_R015 | R015 | PFO/transitional; no primary evidence for prior secondary PPHN interpretation |
| U_R017 | R017 | highly informative |
| U_R018 | R018 | PFO/transitional |
| U_R019 | R019 | clean sepsis outcome |
| U_R020 | R020 | Dutch POLAR; `program_cluster_id=DUTCH_POLS_POLAR` |
| U_R021 | R021 | lesion mapping required |
| U_R022 | R022 | one unascertained positive; largely non-actionable findings |
| U_R023 | R023 | noncritical-CHD actionability mapping |
| U_R024 | R024 | clean actionable/transitional split |
| U_R025 | R025 | clean PH + healthy outcome |
| U_R026 | R026 | standard extraction |
| U_R029 | R029 | Taipei extended program; `program_cluster_id=TAIPEI_POX_PROGRAM` |
| U_R030 | R030 | target mapping + transitional-period + duplicate-publication flag |
| U_R031 | R031 | Jordan; target/table QA before pooling |
| U_R032 | R032 | Tanzania; 2 screen-positive infants unascertained outside confirmed denominator |
| U_R033 | R033 | Qatar; detailed alternative diagnoses require final extraction |
| U_R034 | R034 | Denmark; treatment/actionability coding |
| U_R035 | R035 | partial outcome ascertainment |
| U_R036 | R036 | standard extraction |
| U_R037 | R037 | standard extraction |
| U_R039 | R039 | 3/8 CCHD-negative positives not fully ascertained |
| U_R041 | R041 | detailed secondary-target distribution |
| U_R042 | R042 | standard extraction |
| U_R043 | R043 | highly informative |
| U_R049 | R049 | lesion/actionability mapping |
| U_R053 | R053 | Ghana; confirmed denominator excludes two pre-echo deaths unless diagnosis established |
| U_R066 | R066 | standard extraction |
| U_R067 | R067 | standard extraction |
| U_R068 | R068 | PPHN/PFO/VSD/large symptomatic PDA mapping |
| U_R069 | R069 | ASD/PFO mapping |
| U_R071 | R071 | clean early-onset sepsis outcome |
| U_R072 | R072 | exact actionable numerator 10/33; subtype-limited |
| U_R076 | R076 | 6 PPHN + 2 congenital pneumonia |
| U_R077 | R077 | Taipei pilot; `program_cluster_id=TAIPEI_POX_PROGRAM` |
| U_R086 | R086 | denominator framing QA |
| U_R087 | R087 | Minnesota; R088 companion; implementation-error flag |
| U_R089 | R089 | clean 1/1 PPHN |
| U_R093 | R093 | clean 2/2 respiratory illness |
| U_R099 | R099 | PPHN/sepsis overlap; PDA/ASD mapping |
| U_R100 | R100 | New Zealand; cardiac classification QA |
| U_R101 | R101 | denominator convention 360 algorithm-positive vs 189 study-defined true-positive |
| U_R102 | R102 | category mutual-exclusivity QA |
| U_R104 | R104 | standard extraction |
| U_R105 | R105 | detailed noncardiac classification |
| U_R108 | R108 | early/transitional findings without follow-up |
| U_R109 | R109 | ASD/PFO actionability mapping |
| U_R126 | R126 | abstract/detail discrepancy; detailed flow governs unless resolved |
| U_R127 | R127 | high-altitude subgroup |
| U_R128 | R128 | PFO/transitional coding |
| U_R130 | R130 | early-screen timing + lesion actionability |
| U_R135 | R135 | partial alternative-pathology classification |

### Standard one-report units — NR lineage

| Unit ID | Source report | Core Phase 5 note |
|---|---|---|
| U_NR002 | NR002 | Gamhewage Sri Lanka; CCHD-negative diagnoses incompletely specified |
| U_NR007 | NR007 | Williams out-of-hospital; denominator-convention flag |
| U_NR008 | NR008 | Dutch POLS; `program_cluster_id=DUTCH_POLS_POLAR`; non-overlapping with R020 |
| U_NR009 | NR009 | altitude; 9 PDA + 12 incompletely characterized positives |
| U_NR044 | NR044 | Bangalore; locked CCHD lesion remapping required |
| U_NR050 | NR050 | Bagalkot representative; NR051–NR054 companions |
| U_NR058 | NR058 | ASD+VSD+pulmonary stenosis target mapping |
| U_NR059 | NR059 | West Virginia; 10 confirmed CCHD-negative nominal diagnoses; 2 failed screens without TTE unascertained |
| U_NR062 | NR062 | Nellore; target-definition/lesion mapping; NR063 companion |
| U_NR064 | NR064 | echo-normal CCHD-negative infant is not automatically healthy |

### Collapsed overlap unit

| Unit ID | Source reports | Main representative | Rule |
|---|---|---|---|
| U_BIRMINGHAM_R027_MAIN | R014 + R027 | R027 Henderson 2022 | April–July 2013 participant-period overlap. R014 retained for supporting detail and sensitivity replacement; never sum both as independent. |

### R125 SIBEN site/program units

| Unit ID | Site/program | Core Phase 5 note |
|---|---|---|
| U_R125_SAN_LUIS_AR | San Luis, Argentina | >1,400 screened; 4 CCHD-negative hypoxemic infants; all required O2; diagnoses not reported → `diagnosis_not_reported + treatment_required`. |
| U_R125_ROSARIO_AR | Provincial Hospital Rosario, Argentina | final positive n=1; no CCHD; severe TTN, NICU, O2 5 days. |
| U_R125_BARRANQUILLA_CO | Hospital Niño Jesús/MACSA, Barranquilla | 9,241 screened; 38 positive; detailed structural/hypoxemic table; locked CCHD lesion mapping required. |
| U_R125_SONORA_MX | Sonora program, Mexico | 9,181 screened; 22 positive; source category counts arithmetically inconsistent (sum 24) → extraction allowed but HOLD_FROM_PRIMARY_POOLING until reconciled. |
| U_R125_GUADALAJARA_MX | private hospital, Guadalajara | >1,000 analyzed; 6 fails; 2 CCHD, 2 PPHN, 2 study-defined true false positives. CCHD-negative denominator=4. |

## Program-cluster relationships without participant overlap

These are not merged, but should be available for sensitivity/robust analysis:

- `TAIPEI_POX_PROGRAM`: U_R077 + U_R029. Pilot 10/2013–3/2014; extended cohort begins 4/2014.
- `DUTCH_POLS_POLAR`: U_NR008 + U_R020. Feasibility cohort 10/2013–10/2014; POLAR 7/2015–12/2016.
- `R125_SIBEN_2020`: five R125 site/program units from one multisite implementation publication.

## Non-quantitative eligible/report relationships

- R014 remains an eligible report but contributes no separate main-analysis weight because of overlap with R027.
- NR001 remains `CONDITIONAL_SUPPORTING` and is not part of the 76-unit primary extraction inventory.
- Companion reports remain linked for provenance but create no weight.

## Primary-pooling hold flags carried into Phase 5

At minimum:
- U_R101 — denominator convention unresolved.
- U_R102 — diagnostic-category mutual exclusivity.
- U_R126 — abstract/full-text CCHD count discrepancy.
- U_R125_SONORA_MX — arithmetic inconsistency in diagnostic categories.
- Any unit requiring locked lesion-level CCHD/actionability mapping before a valid numerator can be computed.

## Frozen conclusion

The Phase 4.5 evidence base now has a fully enumerated, provenance-linked, overlap-resolved inventory of **76 unique quantitative extraction units** derived from 73 eligible primary reports.

The next phase is **Phase 5 structured extraction and lesion/actionability coding**, followed by determination of which of the 76 units can enter each primary and sensitivity meta-analysis.