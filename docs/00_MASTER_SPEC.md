# CAN-CCHD Browser Operator Agent — Master Specification

## Goal
Build a new app from scratch. Do **not** refactor the current app into this design.

The app must use a **continuous gated workflow**:

```text
Research Plan → Search Collection → Deduplication → Title/Abstract Screening → Full-Text Retrieval → Full-Text Eligibility → Data Extraction → Extraction Verification → Diagnosis Mapping → QA Sentinel → Analysis → Manuscript / Abstract Draft
```

The user must not advance to the next phase until the current phase is complete or explicitly closed with a documented human decision.

## Product Concept
A human-supervised browser-operating evidence agent for the CAN-CCHD systematic review/meta-analysis.

It should behave like a sequential research assistant:
1. The approved protocol defines what must be done.
2. The agent executes or guides searches.
3. The app locks the next stage until the current stage is complete.
4. The app prepares queues.
5. The physician makes scientific decisions.
6. Every action is logged.
7. Only verified data enters analysis.

Core principle:
> Autonomy is allowed for mechanical, reversible, auditable tasks. Scientific decisions remain human-controlled.

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

## Non-Negotiable Safety Rules
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
```

## Final Deliverable
A working app where a user can define/approve protocol, run/document searches, deduplicate, screen, retrieve full text, decide eligibility, extract/verify data, map diagnoses, run QA, analyze, and draft the abstract/manuscript. All phases must be gated, logged, and auditable.
