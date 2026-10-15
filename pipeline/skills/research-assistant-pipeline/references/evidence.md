# Evidence identity, selection and verification

## Entities and deduplication

Preserve raw records, normalize into stable IDs and link each to query/source.
Distinguish database record, publication/report, underlying study/cohort/patient,
site/cluster, and analytic unit. Two reports may share participants without being
duplicate publications. A report can contain multiple eligible units.

Create an approved deduplication policy based on the actual metadata. Exact
identifiers can support mechanical grouping under that policy; conflicts still need
review. Title/year alone is a candidate match, not universally sufficient proof.
Propose fuzzy thresholds with rationale and calibration; never import legacy numeric
thresholds. Preserve all originals and merge provenance. Human-review ambiguous
matches and population overlap. Prioritization may order work; it is not eligibility.

## Selection

Convert the question into operational inclusion/exclusion rules and ambiguity handling.
At title/abstract level retain uncertainty for fuller evidence where appropriate.
Provide item ID, source, applicable criterion and reason with every AI suggestion.
Keep proposed decisions separate from final human dispositions.

For final selection, distinguish eligible, excluded with scientific reason, not
retrieved, insufficient information and awaiting adjudication. Report missing texts
as such, even if the final synthesis cannot include them. Preserve companion reports
as evidence while avoiding duplicate analytic weight. Choose an independent human
review process appropriate to the method; never describe AI plus one human as two
independent human reviewers.

## Extraction and appraisal

Co-design a dictionary with field definition/type/unit, required status, allowable
values, missingness, evidence requirement and derivation rules. Separate raw text and
numeric/transformed values. Retain source ID and page/table/section; use brief
necessary quotations within permitted use, not a public corpus of copyrighted PDFs.

Represent suggestions with `ai_suggested`; record verification as `verified`,
`corrected`, `rejected`, `unavailable_with_note` or `needs_review`. Human verification
must identify the field or bounded batch and evidence. Confidence scores do not
replace verification. Unknown, not reported, not applicable and zero remain distinct.

Select appraisal tools for included designs and question. Record domain-level
judgments/evidence and human review. Do not manufacture a numeric quality score or
call a reporting checklist a risk-of-bias tool. If a required method was not done,
disclose and address that rather than inventing retrospective completion.

## Mapping and derivation

Retain original terms beside harmonized variables. Obtain human approval of mapping
rules and consequential ambiguous cases. Never silently convert a loosely reported
diagnosis into a protocol-defined endpoint. Preserve primary/secondary/exploratory
hierarchy. Record denominator bases, overlapping categories and time windows.

Derived values require accepted source fields, an explicit formula, assumptions and
verification. A plausible subtraction is not sufficient if definitions/time frames
differ. Verify units, non-additivity and dependence before combining quantities.

For clinical cases, distinguish planned from performed care and contemporaneous
observations from later interpretation. Literature cannot rewrite the clinical record.
For a case plus review, merge interpretive streams only after separate verification.

## Lock

Before synthesis, export accepted inputs, definitions, report-unit crosswalk, missingness,
appraisal and limitations. Freeze the actual files with hashes and a human approval.
An accepted missing value can remain missing; it cannot enter a calculation as a
fabricated zero. Reopen and revalidate if data, rules or identities change.
