# Phase 1 — Search Collection and Browser Operator Agent

## Purpose
Collect studies from all predefined sources based on the approved protocol. The agent performs or guides all non-decisional search tasks, logs every action, and preserves search provenance.

## Source Access Modes
Each source must be classified:
```text
api_autonomous
browser_autonomous
browser_supervised
supervised_login
manual_import_only
```
API autonomous: PubMed, Europe PMC, Crossref, OpenAlex, Semantic Scholar, Unpaywall/OA resolver.
Browser supervised/variable: LILACS/BVS, SciELO if API unavailable, IMEMR, Google Scholar.
Supervised login: Embase, Scopus, Web of Science, institutional proxy.

## Search Collection UI
The phase shows source cards in required order. Each card shows source name, access mode, required/optional/supplementary status, planned queries, status, records found/imported, warnings, and human action required.

Allowed source statuses:
```text
not_started
ready
running
waiting_for_login
waiting_for_human_export
completed
completed_with_warnings
no_results_found_with_note
unavailable_with_note
skipped_with_justification
failed
```
Deduplication remains locked until all required sources are completed, unavailable with note, or skipped with justification.

## Browser Operator Agent
Create module:
```text
can_cchd/browser_agent/
  agent.py
  browser_controller.py
  source_profiles.py
  action_logger.py
  result_counter.py
  export_handler.py
  import_bridge.py
  interventions.py
  snapshots.py
```
Use Playwright. Add `playwright>=1.40.0` to requirements and document:
```bash
python -m playwright install chromium
```

## Agent Run Table
Create `agent_runs`:
```text
agent_run_id
protocol_version_id
phase_id
status
execution_mode
current_source
current_query_label
current_action
started_at
completed_at
records_found_total
records_imported_total
warnings_count
human_interventions_count
summary
```
Allowed status: not_started, running, paused, waiting_for_human, completed, completed_with_warnings, failed, cancelled.

## Action Log Table
Create `agent_action_log`:
```text
action_id
agent_run_id
timestamp
source_database
source_access_mode
action_type
action_status
query_label
query_string
url
result_count
records_exported
records_imported
download_path
screenshot_path
html_snapshot_path
message
error_message
requires_human_intervention
```
Allowed action types:
```text
open_source
wait_for_manual_login
manual_login_confirmed
enter_query
run_query
capture_result_count
apply_filter
open_export_menu
export_records
download_file
import_records
deduplicate_preview
pause_for_human
error
```

## Live Agent UI
When running, show cockpit panel:
```text
Agent status
Execution mode
Current source
Current query
Current action
Records found
Records imported
Warnings
Human intervention needed
```
Observation panel shows latest screenshot, current URL, last action, selector clicked, downloaded file path.

If local headed browser: show “Visible browser window open — observe directly.”
If Codespaces/headless: update screenshot after each meaningful action.

## Supervised Login
For Embase/Scopus/Web of Science:
```text
agent opens platform
agent pauses
user logs in manually
user clicks Continue after login
agent resumes
```
Do not store credentials. Do not capture login screenshots unless explicitly allowed.

## Manual Export Fallback
If source cannot export automatically:
```text
agent pauses
shows instructions
user exports file
user uploads file
agent imports and logs
```

## Source Completion
A source is complete when all planned queries are completed, completed_with_warnings, no_results_found_with_note, or skipped_with_justification. It is not complete if any query is not_started, running, waiting_for_login, waiting_for_human_export, or failed_unresolved.
