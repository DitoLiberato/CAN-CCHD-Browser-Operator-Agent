# Phase 4.5 — corrected deduplication and membership rebuild

Date: 2026-08-21
Status: REQUIRED BEFORE PHASE 4 CLOSURE

## Why the previous reconciliation plan is superseded

The prior plan attempted to recover the historical 156-record Phase 4 roster (`Nxxx`) and reconcile the current report-level ledger against it. That plan is now superseded.

The project history and repository architecture show that the historical Nxxx/Phase 3 stack was produced downstream of a deduplication implementation that still operated on the legacy `records` table. The locked architecture correction explicitly states that deduplication must instead consume `normalized_records`, preserve every source/query occurrence, and create deduplicated study entities plus provenance links.

Therefore the old 156-member Nxxx roster is not a valid gold-standard membership list. Reconstructing it exactly would reproduce a known-invalid deduplication state.

## Binding decision

Do **not** use the old 156 Nxxx roster as the final Phase 4 denominator.

Instead:

1. recover the authoritative 327-record collection at the `normalized_records` level;
2. rerun deduplication using the corrected architecture;
3. create a new set of unique bibliographic reports/studies with complete provenance links;
4. project all existing Phase 4 full-text adjudications onto that corrected deduplicated set by PMID, DOI, PMCID, exact normalized title, and manual identity review where necessary;
5. adjudicate only genuinely unmatched corrected studies;
6. freeze the corrected Phase 4 membership and only then proceed to structured extraction/meta-analysis.

The historical counts `49 include + 107 maybe = 156` remain useful as an audit trail of what happened, but **not as a binding membership denominator**.

## Evidence for this correction

Repository design documentation states:

- Phase 1 collection source of truth = `normalized_records`;
- legacy deduplication incorrectly used `records`;
- corrected dedup must create `unique_studies`, `unique_study_record_links`, `dedup_groups`, `dedup_group_members`, and a dedup audit log;
- normalized/raw records must never be deleted or overwritten;
- exact duplicates may be merged only while preserving all source/query provenance;
- fuzzy/possible duplicates require review;
- screening is locked until deduplication is complete.

The legacy `can_cchd/dedup/manager.py` confirms the defect directly: it queries `records`, creates `studies`, and links through legacy `study_links`.

## Phase 4.5 target data model

### Source occurrence

`normalized_records`

One row per normalized source/query bibliographic occurrence, linked to immutable `raw_records`.

### Corrected deduplicated report/study

`unique_studies`

One row per deduplicated bibliographic report/study identity.

### Provenance

`unique_study_record_links`

Every normalized occurrence remains linked to the deduplicated entity, retaining:

- raw record ID;
- query run;
- source database;
- query label;
- PMID/DOI/PMCID;
- URLs/OA locations;
- source-specific metadata.

### Phase 4 adjudication projection

Create a crosswalk:

| unique_study_id | canonical citation | linked normalized record(s) | linked Rxxx/report identity | prior Phase 4 decision | projection confidence | action required |
|---|---|---|---|---|---|---|

Allowed projection confidence:

- `exact_pmid`
- `exact_doi`
- `exact_pmcid`
- `exact_title`
- `title_author_manual_confirmed`
- `manual_identity_confirmed`
- `unmatched`

## Correct deduplication rules

Run exact grouping on `normalized_records` using, in order:

1. exact non-empty PMID;
2. exact normalized DOI;
3. exact non-empty PMCID;
4. exact normalized title when sufficiently long;
5. exact normalized title + first author when identifiers are absent.

Important: exact identifier groups are transitive. If record A shares PMID with B and B shares DOI with C, A/B/C belong to one connected duplicate component even if A and C do not share the same single identifier field. Deduplication must therefore operate on connected components, not create independent overlapping groups.

Fuzzy-title or possible-cohort similarities are **not automatically merged**. They are queued for manual review.

Companion reports of the same cohort remain separate bibliographic reports but are linked by a cohort/overlap register. Bibliographic deduplication and cohort-level non-independence are distinct operations.

## Preservation of existing Phase 4 work

The full-text adjudication already completed in the Rxxx tranche files is **not discarded**.

It becomes a reusable adjudication library. After corrected deduplication, each unique report is matched against this library. When identity is exact/confirmed, carry forward:

- INCLUDE/EXCLUDE/CONDITIONAL/COMPANION status;
- full-text notes;
- CCHD-negative failed-screen denominator;
- CAN-CCHD outcome information;
- transitional/healthy/not-ascertained categories;
- overlap/cohort flags;
- QA flags.

No report should be re-read simply because its identifier changed.

## Historical roster handling

The old Nxxx IDs and counts are preserved only as legacy audit metadata:

- raw corpus historically reported: 327;
- old Phase 3 routes: 49 `include`, 111 `maybe`, 9 `separate_analysis`;
- old active full-text queue: 156;
- old special IDs N228/N265/N298/N299 remain legacy references.

They do not define the corrected membership.

## Operational sequence

### 4.5A — Recover authoritative normalized collection

Obtain/export all rows from `normalized_records` and verify:

- expected collection size;
- all source/query provenance fields present;
- PMID/DOI/PMCID normalization;
- title normalization;
- no silent `LIMIT 500` export truncation;
- raw-record links intact.

### 4.5B — Correct exact deduplication

Build transitive exact duplicate components from normalized identifiers/title.

Output:

- dedup groups;
- member rows;
- representative selection;
- unique report entities;
- provenance links;
- audit log.

### 4.5C — Manual duplicate review

Review only:

- fuzzy-title groups;
- identifier conflicts;
- same-title/different-year anomalies;
- translations/alternate-language titles;
- true companion reports mistakenly proposed as duplicates.

### 4.5D — Project Phase 4 decisions

Crosswalk corrected unique reports against all adjudicated Rxxx/non-PubMed reports.

### 4.5E — Delta adjudication

Only corrected unique reports with no prior adjudication are sent to title/abstract/full-text review.

### 4.5F — Freeze membership

Produce final counts from the corrected unique-report set:

- eligible primary reports;
- excluded reports by reason;
- companion reports;
- secondary/sensitivity populations;
- zero-event eligible cohorts;
- unique quantitative cohorts after overlap resolution.

Then Phase 4 closes.

## Current technical constraint

The repository contains `data/processed/can_cchd_agent.db` (~25 MB), but the current GitHub connector cannot return the SQLite binary contents and this execution environment cannot access github.com directly. The visible File Library workbooks (`v0.1`–`v0.6`) are pre-dedup public-corpus snapshots and explicitly state that deduplication was blocked; they do not contain the authoritative 327-row normalized export.

Therefore the immediate blocking artifact is **the full `normalized_records` export (or an accessible copy of the SQLite database)**. Once that artifact is available in an executable/readable form, Phase 4.5A–F can be completed deterministically.

## Closure criterion

Phase 4 is complete only when:

1. corrected deduplication has been run from authoritative `normalized_records`;
2. every corrected unique report has a terminal Phase 4 disposition or documented out-of-scope status;
3. every carried-forward adjudication has an identity/provenance link;
4. all cohort overlaps are explicitly registered;
5. the corrected study-selection and extraction datasets are frozen and versioned.

No future `x/156` claim should be used as the primary completion metric.