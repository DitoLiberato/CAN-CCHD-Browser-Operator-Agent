# CAN-CCHD Browser Operator Agent — Phase 1 Export, QA Flag Fixes, and New Deduplication Architecture

## Purpose

This document instructs Codex to implement the next critical corrections after the robust Phase 1 search collection reform.

Current state:

- Phase 1 now correctly collects into `raw_records`, `normalized_records`, `query_runs`, `record_enrichment_log`, `collection_qa_findings`, and `collection_qa_gate`.
- The exported CSV from Phase 1 showed high-quality PubMed records with PMIDs, DOIs, abstracts, and completeness score.
- However, the Phase 1 export currently appears to export only a limited view/top 500 records.
- The QA flags need refinement.
- The current deduplication phase still works on the old `records` table instead of the new `normalized_records` collection table.

Core decision:

> From this point forward, deduplication must be based on `normalized_records`, not the legacy `records` table.

Note on phase numbering:

- In the current app, deduplication is implemented as **Phase 2**.
- The user may refer to the post-collection study stack as **Phase 3** because it is the next practical work stage after search/collection.
- In code, repair the deduplication phase wherever it is implemented, currently `can_cchd/ui/phase2_dedup.py`, `can_cchd/dedup/matcher.py`, and `can_cchd/dedup/manager.py`.

---

# 1. Summary of Required Work

Implement these corrections:

```text
1. Fix QA flag logic in Phase 1.
2. Make Phase 1 export the full collection database, not only the top 500 rows.
3. Add explicit exports for normalized records, raw records, query runs, enrichment log, and collection QA.
4. Rebuild deduplication to consume `normalized_records`.
5. Create a new dedup output model: unique studies + study-record provenance links.
6. Preserve all source/query provenance through deduplication.
7. Ensure exact duplicates can be bulk-merged with researcher confirmation.
8. Ensure fuzzy duplicates are queued for manual review.
9. Lock screening until deduplication is complete.
```

---

# 2. Fix Phase 1 QA Flags

## 2.1 Current problem: year == current year

Current logic treats:

```text
year >= current_year
```

as suspicious.

This is too aggressive.

In the current year, recently published PubMed articles may legitimately have `year == current_year`.

## Required correction

Use:

```text
year > current_year
```

as a warning for impossible future year.

Use:

```text
year == current_year
```

as **info**, not warning, unless the source is known to have a suspicious default-year issue.

## Source-specific exception

For Europe PMC:

```text
year == current_year
```

or a mass concentration of a single year across many records may be suspicious if there is PMID/DOI disagreement.

Europe PMC-specific warning should be:

```text
Europe PMC year requires verification when PMID or DOI exists and enrichment source disagrees.
```

Do not mark all current-year PubMed records as suspicious.

## Required implementation changes

Modify:

```text
can_cchd/collection/base_adapter.py
can_cchd/collection/adapters/europepmc_adapter.py
can_cchd/collection/qa_gate.py
```

Rules:

```python
if norm.year and norm.year > current_year:
    finding_type = "future_year"
    severity = "warning"

elif norm.year == current_year:
    finding_type = "current_year"
    severity = "info"
```

For Europe PMC:

```python
if source_database == "Europe PMC" and norm.year == current_year and (norm.pmid or norm.doi):
    finding_type = "europepmc_year_needs_verification"
    severity = "warning"
```

But if PubMed enrichment confirms the same year:

```text
resolve or suppress the warning.
```

---

## 2.2 Current problem: completeness score uses identifier as proxy for raw metadata

Current scoring may give raw metadata credit based on presence of PMID/DOI.

That defeats one of the central goals of the reform: raw source metadata must be preserved.

## Required correction

Modify:

```text
can_cchd/collection/completeness.py
```

`calculate_completeness_score()` should receive or know whether raw metadata exists.

Preferred approach:

Add a field to `NormalizedRecord`:

```python
raw_metadata_available: int = 0
```

or calculate raw metadata availability during saving and pass it into the score function.

Scoring should be:

```text
title: 20
PMID or DOI or PMCID: 20
abstract: 20
year: 10
journal: 10
authors: 10
source URL or landing page URL: 5
raw_metadata_json exists: 5
```

Do **not** award raw metadata points merely because PMID/DOI exists.

If changing dataclass is too invasive, calculate score after raw record insert by checking `raw.raw_metadata_json`.

Example:

```python
norm.metadata_completeness_score = calculate_completeness_score(
    norm,
    raw_metadata_available=bool(raw.raw_metadata_json)
)
```

---

## 2.3 Current problem: enrichment_status remains `pending` even for complete records

Observed CSV:

```text
metadata_completeness_score = 100
abstract_status = available
enrichment_status = pending
```

This is confusing.

A complete PubMed record with title, identifier, abstract, year, journal, authors, URL, and raw metadata does not need enrichment.

## Required statuses

Use:

```text
not_required
needs_enrichment
enrichment_attempted
enriched
failed
```

## Required logic

When a normalized record is first created:

```python
if metadata_completeness_score >= 80 and abstract_status == "available":
    enrichment_status = "not_required"
elif missing abstract or missing identifier or missing journal or missing year:
    enrichment_status = "needs_enrichment"
else:
    enrichment_status = "pending"
```

Prefer avoiding `pending` altogether if possible.

Suggested normalized record enrichment status assignment:

```python
def determine_initial_enrichment_status(norm, raw_metadata_available: bool) -> str:
    if (
        norm.title
        and (norm.pmid or norm.doi or norm.pmcid)
        and norm.abstract
        and norm.year
        and norm.journal
        and norm.authors_raw
        and raw_metadata_available
    ):
        return "not_required"
    return "needs_enrichment"
```

After enrichment attempt:

```text
enriched
enrichment_attempted
failed
```

If a record remains without abstract after all attempts:

```text
enrichment_attempted
abstract_status = unavailable_after_enrichment
```

---

## 2.4 Collection QA Gate refinement

Modify:

```text
can_cchd/collection/qa_gate.py
```

The gate should report but not overblock.

Blocking:

```text
no normalized records
>10% missing title
>25% missing source/query provenance
query_runs missing query_string
raw metadata missing for API sources above threshold
```

Warnings:

```text
high missing abstract rate
high missing identifier rate
Europe PMC year conflicts
large enrichment queue remaining
source result count mismatch
```

Info:

```text
current-year publications
records without DOI but with PMID
records without PDF
Google Scholar supplementary records
```

Do not block because:

```text
abstract unavailable after enrichment
no free PDF
current-year article
no DOI if PMID exists
```

---

# 3. Full Phase 1 Export

## 3.1 Current problem

The Phase 1 UI export labeled "Download Full Dataset" currently uses a query with:

```sql
LIMIT 500
```

and exports only a few columns.

This is not a full export.

## Required correction

Modify:

```text
can_cchd/ui/phase1_search.py
```

The "Download Full Dataset" button must export **all** rows from `normalized_records` and all relevant columns.

Remove:

```sql
LIMIT 500
```

from the export query.

It is fine to keep a screen preview limited to 500 rows, but the CSV download must include all rows.

## Required UI distinction

Show two separate things:

```text
Preview: top 500 records
Download: full normalized_records export
```

UI wording:

```text
Preview below is limited to 500 rows for performance.
The download button exports all normalized records.
```

---

## 3.2 Full normalized records export

Export file:

```text
can_cchd_normalized_records_full.csv
```

Required columns:

```text
record_id
raw_record_id
query_run_id
source_database
source_record_id
title
title_normalized
authors_raw
first_author
year
journal
doi
doi_normalized
pmid
pmcid
abstract
abstract_status
publication_type
language
country
keywords_json
mesh_terms_json
landing_page_url
pdf_url
is_open_access
oa_status
metadata_completeness_score
metadata_warnings_json
normalization_status
enrichment_status
is_supplementary_source
created_at
updated_at
```

---

## 3.3 Additional Phase 1 exports

Add download buttons for:

```text
query_runs.csv
raw_records.csv
record_enrichment_log.csv
collection_qa_findings.csv
collection_qa_gate.json
collection_readiness_report.md
```

### Query runs export

Required columns:

```text
query_run_id
protocol_version_id
source_id
source_database
query_label
query_role
query_string
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

### Raw records export

Required columns:

```text
raw_record_id
query_run_id
source_database
source_record_id
source_url
raw_title
raw_authors
raw_year
raw_journal
raw_doi
raw_pmid
raw_pmcid
raw_abstract
raw_publication_type
raw_language
raw_metadata_json
harvested_at
raw_hash
```

For very large `raw_metadata_json`, optionally provide:

```text
raw_records_summary.csv
raw_records_full.csv
```

### Collection readiness report

Generate a markdown report with:

```text
total raw records
total normalized records
records by source
records by query
abstract availability
PMID/DOI/PMCID availability
journal/year availability
metadata completeness distribution
enrichment status distribution
collection QA status
warnings
blocking issues
recommended next step
```

---

# 4. Rebuild Deduplication Based on normalized_records

## 4.1 Current problem

Current deduplication code uses the legacy table:

```text
records
```

Current files affected:

```text
can_cchd/ui/phase2_dedup.py
can_cchd/dedup/matcher.py
can_cchd/dedup/manager.py
```

The new collection pipeline produces:

```text
normalized_records
```

Therefore, deduplication must use `normalized_records` as the source of truth.

---

## 4.2 New conceptual model

```text
normalized_records = source/query-level bibliographic occurrences
unique_studies = deduplicated studies/articles
study_record_links = provenance links from unique_study to all normalized_records
dedup_groups = proposed duplicate clusters
dedup_group_members = normalized_records belonging to a group
```

Do not delete `normalized_records`.

Do not overwrite raw provenance.

A deduplicated study must preserve:

```text
all source databases
all query labels
all query_run_ids
all raw_record_ids
all record_ids
all identifiers found
all URLs/PDFs/OA locations
```

---

# 5. New Deduplication Tables

Create new tables or migrate existing ones.

Preferred: create new tables to avoid confusion with legacy `records`.

## 5.1 `dedup_groups`

```sql
CREATE TABLE IF NOT EXISTS dedup_groups (
    dedup_group_id TEXT PRIMARY KEY,
    match_type TEXT,
    match_key TEXT,
    confidence REAL,
    status TEXT,
    representative_record_id TEXT,
    representative_study_id TEXT,
    created_at TEXT,
    reviewed_at TEXT,
    reviewer_note TEXT
);
```

Allowed `match_type`:

```text
exact_pmid
exact_doi
exact_pmcid
exact_title
exact_title_author
fuzzy_title
possible_overlapping_cohort
```

Allowed `status`:

```text
pending
auto_merge_ready
merged
merged_by_human
kept_separate
rejected
deferred
```

## 5.2 `dedup_group_members`

```sql
CREATE TABLE IF NOT EXISTS dedup_group_members (
    dedup_group_id TEXT,
    record_id TEXT,
    is_representative_candidate INTEGER DEFAULT 0,
    source_database TEXT,
    query_run_id TEXT,
    query_label TEXT,
    pmid TEXT,
    doi TEXT,
    pmcid TEXT,
    title TEXT,
    year INTEGER,
    journal TEXT,
    metadata_completeness_score REAL,
    PRIMARY KEY (dedup_group_id, record_id)
);
```

## 5.3 `unique_studies`

```sql
CREATE TABLE IF NOT EXISTS unique_studies (
    study_id TEXT PRIMARY KEY,
    representative_record_id TEXT,
    title TEXT,
    first_author TEXT,
    year INTEGER,
    journal TEXT,
    doi TEXT,
    pmid TEXT,
    pmcid TEXT,
    abstract TEXT,
    publication_type TEXT,
    language TEXT,
    source_databases_json TEXT,
    query_labels_json TEXT,
    query_run_ids_json TEXT,
    linked_record_count INTEGER,
    metadata_completeness_score REAL,
    dedup_status TEXT,
    screening_status TEXT DEFAULT 'not_started',
    created_at TEXT,
    updated_at TEXT
);
```

## 5.4 `unique_study_record_links`

```sql
CREATE TABLE IF NOT EXISTS unique_study_record_links (
    study_id TEXT,
    record_id TEXT,
    raw_record_id TEXT,
    query_run_id TEXT,
    source_database TEXT,
    query_label TEXT,
    link_reason TEXT,
    created_at TEXT,
    PRIMARY KEY (study_id, record_id)
);
```

## 5.5 `dedup_audit_log`

```sql
CREATE TABLE IF NOT EXISTS dedup_audit_log (
    audit_id TEXT PRIMARY KEY,
    timestamp TEXT,
    action_type TEXT,
    dedup_group_id TEXT,
    study_id TEXT,
    record_ids_json TEXT,
    previous_status TEXT,
    new_status TEXT,
    reason TEXT,
    reviewer_note TEXT
);
```

---

# 6. Exact Deduplication Rules

Run exact matching on `normalized_records`.

## Exact PMID

Group if:

```text
same non-empty PMID
```

## Exact DOI

Group if:

```text
same normalized DOI
```

Use `doi_normalized`, not raw DOI.

## Exact PMCID

Group if:

```text
same non-empty PMCID
```

## Exact title

Group if:

```text
same title_normalized
```

Only if title length is reasonable:

```text
len(title_normalized) >= 20
```

Do not require year for exact title if year quality is uncertain.

## Exact title + first author

Group if:

```text
same title_normalized
same normalized first_author
```

Useful when identifiers absent.

---

# 7. Bulk Merge Exact Groups

The UI should allow bulk merge for high-confidence exact groups.

Bulk merge-ready groups:

```text
exact_pmid
exact_doi
exact_pmcid
exact_title, if title is long and identical
```

User must see:

```text
number of groups
number of records
examples
representative selection logic
backup warning
checkbox confirmation
```

Required UI text:

```text
This will not delete normalized records. It will create unique studies and link all duplicate records to them, preserving source/query provenance.
```

Before merge:

```text
Offer database backup.
```

Bulk action:

```text
[ ] I understand that exact duplicate groups will be merged into unique studies while preserving all source records.
Button: Merge selected exact groups
```

---

# 8. Representative Record Selection

For each dedup group, select representative record using this priority:

```text
1. Highest metadata_completeness_score
2. Has abstract
3. Has PMID
4. Has DOI
5. Has PMCID
6. Has journal
7. Has publication year
8. Preferred source priority:
   PubMed > Embase > Scopus > Web of Science > Europe PMC > SciELO > LILACS/BVS > Semantic Scholar > OpenAlex > Crossref > Google Scholar
9. Longest title/abstract metadata if still tied
```

Representative selection should be deterministic.

Store:

```text
representative_record_id
```

in `dedup_groups`.

---

# 9. Merge Behavior

When merging a group:

```text
create one row in unique_studies
link all normalized_records to that study in unique_study_record_links
update dedup_group status to merged
write dedup_audit_log
```

Study fields should come from representative record.

But aggregate provenance fields should include all records:

```text
source_databases_json
query_labels_json
query_run_ids_json
linked_record_count
```

If multiple DOI/PMID conflicts exist within a group:

```text
do not auto-merge
mark group as pending
raise identifier_conflict warning
```

---

# 10. Fuzzy Deduplication Rules

Use fuzzy matching after exact groups are resolved or excluded from comparison.

Suggested library:

```text
rapidfuzz
```

If not installed, add:

```text
rapidfuzz>=3.0.0
```

## Fuzzy title matching

Use `title_normalized`.

Rules:

```text
score >= 0.97:
    likely duplicate
    require same first_author or same year or shared identifier evidence
score 0.90–0.96:
    possible duplicate
    manual review required
score < 0.90:
    ignore unless special heuristic
```

Do not use year as a mandatory hard filter if year quality is uncertain.

Use year as supportive evidence only.

## Fuzzy group statuses

```text
pending
merged_by_human
kept_separate
deferred
```

No fuzzy group should be auto-merged without human confirmation unless there is also shared PMID/DOI/PMCID.

---

# 11. Process Singletons

After all pending dedup groups are resolved:

```text
all normalized_records not linked to any unique_study become singleton unique_studies
```

Singleton creation must also preserve provenance via `unique_study_record_links`.

---

# 12. Deduplication UI Requirements

Rebuild:

```text
can_cchd/ui/phase2_dedup.py
```

Required tabs:

```text
1. Overview
2. Exact Duplicate Groups
3. Bulk Merge
4. Fuzzy Review
5. Singletons Preview
6. Deduplication Audit
7. Finalize Phase
```

## 12.1 Overview

Show:

```text
total normalized_records
records already linked to unique_studies
exact groups pending
fuzzy groups pending
identifier conflicts
estimated unique studies
collection QA status
```

If `collection_qa_gate.status` is not `pass` or `warn`:

```text
block deduplication
show message
```

## 12.2 Exact duplicate groups

Show grouped by:

```text
exact_pmid
exact_doi
exact_pmcid
exact_title
exact_title_author
```

For each group:

```text
match key
number of records
sources
query labels
representative candidate
metadata completeness
conflicts
```

## 12.3 Bulk merge

Checkboxes:

```text
select all exact_pmid
select all exact_doi
select all exact_pmcid
select all exact_title without conflicts
```

Require confirmation checkbox before action.

## 12.4 Fuzzy review

For each fuzzy group:

```text
side-by-side record cards
title
authors
year
journal
doi
pmid
source
query labels
abstract snippet
similarity score
AI/rule suggestion
```

Actions:

```text
merge
keep separate
defer
mark possible overlapping cohort
```

## 12.5 Singletons preview

Show records that will become unique studies if finalized.

## 12.6 Audit

Show `dedup_audit_log`.

## 12.7 Finalize phase

Allow phase completion only when:

```text
no pending exact groups
no pending fuzzy groups requiring review
all normalized_records linked to unique_studies or explicitly deferred with note
dedup report generated
```

---

# 13. Phase 3 / Screening Input

Screening must consume:

```text
unique_studies
```

not:

```text
records
normalized_records
```

The screening queue should show:

```text
one row per unique_study
linked_record_count
source_databases_json
query_labels_json
representative abstract
```

Prepare but do not fully implement screening here unless needed.

At minimum, ensure the next phase will receive `unique_studies`.

---

# 14. Backward Compatibility

Legacy tables may remain:

```text
records
studies
duplicate_groups
duplicate_group_members
study_links
```

But new deduplication must not depend on them.

Options:

```text
A. Leave legacy tables unused.
B. Create compatibility views from new tables.
```

Preferred:

```text
Leave legacy tables unused and label them deprecated.
```

If old UI code still expects `studies`, either:

```text
1. Update downstream phases to use `unique_studies`, or
2. Create a compatibility view/table after dedup finalize.
```

For now, prioritise correctness:

```text
unique_studies is the new source of truth after deduplication.
```

---

# 15. Required Exports After Deduplication

Generate:

```text
dedup_groups.csv
dedup_group_members.csv
unique_studies.csv
unique_study_record_links.csv
dedup_audit_log.csv
deduplication_report.md
```

`deduplication_report.md` should include:

```text
total normalized records
exact PMID groups
exact DOI groups
exact PMCID groups
exact title groups
fuzzy groups
groups merged
groups kept separate
singletons created
final unique studies count
source/query provenance preserved statement
```

---

# 16. Tests

Add tests:

```text
tests/test_phase1_export.py
tests/test_collection_qa_flags.py
tests/test_dedup_from_normalized_records.py
```

## 16.1 Phase 1 export tests

```text
test_full_normalized_export_has_no_limit
test_preview_query_can_have_limit_but_export_query_cannot
test_export_includes_abstract_and_identifier_columns
test_query_runs_export_available
test_raw_records_export_available
```

## 16.2 QA flag tests

```text
test_current_year_pubmed_is_info_not_warning
test_future_year_is_warning
test_europepmc_current_year_with_pmid_requires_verification
test_raw_metadata_score_requires_raw_metadata_json
test_complete_pubmed_record_enrichment_status_not_required
test_missing_abstract_after_enrichment_is_warning_not_blocking
```

## 16.3 Dedup tests

```text
test_exact_pmid_groups_created_from_normalized_records
test_exact_doi_groups_created_from_normalized_records
test_exact_pmcid_groups_created_from_normalized_records
test_exact_title_groups_created_from_normalized_records
test_dedup_does_not_use_legacy_records_table
test_bulk_merge_creates_unique_study
test_bulk_merge_preserves_all_record_links
test_unique_study_aggregates_source_databases
test_unique_study_aggregates_query_labels
test_fuzzy_match_requires_human_review
test_singletons_created_after_groups_resolved
test_screening_input_is_unique_studies
```

---

# 17. Acceptance Criteria

This implementation is complete when:

```text
QA no longer falsely flags current-year PubMed records as suspicious warnings
Europe PMC year conflicts are source-specific warnings
raw metadata completeness points require actual raw metadata
complete records receive enrichment_status = not_required
Phase 1 full export includes all normalized_records without LIMIT 500
Phase 1 export includes all important metadata columns
query_runs/raw_records/enrichment/QA exports exist
deduplication consumes normalized_records
legacy records table is not required for deduplication
exact duplicate groups are built from normalized_records
bulk merge creates unique_studies
all source/query provenance is preserved
fuzzy duplicates are reviewed manually
screening receives unique_studies, not raw/normalized records
deduplication report/export is generated
```

---

# 18. Methodological Statement

After these corrections, the app should be able to claim:

> The system collects source-native raw metadata and standardized enriched bibliographic records before any deduplication occurs. Deduplication is then performed on the normalized evidence collection, creating unique study records while preserving all source/query-level provenance. Current-year publications, missing free PDFs, and missing abstracts after enrichment are not treated as exclusionary errors, while source-specific metadata conflicts remain auditable QA warnings.

This is the minimum architecture required before formal screening begins.
