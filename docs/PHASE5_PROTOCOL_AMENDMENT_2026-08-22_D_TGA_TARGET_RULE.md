# CAN-CCHD Phase 5 — Protocol Amendment: d-TGA Harmonized Target Rule

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BINDING PROTOCOL AMENDMENT — BEFORE FINAL POOL FREEZE / BEFORE META-ANALYSIS**

## 1. Scope of this amendment

This amendment changes **only the transposition-of-the-great-arteries component** of the Phase 5 harmonized CCHD target mapping.

It does **not** broaden the target rules for DORV, truncus arteriosus, tricuspid atresia, Ebstein anomaly, single-ventricle labels, AVSD, VSD, PDA, or any other lesion not otherwise changed below.

The restart legacy-data firewall remains fully binding. This decision is based on methodological adjudication of the harmonized target and independent screening-framework evidence, not on legacy data or on a desire to alter study results.

## 2. Problem identified after structural extraction

The original harmonized lock imported the Cochrane 2018 wording literally and treated only `simple TGA` as an unconditional target lesion.

After all 76 frozen quantitative units had been structurally extracted, this produced an internally incoherent consequence for the CAN-CCHD estimand:

- `simple d-TGA` would be classified as harmonized target disease and removed from the CAN denominator;
- `d-TGA` with an associated VSD or other associated anatomy could remain in the harmonized-CCHD-negative denominator solely because it was not anatomically `simple`;
- the latter could then appear as a collateral actionable non-CCHD diagnosis despite being a core disease that CCHD pulse-oximetry screening is intended to detect.

That distinction is not clinically or screening-conceptually defensible for **dextro-transposition of the great arteries (d-TGA)**.

## 3. External screening-framework evidence

The original Cochrane anchor remains the provenance of the broader Phase 5 harmonized mapping framework:

Plana MN, Zamora J, Suresh G, Fernandez-Pineda L, Thangaratinam S, Ewer AK. *Pulse oximetry screening for critical congenital heart defects.* Cochrane Database Syst Rev. 2018;(3):CD011912. PMID 29494750; PMCID PMC6494396.

However, contemporary CCHD screening frameworks identify **d-Transposition of the great arteries** as a core screening condition without restricting the diagnosis to anatomically simple d-TGA:

- American Academy of Pediatrics. Oster ME et al. *Newborn Screening for Critical Congenital Heart Disease: A New Algorithm and Other Updated Recommendations.* Pediatrics. 2025;155(1):e2024069667. Table 1 lists `D-Transposition of the great arteries` among core CCHD conditions.
- US Centers for Disease Control and Prevention. *Clinical Screening and Diagnosis for Critical Congenital Heart Defects.* The CDC lists `d-Transposition of the great arteries` among CCHDs targeted by pulse-oximetry screening.

These sources support treating d-TGA itself, rather than only the anatomically simple subtype, as target disease for the screening estimand.

## 4. Amended binding rule

Effective from this amendment:

> **Dextro-transposition of the great arteries (d-TGA) is an unconditional harmonized CCHD target lesion, whether anatomically simple or associated with additional cardiac lesions.**

Therefore, when d-TGA is adequately established among final failed screens:

- it is counted once as harmonized CCHD;
- it is removed from the harmonized-CCHD-negative CAN denominator;
- associated VSD, ASD, CoA, PS, or other lesions do not negate its target status;
- no separate <=28-day death, surgery, or catheterization evidence is required to establish target status through the d-TGA component.

If another associated lesion independently meets a harmonized target rule, the infant is still counted once.

## 5. Source terminology rule

Phase 5 must preserve the raw source diagnosis exactly.

For target mapping:

- explicit `d-TGA`, `D-TGA`, `dextro-transposition`, or equivalent conventional complete transposition terminology -> **unconditional harmonized CCHD**;
- explicit `simple TGA` -> **unconditional harmonized CCHD**;
- `TGA` reported without a qualifier in a neonatal CCHD/pulse-oximetry context -> map to **d-TGA target disease unless the primary source provides evidence that the label refers to congenitally corrected/l-TGA or another non-d-TGA transposition anatomy**;
- explicit `congenitally corrected TGA`, `ccTGA`, or `l-TGA` -> **not automatically promoted by this amendment**; evaluate under the remaining harmonized rules and source-specific anatomy/course.

This rule does not require assuming that an unqualified `TGA` is anatomically `simple`; the relevant distinction is now **d-TGA versus corrected/l-TGA**, not simple versus complex d-TGA.

## 6. CAN-CCHD consequence

The CAN-CCHD estimand remains:

`harmonized-CCHD-negative final failed screens`

Accordingly, a d-TGA infant is a **target-disease detection**, not a CAN-CCHD collateral diagnosis.

Even though d-TGA is clinically highly actionable, its actionability does not place it in the CAN numerator when it meets the harmonized CCHD target. It is removed from the denominator before CAN classification.

Conceptually:

`final failed POx -> harmonized CCHD? -> yes: target detection / exclude from CAN denominator`

`final failed POx -> harmonized CCHD? -> no: classify CAN-A / CAN-B / CAN-AB / CAN-U / NON_CAN / UNKNOWN`

## 7. Impact on the previously deferred Block 21 TGA cases

This amendment resolves the simple-versus-complex TGA question prospectively for the final target audit.

At minimum, the following previously deferred unqualified `TGA` diagnoses now map as harmonized target d-TGA unless primary-source evidence indicates corrected/l-TGA:

- U_R006 Meberg 2008 — TGA x11;
- U_R008 de-Wahl Granelli 2009 — TGA x2;
- U_R013 Turska-Kmiec 2012 — TGA x3;
- U_R036 Arlettaz 2006 — TGA x2.

In U_R013, the separately reported `congenitally corrected TGA` case is **not** promoted by this amendment.

These counts are not yet a substitute for the required all-76 target rerun.

## 8. Bias-control / sensitivity plan

Because this amendment was adjudicated **after structural extraction was complete (76/76) but before final pool freezing and before quantitative synthesis**, the original Cochrane-literal mapping is retained as a prespecified sensitivity framework for the TGA component.

Final reporting must therefore preserve:

1. **Primary amended target analysis:** all adequately established d-TGA, simple or complex, is unconditional harmonized CCHD.
2. **Sensitivity analysis:** original Cochrane-literal rule in which only explicit/adequately established `simple TGA` is unconditional.

This prevents the amendment from silently altering results and permits direct assessment of whether the TGA ontology decision materially changes pooled CAN-CCHD estimates.

## 9. Required downstream actions

Before final meta-analysis:

1. rerun harmonized target mapping across **all 76** extracted units under this amended rule;
2. search all raw lesion fields for `TGA`, `d-TGA`, transposition terminology, `ccTGA`, `corrected TGA`, and `l-TGA`;
3. preserve raw wording while recording the amended mapping decision;
4. recompute harmonized-CCHD-negative denominators and any CAN counts affected by target removal;
5. re-audit conditional lesions for actual <=28-day death/surgery/catheterization evidence under the otherwise unchanged lock;
6. resolve remaining HOLD_PENDING_QA units where possible;
7. freeze final primary/sensitivity/not-poolable analysis sets;
8. only then perform quantitative synthesis.

## 10. Historical integrity

Snapshot R and Block 21 remain historical records of the state **before** this amendment and must not be rewritten to make the earlier deferred decision disappear.

A new post-amendment snapshot must supersede Snapshot R as the safe resume point.
