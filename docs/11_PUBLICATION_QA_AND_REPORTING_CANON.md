# Publication QA and Reporting Canon v1.0

## Scope
This document is a reusable publication-quality gate for every systematic review, meta-analysis, abstract, manuscript, conference submission, or derivative scientific report produced with this phase-gated evidence pipeline.

It converts lessons learned during CAN-CCHD manuscript QA into prospective requirements for future projects. Project-specific scientific rules still live in the approved protocol; this document governs how verified science is translated into a publication-ready artifact.

## Core principle
Repository-native provenance and publication-native prose are separate layers.

The repository may use explicit machine/status labels such as `PRIMARY_POOLABLE`, `HOLD_PENDING_QA`, internal report IDs, phase numbers, or implementation tokens. Published prose must translate these into normal scientific language unless the internal label itself is scientifically necessary.

No publication artifact may sacrifice traceability, but traceability must not require the reader to understand internal repository syntax.

---

# 1. Mandatory Phase-11 Publication QA sub-gate

Phase 11 remains one numbered workflow phase. It contains a mandatory sub-gate:

```text
Draft -> Publication QA -> Human author review -> Release candidate
```

A manuscript or abstract may not be labeled `release_candidate`, `submission_ready`, or equivalent while any HIGH/SCIENTIFIC-STOP publication-QA finding remains open.

Allowed verdicts:

```text
PASS
MINOR_REVISION
MAJOR_REVISION
SCIENTIFIC_STOP
```

`SCIENTIFIC_STOP` is required for unresolved problems that could change scientific meaning or make the report non-auditable, including an unidentified analytic source, unsupported quantitative claim, fabricated or inferred method, unresolved primary/secondary outcome mismatch, or a study displayed without a defensible source publication.

---

# 2. Authorship and affiliations

Before release:

1. Verify the exact spelling and order of every author against author-provided metadata.
2. The byline should contain names only unless the target journal/conference explicitly requires degrees or credentials.
3. Administrative roles (for example, Medical Director, Head of Department, Consultant) should not be inserted into the scientific byline unless required by the target venue.
4. Affiliation numbers are assigned by first appearance among authors. The affiliation of the first author is affiliation 1; a new institution first introduced by a later author receives the next unused number.
5. Multi-affiliated authors receive all applicable affiliation numbers.
6. Institutional names must be normalized consistently across manuscript, submission portal, cover page, and author metadata sheet.
7. Funding, competing interests, corresponding-author information, and other required declarations must be resolved before release; placeholders are not permitted in a final submission artifact.

Target-specific instructions override formatting conventions but must be documented.

---

# 3. Outcome hierarchy and terminology

The manuscript must preserve the protocol-defined hierarchy of outcomes.

Required checks:

```text
primary outcome explicitly named as primary
secondary outcomes explicitly named as secondary
sensitivity/exploratory outcomes not promoted to primary
outcome names consistent across Abstract, Methods, Results, tables, figures, and supplement
participant-level outcomes not confused with study-level estimands
observed aggregates not described as random-effects pooled estimates
```

Primary and secondary outcomes should not be presented as one visually undifferentiated list when that could imply equal status. Tables should use separate panels, separate tables, or explicit hierarchy labels.

Internal coding categories may be described in Methods if scientifically necessary, but repository status tokens must not substitute for scientific outcome definitions.

---

# 4. Abbreviation and terminology audit

1. Define nonstandard abbreviations at first use in the abstract.
2. Define them again at first use in the main text because abstracts are often indexed/read independently.
3. Tables and figures must be independently interpretable; define relevant abbreviations in titles, legends, or footnotes.
4. Avoid unexplained abbreviations in titles unless they are universally recognized in the target field or explicitly permitted by the venue.
5. Do not introduce an abbreviation that is used only once or twice if writing the term in full is clearer.
6. Bibliographic titles are reproduced as published and are exempt from manuscript abbreviation normalization.

---

# 5. Reference architecture: citation first, bibliography second

The bibliography must be generated from actual first citation, not preassembled and then retrofitted to the prose.

For numbered citation styles, assign reference numbers in order of first appearance across the publishable artifact. Reuse of a source retains its original number.

Mandatory reference QA:

```text
every reference exists
author/title/journal/year identifiers verified where possible
primary source preferred for study-level data
citation supports the specific claim it follows
no orphan bibliography entries
every factual claim requiring citation has one
every named study in a table or figure has a bibliographic reference
every analytic unit displayed can be mapped to its source publication
companion reports are distinguished from independent analytic units
one publication supporting multiple sites/units reuses one reference number
```

A source may be valid but omitted from the final bibliography if no retained statement, table, or figure actually cites it.

### Reference-to-claim matrix
For every manuscript release candidate, generate an auditable matrix with at least:

```text
reference_number
full_citation_or_identifier
first_use_location
claim_or_role_supported
verification_status
notes
```

### Analytic-unit-to-publication crosswalk
When study-level results are displayed, generate a crosswalk with at least:

```text
analytic_unit_id
publication_label_used_in_table_or_figure
primary_source_report_id
reference_number
publication_identity
companion_or_cluster_note
verification_status
```

No study-level figure/table is publication-ready until every displayed analytic unit has a verified crosswalk entry.

---

# 6. Tables

Tables are scientific objects, not decorative summaries.

Required table QA:

1. Title states what is being shown and, when necessary, whether outcomes are primary or secondary.
2. Primary and secondary outcome families are separated or clearly labeled.
3. Column definitions distinguish descriptive aggregates from model-based estimands.
4. Denominators and outcome-specific subsets are explicit.
5. Overlapping categories are identified and must not be visually presented as additive if they are not mutually exclusive.
6. Footnotes define abbreviations, model type, missingness conventions, and non-additivity where relevant.
7. Bold, shading, or other emphasis must have a declared semantic purpose. Do not bold selected scientific values merely because they appear important.
8. Cell alignment, decimal precision, confidence-interval format, row height, wrapping, and headers must be visually consistent.
9. A table that names individual studies must include citation numbers or an unambiguous citation mechanism.

---

# 7. Figures and forest plots

Every named study/unit shown in a forest plot or study-level figure must be bibliographically traceable.

Required checks:

```text
all row labels map to a verified analytic unit
all analytic units map to a primary source publication
reference number shown in row label, caption, or explicit crosswalk
site-level units from one report share the same reference when appropriate
companion publications do not create duplicate analytic weight
point estimate and confidence interval reproduce frozen study-level data
figure endpoint and denominator match the manuscript definition
```

Do not infer publication authorship from an internal study label. If a row label and source provenance conflict, the provenance must be resolved before release.

All final figures must undergo visual inspection at the size likely to be read by reviewers/readers.

---

# 8. Search and methods transparency

The published Methods must describe what was actually done, not only what the protocol originally planned.

At minimum report:

- databases/sources actually searched;
- unavailable or prespecified-but-unsearched major sources when methodologically relevant;
- search end date;
- representative or exact search strategy in the manuscript and complete reproducible queries in a supplement when feasible;
- supplementary discovery methods such as Google Scholar, citation chasing, author/title expansion, regional searches, or metadata services;
- deduplication and report/cohort reconciliation approach;
- eligibility and full-text adjudication approach;
- extraction, verification, and missingness rules;
- prespecified outcome hierarchy;
- analytic-unit and overlap rules;
- risk-of-bias/quality method actually used, including explicit disclosure if no separate validated instrument was applied;
- statistical model and sensitivity analyses;
- limitations in recoverability of historical/native-platform counts rather than invented PRISMA numbers.

A public-web saturation statement must not be represented as native-platform completeness unless native-platform completeness was actually demonstrated.

Exact queries and query-level provenance should be retained in the repository even if journal word limits require moving them to a supplement.

---

# 9. AI-use transparency and human control

If generative AI, browser-operating agents, LLMs, or AI-assisted extraction tools materially contributed to the review workflow, their role must be described transparently in Methods and/or the target venue's required AI disclosure.

The report must distinguish:

```text
AI-assisted mechanical/reversible tasks
AI-suggested scientific content
human-verified/corrected data
final human scientific decisions
```

Do not describe an AI system as an independent second reviewer unless it actually functioned as a prespecified independent reviewer under the review design.

For this pipeline, the default scientific-control rule is:

> AI may assist mechanical, reversible, and auditable tasks. Final eligibility, extraction acceptance, diagnosis/outcome mapping, overlap adjudication, dataset locking, model selection, interpretation, and publication decisions remain human-controlled unless a future protocol explicitly and prospectively specifies otherwise.

AI-suggested extracted data must remain segregated from analysis until human verification/correction.

When available and prospectively recorded, retain model/provider/version, date, task class, and human verification status in the audit log. If exact historical model/version metadata were not retained, disclose the role of AI without inventing model details.

The number and names of workflow phases reported in a manuscript must match the repository's actual workflow. Never simplify or miscount phases merely for narrative convenience.

---

# 10. Abstract and venue compliance

Before submission, independently verify current target-venue instructions.

At minimum check:

```text
title word/character limit
abstract total word limit
whether headings count
required section names
figure/table allowance
file-format restrictions
author/affiliation rules
award/manuscript requirements
post-deadline correction rules
```

The portal's own counter, if present, is the final operational check after copy/paste.

Abstract numerical values, terminology, and conclusions must be reconciled to the manuscript/frozen analysis immediately before submission.

---

# 11. Visual and artifact QA

Every generated DOCX/PDF submitted externally must be rendered and visually inspected after meaningful edits.

Inspect:

```text
byline and affiliation numbering
page breaks
headings
reference numbering
orphaned captions
figure resolution and cropping
table alignment and wrapping
footnote placement
unexpected bold/italics
special characters and mathematical symbols
missing pages
clipping/overlap
```

A source Markdown file passing textual checks is not sufficient evidence that the rendered PDF/DOCX is submission-ready.

---

# 12. Required Publication-QA outputs

For a full manuscript release candidate, preserve when applicable:

```text
PUBLICATION_QA_REPORT.md
REFERENCE_CLAIM_AUDIT.md
ANALYTIC_UNIT_REFERENCE_CROSSWALK.md
SUPPLEMENTARY_SEARCH_STRATEGIES.md
AUTHOR_METADATA.md
ABBREVIATION_AUDIT.md or equivalent checklist
VISUAL_QA_LOG.md or documented render inspection
```

These may be combined when efficient, but the underlying checks may not be skipped.

---

# 13. Release checklist

A release candidate requires all of the following or an explicit documented exception:

```text
[ ] author names and order verified
[ ] affiliations numbered by first appearance and verified
[ ] declarations complete
[ ] primary/secondary outcome hierarchy explicit
[ ] terminology translated from repository-native labels
[ ] abbreviations audited
[ ] all numerical claims reconciled to frozen analysis
[ ] references ordered by first appearance
[ ] every reference existence/metadata checked
[ ] every citation supports its claim
[ ] no orphan references
[ ] every study named in table/figure referenced
[ ] analytic-unit/publication crosswalk complete
[ ] companion/overlap handling reflected correctly
[ ] tables scientifically and visually QA'd
[ ] figures scientifically and visually QA'd
[ ] exact search strategy preserved/reported
[ ] unavailable sources disclosed without implying they were searched
[ ] AI role and human control described accurately
[ ] risk-of-bias/quality approach described accurately
[ ] abstract/manuscript terminology and numbers consistent
[ ] target-venue limits checked
[ ] final rendered artifacts visually inspected
```

Only after this checklist passes should `draft_requires_human_review` be eligible to advance to a submission/release-candidate state.
