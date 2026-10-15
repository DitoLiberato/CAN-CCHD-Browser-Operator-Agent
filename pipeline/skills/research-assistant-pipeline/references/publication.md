# Publication QA

Draft from accepted scientific artifacts. A draft is not submission-ready. Use
scientific language that readers understand while retaining repository traceability.

## Required checks, tailored to the project

- Reconcile numerical statements and all tables/figures to accepted, locked results.
- Preserve primary/secondary/exploratory hierarchy and the exact estimand/denominator.
- Distinguish case observations, source claims, biological plausibility and author
  interpretation. Calibrate novelty, causality and generalizability.
- Report actual searches, dates, restrictions, unavailable sources, reviewer roles,
  selection, extraction, appraisal, analysis and deviations. Do not retrofit ideal
  methods that were not performed.
- Verify each reference's existence/identity and support for its attached claim.
  Prioritize primary evidence. Maintain `REFERENCE_CLAIM_AUDIT.csv`; assign numeric
  references by first appearance where the style requires it, with no orphan entries.
- Map each displayed study/unit to its publication in a source crosswalk. Multiple
  units from one report share its reference; companion reports do not gain weight.
- Make tables/figures self-contained: endpoint, denominator, units, interval/model,
  missingness, overlap, abbreviations and citations. Verify labels against data.
- Apply the correct reporting checklist(s), document applicability and actual item
  locations. PRISMA is not a substitute for conduct/appraisal; CARE is not a trial
  standard. A checklist pass does not establish validity.
- Verify author names/order, contributions, affiliations, funding, conflicts,
  corresponding-author metadata, ethics/consent and target-required declarations.
  Do not invent approvals or write blanket ethics exemptions.
- Prepare truthful pipeline citation and AI disclosure from recorded use. Distinguish
  tool authors from study authors. Never call the AI an independent human reviewer.
- Verify current target-venue instructions only when relevant, including AI policy,
  limits, sections, figures, format and declarations. Record source and date.
- Render final DOCX/PDF/slides and inspect actual pages for clipping, tables, captions,
  fonts/symbols, pagination and figure legibility. Record what was inspected. Do not
  mark unrendered or uninspected artifacts visually checked.

## Verdict and human release

Use PASS, MINOR_REVISION, MAJOR_REVISION or SCIENTIFIC_STOP with findings, evidence,
severity, owner and resolution. Missing verified sources, unsupported quantitative
claims, misrepresented methods or material unresolved conflicts block release.
Fix or remove the affected claim/unit through human review and rerun affected checks.

Provide `publication/PUBLICATION_QA.md`, claim/reference audit, source crosswalk when
applicable, reporting checklist, AI-use statement and citation check. Have the human
authors review scientific content, contributions and final artifact. Record explicit
release approval with artifact scope/hash. A manuscript can be internally approved
without authorization to submit or send it externally.
