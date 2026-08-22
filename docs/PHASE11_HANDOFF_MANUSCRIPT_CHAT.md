# CAN-CCHD Phase 11 — Handoff for Dedicated Manuscript Chat

Date: 2026-08-22  
Target branch: `phase11-manuscript`  
Status: **SAFE RESUME — FULL ARTICLE / MANUSCRIPT DRAFTING ONLY**

## Mission of this chat

Develop the full CAN-CCHD systematic-review/meta-analysis manuscript from the frozen restart-native evidence base and Phase 6 analysis-complete package.

This chat owns the scientific article: architecture, Methods, Results, Discussion, limitations, PRISMA/reporting assembly, tables/figures/supplement strategy, references and eventual journal adaptation.

It must **not** simply expand the SHA conference abstract sentence-by-sentence. The manuscript is the fuller scientific record and should be written directly from the frozen review artifacts.

## Start here

Read in this order:

1. `docs/PHASE11_WRITING_SPLIT_HANDOFF_2026-08-22.md`
2. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
3. `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
4. `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
5. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
6. `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
7. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
8. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`
9. `docs/PROTOCOL_CORE_v1.0_RESTART_LOCK_RECONSTRUCTED.md`

Then inspect machine-readable result/extraction files only as needed.

## Scientific source of truth

Frozen primary input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA: `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

Primary analysis set:

- 28 PRIMARY_POOLABLE independent units;
- 1,999 harmonized-CCHD-negative final failed screens;
- 638 Strict CAN-CCHD events;
- 1,015 Expanded CAN-CCHD events.

Primary model:

one-stage random-effects binomial-logistic-normal GLMM, exact binomial likelihood, logit link, no continuity correction.

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
- 95% prediction interval 20.4%-95.2%.

Etiologic secondary outcomes:

- PPHN/pulmonary hypertension 10.3% (4.7%-16.3%), k=22;
- respiratory disease 8.7% (1.6%-23.0%), k=22;
- infection/sepsis 16.7% (9.4%-24.2%), k=22;
- other/non-target structural cardiac diagnosis 26.6% (14.4%-43.0%), k=26.

Etiologic categories can overlap and non-point-identifiable categories are missing, never zero.

## Core scientific narrative to test and refine

The historic concept of a pulse-oximetry `false positive` is clinically incomplete. Among newborns with a final failed CCHD screening pathway but without harmonized target CCHD, alternative clinically relevant diagnoses are common. However, the fraction with specifically documented qualifying management consequences is extremely heterogeneous across programs and reporting structures.

The manuscript should separate three concepts carefully:

1. **target-disease diagnostic performance** of CCHD pulse oximetry;
2. **Strict CAN-CCHD actionability**, requiring documented management consequence;
3. **Expanded clinically relevant disease**, where a meaningful diagnosis is present even if the report does not document qualifying actionability.

Do not blur these constructs.

## Recommended manuscript build order

### 1. Results first

Use `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md` as the starting skeleton.

Write:

- corpus/primary-analysis-set paragraph;
- Strict primary result with heterogeneity fully contextualized;
- Expanded result;
- S1-S6 robustness;
- etiologic secondaries;
- timing subgroup/meta-regression feasibility;
- reporting-bias assessment limitations.

### 2. Methods

Reconstruct directly from locked protocol, search documents, Phase 4/5 eligibility/extraction rules and Phase 6 SAP. Include enough detail to make the unusual denominator and CAN-CCHD taxonomy independently reproducible.

Key Methods components:

- eligibility and review question;
- information sources/search strategy;
- screening/full-text adjudication;
- report-to-study/unit identity and overlap handling;
- harmonized target-CCHD definition, including d-TGA amendment provenance;
- final-failed-screen denominator construction;
- Strict/Expanded CAN-CCHD definitions;
- etiologic outcome derivation and missing-not-zero rule;
- data extraction/QA;
- statistical analysis;
- sensitivities/subgroups;
- reporting-bias decision;
- software/reproducibility;
- AI-assisted workflow disclosure if required/appropriate.

### 3. Introduction

Build a focused rationale, not a generic CCHD-screening review. The gap is specifically what happens to CCHD-negative failed screens and whether calling them `false positives` hides clinically meaningful detection.

### 4. Discussion

Organize around:

- principal finding;
- clinical meaning of Strict versus Expanded;
- why extreme Strict heterogeneity likely reflects both biology/setting and differential documentation of actionability;
- implications for counselling, screening-program metrics and interpretation of `false-positive rate`;
- etiologic pattern;
- screening-timing findings and why no causal timing claim is justified;
- comparison with prior CCHD screening literature;
- strengths;
- limitations;
- research/reporting recommendations;
- restrained conclusion.

### 5. Reporting assembly

- PRISMA flow diagram from frozen search/screening counts;
- study-characteristics table;
- main quantitative table;
- robustness table if journal space permits;
- Strict and Expanded forest plots;
- supplementary extraction/sensitivity/subgroup materials;
- references;
- abstract after the manuscript body is stable.

## Main-table / figure strategy already locked

Main quantitative table and captions are in:

`docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`.

Main figures:

- Strict forest: `analysis/phase6/figures/forest_strict.svg`;
- Expanded forest: `analysis/phase6/figures/forest_expanded.svg`;
- PRISMA flow to be assembled during manuscript reporting.

Four etiologic forest plots are not required in the main manuscript by default; generate only if useful for supplement/journal request.

## Interpretation guardrails

Never write:

- “17% of babies had actionable disease” as an unqualified population statement;
- crude aggregate ratios as the random-effects pooled estimates;
- etiologic categories as mutually exclusive components;
- that timing proves screening before/after 24 h is superior, inferior or equivalent;
- that setting/altitude had no association (they were not estimable adequately);
- that absence of an inferential funnel test means absence of reporting bias;
- that all Expanded cases had documented treatment/escalation/follow-up;
- causal claims that the screening test itself improved outcomes unless a source design supports that separate causal inference.

## Special methodological issues the manuscript must explain clearly

### Median-study versus marginal mean

Because heterogeneity is especially large for Strict, the GLMM intercept back-transformation (17.0%) and marginal mean (33.8%) differ markedly. This is not an error. Explain the estimands and avoid privileging one without context.

### Prediction interval

The near-0-to-near-100% Strict prediction interval is scientifically important evidence of extreme program/report heterogeneity, not merely a statistical nuisance.

### Actionability documentation

Strict is deliberately conservative and documentation-dependent. Expanded should not be portrayed as a weaker `positive` version of Strict; it answers a different clinical question: whether another clinically relevant disease was present.

### Report/unit independence

Preserve the Phase 4.5/5 overlap and multisite adjudications. Do not revert to publication count as if each paper were automatically one independent study.

### Harmonized target diagnosis

Use the locked target mapping and d-TGA amendment consistently. Historical source labels such as `critical CHD` do not automatically override the harmonized review target.

## Journal strategy

Do not hard-format the manuscript prematurely for a journal unless a target has been selected. First produce a strong journal-neutral scientific manuscript with complete reporting. Then perform a separate journal-fit/adaptation step.

When journal selection begins, reassess current author instructions on the web rather than relying on static repository notes.

## Relationship to SHA abstract chat

The SHA abstract is being developed separately on `phase11-sha-abstract`.

Do not use conference word-limit compromises as the manuscript's scientific architecture. Conversely, when the manuscript reaches a stable version, perform a cross-document consistency audit against the SHA abstract for:

- terminology;
- unit counts;
- denominators/events;
- endpoint definitions;
- pooled estimates;
- conclusions.

## Deliverables for this chat

Expected sequence:

1. manuscript architecture + working title;
2. Results v0.1;
3. Methods v0.1;
4. Introduction v0.1;
5. Discussion/limitations v0.1;
6. PRISMA and study-characteristics reporting package;
7. tables/figures/supplement map;
8. complete manuscript v0.1 marked `draft_requires_human_review`;
9. scientific consistency/claim audit;
10. target-journal selection/adaptation;
11. submission-ready manuscript after human review.

## One-line prompt for the new chat

**Continue CAN-CCHD Phase 11 on branch `phase11-manuscript`. Read `docs/PHASE11_HANDOFF_MANUSCRIPT_CHAT.md` first. Build the full journal-neutral manuscript directly from the frozen Phase 6 package, starting with Results and Methods, without silently changing any scientific value or using the SHA abstract as the manuscript template.**
