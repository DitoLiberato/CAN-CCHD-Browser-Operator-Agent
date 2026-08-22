# CAN-CCHD Phase 7 — Risk-of-Bias and Certainty Gate

Date: **2026-08-22**  
Status: **REQUIRED FOR INDEXED-JOURNAL MANUSCRIPT / NOT YET COMPLETED**

## Why this is a new gate

The restart performed unusually detailed eligibility, denominator, overlap, missingness, source-verification and numerical QA. Those controls support the validity of the frozen Phase 6 analysis, but they are not a formally labelled study-level risk-of-bias assessment.

It would be methodologically inaccurate to backdate such an assessment into the frozen protocol or claim it as completed in the SHA abstract. Instead, this gate prospectively defines the appraisal required before the later manuscript is submission-ready.

This is a reporting-and-interpretation extension. It does not reopen the frozen database or silently alter Phase 6 estimates.

## Primary appraisal tool

Use the **JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data**, appropriate to the review's primary proportion question.

Official source:

`https://jbi.global/critical-appraisal-tools`

Retain item-level judgments (`Yes`, `No`, `Unclear`, `Not applicable`) and supporting quotations/page references. Do not collapse the checklist into an unvalidated total quality score.

## Scope

Appraise:

1. all 28 primary analytic units;
2. every additional unit entering a reported sensitivity analysis;
3. outcome-specific missingness separately when an etiologic endpoint is not point-identifiable.

If one report contains multiple non-overlapping analytic units, record report-level judgments once and unit-specific judgments where sampling, ascertainment or reporting differs.

## CAN-CCHD-specific supplemental domains

Keep these supplemental flags separate from the standard JBI checklist:

- final-failed-screen denominator integrity;
- harmonized target-CCHD misclassification risk;
- completeness of alternative-diagnosis ascertainment;
- actionability-documentation risk affecting Strict CAN-CCHD;
- risk of recoding missing outcomes as zero/healthy;
- participant overlap or program-cluster dependence;
- selective reporting of diagnoses or management consequences;
- timing, altitude and setting applicability.

These flags explain heterogeneity and the Strict-versus-Expanded contrast; they must not be converted into an invented composite score.

## Assessment process

- Complete a primary item-level appraisal from the full text and existing extraction provenance.
- Obtain an independent second assessment or documented human verification before claiming dual appraisal.
- Resolve disagreements explicitly and retain both initial judgments.
- Keep assessors aware that the database and primary estimates are frozen; appraisal may inform interpretation and prespecified sensitivity analyses, but cannot silently recode data.

## Required outputs

- `data/phase7/PHASE7_JBI_PREVALENCE_RISK_OF_BIAS_v1.0.csv`
- `data/phase7/PHASE7_CAN_CCHD_SUPPLEMENTAL_BIAS_DOMAINS_v1.0.csv`
- `docs/PHASE7_RISK_OF_BIAS_AUDIT.md`
- manuscript-ready risk-of-bias table/figure;
- decision note on whether a certainty framework is appropriate for this prevalence meta-analysis.

## SHA abstract policy

The SHA abstract may truthfully state that prespecified denominator, ascertainment and primary-source verification rules were audited. It must **not** state that a formal JBI risk-of-bias assessment was completed until this gate is closed.

## Manuscript gate

The dedicated manuscript branch must not be labelled `SUBMISSION_READY` until this appraisal, an updated-search decision, and the PRISMA reporting package are complete.

