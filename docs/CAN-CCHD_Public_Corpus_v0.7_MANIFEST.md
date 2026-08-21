# CAN-CCHD Public Corpus v0.7 — Consolidation Manifest

## Status

This manifest consolidates the IMEMR / Eastern Mediterranean regional public-web collection phase on top of `CAN-CCHD_Public_Corpus_v0.6.xlsx`.

The base v0.6 workbook remains the preceding binary corpus artifact. The v0.7 consolidation adds report-level provenance and corrections without deduplication.

## Corpus counts

| Metric | v0.6 | v0.7 delta | v0.7 logical total |
|---|---:|---:|---:|
| Raw reports | 132 | 13 | 145 |
| `candidate_primary` | 86 | 1 | 87 |
| `needs_full_record_review` | 25 | 12 | 37 |
| `secondary_citation_chasing` | 18 | 0 | 18 |
| `clearly_ineligible` | 3 | 0 | 3 |
| Nonblank PMIDs | 118 | 4 | 122 |

Routing labels remain preliminary collection annotations, not final eligibility decisions.

## R012 bibliographic correction

R012 is corrected in place; the report count does not change.

- Title: *Pulse oximetry screening for clinically unrecognized critical congenital heart disease in the newborns*
- Correct first author: Ruangritnamchai
- Correct year: 2007
- Correct country: Thailand
- PMID: 22368668
- PMCID: PMC3232575
- Preliminary relevance: `candidate_primary`

The v0.6 association of PMID 22368668 with Movahedian / Iran / 2012 was incorrect.

## New raw reports R133–R145

| ID | First author | Year | Country | Preliminary relevance | Key provenance / QA note |
|---|---|---:|---|---|---|
| R133 | Mosayebi | 2012 | Iran | `needs_full_record_review` | WHO/EMRO IMEMR-hosted Razi Journal report; 1,506 newborns; 29 persistent low-SpO2 screens; 6 cyanotic/critical CHD. |
| R134 | Dehvari | 2022 | Iran | `needs_full_record_review` | Pakistan Heart Journal; 3,151 term neonates; 29 persistent SpO2<95%; 26 echocardiograms, 22 CHD. DOI 10.47144/phj.v55i1.2122. |
| R135 | Salih | 2018 | Iraq | `candidate_primary` | 2,181 neonates; 55 CHD false positives; 28/55 had other pathology. DOI 10.24017/science.2018.2.22. |
| R136 | Methlouthi | 2016 | Tunisia | `needs_full_record_review` | Prospective 10,447-newborn cohort. PMID 27575509. |
| R137 | Al Mazrouei | 2013 | United Arab Emirates | `needs_full_record_review` | Abu Dhabi emirate-wide implementation. PMID 23532467; DOI 10.1007/s00246-013-0692-6. |
| R138 | Al Zarouni | 2022 | United Arab Emirates | `needs_full_record_review` | Emirates Health Services automated screening program. PMID 35729549; PMCID PMC9214992; DOI 10.1186/s12911-022-01900-y. |
| R139 | Ismail | 2021 | Egypt | `needs_full_record_review` | Aswan University; N=100; 5 true-positive and 95 true-negative PO/ECHO results. |
| R140 | Abdel Rahman | 2022 | Egypt | `needs_full_record_review` | Benha University asymptomatic-newborn screening cohort. DOI 10.21608/bmfj.2022.118766.1536. |
| R141 | El Bakry | 2023 | Egypt/UAE | `needs_full_record_review` | Enriched/selected CHD population; likely same 2014–2016 cohort as R145. DOI 10.19080/AJPN.2023.13.555912. |
| R142 | Saeedi | 2024 | Iran | `needs_full_record_review` | Combined SpO2/perfusion-index screening. PMID 39534994; PMCID PMC11558613; DOI 10.34172/aim.31293. |
| R143 | Kadivar | 2020 | Iran | `needs_full_record_review` | NICU/enriched diagnostic cohort; Persian report. DOI 10.34172/mj.2020.066. |
| R144 | Majeed-Saidan | 2019 | Saudi Arabia | `needs_full_record_review` | 28,646 eligible births; routine PO introduced during study but no extractable failed-screen denominator. DOI 10.1186/s40949-019-0023-8. |
| R145 | El Bakry | 2024 | Egypt/UAE | `needs_full_record_review` | Companion report discovered during v0.7 validation; likely same cohort as R141. DOI 10.21608/bmfj.2024.262863.1997. |

## IMEMR / regional search reconciliation

1. The initial simple IMEMR public-web sweep surfaced Mosayebi 2012 and known records.
2. A Saudi-specific audit did not identify another directly extractable Saudi CCHD screening cohort beyond known corpus records at that stage.
3. A country-by-country Eastern Mediterranean audit broke the initial saturation impression and recovered multiple primary reports.
4. The initial generic IMEMR saturation claim was therefore **withdrawn**.
5. Seed/author/title expansion recovered Saeedi 2024 and Majeed-Saidan 2019.
6. A multilingual wave, including Farsi, recovered Kadivar 2020.
7. Two independent closing waves then found zero new routine potentially eligible screening cohorts.
8. Bibliographic validation identified R145 as a companion report of the El Bakry report cluster; it is preserved because formal report-level deduplication has not begun.

Final public-web status:

`SATURATED_PUBLIC_WEB_SWEEP_FOR_NEW_ROUTINE_COHORTS`

Native IMEMR exact query/count/export status:

`PENDING`

Public-web saturation is not claimed as native-platform completeness.

## Source state after v0.7

- PubMed/MEDLINE: `REOPENED`; native exact count/export pending.
- Europe PMC: public sweep saturated; native API count/export pending.
- LILACS/BVS: public sweep saturated; native exact count/export pending.
- SciELO: public sweep saturated; native exact count/export pending.
- IMEMR / EMR regional: public-web sweep saturated for new routine cohorts; native exact count/export pending.
- Google Scholar: next, supplementary only.
- Formal citation chasing: pending after Google Scholar.
- Deduplication: **BLOCKED**.

## Next step

Proceed to the protocol-defined supplementary Google Scholar sweep, reconcile every incremental report against the raw corpus, then perform formal backward/forward citation chasing before unlocking deduplication.
