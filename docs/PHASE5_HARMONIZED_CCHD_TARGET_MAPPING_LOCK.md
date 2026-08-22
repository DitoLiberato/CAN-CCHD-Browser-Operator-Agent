# CAN-CCHD Phase 5 — Harmonized CCHD Target Mapping Lock

Date: 2026-08-21  
Original methodological decision: Phase 0.4, 2026-08-20  
Amended: 2026-08-22 — d-TGA target ontology  
Status: **BINDING HARMONIZED TARGET — WITH FORMAL d-TGA AMENDMENT**

## 1. Provenance

During the August 2026 restart, Phase 0.4 changed the primary denominator from each study's historical/study-defined CCHD target to a **harmonized review CCHD target**. The study-defined target was retained for historical/contextual and sensitivity analyses.

The Phase 0.4 conversation explicitly anchored the harmonized target to the definition used by:

Plana MN, Zamora J, Suresh G, Fernandez-Pineda L, Thangaratinam S, Ewer AK. *Pulse oximetry screening for critical congenital heart defects.* Cochrane Database Syst Rev. 2018;(3):CD011912. PMID 29494750; PMCID PMC6494396; DOI 10.1002/14651858.CD011912.pub2.

The exact lesion-level wording was not copied into the repository during Phase 0.4. This file restored it from that pre-specified source.

On 2026-08-22, after structural extraction of all 76 frozen quantitative units but before final pool freezing or meta-analysis, the TGA component was formally amended. The reason was an ontologic inconsistency created by restricting target disease to `simple TGA`: anatomically complex d-TGA could otherwise remain in the harmonized-CCHD-negative denominator and be counted as a collateral actionable diagnosis despite d-TGA itself being a core CCHD screening target.

The amendment is documented in:

`docs/PHASE5_PROTOCOL_AMENDMENT_2026-08-22_D_TGA_TARGET_RULE.md`

The amendment is deliberately narrow: it changes the d-TGA rule only. All other lesion rules remain as specified below unless separately amended.

The legacy Browser Agent/database is not used for this restoration, amendment, or lesion mapping.

## 2. Harmonized CCHD definition

The Cochrane anchor defines CCHD as:

> a potentially life-threatening duct-dependent heart lesion in which the infant either dies or requires an invasive procedure (surgery or cardiac catheterization) in the first 28 days of life.

The operational lesion rules from that review remain the basis of the harmonized rules, with the explicit d-TGA amendment in Sections 3, 5, and 6.

## 3. Unconditional CCHD lesions

The following lesions are classified as harmonized CCHD whenever the lesion identity is adequately established, without requiring a separate report of death/intervention timing:

1. **Hypoplastic left heart syndrome (HLHS)**
2. **Pulmonary atresia with intact ventricular septum (PA/IVS)**
3. **Dextro-transposition of the great arteries (d-TGA), whether anatomically simple or complex/associated with additional cardiac lesions**
4. **Interrupted aortic arch (IAA)**

### Binding d-TGA terminology rule

For target mapping:

- explicit `d-TGA`, `D-TGA`, `dextro-transposition`, or equivalent conventional complete-transposition terminology -> unconditional harmonized CCHD;
- explicit `simple TGA` -> unconditional harmonized CCHD;
- unqualified `TGA` in a neonatal CCHD/pulse-oximetry report -> map to d-TGA target disease unless the primary source provides evidence that the label refers to congenitally corrected/l-TGA or another non-d-TGA transposition anatomy;
- explicit `congenitally corrected TGA`, `ccTGA`, or `l-TGA` -> not automatically promoted by this d-TGA rule.

The raw source wording must always be preserved. An unqualified `TGA` does **not** need to be assumed anatomically `simple`; the relevant target distinction is d-TGA versus corrected/l-TGA.

## 4. Conditional CCHD lesions

The following lesions are harmonized CCHD **only when the infant dies or undergoes cardiac surgery/catheterization within the first 28 days of life**:

1. **Coarctation of the aorta (CoA)**
2. **Aortic valve stenosis**
3. **Pulmonary valve stenosis**
4. **Tetralogy of Fallot (TOF)**
5. **Pulmonary atresia with ventricular septal defect (PA/VSD)**
6. **Total anomalous pulmonary venous connection/return (TAPVC/TAPVR)**

A diagnostic label such as `critical`, `severe`, `cyanotic`, `major CHD`, or the study authors' `CCHD` classification does **not** replace the required early death/intervention evidence for these conditional lesions.

## 5. Lesions not explicitly listed by the anchor or amendment

Structural lesions not explicitly listed above — including, for example, DORV, complete AVSD/CAVSD, isolated ASD, isolated VSD, PDA, truncus arteriosus, tricuspid atresia, Ebstein anomaly, single-ventricle labels, congenitally corrected TGA/l-TGA, or complex combinations that do not contain an independently qualifying component — must **not be automatically promoted to harmonized CCHD from the diagnostic name alone**.

For such lesions:

- preserve the raw lesion identity exactly;
- determine whether the primary report provides enough anatomy and early clinical-course information to establish equivalence to one of the binding lesion rules above;
- if equivalence cannot be established reproducibly, retain the infant in the harmonized-CCHD-negative denominator or place the denominator on `HOLD_PENDING_MAPPING` when participant-level assignment remains genuinely unresolved;
- do not use a study author's broader `critical CHD`, `major CHD`, `cyanotic CHD`, or `CHD` category as a substitute for the harmonized rule.

This conservative rule prevents denominator shrinkage from non-reproducible post hoc target expansion.

The 2026-08-22 amendment does **not** automatically promote other non-listed lesions merely because contemporary screening frameworks may classify them as core CCHD conditions. Any further target broadening would require a separate explicit amendment.

## 6. Complex lesions and combinations

For a complex lesion containing one of the named harmonized components:

- **d-TGA retains unconditional harmonized CCHD status whether anatomically simple or accompanied by VSD, ASD, CoA, pulmonary stenosis, or other associated lesions.** No separate <=28-day event is required to establish target status through the d-TGA component.
- **PA/IVS** retains unconditional CCHD status when an intact ventricular septum is established.
- **PA with a VSD or other non-intact septal anatomy** follows the conditional PA/VSD rule and therefore requires death or invasive cardiac intervention within 28 days.
- **Pulmonary valve stenosis**, including a source label `critical pulmonary stenosis`, follows the conditional pulmonary-valve-stenosis rule unless early death/intervention within 28 days is documented.
- **TAPVR/TAPVC** follows the conditional rule even if the source calls it CCHD.
- **TOF** follows the conditional rule even if the source calls it CCHD.

When an infant has multiple lesions, a single qualifying harmonized component is sufficient to classify the infant as CCHD; the infant is counted once.

## 7. Required Phase 5 evidence fields for conditional lesions

For every conditional lesion, Phase 5 must seek and record:

- lesion identity;
- surgery within 28 days: yes/no/unknown;
- catheter intervention within 28 days: yes/no/unknown;
- death within 28 days attributable to the lesion: yes/no/unknown;
- source location/evidence;
- final harmonized CCHD classification.

If timing is not reported, do not infer it merely because the lesion is severe or because intervention would commonly be expected clinically.

The d-TGA amendment is not a waiver for the timing requirement of an associated conditional lesion when that conditional lesion is being evaluated independently. It simply means that once d-TGA itself is adequately established, the infant already qualifies as target CCHD.

## 8. Consequence for denominator construction

Primary denominator:

`harmonized-CCHD-negative final failed screens`

Therefore:

`harmonized denominator = final failed screens - infants meeting the locked harmonized CCHD definition`

The study-defined CCHD count may differ and must remain separately recorded.

A d-TGA case meeting Section 3 is a **target-disease detection** and is removed from the CAN denominator before CAN classification. Its clinical actionability does not make it a CAN-CCHD collateral diagnosis.

## 9. Immediate implications for existing Phase 5 mappings

### TGA mappings

Previously deferred unqualified `TGA` diagnoses must now be re-audited under Section 3 across all 76 extracted units. At minimum this includes:

- U_R006 Meberg 2008 — TGA x11;
- U_R008 de-Wahl Granelli 2009 — TGA x2;
- U_R013 Turska-Kmiec 2012 — TGA x3;
- U_R036 Arlettaz 2006 — TGA x2.

In U_R013, the separately reported `congenitally corrected TGA` case is not automatically promoted by this amendment.

These examples do not replace the required all-76 rerun.

### U_R018 — Özalkaya 2016

The study's six reported CCHD cases cannot be subtracted automatically from the denominator until their individual lesions and, where required, early death/intervention status are mapped under this lock.

### U_R076 — Mohsin 2019

The study's eight pulse-positive structural-CHD infants are not equivalent to eight harmonized CCHD cases.

Raw lesions already recovered include:
- TGA — now unconditional target disease when the source supports d-TGA/unqualified neonatal TGA and does not indicate corrected/l-TGA;
- PA/IVS x2 — unconditional CCHD when intact ventricular septum is established;
- TOF — conditional;
- DORV/VSD — not automatically harmonized CCHD;
- ASD/CAVSD/pulmonary stenosis/PDA — pulmonary stenosis component is conditional; remaining components not automatically CCHD;
- CAVSD/DORV/pulmonary atresia — non-intact septal anatomy means pulmonary atresia follows the conditional PA/VSD-type rule;
- critical pulmonary stenosis — conditional despite the word `critical`.

Thus R076 still requires conditional-lesion early outcome/intervention evidence for lesions not already qualifying through an unconditional component.

## 10. Sensitivity analysis for the d-TGA amendment

Because the d-TGA ontology was amended after completion of structural extraction but before final pool freezing and meta-analysis, the original Cochrane-literal TGA rule must be retained as a sensitivity framework.

Final quantitative work must therefore preserve both:

1. **Primary amended mapping:** adequately established d-TGA, simple or complex, is unconditional harmonized CCHD; unqualified neonatal `TGA` maps to d-TGA unless corrected/l-TGA evidence is present.
2. **Sensitivity mapping:** original Cochrane-literal rule in which only explicit or adequately established `simple TGA` is unconditional.

The difference between these mappings must be reported if it changes any unit denominator, numerator, poolability status, or pooled estimate.

## 11. Rule against target drift

This lesion mapping may only be changed by an explicit protocol amendment with rationale and sensitivity plan. Phase 5 extraction must not broaden or narrow the target opportunistically according to individual study terminology.

The 2026-08-22 d-TGA amendment satisfies this rule and is formally logged in `PHASE5_PROTOCOL_AMENDMENT_2026-08-22_D_TGA_TARGET_RULE.md`.

No further target changes should be made implicitly during the all-76 rerun.
