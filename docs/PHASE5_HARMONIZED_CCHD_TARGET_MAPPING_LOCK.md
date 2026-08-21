# CAN-CCHD Phase 5 — Harmonized CCHD Target Mapping Lock

Date: 2026-08-21  
Original methodological decision: Phase 0.4, 2026-08-20  
Status: **BINDING RESTORATION OF PRE-SPECIFIED HARMONIZED TARGET**

## 1. Provenance

During the August 2026 restart, Phase 0.4 changed the primary denominator from each study's historical/study-defined CCHD target to a **harmonized review CCHD target**. The study-defined target was retained for historical/contextual and sensitivity analyses.

The Phase 0.4 conversation explicitly anchored the harmonized target to the definition used by:

Plana MN, Zamora J, Suresh G, Fernandez-Pineda L, Thangaratinam S, Ewer AK. *Pulse oximetry screening for critical congenital heart defects.* Cochrane Database Syst Rev. 2018;(3):CD011912. PMID 29494750; PMCID PMC6494396; DOI 10.1002/14651858.CD011912.pub2.

The exact lesion-level wording was not copied into the repository during Phase 0.4. This file restores it from that pre-specified source. This is **not a post hoc change of target definition**.

The legacy Browser Agent/database is not used for this restoration or for any lesion mapping.

## 2. Harmonized CCHD definition

The Cochrane anchor defines CCHD as:

> a potentially life-threatening duct-dependent heart lesion in which the infant either dies or requires an invasive procedure (surgery or cardiac catheterization) in the first 28 days of life.

The operational lesion rules in that review are the binding harmonized rules for this CAN-CCHD review.

## 3. Unconditional CCHD lesions

The following lesions are classified as harmonized CCHD whenever the lesion identity is adequately established, without requiring a separate report of death/intervention timing:

1. **Hypoplastic left heart syndrome (HLHS)**
2. **Pulmonary atresia with intact ventricular septum (PA/IVS)**
3. **Simple transposition of the great arteries (simple TGA)**
4. **Interrupted aortic arch (IAA)**

## 4. Conditional CCHD lesions

The following lesions are harmonized CCHD **only when the infant dies or undergoes cardiac surgery/catheterization within the first 28 days of life**:

1. **Coarctation of the aorta (CoA)**
2. **Aortic valve stenosis**
3. **Pulmonary valve stenosis**
4. **Tetralogy of Fallot (TOF)**
5. **Pulmonary atresia with ventricular septal defect (PA/VSD)**
6. **Total anomalous pulmonary venous connection/return (TAPVC/TAPVR)**

A diagnostic label such as `critical`, `severe`, `cyanotic`, `major CHD`, or the study authors' `CCHD` classification does **not** replace the required early death/intervention evidence for these conditional lesions.

## 5. Lesions not explicitly listed by the anchor

Structural lesions not explicitly listed above — including, for example, DORV, complete AVSD/CAVSD, isolated ASD, isolated VSD, PDA, truncus arteriosus, tricuspid atresia, Ebstein anomaly, single-ventricle labels, or complex combinations — must **not be automatically promoted to harmonized CCHD from the diagnostic name alone**.

For such lesions:

- preserve the raw lesion identity exactly;
- determine whether the primary report provides enough anatomy and early clinical-course information to establish equivalence to one of the binding lesion rules above;
- if equivalence cannot be established reproducibly, retain the infant in the harmonized-CCHD-negative denominator or place the denominator on `HOLD_PENDING_MAPPING` when participant-level assignment remains genuinely unresolved;
- do not use a study author's broader `critical CHD`, `major CHD`, `cyanotic CHD`, or `CHD` category as a substitute for the harmonized rule.

This conservative rule prevents denominator shrinkage from non-reproducible post hoc target expansion.

## 6. Complex lesions and combinations

For a complex lesion containing one of the named harmonized components:

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

## 8. Consequence for denominator construction

Primary denominator:

`harmonized-CCHD-negative final failed screens`

Therefore:

`harmonized denominator = final failed screens - infants meeting the locked harmonized CCHD definition`

The study-defined CCHD count may differ and must remain separately recorded.

## 9. Immediate implications for existing Phase 5 holds

### U_R018 — Özalkaya 2016
The study's six reported CCHD cases cannot be subtracted automatically from the denominator until their individual lesions and, where required, early death/intervention status are mapped under this lock.

### U_R076 — Mohsin 2019
The study's eight pulse-positive structural-CHD infants are not equivalent to eight harmonized CCHD cases.

Raw lesions already recovered include:
- TGA — unconditional only if anatomically `simple TGA`; confirm source detail;
- PA/IVS x2 — unconditional CCHD when intact ventricular septum is established;
- TOF — conditional;
- DORV/VSD — not automatically harmonized CCHD;
- ASD/CAVSD/pulmonary stenosis/PDA — pulmonary stenosis component is conditional; remaining components not automatically CCHD;
- CAVSD/DORV/pulmonary atresia — non-intact septal anatomy means pulmonary atresia follows the conditional PA/VSD-type rule;
- critical pulmonary stenosis — conditional despite the word `critical`.

Thus R076 remains `HOLD_PENDING_MAPPING` until the conditional-lesion early outcome/intervention evidence is sought.

## 10. Rule against target drift

This lesion mapping may only be changed by an explicit protocol amendment with rationale and sensitivity plan. Phase 5 extraction must not broaden or narrow the target opportunistically according to individual study terminology.
