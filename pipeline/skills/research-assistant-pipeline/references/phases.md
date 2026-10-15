# Twelve-phase contract, version 0.1

Preserve IDs 0–11 from the original specification. Translate these process checkpoints
into a project-specific contract in Phase 0. They do not supply scientific criteria,
default databases or numerical thresholds.

| ID | Phase | Typical input → output | Exit evidence / human decision |
|---|---|---|---|
| 0 | Question, feasibility and protocol | Idea/interests → protocol, rules, execution plan | Design, methods, AI roles and phase applicability approved |
| 1 | Search/source planning and collection | Source plan → exact queries/source log, raw collection | Actual coverage/limitations reviewed; plan fulfilled or amended |
| 2 | Normalization and identity reconciliation | Raw records → registry with duplicate/overlap links | Identity rules applied, ambiguities adjudicated, originals preserved |
| 3 | Preliminary relevance screening | Records → initial dispositions | Queue covered, uncertainties retained, human acceptance recorded |
| 4 | Full source retrieval | Candidates → texts or permitted clinical-source references | Attempts/statuses documented; unavailable differs from ineligible |
| 5 | Final eligibility and corpus adjudication | Sources → corpus, exclusions/reasons and limitations | Membership and analytic-unit identities human-approved |
| 6 | Structured extraction and appraisal | Corpus → suggested fields and appropriate appraisal | Required suggestions/locations present, missingness explicit |
| 7 | Human verification | Suggestions → accepted/corrected/rejected/unresolved fields | Scientific inputs and source identities reviewed within recorded scope |
| 8 | Mapping and harmonization | Verified facts → derivations, categories or comparison matrix | Meaning, units, derivations and overlap accepted |
| 9 | Scientific QA and data lock | Accepted inputs → QA report and versioned snapshot | Material defects resolved, limitations explicit, human lock |
| 10 | Synthesis and analysis | Locked inputs/plan → reproducible results | Appropriate methods, uncertainty and sensitivity assessed; interpretation reviewed |
| 11 | Manuscript and publication QA | Results → text, tables, figures, references | Publication QA → human author review → explicit release decision |

## Adaptation

- For a clinical case, collection may mean document inventory, identity reconciliation
  duplicate episodes/documents, and eligibility the defined clinical course. Keep
  clinical sources in the approved environment. Literature has a separate stream.
- Original series need ascertainment and clinical verification; published-case reviews
  need bibliographic and patient-overlap reconciliation. Document both explicitly.
- Phase 10 can be a defensible narrative synthesis with calibrated conclusions.
- Apply PRISMA search counts to the review stream, never fabricate them for original
  patients. Map consent/privacy and other required controls to relevant phases.
- Allow later-phase forms/plans/exploratory code as drafts; do not accept results
  before dependencies are satisfied.
- Use task-level subgates where useful and record them; do not silently renumber phases.

## Transitions

States: `locked`, `available`, `in_progress`, `blocked`, `awaiting_human`, `completed`,
`completed_with_note`, `not_applicable`.

Before dependent scientific work, require evidence and human closure. A limitation
must identify the missing requirement, effects and decision. Integrity defects cannot
be cured by a note. Phase 7–9 can iterate while retaining provenance; obtain the
final lock after all required inputs and derivations are accepted. Post-lock changes
reopen affected work and invalidate dependent results.

Phase 11 includes Draft → Publication QA → Human review → Release. A draft is not
completion. External submission/email/publication requires the researcher's explicit
instruction for that action, separate from scientific approval.
