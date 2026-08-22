# CAN-CCHD Phase 6 — Database Freeze

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **DATABASE-READINESS GATE PASSED / READY FOR META-ANALYSIS**

## 1. Freeze decision

The Phase 6 database-readiness audit is complete.

All gates A-H defined in `docs/HANDOFF_PHASE6_DATABASE_READY_FOR_META_2026-08-22.md` have passed after correction of the pre-amendment sensitivity provenance artifact.

No authoritative meta-analysis, pooled estimate, heterogeneity model, forest plot, leave-one-out analysis, or result-driven model selection was run before this freeze.

## 2. Canonical primary database

Canonical primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

Status:

- rows: **28**;
- unique analytic units: **28**;
- duplicate units: **0**;
- exact match to final Phase 5 `PRIMARY_POOLABLE` membership;
- all participant arithmetic closed;
- all row proportions independently reproduced from integer counts;
- 11 post-rerun rows reconcile exactly to the numerical overlay;
- 17 unchanged rows reconcile to latest frozen extraction blocks;
- all primary units meet the required outcome-ascertainment threshold;
- d-TGA and conditional-lesion ontology is consistent with the binding target lock and rerun;
- R125/SIBEN site units remain separately represented with shared cluster metadata;
- descriptive metadata are provenance-preserving and unknown values remain unknown.

No `v1.1` primary input is created because **no primary value changed during readiness QA**.

## 3. Canonical pre-amendment sensitivity database

Canonical S2 input:

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

Frozen corrected blob SHA:

`61e8ff9f3bb875fbc30f3964ee2e72a448cc94f2`

Correction commit:

`cd2940a1b7712b46d580957f8d3687674b728ad9`

Status:

- rows: **26**;
- unique units: **26**;
- duplicate units: **0**;
- exact reconstruction of the preserved pre-rerun Snapshot R/S `PRIMARY_POOLABLE = 26` framework;
- all arithmetic closed;
- historical numerical provenance traced to frozen extraction blocks;
- explicitly sensitivity-only.

The prior 23-row candidate at commit `60b3fe2bc4b6153a5a5099ffe89f99f453beca6b` is rejected for analysis because it mixed post-rerun values with a pre-amendment label and therefore lacked a single reproducible provenance framework.

Interpretation caveat: S2 is a **historical pre-amendment/pre-rerun framework sensitivity**, not a pure one-variable causal contrast of the d-TGA amendment, because the later all-76 rerun also corrected independent conditional-lesion/anatomy mappings.

## 4. Database-readiness gates

| Gate | Requirement | Result |
|---|---|---|
| A | 28-row exact primary membership, no duplicates | **PASS** |
| B | denominator/category arithmetic and row proportions | **PASS** |
| C | overlay precedence and unchanged-row provenance | **PASS** |
| D | harmonized target ontology | **PASS** |
| E | ascertainment and mutually exclusive terminal states | **PASS** |
| F | non-independence / R125 cluster handling | **PASS** |
| G | country/setting/timing/altitude/cluster metadata | **PASS** |
| H | pre-amendment sensitivity provenance/membership/arithmetic | **PASS AFTER CORRECTION** |

Overall gate: **PASSED**.

## 5. Frozen scientific membership inherited from Phase 5

The Phase 5 disposition remains unchanged by Phase 6 readiness QA:

- total unique quantitative units: **76**;
- `PRIMARY_POOLABLE`: **28**;
- `SENSITIVITY_ONLY`: **40**;
- `HOLD_PENDING_QA`: **3**;
- `NOT_POOLABLE`: **5**.

The three unresolved HOLD units remain quarantined and receive no primary analysis weight. Their existence does not prevent freezing the already adjudicated primary database.

## 6. Binding analysis boundary after freeze

The next quantitative step is governed by:

`docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`

Primary endpoint:

`Strict CAN-CCHD / harmonized-CCHD-negative final failed screens`.

Secondary endpoint:

`Expanded CAN-CCHD / harmonized-CCHD-negative final failed screens`.

Primary model:

one-stage random-effects binomial-logistic-normal GLMM with exact binomial likelihood and no continuity correction.

The statistical plan remains locked prospectively. Any later model deviation requires an explicit dated statistical amendment and preservation of the locked analysis.

## 7. Legacy firewall

**PASS.**

No legacy Browser Agent/app database was used to resolve or modify scientific values during Phase 6 database readiness. The restart-native firewall remains binding.

## 8. Amendment rule after freeze

The primary database is now immutable for routine analysis.

Any later proposed change to:

- primary membership;
- final failed screens;
- harmonized target count;
- denominator;
- Strict/CAN-U/NON_CAN/healthy/UNKNOWN counts;
- program-cluster identity;
- target ontology;

requires a dated `PHASE6_DATABASE_AMENDMENT` artifact explaining the evidence, impact, and whether the frozen analysis must be rerun.

Silent edits are prohibited.

## 9. Canonical QA artifacts

- `docs/PHASE6_PRIMARY_DATABASE_QA.md`
- `docs/PHASE6_PREAMENDMENT_SENSITIVITY_QA.md`
- `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`
- `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`
- `data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`
- `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`

## 10. Freeze conclusion

> **The restart-native CAN-CCHD analysis database is frozen and READY FOR META-ANALYSIS.**

This statement closes the database-readiness gate only. It does not imply that the meta-analysis has already been run.
