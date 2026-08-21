# Phase 4.5 — corrected deduplication and membership rebuild

Date: 2026-08-21
Status: REQUIRED BEFORE PHASE 4 CLOSURE

## Scope boundary

This systematic review was formally restarted from zero in August 2026. The old CAN-CCHD Browser Agent database and its legacy `records` / `studies` / `screening_decisions` stack are **legacy/pilot artifacts only** and must not define the evidence corpus of the restarted review.

A diagnostic GitHub Actions export of `data/processed/can_cchd_agent.db` confirmed that the legacy database contains 2,301 `normalized_records`, 2,259 legacy `records`, and 1,572 legacy `studies`. Those counts are incompatible with the restarted review's manually constructed 327-record raw corpus. The export also exposed identifier-quality problems in the legacy database, including PMCID values reused across clearly unrelated articles. Therefore the legacy SQLite database is explicitly **excluded as a scientific source of membership for the restarted review**.

The legacy database remains useful only to understand software-architecture failure modes and to motivate safer deduplication rules.

## Why the historical 156-roster cannot simply be recovered

The restarted review reached a raw corpus of 327 records and then underwent normalization/deduplication and Phase 3 routing in conversation. A historical working roster was described as 49 `include`, 111 `maybe`, and 9 `separate_analysis`, with an active Phase 4 queue of 49 `include` + 107 `maybe` = 156.

However, the exact 327-row normalized/deduplicated export is not currently present in the accessible File Library or repository. The visible public-corpus workbooks (`v0.1` through `v0.6`) are earlier discovery snapshots of 65–132 raw reports and explicitly state that formal deduplication was still blocked. The repository SQLite is from the legacy app and is not the restarted 327-record corpus.

Therefore:

- the old `156` count is preserved as historical audit metadata;
- it is **not** used as a final denominator until the restarted 327-record corpus is reconstructed or its missing normalization artifact is recovered;
- no legacy-app Nxxx/study mapping is imported automatically.

## Binding decision

Phase 4 closure will be based only on the restarted review corpus.

The reconstruction hierarchy is:

1. **restart-native raw/export artifacts** from the August 2026 searches;
2. restart public-corpus workbooks and source reconciliation sheets;
3. original PubMed/Europe PMC/regional exports uploaded during the restart;
4. the report-level Phase 4 adjudication ledger already created during the restart;
5. external full text / bibliographic verification when needed.

Legacy app data may be consulted only for software QA and never to add, remove, or classify a study in the restarted review.

## Phase 4.5 target

Reconstruct the restarted review's authoritative bibliographic set and perform a fresh, auditable deduplication that preserves provenance.

### Data model

#### Source occurrence

One row per bibliographic occurrence discovered in the restarted search process.

Required provenance where available:

- source/database;
- query/export identity;
- PMID;
- DOI;
- PMCID;
- title;
- first author;
- year;
- source URL;
- raw source/report identifier.

#### Deduplicated report identity

One row per unique bibliographic report.

#### Provenance links

Every source occurrence remains linked to its unique bibliographic report. Nothing is deleted.

#### Cohort relation

Companion reports, overlapping time periods, and repeated analyses of the same cohort remain distinct bibliographic reports but are linked through a separate cohort-overlap register.

Bibliographic deduplication and cohort independence are different operations.

## Correct deduplication rules for the restart corpus

### Strong automatic identity keys

Use connected components formed by:

1. exact normalized PMID;
2. exact normalized DOI.

These are transitive: if A shares PMID with B and B shares DOI with C, all three are one bibliographic identity unless a manual conflict review proves metadata contamination.

### Conditional identity keys

PMCID is **not** an unconditional auto-merge key. It may support identity only when it is concordant with title and does not contradict PMID/DOI, because legacy QA demonstrated that PMCID contamination can occur.

Exact normalized title should not be used alone when the title is generic. Prefer:

- exact normalized title + first-author surname + compatible year;
- exact title + concordant DOI/PMID;
- manual confirmation for translations/alternate-title variants.

### Manual review queue

Never auto-merge solely on fuzzy similarity. Queue:

- fuzzy titles;
- identifier conflicts;
- same title with different authors/years;
- translated titles;
- conference abstract vs full article;
- companion reports from the same cohort;
- corrections/editorials with similar titles.

## Preservation of the completed Phase 4 adjudication work

The report-level Phase 4 decisions already made during the restart remain valid evidence and form a reusable adjudication library.

After the restart corpus is reconstructed and deduplicated, each unique report is matched to that library using:

- exact PMID;
- exact DOI;
- title + author + year;
- manual bibliographic confirmation.

When identity is confirmed, carry forward:

- INCLUDE / EXCLUDE / CONDITIONAL / COMPANION decision;
- reason for decision;
- CCHD-negative failed-screen denominator;
- CAN-CCHD outcome information;
- transitional/non-actionable category;
- healthy/no-diagnosis category;
- diagnosis-not-ascertained category;
- overlap/cohort flags;
- QA flags.

No article should be re-read merely because the bibliographic ID changes.

## Reconstruction sequence

### 4.5A — Recover restart-native raw corpus

Reconstruct the 327 raw records from restart artifacts only.

Current accessible anchors include:

- `pubmed-criticalco-set.txt`;
- `pubmed-21820732PM-set.txt`;
- public-corpus workbooks `CAN-CCHD_Public_Corpus_v0.1` through `v0.6`;
- the v0.7 regional manifest;
- PubMed/Europe PMC/LILACS/SciELO/IMEMR reconciliation sheets;
- report identities and source details preserved in the Phase 4 tranche files and master ledger.

The task is to recover the exact 327-row roster or, if exact historical reconstruction proves impossible, construct a replacement restart-native master roster with explicit provenance and document the delta from the historical 327 count.

### 4.5B — Fresh bibliographic deduplication

Run the conflict-aware rules above and create:

- raw/source-occurrence table;
- unique-report table;
- occurrence-to-report links;
- duplicate audit log;
- manual-review queue.

### 4.5C — Reapply Phase 3 routing only where needed

Do not blindly reproduce old `include/maybe` labels. First project known Phase 4 decisions onto the corrected unique reports.

Only reports without an existing validated full-text decision require title/abstract or full-text reassessment.

### 4.5D — Resolve delta reports

Adjudicate genuinely unmatched reports and verify reports that appeared only through non-PubMed/regional sources.

### 4.5E — Freeze corrected Phase 4 membership

Produce final report-level counts from the reconstructed restart corpus:

- eligible primary reports;
- excluded reports with reasons;
- companion reports;
- NICU/secondary/sensitivity reports;
- zero-event eligible reports;
- unresolved reports, if any.

Then derive **unique quantitative cohorts** after cohort-overlap resolution.

### 4.5F — Structured extraction handoff

Only after membership is frozen, create the Phase 5 extraction dataset with:

- screened population;
- final failed screens;
- CCHD detected;
- CCHD-negative failed-screen denominator;
- actionable CAN-CCHD;
- transitional/non-actionable;
- explicitly healthy/no diagnosis;
- diagnosis not reported/not ascertained;
- diagnosis categories;
- timing/setting/altitude/NICU flags;
- overlap/cohort identifiers.

## Audit handling of the legacy SQLite diagnostic export

The temporary GitHub Actions export of the legacy database is retained only as software-QA evidence. It demonstrated:

- `raw_records`: 2,301 rows;
- `normalized_records`: 2,301 rows;
- legacy `records`: 2,259 rows;
- legacy `studies`: 1,572 rows;
- legacy deduplication cannot be assumed correct;
- PMCID contamination can create false connected components if PMCID is trusted blindly.

None of these rows or counts may be used to alter the restarted review corpus.

## Closure criterion

Phase 4 is complete only when:

1. the restart-native corpus has been reconstructed and versioned;
2. fresh conflict-aware bibliographic deduplication is complete;
3. every unique restart report has a terminal Phase 4 disposition or documented out-of-scope status;
4. every carried-forward adjudication has an explicit identity/provenance link;
5. cohort overlaps are registered separately from bibliographic duplicates;
6. the corrected study-selection dataset is frozen.

The historical `156` remains an audit checkpoint, not the primary completion denominator.