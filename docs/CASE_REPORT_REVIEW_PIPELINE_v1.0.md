# Case Report + Systematic Review of Reported Cases — Pipeline v1.0

**Frozen:** 2026-09-03  
**Branch:** `case-report-01`  
**Status:** **BINDING WORKFLOW ARCHITECTURE**

## Core principles inherited from the parent repository

1. Protocol before prose.
2. Source-of-truth before interpretation.
3. AI may assist with mechanical, reversible, auditable tasks; scientific adjudication remains human-controlled.
4. Every important datum and claim requires provenance.
5. Missing/unknown information remains missing/unknown.
6. Independent evidence streams remain firewalled until verification.
7. Corpus/data are frozen before synthesis.
8. Writing cannot silently repair science.
9. QA precedes conclusions.
10. Novelty is tested, not presumed.
11. Journal-specific adaptation occurs only after a journal-neutral scientific manuscript is stable.

## Two-stream architecture

### CASE STREAM
Represents what actually happened to the index patient, based on primary clinical documentation.

### LITERATURE STREAM
Represents what has actually been published, based on reproducible search, screening, full-text review, extraction and appraisal.

### Firewall
Literature may inform later interpretation but cannot rewrite historical case facts. Case features may motivate searches but cannot determine which literature findings are accepted.

The streams meet only after **Phase 7 — Dual Freeze**.

## Public-repository privacy firewall

The parent repository is public. Until explicit privacy/consent clearance:

- no source PDF with PHI;
- no direct identifiers;
- no detailed rare-case abstraction that could reasonably re-identify the patient;
- use a local/private `CASE_CORE` built from the repository template;
- public branch stores methodology and review artifacts only.

---

# Phase 0 — Case–Review Protocol Lock

Define before formal searching:

- clinical teaching question;
- provisional novelty hypothesis;
- review question;
- review design;
- inclusion/exclusion criteria;
- comparator axes;
- search sources/concepts;
- reporting standards;
- consent/ethics/privacy status;
- amendment rules;
- intended publication endpoint.

Default reporting standards:

- CARE for the index case;
- PRISMA 2020 if the review is retained as systematic;
- appropriate case-report/case-series appraisal framework (default JBI tools) for published reported cases/series.

High-risk claims such as `first`, `unique`, and strong causal attribution are prohibited before evidence adjudication.

**Gate 0:** physician-approved protocol.

---

# Phase 0.5 — Case Source-of-Truth Reconstruction

Build a private/de-identified `CASE_CORE` from primary clinical sources.

Required domains:

- baseline/demographics needed scientifically;
- relevant congenital/acquired diagnoses;
- chronology;
- objective physiology/examinations;
- imaging/laboratory findings;
- differential diagnoses;
- interventions;
- planned versus completed procedures;
- response after each intervention;
- complications;
- discharge/follow-up/outcomes.

Every important event must distinguish:

- observed fact;
- contemporaneous clinician interpretation;
- later author interpretation;
- unknown/uncertain.

A planned procedure is not an outcome.

**Gate 0.5:** case chronology coherent, contradictions resolved/flagged, and intended publication endpoint judged sufficiently mature.

---

# Phase 1 — Search Calibration + Initial Collection

Build high-recall search families around:

- the core anatomic/diagnostic association;
- historical terminology/spelling variants;
- broader sensitivity concepts;
- relevant syndromic/contextual features;
- diagnostic presentation;
- management and intervention sequencing;
- key physiologic manifestations.

Minimum reproducible public core:

- PubMed/MEDLINE;
- Europe PMC;
- citation-metadata support such as Crossref/OpenAlex.

Supplementary:

- Google Scholar;
- backward citation chasing;
- forward citation chasing;
- regional databases where useful;
- Embase/Scopus/Web of Science if accessible.

No-free-PDF is never an exclusion criterion.

Known precedent papers identified during the preliminary probe become **sentinel recall records**. Failure to retrieve them blocks search closure until repaired/explained.

**Gate 1:** documented query strings, dates, counts, provenance, and acceptable sentinel recall.

---

# Phase 1.5 — Publication / Novelty Viability Gate

Assess before labor-intensive processing:

- clinical teaching value;
- direct prior precedent;
- rarity of the relevant presentation/management problem;
- completeness of case documentation;
- presence of meaningful intervention/outcome information;
- feasibility of an enumerable reported-case corpus;
- likely journal-format fit.

Allowed decisions:

- continue;
- continue_with_caution;
- revise_novelty_claim;
- narrow_review_question;
- broaden_management_context;
- convert_to_shorter_format;
- stop_or_archive.

Prior publication of the same anatomic association does not automatically invalidate a case; contribution may lie in presentation, diagnostic reasoning, physiology, management sequence, procedure choice, or outcome.

**Gate 1.5:** human decision recorded.

---

# Phase 2 — Normalization + Deduplication

Preserve raw metadata and source provenance. Exact identifier duplicates may be resolved mechanically; fuzzy matches require human review. Resolve linked publications describing the same patient/cohort.

**Gate 2:** duplicate/identity groups resolved or accepted with note.

---

# Phase 3 — Sensitive Title/Abstract Screening

Use INCLUDE / MAYBE / EXCLUDE with high recall.

Primary-set candidates are reports/series satisfying the locked association criteria.

Secondary evidence roles may include:

- broader-anatomy analog;
- syndrome/context evidence;
- management analog;
- mechanistic support;
- diagnostic context;
- surgical/procedural context;
- background only.

If key subtype or management details are unclear, use MAYBE and retrieve full text.

**Gate 3:** every unique record screened.

---

# Phase 4 — Full-Text Retrieval + Citation Saturation

Retrieve all INCLUDE/MAYBE primary candidates and chase backward/forward citations.

Rules:

- lack of free access is not exclusion;
- retrieval attempts logged;
- old/obscure reports remain eligible;
- continue citation waves until a saturation audit finds no new potentially eligible primary cases or a human closes the search with justification.

**Gate 4:** terminal retrieval status for every candidate + saturation audit complete/closed.

---

# Phase 5 — Final Evidence Corpus Adjudication

Primary statuses:

- DIRECT_ANALOG_CASE;
- DIRECT_ANALOG_CASE_SERIES;
- PARTIAL_ANALOG_CASE;
- EXCLUDE_PRIMARY_SET with reason.

Secondary roles:

- BROADER_ANALOG;
- SYNDROME_CONTEXT;
- MANAGEMENT_ANALOG;
- MECHANISTIC_SUPPORT;
- DIAGNOSTIC_CONTEXT;
- SURGICAL_CONTEXT;
- BACKGROUND_ONLY.

Publication count must not be treated as patient count when multiple reports describe the same patient/cohort.

**Gate 5:** every retrieved candidate has a terminal role and report-to-patient identity is resolved.

---

# Phase 6 — Structured Literature Extraction + Appraisal

For direct reported cases/series, extract when available:

- report/patient identity surrogate;
- age/sex;
- syndromic status;
- core anatomy/severity;
- associated anatomy;
- presenting symptoms;
- diagnostic timing and method;
- major physiologic manifestations;
- interventions;
- **sequence of interventions**;
- authors' stated rationale;
- response after each stage;
- complications;
- final outcome;
- follow-up;
- authors' main teaching claim.

Every important field requires source location and human verification before synthesis.

Use an appropriate case-report/case-series appraisal checklist. Do not invent a numeric risk-of-bias score unless the chosen framework explicitly supports one.

Published cases are a selected literature, not a denominator. Do not infer prevalence, incidence, or probability from reported-case counts.

**Gate 6:** required extraction/appraisal complete or missingness explicit.

---

# Phase 7 — Dual Verification and Freeze

Freeze two separate scientific artifacts:

1. `CASE_CORE_v1.0` — verified index-case facts (kept private until privacy clearance);
2. `REVIEW_CORPUS_v1.0` — verified literature corpus/extraction.

After freeze:

- new/corrected case facts require `CASE_AMENDMENT`;
- corpus/extraction corrections require `REVIEW_CORPUS_AMENDMENT`.

Writing may improve wording and interpretation but cannot silently alter either source of truth.

**Gate 7:** both streams frozen or frozen-with-note.

---

# Phase 8 — Case-to-Literature Comparative Mapping

Build a structured matrix comparing the index case with direct analogs across pre-specified axes such as:

- age/size;
- syndrome/context;
- presentation;
- physiology/severity;
- associated anatomy;
- diagnostic delay/misattribution;
- treatment sequence;
- palliation/definitive intervention;
- response;
- complications;
- follow-up/outcome.

Label manuscript-level ideas as:

- DOCUMENTED_PRECEDENT;
- INDEX_CASE_OBSERVATION;
- BIOLOGICAL_PLAUSIBILITY;
- AUTHOR_INTERPRETATION;
- UNRESOLVED.

**Gate 8:** comparative matrix complete and principal similarities/differences documented.

---

# Phase 9 — Scientific / CARE / PRISMA / Claims QA Sentinel

Block synthesis for unresolved high/critical findings.

Case QA:

- privacy/de-identification;
- consent/ethics status;
- CARE completeness;
- timeline consistency;
- planned vs performed distinction;
- follow-up completeness;
- diagnostic uncertainty preserved.

Review QA:

- reproducible search log;
- sentinel recall;
- duplicate/overlap resolution;
- full-text terminal status;
- citation saturation;
- PRISMA counts if systematic label retained;
- extraction verification;
- appraisal completeness;
- no population-frequency inference from reported cases.

Claims QA blocks:

- unsupported `first`/`unique` language;
- citation mismatch;
- central claim relying on secondary source when primary source is available;
- causal language exceeding evidence;
- missing information written as negative;
- planned treatment written as completed;
- single-intervention attribution despite unresolved co-interventions/confounding;
- review called systematic without meeting the locked process.

**Gate 9:** passed or all high/critical findings resolved/accepted with note.

---

# Phase 10 — Comparative Synthesis + Novelty Adjudication

Create a manuscript-ready synthesis package with:

- principal clinical lesson;
- exact defensible novelty statement;
- what was already known;
- what the index case adds;
- closest published analogs;
- similarities/differences;
- diagnostic implications;
- management/sequencing implications;
- mechanistic interpretation;
- alternative explanations/confounding;
- evidence strength;
- case limitations;
- review limitations/reporting bias;
- restrained conclusion.

Novelty is adjudicated here, not presumed in the title/introduction.

**Gate 10:** synthesis package accepted by physician.

---

# Phase 11 — Journal-Neutral Manuscript + Adversarial Review

Recommended build order:

1. Case Presentation + CARE timeline;
2. Review Methods;
3. Review Findings + comparative table;
4. Discussion;
5. Introduction;
6. Conclusion;
7. Abstract last.

Before journal adaptation, run an adversarial review asking:

1. Does the narrative match the frozen Case Core?
2. Does each central literature claim match the frozen Review Corpus?
3. Is novelty overstated?
4. Is causal language overstated?
5. Are alternative explanations treated fairly?
6. Are privacy/consent/reporting requirements satisfied?

Then perform claim-by-claim citation audit.

Only after scientific stabilization should current target-journal instructions be checked and formatting/word-count/figure adaptation performed.

## Freeze statement

This document freezes the **workflow architecture**, not the case conclusions, search results, review corpus, or novelty claim. Changes to phase order, firewalls, verification requirements, or blocking QA rules require an explicit pipeline amendment.
