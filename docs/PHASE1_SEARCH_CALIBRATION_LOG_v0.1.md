# Case Report 01 — Phase 1 Search Calibration Log v0.1

**Date:** 2026-09-03  
**Branch:** `case-report-01`  
**Status:** **IN PROGRESS — INITIAL CALIBRATION / SENTINEL RECALL PASSED PROVISIONALLY**

## Purpose

Phase 1 has two deliberately separate search targets:

1. **PRIMARY DIRECT-ANALOG CORPUS** — published human cases with Tetralogy of Fallot (TOF) and Morgagni diaphragmatic hernia in the same patient.
2. **SECONDARY CONTEXT CORPUS** — literature relevant to diagnostic delay/respiratory confounding, Down syndrome–Morgagni context, and TOF palliation strategies such as balloon pulmonary/RVOT dilation, RVOT stenting, ductal stenting and surgical shunts.

The two corpora must not be mixed when counting direct cases.

## Search access note

This initial calibration used live web/PubMed-indexed discovery and OpenAlex metadata. Source-native automated result counts were not consistently exposed through the current browser-access route; therefore **Gate 1 is not yet closed**. Formal source-native query counts and reproducible exports remain required before Phase 1 closure.

## Query family A — direct association, high precision

Calibrated concept:

```text
("tetralogy of Fallot" OR "Fallot's tetralogy" OR TOF)
AND
(Morgagni OR "Morgagni hernia" OR "Morgagni's hernia" OR "Morgagni-Larrey")
```

Title/abstract-focused PubMed form to be used in source-native run:

```text
("tetralogy of Fallot"[Title/Abstract] OR "Fallot's tetralogy"[Title/Abstract] OR TOF[Title/Abstract])
AND
(Morgagni[Title/Abstract] OR "Morgagni hernia"[Title/Abstract] OR "Morgagni's hernia"[Title/Abstract] OR "Morgagni-Larrey"[Title/Abstract])
```

Initial PubMed-indexed direct records recovered:

- Kumar CJ et al. 2015 — `Tetralogy of Fallot with concomitant Morgagni hernia in Down syndrome: the value of routine chest roentgenogram.` Ann Thorac Surg. PMID 25639421. DOI 10.1016/j.athoracsur.2014.09.071.
- Aironi B et al. 2015 — `Tetralogy of Fallot with Morgagni's Hernia.` J Card Surg. PMID 25976041. DOI 10.1111/jocs.12574.

**Sentinel recall status:** PASS for both known PubMed-indexed direct sentinels.

## Query family B — direct association, broad sensitivity

Planned source-native form:

```text
("Tetralogy of Fallot"[Mesh] OR "tetralogy of Fallot"[All Fields] OR "Fallot's tetralogy"[All Fields])
AND
("Hernias, Diaphragmatic, Congenital"[Mesh] OR "diaphragmatic hernia"[All Fields] OR Morgagni[All Fields] OR retrosternal[All Fields] OR parasternal[All Fields])
```

Purpose:

- detect older reports that do not use modern `Morgagni` terminology in title/abstract;
- detect indexing-only records;
- identify false-positive broader congenital diaphragmatic hernia reports for later adjudication.

Known calibration example:

- Hatherley LI. 1950 — `Congenital right diaphragmatic hernia associated with Fallot's tetralogy.` Thorax. PMID 15431216. Full text confirms a **posterolateral** diaphragmatic defect, so this is **NOT a direct Morgagni case**. Retain only as historical/contextual evidence about diagnostic and physiologic overlap.

This example demonstrates why `diaphragmatic hernia + TOF` cannot be used as the direct-corpus definition without full-text anatomic adjudication.

## Query family C — direct-case web/citation discovery

General scholarly web variants used:

```text
"tetralogy of Fallot" "Morgagni hernia"
"Morgagni's hernia" tetralogy Fallot
"Morgagni hernia" "Fallot's tetralogy"
"Morgagni-Larrey" tetralogy Fallot
```

Additional direct candidates recovered outside the two PubMed-indexed sentinels:

### Candidate D3 — Eurorad 2006

`Bilateral Morgagni Hernias.` Goldstein M, Braid J, Bakalinova D. Eurorad case 5434, published 2006.

Initial public case description supports:

- male child;
- Down syndrome;
- TOF;
- recurrent respiratory infections;
- prior modified Blalock-Taussig shunt;
- later definitive TOF repair;
- subsequent imaging demonstrating bilateral Morgagni hernias.

Status: **DIRECT_ANALOG_CANDIDATE — full case extraction required.**

### Candidate D4 — Venugopal et al. 2016

`Tetralogy of Fallot with Morgagni diaphragmatic hernia: a rare case report with successful surgical outcome.` Chirurgia. 2016;29(4):133-135.

Initial journal page confirms original human case report with the direct association and successful surgical outcome.

Status: **DIRECT_ANALOG_CANDIDATE — full-text retrieval/extraction required.**

## Provisional direct-case candidate registry after initial calibration

1. Eurorad 2006 — Goldstein/Braid/Bakalinova — bilateral Morgagni + TOF + Down syndrome.
2. Kumar et al. 2015 — Ann Thorac Surg — TOF + Morgagni + Down syndrome.
3. Aironi et al. 2015 — J Card Surg — TOF + Morgagni.
4. Venugopal et al. 2016 — Chirurgia — TOF + Morgagni.

**Important:** this is a calibration registry, not the frozen review corpus. Citation chasing and source-native searches may identify additional older/obscure cases.

## Query family D — syndrome/diagnostic context

Calibrated variants:

```text
Morgagni hernia Down syndrome respiratory distress
Morgagni hernia Down syndrome delayed diagnosis
Morgagni hernia congenital heart disease Down syndrome
```

Key contextual records identified:

- Parmar RC et al. 2001. `Morgagni hernia with Down syndrome: a rare association -- case report and review of literature.` PMID 11832621. The index case had normal echocardiography, so it is not a direct TOF case; useful for Down–Morgagni respiratory presentation and historical literature mining.
- Jetley NK et al. 2011. `Down's syndrome as a factor in the diagnosis, management, and outcome in patients of Morgagni hernia.` J Pediatr Surg. Directly relevant to delayed diagnosis/context.
- Al-Salem AH et al. 2014. `Congenital Morgagni's hernia: a national multicenter study.` PMID 24726101. Pediatric Morgagni series with frequent congenital heart disease and Down syndrome; contextual only unless individual TOF cases become extractable.
- AlFraih Y et al. 2025. `Pediatric Morgagni hernia: A 10 year single center experience.` PMID 41224344. Contemporary pediatric management context.

## Query family E — TOF balloon palliation / response-guided bridge

Calibrated variants:

```text
"tetralogy of Fallot" "balloon pulmonary valvuloplasty" palliation infant
"tetralogy of Fallot" "balloon dilation" RVOT palliation
"tetralogy of Fallot" transcatheter palliation RVOT stent balloon
```

Key contextual records recovered:

- `Balloon dilation of the right ventricular outflow tract in tetralogy of Fallot: a palliative procedure.` PMID 10323533 — immediate saturation improvement reported; contextual palliation evidence.
- `Palliative balloon pulmonary valvuloplasty in tetralogy of fallot: echocardiographic predictors of successful outcome.` PMID 10973368 — documents transient vs sustained success and anatomic predictors.
- `Balloon valvuloplasty as an initial palliation in the treatment of newborns and young infants with severely symptomatic tetralogy of Fallot.` PMID 16254424 — identifies cases avoiding subsequent palliative shunt and cases with short-lived effect.
- `Balloon pulmonary valvotomy as interim palliation for symptomatic young infants with tetralogy of Fallot.` PMID 20300231 — 17 infants; mean saturation increase from approximately 73% to 90%; contextual evidence for bridge-to-repair and PA growth.
- `Early palliative balloon pulmonary valvuloplasty in neonates and young infants with tetralogy of Fallot.` PMID 31302722 — contemporary BPV series.
- `Catheter-based palliation for infants with tetralogy of Fallot.` PMID 32772997 — includes BPV, RVOT stenting and ductal stenting in a modern cohort.
- `Palliation Strategy to Achieve Complete Repair in Symptomatic Neonates with Tetralogy of Fallot.` PMID 35381860 — multicenter comparison including balloon pulmonary valvuloplasty and RVOT stent within RVOT-intervention strategies.
- `Transcatheter Approaches to Palliation for Tetralogy of Fallot.` PMID 35835516 — contemporary review noting RVOT/PDA stenting as generally more durable than BPV, while BPV remains a recognized catheter-based palliation.
- `Palliative Balloon Pulmonary Valvotomy in Tetralogy of Fallot: Is There a Role in 2021?` — focused review concluding BPV retains selected indications, especially when valvar obstruction predominates.

Interpretive rule:

These records establish that balloon-only palliation is **not novel in TOF generally**. The literature question is narrower: whether this strategy has been reported in a TOF–Morgagni patient, and how its use compares with other staged routes in the direct analog corpus.

## Query family F — broader TOF + congenital diaphragmatic hernia management analogs

Calibrated variants:

```text
"tetralogy of Fallot" "congenital diaphragmatic hernia" management
"tetralogy of Fallot" diaphragmatic hernia staged repair
"tetralogy of Fallot" diaphragmatic hernia palliation
```

Contextual analogs identified include:

- Shin HJ et al. 2012. TOF + congenital diaphragmatic hernia + left lung hypoplasia, with attention to pulmonary vascular growth after hernia repair. PMID 21920056.
- Arora Y et al. 2020. TOF + congenital diaphragmatic hernia + right lung aplasia. PMID 33061171.
- Other rare TOF–CDH reports identified by citation discovery remain contextual unless the defect is verified as Morgagni.

## Preliminary calibration conclusions

1. The direct TOF–Morgagni literature appears small enough to support a systematic review of reported cases.
2. The same anatomic association is already clearly published; novelty must not rest on coexistence alone.
3. At least two direct prior cases include Down syndrome.
4. One direct candidate documents a route with surgical palliation followed by later definitive TOF repair before the Morgagni hernia was fully recognized, making intervention sequencing a potentially rich comparison axis.
5. Balloon pulmonary/RVOT dilation is an established TOF palliation strategy; therefore any contribution of the index case lies in **patient selection, response-guided decision not to stent, interaction with the Morgagni lesion, and the subsequent staged/combined course**, not in balloon palliation per se.
6. Broad `TOF + diaphragmatic hernia` searches are necessary for sensitivity but produce anatomically non-Morgagni cases and require full-text adjudication.

## Sentinel registry v0.1

### Direct sentinels

- S-D1: PMID 25639421 — PASS.
- S-D2: PMID 25976041 — PASS.
- S-D3: Eurorad 5434 — PASS via scholarly web discovery.
- S-D4: Venugopal et al. 2016 Chirurgia — PASS via journal/web discovery.

### Context sentinels

- S-C1: PMID 15431216 — PASS, correctly identified as non-Morgagni posterolateral CDH.
- S-C2: PMID 20300231 — PASS for BPV palliation context.
- S-C3: PMID 35835516 — PASS for modern transcatheter palliation context.

## Phase 1 remaining work before Gate 1 closure

1. Run and log source-native PubMed searches with exact hit counts/export.
2. Run and log Europe PMC searches with exact hit counts/export.
3. Reconcile PubMed/Europe PMC records.
4. Use OpenAlex/Crossref to enrich metadata and identify citation links.
5. Run supplementary scholarly-web/Google Scholar queries and record screening boundary.
6. Backward-citation chase all four current direct candidates, especially older references.
7. Forward-citation chase all direct candidates.
8. Determine whether Eurorad 2006 should be treated as an eligible original clinical report under the locked high-quality clinical repository clause.
9. Produce `PHASE1_RAW_DIRECT_CANDIDATE_REGISTRY_v0.1.csv` or equivalent structured registry.
10. Complete a noise audit and confirm that the direct-query family is sufficiently sensitive without relying on syndrome terms.

## Gate 1 status

**IN PROGRESS.**

Sentinel recall is provisionally satisfactory, but formal source-native counts/exports and citation reconciliation remain outstanding.
