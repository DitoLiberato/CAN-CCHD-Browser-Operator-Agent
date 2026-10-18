# ChatGPT guide — Research Assistant Pipeline 0.1.0-pilot

[Português](CHATGPT_GUIDE_PT.md) · [Claude guide](PILOT_GUIDE_EN.md)

Use this guide to start a research project in ChatGPT, with or without an existing
idea. It uses the same method distributed for Claude: twelve phases, personalized
protocols, traceable evidence and human scientific decisions. You retain authorship.

## 1. Download the files

Open one of the links below and use GitHub's **Download raw** button, usually shown
as a downward arrow. If only the text opens, save the complete file and retain its
file extension.

| File | When to use it |
|---|---|
| [Complete ZIP package](dist/research-assistant-pipeline-0.1.0-pilot.zip) | Import into supported skill environments; Python scripts and project templates |
| [Single Markdown context file](dist/research-assistant-pipeline-0.1.0-pilot-context.md) | Manual use in ChatGPT Projects, without installing a skill |

The ZIP contains `research-assistant-pipeline/SKILL.md`, references, scripts and
templates. The context file includes the full SKILL.md instructions, all twelve
references, citation metadata and license, with source hashes; it does not contain the scripts
or project templates. Keep the ZIP as a copy of the original version. You do not need
the entire CAN-CCHD repository. Pasting a link into a chat neither proves that the
files were read nor installs a skill.

## 2. Choose how to load the method

### A. Your account supports Skills

OpenAI documents Skills and the use of `@skill-creator`. Check the interface,
permissions and availability in your own account; this guide does not assume a
universal ZIP import button.

1. Select `@skill-creator`, when available, and provide the package through an
   accepted file mechanism. If ZIP is not accepted, extract it and provide the
   folder or files through the mechanism supported by your environment.
2. Ask it to import the existing skill while preserving its rules and resources:

```text
I want to use Research Assistant Pipeline 0.1.0-pilot from these files.
Check whether this environment can import and install an existing skill.
If it can, preserve the instructions, references, scripts, templates, license,
citation and version identity. Do not replace the method with a summary or
new rules. Report any packaging adaptation required. Confirm where it was
saved, how to activate it, and which resources you could read. If installation
is unavailable, say so explicitly and help me use the Project context mode.
```

3. Confirm that the skill was saved and is available for selection or activation.
   Ask the assistant to identify its version, twelve phases and human decision
   boundaries. A confirmation without reading the resources does not prove installation.
4. Start with section 3. Installing a skill does not grant GitHub access, access
   to bibliographic databases or code execution.

### B. Your account cannot install Skills: use a Project

1. Create a **Project** in ChatGPT for your research.
2. Add `research-assistant-pipeline-0.1.0-pilot-context.md` to its sources or files.
   Confirm that the upload succeeded. If the interface does not accept Markdown,
   save an unchanged copy with a `.txt` extension and attach it.
3. Add these Project instructions:

```text
Use Research Assistant Pipeline 0.1.0-pilot from the attached context file as
the research method. Read its instructions and relevant references before
each phase. Preserve personalized protocols, traceability, human decisions,
versions and authorship. Start new projects at Phase 0. When resuming, use
the project's state, approvals and pinned snapshot; do not automatically
replace its rules. Report which files you could read and which tools are
available. Never invent execution, sources or approvals. This is manual
context use, not native skill installation.
```

4. Start a conversation within that Project using the message in section 3.

Projects keep files and instructions available across their chats. Creating one does
not by itself expose folders on your computer: supply the files or an authorized
connection. In context mode, scripts can run only when the complete package and an
execution tool are actually accessible.

## 3. Start, including without a defined idea

Copy this message and add your field of interest or question, if you have one:

```text
I want to develop a research project using Research Assistant Pipeline.
Start at Phase 0 and respond in English. I do not have a defined question yet;
help me explore my interests, resources, contribution and feasibility.
First confirm the version and which files and tools are accessible.
Ask a few useful questions at a time. Help me choose a design and construct
specific, justified and testable rules. Keep AI proposals distinct from human
decisions. Do not start formal collection or selection without my documented
approval of a concrete protocol.
```

If you already have a question, replace the sentence about not having one with your
proposal. The assistant should discuss alternatives and limitations without assuming
that meta-analysis or scientific novelty will be possible. Initial feasibility
searches are exploratory.

## 4. Create and preserve your project

With Python 3.10+ and the complete package available, the assistant can run this
from the skill folder:

```bash
python3 scripts/bootstrap_project.py /path/to/new-project --title "Working title" --language en
```

Use a new or empty destination. The generator creates local files, a pinned copy
of the skill, Phase 0 state and pending approvals. It does not create a remote
repository. Without execution, use `assets/project-template/` from the ZIP to prepare
equivalent files, record the manual mode, and retain the original tool copy. An
incomplete file set must not be presented as a validated project.

Use your own repository, private by default, or another authorized versioned storage
location. GitHub write access must be verified. With read-only access, the assistant
should prepare files and guide manual upload. Save or download the current state,
protocol, decisions, evidence and handoff files; do not rely only on chat memory or
temporary execution paths.

Do not copy the CAN-CCHD study data or history. Identifiable patient records remain
in an appropriate clinical environment; private GitHub alone is not such an
environment. Do not send passwords or access tokens in messages.

## 5. Check operation and resume

Before proceeding, check that the assistant:

- Identifies version 0.1.0-pilot and Phase 0 without assuming approvals.
- States the mode: installed skill or manual Project context.
- Helps build rules for your question, with rationales and meaningful tests.
- Reports what it can read, search, execute, save and synchronize.
- Keeps sources, AI suggestions and human decisions distinguishable.

When a generated project and Python are available, run:

```bash
python3 _pipeline/skill/scripts/validate_project.py /path/to/project
```

This checks structural consistency; it neither authenticates human decisions nor
establishes scientific validity. Without execution, record checks as manually
reviewed or not run.

In a new conversation within the same Project, provide current files and ask it to
begin with `START_HERE.md`, then check `project.json`, `CURRENT_STATE.md`,
`PIPELINE_LOCK.json`, the protocol, approvals and `handoff/LATEST.md`. Resolve
disagreements before dependent work. Tool updates require explicit migration.

## 6. Attribution, limitations and feedback

If the tool contributes substantially, cite the version using
[CITATION.cff](CITATION.cff). Separately disclose the AI used, actual tasks and human
supervision. Tool developers gain no automatic study coauthorship. No DOI has been
assigned to the pilot.

This guide adapts loading of the same method to ChatGPT. Publishing it does not
establish successful installation in your account or equivalent performance across
models. See [EVALUATION.md](EVALUATION.md). Record difficulties with version, mode,
step, observed behavior and expected outcome, without identifiable information.

Official documentation consulted on 2026-10-19; menu names may vary:

- [Skills & Plugins — OpenAI](https://learn.chatgpt.com/docs/skills-and-plugins)
- [Projects and chats — OpenAI](https://learn.chatgpt.com/docs/projects)
