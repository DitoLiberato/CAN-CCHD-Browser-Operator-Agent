# CAN-CCHD Browser Operator Agent — Robust Search Collection Reform

## Purpose

This document instructs Codex to reform the search and collection layer of the CAN-CCHD Browser Operator Agent.

The current collection successfully identified a broad candidate literature set, but it did not persist enough metadata from the beginning. This is not a methodological failure of the review. It is a development finding showing that the collection pipeline must be redesigned before the real study dataset is built.

Core decision:

> Do not try to repair the current database. Rebuild the search/collection pipeline so that the next collection starts from a complete, auditable, validated metadata record for every candidate article.

The goal is:

```text
complete data from first collection
+ raw source preservation
+ metadata enrichment
+ collection QA
+ only then deduplication and screening
```

---

# 1. Problem Observed

The first large collection produced thousands of candidate records, but the exported raw collection contained only limited metadata:

```text
title
authors
year
pmid
source_name
query_label
imported_at
```

Missing or inconsistently persisted fields included:

```text
abstract
DOI
PMCID
journal
URL
PDF/OA status
publication type
language
country
source record ID
raw metadata JSON
search URL
query string
result count
```

Europe PMC records also showed unreliable `year` parsing, with many records assigned `2024` despite representing older articles.

Conclusion:

```text
The collection layer must be redesigned before the real study dataset is generated.
```

---

# 2. New Collection Philosophy

The search/collection phase must not merely create candidate titles.

It must create **complete, auditable raw records**.

The app should separate:

```text
raw source record
↓
normalized record
↓
enriched record
↓
collection-QA-passed record
↓
deduplication candidate
↓
unique study
```

Do not collapse these stages.

---

# 3. New Data Flow

Required flow:

```text
Research Plan Approved
↓
Source Query Execution
↓
Raw Record Harvest
↓
Raw Metadata Preservation
↓
Identifier Normalization
↓
Metadata Enrichment
↓
Collection QA
↓
Collection Completion Gate
↓
Deduplication
```

Deduplication must not run until collection QA confirms that records have been enriched as far as possible.

---

# 4. New Core Principle: Collection Contract

Every source adapter must try to return the same standard record contract.

## Required standard fields

Every collected record must have:

```text
record_id
source_database
source_access_mode
source_record_id
source_url
query_id
query_label
query_string
query_run_id
search_url
title
authors_raw
first_author
year
journal
doi
pmid
pmcid
abstract
publication_type
language
country
keywords
mesh_terms
landing_page_url
pdf_url
is_open_access
oa_status
source_created_date
source_updated_date
imported_at
raw_metadata_json
metadata_completeness_score
metadata_warnings_json
```

## Required query-level fields

Every query execution must store:

```text
query_run_id
source_database
query_label
query_string
query_role
access_mode
execution_mode
run_started_at
run_completed_at
search_url
filters_applied_json
result_count_reported
records_harvested
records_imported_raw
records_enriched
records_failed
warnings_json
human_intervention_required
status
```

---

# 5. Database Design for Collection

Create or replace collection tables.

## 5.1 `query_runs`

Stores every executed query.

```text
query_run_id TEXT PRIMARY KEY
protocol_version_id TEXT
source_database TEXT
query_label TEXT
query_role TEXT
query_string TEXT
access_mode TEXT
execution_mode TEXT
run_started_at TEXT
run_completed_at TEXT
search_url TEXT
filters_applied_json TEXT
result_count_reported INTEGER
records_harvested INTEGER
records_imported_raw INTEGER
records_enriched INTEGER
records_failed INTEGER
warnings_json TEXT
human_intervention_required INTEGER
status TEXT
```

Allowed status:

```text
not_started
running
completed
completed_with_warnings
failed
manual_pending
waiting_for_login
waiting_for_export
no_results_found_with_note
skipped_with_justification
```

## 5.2 `raw_records`

Stores source output exactly as captured.

```text
raw_record_id TEXT PRIMARY KEY
query_run_id TEXT
source_database TEXT
source_record_id TEXT
source_url TEXT
raw_title TEXT
raw_authors TEXT
raw_year TEXT
raw_journal TEXT
raw_doi TEXT
raw_pmid TEXT
raw_pmcid TEXT
raw_abstract TEXT
raw_publication_type TEXT
raw_language TEXT
raw_metadata_json TEXT
harvested_at TEXT
raw_hash TEXT
```

Important:

```text
raw_records are never edited after insertion.
```

If enrichment corrects metadata, write to normalized/enriched table, not raw table.

## 5.3 `normalized_records`

Stores cleaned metadata.

```text
record_id TEXT PRIMARY KEY
raw_record_id TEXT
query_run_id TEXT
source_database TEXT
source_record_id TEXT
title TEXT
title_normalized TEXT
authors_raw TEXT
first_author TEXT
year INTEGER
journal TEXT
doi TEXT
doi_normalized TEXT
pmid TEXT
pmcid TEXT
abstract TEXT
publication_type TEXT
language TEXT
country TEXT
keywords_json TEXT
mesh_terms_json TEXT
landing_page_url TEXT
pdf_url TEXT
is_open_access INTEGER
oa_status TEXT
metadata_completeness_score REAL
metadata_warnings_json TEXT
normalization_status TEXT
created_at TEXT
updated_at TEXT
```

Allowed `normalization_status`:

```text
complete
partial
needs_enrichment
failed
```

## 5.4 `record_enrichment_log`

Stores every enrichment attempt.

```text
enrichment_id TEXT PRIMARY KEY
record_id TEXT
enrichment_source TEXT
identifier_used TEXT
identifier_value TEXT
fields_updated_json TEXT
warnings_json TEXT
status TEXT
started_at TEXT
completed_at TEXT
```

Allowed `enrichment_source`:

```text
PubMed
EuropePMC
Crossref
OpenAlex
SemanticScholar
Unpaywall
DOIResolver
Manual
```

Allowed status:

```text
success
partial_success
not_found
failed
skipped_no_identifier
```

## 5.5 `collection_qa_findings`

Stores collection-specific QA findings.

```text
collection_qa_id TEXT PRIMARY KEY
record_id TEXT
query_run_id TEXT
severity TEXT
finding_type TEXT
message TEXT
recommended_action TEXT
status TEXT
created_at TEXT
resolved_at TEXT
resolution_note TEXT
```

Finding types:

```text
missing_title
missing_abstract
missing_identifier
missing_year
suspicious_year
missing_source_url
missing_query_link
missing_raw_metadata
identifier_conflict
year_conflict
doi_conflict
pmid_conflict
abstract_unavailable_after_enrichment
source_result_count_mismatch
```

---

# 6. Source Adapter Contract

Every source adapter must implement the same interface.

```python
class SourceAdapter:
    source_name: str
    access_mode: str

    def run_query(self, query: QuerySpec) -> QueryRunResult:
        ...

    def harvest_records(self, query_run: QueryRunResult) -> list[RawRecord]:
        ...

    def normalize_record(self, raw_record: RawRecord) -> NormalizedRecord:
        ...

    def enrich_record(self, record: NormalizedRecord) -> NormalizedRecord:
        ...

    def validate_record(self, record: NormalizedRecord) -> list[CollectionQAFinding]:
        ...
```

Required output objects:

```python
QueryRunResult
RawRecord
NormalizedRecord
CollectionQAFinding
```

All adapters must produce records compatible with the same schema, even if some fields are null.

---

# 7. Source-Specific Collection Requirements

## 7.1 PubMed

Preferred API:

```text
NCBI E-utilities
```

Must collect:

```text
PMID
title
authors
journal
year
abstract
publication types
DOI
PMCID if available
MeSH terms if available
language
PubMed URL
raw XML/JSON
```

PubMed is the gold source for correcting:

```text
year
abstract
journal
PMID-linked metadata
```

If PMID exists in any other source, run PubMed enrichment.

## 7.2 Europe PMC

Must collect:

```text
title
authors
journal
year
abstract if available
PMID
PMCID
DOI
Europe PMC ID
fullTextUrlList if available
isOpenAccess
source URL
raw JSON/XML
```

Special rule:

```text
Do not trust Europe PMC year blindly if PMID or DOI exists.
If PMID exists, verify year via PubMed.
If DOI exists, verify year via Crossref/OpenAlex.
If year conflicts, mark year_conflict and prefer PubMed > Crossref > OpenAlex > Europe PMC.
```

## 7.3 Crossref

Used mainly for metadata enrichment, not primary biomedical eligibility.

Must collect:

```text
title
authors
journal/container-title
published year
DOI
URL
abstract if available
type
raw JSON
```

Special rule:

```text
Crossref records without PMID/abstract should not become screening-ready until enrichment attempt is completed.
```

## 7.4 OpenAlex

Used for metadata/citation enrichment.

Must collect:

```text
title
authors
year
DOI
OpenAlex ID
journal/source
abstract_inverted_index if available
URL
concepts
citation count
raw JSON
```

If abstract is provided as inverted index, reconstruct text and store as abstract.

## 7.5 Semantic Scholar

Used for metadata/citation enrichment.

Must collect:

```text
title
authors
year
abstract
DOI
PMID if available
venue
paperId
url
citationCount
publicationTypes
raw JSON
```

## 7.6 Unpaywall / OA Resolver

Used for full-text status enrichment.

Must collect:

```text
doi
is_oa
oa_status
best_oa_location
pdf_url
landing_page_url
license
host_type
raw JSON
```

## 7.7 BVS/LILACS

Browser/manual export source.

Must capture:

```text
query string
search URL
result count
database filter applied, e.g. LILACS
exported file
all exported citation fields
raw export file path
```

If export lacks abstracts/DOI/PMID, mark:

```text
needs_enrichment
```

## 7.8 SciELO

Must collect:

```text
title
authors
journal
year
DOI
abstract
language
URL
PDF URL if available
raw metadata/export
```

## 7.9 IMEMR

Likely manual/browser source.

Must collect whatever is available and preserve raw source.

If abstracts/DOIs are absent:

```text
needs_enrichment
```

## 7.10 Google Scholar

Supplementary only.

Do not scrape aggressively.

Must collect:

```text
title
authors
year
venue
url
snippet
citation URL if exported
manual/Zotero export file path
query label
rank position, if available
```

Every Google Scholar record must be marked:

```text
supplementary_source = true
```

---

# 8. Metadata Completeness Score

Every normalized record receives a metadata completeness score.

Suggested scoring:

```text
title: 20 points
PMID or DOI or PMCID: 20 points
abstract: 20 points
year: 10 points
journal: 10 points
authors: 10 points
source URL: 5 points
raw metadata JSON: 5 points
```

Total:

```text
0–100
```

Readiness classes:

```text
>= 80: screening_ready
60–79: screening_ready_with_warning
40–59: enrichment_needed
< 40: collection_problem
```

---

# 9. Collection QA Gate

Before deduplication unlocks, the app must run collection QA.

## Required QA checks

```text
query run has query string
query run has source
query run has result count or documented unavailable count
record has title
record has source/query provenance
record has raw metadata
record has identifier or title/year fallback
PMID records enriched via PubMed
DOI-only records enriched via Crossref/OpenAlex/Unpaywall
Europe PMC year conflicts checked
abstract missing rate reported
records with missing abstracts routed to enrichment queue
records with suspicious year flagged
```

## Blocking collection QA

Block deduplication if:

```text
>10% records missing title
>25% records missing source/query provenance
query run lacks query string
query run lacks source name
raw metadata not persisted for API sources
PMID records not enriched through PubMed
```

## Non-blocking warnings

Do not block if:

```text
abstract unavailable after enrichment
DOI absent but PMID present
PDF unavailable
Google Scholar rank unavailable
```

---

# 10. Enrichment Before Deduplication

The app must enrich before deduplication.

Priority:

```text
1. Use PMID to fetch PubMed metadata.
2. Use DOI to fetch Crossref/OpenAlex/Unpaywall metadata.
3. Use PMCID to fetch Europe PMC/full text metadata.
4. Use title + year + author for fuzzy metadata search only if no identifier.
```

Enrichment should fill:

```text
abstract
DOI
PMCID
journal
year
publication type
URL
OA status
PDF URL
```

---

# 11. Correct Handling of Year Conflicts

If multiple sources disagree on year:

Preferred source order:

```text
PubMed
Crossref
journal/publisher
OpenAlex
Semantic Scholar
Europe PMC
Google Scholar
manual
```

If conflict remains:

```text
store preferred_year
store source_years_json
create year_conflict warning
```

Do not use year for exclusion until resolved.

---

# 12. Correct Handling of Abstracts

Abstract collection hierarchy:

```text
PubMed abstract
Europe PMC abstract
Semantic Scholar abstract
OpenAlex reconstructed abstract
publisher abstract, if legally accessible
manual abstract
```

If no abstract is available after enrichment:

```text
abstract_status = unavailable_after_enrichment
```

Do not exclude automatically.

Such records go to:

```text
title_only_screening_queue
```

---

# 13. Correct Handling of Raw Metadata

For every API source, persist raw response.

Examples:

```text
raw_pubmed_xml
raw_europepmc_json
raw_crossref_json
raw_openalex_json
raw_semantic_scholar_json
raw_unpaywall_json
```

For browser/manual sources, persist:

```text
exported RIS/BibTeX/CSV file path
parsed raw fields
screenshot path
search URL
```

---

# 14. Collection Dashboard

The Search Collection phase must show:

```text
sources completed
query runs completed
records harvested
records normalized
records enriched
records collection-QA passed
missing abstract rate
missing identifier rate
suspicious year count
source result count mismatch
metadata completeness distribution
```

Per source:

```text
records harvested
records with PMID
records with DOI
records with abstract
records with journal
records with suspicious year
records enriched
QA status
```

---

# 15. Collection Readiness Report

Before allowing deduplication, generate:

```text
collection_readiness_report.md
collection_metadata_summary.csv
query_run_log.csv
collection_qa_findings.csv
```

The report should include:

```text
total raw records
total normalized records
records by source
records by query
abstract availability
identifier availability
year conflict summary
metadata completeness score distribution
enrichment success/failure
collection QA pass/warning/blocking status
```

---

# 16. Do Not Repair Old Database

For this implementation cycle:

```text
Do not attempt to repair the previous 2249/1572 dataset.
Do not migrate old records as study data.
Use old CSVs only as development test fixtures.
```

The old data can be placed in:

```text
tests/fixtures/old_collection/
```

Use it to write tests that prevent repeating the same failure.

---

# 17. Tests Based on Observed Failure

Add tests using the old CSVs as fixtures.

## Test: raw collection must include abstract field

```text
test_raw_records_schema_includes_abstract
```

## Test: normalized records must include DOI/journal/source URL fields

```text
test_normalized_records_include_required_metadata_fields
```

## Test: Europe PMC year 2024 not blindly accepted

```text
test_europepmc_year_checked_against_pubmed_when_pmid_exists
```

## Test: PMID enrichment fills abstract

```text
test_pmid_enrichment_attempted_for_pubmed_identified_records
```

## Test: collection QA blocks missing query provenance

```text
test_collection_qa_blocks_missing_query_string
```

## Test: deduplication locked before collection QA

```text
test_deduplication_locked_until_collection_qa_complete
```

## Test: missing abstracts routed to title-only screening

```text
test_missing_abstract_after_enrichment_goes_to_title_only_queue
```

---

# 18. Acceptance Criteria

This reform is complete when:

```text
collection stores raw metadata for every API record
collection stores query-level result counts
collection stores source/query provenance for every record
abstract field exists from the beginning
DOI/PMID/PMCID/journal fields exist from the beginning
PMID records are enriched via PubMed before deduplication
DOI-only records are enriched via Crossref/OpenAlex/Unpaywall
Europe PMC year conflicts are detected
metadata completeness score is calculated
collection QA runs before deduplication
deduplication remains locked until collection QA passes or warnings are accepted
old broken collection CSVs are used as regression fixtures
```

---

# 19. Core Methodological Statement

The collection reform supports this methodological claim:

> The agent does not merely collect article titles. It captures query-level provenance, source-native metadata, raw source records, standardized bibliographic fields, enrichment attempts, and collection QA findings before any deduplication or study selection occurs.

This is the minimum required for a serious automated research assistant.
