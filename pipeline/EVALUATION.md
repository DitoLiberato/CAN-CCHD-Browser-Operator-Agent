# Pilot evaluation — 0.1.0-pilot

Evaluation date: 2026-10-15. This is a pilot release, evaluated as software and with
simulated assistant exercises. It has not completed an external Claude user trial,
an end-to-end scientific study, peer review or validation of every supported design.
All software approvals and analytic values in tests are explicitly synthetic.

## Reproducible software checks

From the repository root, with Python 3.10 or newer:

```bash
python3 -m unittest discover -s pipeline/tests -v
python3 pipeline/tests/integrity_scenarios.py
```

The regression suite contains **31 passing tests**. It covers clean bootstrap,
overwrite refusal, correct initial draft state, pinned snapshot integrity, formal
phase prerequisites, recorded human decision role and scope, protocol version and
artifact changes, phase closure, non-applicability requirements, scientific QA,
data freezes, extraction schema and exact field approval, source registry links,
release scope and path containment. It also extracts the distributed ZIP in an
isolated directory, creates a new project and validates it using the bundled scripts.

An independently constructed scenario suite contains **46 cases**. After corrections,
five consistent workflows passed, 40 invalid cases were rejected, and one prose
state-conflict case passed the structural checker as expected because reconciliation
of narrative state is a documented assistant/human task. There were no crashes.
The suite labels this manual boundary explicitly and treats unexpected outcomes as
failures; it does not redefine the contradictory prose as acceptable project state.

The independent review exposed gaps during development: malformed extraction tables,
whitespace inclusion values, source registry links, lock timing, severity values,
manifest consistency and an uncaught unsafe path. These were corrected and rerun;
the associated regressions are retained. Approval scope was also tightened to bind
accepted fields and frozen/release files to their exact reviewed content.

Additional checks: skill metadata validation; identical installed/repository workflow
payloads; referenced local files present; a self-contained 40-file ZIP; deterministic
packaging and checksum. The package contains the general tool and empty project
templates, with no CAN-CCHD study database, results, Git history or patient records.

Installation in the native host regenerates presentation metadata. A regression
test and an actual installed-skill smoke test confirm that this does not invalidate
the workflow payload. The generated project's lock still covers the entire actual
snapshot, including host metadata; edits after the lock are detected.

## Assistant behavior exercises

The [scenario prompts](tests/assistant-scenarios.md) can be reused with another host.
Exercises used fresh Codex agent contexts and actual skill files. They are not Claude
tests and do not establish cross-model performance equivalence.

| Exercise | Observed behavior |
|---|---|
| Researcher without an idea | Started Phase 0, offered alternative directions and asked about context/resources; did not invent novelty, choose a design or claim tools/approvals were available. |
| Eight original cases plus fourteen publications, requested frequency/meta-analysis | Prepared a draft protocol, rules and search plan with separate clinical/literature streams; identified the missing population denominator; made pooling conditional; kept articles as candidate material and scientific approvals pending. |
| Fresh-context resumption | Recovered Phase 0 and draft-0.1 from files, checked 40 pinned hashes, preserved the snapshot and pending human decisions, and prepared the next design decision without repeating searches or claiming approval. |

The design exercise performed labeled exploratory web probes and recorded them as
such. It did not run a native systematic database search, include a corpus, extract
patient data, select a statistical model or produce scientific results. The design
proposal remains subject to actual researcher and methodological review.

## Boundaries that remain

- The validator checks recorded consistency. A user who controls all files can
  fabricate decisions and recompute hashes; this is not authentication or a secure
  electronic signature system.
- Narrative state, sources, clinical truth, inclusion decisions, model suitability,
  ethics/consent, reporting completeness and claim/reference support need actual
  human review and project-specific checks. An empty template is not completed work.
- Structural success does not prove a frozen dataset contains all and only the right
  scientific inputs or that a manuscript faithfully represents them.
- The skill cannot grant tool permissions, subscriptions, GitHub write access or
  persistent storage. Those capabilities must be checked in the actual host.
- A protocol can legitimately end in descriptive or narrative synthesis without
  meta-analysis. No universal statistical implementation is claimed or shipped.
- No external account/repository was created for a pilot researcher, no manuscript
  was submitted and no DOI was registered during these tests.

## Next field test

Use the [Portuguese pilot guide](PILOT_GUIDE_PT.md) in the colleague's own Claude
account. Verify installation/activation, capability discovery, tailored protocol
proposals, a separate research workspace and resumption in a new conversation.
Record observed failures with the exact tool version and a deidentified example.
Only later report a completed scientific workflow when its actual evidence exists.
