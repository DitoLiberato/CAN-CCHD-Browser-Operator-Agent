# CAN-CCHD Phase 5 — Structured Extraction Schema and Coding Rules

Date: 2026-08-21
Status: **PHASE 5 ENTRY SCHEMA / BINDING FOR EXTRACTION**
Branch: `phase5-extraction`
Base freeze: `a64b9048aa45bf45ead575b1d658d13f507b3408`

## 1. Entry gate and provenance

Phase 5 begins exclusively from the **76 frozen unique quantitative extraction units** enumerated in `PHASE45_UNIQUE_QUANTITATIVE_UNITS_FROZEN.md`.

Binding upstream files:
- `docs/PHASE45_CLOSURE.md`
- `docs/PHASE45_UNIQUE_QUANTITATIVE_UNITS_FROZEN.md`
- `docs/PHASE45_TERMINAL_REPORT_STATUS_REGISTRY.md`
- `docs/PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`
- `docs/RESTART_LEGACY_DATA_FIREWALL.md`

The legacy Browser Agent/database is **not a scientific data source**. No legacy row may populate or resolve a study identity, denominator, numerator, diagnosis, actionability class, ascertainment value, overlap relation, poolability decision, PRISMA count, or meta-analysis weight.

## 2. Locked analytic unit

The analytic unit is the **unique newborn after the final failed pulse-oximetry screen**, after the study algorithm/repeat sequence has been completed.

- Repeated measurements on the same newborn are not separate units.
- Participant-overlapping reports are collapsed according to the Phase 4.5 overlap registry.
- Non-overlapping sequential cohorts may remain separate and retain a shared `program_cluster_id`.
- Multisite publications may contribute separate site/program units only where the frozen inventory already authorizes this.

## 3. Locked primary denominator

Primary denominator:

> **harmonized-CCHD-negative final failed screens**

The review's harmonized CCHD definition governs the primary denominator. A study's historical target definition must be preserved separately in `study_target_definition_raw` / `target_definition_flag` and must never silently replace the harmonized target.

A CCHD case removed from the primary denominator must be supported by lesion-level evidence sufficient for harmonized CCHD mapping. Ambiguous lesions remain unresolved until adjudicated.

## 4. Locked CAN-CCHD taxonomy

Among harmonized-CCHD-negative final failed screens:

- `CAN-A` = **acute actionable** condition.
- `CAN-B` = **management/follow-up actionable** condition.
- `CAN-AB` = actionable condition that clearly meets Strict CAN-CCHD but whose A-versus-B acuity subtype cannot be separated from the source.
- `CAN-U` = clinically relevant diagnosis reported, but actionability is not demonstrated by primary evidence.
- `NON_CAN` = non-actionable/transitional/incidental finding.
- `UNKNOWN` = diagnosis/outcome not ascertained or not reported sufficiently for classification.

Primary numerator:

> **Strict CAN-CCHD = CAN-A + CAN-B + CAN-AB**

Expanded sensitivity numerator:

> **Expanded CAN-CCHD = CAN-A + CAN-B + CAN-AB + CAN-U**

Actionability requires primary-source evidence that the failed screen led to a specific change in **management, disposition, treatment, escalation, or follow-up**. Diagnosis alone is not enough.

Etiologic diagnoses remain separately extracted even when they contribute to a CAN class.

## 5. Diagnosis-specific rules carried from Protocol Core v1.0

- PPHN, sepsis, and respiratory disease are not automatically Strict CAN-CCHD. They enter Strict only when primary evidence demonstrates treatment, escalation, disposition change, or follow-up attributable to the condition/screening pathway.
- PFO, physiologic/small PDA, incidental ASD/VSD, and transient physiologic hypoxemia without clinical consequence are `NON_CAN` unless primary evidence demonstrates qualifying actionability.
- `Normal echo` is **not** synonymous with `healthy`. If no noncardiac clinical outcome was ascertained, code `UNKNOWN`, not healthy.
- A report with a calculable CCHD-negative failed-screen count is not sufficient by itself for quantitative CAN-CCHD extraction: diagnosis, clinical outcome, management, or explicit no-diagnosis information must support classification.

## 6. Ascertainment and missingness

Outcome ascertainment must be explicit.

Required fields:
- `ascertained_cchd_negative_failed_screens`
- `cchd_negative_final_failed_screen_denominator`
- `ascertainment_pct`
- `ascertainment_ge_90pct`
- `unknown_unascertained_n`
- `missingness_flag`

The Protocol Core v1.0 threshold is **>=90% ascertainment** for the principal fully classified analysis. Units below this threshold remain extractable but must be flagged and may require sensitivity-only handling.

Missing/unascertained infants must never be recoded as healthy or assigned an etiologic diagnosis by subtraction.

## 7. Raw-first lesion and diagnosis extraction

Phase 5 must preserve the source before harmonization.

For every unit, extract:
1. raw diagnostic labels exactly enough to preserve the source meaning;
2. raw diagnostic counts;
3. whether categories are mutually exclusive, overlapping, or unclear;
4. individual structural lesions where reported;
5. source target-definition language;
6. treatment/management/follow-up evidence tied to each diagnosis when available;
7. only then, harmonized CCHD and CAN-CCHD mapping.

Do not force arithmetic reconciliation where the source is internally inconsistent. Record the discrepancy and hold pooling as needed.

## 8. Poolability is a Phase 5 result, not an entry assumption

All 76 frozen units are eligible for structured extraction. This does **not** mean all 76 enter the primary meta-analysis.

`poolability_status` must begin as `NOT_YET_ASSESSED` and can later become, for example:
- `PRIMARY_POOLABLE`
- `SENSITIVITY_ONLY`
- `HOLD_PENDING_MAPPING`
- `HOLD_PENDING_QA`
- `NOT_POOLABLE`

No final poolability label may be assigned before denominator, numerator, target mapping, diagnostic exclusivity, ascertainment, and missingness have been checked.

The Phase 4.5 closure entry-hold flags must be carried forward explicitly and cannot be silently cleared.

## 9. Phase 4.5 entry-hold units

At Phase 5 entry, the following require an explicit hold/review before primary pooling:

- `U_R101` — denominator convention: 360 algorithm-positive vs 189 study-defined true-positive.
- `U_R102` — diagnostic-category mutual exclusivity.
- `U_R126` — abstract vs detailed CCHD-count discrepancy.
- `U_R125_SONORA_MX` — 22 positives but source categories sum to 24; no forced reconciliation.
- `U_R030`, `U_R021`, `U_R023`, `U_R049`, `U_R068`, `U_R069`, `U_R108`, `U_R109`, `U_R125_BARRANQUILLA_CO`, `U_R127`, `U_R128`, `U_R130`, `U_NR009`, `U_NR044`, `U_NR050`, `U_NR058`, `U_NR059`, `U_NR062` — lesion/target/actionability mapping or related denominator classification requires completion before primary pooling.

Additional holds may be added during extraction if source-level QA requires them.

## 10. Extraction matrix fields

The canonical Phase 5 matrix uses one row per frozen quantitative unit and the following fields:

### Identity / non-independence
- `unit_id`
- `source_report_ids`
- `primary_representative_report_id`
- `program_cluster_id`
- `country`
- `site_program`

### Screening context
- `screening_population`
- `setting_flag`
- `altitude_flag`
- `screening_timing_raw`
- `screening_timing_harmonized`
- `screening_algorithm_raw`
- `total_screened`
- `final_failed_screens`

### CCHD denominator construction
- `study_target_definition_raw`
- `target_definition_flag`
- `harmonized_cchd_cases_among_final_failed_screens`
- `cchd_negative_final_failed_screen_denominator`

### CAN-CCHD classification
- `can_a_n`
- `can_b_n`
- `can_ab_n`
- `strict_can_cchd_n`
- `can_u_n`
- `expanded_can_cchd_n`
- `transitional_nonactionable_n`
- `explicitly_healthy_no_diagnosis_n`
- `unknown_unascertained_n`

### Diagnosis / lesion detail
- `diagnosis_categories_raw`
- `diagnosis_counts_raw`
- `diagnostic_category_exclusivity`
- `individual_diagnoses`
- `lesion_mapping_status`
- `management_actionability_evidence`

### Ascertainment / QA / pooling
- `ascertained_cchd_negative_failed_screens`
- `ascertainment_pct`
- `ascertainment_ge_90pct`
- `missingness_flag`
- `entry_hold_flag`
- `entry_hold_reason`
- `poolability_status`
- `poolability_reason`
- `source_full_text_provenance`
- `extraction_notes`
- `qa_status`

## 11. Arithmetic QA invariants

Where categories are mutually exclusive and fully ascertained:

`strict_can_cchd_n = can_a_n + can_b_n + can_ab_n`

`expanded_can_cchd_n = strict_can_cchd_n + can_u_n`

The denominator reconciliation must be checked against all mutually exclusive terminal categories. A failed reconciliation is a QA flag, never an invitation to invent a correction.

Where source categories overlap, retain overlap explicitly and do not sum diagnostic categories to construct CAN-CCHD unless the actionable infant-level count is independently supported.

## 12. Phase 5 progression rule

The matrix is first initialized with the 76 frozen units and inherited Phase 4.5 notes/holds. Scientific values are then populated from restart-native or independently reverified primary/full-text sources in auditable extraction blocks.

Each extraction block must record provenance and QA before the units are released for poolability adjudication.
