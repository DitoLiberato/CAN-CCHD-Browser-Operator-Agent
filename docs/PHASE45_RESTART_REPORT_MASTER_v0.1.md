# CAN-CCHD Phase 4.5 Restart-Native Report Master v0.1

Date: 2026-08-21
Status: WORKING MASTER / NOT YET FROZEN
Branch: `phase4-consolidation`

## Purpose

This file defines the restart-native bibliographic report master used for corrected Phase 4 accounting. It replaces the invalid attempt to close Phase 4 against the historical `156 Nxxx` roster and explicitly excludes the legacy Browser Agent SQLite database from scientific membership.

## Base report set

The stable restart-native public-corpus lineage contains bibliographic reports **R001–R145**, built progressively through PubMed/public discovery, Cochrane/Saganski/van Vliet reconciliation, Europe PMC, regional/LILACS/SciELO/IMEMR sweeps, and public-web saturation work.

These 145 Rxxx rows are treated as the current base report inventory. They are bibliographic reports, not unique quantitative cohorts and not necessarily primary-eligible studies.

## Verified non-R restart-native deltas

The following reports were explicitly discovered/retained during restart-native reconciliation but were not assigned R001–R145 IDs.

| Delta ID | Citation / identity | Provenance | Relation | Phase 4 disposition | Key CAN-CCHD note |
|---|---|---|---|---|---|
| NR001 | Donia AES, Tolba OA. 2016. *Use of early pulse oximetry in the detection of cardiac lesions among asymptomatic term newborns*. Gaz Egypt Paediatr Assoc. DOI 10.1016/j.epag.2016.02.001 | Saganski reconciliation; verified non-PubMed public source | independent report | CONDITIONAL / SUPPORTING | Selected cohort of 120 asymptomatic term newborns already with persistent SpO2<95%; 38 significant cardiac lesions, 41 insignificant, 41 normal hearts. No full screened source denominator recovered, so cannot contribute population failure incidence. |
| NR002 | Gamhewage NC, Perera KSY, Weerasekera M. 2021. *Effectiveness of newborn pulse oximetry screening for the identification of critical congenital heart disease in a tertiary care hospital in Sri Lanka*. Sri Lanka J Child Health 50(4):699–703. DOI 10.4038/sljch.v50i4.9890 | Saganski + Europe PMC reconciliation; verified non-PubMed public source | independent report | INCLUDE | 8,718 screened; 19 positive; 18 CHD, 14 CCHD; 1 POX-positive infant without CHD, alternative diagnosis not reported. Four non-CCHD cardiac diagnoses remain lesion-level/actionability candidates. |
| NR003 | Zayachnikova T, Delryu N, Shishimorov I, Magnitskaya O, Belan E. 2020. *Accuracy of pulse oximetry for early detection of critical congenital heart disease in Volgograd region (Russia)*. Archive Euromedica 10(2):53–54. DOI 10.35630/2199-885X/2020/10/2.16 | Saganski reference list; previously unresolved, now bibliographically verified | independent report | EXCLUDE PRIMARY / RETAIN ACCURACY CONTEXT | 20,527 asymptomatic newborns screened. Six screen-detected CCHD and 12 false-positive POS results are reported, but the 12 CCHD-negative failed screens are not given diagnosis/outcome/management/no-diagnosis classification. Criterion 6 not met. Note Saganski table reports N=20,547; primary article reports N=20,527. |
| NR004 | Gunaratne CR, Hewage I, Fonseka A, Thennakoon S. 2021. *Comparison of pulse oximetry screening versus routine clinical examination in detecting critical congenital heart disease in newborns*. Sri Lanka J Child Health 50(1):4–11. DOI 10.4038/sljch.v50i1.9393 | Saganski reference list; distinct from NR002 Gamhewage | independent report | EXCLUDE PRIMARY / RETAIN ACCURACY CONTEXT | 5,435 asymptomatic newborns ≥24 h. POX alone: 10 true-positive CCHD, 4 false positives, 1 false negative. Article states POX can detect non-cardiac hypoxaemia, but does not provide a defensible diagnosis/outcome classification for the four CCHD-negative POX-positive infants. Criterion 6 not met. |
| NR005 | Chen QQ, Zhang DF, Wang YZ, Zhang XY. 2023. *Appropriate Technology for Screening, Diagnosis, and Evaluation of Neonatal Congenital Heart Disease in the Southernmost Region of China*. Iranian/Innovative Journal of Pediatrics 33(1):e132589. DOI 10.5812/ijp-132589 | van Vliet reconciliation as Chen/Hainan non-PubMed/unresolved; now directly verified | Hainan 2019–2021 program report; companion/overlap with NR006 | EXCLUDE PRIMARY / RETAIN PROGRAM CONTEXT | 321,447 screened; dual-index cardiac auscultation + POX. POX-alone results are reported (2,176 abnormal POX; 368 CHD; 1,808 CHD false positives), but non-CCHD diagnoses/outcomes among the POX false positives are not classified. Criterion 6 not met. |
| NR006 | Zhang Dufei, Chen Renwei, Mo Zelai, Yang Ling, Wang Yazhou, Wang Haifan. 2023. *Application of Appropriate Technology for Screening, Diagnosis and Evaluation of Congenital Heart Disease in Neonates in Hainan Province*. Chinese General Practice 26(25):3170–3177. DOI 10.12114/j.issn.1007-9572.2022.0687 | van Vliet/Chinese regional follow-up; directly verified | COMPANION / SAME HAINAN PROGRAM AS NR005; no independent cohort contribution | COMPANION / NO INDEPENDENT COHORT | Same Hainan dual-index screening technology/program, same 2019–2021 provincial setting. Preserve Chinese-language report provenance and supplementary details; do not pool independently from NR005. |

## Current restart-native master size

- Base Rxxx reports: 145
- Verified non-R delta reports: 6
- **Current bibliographic report master: 151 reports**

This `151` is a current report-inventory count, **not** a final eligible-study count and **not** a unique-cohort count.

## Important correction: Sri Lanka report identities

The older reconciliation sheet used wording such as `Gamhewage/Gunaratne 2021`, which can falsely imply one report. They are distinct:

- NR002 Gamhewage et al.: Sri Lanka J Child Health 50(4):699–703; 8,718 screened.
- NR004 Gunaratne et al.: Sri Lanka J Child Health 50(1):4–11; 5,435 screened.

They must never be bibliographically merged.

## Delta candidates resolved during this pass

- `de Lira Albuquerque 2015` was later assigned **R124**; not a delta.
- `Chen/Hainan 2023` is now resolved into NR005 plus the related Chinese-language NR006 report.
- `Zayachnikova 2020` is no longer an unresolved citation; it is NR003.
- Donia/Tolba and Gamhewage remain verified non-PubMed deltas NR001–NR002.

## Remaining master-completeness audit

Before freezing this master:

1. Cross-check every primary reference in Cochrane 2018, Saganski 2024, and van Vliet 2024 against R001–R145 + NR001–NR006.
2. Cross-check the native PMID export against the master by PMID; any PMID not represented must be classified as new report, review/method/context record, or duplicate of an existing report.
3. Cross-check regional/LILACS/SciELO/IMEMR reconciliation ledgers for reports explicitly retained outside the Rxxx table.
4. Verify whether any Google Scholar/citation-chasing report after v0.7 was documented only in chat and not in R/NR form.
5. Create a structured TSV/CSV version after no new bibliographic identities are found in two independent closing reconciliation waves.

## Phase 4 projection rule

All prior Rxxx adjudications remain valid at the report level. NR001–NR006 dispositions above are added to the same adjudication library. Once report-master completeness is frozen, final Phase 4 counts must be recomputed from this master, and cohort-level overlap must be resolved separately before quantitative pooling.