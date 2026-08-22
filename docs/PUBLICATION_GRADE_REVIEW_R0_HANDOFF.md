# CAN-CCHD Publication-Grade Review — R0 Handoff

Date: 2026-08-22  
Branch: `manuscript-publication-grade-review`  
Status: **SAFE RESUME — R0 PROTOCOL DEVELOPMENT ONLY / DO NOT SEARCH NEW DATABASES YET**

## Mission

Build the publication-grade systematic review and meta-analysis that will supersede the discovery/probe evidence base for the eventual manuscript if new evidence changes the dataset or estimates.

The SHA abstract and frozen Phase 6 analysis remain preserved as prior products. They are not to be retroactively rewritten as prospective work.

## Read first

1. `docs/PUBLICATION_GRADE_REVIEW_PROTOCOL_v0.1.md`
2. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
3. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`
4. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
5. `docs/PHASE11_SHA_CLINICAL_POSITIONING_CITATION_MINING_2026-08-22.md`
6. original Phase 0/1 search and eligibility artifacts identified during R0 reconstruction.

## Non-negotiable provenance boundary

Discovery/probe frozen primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

Raw restart-native study extraction/provenance:

- `data/phase5/blocks/`
- `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`
- `data/phase5/PHASE5_STRUCTURED_EXTRACTION_MATRIX_v0.1.csv`

Do not use:

`data/processed/can_cchd_agent.db`

It is legacy/historical and outside the restart-native scientific chain.

## Exact R0 objective

Before any Embase, Web of Science, Scopus, CINAHL or CENTRAL search is run:

- reconstruct and audit the original search strategy and eligibility framework;
- finalize the publication-grade question/eligibility lock;
- design database-specific new search strategies;
- prepare PRESS peer-review materials;
- finalize PRISMA 2020 + PRISMA-S reporting architecture;
- define duplicate-independent screening and adjudication;
- lock risk-of-bias methodology;
- lock the publication-grade statistical analysis plan;
- decide transparent registration/timestamping (PROSPERO eligibility and/or OSF);
- freeze `PUBLICATION_GRADE_REVIEW_PROTOCOL_v1.0`.

Only after all of these are complete may R1 begin.

## Expanded-search objective

The new search is not a confirmation exercise.

> Attempt to falsify, refine, or strengthen the existing CAN-CCHD results using a broader, publication-grade evidence base.

Any eligible newly identified evidence must be incorporated through a new publication-grade extraction/database workflow. It must never be inserted silently into the frozen Phase 6 input.

## Prespecified heterogeneity editorial line

The current working hypothesis is that high between-program/report heterogeneity, especially for Strict CAN-CCHD, will persist after the expanded search.

If substantial/high heterogeneity remains robust after:

- expanded bibliographic coverage;
- duplicate-independent screening;
- risk-of-bias assessment;
- outcome harmonization;
- controlled database freeze;
- prespecified sensitivity analyses;

then heterogeneity becomes an explicit substantive finding and manuscript editorial axis.

In that scenario, R7 will perform structured citation mining and guideline/protocol synthesis to test whether differences in post-failed-screen management pathways may contribute to the observed variability and whether current CCHD pulse-oximetry protocols adequately specify action algorithms for clinically relevant non-target disease (CAN-CCHD).

The manuscript may then argue, if supported, that neonatal pulse-oximetry screening pathways should include explicit algorithms for evaluation/escalation of non-CCHD causes of hypoxemia rather than treating CCHD-negative failed screens as a terminal 'false-positive' state.

This is **not yet a conclusion**. If heterogeneity materially attenuates, or if protocol/guideline evidence does not support the hypothesis, this editorial line must be weakened or abandoned.

## R-sequence

- `R0` Protocol/infrastructure lock
- `R1` Expanded database searching
- `R2` Normalization/deduplication
- `R3` Duplicate-independent screening
- `R4` Publication-grade extraction/overlap reconciliation
- `R5` Risk of bias + database-readiness freeze
- `R6` Publication-grade meta-analysis
- `R7` Heterogeneity interpretation + guideline/protocol citation mining
- `R8` PRISMA package + manuscript

## Publication target philosophy

Build to the methodological/reporting standard required by high-impact general pediatrics journals rather than tailoring the science to a favorable result.

Current aspirational sequence:

1. `Pediatrics`
2. `The Journal of Pediatrics`
3. `Journal of Perinatology`
4. `Cardiology in the Young`
5. `International Journal of Neonatal Screening`

Journal requirements may be updated before submission.

## One-line prompt for a new R0 chat

**Continue CAN-CCHD on branch `manuscript-publication-grade-review`. Read `docs/PUBLICATION_GRADE_REVIEW_R0_HANDOFF.md` and `docs/PUBLICATION_GRADE_REVIEW_PROTOCOL_v0.1.md` first. Work only on R0 protocol/infrastructure: reconstruct the original search/eligibility framework, design the expanded database strategy, PRISMA-S/PRESS/RoB/duplicate-review/statistical plan, and freeze Protocol v1.0 before running any new search.**
