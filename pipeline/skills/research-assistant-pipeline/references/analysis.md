# Synthesis and analysis

Read the approved plan, verified inputs, QA report, freeze approval and input hashes.
Refuse to present analyses of AI-only suggestions as scientific results. Exploratory
code may use clearly synthetic data, kept separate and never reported as real results.

Choose methods for the estimand and data structure: descriptive clinical reporting,
narrative/thematic synthesis, proportions, comparative effects, diagnostic accuracy,
time-to-event or other justified methods. The CAN-CCHD analysis is not a generic
statistical engine. Do not copy its transformations, model, priors or denominators.

For quantitative synthesis, justify effect measure, denominator, independent units,
sampling variance, model, transformations, zero/rare events, dependence, uncertainty,
heterogeneity and sensitivity analyses. Distinguish participant-level aggregates,
study-level summaries and model-based estimands. Assess whether pooling is clinically
and statistically defensible. Inadequate comparability may require no pooling.

Use primary methodological references and current library documentation for the
chosen model. For unfamiliar/highly specialized methods, expose uncertainty and
seek methodological input. AI output is not its own method reference.

Prespecify the main analysis where possible. Mark post-hoc/exploratory analyses and
record rationale. Do not select studies, outcomes or models to obtain significance.
Address missingness and reporting/publication bias appropriate to the evidence;
do not apply tests mechanically when their conditions are unmet.

Retain reproducible code, environment/dependency versions, input hashes, parameters,
seeds when relevant and run logs. Validate with independent calculations, known
benchmarks or meaningful synthetic edge cases for the chosen method. Check count
reconciliation, identity independence, event/denominator bounds when applicable,
units, estimates/intervals and sensitivity to consequential choices.

The skill ships no universal meta-analysis implementation. Generate and test scripts
only after method selection, and distinguish code checks from scientific acceptance.
When execution is unavailable, supply a reviewable analysis plan or reproducible
script; never invent results or claim it ran.

For narrative synthesis, preserve contrary findings, quality, uncertainty and limits
of comparison. For published cases, do not infer prevalence/incidence from selected
reports. Avoid causal claims unsupported by design or confounded care sequences.

Produce a results package with tables/figures, analytic-unit crosswalk, definitions,
main/sensitivity/exploratory results and limitations. Obtain human interpretation
review. Lock accepted outputs before writing and propagate corrections explicitly.
