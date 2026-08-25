# CAN-CCHD Phase 11 — SHA37 Abstract Submission Table v1.1

Date: 2026-08-25  
Branch: `phase11-sha-abstract`  
Status: **FORMATTING-REVISED / SCIENTIFIC VALUES UNCHANGED / READY FOR PORTAL UPLOAD**

## Reason for revision

Visual QA of v1.0 identified a baseline/alignment inconsistency in the first numeric row (Strict CAN-CCHD). The source mixed raw string cells with ReportLab `Paragraph` cells in that row, while subsequent rows were paragraph-wrapped. This created slightly different vertical text metrics despite table-level middle alignment.

Version 1.1 is a formatting-only revision. Every body cell is now rendered through the same paragraph object and numeric-center style; fixed row heights and uniform padding were also applied. Strict and Expanded primary rows use the same bold style across all columns. No frozen analytic value was changed.

## Display title

**Clinically Relevant Disease After Failed Newborn Pulse Oximetry Screening**

Subtitle:

**Random-effects proportional synthesis among final failed screens without target critical congenital heart disease**

## Frozen table content

| Outcome | k | Observed events / denominator* | Median-study probability, % (95% CI) | Marginal mean, % | tau |
|---|---:|---:|---:|---:|---:|
| **Strict CAN-CCHD** | **28** | **638 / 1,999** | **17.0 (3.1-46.8)** | **33.8** | **3.369** |
| **Expanded CAN-CCHD** | **28** | **1,015 / 1,999** | **69.4 (57.7-81.4)** | **65.8** | **1.110** |
| Other/non-target structural cardiac diagnosis | 26 | 280 / 1,952 | 26.6 (14.4-43.0) | 33.0 | 1.556 |
| Infection / sepsis | 22 | 212 / 1,063 | 16.7 (9.4-24.2) | 18.9 | 0.720 |
| PPHN / pulmonary hypertension | 22 | 148 / 1,071 | 10.3 (4.7-16.3) | 12.5 | 0.790 |
| Respiratory disease | 22 | 126 / 1,063 | 8.7 (1.6-23.0) | 20.3 | 2.220 |

Footnote:

> *Observed totals are descriptive aggregates, not the random-effects estimates. CCHD = critical congenital heart disease; CAN-CCHD = clinically actionable non-CCHD; CI = confidence interval; PPHN = persistent pulmonary hypertension of the newborn. Expanded CAN-CCHD includes clinically relevant diagnoses without documented qualifying actionability. Etiologic categories have outcome-specific reporting subsets, may overlap, and must not be summed. Model: one-stage binomial-logistic-normal generalized linear mixed model with exact binomial likelihood.*

## Formatting lock

- Every body cell is a ReportLab paragraph object; no mixed string/paragraph baselines.
- Numeric columns are centered consistently.
- All rows use fixed height and identical vertical padding.
- Strict and Expanded rows are consistently bold across all cells.
- The title no longer depends on the undefined `CCHD` abbreviation; CCHD is expanded in the subtitle/footnote.
- PDF and PNG were rendered and visually inspected after the revision.

## Guardrails

- Do not relabel crude event/denominator ratios as pooled proportions.
- Do not imply Expanded CAN-CCHD represents documented actionability.
- Do not sum etiologic categories.
- Do not remove the `median-study` qualifier from the pooled-estimate column.
