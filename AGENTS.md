# Repository routing

For new researchers, reusable methods, the portable skill or the Claude pilot, read
`START_RESEARCH_PROJECT.md` and `pipeline/README.md`. Work within `pipeline/` for the
general tool. Keep tests/fixtures free of actual patient data and study outcomes.

For CAN-CCHD scientific work, read `CURRENT_STATE.md` and follow its designated
branch. Do not use legacy app/database artifacts as current scientific evidence.

Do not turn this whole repository into a new user's research template. Use the
bootstrap under `pipeline/skills/research-assistant-pipeline/scripts/`.

Rebuild `pipeline/dist/` and rerun relevant tests after changing the skill. Inspect
the archive and verify all bundled references. Test results must distinguish recorded
structural integrity from scientific validation and real Claude testing.
Regenerate the manual context export with `pipeline/build_chatgpt_context.py` when
the workflow payload changes. Keep the ChatGPT guides clear about native installation
versus manual Project context; never claim account access or unperformed field tests.

The license under `pipeline/` applies to that tool, not all historical repository content.
