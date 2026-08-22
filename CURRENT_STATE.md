# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**

Last updated: **2026-08-22**  
Writing hub branch: **`phase11-writing`**  
Frozen analysis branch: **`phase6-analysis`**  
Current safe-resume snapshot: **`docs/PHASE11_PROGRESS_SNAPSHOT_2026-08-22_WRITING_SPLIT.md`**  
Current phase status: **PHASE 11 — WRITING SPLIT INTO DEDICATED ABSTRACT + MANUSCRIPT STREAMS**

## 1. Mandatory routing

Read:

1. `CURRENT_STATE.md`
2. `docs/PHASE11_PROGRESS_SNAPSHOT_2026-08-22_WRITING_SPLIT.md`
3. `docs/PHASE11_WRITING_SPLIT_HANDOFF_2026-08-22.md`

Then choose exactly one writing stream:

### SHA abstract

Branch: `phase11-sha-abstract`  
First file: `docs/PHASE11_HANDOFF_SHA_ABSTRACT_CHAT.md`

### Full manuscript/article

Branch: `phase11-manuscript`  
First file: `docs/PHASE11_HANDOFF_MANUSCRIPT_CHAT.md`

The hub `phase11-writing` preserves shared routing and guardrails; it should not become a third independent drafting stream.

## 2. Frozen Phase 6 science

Canonical primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA: `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

Primary set:

- 28 PRIMARY_POOLABLE independent units;
- denominator 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD outcomes;
- 1,015 Expanded CAN-CCHD outcomes.

Strict CAN-CCHD: median-study 17.0% (95% CI 3.1%-46.8%), marginal mean 33.8%, tau 3.369, prediction interval approximately 0.03%-99.34%.

Expanded CAN-CCHD: median-study 69.4% (57.7%-81.4%), marginal mean 65.8%, tau 1.110, prediction interval 20.4%-95.2%.

No Phase 6 scientific value may be silently altered during writing. A genuine scientific correction requires explicit amendment and controlled rerun.

## 3. Shared scientific package

Start all scientific verification from:

- `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
- `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
- `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
- `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
- `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
- `docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`

## 4. Existing abstract artifact

`docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.1.md`

Status: `draft_requires_human_review`. It is the starting point for the abstract stream only.

The manuscript stream must be built directly from the frozen Phase 6 package, not by expanding the conference abstract.

## 5. Cross-document rule

Abstract and manuscript are sibling deliverables. Before final submission/publication, run a consistency audit for terminology, outcome definitions, counts, pooled estimates and conclusions.

## 6. Critical legacy firewall

Legacy Browser Agent/app databases remain historical only and cannot be used to alter current scientific values, diagnoses, denominators, numerators, eligibility decisions or weights.

## 7. One-line handoff

**PHASE 11 WRITING SPLIT COMPLETE. Use `phase11-sha-abstract` for the SHA abstract and `phase11-manuscript` for the full article; both must remain anchored to the frozen Phase 6 analysis.**
