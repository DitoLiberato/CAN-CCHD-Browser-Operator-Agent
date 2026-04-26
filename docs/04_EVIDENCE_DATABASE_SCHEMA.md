# Evidence Database Schema

## Purpose
Define the clean SQLite schema for the new gated app.

## Database Location
Default: `data/processed/can_cchd_agent.db`. Backups: `data/backups/can_cchd_agent_YYYYMMDD_HHMMSS.db`.

## Core Tables
### `research_plans`
```text
research_plan_id TEXT PRIMARY KEY
title TEXT
review_question TEXT
objective TEXT
primary_denominator TEXT
primary_outcome TEXT
secondary_outcomes_json TEXT
criteria_json TEXT
case_report_policy TEXT
status TEXT
created_at TEXT
approved_at TEXT
```
### `protocol_versions`
```text
protocol_version_id TEXT PRIMARY KEY
research_plan_id TEXT
version_number INTEGER
protocol_markdown TEXT
query_plan_json TEXT
criteria_json TEXT
approved_at TEXT
approved_by TEXT
```
### `workflow_phases`
```text
phase_id TEXT PRIMARY KEY
phase_order INTEGER
phase_name TEXT
status TEXT
started_at TEXT
completed_at TEXT
completion_note TEXT
skip_justification TEXT
locked_reason TEXT
updated_at TEXT
```
### `research_sources`
```text
source_id TEXT PRIMARY KEY
protocol_version_id TEXT
source_name TEXT
priority_order INTEGER
access_mode TEXT
required_status TEXT
status TEXT
rationale TEXT
records_found INTEGER
records_imported INTEGER
records_unique_after_dedup INTEGER
completed_at TEXT
closure_note TEXT
```
### `research_queries`
```text
query_id TEXT PRIMARY KEY
source_id TEXT
query_label TEXT
query_role TEXT
query_string TEXT
status TEXT
result_count INTEGER
records_imported INTEGER
run_at TEXT
notes TEXT
```

## Agent Tables
### `agent_runs`
```text
agent_run_id TEXT PRIMARY KEY
protocol_version_id TEXT
phase_id TEXT
status TEXT
execution_mode TEXT
current_source TEXT
current_query_label TEXT
current_action TEXT
started_at TEXT
completed_at TEXT
summary TEXT
```
### `agent_action_log`
```text
action_id TEXT PRIMARY KEY
agent_run_id TEXT
timestamp TEXT
source_database TEXT
source_access_mode TEXT
action_type TEXT
action_status TEXT
query_label TEXT
query_string TEXT
url TEXT
result_count INTEGER
records_exported INTEGER
records_imported INTEGER
duplicates_detected INTEGER
download_path TEXT
screenshot_path TEXT
html_snapshot_path TEXT
message TEXT
error_message TEXT
requires_human_intervention INTEGER
```
### `agent_interventions`
```text
intervention_id TEXT PRIMARY KEY
agent_run_id TEXT
source_database TEXT
query_label TEXT
intervention_type TEXT
message TEXT
status TEXT
created_at TEXT
resolved_at TEXT
resolution_note TEXT
```

## Evidence Tables
### `studies`
A unique study after deduplication.
```text
study_id TEXT PRIMARY KEY
title TEXT
first_author TEXT
year INTEGER
journal TEXT
doi TEXT
pmid TEXT
pmcid TEXT
country TEXT
study_design TEXT
status TEXT
created_at TEXT
updated_at TEXT
```
Status examples: candidate, merged_duplicate, screening_include, screening_maybe, screening_exclude, fulltext_pending, fulltext_include, fulltext_exclude, citation_mining_only, separate_analysis, included_quantitative, excluded_quantitative.

### `records`
A database hit/report.
```text
record_id TEXT PRIMARY KEY
study_id TEXT
source_id TEXT
query_id TEXT
source_database TEXT
source_record_id TEXT
title TEXT
authors TEXT
year INTEGER
journal TEXT
doi TEXT
pmid TEXT
pmcid TEXT
abstract TEXT
url TEXT
pdf_url TEXT
is_open_access INTEGER
metadata_json TEXT
imported_at TEXT
```
Many records may point to one study. Never delete records after merge.

## Review Tables
Implement:
```text
duplicate_groups
duplicate_group_members
study_links
screening_decisions
fulltext_records
extraction_tasks
extraction_fields
diagnosis_terms
diagnosis_mappings
qa_runs
qa_findings
analysis_dataset
draft_outputs
audit_log
```
Only verified/corrected extraction fields enter `analysis_dataset`.
