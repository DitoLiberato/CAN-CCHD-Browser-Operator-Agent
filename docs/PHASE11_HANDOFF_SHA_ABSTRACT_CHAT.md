# CAN-CCHD Phase 11 — Handoff for Dedicated SHA Abstract Chat

Date: 2026-08-22  
Target branch: `phase11-sha-abstract`  
Status: **SAFE RESUME — SHA ABSTRACT DRAFTING ONLY**

## Mission of this chat

Produce, refine and finalize the Saudi Heart Association (SHA37) conference abstract from the frozen CAN-CCHD systematic review/meta-analysis.

This chat is an editorial/compression stream. It is **not** an analysis stream and must not reopen Phase 5/6 scientific decisions by default.

## Start here

Read in this order:

1. `docs/PHASE11_WRITING_SPLIT_HANDOFF_2026-08-22.md`
2. `docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.1.md`
3. `docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`
4. `docs/PHASE6_PROGRESS_SNAPSHOT_2026-08-22_ANALYSIS_COMPLETE.md`
5. `docs/PHASE6_ANALYSIS_CLOSEOUT_2026-08-22.md`

Only open deeper Phase 6 audit/results files when necessary to verify a statement or number.

## Existing draft

Current starting draft:

`docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.1.md`

It is explicitly `draft_requires_human_review`.

Current candidate title:

**Clinically Actionable Non-CCHD Diagnoses After Failed Newborn Pulse Oximetry Screening: A Systematic Review and Meta-analysis**

Alternative already preserved for comparison:

**Beyond False Positives: Clinically Relevant Disease After Failed Newborn CCHD Pulse Oximetry Screening — A Systematic Review and Meta-analysis**

## SHA submission constraints already verified in the project

At the last check on 2026-08-22:

- English language;
- title <=40 words;
- abstract <=300 words;
- required headings: Introduction, Methodology, Results, Conclusion;
- current published deadline: 31 August 2026.

Portal counting and any author/institution/approval fields must be rechecked immediately before submission because congress instructions can change independently of the frozen scientific analysis.

## Scientific hierarchy for the abstract

Primary endpoint: **Strict CAN-CCHD**.

But the most clinically intuitive headline finding is the broader **Expanded CAN-CCHD** burden. The abstract must therefore preserve the prespecified hierarchy while avoiding a presentation in which the striking Expanded result hides the extreme heterogeneity of Strict.

Essential numbers available for inclusion:

- 28 independent primary units;
- denominator 1,999;
- Strict median-study 17.0% (95% CI 3.1%-46.8%), marginal mean 33.8%, tau 3.369;
- Expanded median-study 69.4% (57.7%-81.4%), marginal mean 65.8%, tau 1.110;
- etiologic outcomes: PPHN/PH 10.3%, respiratory 8.7%, infection/sepsis 16.7%, other/non-target structural cardiac diagnoses 26.6%;
- sensitivity analyses did not reverse interpretation;
- no clear timing subgroup effect.

Not all of these must survive into the <=300-word final version.

## Editorial priorities

1. Make the question immediately understandable to cardiology/congenital-heart-disease reviewers.
2. Frame the historical label `false positive` carefully: failed screens without target CCHD may still reveal clinically useful disease.
3. Avoid spending excessive words explaining statistical machinery unless needed to make the unusual estimand understandable.
4. Preserve `median-study` wording or an equally accurate alternative whenever reporting the GLMM intercept estimate.
5. Do not present 17.0% as a universal rate.
6. Decide whether all four etiologic estimates materially improve acceptance probability; remove them if their words are better spent strengthening the core clinical message.
7. Avoid a conclusion stronger than the evidence supports.
8. Keep the draft comfortably below 300 words to allow portal-specific counting differences.

## Questions this chat should resolve

- Is `Clinically Actionable` too narrow for the title given that Expanded CAN-CCHD is the clearest finding?
- Is `Beyond False Positives` compelling or too promotional for SHA?
- How much of the extreme Strict heterogeneity must remain in a 300-word abstract?
- Should the abstract foreground the Expanded 69.4% result after establishing Strict as primary?
- Should etiologic outcomes be all listed, selectively listed, or omitted?
- Is one concise sentence on sensitivity/subgroup robustness worth the word cost?

## Non-negotiable guardrails

Do not state:

- “17% of false-positive babies had actionable disease” without estimand/heterogeneity qualification;
- that 638/1,999 is the random-effects estimate;
- that 69.4% had documented actionability;
- that timing had no effect/equivalence;
- that publication bias was absent;
- that etiologic categories sum to the Expanded endpoint.

If a number appears inconsistent with the frozen package, verify it rather than inventing a reconciliation. A genuine scientific inconsistency must be escalated explicitly instead of being silently edited in prose.

## Deliverables for this chat

Expected progression:

- v0.2 scientific positioning revision;
- title comparison/selection;
- v0.3 near-final <=300-word version;
- explicit word count;
- submission-field checklist;
- final `draft_requires_human_review` version;
- repository snapshot before portal submission.

Do not start writing the full manuscript in this chat. Cross-document consistency will be checked later against the manuscript stream.

## One-line prompt for the new chat

**Continue CAN-CCHD Phase 11 on branch `phase11-sha-abstract`. Read `docs/PHASE11_HANDOFF_SHA_ABSTRACT_CHAT.md` first. Refine the existing SHA abstract v0.1 toward a scientifically precise, compelling <=300-word submission without changing any frozen Phase 6 scientific value.**
