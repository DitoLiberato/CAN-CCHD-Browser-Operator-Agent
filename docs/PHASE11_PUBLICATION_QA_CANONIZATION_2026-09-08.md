# Phase 11 Publication-QA Canonization — 2026-09-08

## Purpose
This document records the manuscript-QA defects discovered during post-deadline author review of the CAN-CCHD manuscript and the permanent pipeline changes made so future evidence-synthesis projects do not repeat them.

This is a methodological lessons-to-canon record. It does not alter frozen CAN-CCHD scientific estimates.

## Canonical reusable specification

Primary new canon:

`docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md`

Operational template:

`docs/templates/PUBLICATION_QA_REPORT_TEMPLATE.md`

The Publication QA Canon is now incorporated into the Master Specification, Phase 0 protocol requirements, Search Collection, Extraction/QA, Analysis/Writing, and acceptance tests.

---

# QA lessons discovered and permanent corrections

## 1. Author credentials leaked into the byline
Observed defect: the first author carried `MD` while other authors correctly appeared as names only.

Permanent rule:
- scientific byline defaults to author names only;
- degrees/credentials are included only if required by the target venue;
- administrative roles are not byline content unless explicitly required.

Canon: Publication QA sections 2 and 13; Phase-11 tests.

## 2. Affiliation numbering was administratively ordered rather than author-first ordered
Observed defect: the first author's institution was not affiliation 1.

Permanent rule:
- affiliation numbers are assigned in order of first appearance among authors;
- first author's first institution is affiliation 1;
- new institutions receive the next unused number when first encountered.

Canon: Publication QA section 2; Phase-11 acceptance tests.

## 3. Bibliography was assembled before the citation architecture
Observed defect: reference numbers reflected a prebuilt list rather than strict order of first use in the manuscript.

Permanent rule:
- citation architecture is built first;
- bibliography is generated second;
- numbered references follow actual first appearance in publishable content;
- reused sources retain their first assigned number.

Canon: Publication QA section 5.

## 4. Reference existence and claim support were not fully audited
Observed defect: a citation could exist in the list without explicit documentation that it supported the sentence for which it was used; at least one prior bibliography entry was not required by retained prose.

Permanent rule:
- generate a reference-to-claim matrix;
- verify source identity/metadata;
- verify that the source supports the specific claim;
- remove orphan references from release candidates.

CAN-CCHD implementation example:
`docs/PHASE11_MANUSCRIPT_REFERENCE_CLAIM_AUDIT_v1.0.md`

Canon: Publication QA section 5; acceptance tests.

## 5. Study-level figures contained publications absent from the bibliography
Observed defect: forest plots displayed 28 analytic units, but the bibliography initially covered only a subset of the source publications.

Permanent rule:
- every named study/unit in any table or figure must map to a bibliographic reference;
- generate an analytic-unit-to-publication crosswalk before publication release;
- every row must resolve to the primary publication actually supplying the analytic unit;
- site-level units from one publication reuse one reference;
- companion reports do not create duplicate analytic weights.

CAN-CCHD implementation example:
`docs/PHASE11_CAN_CCHD_PRIMARY_FIGURE_REFERENCE_CROSSWALK_v1.0.md` / latest equivalent crosswalk artifact.

Canon: Publication QA sections 5 and 7; Extraction/QA source-identity fields; acceptance tests.

## 6. Internal study labels were treated as if they were sufficient bibliographic identity
Observed defect: the internal label `Kumar 2017` was initially carried forward without a complete source-identity audit; the definitive 22,601-newborn publication required separate verification.

Permanent rule:
- `analytic_unit_id`, surname-year labels, report IDs, or plot labels are not bibliographic provenance;
- every quantitative unit must carry verified primary publication identity before publication display;
- apparent conflict between internal label and source provenance is a publication SCIENTIFIC STOP until resolved.

Canon: Extraction/QA publication-identity fields and Publication QA section 7.

## 7. Primary and secondary outcomes were visually mixed
Observed defect: a table presented primary, key secondary/sensitivity, and secondary etiologic outcomes as one undifferentiated list.

Permanent rule:
- primary outcome is explicitly named;
- secondary outcomes are explicitly named;
- sensitivity/exploratory outcomes retain their status;
- tables use separate panels/tables or explicit hierarchy labels where mixing could imply equal endpoint status.

Canon: Phase 0 hierarchy requirement; Publication QA sections 3 and 6.

## 8. Selective bold created unintended scientific emphasis
Observed defect: table formatting used bold on selected scientific results without a prespecified semantic reason.

Permanent rule:
- bold/shading/emphasis in scientific tables requires an explicit function;
- values are not highlighted merely because they are important or primary unless the table's design rule states that purpose.

Canon: Publication QA section 6; acceptance tests.

## 9. Outcome hierarchy was incompletely named in prose
Observed defect: manuscript prose discussed multiple endpoints without consistently calling them primary versus secondary.

Permanent rule:
- protocol must prospectively freeze outcome hierarchy;
- manuscript/abstract/results/tables/figures must use the same hierarchy language;
- no post-result promotion of a secondary/sensitivity endpoint without documented protocol amendment.

Canon: Phase 0 reusable requirements; Publication QA section 3.

## 10. AI use was initially insufficiently transparent in Methods
Observed defect: early manuscript versions did not adequately describe material AI assistance, the phase-gated GitHub workflow, human checkpoints, or the distinction between AI suggestions and human scientific decisions.

Permanent rule:
- disclose material generative-AI/browser-agent use;
- state actual tasks assisted;
- state human-only scientific decisions;
- do not describe AI as an independent second reviewer unless prospectively designed and implemented as such;
- segregate AI-suggested extraction until human verification;
- report the actual phase count/names;
- do not invent historical model/version metadata if it was not prospectively retained.

Canon: Phase 0 AI plan; Publication QA section 9; Phase-11 acceptance tests.

## 11. Search methods needed exact-query and source-availability transparency
Observed defect: a concise manuscript description risked obscuring exact queries, public-web versus native-platform completeness, and unavailable prespecified subscription sources.

Permanent rule:
- preserve executed exact queries and source-level status;
- publish representative query plus complete supplement when possible;
- disclose planned-but-unavailable major sources;
- distinguish public-web saturation from native-platform completeness;
- never manufacture unrecoverable native counts/PRISMA identification numbers.

Canon: Search Collection publication-provenance section; Publication QA section 8.

## 12. Repository-native labels leaked into publication prose
Observed defect: terms such as `PRIMARY_POOLABLE`, `HOLD_PENDING_QA`, internal phase labels, and report/unit identifiers created a copy-from-repository appearance and reduced editorial readability.

Permanent rule:
- preserve exact machine labels in audit trail;
- translate them into scientific prose in publication artifacts unless the code/status is itself scientifically relevant.

Canon: Publication QA core principle and Phase-11 publication-language firewall.

## 13. Abbreviations required an independent publication audit
Observed defect: some abbreviations were initially not expanded at first use or appeared in contexts where the abstract/table/figure needed to stand alone.

Permanent rule:
- abstract and main text each receive independent first-use abbreviation checks;
- tables/figures define abbreviations independently;
- avoid nonstandard title abbreviations.

Canon: Publication QA section 4.

## 14. Rendered artifacts exposed formatting defects invisible in source text
Observed defects included misaligned first-row table numbers and the need to inspect page breaks, figure readability, and final rendered output.

Permanent rule:
- after meaningful edits, render DOCX/PDF;
- inspect every page or equivalent complete visual representation;
- check alignment, clipping, captions, footnotes, special characters, unintended emphasis, and figure resolution.

Canon: Publication QA section 11.

## 15. Venue compliance is a separate QA task
Observed need: conference title/abstract limits, structured headings, table/figure allowance, award manuscript rules, and portal behavior required independent verification rather than being assumed from manuscript conventions.

Permanent rule:
- verify current target-venue instructions immediately before submission;
- use the portal word counter as the final operational check when available;
- reconcile abstract values to the frozen manuscript/analysis immediately before final submit.

Canon: Publication QA section 10.

---

# Upstream schema change

The most important prospective change is upstream of writing.

Every analytic unit that may enter synthesis or a study-level display now requires verified publication identity fields, including:

```text
analytic_unit_id
primary_source_report_id
primary publication author/year/title/source
DOI/PMID/PMCID or another stable identifier when available
full-text provenance
companion/report/program cluster information
publication_identity_verification_status
```

A unit can be scientifically analyzable while bibliographic cleanup is pending, but it cannot be declared publication-display-ready until source publication identity is verified.

This prevents late-stage reconstruction of forest-plot references.

---

# Release-state change

Phase 11 now has a mandatory sub-gate without adding a new numbered phase:

```text
Draft -> Publication QA -> Human author review -> Release candidate
```

The canonical workflow therefore remains Phases 0-11 (12 numbered stages).

A `SCIENTIFIC_STOP` or open HIGH publication-QA finding blocks release.

---

# Files changed to implement the canon

- `docs/00_MASTER_SPEC.md`
- `docs/01_RESEARCH_PLAN_AND_PROTOCOL.md`
- `docs/03_SEARCH_COLLECTION_AND_BROWSER_AGENT.md`
- `docs/07_EXTRACTION_DIAGNOSIS_AND_QA.md`
- `docs/08_ANALYSIS_AND_WRITING.md`
- `docs/10_TESTS_AND_ACCEPTANCE_CRITERIA.md`
- `docs/11_PUBLICATION_QA_AND_REPORTING_CANON.md` (new)
- `docs/templates/PUBLICATION_QA_REPORT_TEMPLATE.md` (new)
- `README.md`

Project-specific QA artifacts remain useful examples but are not substitutes for the reusable canon.

## Scientific impact

None of these changes alter the frozen CAN-CCHD analysis values. They strengthen reporting, traceability, reproducibility, bibliographic integrity, and publication-readiness controls.
