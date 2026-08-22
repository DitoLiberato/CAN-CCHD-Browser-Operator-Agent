# CAN-CCHD Phase 11 — Adversarial Review Handoff for SHA Abstract

Date: 2026-08-22  
Target branch: `phase11-sha-abstract`  
Status: **READY FOR INDEPENDENT ADVERSARIAL REVIEW — READ ONLY UNTIL VERDICT**

## Mission

Act as an independent, skeptical scientific reviewer of the SHA37 abstract candidate:

`docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.3.md`

Your task is **not** to make the abstract prettier by default. Your task is to try to break it scientifically and methodologically before submission.

Audit every quantitative claim, endpoint description, estimand, methodological statement and clinical implication against the restart-native evidence chain in this repository.

Assume that any apparently convenient simplification may hide a scientific problem until proven otherwise.

Do not alter Phase 6 scientific values silently. If you identify a genuine discrepancy between the abstract and the frozen database/results, classify it explicitly as a possible `PHASE6_DATABASE_AMENDMENT` or analysis/reporting inconsistency and stop normal editorial revision.

## First reading order

Read these files in order:

1. `CURRENT_STATE.md`
2. `docs/PHASE11_HANDOFF_SHA_ABSTRACT_CHAT.md`
3. `docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.3.md`
4. `docs/PHASE11_SHA_CLINICAL_POSITIONING_CITATION_MINING_2026-08-22.md`
5. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
6. `docs/PHASE6_DATABASE_FREEZE_2026-08-22.md`
7. `docs/PHASE6_STATISTICAL_ANALYSIS_PLAN_LOCK.md`
8. `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`
9. `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
10. `docs/PHASE6_META_ANALYSIS_AUDIT_2026-08-22.md`
11. `docs/PHASE6_SECONDARY_ETIOLOGY_AND_SUBGROUP_AUDIT_2026-08-22.md`
12. `docs/PHASE6_SMALL_STUDY_REPORTING_BIAS_DECISION_2026-08-22.md`

## Where the restart-native raw extraction data are

The study-level **raw extraction layer** for this restart-native project is in:

`data/phase5/blocks/`

The directory contains the study/unit extraction blocks used during Phase 5:

- `PHASE5_EXTRACTION_BLOCK_01.csv` through `PHASE5_EXTRACTION_BLOCK_17.csv`;
- `PHASE5_IDENTITY_RECONSTRUCTION_BLOCK_18.csv` for the identity-reconstruction work that replaced a conventional extraction block at that position;
- `PHASE5_EXTRACTION_BLOCK_19.csv`;
- `PHASE5_EXTRACTION_BLOCK_20.csv`;
- `PHASE5_EXTRACTION_BLOCK_21.csv`.

These block files are the closest repository layer to the publication-level extraction decisions. They preserve unit IDs, source-report linkage, denominators, diagnoses, target-lesion mapping, actionability evidence, ascertainment, poolability decisions, provenance notes and QA commentary.

For publication-level traceability, use the source-report identifiers, `source_full_text_provenance`, diagnosis fields and extraction notes in these files together with the Phase 5 audit documentation. Do not infer absent data as zero.

### Post-rerun precedence layer

A systematic all-76 rerun later corrected target-diagnosis/conditional-lesion mappings for a subset of units. The numerical correction overlay is:

`data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`

This overlay has precedence for the post-rerun rows it explicitly updates. The Phase 6 database-freeze audit states that:

- 11 post-rerun primary rows reconcile to this numerical overlay;
- 17 unchanged primary rows reconcile to the latest frozen extraction blocks.

Do not compare the final Phase 6 input against an earlier block value and call it an error without first checking whether that unit is superseded by the post-rerun overlay.

### Early structured matrix

`data/phase5/PHASE5_STRUCTURED_EXTRACTION_MATRIX_v0.1.csv`

is an early structured extraction scaffold/schema and provenance aid. It is **not** the final authoritative numerical database and must not overrule later frozen extraction blocks, the rerun overlay or the Phase 6 frozen input.

## Frozen analysis-ready data

### Primary authoritative input

`data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`

Frozen blob SHA:

`1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`

Expected state:

- 28 rows;
- 28 unique `PRIMARY_POOLABLE` analytic units;
- denominator total = 1,999 harmonized-CCHD-negative final failed screens;
- Strict events total = 638;
- Expanded events total = 1,015;
- no duplicate primary analytic unit;
- all integer arithmetic closed.

This is the authoritative input for the primary Phase 6 meta-analysis.

### Etiologic secondary derivation

`data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`

Use this to audit the four etiologic outcomes appearing in the abstract.

Binding rule:

> Non-reported or non-point-identifiable etiologic categories are missing for that outcome, never zero.

Etiologic categories may overlap and must never be summed to reconstruct Expanded CAN-CCHD.

### Historical sensitivity input

`data/phase6/PHASE6_PREAMENDMENT_TGA_SENSITIVITY_INPUT.csv`

This is sensitivity-only and must not be substituted for the primary 28-unit input.

## Executable analysis

Primary/sensitivity analysis script:

`analysis/phase6/run_phase6_meta.py`

Secondary etiologic/subgroup script:

`analysis/phase6/run_phase6_secondary.py`

If execution is available, independently rerun them from the frozen Phase 6 inputs and compare the machine outputs with the abstract. Do not modify the inputs.

## Machine-readable results

Primary results:

`analysis/phase6/results/phase6_primary_results.json`

Secondary results:

`analysis/phase6/results/phase6_secondary_results.json`

Study-level primary results:

`analysis/phase6/results/phase6_study_results.csv`

Etiologic study-level results:

`analysis/phase6/results/phase6_etiology_study_results.csv`

Sensitivity results:

`analysis/phase6/results/phase6_sensitivity_results.csv`

Leave-one-out results:

`analysis/phase6/results/phase6_leave_one_out.csv`

Subgroup results:

`analysis/phase6/results/phase6_subgroup_results.csv`

## CRITICAL legacy firewall

Do **not** use:

`data/processed/can_cchd_agent.db`

for any scientific verification.

That database belongs to the legacy Browser Agent/app lineage and is preserved only as historical/legacy material. The restart-native CAN-CCHD project explicitly prohibited scientific data leakage from that database.

Any apparent agreement between legacy values and the current analysis is irrelevant. Any apparent disagreement is also irrelevant unless independently reproduced from the restart-native Phase 5/6 evidence chain.

## Frozen values the abstract currently claims

The v0.3 abstract should be checked against the following authoritative Phase 6 values:

- primary units: 28;
- harmonized-CCHD-negative final failed-screen denominator: 1,999;
- Strict CAN-CCHD median-study probability: 17.0%;
- Strict 95% profile-likelihood CI: 3.1%-46.8%;
- Strict marginal mean: 33.8%;
- Strict tau: 3.369;
- Expanded CAN-CCHD median-study probability: 69.4%;
- Expanded 95% CI: 57.7%-81.4%;
- Expanded marginal mean: 65.8%;
- Expanded tau: 1.110;
- other/non-target structural cardiac diagnosis: 26.6%;
- infection/sepsis: 16.7%;
- PPHN/pulmonary hypertension: 10.3%;
- respiratory disease: 8.7%;
- core sensitivity analyses do not reverse interpretation.

Do not merely confirm that the numbers are copied correctly. Audit whether each number is described with the correct estimand and level of generalizability.

## Required adversarial review questions

### A. Data integrity

1. Does the 28-row primary input truly reconcile to the Phase 5 extraction/rerun provenance?
2. Do denominator, Strict and Expanded integer totals reproduce exactly?
3. Are any primary units duplicated through report overlap or multisite handling?
4. Are any HOLD/SENSITIVITY_ONLY/NOT_POOLABLE units accidentally contributing primary weight?
5. Does the d-TGA/conditional-lesion post-rerun precedence remain correctly represented?
6. Is there any evidence of legacy-database contamination?

### B. Statistical claims

1. Is `median-study probability` an accurate description of the GLMM intercept-scale estimand used here?
2. Is `marginal mean` used correctly and never confused with the crude aggregate event ratio?
3. Does the abstract adequately communicate the extreme heterogeneity of Strict CAN-CCHD?
4. Is omission of the Strict prediction interval scientifically acceptable in a <=300-word conference abstract, or does it materially soften the heterogeneity problem?
5. Is Expanded appropriately described as `less heterogeneous`, not homogeneous or universal?
6. Is `Sensitivity analyses did not reverse the interpretation` fully supported by S1-S6?

### C. Etiologic claims

1. Reproduce the four reported pooled probabilities from the secondary results.
2. Confirm their outcome-specific `k` and missingness handling.
3. Determine whether listing them without confidence intervals in the conference abstract is scientifically misleading.
4. Confirm that the text does not imply mutual exclusivity or summability.

### D. Clinical implication / pediatric cardiology positioning

The abstract states:

> `These findings suggest that for pediatric cardiologists, frequently involved early after a failed screen, the encounter may represent more than exclusion of target heart disease...`

Treat this as an **external-evidence-supported clinical implication**, not a Phase 6 measured result.

Audit it independently against the sources summarized in:

`docs/PHASE11_SHA_CLINICAL_POSITIONING_CITATION_MINING_2026-08-22.md`

At minimum, independently verify the AAP 2025 clinical report, current CDC guidance, Saudi national screening experience/recommendations and the Saudi prospective cohort before accepting the wording.

Questions:

1. Is `frequently involved early` supportable across published pathways without implying universal referral hierarchy?
2. Does `opportunity to recognize ... and expedite multidisciplinary care` overstate the evidence or appropriately express professional implication?
3. Does the sentence improperly imply that pediatric cardiologists themselves are responsible for diagnosing/managing sepsis or respiratory disease?
4. Would a narrower wording preserve the SHA-specific relevance with less inference?

### E. Abstract reporting / SHA fit

1. Verify the <=300-word count independently, including all four required headings.
2. Verify the title remains <=40 words.
3. Does the title accurately reflect the primary/secondary outcome hierarchy?
4. Does `Beyond CCHD` risk implying the review is not fundamentally about CCHD screening?
5. Does the introduction clearly define the clinical problem without using `false positive` pejoratively or imprecisely?
6. Is the Methodology sufficient for a scientific reviewer to understand denominator, endpoint hierarchy and random-effects model?
7. Does the Conclusion go beyond what the data and external pathway evidence can defend?
8. Identify any sentence that would make you reject, downgrade or challenge the abstract if you were a skeptical SHA reviewer.

## Forbidden shortcuts

Do not:

- treat 638/1,999 or 1,015/1,999 as the pooled random-effects estimates;
- write that 17.0% is a universal patient-level rate;
- write that 69.4% had documented management consequences;
- sum etiologic categories;
- convert etiologic missingness to zero;
- claim early vs late screening equivalence;
- claim publication bias is absent;
- use the legacy SQLite database;
- repair any genuine scientific inconsistency silently;
- begin with stylistic rewriting before completing the scientific audit.

## Required output format

Start the review with one overall verdict:

- **PASS** — no material scientific/reporting concern;
- **MINOR REVISION** — scientifically sound, but wording/reporting changes advisable;
- **MAJOR REVISION** — important claims or methods presentation require correction before submission;
- **SCIENTIFIC STOP** — discrepancy may affect frozen data/results and requires investigation before further drafting.

Then provide:

1. **Claim-by-claim audit table** with columns: `Abstract claim | Source checked | Verdict | Problem | Required correction`.
2. **Independent numerical reconciliation** of the 28-unit primary input and the four etiologic outcomes.
3. **Estimand/heterogeneity audit**.
4. **Clinical-positioning evidence audit**.
5. **SHA acceptance-risk assessment**: strongest feature, most vulnerable feature, likely reviewer objection.
6. **Exact recommended edits only after the audit is complete**.
7. **Final recommendation**: submit as-is / minor v0.4 / major rewrite / scientific stop.

If you create a repository report, save it as:

`docs/PHASE11_SHA_ADVERSARIAL_REVIEW_REPORT_2026-08-22.md`

Do not overwrite `PHASE11_SHA_ABSTRACT_DRAFT_v0.3.md` during the first-pass review.

## One-line prompt for the adversarial-review chat

**Act as an independent adversarial reviewer of CAN-CCHD SHA abstract v0.3 on branch `phase11-sha-abstract`. Read `docs/PHASE11_SHA_ADVERSARIAL_REVIEW_HANDOFF.md` first, audit the abstract all the way back to the restart-native Phase 5 raw extraction blocks and frozen Phase 6 inputs/results, independently verify the pediatric-cardiology positioning evidence, and do not edit the abstract until you have issued a PASS/MINOR/MAJOR/SCIENTIFIC STOP verdict.**
