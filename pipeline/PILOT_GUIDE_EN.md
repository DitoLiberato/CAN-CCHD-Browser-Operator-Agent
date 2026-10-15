# Claude pilot — Research Assistant Pipeline 0.1.0

Use this skill to co-design a research protocol, conduct traceable work through twelve
phases and retain human scientific decisions. You may start without a research idea.

1. Download the [skill ZIP](dist/research-assistant-pipeline-0.1.0-pilot.zip) using
   GitHub's download control. Do not upload the entire CAN-CCHD repository.
2. In Claude, enable code execution/file creation where available. Current official
   guidance describes **Customize → Skills → Create skill → Upload a skill**. Upload
   the ZIP and enable it; consult [official help](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
   if the interface or organization policy differs.
3. Ask Claude to use Research Assistant Pipeline. Explain your field, question,
   available evidence and constraints, or say you have no idea yet.
4. Review the proposed question/design and personalized protocol. Formal collection
   and screening require your actual approval; exploratory probes stay labeled.
5. Ask the skill to generate an empty project with `scripts/bootstrap_project.py`,
   or equivalent templates if execution is unavailable. Create your own private
   GitHub repository using actual authorized write tools or manual upload. The skill
   itself grants no GitHub access and the bootstrap does not create a remote.
6. Resume a new conversation from the project's `START_HERE.md`, pinned skill,
   protocol, decisions and handoff. Do not automatically update the pinned method.

Claude Code can load the directory in `.claude/skills/` or `~/.claude/skills/`.
For other hosts, verify the supported installation method and capabilities.

Keep identifiable clinical material in an appropriately authorized environment;
private GitHub is not automatically a suitable patient-record store. Do not copy
CAN-CCHD data/history into a new project. Preserve the researcher's own content and
only upload permitted, appropriately de-identified derivatives.

Please cite the tool/version when it materially contributes, using
[CITATION.cff](CITATION.cff), and disclose actual AI tasks and human supervision.
No DOI is assigned to this pilot and tool creators gain no automatic study coauthorship.

Report usability problems with version, workflow step, observed behavior and expected
outcome, without confidential data. See [EVALUATION.md](EVALUATION.md) for actual test
coverage and limitations. A structural validator pass is not scientific validation.
