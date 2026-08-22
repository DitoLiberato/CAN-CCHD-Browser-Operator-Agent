# CAN-CCHD — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR NEW CHATS, AGENTS, AND REPOSITORY REVIEWS**
>
> Before interpreting any Phase file, CSV, snapshot, extraction block, database, or historical note in this repository, **read this file first**.
>
> This file exists to answer one question: **Where is the current scientific state of the project, and which artifacts supersede older work?**

Last updated: **2026-08-22**  
Current scientific branch: **`phase5-extraction`**  
Current safe-resume snapshot: **Snapshot T**  
Snapshot T commit: **`9293bd461998c74f883289b0661bb5f91d53f297`**  
Current phase status: **PHASE 5 FROZEN / READY FOR QUANTITATIVE SYNTHESIS**

---

## 1. Rule for every new chat or agent

When opening this repository in a new conversation:

1. **Do not infer the current state from the default branch, file modification dates, block numbers, or old snapshots.**
2. Read `CURRENT_STATE.md` first.
3. Checkout/read the branch named in `Current scientific branch` above.
4. Read the current safe-resume snapshot named above.
5. Follow the artifact-precedence list in this file.
6. Only then inspect older extraction blocks or protocol history as needed.

If a newer `CURRENT_STATE.md` and an older snapshot disagree, **`CURRENT_STATE.md` is the navigation authority** and must point to the newer canonical artifact.

Whenever the project advances to a new safe-resume point, **this file must be updated in the same work session**.

---

## 2. Current project state

The systematic-review corpus was rebuilt from scratch under the restart protocol. Phase 5 is complete.

Frozen quantitative units: **76**

Final Phase-5 analysis membership:

- **PRIMARY_POOLABLE: 28**
- **SENSITIVITY_ONLY: 40**
- **HOLD_PENDING_QA: 3**
- **NOT_POOLABLE: 5**
- **TOTAL: 76**

Completed before freeze:

- structural extraction: **76/76**;
- d-TGA/TGA/ccTGA rerun: **76/76**;
- conditional-lesion <=28-day audit: **76/76**;
- pulmonary-atresia anatomy audit;
- final resolution attempt for all remaining holds;
- structured post-rerun numerical overlay;
- final analysis-pool freeze.

**No meta-analysis has yet been run after this freeze.**

The exact next scientific movement is:

> **Build the canonical 28-row PRIMARY_POOLABLE analysis-input dataset, then begin the prespecified quantitative synthesis (Strict primary outcome first, Expanded second, followed by sensitivity/robustness analyses).**

---

## 3. Read these files in this order

### A. Current safe-resume snapshot

`docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_T.md`

This is the fastest complete description of where the work stopped and what must happen next.

### B. Final pool freeze

`docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`

This contains the frozen membership of the 28 primary, 40 sensitivity, 3 hold, and 5 not-poolable units.

### C. Post-rerun numerical overlay

`data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`

This file contains the **current amended numerical values for the 20 units changed by the final target rerun**.

For any unit present in this overlay, **do not use the older target/denominator/CAN values from its historical extraction block for the amended primary analysis**.

### D. Final target-rerun audit

`docs/PHASE5_ALL76_TARGET_RERUN_BATCH01_TGA_SWEEP.md`

`docs/PHASE5_ALL76_TARGET_RERUN_BATCH02_CONDITIONAL_LESIONS.md`

These explain why the amended values differ from the historical Phase-5 extraction.

### E. Binding target ontology

`docs/PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`

`docs/PHASE5_PROTOCOL_AMENDMENT_2026-08-22_D_TGA_TARGET_RULE.md`

These define the current harmonized target.

### F. Remaining unresolved evidence limitations

`docs/PHASE5_FINAL_HOLD_RESOLUTION_ATTEMPT.md`

The remaining holds are closed evidence limitations, not an active extraction queue.

---

## 4. Artifact precedence — binding rule

When two artifacts disagree, use this precedence for the current Phase-5 scientific state:

1. `CURRENT_STATE.md` — navigation/current-state pointer;
2. `docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_T.md` — current safe-resume state;
3. `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md` — final analysis membership;
4. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv` — current values for changed units;
5. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH01_TGA_SWEEP.md`;
6. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH02_CONDITIONAL_LESIONS.md`;
7. `docs/PHASE5_FINAL_HOLD_RESOLUTION_ATTEMPT.md`;
8. binding protocol/target-lock documents;
9. historical Phase-5 Blocks 01-21 and Snapshots R/S for provenance and pre-amendment sensitivity only.

**Do not choose a historical value merely because it appears in a detailed block CSV.** A later overlay/amendment may supersede it.

---

## 5. Critical methodological safeguards

### Restart / legacy firewall

The current review was reconstructed from scratch.

The old Browser Agent, old app database, `can_cchd.db`, and other legacy application/database artifacts are **historical only**.

They must **not** be used to resolve:

- study identity;
- eligibility;
- denominator;
- numerator;
- diagnosis;
- target mapping;
- actionability;
- overlap;
- PRISMA counts;
- analysis weights.

If a value is not supported by restart-native evidence, do not recover it from legacy data.

### d-TGA amendment

Current primary ontology:

- d-TGA is unconditional harmonized CCHD whether simple or complex/associated;
- unqualified neonatal `TGA` maps to d-TGA unless the source indicates corrected/l-TGA anatomy;
- explicit ccTGA/l-TGA is **not** automatically promoted;
- the historical simple-TGA-only rule is retained only as a sensitivity framework.

### Conditional lesions

CoA, aortic stenosis, pulmonary stenosis, TOF, PA/VSD, and TAPVC/TAPVR require actual death, surgery, or cardiac catheter intervention within **<=28 days** to qualify as harmonized target.

A source label such as `critical`, `CCHD`, `major`, `cyanotic`, or `requiring early intervention` does not replace the observed-event requirement.

PA/IVS is unconditional; generic pulmonary atresia without septal anatomy must not be silently assumed to be PA/IVS.

---

## 6. Current frozen hold/not-poolable state

### HOLD_PENDING_QA = 3

- `U_R033` — Qatar: internal source inconsistency;
- `U_R102` — Turkey 2025: lesion/category structure insufficient;
- `U_R125_SONORA_MX` — 22 positives versus 21 categorized + CCHD lesions unavailable.

These are **closed unresolved evidence limitations**. Do not continue searching automatically unless explicitly reopening them becomes scientifically necessary.

### NOT_POOLABLE = 5

- `U_R001` Richmond;
- `U_R003` Reich;
- `U_R105` Wardha;
- `U_NR009` Tekgündüz;
- `U_BIRMINGHAM_R027_MAIN`.

They may be used descriptively where relevant but receive no CAN-CCHD proportion weight.

---

## 7. What not to do when resuming

A new chat must **not**:

- restart Phase 4 or Phase 5 screening/extraction from scratch;
- treat Snapshot S as current;
- use the original Block CSV values for a unit present in the post-rerun overlay;
- assume all source-defined CCHD cases are harmonized target;
- assume all pulmonary atresia is PA/IVS;
- treat ccTGA as d-TGA;
- use the old app/database to fill missing evidence;
- rerun the meta-analysis before constructing and QA-checking the canonical 28-row primary input table;
- add R014 and R027 as independent Birmingham weights;
- treat R125 site units as unrelated publications in cluster-sensitive analyses.

---

## 8. Maintenance rule for future phases

This file is intentionally phase-agnostic as a navigation mechanism.

At every future major freeze/snapshot:

1. update `Last updated`;
2. update `Current scientific branch` if needed;
3. update the safe-resume snapshot filename and commit;
4. replace the short `Current project state` section;
5. update the read-order/artifact-precedence list;
6. update the exact next movement.

Do **not** create a sequence of `CURRENT_STATE_v2`, `CURRENT_STATE_v3`, etc. The stable filename `CURRENT_STATE.md` must always point to the newest canonical state so a new chat has exactly one entry point.

---

## 9. Current one-line handoff

**Phase 5 is frozen at Snapshot T (`9293bd4`): 28 PRIMARY_POOLABLE, 40 SENSITIVITY_ONLY, 3 HOLD_PENDING_QA, 5 NOT_POOLABLE. Next: construct the canonical 28-row primary analysis dataset using the post-rerun overlay where applicable, QA it, then start quantitative synthesis.**
