# Phases 3–5 — Screening, Full-Text Retrieval, and Eligibility

## Phase 3 — Title/Abstract Screening

Principle:
```text
Be sensitive.
```
Do not exclude a newborn CCHD pulse oximetry screening study only because the abstract does not mention non-CCHD outcomes. If uncertain, mark `maybe`.

## Screening Queue
Only unique studies after deduplication enter screening.

Order:
```text
do_not_discard first
high priority
medium priority
needs_human_review
low priority
very_low quick review
citation_mining candidates
```

Each item shows:
```text
title
authors
year
journal
abstract
sources/queries that found it
priority reason
AI suggestion, if available
do-not-discard flag
available decisions
```

Allowed decisions:
```text
include
maybe
exclude
citation_mining_only
separate_analysis
```

Title/abstract exclusion reasons:
```text
not_newborn_or_neonatal
not_human
not_pulse_oximetry
not_cchd_screening
no_failed_or_positive_screen_data_clearly
case_report
editorial_commentary_letter_no_original_data
clearly_unrelated
duplicate
other
```

Case reports should be `citation_mining_only` or `exclude_from_quantitative_synthesis`.

Screening phase complete when all unique studies have title/abstract decision.

---

# Phase 4 — Full-Text Retrieval

## Purpose
Find legal full text or document inability to retrieve. No article may be excluded solely because it lacks a free PDF.

Retrieval queues:
```text
OA PDF available
OA XML available
manual retrieval required
manual PDF attached
not obtainable with note
citation mining only
```

Actions:
```text
download legal OA PDF
attach manual PDF
open DOI/PubMed/source link
mark manual retrieval required
mark not obtainable with note
```

Phase complete when all include/maybe/separate-analysis studies have retrieval status:
```text
downloaded
manual_pdf_attached
not_obtainable_with_note
not_needed_with_note
```

---

# Phase 5 — Full-Text Eligibility

## Full-Text Checklist
```text
newborn/neonatal screening population
pulse oximetry used
CCHD screening target
reports failed/positive/abnormal screens
CCHD-positive and CCHD-negative failed screens identifiable
non-CCHD diagnosis/outcome/management/no-diagnosis category reported
denominator extractable or calculable
```

Full-text decisions:
```text
include_quantitative
exclude_full_text
citation_mining_only
separate_analysis
not_retrieved
```

Full-text exclusion reasons:
```text
not_newborn_or_neonatal_screening
not_pulse_oximetry_screening
not_cchd_screening_program
no_failed_or_positive_screen_data
cannot_identify_cchd_negative_failed_screens
no_non_cchd_diagnosis_outcome_or_management_reported
no_extractable_or_calculable_denominator
case_report
review_article_citation_mining_only
nicu_only_population_analyze_separately
overlapping_cohort
insufficient_data
not_retrieved
other
```

Unlock Data Extraction only when all full-text candidates have decision, all exclusions have reason, all not-retrieved reports are documented, and citation-mining/separate-analysis records are separated.
