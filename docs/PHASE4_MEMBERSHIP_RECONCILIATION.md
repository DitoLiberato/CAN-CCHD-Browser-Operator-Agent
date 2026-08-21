# Phase 4 normalized-membership reconciliation

Date: 2026-08-21
Status: REQUIRED BEFORE PHASE 4 CLOSURE

## Why this gate exists

The historical Phase 4 active full-text universe was created after normalization/deduplication of the 327-record raw corpus and was tracked by normalized IDs (`Nxxx`). It contained 156 active reports: 49 routed `include` and 107 routed `maybe`. Four additional maybe-routed normalized records (`N228`, `N265`, `N298`, `N299`) were not part of the active full-text-resolvable queue, and 9 records were preserved as `separate_analysis` outside the primary Phase 4 universe.

The current report-level adjudication ledger was reconstructed mainly from raw/public-corpus IDs (`Rxxx`) and later citation/regional reports. Those IDs are not guaranteed to map one-to-one to the 156 normalized Phase 4 members. Therefore the previously reported working countdown `149/156; 7 remaining` is WITHDRAWN as a formal closure metric.

## Binding rule

Phase 4 is not closed until every one of the 156 normalized active records has exactly one crosswalk row and one terminal Phase 4 status. Raw-report adjudications remain valid evidence, but they must be linked to the normalized membership set before global counts are frozen.

## Required crosswalk schema

| normalized_id | phase3_route | title/citation | raw_report_id(s) | report/cohort relation | full_text_status | phase4_decision | CAN-CCHD extraction status | notes |
|---|---|---|---|---|---|---|---|---|

## Known normalized-universe facts

- Raw corpus before normalization: 327 records.
- Phase 3 routes feeding full text: 49 `include`, 111 `maybe`, plus 9 `separate_analysis`.
- Active Phase 4 universe: 49 `include` + 107 `maybe` = 156.
- Four maybe-routed records outside the active FT-resolvable queue: `N228`, `N265`, `N298`, `N299`.
- The 9 `separate_analysis` records remain outside the primary 156.

## Current reconciliation state

- The Rxxx tranche files and master ledger contain extensive full-text adjudications and remain authoritative at the report level.
- All raw public-corpus IDs R001-R145 have effectively been reviewed or represented in tranche/ledger work, but R001-R145 is NOT equivalent to the normalized Phase 4 membership set.
- Several former no-ID reports were subsequently assigned raw IDs (examples: Garg 2013 = R086; Kochilas/Minnesota = R087; Singh & Chen 2022 = R101; Gaonkar 2024 = R104; Jain 2022 = R105; Eltahlawi 2025 = R106; Murni 2022 = R109; Hu 2016 = R118). This demonstrates why report-level counting can double-count unless the Nxxx crosswalk is used.
- Known non-PubMed/unresolved citations such as Zayachnikova (reported N=20,547 in a secondary review), Chen/Hainan, Gamhewage and Donia/Tolba must not be assumed to belong to the 156 until normalized membership is verified.

## Closure procedure

1. Recover or reconstruct the 156-row normalized Phase 4 membership list (`Nxxx`).
2. Map each Nxxx record to zero/one/multiple Rxxx/raw reports and citation identity.
3. Collapse raw duplicate/companion reports without losing report-level provenance.
4. Carry forward the already completed full-text adjudication from the Rxxx ledger when identity is verified.
5. Adjudicate only genuinely unmatched Nxxx members.
6. Recompute terminal counts from the 156 Nxxx rows only.
7. Freeze Phase 4 and then create the structured extraction dataset for quantitative synthesis.

## Audit note

No `156/156` claim should be made from the current Rxxx report count alone. This amendment supersedes prior chat/master-ledger countdown language without invalidating the individual study adjudications already completed.