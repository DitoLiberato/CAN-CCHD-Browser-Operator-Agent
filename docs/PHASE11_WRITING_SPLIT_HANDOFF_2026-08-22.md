# CAN-CCHD Phase 11 — Dedicated Writing Chats Handoff

Date: 2026-08-22  
Parent writing branch: `phase11-writing`  
Status: **SAFE WRITING SPLIT — ABSTRACT AND MANUSCRIPT MAY PROCEED IN DEDICATED CHATS**

## Purpose

Phase 6 quantitative analysis is complete and frozen. Phase 11 writing is now deliberately split into two sibling workstreams so that conference-abstract compression does not distort the full manuscript and manuscript development does not destabilize a near-submission abstract.

Dedicated branches/chats:

1. **SHA abstract:** `phase11-sha-abstract`
2. **Full article/manuscript:** `phase11-manuscript`

The parent branch `phase11-writing` is the common handoff hub and should not become a third independent drafting stream.

## Immutable scientific source of truth

Neither writing chat may silently alter extraction, eligibility, target mapping, denominators, numerators, pool membership, statistical methods, or frozen quantitative results.

Canonical frozen scientific entry point:

`docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`

Primary scientific package:

- `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
- `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
- `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
- `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
- `docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`
- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_secondary_results.json`
- `analysis/phase6/results/phase6_sensitivity_results.csv`

Frozen primary database:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA: `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

Any genuine scientific correction discovered during writing must STOP normal drafting and be raised explicitly as a possible `PHASE6_DATABASE_AMENDMENT`. Writing chats may improve wording, organization, interpretation and citation support; they may not repair science invisibly.

## Shared quantitative facts that must remain consistent

Primary analysis set:

- 28 PRIMARY_POOLABLE independent units;
- 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD outcomes;
- 1,015 Expanded CAN-CCHD outcomes.

Strict CAN-CCHD:

- median-study probability 17.0%;
- 95% profile-likelihood CI 3.1%-46.8%;
- marginal mean 33.8%;
- tau 3.369;
- 95% prediction interval approximately 0.03%-99.34%.

Expanded CAN-CCHD:

- median-study probability 69.4%;
- 95% CI 57.7%-81.4%;
- marginal mean 65.8%;
- tau 1.110;
- prediction interval 20.4%-95.2%.

Secondary etiologic GLMMs:

- PPHN/pulmonary hypertension 10.3% (4.7%-16.3%), k=22;
- respiratory disease 8.7% (1.6%-23.0%), k=22;
- infection/sepsis 16.7% (9.4%-24.2%), k=22;
- other/non-target structural cardiac diagnosis 26.6% (14.4%-43.0%), k=26.

Core S1-S6 sensitivities do not reverse the interpretation. Timing shows no clear omnibus subgroup effect (Strict p=0.263; Expanded p=0.493), but this is not evidence of equivalence. Setting/altitude meta-regression is infeasible. No inferential funnel/Egger/Begg/trim-and-fill result is promoted.

## Shared interpretation guardrails

Never write:

- that 17% is a universal patient-level rate;
- that the crude ratios 638/1,999 or 1,015/1,999 are the random-effects pooled estimates;
- that etiologic categories are mutually exclusive or sum to Expanded CAN-CCHD;
- that timing proves early versus late screening superiority/equivalence;
- that publication bias is absent;
- that all Expanded diagnoses had documented management consequences.

Preferred shared core message:

> A failed CCHD pulse-oximetry screen that is negative for harmonized target CCHD frequently identifies other clinically relevant neonatal disease. The fraction for which a specific qualifying management consequence is documented is highly heterogeneous across programs and reports, while the broader presence of clinically relevant alternative disease is consistently common.

## Separation rule between the two writing chats

### Abstract chat

Optimizes for conference communication, word economy, clarity, novelty and SHA submission rules. It may omit secondary detail for space, but may not distort the hierarchy of outcomes or overstate certainty.

Canonical handoff: `docs/PHASE11_HANDOFF_SHA_ABSTRACT_CHAT.md`.

### Manuscript chat

Optimizes for full scientific reporting, PRISMA compliance, transparent methods, complete results, limitations, discussion and journal strategy. It should not simply expand the conference abstract sentence-by-sentence.

Canonical handoff: `docs/PHASE11_HANDOFF_MANUSCRIPT_CHAT.md`.

## Reconciliation rule

The two drafts are siblings, not master/slave versions. Before final submission/publication they must undergo one cross-document consistency audit for title terminology, outcome definitions, counts, pooled estimates and conclusions.

The manuscript remains the fuller scientific record. The abstract may be more compressed but cannot introduce a claim that the manuscript cannot defend.

## One-line handoff

**Phase 6 science is frozen. Use `phase11-sha-abstract` for the SHA abstract and `phase11-manuscript` for the full paper; both derive from the same analysis-complete snapshot and may change writing, never scientific values silently.**
