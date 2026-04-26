# Continuous Workflow, Gating, and UI

## Purpose
Implement a continuous workflow where phases unlock sequentially. The user cannot skip ahead without completing or explicitly closing the current phase.

## Main UI
Single main screen:
```text
Workflow Console
```
It displays current phase, phase progress, locked phases, required tasks, blocking issues, next action, audit trail, and a phase-specific work panel.

## Phase List
```text
0. Research Plan
1. Search Collection
2. Deduplication
3. Title/Abstract Screening
4. Full-Text Retrieval
5. Full-Text Eligibility
6. Data Extraction
7. Extraction Verification
8. Diagnosis Mapping
9. QA Sentinel
10. Analysis
11. Manuscript / Abstract Draft
```

## Phase Table
Create `workflow_phases`:
```text
phase_id
phase_order
phase_name
status
started_at
completed_at
completion_note
skip_justification
locked_reason
updated_at
```
Allowed statuses: locked, available, in_progress, blocked, completed, completed_with_note, skipped_with_justification.

## Gating Rules
```text
Phase 0 available at first run.
Phase 1 unlocks after Research Plan approved.
Phase 2 unlocks after all required sources are completed, unavailable_with_note, or skipped_with_justification.
Phase 3 unlocks after deduplication completed.
Phase 4 unlocks after all unique records have title/abstract decision.
Phase 5 unlocks after full-text retrieval status is complete for all include/maybe records.
Phase 6 unlocks after full-text eligibility is complete.
Phase 7 unlocks after extraction suggestions/tasks are created.
Phase 8 unlocks after all required extraction fields are verified/corrected/rejected/unavailable_with_note.
Phase 9 unlocks after diagnosis mapping is complete.
Phase 10 unlocks after QA passed or high/critical findings resolved/accepted with note.
Phase 11 unlocks after analysis dataset built and QA passed.
```

## Locked UI Behavior
Example:
```text
Research Plan          ✅ completed
Search Collection      🟦 in progress
Deduplication          🔒 locked — required searches not completed
Title/Abstract         🔒 locked
Full-Text Retrieval    🔒 locked
```
The user may view read-only summaries of later phases, but action buttons are disabled.

## Override
Create `workflow_overrides`: override_id, phase_id, requested_action, reason, created_at, created_by. Button: `Override and continue with note`. Show warning that this will be recorded and may affect methodological defensibility.

## Next Action Engine
Create `workflow/next_action.py` with `get_next_action(conn) -> dict` returning phase, priority, message, target_component, blocking.

## Acceptance Criteria
The app starts at Research Plan; locked later-phase actions are disabled; each phase has explicit completion criteria; next action is always visible; phase transitions are logged; override requires justification.
