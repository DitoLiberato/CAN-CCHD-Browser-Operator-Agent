# Phases 10–11 — Analysis and Writing

## Phase 10 — Analysis
Analysis is locked until QA passes.

## Dataset Construction
Include only studies with:
```text
full_text_decision = include_quantitative
required extraction fields verified/corrected
number_cchd_negative_failed available
```
Exclude:
```text
case reports
citation_mining_only
conceptual_background_only
not_retrieved
separate_analysis unless explicitly included in sensitivity analysis
```

## Primary Analysis
```text
number_can_cchd / number_cchd_negative_failed
```

Secondary proportions:
```text
number_pphn / number_cchd_negative_failed
number_respiratory_disease / number_cchd_negative_failed
number_infection_sepsis / number_cchd_negative_failed
number_noncritical_chd / number_cchd_negative_failed
number_no_actionable_diagnosis / number_cchd_negative_failed
```
Report overlap limitations.

## Outputs
Generate:
```text
analysis_dataset.csv
study_level_results.csv
source_yield_table.csv
descriptive_summary.md
proportions_table.csv
figures/
```
If meta-analysis is implemented: random-effects proportional meta-analysis, heterogeneity, forest plots, sensitivity analysis. For SHA abstract, descriptive pooled/proportional summary may be sufficient if meta-analysis is unstable.

---

# Phase 11 — Manuscript / Abstract Draft
Generate drafts only after analysis and QA.

Draft types:
```text
SHA abstract
structured abstract
methods section
results section
discussion skeleton
AI-use disclosure
PRISMA search summary
QA methods paragraph
```

All drafts must be labeled:
```text
draft_requires_human_review
```

Suggested SHA title:
```text
Clinically Actionable Non-CCHD Diagnoses After Failed Newborn Pulse Oximetry Screening: A Systematic Review and Meta-analysis
```
Core message:
```text
Failed CCHD pulse oximetry screens that are negative for CCHD may still identify clinically actionable neonatal disease.
```

Secondary methodology title:
```text
From Solo Clinician to Supervised Evidence Team: A Human-in-the-Loop Browser-Operating AI Workflow for Cardiovascular Literature Review
```

Core methodology claim:
```text
A solo clinician can be supported by an autonomous browser-operating evidence workflow when autonomy is restricted to non-decisional, reversible, auditable tasks and paired with mandatory physician verification.
```

Do not generate final conclusions if QA is blocked, analysis dataset is missing, primary denominator is unresolved, or extraction is unverified.
