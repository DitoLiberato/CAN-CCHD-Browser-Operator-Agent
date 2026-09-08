# CAN-CCHD — CURRENT STATE / MANUSCRIPT STREAM

> **DEDICATED CHAT ENTRY POINT**

Last updated: **2026-09-08**  
Current branch: **`phase11-manuscript`**  
Parent writing hub: **`phase11-writing`**  
Frozen analysis branch: **`phase6-analysis`**  
Current status: **PHASE 11 — AUTHOR-LED MANUSCRIPT QA / PHASE 6 SCIENCE FROZEN**

## Mandatory reading order

1. `CURRENT_STATE.md`
2. `docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md`
3. `docs/PHASE11_PUBLICATION_QA_CANONIZATION_2026-09-08.md`
4. `docs/PHASE11_HANDOFF_MANUSCRIPT_CHAT.md`
5. `docs/PHASE11_WRITING_SPLIT_HANDOFF_2026-08-22.md`
6. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
7. `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
8. `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
9. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
10. `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
11. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
12. `docs/PROTOCOL_CORE_v1.0_RESTART_LOCK_RECONSTRUCTED.md`

## Mission

Build and author-review the full journal-neutral systematic-review/meta-analysis manuscript directly from the frozen scientific record.

Do not use the SHA abstract or award manuscript as the scientific template. Conference artifacts are historical derivatives; the journal manuscript is the fuller scientific record and must pass the reusable Phase-11 Publication QA gate.

## Frozen scientific anchors

Primary set: 28 independent units; denominator 1,999; Strict events 638; Expanded events 1,015.

Strict: median-study 17.0% (95% CI 3.1%-46.8%), marginal mean 33.8%, tau 3.369, prediction interval approximately 0.03%-99.34%.

Expanded: median-study 69.4% (57.7%-81.4%), marginal mean 65.8%, tau 1.110, prediction interval 20.4%-95.2%.

Any scientific-value inconsistency must be escalated explicitly; do not silently alter Phase 6 values during writing or publication QA.

## Publication-QA canon now mandatory

The post-deadline manuscript review identified reusable QA defects involving authorship/affiliations, endpoint hierarchy, reference order and claim support, citation coverage of study-level figures, analytic-unit/source identity, table hierarchy/formatting, abbreviations, AI-method transparency, search reproducibility, and rendered-artifact QA.

These lessons have been canonized prospectively in:

- `docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md`
- `docs/templates/PUBLICATION_QA_REPORT_TEMPLATE.md`
- `docs/PHASE11_PUBLICATION_QA_CANONIZATION_2026-09-08.md`

The core pipeline specifications and acceptance tests were also amended so these checks apply to future projects using the workflow.

## Important Phase-11 project-specific QA artifacts

- `docs/PHASE11_MANUSCRIPT_REFERENCE_CLAIM_AUDIT_v1.0.md`
- `docs/PHASE11_PRIMARY_FIGURE_REFERENCE_CROSSWALK_v1.0.md`
- `manuscript/supplements/CAN_CCHD_Supplementary_Search_Strategies_v1.0.md`
- latest committed manuscript source under `manuscript/`

The study-display audit established that the 28 primary analytic units derive from 27 unique primary publications because two site-level SIBEN units share one publication. Every study-level table/figure in a release candidate must preserve that source mapping.

## Phase-11 release rule

Phase 11 remains one numbered workflow phase but contains the mandatory sub-gate:

```text
Draft -> Publication QA -> Human author review -> Release candidate
```

`draft_requires_human_review` must not be promoted to release/submission-ready while any HIGH or SCIENTIFIC-STOP publication-QA finding remains open.

## Exact next movement

Continue author-led manuscript review, using the latest committed manuscript as the prose base and the frozen Phase-6 package as the scientific source of truth. For every substantive revision:

1. preserve frozen numeric results unless a scientific inconsistency is explicitly escalated;
2. apply the Publication QA Canon;
3. maintain reference-to-claim and analytic-unit-to-publication traceability;
4. rerender final DOCX/PDF after meaningful edits and inspect the complete artifact;
5. only then create a release candidate.

## One-line handoff

**Work only on the full article on `phase11-manuscript`; Phase 6 science is frozen, and all future manuscript/abstract release candidates must pass `docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md` before external use.**