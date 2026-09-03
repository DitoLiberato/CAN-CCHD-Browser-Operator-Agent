# Case Report 01 — Phase 1 Scientific Search Closeout v1.0

**Date:** 2026-09-03  
**Branch:** `case-report-01`  
**Scientific discovery status:** **CLOSED AT SATURATION**  
**Formal Phase 1 workflow gate:** **OPEN — source-native count/export reproducibility backfill only**

## Canonical Phase 1 search artifacts

1. `docs/PHASE1_SEARCH_CALIBRATION_LOG_v0.2.md` — calibrated query families and sentinel logic.
2. `docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md` — terminology/noise decisions.
3. `docs/PHASE1_SATURATION_AUDIT_v1.0.md` — terminal saturation adjudication.
4. `review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.3_SATURATION.csv` — raw candidate/signal registry at saturation.

Earlier registries remain provenance history and are superseded for current scientific state by v0.3.

## Search stopping decision

Active discovery expansion is stopped because the literature search has reached a defensible plateau across independent pathways:

- modern direct terminology;
- historical/subcostosternal terminology;
- broad congenital diaphragmatic hernia sensitivity;
- Pentalogy of Cantrell/anterior-midline sensitivity;
- hidden-case mining in Morgagni series;
- adult/repaired-TOF searches;
- multilingual modern-term searches;
- recent/grey literature;
- backward citation chasing;
- forward citation chasing;
- large-series anomaly mining;
- final exact/semantic plateau checks.

Late independent waves no longer yielded new individually extractable direct patients.

## Raw direct landscape at saturation

The raw registry contains eight individually identifiable direct candidate records/patient-level reports:

1. Johnson & Mangiardi 1952 — historical subcostosternal/Morgagni-equivalent terminology + TOF.
2. Sönmez et al. 2006 — TOF patient hidden inside a Morgagni case series.
3. Goldstein et al. 2006 — bilateral Morgagni + TOF in a clinical case repository.
4. Rao et al. 2014 — adult with repaired TOF + large Morgagni; competing-physiology/conservative route.
5. Kumar et al. 2015 — TOF + Morgagni + Down syndrome.
6. Aironi et al. 2015 — TOF + Morgagni.
7. Venugopal et al. 2016 — TOF + Morgagni with reported surgical outcome.
8. Veejeyahshegarun et al. 2024 — Pentalogy of Cantrell abstract with operative Morgagni repair and TOF.

In addition, Ortiz et al. 2025 reports **two TOF patients among 55 children with Morgagni hernia**, but currently without individually mappable clinical data in the accessible report. These two remain an aggregate direct signal and are not silently converted into two patient-level extractions.

Other series signals remain unresolved or contextual and are preserved in the saturation registry without inflating the direct count.

## Important newly recovered Phase 1 cases/signals

The initial title-driven direct registry materially underestimated the literature.

The most important late recoveries were:

- **Sönmez et al. 2006**, found only by mining a Morgagni case-series table;
- **Rao et al. 2014**, an adult repaired-TOF case useful for competing-physiology reasoning;
- **Ortiz et al. 2025**, with two aggregate TOF patients hidden in a 55-patient Morgagni series.

These findings validate the decision to continue Phase 1 beyond easy exact-title hits.

## Scientific framing after saturation

The literature supports the article's intended educational value:

> a rare combined anatomy can lead to substantially different diagnostic and management routes depending on age, physiology, associated disease, timing of recognition and response to palliation.

The article should not claim novelty of the association.

No management route is currently considered superior.

The direct and contextual literature together provide examples of cardiac-first, hernia-first, combined/staged, conservative and device-bridge approaches.

The broader TOF literature establishes balloon pulmonary/RVOT palliation as a recognized strategy. The direct TOF–Morgagni saturation search did not identify a patient-level report clearly matching the narrower pattern of balloon dilation producing sufficient immediate response for a planned RVOT stent to be intentionally omitted. This remains a provisional novelty signal to be tested during full-text extraction and Phase 10 comparative adjudication.

## What is intentionally NOT concluded in Phase 1

Phase 1 does not establish:

- a final number of unique published patients;
- final direct eligibility;
- report-to-patient independence;
- comparative efficacy of management strategies;
- prevalence/incidence of TOF–Morgagni association;
- superiority of balloon dilation, RVOT stenting, surgical shunt, hernia-first or combined repair;
- novelty of the index case.

Those questions belong to later deduplication, eligibility, extraction, comparative mapping and novelty adjudication phases.

## Outstanding reproducibility task

Formal Gate 1 remains technically open because exact source-native PubMed and Europe PMC custom-query counts/exports have not yet been captured through the available access route.

This should be treated as a **bounded documentation backfill**, not a reason to restart scientific discovery.

Required before full Gate 1 closure:

1. run the locked calibrated PubMed families natively and preserve exact counts/export;
2. run the locked calibrated Europe PMC families natively and preserve exact counts/export;
3. reconcile those exports against the saturated registry;
4. freeze the Phase 1 raw collection for Phase 2.

## One-line closeout

**Phase 1 scientific discovery is closed at saturation; do not broaden searching further without a new evidence signal or protocol amendment. Complete only the native PubMed/Europe PMC reproducibility backfill, reconcile, and freeze the raw collection before Phase 2.**
