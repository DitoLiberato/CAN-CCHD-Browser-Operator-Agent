# Restart Review ↔ Legacy App Data Firewall

Date: 2026-08-21
Status: BINDING

## Purpose

This document establishes a hard provenance boundary between:

1. the **August 2026 restarted CAN-CCHD systematic review**, which is being rebuilt from zero; and
2. the **legacy CAN-CCHD Browser Agent / pilot application**, including its historical SQLite database, legacy `records`, `studies`, `screening_decisions`, `eligibility_decisions`, and related tables.

The legacy application and its data are retained only as historical/software artifacts. They are not evidence sources for the restarted review.

## Hard prohibition

No value originating only from the legacy application/database may be used to:

- add a bibliographic report to the restarted review;
- remove a bibliographic report from the restarted review;
- assign or alter INCLUDE / EXCLUDE / CONDITIONAL / COMPANION status;
- populate a CCHD-negative failed-screen denominator;
- populate a CAN-CCHD numerator;
- classify an infant as actionable, transitional, healthy, or diagnosis-not-ascertained;
- establish a cohort overlap or companion relation;
- supply publication metadata when that identity is not independently verified in restart-native sources;
- determine PRISMA counts;
- determine meta-analysis counts or weights;
- resolve a disagreement in favor of the legacy database.

## Allowed uses of legacy artifacts

Legacy files may be consulted only for:

- understanding old software architecture;
- identifying software failure modes;
- designing safer database schemas;
- testing code paths that do not feed scientific decisions;
- historical documentation of the abandoned/pilot app.

A legacy-derived software lesson may influence **method design** (for example, deciding not to trust PMCID blindly if a legacy database demonstrated identifier contamination), but legacy rows may not influence **which evidence enters the review or what that evidence says**.

## Restart-native evidence hierarchy

Scientific membership and adjudication may use only restart-native or independently reverified sources, in this order:

1. source exports generated during the August 2026 restart;
2. restart-native public corpus workbooks / manifests (`Rxxx` lineage);
3. original PubMed, Europe PMC, LILACS/BVS, SciELO, IMEMR and other regional exports gathered during the restart;
4. full texts and bibliographic records independently retrieved during the restart;
5. Phase 4 tranche files and ledger entries whose provenance is traceable to items 1–4;
6. independently verified citation-chasing additions (`NRxxx`) with explicit source provenance.

## Audit of the 2026-08-21 legacy database inspection

During Phase 4.5 troubleshooting, the repository's pre-existing legacy SQLite file `data/processed/can_cchd_agent.db` was inspected through a temporary GitHub Actions workflow to determine whether it contained the missing restart corpus artifact.

The inspection established that it did **not**: it contained a much larger legacy collection (2,301 normalized rows), incompatible with the restarted review's historical raw count of 327, and showed identifier-quality problems. The inspection was stopped as a scientific route immediately after this distinction was recognized.

Audit findings:

- The temporary workflow only **read/exported** the pre-existing legacy database; it did not write to it.
- The generated CSV/ZIP artifact was not committed to the review branch or merged through the temporary PR.
- Temporary PR #4 was closed without merge.
- The temporary workflow file was subsequently removed from `phase4-consolidation`.
- The downloaded local ZIP was deleted from the working runtime after the audit.
- No Rxxx/NRxxx study identity, Phase 4 eligibility decision, denominator, numerator, or diagnostic category was created from a legacy database row.
- The only retained consequence of the legacy inspection is a **software-QA lesson**: PMCID must not be treated as an unconditional auto-merge key. This is a methodological guardrail, not imported evidence.

## Existing Phase 4 work

The Rxxx Phase 4 adjudications were built from restart-native corpus records and independently retrieved primary/full-text sources. They are not projections from the legacy app's `studies`, `screening_decisions`, or `eligibility_decisions` tables.

The current restart report master (`PHASE45_RESTART_REPORT_MASTER_v0.1.md`) explicitly excludes the legacy Browser Agent SQLite database from scientific membership.

## Conflict rule

If a future restart-native source conflicts with any legacy-app value, the legacy value is ignored for scientific purposes. It may be logged only as a historical discrepancy.

## Future operational rule

Before any future tool or script reads a repository database/file whose provenance predates the August 2026 restart, it must be classified first as:

- `RESTART_NATIVE_SCIENTIFIC`, or
- `LEGACY_HISTORICAL_ONLY`.

If classification is uncertain, default to `LEGACY_HISTORICAL_ONLY` until provenance is proven.

No automated crosswalk from legacy IDs/tables into the restart dataset is permitted.

## Closure requirement

The restarted review may be frozen only from a master inventory whose every report has restart-native or independently reverified provenance. The presence of legacy files in the same Git repository must never be interpreted as permission to use their contents.