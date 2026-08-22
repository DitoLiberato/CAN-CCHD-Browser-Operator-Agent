# CAN-CCHD Phase 11 — Safe Resume Snapshot — Dedicated Writing Split

Date: 2026-08-22  
Hub branch: `phase11-writing`  
Status: **SAFE RESUME — ABSTRACT AND MANUSCRIPT MOVED TO DEDICATED CHAT STREAMS**

## Frozen scientific state

Phase 6 is analysis-complete and remains frozen on `phase6-analysis`.

Primary scientific input remains `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv`, blob SHA `1dff5eb2475ab588de2a0a76d53d2176f0d3cd35`.

Primary set remains 28 independent PRIMARY_POOLABLE units, denominator 1,999, Strict events 638 and Expanded events 1,015. No scientific database amendment occurred during Phase 11 setup.

## Writing split

Phase 11 is no longer one shared drafting stream.

Dedicated streams:

- SHA abstract chat/branch: `phase11-sha-abstract`
- full manuscript chat/branch: `phase11-manuscript`

Parent/hub: `phase11-writing`.

Canonical split rules:

`docs/PHASE11_WRITING_SPLIT_HANDOFF_2026-08-22.md`

Dedicated handoffs:

- `docs/PHASE11_HANDOFF_SHA_ABSTRACT_CHAT.md`
- `docs/PHASE11_HANDOFF_MANUSCRIPT_CHAT.md`

## Abstract stream state

Existing starting draft:

`docs/PHASE11_SHA_ABSTRACT_DRAFT_v0.1.md`

Status: `draft_requires_human_review`.

Current body count: 248 words by repository whitespace count. Last-checked SHA constraints: English, <=40-word title, <=300-word structured abstract with Introduction/Methodology/Results/Conclusion, published deadline 31 August 2026. Portal requirements must be rechecked before submission.

## Manuscript stream state

No full manuscript prose is frozen yet. The manuscript stream should begin directly from:

`docs/PHASE6_MANUSCRIPT_READY_RESULTS_PACKAGE.md`

Recommended build order:

1. Results;
2. Methods;
3. Introduction;
4. Discussion/limitations;
5. PRISMA and study characteristics;
6. tables/figures/supplement;
7. complete journal-neutral manuscript;
8. journal selection/adaptation;
9. cross-document consistency audit against the SHA abstract.

## Shared interpretation lock

Strict median-study 17.0% is not a universal patient-level rate and must be contextualized by marginal mean 33.8%, tau 3.369 and the very wide prediction interval.

Expanded median-study 69.4% represents broader clinically relevant alternative disease and must not be described as documented management actionability.

Etiologic outcomes can overlap. Timing did not demonstrate a clear group effect but no equivalence claim is allowed. Setting/altitude meta-regression was infeasible. Reporting bias cannot be ruled out statistically and no funnel-derived adjusted estimate is promoted.

## New-chat routing

If the task is the SHA abstract, switch to `phase11-sha-abstract` and read `docs/PHASE11_HANDOFF_SHA_ABSTRACT_CHAT.md` first.

If the task is the full article, switch to `phase11-manuscript` and read `docs/PHASE11_HANDOFF_MANUSCRIPT_CHAT.md` first.

Do not draft both deliverables in the same dedicated chat by default.

## One-line handoff

**Phase 11 is split safely: use `phase11-sha-abstract` for the SHA abstract and `phase11-manuscript` for the full paper. Both inherit the same frozen Phase 6 science; the hub `phase11-writing` preserves routing and shared guardrails.**
