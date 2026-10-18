# Research Assistant Pipeline — 0.1.0-pilot

A portable Agent Skill for **human-led, protocol-governed research assistance**.
Developed by Rodrigo Liberato de Oliveira from the CAN-CCHD workflow, with AI-assisted
implementation. The skill helps a researcher's own AI co-design personalized rules,
execute authorized work, verify evidence and retain human scientific decisions.

**Claude:** [Português](PILOT_GUIDE_PT.md) · [English](PILOT_GUIDE_EN.md)

**ChatGPT:** [Português](CHATGPT_GUIDE_PT.md) · [English](CHATGPT_GUIDE_EN.md)

## What this is

- A reusable scientific-integrity core and twelve process phases, numbered 0–11.
- A co-design process for study-specific questions, eligibility, searches, extraction,
  mapping, synthesis and meaningful acceptance tests.
- A self-contained skill, project bootstrap and structural validator.
- Human decision records, immutable source provenance, controlled amendments and
  project-local version pinning for continuity between conversations.
- Citation and actual AI-use documentation, with no automatic tool-creator coauthorship.

The starting scope includes case reports, original case series, published-case
synthesis, focused/narrative/scoping/systematic reviews and appropriate meta-analysis.
These are methodological entry points, not prevalidated recipes. A researcher may
start without an idea. PRISMA supports reporting; the project must select suitable
conduct, appraisal and other guidance separately.

## Repository separation

This directory contains the general tool. The rest of this repository includes the
historical CAN-CCHD study/app and active scientific branches. **Do not use this whole
repository as a template or fork for a colleague's new research.**

The bootstrap creates an empty, independent project with a pinned copy of the skill.
The researcher can push that project to their own private GitHub repository. The
bootstrap neither creates a remote repository nor uploads data or grants approvals.

Original identifiable patient sources must stay in an appropriately approved data
environment. A private GitHub repository is not automatically a clinical-data store.

## Structure

- `skills/research-assistant-pipeline/`: self-contained skill and project templates.
- `dist/`: full skill ZIP, manual project-context export and checksums.
- `build_distribution.py`: reproducible packaging from the skill source.
- `build_chatgpt_context.py`: one-file export of the same instructions/references
  for manual Project context, without native installation or bundled execution tools.
- `tests/`: synthetic integrity scenarios.
- `EVALUATION.md`: scope and results of actual checks, including limitations.
- `CITATION.cff`, `LICENSE`: attribution metadata and license for this tool only.

## Build and check

Python 3.10+; bootstrap and structural checks use the standard library.

```bash
python3 pipeline/build_distribution.py
python3 pipeline/build_chatgpt_context.py
python3 -m unittest discover -s pipeline/tests -v
python3 pipeline/skills/research-assistant-pipeline/scripts/bootstrap_project.py ../my-research --title "My research" --language en
python3 pipeline/skills/research-assistant-pipeline/scripts/validate_project.py ../my-research
```

The validator checks recorded integrity, not scientific validity or the authenticity
of human decisions. The assistant and researcher must inspect the actual evidence.
No universal meta-analysis script is shipped; project-specific analyses require
appropriate methods, execution and testing.

The ChatGPT guides distinguish native skill environments from manual Project context.
Account capabilities and import mechanisms must be checked; no universal ZIP import
or equivalent performance across hosts is assumed. The context export is derived
from the unchanged skill payload and does not represent a completed external user trial.

## Attribution and reuse

If the tool materially contributes to research, please cite its exact version using
[CITATION.cff](CITATION.cff), describe actual AI use and human supervision, and retain
the software license notice. The pilot has no DOI or peer-reviewed methods article.
The [MIT license](LICENSE) applies only to files under `pipeline/` (and the identical
skill distribution). It does not relicense the CAN-CCHD study, third-party materials,
patient records or a user's original research. Academic citation is requested as a
separate scholarly attribution policy.

## Pilot status

Read [EVALUATION.md](EVALUATION.md) before describing validation. Simulated assistant
exercises and script tests do not constitute a completed Claude field trial or
validation of every design. The external Claude pilot remains the next user test.
