# CAN-CCHD Browser Operator Agent — Master Specification

## Goal
Build a new app from scratch. Do **not** refactor the current app into this design.

The app must use a **continuous gated workflow**:

```text
Research Plan → Search Collection → Deduplication → Title/Abstract Screening → Full-Text Retrieval → Full-Text Eligibility → Data Extraction → Extraction Verification → Diagnosis Mapping → QA Sentinel → Analysis → Manuscript / Abstract Draft
```

The user must not advance to the next phase until the current phase is complete or explicitly closed with a documented human decision.

Phase 11 contains a mandatory publication-quality sub-gate:

```text
Draft → Publication QA → Human author review → Release candidate
```

This is a sub-gate, not a new numbered phase; the canonical workflow remains Phases 0–11 (12 numbered stages).

The reusable publication rules are defined in:

```text
docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md
```

## Product Concept
A human-supervised browser-operating evidence agent for the CAN-CCHD systematic review/meta-analysis and a reusable model for future protocol-driven evidence projects.

It should behave like a sequential research assistant:
1. The approved protocol defines what must be done.
2. The agent executes or guides searches.
3. The app locks the next stage until the current stage is complete.
4. The app prepares queues.
5. The physician makes scientific decisions.
6. Every action is logged.
7. Only verified data enters analysis.
8. Publication artifacts undergo a separate source/citation/method/visual QA gate before release.

Core principle:
> Autonomy is allowed for mechanical, reversible, auditable tasks. Scientific decisions remain human-controlled.

Publication principle:
> Repository-native traceability must be preserved, but published prose, tables, figures, authorship, references, and methods must be independently audited for scientific readability and bibliographic completeness.

## Required App Structure
```text
app.py
.env.example
README.md
can_cchd/
  app_state/ db/ workflow/ protocol/ sources/ browser_agent/ importers/
  dedup/ screening/ fulltext/ extraction/ diagnosis/ qa/ analysis/ writing/ ui/
tests/
```

No legacy multipage UI. The app opens into a single **Workflow Console**.

Allowed top-level sections:
```text
Workflow Console
Settings / Credentials
Audit Log
Exports / Backups
Developer Tools, optional and hidden
```

## Phase Status
```text
locked
available
in_progress
blocked
completed
completed_with_note
skipped_with_justification
```

Default rule:
```text
Next phase remains locked until previous phase is completed.
```

Override is allowed only with a written physician justification and audit log entry.

For Phase 11, draft generation does not imply publication readiness. A release-candidate state is blocked until Publication QA passes or an exception is explicitly documented.

## Source Access Classes
API-autonomous:
```text
PubMed / NCBI E-utilities
Europe PMC
Crossref
OpenAlex
Semantic Scholar
Unpaywall / OA resolver
```
Browser-autonomous or browser-supervised:
```text
BVS/LILACS
SciELO, if API unreliable
IMEMR
Google Scholar, supervised only
```
Supervised-login:
```text
Embase
Scopus
Web of Science
institutional proxy platforms
```

For supervised-login platforms:
```text
agent opens platform → user logs in manually → agent never stores password → user clicks Continue after login → agent resumes
```

## Non-Negotiable Safety and Scientific-Integrity Rules
The app must not:
```text
exclude studies automatically
bypass paywalls
bypass CAPTCHA
store user credentials
delete records without audit
use AI-suggested extraction in analysis without human verification
treat lack of free PDF as exclusion
treat old publication date as exclusion
treat low AI score as exclusion
invent unrecoverable PRISMA/search counts
represent an unavailable database as searched
represent public-web saturation as native-platform completeness
present an unidentified analytic unit in a publication figure/table
release a manuscript with an unsupported quantitative claim
release a manuscript with unresolved primary/secondary outcome hierarchy
```

## Phase-11 Publication QA Minimums
Before external release, the workflow must be able to verify or document:

```text
author names/order and affiliation numbering
funding/competing-interest/required declarations
primary/secondary outcome hierarchy
publication-native terminology and abbreviation expansion
numerical consistency with frozen analysis
reference order by first appearance
reference existence and claim support
no orphan references
citation coverage of every named study in tables/figures
analytic-unit-to-publication crosswalk
companion/overlap handling
search-method reproducibility
AI-use and human-control transparency
risk-of-bias/quality-method transparency
target-venue limits
rendered DOCX/PDF visual QA
```

## Final Deliverable
A working app where a user can define/approve protocol, run/document searches, deduplicate, screen, retrieve full text, decide eligibility, extract/verify data, map diagnoses, run QA, analyze, and draft the abstract/manuscript. All phases must be gated, logged, and auditable.

The pipeline is not considered complete merely because a manuscript has been generated. It must also produce a publication-QA record demonstrating that the external artifact is bibliographically complete, methodologically transparent, numerically reconciled, visually inspected, and traceable back to verified evidence.