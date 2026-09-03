# Case Report + Review — CURRENT STATE / START HERE

> **MANDATORY ENTRY POINT FOR THIS BRANCH**

Last updated: **2026-09-03**  
Branch: **`case-report-01`**  
Parent architecture: **`phase11-writing`**  
Current status: **CASE REPORT + REVIEW PIPELINE v1.0 FROZEN; PHASE 0 IN PROGRESS**

## Privacy boundary

This repository is public. Patient-level source documents and potentially identifying clinical details must remain outside this branch until an explicit privacy/consent decision makes public storage appropriate.

The branch may contain:

- generic methodology;
- de-identification-safe templates;
- search/review artifacts that do not expose the index patient;
- later manuscript material only after privacy review.

The branch must not contain direct patient identifiers or a detailed case core capable of re-identification before consent/privacy clearance.

## Start here

Read:

1. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
2. `docs/PROJECT_DECISION_RECORD_v0.1.md`
3. `case/CASE_CORE_TEMPLATE.md`

## Scientific architecture

Two streams remain separate until verification and freeze:

- **CASE STREAM** — what actually happened to the index patient;
- **LITERATURE STREAM** — what has actually been published.

Literature cannot retrospectively rewrite case facts. Case features cannot determine which literature findings are accepted.

## Current methodological decision

The review component is provisionally set to **systematic review of reported cases**, because a small and enumerable prior-case literature is expected to be more informative than an unsystematic narrative review for novelty and management comparison.

The central association itself must not be presumed novel. The final novelty claim will be adjudicated only after formal review and completion of the clinically relevant case outcome.

## Case Core storage

The detailed `CASE_CORE` is intentionally **not committed to this public branch** at this stage. Use the repository template locally/private-side and commit only after explicit privacy review.

## One-line handoff

**Continue on `case-report-01`; follow `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`, keep the CASE and LITERATURE streams firewalled, keep patient-level source material off the public branch, and complete Phase 0 before formal collection or manuscript drafting.**
