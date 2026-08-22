# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> The default branch is **not** the authoritative location of the current scientific work.

Last updated: **2026-08-22**  
Current scientific branch: **`phase6-analysis`**  
Current safe-resume snapshot: **`docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_DATABASE_READY.md`**  
Snapshot creation commit: **`fab26aa6261de33d5cc5862f432bef564d5d4999`**  
Current phase status: **PHASE 6 — DATABASE FROZEN / READY FOR META-ANALYSIS**

## Mandatory new-chat procedure

1. Do **not** infer the scientific state from old files on `main`.
2. Switch to/read branch `phase6-analysis`.
3. Read its `CURRENT_STATE.md` first.
4. Then read `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_DATABASE_READY.md` and `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`.
5. Follow `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md` when quantitative synthesis begins.

## Current frozen state

Phase 5 remains frozen at:

- **76** quantitative units;
- PRIMARY_POOLABLE: **28**;
- SENSITIVITY_ONLY: **40**;
- HOLD_PENDING_QA: **3**;
- NOT_POOLABLE: **5**.

The Phase 6 database-readiness gate has **PASSED**.

Canonical inputs on `phase6-analysis`:

- `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv` — frozen primary database, **28 unique units**;
- `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv` — corrected historical pre-amendment sensitivity database, **26 units**, sensitivity-only;
- `docs/PHASE6_PRIMARY_DATABASE_QA.md`;
- `docs/PHASE6_PREAMENDMENT_SENSITIVITY_QA.md`;
- `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`;
- `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`.

No authoritative meta-analysis has yet been run.

## Exact next movement

> Begin Phase 6 quantitative synthesis from the frozen restart-native inputs under the prospectively locked statistical analysis plan. Do not edit the frozen database silently during analysis; any new scientific correction requires a formal database amendment first.

## Critical legacy warning

The old Browser Agent/app/database artifacts are historical only and must not be used to recover or resolve scientific review data, denominators, numerators, diagnoses, eligibility, target mappings, missingness, overlap, PRISMA counts, or analysis weights.

## One-line handoff

**Switch to `phase6-analysis`, read its database-ready `CURRENT_STATE.md` and safe-resume snapshot, and run the locked Phase 6 analysis only from the frozen 28-unit primary database and the audited sensitivity inputs.**
