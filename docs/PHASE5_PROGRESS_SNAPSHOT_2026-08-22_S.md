# CAN-CCHD Phase 5 — Progress Snapshot S

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **SAFE RESUME POINT — 76/76 STRUCTURALLY EXTRACTED / d-TGA TARGET RULE FROZEN / ALL-76 TARGET RERUN NEXT**

## 1. Structural extraction state

All 76 frozen quantitative units remain structurally extracted.

- extracted: **76/76 (100%)**
- identity queue: **0**
- unextracted queue: **0**

The provisional pre-rerun disposition inherited from Snapshot R remains:

- PRIMARY_POOLABLE: 26
- SENSITIVITY_ONLY: 42
- HOLD_PENDING_QA: 3
- NOT_POOLABLE: 5

These counts are **not final** and must not be treated as the frozen analysis pools because the harmonized target rerun has not yet been executed under the amended d-TGA rule.

## 2. Binding target-policy adjudication completed

The jointly deferred TGA question has now been resolved by formal protocol amendment.

### Primary amended rule

**Dextro-transposition of the great arteries (d-TGA) is an unconditional harmonized CCHD target lesion whether anatomically simple or complex/associated with additional cardiac lesions.**

Consequences:

- d-TGA is removed from the harmonized-CCHD-negative CAN denominator as target disease;
- associated VSD, ASD, CoA, PS, or other lesions do not negate d-TGA target status;
- no separate <=28-day death/surgery/catheterization evidence is required to establish target status through the d-TGA component;
- an infant with multiple qualifying components is counted once.

### Source terminology

- explicit d-TGA / dextro-transposition / conventional complete-transposition terminology -> unconditional target;
- explicit simple TGA -> unconditional target;
- unqualified `TGA` in neonatal CCHD/pulse-oximetry context -> map to d-TGA unless the primary source indicates congenitally corrected/l-TGA or other non-d-TGA anatomy;
- explicit congenitally corrected TGA / ccTGA / l-TGA -> not automatically promoted by this amendment.

The raw diagnostic wording remains preserved.

## 3. Why the rule changed

The former literal `simple TGA` restriction created an ontologic inconsistency: simple d-TGA could be removed as target disease while complex d-TGA could remain in the denominator and potentially be counted as a collateral actionable diagnosis.

That is incompatible with the screening estimand because d-TGA itself is a core CCHD condition targeted by neonatal pulse-oximetry screening.

The amendment was made after structural extraction reached 76/76 but before final pool freezing and before meta-analysis. It was therefore logged transparently and paired with a sensitivity plan rather than silently changing prior extraction records.

## 4. Narrow scope / no collateral target drift

This amendment changes only the d-TGA component.

It does **not** automatically promote DORV, truncus arteriosus, tricuspid atresia, Ebstein anomaly, single-ventricle labels, AVSD, VSD, PDA, congenitally corrected TGA/l-TGA, or other non-listed lesions.

All pre-existing conditional rules remain unchanged unless separately amended:

- CoA
- aortic stenosis
- pulmonary stenosis
- TOF
- PA/VSD
- TAPVC/TAPVR

These still require actual death/surgery/catheterization <=28 days under the current lock.

## 5. Sensitivity framework preserved

Because the change occurred after structural extraction, the original Cochrane-literal TGA rule is retained as a formal sensitivity framework.

Final quantitative work must preserve:

1. **Primary amended analysis:** adequately established d-TGA, simple or complex, is unconditional target disease; unqualified neonatal TGA maps to d-TGA unless corrected/l-TGA evidence is present.
2. **Sensitivity analysis:** original Cochrane-literal rule in which only explicit/adequately established simple TGA is unconditional.

Any resulting changes in denominator, numerator, poolability, or pooled estimate must be reported.

## 6. Immediate known Block 21 impact to audit

At minimum, the all-76 rerun must update/recheck:

- U_R006 Meberg 2008 — TGA x11;
- U_R008 de-Wahl Granelli 2009 — TGA x2;
- U_R013 Turska-Kmiec 2012 — TGA x3;
- U_R036 Arlettaz 2006 — TGA x2.

U_R013's separately reported congenitally corrected TGA remains outside this automatic promotion.

No final numerical replacement is frozen in this snapshot because the rule must first be applied consistently across **all 76** units rather than only the four units that triggered adjudication.

## 7. Historical records preserved

Snapshot R and Block 21 remain intentionally unchanged as pre-amendment historical records.

The new binding documents are:

- `docs/PHASE5_PROTOCOL_AMENDMENT_2026-08-22_D_TGA_TARGET_RULE.md`
- amended `docs/PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`

Snapshot S supersedes Snapshot R as the safe resume point.

## 8. Exact next movement

Do **not** begin final meta-analysis yet.

Next:

1. rerun target mapping across all 76 extracted units under the amended d-TGA rule;
2. globally search raw lesion fields for TGA/d-TGA/transposition/ccTGA/corrected TGA/l-TGA;
3. simultaneously re-audit every conditional lesion for actual <=28-day death/surgery/catheterization evidence;
4. recompute exact harmonized denominators, CAN numerators, ascertainment, and affected poolability statuses;
5. resolve the three remaining HOLD_PENDING_QA units where possible;
6. freeze final PRIMARY_POOLABLE / SENSITIVITY_ONLY / NOT_POOLABLE sets;
7. then proceed to quantitative synthesis.

## 9. Commits defining this snapshot

- d-TGA protocol amendment: `f6d60689c2aa341661be5d212db7f554cc93cacf`
- harmonized target lock integration: `c21a428b451b86257a8ba646da5f26859926583a`

The commit containing this Snapshot S is the current safe-resume head after creation.
