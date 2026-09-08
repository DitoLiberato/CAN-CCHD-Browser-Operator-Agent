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
If meta-analysis is implemented: random-effects proportional meta-analysis, heterogeneity, forest plots, sensitivity analysis. For a conference abstract, descriptive pooled/proportional summary may be sufficient only if the protocol/statistical plan supports it and the limitations are stated.

---

# Phase 11 — Manuscript / Abstract Draft
Generate drafts only after analysis and QA.

Draft types:
```text
conference abstract
structured abstract
methods section
results section
discussion skeleton
AI-use disclosure
PRISMA search summary
QA methods paragraph
full manuscript
supplementary search strategy
reference-to-claim audit
analytic-unit-to-publication crosswalk
```

All initial drafts must be labeled:
```text
draft_requires_human_review
```

## Mandatory Publication QA sub-gate
Phase 11 does not end when prose has been drafted. Every externally submitted artifact must pass:

```text
Draft -> Publication QA -> Human author review -> Release candidate
```

The canonical rules are in:

```text
docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md
```

A manuscript/abstract cannot advance to `release_candidate` or `submission_ready` with unresolved HIGH or SCIENTIFIC-STOP findings.

At minimum, Phase-11 Publication QA must verify:

```text
authors and affiliations
primary/secondary outcome hierarchy
abbreviations and publication-native terminology
all numerical claims against frozen analysis
reference order by first appearance
reference existence and claim support
no orphan references
bibliographic coverage of every named study in tables/figures
analytic-unit-to-publication crosswalk
companion/overlap handling
table scientific hierarchy and formatting
figure/forest-plot source traceability
search-method reproducibility
AI-use transparency and human-control description
risk-of-bias/quality-method transparency
target-venue limits and formatting
rendered DOCX/PDF visual QA
```

## Publication-language firewall
Repository-native status labels are allowed in audit artifacts but should not leak into published prose unless scientifically necessary.

Examples requiring translation before publication include:
```text
PRIMARY_POOLABLE
SENSITIVITY_ONLY
HOLD_PENDING_QA
NOT_POOLABLE
internal phase labels used as prose
report/unit IDs used without explanation
```

The publication should describe the scientific meaning, while the repository preserves the exact internal status for traceability.

## Outcome hierarchy
The protocol-defined hierarchy must remain explicit throughout the publication:

```text
primary outcome named as primary
secondary outcomes named as secondary
sensitivity/exploratory outcomes not promoted
Tables/Figures use the same hierarchy
```

Primary and secondary outcome families should be separated or explicitly labeled rather than placed in one undifferentiated visual list.

## Reference and study-display requirements
The bibliography must follow actual first citation rather than being preassembled and retrofitted.

For every release candidate:
```text
- generate a reference-to-claim matrix;
- verify each retained reference exists and supports its cited role;
- remove orphan references;
- ensure every named study in every table/figure has a reference;
- generate an analytic-unit-to-publication crosswalk for study-level displays;
- distinguish companion reports from independent analytic units;
- reuse one reference for multiple site-level units from the same publication when appropriate.
```

Forest-plot row labels, captions, or an explicit crosswalk must make the publication source of every displayed unit recoverable.

## AI-use disclosure
If generative AI/browser-operating agents materially contributed, describe what they did and what they did not decide.

Default pipeline rule:
> AI may assist mechanical, reversible, auditable tasks. Final eligibility, extraction acceptance, diagnosis/outcome mapping, overlap adjudication, dataset locking, model selection, interpretation, and publication decisions remain human-controlled unless a future protocol prospectively specifies otherwise.

Do not describe AI as an independent second reviewer unless that role was genuinely prespecified and implemented. AI-suggested extraction remains barred from analysis until human verification/correction.

## Methods reproducibility
The Methods must report what was actually done, including databases/sources used, unavailable planned sources when relevant, search end date, query strategy, supplementary discovery, overlap/deduplication, eligibility, extraction/verification, outcome hierarchy, QA/risk-of-bias approach, and statistical model.

Exact source-specific queries should be preserved in a supplement when manuscript word limits prevent full reporting. Do not infer missing native-platform counts or represent public-web saturation as native-platform completeness.

## Visual QA
Every meaningful DOCX/PDF revision must be rendered and visually inspected for authorship, affiliation numbering, headings, tables, figures, references, page breaks, clipping, alignment, special characters, and unintended emphasis.

A text-source check alone is not sufficient for submission readiness.

## CAN-CCHD example positioning
Suggested project title:
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

Do not generate final conclusions if QA is blocked, analysis dataset is missing, primary denominator is unresolved, extraction is unverified, the reference/study crosswalk is incomplete, or publication QA has a SCIENTIFIC-STOP finding.