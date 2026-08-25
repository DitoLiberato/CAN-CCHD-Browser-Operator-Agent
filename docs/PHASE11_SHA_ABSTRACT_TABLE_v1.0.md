# CAN-CCHD Phase 11 — SHA37 Abstract Submission Table v1.0

Date: 2026-08-25  
Branch: `phase11-sha-abstract`  
Status: **TABLE CONTENT FROZEN FOR PORTAL UPLOAD / NO PHASE 6 VALUE CHANGED**

## Rationale

SHA37 permits one table or one figure with the abstract. For CAN-CCHD, a compact quantitative table is preferred to a single forest plot because it displays the prespecified Strict endpoint, the more stable Expanded endpoint, and the four clinically recognizable etiologic syntheses in one element while preserving the distinction between documented actionability and clinically relevant disease.

## Table title

**Clinically Relevant Disease After Failed Newborn CCHD Pulse Oximetry Screening**

Subtitle:

**Random-effects proportional synthesis among harmonized-CCHD-negative final failed screens**

## Frozen table content

| Outcome | k | Observed events / denominator* | Median-study probability, % (95% CI) | Marginal mean, % | tau |
|---|---:|---:|---:|---:|---:|
| **Strict CAN-CCHD** | 28 | 638 / 1,999 | **17.0 (3.1-46.8)** | **33.8** | 3.369 |
| **Expanded CAN-CCHD** | 28 | 1,015 / 1,999 | **69.4 (57.7-81.4)** | **65.8** | 1.110 |
| Other/non-target structural cardiac diagnosis | 26 | 280 / 1,952 | 26.6 (14.4-43.0) | 33.0 | 1.556 |
| Infection / sepsis | 22 | 212 / 1,063 | 16.7 (9.4-24.2) | 18.9 | 0.720 |
| PPHN / pulmonary hypertension | 22 | 148 / 1,071 | 10.3 (4.7-16.3) | 12.5 | 0.790 |
| Respiratory disease | 22 | 126 / 1,063 | 8.7 (1.6-23.0) | 20.3 | 2.220 |

Footnote:

> *Observed totals are descriptive aggregates, not the random-effects estimates. CAN-CCHD = clinically actionable non-CCHD. Expanded CAN-CCHD includes clinically relevant diagnoses without documented qualifying actionability. Etiologic categories have outcome-specific reporting subsets, may overlap, and must not be summed. Model: one-stage binomial-logistic-normal GLMM with exact binomial likelihood.*

## Upload formats generated

A one-page landscape PDF and a PNG alternative were generated from this frozen content and visually inspected. Only one format should be uploaded to the SHA abstract submission field.

## Guardrails

- Do not relabel the crude event/denominator ratios as pooled proportions.
- Do not imply that Expanded CAN-CCHD represents documented actionability.
- Do not sum etiologic categories.
- Do not remove the `median-study` qualifier from the pooled estimate column.
