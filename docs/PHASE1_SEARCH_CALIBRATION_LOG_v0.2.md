# Case Report 01 — Phase 1 Search Calibration Log v0.2

**Date:** 2026-09-03  
**Branch:** `case-report-01`  
**Supersedes for current state:** `PHASE1_SEARCH_CALIBRATION_LOG_v0.1.md`  
**Status:** **IN PROGRESS — SENTINEL RECALL PASS; TERMINOLOGY/NOISE AUDIT PASS WITH EXPANSION; GATE 1 OPEN**

## 1. Search architecture

Maintain two distinct evidence streams inside the literature arm:

### A. Primary direct-analog corpus

Unique human patients with both:

- Tetralogy of Fallot; and
- Morgagni-type anterior/subcostosternal diaphragmatic hernia.

### B. Secondary contextual corpus

Includes:

- TOF + other congenital diaphragmatic hernias;
- Pentalogy of Cantrell with anatomy not yet sufficient to classify the diaphragmatic defect;
- Down syndrome + Morgagni context;
- diagnostic-delay/cardiorespiratory-confounding literature;
- TOF palliation literature: balloon pulmonary/RVOT dilation, RVOT stent, ductal stent, surgical shunt and early repair.

Context records are never counted as direct cases unless the locked direct anatomy criterion is met.

## 2. Direct search families — current calibrated forms

### Family A — modern direct terminology

```text
("tetralogy of Fallot" OR "Fallot's tetralogy" OR TOF)
AND
(Morgagni OR "Morgagni hernia" OR "Morgagni's hernia" OR "Morgagni-Larrey")
```

This recovers both known PubMed-indexed 2015 sentinel reports.

### Family B — historical/anatomic terminology

```text
("tetralogy of Fallot" OR "Fallot's tetralogy" OR TOF)
AND
(Morgagni OR Larrey OR subcostosternal OR subcosto-sternal OR retrosternal OR parasternal OR "anterior diaphragmatic hernia")
```

Purpose: recover older reports that describe the Morgagni-type defect anatomically rather than eponymously.

### Family C — broad CDH sensitivity

```text
("tetralogy of Fallot" OR "Fallot's tetralogy" OR TOF)
AND
("congenital diaphragmatic hernia" OR "diaphragmatic hernia")
```

Purpose: maximize recall. Requires full-text anatomy adjudication because it retrieves Bochdalek/posterolateral and complex CDH cases.

### Family D — Pentalogy of Cantrell sensitivity

```text
("tetralogy of Fallot" OR TOF)
AND
("pentalogy of Cantrell" OR "Cantrell syndrome")
AND
(diaphragm OR diaphragmatic OR Morgagni)
```

Purpose: recover complex anterior midline-defect cases where Morgagni terminology may appear only in full text/operative description.

### Family E — syndrome sensitivity, non-mandatory

```text
("tetralogy of Fallot" OR TOF)
AND
(Morgagni OR subcostosternal)
AND
("Down syndrome" OR trisomy 21)
```

This is a sensitivity/subgroup search only. Down syndrome remains non-mandatory for eligibility.

## 3. Direct sentinel recall

### Modern PubMed-indexed sentinels

- PMID 25639421 — Kumar et al. 2015 — PASS.
- PMID 25976041 — Aironi et al. 2015 — PASS.

### Known non-PubMed/web direct sentinels

- Eurorad 5434, Goldstein et al. 2006 — PASS.
- Venugopal et al. 2016, Chirurgia — PASS.

**Overall sentinel recall: PASS.**

## 4. New historical direct candidate from terminology expansion

Johnson EK, Mangiardi JL. `Subcostosternal diaphragmatic hernia.` Am J Surg. 1952;84(2):245-248. PMID 14952651. DOI 10.1016/0002-9610(52)90047-0.

Accessible abstract explicitly states that a **subcostosternal diaphragmatic hernia with coexisting Tetralogy of Fallot** is reported.

Independent modern/historical terminology sources establish that anteromedial subcostosternal defects are the Morgagni/foramen-of-Morgagni type.

Decision:

`DIRECT_ANALOG_CANDIDATE`, pending full-text confirmation of the defect location and case details.

This discovery materially validates the historical-terminology arm.

## 5. New recent direct candidate from Pentalogy sensitivity search

`Pentalogy on Cantrell: an unwanted surprise.` Malaysian Journal of Paediatrics and Child Health Supplementary, 2024.

Accessible full abstract explicitly reports:

- neonatal operation for a ruptured omphalocele;
- operative identification and primary repair of a **Morgagni diaphragmatic hernia**;
- postoperative echocardiographic diagnosis of **Tetralogy of Fallot**;
- subsequent recurrent desaturation;
- death in the neonatal period after a conservative-care decision.

Decision:

`DIRECT_ANALOG_CANDIDATE` under the locked original case-level report eligibility framework. Final inclusion and appraisal will be adjudicated in Phase 5/6.

This is a clinically important **hernia-first** route and broadens the management spectrum substantially.

## 6. High-value anatomy-pending management candidate

Zhu Y et al. `Surgical Repair of Tetralogy of Fallot and a Large Congenital Diaphragmatic Hernia in a 16-Week-Old Infant With Pentalogy of Cantrell and a Large Omphalocele: A Case Report.` World J Pediatr Congenit Heart Surg. Epub 2025; issue 2026. PMID 41204094. DOI 10.1177/21501351251375452.

Accessible abstract reports:

- TOF with a large congenital diaphragmatic hernia in Pentalogy of Cantrell;
- RVOT stent at 7 weeks due to hypoxia;
- temporary symptomatic improvement;
- progression;
- combined definitive repair at 16 weeks including diaphragmatic repair and major cardiac reconstruction.

The accessible abstract does **not** establish that the diaphragmatic defect is Morgagni.

Decision:

`ANATOMY_PENDING_PRIMARY_CANDIDATE` until full-text anatomy review. If non-Morgagni or not sufficiently classifiable, retain as `MANAGEMENT_ANALOG` only.

This case is especially valuable for comparing a **stent-first bridge** with the index case's response-guided balloon-only bridge.

## 7. Historical false-positive / anatomy-control case

Hatherley LI. 1950. `Congenital right diaphragmatic hernia associated with Fallot's tetralogy.` Thorax.

Full-text evidence identifies the diaphragmatic defect as posterolateral.

Decision:

- `EXCLUDE_DIRECT_SET — NON_MORGAGNI_ANATOMY`;
- retain as `HISTORICAL_DIAGNOSTIC_PHYSIOLOGY_CONTEXT`.

This remains a positive control for the anatomy-adjudication safeguard.

## 8. Provisional direct candidate count after calibration wave 2

Current raw registry contains:

- **6 records with explicit or historically equivalent Morgagni/subcostosternal signal**, pending Phase 5 final eligibility;
- **1 additional high-value anatomy-pending Pentalogy/CDH case**.

These are candidate records, not frozen unique-patient counts.

Current registry:

`review/PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.2.csv`

## 9. Management-route signal already visible

Without yet performing formal extraction, current candidates demonstrate markedly different routes, including:

- hernia detected after earlier surgical TOF palliation and later cardiac repair;
- direct published TOF–Morgagni surgical cases;
- neonatal hernia-first management with later TOF recognition;
- an anatomy-pending modern Pentalogy case using RVOT stent before definitive combined repair.

This supports the physician's intended article value:

> not a claim of a new association, but a structured comparison of **different practical routes through a rare, competing cardiorespiratory problem**.

No route is yet claimed superior.

## 10. TOF balloon-palliation contextual calibration

The contextual search confirms balloon pulmonary/RVOT dilation as an established palliation strategy in symptomatic infants with TOF.

Relevant evidence includes reports/series describing:

- acute oxygen-saturation improvement after balloon dilation;
- bridge-to-repair use;
- variable durability;
- avoidance of surgical shunt in selected infants;
- predictors of early failure;
- modern coexistence of BPV, RVOT stenting and ductal stenting as catheter-based palliation options.

Therefore:

> `balloon dilation in TOF` is not a novelty claim.

The later comparative question is whether the **response-guided decision to stop after balloon dilation and omit a planned stent**, in the setting of TOF + Morgagni and a growth-to-definitive-surgery strategy, has direct precedent.

## 11. Citation chasing — current status

### Backward/related-reference signal

- Historical subcostosternal literature confirms the terminology pathway and points to pre-1952 Morgagni literature for background, but no earlier TOF co-occurrence has yet been verified.
- Modern direct case pages/repositories repeatedly cross-reference the known 2015 direct reports and broader non-Morgagni TOF–CDH cases.

### Forward signal

- The 2015 Kumar paper has later citation activity, but current web-indexed citation pages do not yet establish additional direct TOF–Morgagni cases.
- A 2024 conference abstract provides a new direct case-level record.
- A 2025/2026 Pentalogy case provides a major management analog and awaits diaphragmatic-anatomy adjudication.

Citation chasing is **not yet saturated**.

## 12. Noise/terminology audit

Separate artifact:

`docs/PHASE1_NOISE_AND_TERMINOLOGY_AUDIT_v0.1.md`

Result:

**PASS WITH EXPANSION REQUIRED.**

Main conclusions:

- modern `Morgagni` query = high precision but historically incomplete;
- `subcostosternal` terminology = essential;
- broad CDH query = necessary but anatomically noisy;
- Pentalogy search = necessary for complex recent cases;
- syndrome terms must never become required search terms.

## 13. Source-native reproducibility status

Current browser-access route has not exposed reliable machine-readable **exact native result counts and exports** for custom PubMed and Europe PMC queries.

No count has been invented or inferred from search-engine visibility.

Therefore the formal Phase 1 gate remains open until source-native runs/counts/exports are obtained or an explicit documented alternative reproducibility method is approved.

## 14. Remaining work before Gate 1 closure

1. Obtain source-native PubMed query counts/export for modern, historical and broad sensitivity families.
2. Obtain Europe PMC query counts/export.
3. Reconcile PubMed and Europe PMC.
4. Complete OpenAlex/Crossref metadata enrichment.
5. Continue scholarly-web/Google Scholar sensitivity search.
6. Complete backward citation chase for all direct candidates, especially the 1952 report.
7. Complete forward citation chase for all direct candidates.
8. Retrieve/adjudicate full text for the anatomy-pending 2025/2026 Pentalogy case.
9. Confirm final eligibility policy implementation for conference abstract and Eurorad case repository during Phase 5.
10. Produce raw collection freeze for Phase 2 normalization/deduplication.

## Gate 1 status

**OPEN — meaningful progress; no methodological blocker beyond reproducible source-native collection/count capture.**
