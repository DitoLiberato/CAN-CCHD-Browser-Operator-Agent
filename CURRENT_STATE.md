# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> Before interpreting any Phase file, CSV, snapshot, extraction block, database, or historical note, **read this file first**.

Last updated: **2026-08-22**  
Current scientific branch: **`phase6-analysis`**  
Current safe-resume handoff: **`docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md`**  
Handoff commit: **`dbb43f7478cc3492f50d99885a7066ab0f00390f`**  
Current phase status: **PHASE 6 — DATABASE READINESS / QA BEFORE META-ANALYSIS**

---

## 1. Mandatory new-chat procedure

A new chat must read, in order:

1. `CURRENT_STATE.md`
2. `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md`
3. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
4. `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`
5. `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
6. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`
7. `docs/PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`

Then perform the database-readiness QA defined in the handoff.

Do **not** run or interpret the authoritative meta-analysis until that gate is formally passed.

---

## 2. Current scientific state

Phase 5 is frozen at:

- **76** unique quantitative units;
- `PRIMARY_POOLABLE`: **28**;
- `SENSITIVITY_ONLY`: **40**;
- `HOLD_PENDING_QA`: **3**;
- `NOT_POOLABLE`: **5**.

The canonical Phase-5 safe snapshot remains:

`docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_T.md`

Phase 6 has already created:

### Primary candidate analysis dataset

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Commit: `f266cc9a469e5d114578b52e17568b80a29a6445`

Contains the **28 frozen PRIMARY_POOLABLE units** and must now undergo the final database-readiness audit/freeze.

### Locked statistical analysis plan

`docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`

Commit: `7abc2bfe3982a53ab33cd954de510370f23292b5`

The statistical method was locked before any authoritative pooled result. It must not be altered in response to later results without an explicit dated protocol amendment.

### Pre-amendment TGA sensitivity input

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

Commit: `60b3fe2bc4b6153a5a5099ffe89f99f453beca6b`

This is sensitivity-only and requires its own provenance/membership QA before later use.

### Current handoff

`docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md`

Commit: `dbb43f7478cc3492f50d99885a7066ab0f00390f`

This is the binding task description for the next chat.

---

## 3. Exact current objective

> **Leave the restart-native Phase 6 analysis database completely ready, internally consistent, auditable, and frozen for meta-analysis.**

The next chat should finish:

- 28/28 primary membership reconciliation;
- duplicate check;
- participant arithmetic;
- recalculation of proportions from integer counts;
- post-rerun overlay precedence verification;
- unchanged-row provenance verification;
- ontology consistency;
- ascertainment / terminal-state integrity;
- R125 cluster metadata;
- timing/setting/altitude/country metadata QA;
- pre-amendment TGA sensitivity provenance and membership QA;
- formal database freeze and safe-resume snapshot.

Only after this gate passes should the locked meta-analysis be executed.

---

## 4. Critical legacy firewall

The current systematic review was rebuilt from scratch.

The old Browser Agent, old application databases, `can_cchd.db`, `data/processed/can_cchd_agent.db`, and related legacy artifacts are **historical only**.

They must not be used to resolve scientific values, including:

- study identity;
- eligibility;
- numerator;
- denominator;
- diagnosis;
- target mapping;
- actionability;
- missingness;
- overlap;
- PRISMA counts;
- analysis weights.

Use only restart-native evidence and the frozen scientific artifacts.

---

## 5. Binding numerical precedence

For current quantitative values:

1. current Phase-6 frozen/candidate dataset after QA;
2. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv` for units present there;
3. final target-rerun audit documents;
4. target mapping lock + d-TGA amendment;
5. latest frozen Phase-5 extraction blocks for unchanged units only.

Do not restore stale block values over a later post-rerun overlay.

---

## 6. Meta-analysis boundary

The locked primary endpoint is:

`Strict CAN-CCHD / harmonized-CCHD-negative final failed screens`

The secondary endpoint is:

`Expanded CAN-CCHD / harmonized-CCHD-negative final failed screens`

The locked primary model is a one-stage random-effects binomial-logistic-normal GLMM using exact binomial likelihood and no continuity correction.

However, **model execution is not the current task**. The current task is to freeze the database that will feed that model.

No exploratory calculation or non-frozen computation should be treated as a canonical meta-analytic result.

---

## 7. Maintenance rule

`CURRENT_STATE.md` must remain the stable entry point.

When the database-readiness gate passes:

1. create the Phase-6 database QA/freeze artifact;
2. create a new safe-resume snapshot;
3. update this file in the same work session;
4. only then change the status to `READY FOR META-ANALYSIS`.

---

## 8. One-line handoff

**Phase 5 is frozen (28 primary / 40 sensitivity / 3 hold / 5 not poolable). Phase 6 already has a 28-row candidate primary dataset, a locked statistical plan, and a pre-amendment TGA sensitivity dataset. Read `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md` and complete/freeze the restart-native analysis database before running the authoritative meta-analysis.**
