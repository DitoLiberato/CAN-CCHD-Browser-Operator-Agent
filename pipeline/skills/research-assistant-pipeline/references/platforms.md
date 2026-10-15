# Host capabilities and GitHub

Check capabilities in the current environment. A skill supplies instructions/resources;
it does not grant web access, subscriptions, filesystem persistence, execution or
GitHub write permissions. Never ask for pasted passwords/tokens in chat or commit them.

## Operating modes

| Capability | With access | Without access |
|---|---|---|
| Web/source retrieval | Search/read permitted sources and preserve evidence | Prepare source-specific queries; request exports and record unexecuted work |
| Files | Create/read a persistent project | Return a complete checkpoint for the user to save; state persistence is manual |
| Python | Run bootstrap and structural validator | Create/review the same templates manually; state checks were not executed |
| GitHub read | Load actual files/ref before resume | Have user supply the current project files/snapshot |
| GitHub write | Commit/push approved safe project files to verified destination | Prepare files and guide manual upload or CLI use |

Do not confuse a reading connector with a writing connector. Verify actual tool scope.
Never claim syncing until a remote read confirms the expected files/revision.

## Claude

Distribute the `research-assistant-pipeline/` directory in a ZIP containing that one
top-level directory, with `SKILL.md` directly inside it and all referenced resources.
Current official guidance describes Customize → Skills → Create skill → Upload a
skill, with code execution/file creation enabled. Check the current UI/help if this
differs; do not assume a particular subscription or organization policy.

Claude Code can load the directory under `.claude/skills/` (project) or
`~/.claude/skills/` (personal). Other Agent Skills-compatible clients have their own
installation paths. For unsupported hosts, load the instructions and bundled files
as project context, clearly labeling this as manual rather than native activation.

Official references checked 2026-10-15:
- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://agentskills.io/specification

## Researcher's own repository

Bootstrap an empty project locally; verify it contains no study data copied from the
tool's repository. Establish owner/name and prefer private visibility. With an
authorized GitHub write tool or CLI, create an empty repository then push the generated
project. Otherwise guide the user through GitHub's New repository and upload process.
Use credentials through the host's normal secure authorization, not project files.

Do not suggest “Use this template” unless the source actually is a clean, designated
template repository. The CAN-CCHD repository is a study repository and must not be
cloned wholesale into a colleague's research project. This pilot's bootstrap is the
template mechanism; no GitHub template flag is required.

If using git locally: initialize the generated directory, inspect tracked paths,
stage the generated safe files, commit and push to the verified private remote.
Before later commits inspect changes, especially clinical sources and licensed PDFs.
The project's `_pipeline/skill/` snapshot pins its instructions. Updates are explicit
migrations with impact review, not automatic pulls from a moving branch.
