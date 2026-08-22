# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> The default branch is **not** the authoritative location of the current scientific work.

Last updated: **2026-08-22**  
Current scientific branch: **`phase6-analysis`**  
Current safe-resume handoff: **`docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md`**  
Handoff commit: **`dbb43f7478cc3492f50d99885a7066ab0f00390f`**  
Current phase status: **PHASE 6 — DATABASE READINESS / QA BEFORE META-ANALYSIS**

## Mandatory new-chat procedure

1. Do **not** infer the current scientific state from `main`.
2. Switch to/read branch `phase6-analysis`.
3. Read its `CURRENT_STATE.md` first.
4. Then read `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md`.
5. Complete the database-readiness gate before running or interpreting the authoritative meta-analysis.

## Current frozen background

Phase 5 is frozen at:

- **76** quantitative units;
- PRIMARY_POOLABLE: **28**;
- SENSITIVITY_ONLY: **40**;
- HOLD_PENDING_QA: **3**;
- NOT_POOLABLE: **5**.

Phase 6 already contains:

- `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv` — 28-row candidate primary dataset;
- `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md` — prospectively locked statistical plan;
- `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv` — historical TGA-mapping sensitivity input;
- `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md` — exact task for the next chat.

## Exact next movement

> Audit, reconcile, document, and freeze the restart-native Phase-6 analysis database. Only after the database-readiness gate passes should the locked meta-analysis be executed.

## Critical legacy warning

The old Browser Agent/app/database artifacts are historical only and must not be used to recover or resolve scientific review data, denominators, numerators, diagnoses, eligibility, target mappings, missingness, overlap, PRISMA counts, or analysis weights.

## One-line handoff

**Switch to `phase6-analysis`, read its `CURRENT_STATE.md` and `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md`, and finish the database QA/freeze before meta-analysis.**
