# Case Report 01 — Handoff

**Branch:** `case-report-01`  
**Last updated:** 2026-09-03  
**Status:** **Pipeline v1.0 frozen; Phase 0 locked; Phase 0.5 private Case Core in progress; Phase 1 search calibration in progress.**

## Read first

1. `CURRENT_STATE.md`
2. `docs/CASE_REPORT_REVIEW_PIPELINE_v1.0.md`
3. `docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`
4. `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.1.md`
5. `docs/PHASE0_05_PROGRESS_SNAPSHOT_2026-09-03.md`
6. `docs/PROJECT_DECISION_RECORD_v0.2.md`
7. `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.1.csv`
8. `case/CASE_CORE_TEMPLATE.md`

## Scientific architecture

Two independent streams remain firewalled until Phase 7:

- **CASE STREAM** — verified facts of the index case from primary clinical sources;
- **LITERATURE STREAM** — verified published evidence from reproducible search and review.

Literature cannot rewrite historical case facts. Case features may motivate search sensitivity analyses but cannot determine which published evidence is accepted.

## Phase 0 — CLOSED

The physician approved the protocol and the locked source is:

`docs/PHASE0_CASE_REVIEW_PROTOCOL_v1.0_LOCKED.md`

Article design:

> **Case report with an embedded systematic review of reported cases.**

Direct primary-set definition:

> unique published human patients with coexisting Tetralogy of Fallot and Morgagni diaphragmatic hernia.

Trisomy 21 remains a comparison/modifier axis, not an inclusion criterion.

The publication endpoint is deliberately locked to:

> **the full staged clinical course through definitive correction of the diaphragmatic lesion and cardiac defect, with an initial postoperative/early follow-up endpoint.**

The project may prepare the literature review, extraction, figures and most manuscript sections in advance, but the final Case Core/conclusion/submission must wait for the definitive surgical course. An earlier bridge-only endpoint would require an explicit protocol amendment.

## Phase 0.5 — PRIVATE / IN PROGRESS

A de-identified private artifact exists outside GitHub:

`CASE_CORE_PRIVATE_v0.1.md`

It records source provenance, factual chronology, intervention status, early response, imaging inventory, fact-vs-interpretation boundaries and missing-source requirements.

The detailed Case Core remains intentionally off-repository because the GitHub repository is public.

Priority private sources as they become available:

- full catheterization report and measurements;
- technical balloon/procedural details;
- ward/discharge summary;
- outpatient course and growth;
- recurrence/non-recurrence of major hypoxemic events;
- definitive diaphragmatic and cardiac operative notes;
- early postoperative outcome;
- guardian publication consent and institutional ethics/IRB determination.

## Phase 1 — ACTIVE

Initial calibration is recorded in:

`docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.1.md`

Initial direct candidate registry:

`review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.1.csv`

### Current direct candidates

1. Eurorad 2006 — `Bilateral Morgagni Hernias` — Down syndrome + TOF; prior modified BT shunt and later definitive TOF repair.
2. Kumar et al. 2015 — Ann Thorac Surg — PMID 25639421 — TOF + Morgagni + Down syndrome.
3. Aironi et al. 2015 — J Card Surg — PMID 25976041 — TOF + Morgagni.
4. Venugopal et al. 2016 — Chirurgia — direct TOF + Morgagni case with reported successful surgical outcome.

This is not yet a frozen corpus.

### Sentinel recall

Provisionally PASS:

- both known PubMed-indexed direct sentinel papers recovered;
- Eurorad direct case recovered by scholarly-web discovery;
- Venugopal/Chirurgia direct case recovered by journal/web discovery.

### Important calibration findings

- the association itself is clearly not novel;
- the direct case literature appears small and enumerable;
- broad `TOF + diaphragmatic hernia` searches recover non-Morgagni defects and require anatomy-level adjudication;
- Hatherley 1950 is a useful example: full text identifies a posterolateral defect, so it is contextual rather than a direct case;
- balloon pulmonary/RVOT palliation is established in TOF generally, including series showing immediate saturation improvement and bridge-to-repair use;
- therefore the index-case contribution, if ultimately supported, must be narrower: response-guided balloon palliation sufficient to defer stent, interaction with the diaphragmatic lesion, growth strategy, and the later definitive combined/staged course.

## Phase 1 work remaining before Gate 1 closure

1. Source-native PubMed run with exact counts/export.
2. Europe PMC run with exact counts/export.
3. PubMed/Europe PMC reconciliation.
4. OpenAlex/Crossref enrichment and citation-link recovery.
5. Supplementary scholarly-web/Google Scholar search.
6. Backward citation chase of every direct candidate.
7. Forward citation chase of every direct candidate.
8. Noise audit.
9. Eligibility/provenance decision for Eurorad as an original clinical case repository.
10. Freeze raw candidate registry for Phase 2 normalization/deduplication.

**Gate 1 remains OPEN.**

## Privacy rule

Until explicit consent/privacy clearance:

- no original patient PDF;
- no direct identifiers;
- no detailed rare-case chronology in public GitHub;
- no clinical images;
- no public Case Core.

Public branch may contain methodology, literature-review artifacts and privacy-safe state summaries.

## One-line resume prompt

**Continue Case Report 01 on `case-report-01`. Phase 0 is locked to a full staged-course endpoint. Keep the Case Core private through definitive surgery; continue Phase 1 high-recall direct-case searching, source reconciliation and citation chasing, while maintaining a separate contextual TOF-palliation corpus.**
