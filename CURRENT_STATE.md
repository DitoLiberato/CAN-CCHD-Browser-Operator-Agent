# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> The repository default branch is **not** the authoritative location of the current scientific extraction state.
>
> Before interpreting any Phase file, CSV, snapshot, database, or historical note, read this file and then move to the current scientific branch named below.

Last updated: **2026-08-22**  
Current scientific branch: **`phase5-extraction`**  
Current safe-resume snapshot: **Snapshot T**  
Snapshot T commit: **`9293bd461998c74f883289b0661bb5f91d53f297`**  
Current phase status: **PHASE 5 FROZEN / READY FOR QUANTITATIVE SYNTHESIS**

## Mandatory new-chat procedure

1. Do **not** infer current scientific state from `main`.
2. Read the `phase5-extraction` branch.
3. On that branch, read `CURRENT_STATE.md` first.
4. Then read `docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_T.md`.
5. Follow the artifact-precedence rules in the branch-level `CURRENT_STATE.md` before using older extraction blocks or snapshots.

## Current frozen state

- frozen quantitative units: **76**;
- PRIMARY_POOLABLE: **28**;
- SENSITIVITY_ONLY: **40**;
- HOLD_PENDING_QA: **3**;
- NOT_POOLABLE: **5**.

Phase 5 has completed:

- 76/76 structural extraction;
- 76/76 d-TGA/TGA/ccTGA rerun;
- 76/76 conditional-lesion <=28-day audit;
- final hold-resolution attempt;
- post-rerun numerical overlay;
- final pool freeze.

**No post-freeze meta-analysis has yet been run.**

Exact next movement:

> Construct and QA the canonical 28-row PRIMARY_POOLABLE analysis-input dataset, using the post-rerun numeric overlay for changed units, then begin the prespecified quantitative synthesis.

## Critical legacy warning

The old Browser Agent/app/database artifacts in this repository are historical only. They must not be used to recover missing review evidence, denominators, numerators, diagnoses, eligibility, target mappings, overlap, PRISMA counts, or analysis weights.

## One-line handoff

**Switch to `phase5-extraction` and read its `CURRENT_STATE.md`; Snapshot T (`9293bd4`) is the current safe-resume point.**
