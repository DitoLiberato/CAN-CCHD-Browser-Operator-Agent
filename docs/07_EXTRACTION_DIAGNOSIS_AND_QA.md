# Phases 6–9 — Data Extraction, Verification, Diagnosis Mapping, and QA Sentinel

## Phase 6 — Data Extraction
Extraction happens only after full-text eligibility. The agent may suggest extraction from PDF/XML/full text. Suggestions are not final.

## Required Extraction Fields
Study characteristics:
```text
country
setting
study design
screening population
screening period
gestational age inclusion/exclusion
well-baby vs NICU inclusion
screening timing
preductal/postductal strategy
screening algorithm
repeat screen protocol
echo strategy
follow-up strategy
```

Publication/source identity:
```text
analytic_unit_id
primary_source_report_id
primary_publication_first_author
primary_publication_year
primary_publication_title
journal_or_source
DOI, if available
PMID/PMCID or other stable identifier, if available
full_text_provenance
report_cluster_id, if applicable
program/site_cluster_id, if applicable
companion_report_ids, if applicable
publication_identity_verification_status
```

These source-identity fields are mandatory for every unit that may enter a study-level table, figure, forest plot, or quantitative synthesis. Internal labels such as `Kumar 2017` or `R125` are not sufficient bibliographic provenance by themselves.

Primary denominator fields:
```text
number_screened
number_failed_screen
number_cchd
number_cchd_negative_failed
```
Primary outcome:
```text
number_can_cchd
```
Secondary outcomes:
```text
number_pphn
number_respiratory_disease
number_infection_sepsis
number_noncritical_chd
number_no_actionable_diagnosis
number_nicu_admission
number_oxygen_respiratory_support
number_antibiotics_or_sepsis_workup
number_delayed_discharge
```

## Required Evidence Per Field
Every scientific field must include:
```text
value_raw
value_numeric, if numeric
source_location
page/table/section
supporting_quote
confidence
```
AI-created fields are stored as `ai_suggested` and do not enter analysis.

For publication identity, preserve the exact source used to derive the analytic unit. If a companion report supplies only supplementary detail, it must not silently replace the primary publication identity or create a new analytic weight.

---

# Phase 7 — Extraction Verification
The user reviews every field.

Statuses:
```text
verified
corrected
rejected
needs_second_look
unavailable_with_note
```
Only `verified` and `corrected` scientific extraction fields enter analysis.

Any unit eligible for quantitative synthesis must also have:
```text
publication_identity_verification_status = verified | corrected
```

If publication identity is unresolved, the unit may remain in scientific QA but is not publication-display-ready.

## Denominator Logic
Primary denominator:
```text
number_cchd_negative_failed
```
If not directly reported, calculate:
```text
number_failed_screen - number_cchd
```
Only if both fields are verified/corrected and the study design supports the calculation.

Store:
```text
cchd_negative_failed_source = direct_reported | calculated_failed_minus_cchd | unavailable
```

---

# Phase 8 — Diagnosis Mapping
Map original terms to CAN-CCHD categories.

Categories:
```text
pphn
respiratory_disease
infection_sepsis
noncritical_chd
transitional_circulation
no_actionable_diagnosis
other_actionable
unclear
```

For each diagnosis term:
```text
original term
count
source quote
mapped category
CAN-CCHD yes/no
overlap possible yes/no
human verification
```
Do not assume categories are mutually exclusive unless the study states so.

---

# Phase 9 — QA Sentinel
QA runs before analysis.

Required QA modules:
```text
denominator sentinel
extraction verification completeness
diagnosis mapping completeness
case report exclusion check
non-OA non-exclusion check
not-retrieved documentation check
duplicate merge audit
source completion audit
AI-suggested data exclusion check
publication identity completeness
report/companion/site cluster reconciliation
consistency checks
```

Block analysis if:
```text
primary denominator missing for included quantitative study
number_can_cchd > number_cchd_negative_failed
number_pphn > number_cchd_negative_failed
unverified primary outcome field
ai_suggested data would enter analysis
case report included in quantitative synthesis
not-retrieved report treated as exclusion without documentation
duplicate groups unresolved
high/critical QA findings open
```

Publication identity does not necessarily block scientific analysis if the underlying source report is securely preserved, but it **does block publication display/release** of that analytic unit until the primary bibliographic identity is verified.

Before Analysis is frozen, export a machine-readable analytic-unit provenance table containing at least:
```text
analytic_unit_id
primary_source_report_id
verified_primary_publication_identity
companion_report_ids
cluster/overlap note
```

This table becomes the upstream source for the Phase-11 analytic-unit-to-publication crosswalk.

Unlock Analysis only when QA status is passed or all high/critical scientific findings are resolved/accepted with note.