# HANDOFF — Phase 6 database readiness before meta-analysis

Date: 2026-08-22
Branch: `phase6-analysis`
Status: **SAFE HANDOFF — DATABASE PREPARATION / QA ONLY**

## 1. Objective of the next chat

The next chat has one bounded objective:

> **Leave the restart-native Phase 6 analysis database completely ready, internally consistent, auditable, and frozen for meta-analysis.**

The next chat should **not interpret pooled meta-analytic results** and should **not advance to manuscript conclusions** until the database-readiness gate below has been explicitly passed.

The statistical analysis plan has already been locked prospectively; the immediate work is data readiness, not model selection.

---

## 2. Scientific state inherited from Phase 5

Phase 5 is frozen.

Frozen quantitative units: **76**

Final membership:

- `PRIMARY_POOLABLE`: **28**
- `SENSITIVITY_ONLY`: **40**
- `HOLD_PENDING_QA`: **3**
- `NOT_POOLABLE`: **5**

Canonical Phase-5 snapshot:

`docs/PHASE5_PROGRESS_SNAPSHOT_2026-08-22_T.md`

Canonical final pool freeze:

`docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`

Current amended numeric overlay:

`data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`

The overlay supersedes historical extraction-block values for every unit it contains.

---

## 3. Phase 6 artifacts already created

### A. Canonical primary analysis input

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Commit:

`f266cc9a469e5d114578b52e17568b80a29a6445`

This file contains the **28 frozen PRIMARY_POOLABLE units** and is intended to become the canonical main-analysis dataset after final database-readiness QA.

Columns currently include:

- `unit_id`
- `study_label`
- `country`
- `program_cluster`
- `total_screened`
- `final_failed`
- `target`
- `denominator`
- `strict`
- `can_u`
- `expanded`
- `noncan`
- `healthy`
- `unknown`
- `strict_prop`
- `expanded_prop`
- `setting`
- `timing`
- `altitude`
- `value_source`

### B. Locked statistical analysis plan

`docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`

Commit:

`7abc2bfe3982a53ab33cd954de510370f23292b5`

Status: **LOCKED BEFORE ANY AUTHORITATIVE META-ANALYTIC RESULT**.

Primary endpoint:

`Strict CAN-CCHD / harmonized-CCHD-negative final failed screens`

Secondary endpoint:

`Expanded CAN-CCHD / harmonized-CCHD-negative final failed screens`

Primary model after the database is frozen:

one-stage random-effects binomial-logistic-normal GLMM with exact binomial likelihood and no continuity correction.

Do not change the statistical plan merely because a later result is inconvenient. Any genuine necessary change requires a dated protocol amendment preserving the locked analysis as sensitivity analysis.

### C. Pre-amendment TGA sensitivity input

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

Commit:

`60b3fe2bc4b6153a5a5099ffe89f99f453beca6b`

This file reconstructs the historical pre-d-TGA-amendment framework for sensitivity analysis. It is **not the primary dataset** and must itself be QA-checked before later use.

---

## 4. Critical instruction: do not use legacy application/database data

The current review was rebuilt from scratch.

The old application/database artifacts — including `can_cchd.db`, `data/processed/can_cchd_agent.db`, Browser Agent state, and other legacy app structures — are **historical only** and prohibited as scientific evidence.

They must not be used to fill or resolve:

- study identity;
- eligibility;
- numerator;
- denominator;
- diagnosis;
- target mapping;
- actionability;
- missingness;
- overlap;
- cluster relation;
- analysis weight.

Use only restart-native frozen artifacts and primary-source evidence already documented in the Phase-4.5/Phase-5 scientific files.

---

## 5. Binding artifact precedence for database construction

When values disagree, use this order:

1. `CURRENT_STATE.md` — navigation authority;
2. this handoff — current task boundary;
3. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md` — analysis specification;
4. `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv` — candidate canonical primary dataset;
5. `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md` — frozen pool membership;
6. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv` — amended values for changed units;
7. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH01_TGA_SWEEP.md`;
8. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH02_CONDITIONAL_LESIONS.md`;
9. binding target ontology and d-TGA amendment;
10. historical Phase-5 extraction blocks only for units/fields not superseded by later artifacts.

Never prefer an older detailed block simply because it contains more columns if a later overlay or amendment supersedes the relevant value.

---

## 6. Database-readiness QA that the next chat must complete

### Gate A — membership identity

Confirm programmatically and manually that:

- primary dataset has exactly **28 rows**;
- `unit_id` is unique;
- its set of unit IDs is exactly identical to the `PRIMARY_POOLABLE` set in `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`;
- no `SENSITIVITY_ONLY`, `HOLD_PENDING_QA`, or `NOT_POOLABLE` unit appears in the primary dataset;
- no frozen primary unit is missing.

### Gate B — participant arithmetic

For every primary row confirm:

`denominator = final_failed - target`

and

`strict + can_u + noncan + healthy + unknown = denominator`

and

`expanded = strict + can_u`

and

`0 <= strict <= expanded <= denominator`.

Recompute `strict_prop` and `expanded_prop` from integer counts; do not trust stored decimal values blindly.

Any exception must be resolved from restart-native provenance before freezing.

### Gate C — value-source precedence

For every unit present in:

`data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`

confirm that the Phase-6 primary dataset uses the post-rerun values rather than stale historical block values.

For unchanged units, verify the numeric values against their latest frozen Phase-5 extraction blocks/audits.

The `value_source` field should accurately state whether the row derives from the post-rerun overlay or unchanged frozen extraction.

### Gate D — ontology consistency

Confirm the final dataset respects:

- d-TGA unconditional harmonized target rule;
- unqualified neonatal TGA -> d-TGA unless corrected/l-TGA indicated;
- ccTGA/l-TGA not automatically target;
- conditional lesions require actual death/surgery/cardiac catheter intervention <=28 days;
- PA/IVS unconditional;
- generic pulmonary atresia not silently assumed PA/IVS.

Do not reopen Phase-5 lesion adjudication unless a genuine inconsistency is discovered.

### Gate E — ascertainment / terminal-state integrity

Confirm all 28 primary units satisfy the frozen primary-pool requirements, including the Protocol Core's >=90% outcome ascertainment rule where applicable.

Participant terminal categories must remain mutually exclusive at the CAN-CCHD endpoint:

- Strict components (`CAN-A`, `CAN-B`, `CAN-AB`);
- `CAN-U`;
- `NON_CAN`;
- `healthy/no qualifying diagnosis` where affirmatively supported;
- `UNKNOWN`.

Do not redistribute unknown infants by subtraction.

### Gate F — non-independence and cluster fields

Carry forward all known study/report/program relations.

For the current primary set, the active report cluster is:

`R125_SIBEN_2020`

with:

- `U_R125_BARRANQUILLA_CO`
- `U_R125_ROSARIO_AR`

They are geographically distinct/non-overlapping site units in the primary analysis, but later sensitivity analysis must aggregate them into one report-level contribution as specified in the locked SAP.

Recheck the Phase-4.5 overlap document before adding or modifying any cluster metadata:

`docs/PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`

### Gate G — metadata readiness

Audit the analysis-modifier fields used later for descriptive/subgroup work:

- `country`
- `setting`
- `timing`
- `altitude`
- `program_cluster`

Do not invent missing metadata.

`total_screened` is descriptive and is not the primary meta-analytic denominator. A missing `total_screened` value (e.g. where source-level screened total is not exact for a site) must not be fabricated merely to make the table complete.

### Gate H — sensitivity database readiness

Audit:

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

Confirm explicitly:

- why its unit membership differs, if it differs, from the current 28-unit primary set;
- each historical target/denominator count is traceable to the preserved pre-amendment framework;
- its arithmetic closes;
- it is clearly labelled sensitivity-only and cannot accidentally replace the current harmonized primary dataset.

If necessary, create a provenance/QA note documenting unit-by-unit membership differences between current-primary and pre-amendment sensitivity sets.

---

## 7. Recommended outputs of the next chat

The next chat should create, at minimum:

1. `docs/PHASE6_PRIMARY_DATABASE_QA.md`
   - membership reconciliation;
   - arithmetic checks;
   - overlay-precedence checks;
   - cluster checks;
   - metadata/missingness checks;
   - final pass/fail status.

2. `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.1_FROZEN.csv`
   - only if QA requires corrections or metadata normalization;
   - if no values change, the v1.0 file may be formally frozen instead of creating gratuitous version churn.

3. `docs/PHASE6_PREAMENDMENT_SENSITIVITY_QA.md`
   - provenance and membership audit for the historical TGA sensitivity dataset.

4. A machine-readable QA output if useful, for example:
   - `data/phase6/PHASE6_DATABASE_QA_RESULTS.csv` or JSON.

5. A new safe-resume snapshot and an updated `CURRENT_STATE.md` once the database gate is passed.

---

## 8. Database-readiness freeze criterion

The primary database may be declared **READY FOR META-ANALYSIS** only when all of the following are true:

- 28/28 membership reconciled;
- zero duplicate unit IDs;
- all integer arithmetic closes;
- all proportions reproduce from counts;
- all amended units match the post-rerun overlay;
- all unchanged units match their frozen extraction provenance;
- ontology rules are respected;
- terminal-state accounting is valid;
- cluster/non-independence metadata is carried forward;
- no legacy scientific data has been used;
- sensitivity input provenance is documented;
- unresolved problems, if any, are explicitly quarantined rather than silently repaired.

At that point create a Phase-6 database-freeze snapshot and only then authorize execution of the locked meta-analysis plan.

---

## 9. What the next chat should NOT do

Do not:

- restart literature search;
- reopen Phase 4.5 screening globally;
- rerun all Phase-5 extraction;
- use the legacy database/app;
- add HOLD or SENSITIVITY units to the primary dataset;
- treat historical study-defined `CCHD` labels as harmonized target;
- alter d-TGA mapping without protocol amendment;
- impute missing diagnosis/outcome;
- collapse R125 site units in the primary dataset itself;
- run or interpret the final meta-analysis before the database-readiness gate passes;
- draft final Results/Discussion conclusions from any exploratory/non-frozen computation.

---

## 10. Exact starting action for the new chat

Start by reading, in order:

1. `CURRENT_STATE.md`
2. `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md`
3. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
4. `docs/PHASE5_FINAL_ANALYSIS_POOL_FREEZE.md`
5. `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
6. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`
7. `docs/PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`

Then perform the primary membership + arithmetic QA before touching any model.

---

## 11. One-line handoff

**Phase 5 is frozen (28 primary / 40 sensitivity / 3 hold / 5 not poolable). Phase 6 has a 28-row candidate primary analysis dataset and a prospectively locked statistical plan. The next chat must audit, reconcile, document, and freeze the restart-native analysis database — including sensitivity provenance and cluster metadata — and must not proceed to authoritative meta-analysis until the database-readiness gate is formally passed.**
