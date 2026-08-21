# CAN-CCHD Systematic Review — Protocol Core v1.0 Restart Lock (Repository Reconstruction)

**Original lock date:** 2026-08-20  
**Repository reconstruction date:** 2026-08-21  
**Status:** BINDING PRE-SEARCH PROTOCOL DECISIONS — RECONSTRUCTED FROM THE APPROVED AUGUST 2026 RESTART CONVERSATION

## Provenance note

This file does **not** introduce a new Phase 5 method. It restores to the repository methodological decisions that were explicitly approved and locked during Phase 0 / Phase 0.4 on 2026-08-20, before evidence extraction and meta-analysis.

The repository's older `docs/01_RESEARCH_PLAN_AND_PROTOCOL.md` preserves the review question, inclusion criterion 6, source hierarchy and search framework, but does not contain all of the later Phase 0.4 amendments. This reconstruction closes that documentation gap without changing the frozen Phase 4.5 evidence base.

The legacy Browser Agent/database remains prohibited as a scientific source under `docs/RESTART_LEGACY_DATA_FIREWALL.md`.

## 1. Review question

Among newborns who fail pulse-oximetry screening for critical congenital heart disease (CCHD) but are not diagnosed with CCHD under the review's harmonized target definition, what proportion have a clinically actionable non-CCHD diagnosis?

## 2. Analytic unit and final failed screen

The analytic unit is the **unique newborn after completion of the study's protocol-defined screening/repeat sequence**.

An initial abnormal or indeterminate measurement that normalizes on a protocol-defined repeat is a **PASS**, not a final failed screen and not part of the primary denominator.

Repeated measurements from the same newborn are never independent observations.

## 3. Harmonized CCHD denominator

The primary denominator is:

> **harmonized-CCHD-negative final failed screens**

The review's harmonized CCHD definition governs primary classification. Each study's historical/study-defined target must be preserved separately for transparency and sensitivity analyses.

A study's own label (`CCHD`, `critical CHD`, `major CHD`, `CCCHD`, etc.) must not automatically override lesion-level harmonized mapping.

No lesion may be removed from the CCHD-negative denominator merely because the authors called it critical unless lesion-level evidence supports harmonized CCHD classification.

## 4. CAN-CCHD classification

Among harmonized-CCHD-negative final failed screens:

- **CAN-A** — acute actionable non-CCHD condition with documented acute treatment or escalation of care attributable to the condition/screening pathway.
- **CAN-B** — management/disposition/follow-up actionable non-CCHD condition with documented management change, altered disposition, or clinically required follow-up, but not clearly an acute-treatment CAN-A event.
- **CAN-AB** — clearly actionable and therefore Strict CAN-CCHD, but the primary source does not permit reliable separation into A versus B.
- **CAN-U** — clinically relevant non-CCHD diagnosis is present, but the primary source does not demonstrate qualifying actionability.
- **NON_CAN** — non-actionable/transitional/incidental finding.
- **UNKNOWN** — diagnosis/outcome is not reported or not sufficiently ascertained for CAN-CCHD classification.

## 5. Strict and expanded numerators

Primary numerator:

> **Strict CAN-CCHD = CAN-A + CAN-B + CAN-AB**

Expanded sensitivity numerator:

> **Expanded CAN-CCHD = CAN-A + CAN-B + CAN-AB + CAN-U**

`CAN-U` therefore does **not** enter the primary Strict CAN-CCHD meta-analysis.

## 6. Actionability rule

Diagnosis alone is not sufficient for Strict CAN-CCHD.

Qualifying actionability requires primary-source evidence of a specific clinically meaningful consequence attributable to the diagnosis/screening pathway, such as:

- treatment;
- respiratory or other organ support;
- escalation of care;
- NICU/special-care admission or equivalent disposition change;
- delayed discharge for clinical management;
- a required management/follow-up pathway.

The exact diagnosis remains separately extracted from the actionability class.

Treatment or management **without a supported clinical diagnosis/category** must not be silently converted into a named CAN-CCHD diagnosis. Preserve the management evidence and diagnostic missingness separately.

## 7. Etiologic diagnosis rules

PPHN/pulmonary hypertension, sepsis/infection, respiratory disease, and non-critical CHD are etiologic categories, not automatic actionability labels.

- They enter **Strict CAN-CCHD** only when qualifying management/actionability is documented by the primary source.
- If clinically relevant but actionability is not demonstrated, they are **CAN-U**.
- PFO, physiologic/small PDA, incidental ASD/VSD, and transient physiologic hypoxemia/transitional circulation without qualifying management consequence are **NON_CAN**.
- A lesion ordinarily regarded as minor/noncritical can still become actionable if the primary source explicitly documents qualifying management or follow-up attributable to it.

## 8. Healthy versus unknown

`Normal echo` is **not** equivalent to globally healthy.

Absence of a reported alternative diagnosis is **not** equivalent to healthy.

Use `explicitly_healthy_no_diagnosis` only when the primary source affirmatively supports that status.

If noncardiac outcome/diagnosis was not ascertained, use `UNKNOWN`.

## 9. Ascertainment and missingness

The principal fully classified analysis requires **>=90% outcome ascertainment** among the harmonized-CCHD-negative final failed screens.

No individual-level imputation is permitted.

Missing/unascertained infants must remain explicit and must not be redistributed by subtraction into healthy, transitional, or actionable categories.

Units below the 90% threshold remain extractable but require sensitivity/hold handling rather than automatic entry into the fully classified primary analysis.

## 10. Mutually exclusive participant-level endpoint

For the primary quantitative endpoint, each harmonized-CCHD-negative final failed infant must resolve to one terminal CAN-CCHD state when the source permits:

- CAN-A;
- CAN-B;
- CAN-AB;
- CAN-U;
- NON_CAN;
- UNKNOWN.

Etiologic diagnosis categories may overlap and must not be summed unless the source confirms participant-level mutual exclusivity.

## 11. Study-defined versus harmonized target

Both must be retained:

1. `study_target_definition_raw` / study-defined CCHD outcome — historical/contextual and sensitivity role;
2. harmonized review CCHD mapping — governs the primary denominator.

Disagreement between these definitions is a QA flag, not a reason to force the study's terminology into the review denominator.

## 12. Relationship to Phase 4.5 and Phase 5

Phase 4.5 frozen report/cohort membership remains unchanged by this reconstruction.

Phase 5 must apply these pre-specified rules to the **76 frozen unique quantitative units** and may change only the downstream quantitative classification/poolability of a unit when primary-source extraction demonstrates that a prior working Phase 4 shorthand was too permissive.

In particular, an older Phase 4 note that calls a diagnosis `actionable` does not override the Protocol Core if the primary source lacks qualifying management evidence.
