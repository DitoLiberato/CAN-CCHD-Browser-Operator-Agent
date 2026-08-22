# CAN-CCHD-Browser-Operator-Agent

An AI autonomous research assistant for the CAN-CCHD systematic review and meta-analysis.

## START HERE — mandatory for new chats and agents

**Before reviewing this repository, read [`CURRENT_STATE.md`](CURRENT_STATE.md).**

`CURRENT_STATE.md` is the stable navigation entry point for the project. It tells a new chat or agent:

- which branch contains the current scientific work;
- which snapshot is the current safe-resume point;
- which artifacts supersede older extraction blocks and snapshots;
- the current frozen study/pool counts;
- the exact next scientific movement;
- which legacy files must not be used as evidence.

Do **not** infer the current project state from the default branch, the highest-numbered block, file modification dates, old snapshots, or the legacy database/app.

### Current pointer

As of 2026-08-22:

- scientific branch: `phase5-extraction`;
- Phase 5: **FROZEN**;
- canonical safe-resume point: **Snapshot T**;
- Snapshot T commit: `9293bd461998c74f883289b0661bb5f91d53f297`;
- final pool membership: **28 PRIMARY_POOLABLE / 40 SENSITIVITY_ONLY / 3 HOLD_PENDING_QA / 5 NOT_POOLABLE**;
- next movement: construct and QA the canonical 28-row primary analysis dataset, then begin quantitative synthesis.

For all details and artifact precedence, read **`CURRENT_STATE.md` first**.
