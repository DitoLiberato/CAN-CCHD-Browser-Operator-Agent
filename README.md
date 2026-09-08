# CAN-CCHD-Browser-Operator-Agent

A human-supervised, AI-assisted, phase-gated evidence workflow developed for the CAN-CCHD systematic review/meta-analysis and designed to provide reusable methodological components for future evidence-synthesis projects.

## START HERE — mandatory for new chats and agents

**Before reviewing this repository, read [`CURRENT_STATE.md`](CURRENT_STATE.md).**

`CURRENT_STATE.md` is the stable navigation entry point. It tells a new chat or agent:

- which branch contains the current scientific work;
- which handoff/snapshot is the current safe-resume point;
- which artifacts supersede older extraction blocks and snapshots;
- the current frozen study/pool counts;
- the exact next scientific movement;
- which legacy files must not be used as evidence.

Do **not** infer current state from the default branch, file timestamps, block numbers, old snapshots, or legacy databases.

## Core pipeline specification

For the reusable workflow, read in this order:

1. [`docs/00_MASTER_SPEC.md`](docs/00_MASTER_SPEC.md)
2. [`docs/01_RESEARCH_PLAN_AND_PROTOCOL.md`](docs/01_RESEARCH_PLAN_AND_PROTOCOL.md)
3. [`docs/03_SEARCH_COLLECTION_AND_BROWSER_AGENT.md`](docs/03_SEARCH_COLLECTION_AND_BROWSER_AGENT.md)
4. [`docs/07_EXTRACTION_DIAGNOSIS_AND_QA.md`](docs/07_EXTRACTION_DIAGNOSIS_AND_QA.md)
5. [`docs/08_ANALYSIS_AND_WRITING.md`](docs/08_ANALYSIS_AND_WRITING.md)
6. [`docs/10_TESTS_AND_ACCEPTANCE_CRITERIA.md`](docs/10_TESTS_AND_ACCEPTANCE_CRITERIA.md)
7. [`docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md`](docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md)

The Phase-11 publication QA rules are mandatory for any manuscript, abstract, conference submission, or study-level table/figure produced from the pipeline.

Reusable QA template:

[`docs/templates/PUBLICATION_QA_REPORT_TEMPLATE.md`](docs/templates/PUBLICATION_QA_REPORT_TEMPLATE.md)

## Core principles

> Autonomy is allowed for mechanical, reversible, auditable tasks. Scientific decisions remain human-controlled.

> Draft generation is not publication readiness. A release candidate requires a separate publication-QA gate covering authorship, outcome hierarchy, references, analytic-unit/source traceability, methods/AI transparency, numerical consistency, and rendered-artifact QA.

## Current manuscript stream

Current branch: `phase11-manuscript`.

The scientific analysis is frozen upstream; manuscript work must not silently alter frozen Phase-6 values. Read `CURRENT_STATE.md` for the current writing/QA state and exact artifact precedence.

For manuscript work, also read:

- `docs/PHASE11_MANUSCRIPT_REFERENCE_CLAIM_AUDIT_v1.0.md`
- `docs/PHASE11_SHA_ALFAGIH_AWARD_PACKAGE_2026-08-25.md` only as historical submission context, not as the canonical journal-manuscript specification;
- `manuscript/supplements/CAN_CCHD_Supplementary_Search_Strategies_v1.0.md`;
- the latest analytic-unit/publication crosswalk and manuscript version recorded in `CURRENT_STATE.md`.

## Legacy firewall

Do not use legacy databases or historical app state as scientific evidence unless a current canonical document explicitly authorizes that source. Current artifact precedence is defined in `CURRENT_STATE.md` and the relevant freeze/QA documents.