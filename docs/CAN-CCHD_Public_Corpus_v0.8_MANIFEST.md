# CAN-CCHD Public Corpus v0.8 — Google Scholar Supplementary + Citation Chasing Manifest

Date: 2026-08-21

## Scope

This manifest records the Google-Scholar-style supplementary public-web discovery and formal citation-chasing phase performed after corpus v0.7.

Google Scholar is supplementary only. The current environment did not provide a native Google Scholar UI with a reproducible exact result count/export. Therefore this phase claims **public-web/citation saturation**, not native Google Scholar exhaustive coverage.

## Corpus state

- v0.7 logical raw reports: **145**
- new raw reports in this phase: **31** (`R146`–`R176`)
- v0.8 logical raw reports: **176**
- `candidate_primary`: **94** (87 + 7)
- `needs_full_record_review`: **58** (37 + 21)
- `secondary_citation_chasing`: **20** (18 + 2)
- `clearly_ineligible`: **4** (3 + 1)
- verified PMIDs: **125**

No report-level deduplication was performed.

## Search architecture

The phase included:

1. Protocol-specified Google Scholar supplementary queries.
2. Author/title/journal seed expansion.
3. Backward citation chasing from historical and recent systematic reviews and high-yield primary studies.
4. Forward/recent-publication discovery, especially 2025–2026.
5. Materialization of unresolved non-PubMed references already documented in earlier reconciliation tables.
6. Report-cluster chasing, including Hainan/China.
7. Long-tail national-journal discovery, especially India and Sri Lanka.
8. Local-language/regional expansion, including Portuguese/Brazil and Spanish/Latin America.
9. Two independent closing waves after the final genuine new routine-primary gain.

## New raw reports

| ID | First author | Year | Setting | Routing status | Key note |
|---|---|---:|---|---|---|
| R146 | Gamhewage | 2021 | Sri Lanka | candidate_primary | 8,718 screened; 19 POS positive; 14 CCHD; 5 CCHD-negative failures identifiable. |
| R147 | Gunaratne | 2021 | Sri Lanka | needs_full_record_review | 5,435 newborns; 4 implied CCHD-negative POS failures require outcome extraction. |
| R148 | Mamun | 2016 | Bangladesh | needs_full_record_review | 510 neonates; 28 positive; 21 critical CHD. |
| R149 | Mannan | 2022 | Bangladesh | needs_full_record_review | 1,033 newborns; 16 positive; 4 CCHD. |
| R150 | Reddy | 2018 | India | candidate_primary | 800 asymptomatic newborns; one POS-positive non-target CHD case. |
| R151 | Lanker | 2014 | India | candidate_primary | 1,200 newborns; 3 low-SpO2, 2 critical cyanotic CHD, 1 structurally normal. |
| R152 | Lone | 2016 | India | needs_full_record_review | 2,600 asymptomatic neonates; exact false-positive denominator requires full text. |
| R153 | Siva | 2016 | India | candidate_primary | 430 newborns; 5 positive screens reported as CCHD; confirm at full text. |
| R154 | Shenoy | 2017 | India | candidate_primary | 278 term neonates; 1 positive screen reported CCHD. |
| R155 | Shah | 2015 | India | candidate_primary | 700 newborns; 4 positive screens, apparently CCHD. |
| R156 | Suresh | 2024 | India | needs_full_record_review | POX + echo study; CCHD-specific outcomes need extraction. |
| R157 | Panuganti | 2024 | India | needs_full_record_review | Combined POX + clinical examination. |
| R158 | Gunasekaran | 2026 | India | needs_full_record_review | 116 newborns; 3 positive screens. |
| R159 | Kalpana | 2019 | India | needs_full_record_review | 783 births; combined clinical/POX pathway. |
| R160 | Donia | 2016 | Egypt | needs_full_record_review | Previously unresolved; 120 persistent low-SpO2 asymptomatic term newborns; positive-screen-enriched cohort. |
| R161 | Zayachnikova | 2020 | Russia | needs_full_record_review | Previously unresolved regional report. |
| R162 | Chen | 2023 | Hainan, China | needs_full_record_review | Hainan report cluster; 321,447 screened; combined dual-index strategy. |
| R163 | Zhang | 2023 | Hainan, China | needs_full_record_review | 2020–2021 Hainan subset; possible overlap with R162/R164. |
| R164 | Kong | 2023 | Hainan, China | needs_full_record_review | Companion Hainan implementation report. |
| R165 | Schena | 2013 | Italy | needs_full_record_review | Conference-supplement report; possible companion/precursor to existing Schena report. |
| R166 | Mathur | 2015 | India | needs_full_record_review | PMID 26519711; NICU-only sick-neonate cohort. |
| R167 | Kalita | 2016 | India | needs_full_record_review | 1,720 NICU newborns. |
| R168 | Ramachandran | 2016 | India | clearly_ineligible | Known cyanotic-heart-disease children, mixed age; not newborn screening. |
| R169 | Oko | 2026 | Republic of the Congo | needs_full_record_review | 300 newborns; target reported as all/cyanotic CHD; outcome adjudication needed. |
| R170 | Mettananda | 2026 | Sri Lanka | needs_full_record_review | PMID 42243713; 8 CCHD-screen referrals, 1 CCHD. |
| R171 | Arican | 2019 | Turkey | needs_full_record_review | 1,000 newborns; 29 positive screens. |
| R172 | Lakra | 2022 | Sri Lanka | secondary_citation_chasing | Correspondence on Gamhewage; no new primary dataset. |
| R173 | Huang | 2025 | China | secondary_citation_chasing | Training/program report, PMID 39846594; no clinical failed-screen denominator. |
| R174 | Nascimento | 2024 | Brazil | needs_full_record_review | 10,053 tests; 42 altered; incomplete follow-up but high CAN-CCHD relevance. |
| R175 | Maciel | 2019 | Brazil | needs_full_record_review | 2,576 tests; conference/experience report; diagnostic breakdown unavailable in abstract. |
| R176 | Suniga | 2026 | Brazil | candidate_primary | 2,057 asymptomatic rooming-in newborns; 4 positive screens; all 4 final diagnoses normal. Last genuine new routine-primary gain. |

## Reconciliation decisions

The following rediscoveries were **not duplicated** because they were already materialized in v0.6/v0.7: Rendón Díez 2025 (`R130`), de Lira Albuquerque 2015 (`R124`), Rajani 2025 (`R107`), Taivassalo 2025 (`R103`), Hardik Shah 2026 (`R108`), Mohsin 2019 (`R076`) and multiple other PubMed/high-yield studies.

Earlier unresolved leads were materialized rather than left as bibliographic placeholders:

- Gamhewage 2021 → `R146`
- Donia & Tolba 2016 → `R160`
- Zayachnikova 2020 → `R161`
- vague Chen/Hainan 2023 lead → report cluster `R162`–`R164`

Potential companion/overlap relationships are preserved and must be adjudicated only during formal deduplication/study clustering.

## Saturation test

The last genuine new routine-primary report was `R176` (Suniga 2026).

Two independent closing waves were then executed:

### Closing wave A — Portuguese/Spanish/Latin America

Used localized combinations around `teste do coraçãozinho`, `resultado alterado`, `oximetria de pulso`, `tamizaje`, `oximetría`, newborn/recién nacido, echocardiography and hospital/cohort terms.

Result: **0 incremental routine-primary reports** after reconciliation. Rendón Díez 2025 resurfaced but was already `R130`.

### Closing wave B — global alternate vocabulary/recent literature

Used combinations of pulse oximetry/oxymetry, oxygen saturation, newborn screening, positive/failed/false-positive screen, CCHD/CHD, PPHN, sepsis, respiratory disease, and years 2022–2026.

Result: **0 incremental routine-primary reports** after reconciliation. Hits were already in the corpus or had already been added earlier in this same citation phase.

Therefore:

- `GOOGLE_SCHOLAR_SUPPLEMENTARY_PUBLIC_DISCOVERY = SATURATED_FOR_NEW_ROUTINE_PRIMARY`
- `CITATION_CHASING = SATURATED_FOR_NEW_ROUTINE_PRIMARY`

This does **not** imply a native Google Scholar exhaustive search or exact result count.

## Remaining source limitations

- PubMed/MEDLINE public-web completeness remains reopened because later cross-source work surfaced PubMed-indexed records absent from earlier public-web collection. Native exact execution/export remains pending.
- Europe PMC public sweep is saturated; native API count/export remains pending.
- LILACS/BVS public sweep is saturated; native exact count/export remains pending.
- SciELO public sweep is saturated; native exact count/export remains pending.
- IMEMR/EMR public sweep is saturated for new routine cohorts; native exact count/export remains pending.
- Google Scholar supplementary/citation discovery is saturated for new routine primary reports, but no native exact Scholar count/export is claimed.

## Gate

`DEDUPLICATION = BLOCKED_PENDING_COLLECTION_CLOSEOUT`

The next methodological step is a global Phase 1 collection-closeout QA: formally adjudicate whether the documented native-access limitations are acceptable for this review or whether additional native executions are required before deduplication is unlocked.
