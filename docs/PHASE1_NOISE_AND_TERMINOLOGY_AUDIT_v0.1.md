# Case Report 01 — Phase 1 Terminology + Noise Audit v0.1

**Date:** 2026-09-03  
**Branch:** `case-report-01`  
**Status:** **CALIBRATION ARTIFACT — PHASE 1 IN PROGRESS**

## Purpose

Test whether the direct TOF–Morgagni search is sensitive to historical nomenclature while preserving the locked anatomy-level eligibility boundary.

## Finding 1 — modern-name query is high precision but incompletely sensitive

A query requiring `Morgagni` retrieves the known modern direct case reports but risks missing older reports that describe the same anatomic defect using historical language.

## Finding 2 — `subcostosternal` is a required historical synonym family

Modern review literature describes anteromedial subcostosternal diaphragmatic defects as Morgagni hernias, and older literature explicitly uses formulations such as `subcostosternal (Morgagni)` or `subcostosternal (foramen of Morgagni)`.

Therefore Phase 1 direct sensitivity searches must include:

```text
subcostosternal
subcosto-sternal
anteromedial diaphragmatic hernia
anterior subcostosternal diaphragmatic hernia
foramen of Morgagni
foramen of Larrey
Morgagni-Larrey
retrosternal / parasternal, as sensitivity terms requiring anatomic adjudication
```

These terms are search expansions, not automatic eligibility labels.

## Historical direct candidate recovered

Johnson EK, Mangiardi JL. `Subcostosternal diaphragmatic hernia.` Am J Surg. 1952;84(2):245-248. PMID 14952651. DOI 10.1016/0002-9610(52)90047-0.

The abstract explicitly states that a subcostosternal diaphragmatic hernia with coexisting Tetralogy of Fallot is reported.

Given the established historical equivalence of subcostosternal/foramen-of-Morgagni terminology, this record is promoted to **DIRECT_ANALOG_CANDIDATE**, pending full-text confirmation of the defect location/anatomy.

## Finding 3 — broad `diaphragmatic hernia + TOF` search has necessary but substantial anatomic noise

Example:

Hatherley LI. 1950. `Congenital right diaphragmatic hernia associated with Fallot's tetralogy.`

Full-text review identifies a **posterolateral** diaphragmatic defect. It is therefore excluded from the direct TOF–Morgagni set and retained only as historical/contextual evidence.

This validates the rule:

> Search broadly; adjudicate the diaphragmatic defect anatomically at full text.

## Finding 4 — Pentalogy of Cantrell creates a second terminology pathway

Pentalogy of Cantrell contains an anterior diaphragmatic defect as part of its classic spectrum. However, a paper mentioning `Pentalogy of Cantrell + TOF + diaphragmatic hernia` is **not automatically a direct Morgagni case**.

Rules:

- if the source explicitly calls the defect `Morgagni`, `subcostosternal`, or otherwise provides anatomy sufficient to establish the locked anterior Morgagni-type defect, retain as direct candidate;
- if the source only says `congenital diaphragmatic hernia`, mark `ANATOMY_PENDING` until full text;
- do not infer Morgagni solely from the syndrome label.

### 2024 explicit case-level abstract

`Pentalogy on Cantrell: an unwanted surprise` explicitly reports a Morgagni diaphragmatic hernia found at surgery and postoperative echocardiographic diagnosis of TOF. It is therefore a direct candidate despite being a conference abstract rather than a full journal case report.

### 2025/2026 management analog pending anatomy

Zhu et al. report TOF + large congenital diaphragmatic hernia in Pentalogy of Cantrell, with RVOT stenting at 7 weeks and definitive cardiac/diaphragmatic repair at 16 weeks. The accessible abstract does not establish Morgagni anatomy. Therefore it is `ANATOMY_PENDING_PRIMARY_CANDIDATE` and, at minimum, a high-value `MANAGEMENT_ANALOG`.

## Finding 5 — generic `Morgagni + TOF` web search contains lexical false positives

Potential noise sources include:

- author/institution addresses containing the word `Morgagni`;
- reviews listing TOF among many anomalies associated with Morgagni hernia without presenting an individual TOF case;
- Pentalogy of Cantrell reviews where TOF and Morgagni appear in different patients;
- veterinary reports;
- non-Morgagni congenital diaphragmatic hernia cases;
- papers about other thoracic/pericardial hernias in TOF.

Each retrieved record therefore needs case-level co-occurrence confirmation.

## Search-family amendment decision

This is **not** a Phase 0 protocol amendment because the protocol already pre-specified historical terminology and high-recall sensitivity expansion.

Phase 1 query families should now explicitly contain a historical-anatomy arm:

```text
("tetralogy of Fallot" OR "Fallot's tetralogy" OR TOF)
AND
(Morgagni OR Larrey OR subcostosternal OR subcosto-sternal OR retrosternal OR parasternal OR "anterior diaphragmatic hernia")
```

and a Pentalogy sensitivity arm:

```text
("tetralogy of Fallot" OR TOF)
AND
("pentalogy of Cantrell" OR "Cantrell syndrome")
AND
(diaphragm OR diaphragmatic OR Morgagni)
```

Neither arm changes the final direct-set eligibility rule.

## Noise audit conclusion

**PASS WITH EXPANSION REQUIRED.**

- Modern-name query: good precision, insufficient historical sensitivity alone.
- Broad CDH query: adequate sensitivity, high anatomy-level noise.
- Historical subcostosternal terminology: essential.
- Pentalogy pathway: essential for recent/complex management cases, but anatomy must be verified.

Gate 1 remains open pending source-native collection, citation chasing and reconciliation.
