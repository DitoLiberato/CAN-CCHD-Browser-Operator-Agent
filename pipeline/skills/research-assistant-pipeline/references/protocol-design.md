# Co-design a project protocol

## Discover a worthwhile question

Accept either a concrete question or no idea yet. Ask about field, recurring
uncertainties, available cases/data, collaborators, access, time and audience. Ask a
few questions at a time. Offer a small set of directions with tradeoffs. Never invent
patients, resources, novelty or feasibility.

Use labeled exploratory probes to challenge novelty and establish terminology. Record
sources and limits. Preserve candidates/sentinels separately from an eligible corpus.
Assess teaching value, unresolved questions, conflicting evidence, context, updates
and feasibility. Similar prior publications may change the contribution rather than
invalidate it. Keep “first”/“unique” provisional until justified and human-reviewed.

## Choose and justify a design

Determine whether evidence comes from original clinical material, publications or
both. Explain alternatives and burdens; obtain the researcher's decision.

- Case report: source documentation, timeline/endpoint, teaching purpose, uncertainty,
  consent/privacy status and the literature's role.
- Original case series: setting/time, ascertainment, selection/completeness, variables,
  follow-up and descriptive aims. Check whether comparisons require another design.
- Published-case synthesis: report/patient identities, overlap and reporting bias;
  selected reported cases do not provide a population-frequency denominator.
- Focused/narrative review: explicit scope and selection, without unsupported claims
  of comprehensive or systematic coverage.
- Broad/focused review: choose scoping, narrative or systematic methods according to
  purpose, not manuscript length. Consider synthesis with or without pooling.
- Meta-analysis: estimand, unit, data structure and a conditional pooling plan. A
  review without pooling may be the valid final outcome.

For a clinical article plus review, plan two streams, separate identifiers and
verification, and integration only after the source facts are accepted.

## Generate rules with reasons and tests

Use `protocol/RULES.csv`. For consequential rules record `rule_id, domain, rule,
rationale, methodological_source, operational_test, human_approval_id, status`.

Sources can be recognized guidance or an explicit reasoned researcher choice where
guidance permits it. Record version/access date and applicability. Do not invent
universal cutoffs or attribute unsupported thresholds to a guideline.

Personalize question/design/contribution; population/context; exposure/intervention/
comparator when relevant; outcome hierarchy or qualitative/teaching objectives;
units/denominators/overlap; sources/queries/restrictions; eligibility and review roles;
extraction/provenance/missingness/verification; appraisal and certainty methods;
mapping/derivations; synthesis/assumptions/sensitivity; ethics/privacy requirements
for the actual setting; AI scope; human decisions; phase criteria and amendments.

## Compile the execution plan

Keep phase IDs 0–11. In `protocol/EXECUTION_PLAN.md` define each phase's local meaning,
streams, tasks, inputs, outputs, criteria, human decisions and dependencies. Mark a
phase not applicable only with an approved rationale and replacement control where
needed. Never waive traceability or human control.

Distinguish external standards from local decisions. Reporting checklists are not
conduct methods or validity scores. Verify current primary guidance when selecting
methods. If access fails, disclose this and defer dependent commitments rather than
claiming verification.

Generate meaningful tests: justified sentinel retrieval, companion-report/cohort
identity, evidence for each required field, valid denominator derivations, and
reproduction of locked results. Avoid arbitrary numeric targets just to automate a gate.

## Approve and freeze

Present protocol, rules, execution plan and unresolved choices for human review.
Record the actual decision/scope in `audit/approvals.jsonl`; preserve approved versions
and hashes. Identify the human and a real source of their decision. The assistant can
transcribe a decision, never supply it.

Overall approval may cover explicitly included component rules. Unresolved choices
remain pending. Changes after relevant results are seen require amendments that
distinguish prospective, post-hoc and exploratory choices. Reopen affected work;
preserve the former protocol and approval.
