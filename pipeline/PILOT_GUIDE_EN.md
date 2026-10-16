# Claude pilot guide — Research Assistant Pipeline 0.1.0-pilot

This skill helps you and your AI turn an idea into a personalized research protocol,
develop your project through twelve phases, and preserve sources, human decisions
and scientific authorship. You can start without a defined research question.

The skill and its methodological references are written in English. The assistant
can work in your preferred language; no separate English skill package is needed.

## 1. Install the skill

1. Open the [pilot package](dist/research-assistant-pipeline-0.1.0-pilot.zip) and use
   GitHub's download button to save the ZIP.
2. In Claude, enable code execution and file creation where available.
3. The installation guidance is **Customize → Skills → Create skill → Upload a skill**.
   Upload the entire ZIP and enable the skill. If your interface differs, consult
   the [official help](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
4. In Claude Code, the skill folder can also be installed under `.claude/skills/`
   in your project or `~/.claude/skills/` for your local account.

The ZIP contains one `research-assistant-pipeline/` folder, with `SKILL.md` and its
supporting resources inside. Do not upload a ZIP of the entire CAN-CCHD repository
as a skill.

## 2. Get started

Ask Claude to use **Research Assistant Pipeline** and describe your field of interest,
a question, or a case that motivated the project. Say if you do not have an idea yet.
The assistant should explore the question, available resources and feasibility
before proposing a study design.

It will help develop a protocol with rationales, methodological sources, operational
rules, completion criteria and decisions requiring your judgment. Review and approve
the protocol before formal data collection or study selection begins. Early
exploratory searches must be clearly identified as exploratory.

## 3. Create your own project

The skill includes a tool that creates an empty research project. If Claude can
execute Python:

```bash
python3 scripts/bootstrap_project.py /path/to/new-project --title "Working title" --language en
```

Run this command from the skill folder, using a new or empty destination. Claude can
locate the skill folder in its environment. Without code execution, the assistant
can prepare equivalent files and state which checks were not run. The command creates
local project files; it does not create a remote GitHub repository or grant scientific
approval.

Then create a repository **in your own GitHub account**, private by default. With
authorized write tools, the assistant can help create it and upload your project.
With read-only access, it should prepare the files and guide you through a manual
upload. Installing the skill does not grant GitHub access. Do not paste passwords
or access tokens into messages.

The CAN-CCHD repository **is not an empty project template**. Use the generated project
without copying the original study, results, database or history. Identifiable clinical
documents must remain in an appropriately authorized environment; a private GitHub
repository is not automatically suitable for patient records.

## 4. Resume in a new conversation

Provide the current repository or project files and ask the assistant to begin with
`START_HERE.md`. It should check the protocol, decisions, project state and the pinned
skill version. Work should resume from the saved files without depending on chat memory.

If a new tool version becomes available, migration requires an explicit decision and
an assessment of its effects. Do not automatically change the rules during a study.

## 5. Attribution and publication

If the pipeline contributes substantially to your research, please cite it using
[CITATION.cff](CITATION.cff), including the version used. Your article should also
describe which AI was used, its actual tasks, and how the researchers reviewed the
work and made decisions. Using the skill does not make its developers coauthors of
your study. No DOI has been assigned to this pilot.

## 6. What to assess during the pilot

- Does the AI help formulate a feasible question without imposing a study design?
- Do the proposed rules fit your objectives and include a rationale?
- Does it distinguish AI suggestions from actual human decisions?
- Does it preserve sources, uncertainty and versions?
- Can a new conversation recover the correct project state?
- Does it accurately report limitations of tools, searches and verification?

Record the version, the step where a problem occurred, the observed behavior and the
expected outcome. Share only examples without identifiable or confidential information.
See [EVALUATION.md](EVALUATION.md) for the scope and limitations of the tests performed.
A structural validation pass does not establish scientific validity, and the external
Claude user pilot has not yet been completed.
