# Research project — start here

Read in order:
1. `project.json` and `CURRENT_STATE.md`.
2. `PIPELINE_LOCK.json` and `_pipeline/skill/SKILL.md`.
3. `protocol/PROTOCOL.md`, `protocol/RULES.csv` and `protocol/EXECUTION_PLAN.md`.
4. `audit/approvals.jsonl`, `audit/amendments.jsonl` and `qa/findings.json`.
5. `handoff/LATEST.md` and the evidence needed for the next action.

This is the researcher's own project. Empty templates and generated scaffolding are
not approved science. Start at Phase 0, including idea exploration if needed. Follow
the pinned skill. Preserve clinical privacy and original evidence. Keep AI suggestions
separate from human-accepted scientific decisions/data.

Run `python3 _pipeline/skill/scripts/validate_project.py .` for structural checks.
Read the findings and inspect the evidence; a structural pass is not scientific validation.

## GitHub setup

Create an empty repository in the researcher's own account, private by default.
Inspect generated files, initialize git if needed and push only safe project files.
Verify the remote owner/name/visibility and successful remote persistence. If the
assistant cannot write to GitHub, it must say so and guide manual setup. Do not copy
the CAN-CCHD study database or history into this project.

## Citation

If the pipeline materially contributes to this research, cite the exact version in
`_pipeline/skill/CITATION.cff`, describe actual AI assistance and document human
responsibility. The tool license covers the bundled tool, not your original research.
