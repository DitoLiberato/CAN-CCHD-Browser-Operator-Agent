# CAN-CCHD Browser Operator Agent — Hypothesis Viability Assessment Module

## Purpose

This document instructs Codex to implement a new module called:

```text
Hypothesis Viability Assessment
```

Subtitle:

```text
Early evidence landscape analysis before labor-intensive review phases
```

The module evaluates whether a research hypothesis appears feasible after the initial search/collection stage, before the project commits to the labor-intensive phases of deduplication, screening, full-text retrieval, extraction, and analysis.

This module does **not** test the hypothesis statistically.

It provides an auditable, structured, AI-assisted assessment of whether the raw evidence landscape appears sufficient to justify continuing, revising, or stopping the review.

Core principle:

> The system should help the researcher decide whether to invest substantial effort in the review, while documenting the evidence, assumptions, uncertainty, and reasoning behind the recommendation.

---

# 1. Conceptual Placement in Workflow

Insert this module after robust initial collection and collection QA.

Workflow:

```text
Research Plan
↓
Initial Search Collection
↓
Raw Metadata Preservation
↓
Metadata Enrichment
↓
Collection QA
↓
Hypothesis Viability Assessment
↓
Human Decision:
    Continue
    Revise search/hypothesis
    Stop / archive project
↓
Deduplication
↓
Formal Screening
↓
Full-Text Review
↓
Extraction
↓
Analysis
↓
Writing
```

The user must not proceed from initial collection to formal deduplication/screening until the Hypothesis Viability Assessment has been generated and acknowledged by the researcher.

---

# 2. Why This Module Exists

Traditional systematic review workflows often require significant labor before the researcher discovers that:

```text
too few relevant studies exist
metadata is too poor
denominators are unavailable
the question is too broad
the question is too narrow
the available literature cannot answer the hypothesis
```

This module formalizes the early feasibility judgment that researchers already make informally.

The module should answer:

```text
Is there enough literature signal to justify continuing?
Is the evidence base likely to contain analyzable studies?
Is the search strategy retrieving the right kind of records?
Is the raw collection metadata sufficient?
What is the main risk to feasibility?
Should the researcher continue, revise, or stop?
```

---

# 3. Naming

Preferred module name in UI:

```text
Hypothesis Viability Assessment
```

Alternative short label:

```text
Viability Assessment
```

Avoid using:

```text
Null hypothesis test
Hypothesis confirmed
Hypothesis rejected
Statistical significance prediction
```

Reason:

At this phase, the app is evaluating evidence landscape feasibility, not performing statistical inference.

---

# 4. Outputs

The module generates:

```text
Viability score
Recommendation
Structured metrics
AI rationale
Uncertainty statement
Main risks
Suggested next action
Audit record
Markdown report
CSV/JSON export
```

Allowed recommendation labels:

```text
continue
continue_with_caution
revise_search_strategy
revise_hypothesis_or_scope
stop_or_archive
insufficient_metadata_to_assess
```

User-facing labels:

```text
Continue
Continue with caution
Revise search strategy
Revise hypothesis/scope
Stop/archive
Insufficient metadata to assess
```

---

# 5. Database Tables

Create table:

```text
hypothesis_viability_assessments
```

Fields:

```text
assessment_id TEXT PRIMARY KEY
protocol_version_id TEXT
collection_snapshot_id TEXT
assessment_status TEXT
recommendation TEXT
viability_score REAL
evidence_volume_score REAL
core_concept_signal_score REAL
metadata_quality_score REAL
source_diversity_score REAL
denominator_likelihood_score REAL
outcome_signal_score REAL
deduplication_risk_score REAL
full_text_risk_score REAL
overall_risk_level TEXT
estimated_unique_records_min INTEGER
estimated_unique_records_max INTEGER
estimated_screening_core_min INTEGER
estimated_screening_core_max INTEGER
estimated_fulltext_candidate_min INTEGER
estimated_fulltext_candidate_max INTEGER
estimated_quantitative_core_min INTEGER
estimated_quantitative_core_max INTEGER
metrics_json TEXT
ai_rationale TEXT
ai_uncertainty TEXT
main_risks_json TEXT
recommended_actions_json TEXT
researcher_decision TEXT
researcher_note TEXT
created_at TEXT
acknowledged_at TEXT
```

Allowed `assessment_status`:

```text
draft
generated
acknowledged
superseded
invalidated
```

Allowed `overall_risk_level`:

```text
low
moderate
high
critical
unknown
```

Allowed `researcher_decision`:

```text
continue
continue_with_caution
revise_search_strategy
revise_hypothesis_or_scope
stop_or_archive
defer_decision
```

---

## Collection snapshot table

Create:

```text
collection_snapshots
```

Purpose:

The assessment should be tied to a frozen snapshot of the raw/enriched collection.

Fields:

```text
collection_snapshot_id TEXT PRIMARY KEY
protocol_version_id TEXT
created_at TEXT
total_raw_records INTEGER
total_normalized_records INTEGER
total_enriched_records INTEGER
source_summary_json TEXT
query_summary_json TEXT
metadata_summary_json TEXT
dedup_preview_json TEXT
core_signal_summary_json TEXT
hash_of_collection_state TEXT
notes TEXT
```

The assessment should not be based on a moving target.

If collection changes after assessment, create a new snapshot and supersede the old assessment.

---

# 6. Objective Metrics

The module must calculate objective metrics before calling any LLM.

The AI should interpret metrics, not invent them.

## 6.1 Evidence volume metrics

Calculate:

```text
total_raw_records
total_normalized_records
total_enriched_records
records_by_source
records_by_query
records_by_year
records_with_title
records_with_abstract
records_with_pmid
records_with_doi
records_with_pmcid
records_with_journal
records_with_source_url
records_with_raw_metadata
```

## 6.2 Estimated unique literature size

Before formal deduplication, estimate likely unique records using conservative clustering:

```text
same PMID
same DOI
same PMCID
same normalized title
same normalized title + first author
same normalized title + year, only if year is trusted
```

Return:

```text
estimated_unique_records_min
estimated_unique_records_max
estimated_duplicate_burden
```

Important:

If year quality is poor, do not rely on year for uniqueness.

## 6.3 Core concept signal

Calculate counts for records whose title/abstract/keywords contain:

```text
CCHD / critical congenital heart disease
pulse oximetry / oxygen saturation
newborn / neonate / neonatal / infant
screening / screen / screened
```

Calculate:

```text
records_with_cchd_signal
records_with_pulse_ox_signal
records_with_newborn_signal
records_with_screening_signal
records_with_all_core_signals
records_with_cchd_pulse_newborn
records_with_cchd_pulse_newborn_screening
```

Use title + abstract + keywords when available.

If only title is available, flag:

```text
core_signal_based_on_title_only = true
```

## 6.4 Outcome signal

Calculate records mentioning:

```text
false positive
failed screen
positive screen
screen positive
abnormal screen
secondary condition
hypoxemia
hypoxaemia
pulmonary hypertension
PPHN
respiratory
sepsis
infection
NICU
oxygen
antibiotics
```

Output:

```text
records_with_failed_screen_signal
records_with_pphn_signal
records_with_respiratory_signal
records_with_sepsis_signal
records_with_noncritical_chd_signal
records_with_any_can_cchd_signal
```

## 6.5 Denominator likelihood proxy

Because the denominator is not extractable yet, estimate likelihood using study-design and reporting signals:

Positive indicators:

```text
cohort
population
screening program
implementation
prospective
retrospective
national
regional
multicenter
newborn screening
screening algorithm
screen positive
failed screen
false positive rate
specificity
sensitivity
```

Negative indicators:

```text
case report
editorial
commentary
review
letter
prenatal only
fetal only
adult
device-only technical paper
```

Calculate:

```text
records_with_denominator_likelihood_high
records_with_denominator_likelihood_moderate
records_with_denominator_likelihood_low
```

This is not a final eligibility decision.

It is a feasibility proxy.

## 6.6 Metadata quality metrics

Calculate:

```text
abstract_availability_rate
identifier_availability_rate
pmid_availability_rate
doi_availability_rate
journal_availability_rate
year_availability_rate
source_url_availability_rate
raw_metadata_availability_rate
metadata_completeness_distribution
suspicious_year_count
identifier_conflict_count
year_conflict_count
```

## 6.7 Source diversity metrics

Calculate:

```text
number_of_sources_searched
number_of_sources_with_results
records_by_source
core_signal_records_by_source
unique_estimated_records_by_source
missing_required_sources
unavailable_sources_with_note
```

## 6.8 Burden estimates

Estimate:

```text
expected_screening_burden
expected_fulltext_burden
expected_manual_retrieval_burden
expected_duplicate_resolution_burden
expected_extraction_burden
```

These estimates can be rough ranges.

---

# 7. Scoring Model

The app should calculate a transparent viability score.

Suggested components:

```text
Evidence volume score: 0–20
Core concept signal score: 0–20
Outcome signal score: 0–15
Denominator likelihood score: 0–15
Source diversity score: 0–10
Metadata quality score: 0–10
Deduplication/manageability score: 0–5
Full-text feasibility score: 0–5
```

Total:

```text
0–100
```

## Suggested interpretation

```text
80–100: high viability
60–79: moderate-to-high viability
40–59: uncertain / revise before continuing
20–39: low viability
0–19: not currently viable
```

## Risk modifiers

Downgrade recommendation if:

```text
metadata_quality_score is critically low
abstract_availability_rate < 30%
identifier_availability_rate < 40%
source diversity is poor
all signal comes from one source
duplicate burden is extreme
required primary source failed
collection QA is blocked
```

Upgrade cautiously if:

```text
large core signal despite metadata limitations
multiple independent sources recover relevant records
many PMID/DOI identifiers available for enrichment
strong denominator likelihood signals exist
```

---

# 8. AI Interpretation Layer

After objective metrics are calculated, the LLM may generate an interpretation.

## Required input to LLM

The LLM receives:

```text
review question
primary denominator
primary outcome
secondary outcomes
source/query summary
objective metrics
collection QA status
representative sample of titles/abstracts
known limitations
```

Do not send:

```text
API keys
passwords
session tokens
full raw database if unnecessary
```

## Required LLM output JSON

The LLM must return structured JSON:

```json
{
  "recommendation": "continue | continue_with_caution | revise_search_strategy | revise_hypothesis_or_scope | stop_or_archive | insufficient_metadata_to_assess",
  "viability_summary": "...",
  "main_supporting_evidence": [
    "..."
  ],
  "main_risks": [
    {
      "risk": "...",
      "severity": "low | moderate | high | critical",
      "why_it_matters": "...",
      "mitigation": "..."
    }
  ],
  "estimated_path_forward": "...",
  "recommended_next_actions": [
    "..."
  ],
  "uncertainty_statement": "...",
  "not_a_statistical_test_statement": "..."
}
```

## Required safety language

The AI must include:

```text
This assessment does not confirm or reject the research hypothesis. It evaluates the feasibility of continuing the review based on the current evidence landscape and metadata quality.
```

---

# 9. Explainable AI Decision Process

The user requested that the app document and present the AI decision process.

Important boundary:

The app should present a **transparent rationale** and **structured evidence trail**, not hidden chain-of-thought.

The UI should show:

```text
objective metrics used
thresholds applied
risk modifiers triggered
AI recommendation
AI rationale summary
uncertainty statement
records/sources supporting the conclusion
limitations of the assessment
human decision
```

Do not expose hidden private reasoning.

Instead, present:

```text
Rationale Summary
Evidence Considered
Risk Factors
Thresholds Triggered
Alternative Interpretations
Recommended Next Action
```

## UI section: "How the recommendation was reached"

Display:

```text
1. Evidence volume:
   - X raw records
   - Y estimated unique records
   - interpretation

2. Core signal:
   - A records include CCHD + pulse ox + newborn
   - B include CCHD + pulse ox + newborn + screening
   - interpretation

3. Outcome signal:
   - PPHN signal: X
   - respiratory/sepsis signal: Y
   - interpretation

4. Metadata quality:
   - abstract availability: X%
   - identifier availability: Y%
   - interpretation

5. Main feasibility risks:
   - denominator extraction
   - duplicate burden
   - missing abstracts
   - source limitations

6. Recommendation:
   - Continue / Revise / Stop
```

---

# 10. Human Researcher Decision

The module must require human acknowledgment.

After the AI assessment, show:

```text
Researcher decision
```

Options:

```text
Continue to deduplication
Continue with caution
Revise search strategy and recollect
Revise hypothesis/scope
Stop/archive project
Defer decision
```

Require a note for:

```text
continue despite high risk
stop/archive
revise hypothesis
override AI recommendation
```

Store in:

```text
hypothesis_viability_assessments.researcher_decision
hypothesis_viability_assessments.researcher_note
```

Also write to audit log.

---

# 11. UI Requirements

Create phase panel:

```text
Hypothesis Viability Assessment
```

The panel should show:

## 11.1 Status header

```text
Collection snapshot: [timestamp]
Collection QA status: pass / warning / blocked
Assessment status: not generated / generated / acknowledged
Recommendation: Continue / Continue with caution / Revise / Stop
```

## 11.2 Score cards

```text
Overall viability score
Evidence volume
Core concept signal
Outcome signal
Denominator likelihood
Metadata quality
Source diversity
Deduplication risk
Full-text risk
```

## 11.3 Evidence landscape table

Columns:

```text
Metric
Value
Interpretation
Risk level
```

## 11.4 Source contribution table

Columns:

```text
Source
Records
Estimated unique
Core signal records
Outcome signal records
Abstract availability
Identifier availability
Warnings
```

## 11.5 AI rationale

Sections:

```text
Viability summary
Main supporting evidence
Main risks
Recommended next actions
Uncertainty
```

## 11.6 Decision panel

Buttons:

```text
Continue to Deduplication
Revise Search Strategy
Revise Hypothesis / Scope
Stop / Archive
Defer
```

---

# 12. Integration With Workflow Gating

The Deduplication phase remains locked until:

```text
collection QA is passed or warnings acknowledged
AND
hypothesis viability assessment is generated
AND
researcher decision is recorded
```

If recommendation is:

```text
stop_or_archive
```

Deduplication remains locked unless the researcher overrides with note.

If recommendation is:

```text
revise_search_strategy
```

The app should route back to Search Collection.

If recommendation is:

```text
insufficient_metadata_to_assess
```

The app should route to Metadata Enrichment / Collection QA.

---

# 13. Example Assessment for CAN-CCHD

The module should be able to produce something like:

```text
Recommendation: Continue with caution

The raw evidence landscape suggests moderate-to-high viability. A substantial number of records contain the core concepts of newborn CCHD pulse oximetry screening, and outcome-related terms such as false positive, PPHN, respiratory disease, or sepsis appear in a meaningful subset. This suggests that the hypothesis is unlikely to fail solely due to absence of literature.

However, the current collection is not ready for formal review because abstracts are missing for most records, Europe PMC year metadata appears unreliable, and the duplicate burden is high. The main feasibility risk is not evidence absence but metadata quality and denominator extractability.

Recommended next action: repeat or enrich collection to ensure abstracts, identifiers, journal, publication year, and raw source metadata are captured before formal deduplication and screening.
```

---

# 14. Reports and Exports

Generate:

```text
hypothesis_viability_assessment.md
hypothesis_viability_metrics.csv
hypothesis_viability_metrics.json
source_signal_summary.csv
risk_register.csv
researcher_decision_log.csv
```

The markdown report should be suitable for inclusion in a methodology appendix.

---

# 15. Regression Test Using Current Failed Collection

Use the previous flawed collection CSVs as fixtures.

The assessment should correctly conclude:

```text
literature signal appears present
metadata quality is insufficient
collection should be repeated/enriched before formal review
recommendation = continue_with_caution or revise_search_strategy
```

Test fixture expectations:

```text
does not conclude hypothesis confirmed
does not conclude statistical significance likely
does not recommend formal screening if abstracts are absent and metadata QA is poor
does identify substantial CCHD/pulse/newborn signal from titles
does flag missing abstracts
does flag duplicate burden
does flag suspicious Europe PMC year issue if present
```

---

# 16. Tests

Add:

```text
tests/test_hypothesis_viability.py
```

Required tests:

```text
test_viability_requires_collection_snapshot
test_viability_requires_collection_qa
test_viability_calculates_core_signal
test_viability_calculates_outcome_signal
test_viability_calculates_metadata_quality
test_viability_estimates_unique_records
test_viability_flags_missing_abstracts
test_viability_flags_duplicate_burden
test_viability_does_not_claim_hypothesis_confirmed
test_viability_routes_insufficient_metadata_to_enrichment
test_researcher_decision_required_before_deduplication_unlocks
test_override_ai_recommendation_requires_note
test_report_export_created
```

---

# 17. Acceptance Criteria

This module is complete when:

```text
assessment is generated only after collection snapshot and collection QA
objective metrics are calculated before AI interpretation
AI receives metrics and produces structured JSON
recommendation is Go/Revise/Stop style, not statistical hypothesis testing
UI shows objective metrics and explanation of recommendation
researcher decision is required and stored
deduplication remains locked until assessment acknowledged
reports/exports are generated
old flawed collection is used as regression fixture
```

---

# 18. Methodological Claim Enabled

This module supports the following methodological claim:

> Before committing to labor-intensive screening and extraction, the system performs an auditable hypothesis viability assessment based on the raw evidence landscape. It quantifies evidence volume, core concept signal, source diversity, metadata quality, duplicate burden, and likely denominator availability, then presents a structured AI-assisted Go/Revise/Stop recommendation for the researcher-in-the-loop.

This transforms AI from a simple labor-saving tool into a decision-support layer for research feasibility.
