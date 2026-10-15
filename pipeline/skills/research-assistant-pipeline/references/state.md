# Project state and continuity

## Canonical files

| File | Purpose |
|---|---|
| `START_HERE.md` | Entry point and reading order for a fresh conversation |
| `project.json` | Structured protocol/phase/approval state |
| `CURRENT_STATE.md` | Human-readable status, blockers and next action |
| `PIPELINE_LOCK.json` | Exact tool version and hashes of the bundled snapshot |
| `_pipeline/skill/` | Pinned full skill; source of workflow instructions for this project |
| `protocol/PROTOCOL.md` | Project-specific scientific protocol |
| `protocol/RULES.csv` | Rules, rationale, sources, tests and approval scope |
| `protocol/EXECUTION_PLAN.md` | Local meaning, applicability and gates of phases 0–11 |
| `protocol/STANDARDS.md` | Methods/reporting/appraisal sources actually consulted |
| `audit/approvals.jsonl` | Actual human decisions with provenance |
| `audit/decisions.jsonl` | Proposals, reasoning and operational decisions |
| `audit/amendments.jsonl` | Changes, reasons, impact and reapproval |
| `audit/tool_use.csv` | Actual pipeline/AI/model role and verification |
| `handoff/LATEST.md` | Precise resume instructions |
| `qa/findings.json` | Open/resolved findings, severity and evidence |

Scaffolding is not completed research. A heading or empty table proves no scientific
work. Populate these files as work occurs, preserving prior versions via git or another
explicit version history. Raw evidence is immutable; derived artifacts are versioned.

## Approval record

Each nonempty line in `audit/approvals.jsonl` is a JSON object with:
`id, kind, decision, actor_role, actor_name, decided_at, source_ref, scope,
protocol_version, artifacts` and `phase_id` when phase-specific.

- `actor_role` must be `human`; `actor_name` identifies the real researcher.
- `decision` is `approved` or `rejected`; only approved records can satisfy gates.
- Kinds: `protocol`, `phase_close`, `not_applicable`, `extraction`, `mapping`,
  `data_freeze`, `release`, `amendment`, `migration` or a clearly documented extension.
- `source_ref` locates the actual decision (message ID/date, signed record or other
  honest provenance). Do not invent signatures or message identifiers. When a host
  exposes no message ID, record its actual date and a concise faithful decision
  excerpt/context, without unnecessary personal information.
- `scope` specifies precisely what was approved. Include reviewed artifacts as
  objects with `path` (project-relative) and `sha256`. Preserve approved versions;
  changing a file means its old approval no longer proves approval of the new content.
- A decision may be transcribed by the assistant, but the human must actually have
  made it. Structural validation cannot authenticate the provenance or identity.

For `extraction`/`mapping` approvals used by included extraction rows, also record
`verified_fields`: a list of the exact reviewed `item_id`, `field`, `value`, `unit`,
`source_id`, `source_location` and `status` strings. This binds approval to specific
facts rather than allowing an unrelated approval ID to authorize other data. Preserve
the reviewed artifact as a snapshot; later additions to the working extraction table
must not alter that approved snapshot. Freeze/release artifacts must be among the
exact path/hash pairs covered by their respective human decisions.

## Manifest changes

The distribution manifest hashes the scientific/workflow payload. Two fixed,
presentation-only paths, `agents/openai.yaml` and `assets/icon.svg`, are excluded
because a host may regenerate them at installation. They must contain no scientific
rules. `PIPELINE_LOCK.json` still hashes every file in the actual project snapshot,
including those presentation files, so subsequent snapshot changes are detected.

The bootstrap starts at Phase 0 with a draft protocol, all scientific approvals null,
and no data lock. To approve the protocol, save its reviewed files, record the actual
approval, and set `protocol.status=approved`, `protocol.approval_id` and its version.
Close Phase 0 with that decision/evidence, then open Phase 1.

For each closed phase, set status, applicability, evidence file paths and
`closure_approval_id`. Completed-with-note needs `closure_note`; not-applicable needs
an approved `not_applicable_reason`. Keep one current phase; later dependent phases
stay locked until prerequisites close. Prepared draft artifacts do not close a phase.

Set `data_freeze` to an object containing `protocol_version`, `approval_id` and
`artifacts` (path/hash objects) when accepted inputs are locked. Any included
extraction row needs verified/corrected status, source/location and human approval.
Use project-specific checks in addition to the supplied structural validator.

Extraction CSVs must retain the template's required columns. Set `analysis_included`
explicitly to `true` or `false` for every row; included source IDs must resolve to
unique entries in `evidence/source_registry.csv`. Do not mark exploratory Phase 0
material as accepted analytic inputs before protocol approval. Phase 9 completion
requires a data freeze; an open high/critical/scientific-stop finding invalidates it.
QA findings use severity `info`, `low`, `medium`, `high`, `critical` or
`scientific_stop`, and status `open`, `in_progress` or `resolved`. Record a paused
current phase as `blocked`, not `locked` (which denotes a future phase).

Final `release.status=release_candidate` needs the `release` approval and artifact
hashes, all applicable phases closed and publication QA evidence. Approval for external
submission remains a separate user instruction. Never manufacture any of these fields
to make a checker pass.

## Amendments and migration

Append an amendment with ID/date, trigger, old/new versions, exact changes, reasons,
whether relevant results were already seen, affected artifacts/phases, human decision
and revalidation plan. Preserve old protocol and approved snapshots. Reset affected
closures/locks/release approvals; mark dependent results superseded. Reapprove the
current protocol and affected gates before using the revised results.

For a pipeline update, compare versions, preserve the former lock/snapshot outside
the active snapshot, document changes/impact and obtain a migration decision. Never
auto-update from a moving branch in the middle of a study. Researcher-specific rules
belong in `protocol/`, not edits to the pinned upstream snapshot.

## Session handoff

Reconcile `project.json` and `CURRENT_STATE.md`. If they conflict, inspect approvals
and evidence and stop dependent scientific work until resolved; do not guess from
file timestamps. Record current protocol/phase, accepted artifacts, exact unresolved
decisions, limitations, next step, and what was locally saved versus remotely synced.
New sessions should need these files rather than previous conversational memory.
