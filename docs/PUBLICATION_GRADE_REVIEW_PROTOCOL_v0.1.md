# CAN-CCHD Publication-Grade Systematic Review and Meta-analysis — Protocol v0.1

Date: 2026-08-22  
Branch: `manuscript-publication-grade-review`  
Status: **R0 PROTOCOL DRAFT — MUST BE FROZEN BEFORE ANY NEW DATABASE SEARCH IS EXECUTED**

## 1. Purpose

This branch upgrades the CAN-CCHD project from the frozen discovery/probe systematic review and meta-analysis into a publication-grade systematic review and meta-analysis designed for submission to a high-impact pediatric journal.

The existing restart-native review, Phase 5 database, Phase 6 freeze, and Phase 6 meta-analysis remain preserved as the discovery/probe evidence base. They must not be silently overwritten, retroactively relabeled, or represented as prospectively registered work.

The expanded review is a new, prospectively documented evidence-synthesis iteration whose purpose is to **attempt to falsify, refine, or strengthen** the existing CAN-CCHD findings using broader bibliographic coverage and higher-level reporting safeguards.

The existing SHA abstract remains a separate conference product and is not the scientific source of truth for the publication-grade review.

## 2. Core scientific question

Among newborns with a final failed CCHD pulse-oximetry screen who do not have harmonized target CCHD, how frequently are clinically relevant alternative diagnoses identified, how frequently is a qualifying management consequence documented, which etiologic categories are represented, and how much do these outcomes vary across screening programs and reports?

### Primary endpoint

`Strict CAN-CCHD` as already operationalized in the frozen CAN-CCHD framework: documented treatment, escalation, altered disposition, or clinically required follow-up attributable to a non-target-CCHD diagnosis.

### Key secondary endpoint

`Expanded CAN-CCHD`: Strict CAN-CCHD plus clinically relevant alternative diagnoses for which qualifying actionability is not directly documented.

### Secondary etiologic outcomes

At minimum:

- PPHN / pulmonary hypertension;
- respiratory disease;
- infection / sepsis;
- other/non-target structural cardiac diagnoses.

Existing ontology and harmonized target-CCHD definitions remain the starting framework. Any scientifically necessary amendment identified before or during the expanded review must be explicit, dated, justified, and propagated reproducibly.

## 3. Existing frozen discovery/probe evidence base

The prior analysis is preserved and remains auditable.

Canonical primary analysis input:

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

Underlying restart-native extraction:

- `data/phase5/blocks/`
- `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`
- `data/phase5/PHASE5_STRUCTURED_EXTRACTION_MATRIX_v0.1.csv`

Canonical Phase 6 outputs:

- `analysis/phase6/results/phase6_primary_results.json`
- `analysis/phase6/results/phase6_secondary_results.json`
- `analysis/phase6/results/phase6_sensitivity_results.csv`
- `analysis/phase6/results/phase6_leave_one_out.csv`
- `analysis/phase6/results/phase6_subgroup_results.csv`

The legacy app database `data/processed/can_cchd_agent.db` remains outside the restart-native scientific chain and must not contribute scientific values.

## 4. Publication-grade expansion principle

The expanded search is **not** undertaken to reproduce the existing 17.0% or 69.4% estimates.

Binding principle:

> The purpose of the expanded search is to attempt to falsify, refine, or strengthen the frozen CAN-CCHD findings using a broader evidence base. New evidence may increase, decrease, destabilize, or otherwise materially change any estimate or interpretation.

If new eligible studies are found, the publication-grade article must use a newly frozen publication-grade database and a complete controlled rerun. Phase 6 values remain historically frozen but do not automatically remain the manuscript's final estimates.

## 5. Search expansion

### Previously searched sources to retain

- PubMed/MEDLINE;
- Europe PMC;
- LILACS/BVS;
- SciELO;
- regional/public sources already documented;
- backward/forward citation chasing already documented.

### Priority additional bibliographic sources

The publication-grade search should seek access to and search, at minimum where feasible:

1. Embase;
2. Web of Science Core Collection;
3. Scopus;
4. CINAHL;
5. Cochrane CENTRAL.

Additional registries/grey-literature sources may be added prospectively if justified.

### Search-method reporting standards

The review will target:

- PRISMA 2020;
- PRISMA-S for complete search reporting;
- PRESS peer review of the electronic search strategy before execution of the new database searches.

Search strings must be preserved exactly as executed, with platform, database, date, limits, result counts, export format, and deduplication provenance.

Where possible, an information specialist/librarian should independently review the final electronic search strategies before execution.

## 6. Review-process safeguards

Publication-grade review procedures should include:

- duplicate-independent title/abstract screening;
- duplicate-independent or independently verified full-text eligibility decisions;
- explicit adjudication of disagreements;
- preserved exclusion reasons at full text;
- extraction with independent verification of all quantitative values used in synthesis;
- duplicate/overlap/companion-report adjudication;
- prospective handling rules for multi-site and non-independent reports;
- formal risk-of-bias assessment appropriate to the underlying study designs;
- preservation of study-level evidence supporting Strict actionability classification;
- no conversion of non-reported/non-point-identifiable etiologic outcomes to zero.

The JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data is a leading candidate for the proportional synthesis, but the exact risk-of-bias framework must be finalized in R0 before new study results are incorporated. CAN-CCHD-specific ascertainment, denominator, overlap, and actionability checks remain separate domain-specific QA layers.

## 7. Registration and transparency

Before executing the expanded searches:

- assess whether the expanded/update review is eligible for prospective registration in PROSPERO given that an earlier review iteration already exists;
- if registered, disclose the prior completed exploratory/discovery iteration transparently;
- timestamp and preserve the publication-grade protocol independently (for example through OSF) before the new searches when feasible;
- never represent the original Phase 1–6 work as retrospectively prospectively registered.

## 8. Statistical analysis boundary

The existing Phase 6 statistical plan is the starting reference, not an unchangeable manuscript mandate.

The primary proportional synthesis should retain a one-stage exact-binomial random-effects approach unless the publication-grade statistical protocol prospectively justifies a change before the expanded results are inspected.

The publication-grade protocol must predefine:

- estimands to be promoted;
- treatment of zero/boundary studies;
- heterogeneity measures;
- prediction intervals where estimable;
- influence analyses;
- sensitivity analyses;
- handling of report clusters and multi-site studies;
- subgroup/meta-regression feasibility gates;
- risk-of-bias sensitivity strategy;
- missingness rules;
- publication/reporting-bias approach appropriate to single-proportion meta-analysis.

Any new data-driven model change requires an explicit amendment.

## 9. Prespecified heterogeneity editorial contingency

### Scientific premise

The frozen discovery/probe analysis showed extreme between-program/report heterogeneity for Strict CAN-CCHD and materially lower, but still important, heterogeneity for Expanded CAN-CCHD.

The publication-grade review must not assume that this pattern will persist.

### Binding contingency

If, after inclusion of the expanded databases, duplicate-independent review, formal risk-of-bias assessment, controlled database freeze, and prespecified sensitivity analyses, **substantial/high heterogeneity remains a robust feature of Strict CAN-CCHD and/or other clinically relevant post-failure outcomes**, that persistence will be treated as a substantive scientific finding rather than merely a statistical nuisance.

In that circumstance, the manuscript's editorial line may explicitly examine whether variability in what happens after a failed CCHD pulse-oximetry screen reflects differences in:

- post-failure diagnostic pathways;
- documentation of non-CCHD diagnoses;
- referral thresholds;
- echocardiography/cardiology involvement;
- evaluation for pulmonary, infectious, transitional, and other systemic causes of hypoxemia;
- disposition and follow-up algorithms;
- program-level definitions of what constitutes a clinically meaningful 'false positive'.

### Citation-mining / guideline-synthesis trigger

Persistence of high heterogeneity will trigger a structured citation-mining and guideline/protocol review focused on post-failed-screen management.

The specific proposition to be tested is:

> Current CCHD pulse-oximetry screening protocols may vary substantially in how explicitly they define action pathways for clinically relevant non-target disease after a failed screen, and greater protocol standardization for CAN-CCHD evaluation may represent an opportunity to improve neonatal screening care.

The citation-mining stream should examine, among others:

- AAP recommendations and implementation updates;
- CDC guidance;
- national CCHD screening protocols;
- neonatal/pediatric cardiology society guidance;
- Saudi national screening policy and regional pathways;
- implementation studies that describe immediate clinical actions after failed screens.

The review should determine whether protocols explicitly address:

1. evaluation for non-CCHD causes of hypoxemia;
2. immediate clinical assessment thresholds;
3. cardiology/neonatology/pediatric escalation;
4. investigation for PPHN, infection/sepsis, respiratory disease and non-target structural cardiac disease;
5. disposition/follow-up requirements;
6. data capture/reporting of non-CCHD conditions.

### Guardrail against confirmation bias

The project currently hypothesizes that high heterogeneity will persist and may indicate an important improvement opportunity in pulse-oximetry-based neonatal screening pathways. **This is a hypothesis, not a result.**

The manuscript may recommend explicit CAN-CCHD action algorithms only if the expanded evidence and guideline/protocol synthesis support that conclusion.

If heterogeneity materially attenuates after the expanded search, quality restriction, improved outcome harmonization, or other prespecified analyses, the protocol-gap editorial line must be weakened or abandoned accordingly.

No citation mining may be used selectively to manufacture support for a conclusion contradicted by the publication-grade evidence.

## 10. Potential clinical interpretation if supported

If both the quantitative and guideline/protocol evidence support the hypothesis, the paper may argue that a failed CCHD pulse-oximetry screen should not be conceptualized only as a target-CCHD detection event.

A broader implementation framework may be warranted in which post-failure protocols explicitly address clinically relevant alternative neonatal disease (CAN-CCHD), including the role of pediatric cardiology, neonatology, general pediatrics, respiratory/infectious evaluation, disposition and follow-up.

This interpretation must remain multidisciplinary. It must not imply that pediatric cardiology alone owns or manages non-cardiac disease.

## 11. Planned review phases

To avoid rewriting historical Phase 1–6 nomenclature, the publication-grade expansion uses an `R` sequence.

### R0 — Protocol and infrastructure lock

- finalize research question and eligibility;
- lock outcome ontology;
- lock search sources;
- PRESS review;
- PRISMA/PRISMA-S reporting plan;
- registration/timestamping decision;
- risk-of-bias framework;
- duplicate-review workflow;
- statistical analysis plan;
- freeze protocol before new searches.

### R1 — Expanded database searching

Execute and archive all new database searches and exports.

### R2 — Normalization and deduplication

Integrate new retrievals with the known corpus while preserving provenance. Classify known records separately from genuinely new candidates.

### R3 — Duplicate-independent screening

Title/abstract then full-text screening with adjudication and PRISMA accounting.

### R4 — Publication-grade extraction and overlap reconciliation

Reconcile all eligible studies, including the prior corpus, under the locked publication-grade rules.

### R5 — Risk-of-bias and database-readiness gate

Complete RoB, QA, missingness, overlap, denominator, target-ontology and actionability audits. Freeze the new database before viewing new pooled estimates.

### R6 — Publication-grade meta-analysis

Run the prespecified synthesis and robustness analyses.

### R7 — Heterogeneity interpretation and guideline/protocol citation mining

Triggered especially if substantial heterogeneity persists. Evaluate post-failure action algorithms and the CAN-CCHD implementation hypothesis.

### R8 — PRISMA package and manuscript writing

Write the systematic review and meta-analysis from the newly frozen evidence base, including complete PRISMA/PRISMA-S supplements.

## 12. Target publication concept

The article should be written as a genuine **Systematic Review and Meta-analysis**, not as a narrow statistical report.

The quantitative synthesis is the analytic core, while the systematic review should also explain:

- what a failed CCHD pulse-oximetry screen means clinically;
- how non-CCHD conditions have been conceptualized historically;
- the evolving recognition of clinically important non-CCHD detection;
- variation in post-failure diagnostic pathways;
- implications for pediatric cardiology, neonatology and newborn-screening programs;
- whether current evidence supports explicit CAN-CCHD action pathways.

High-priority target journals currently include `Pediatrics`, `The Journal of Pediatrics`, and `Journal of Perinatology`, with cardiology/neonatal-screening journals retained as strong alternatives.

## 13. Stop rules

Do not execute new bibliographic searches until R0 is frozen.

Do not incorporate a newly found study into the old Phase 6 database.

Do not silently change an old frozen scientific value.

Do not use the SHA abstract as evidence.

Do not promote the protocol-gap/heterogeneity narrative unless it survives the expanded publication-grade review.

## 14. R0 immediate next actions

1. reconstruct the full existing Phase 1 search strategy and eligibility framework from the repository;
2. draft database-specific Embase, Web of Science, Scopus, CINAHL and CENTRAL strategies;
3. create a PRESS review package;
4. define independent reviewer workflow;
5. select and lock the risk-of-bias tool(s);
6. finalize publication-grade statistical analysis plan;
7. decide PROSPERO/OSF registration/timestamping route;
8. freeze Protocol v1.0;
9. only then begin R1 searches.
