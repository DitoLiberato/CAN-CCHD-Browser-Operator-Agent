# CAN-CCHD Phase 5 — Progress Snapshot B

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT**

## Current Phase 5 state

Phase 5 continues exclusively from the 76 frozen unique quantitative units created at Phase 4.5 closure. No scientific value is imported from the legacy Browser Agent/database.

## Completed structured extraction

Eleven units have been structurally extracted:

- U_R009
- U_R017
- U_R018
- U_R019
- U_R024
- U_R025
- U_R071
- U_R072
- U_R076
- U_R089
- U_R093

## Current QA disposition

### PRIMARY_POOLABLE = 10

- U_R009
- U_R017
- U_R018
- U_R019
- U_R024
- U_R025
- U_R071
- U_R072
- U_R089
- U_R093

### SENSITIVITY_ONLY = 1

- U_R076 Mohsin 2019

### Unresolved holds among extracted units = 0

Mohsin is no longer a blocker.

## Mohsin terminal resolution

Primary article:
Mohsin M, Humayun KN, Atiq M. Cureus. 2019;11(6):e4808. PMID 31403007; PMCID PMC6682379.

Key facts:
- 1,650 newborns;
- mixed Well Baby Unit + NICU population, not separable;
- 16 final pulse-positive infants;
- study target = CHD broadly;
- 8 structural CHD;
- 8 study-defined non-CHD false positives = PPHN 6 + congenital pneumonia 2.

Raw structural lesions recovered:
- TGA;
- PA/IVS x2;
- TOF;
- DORV/VSD;
- ASD/CAVSD/pulmonary stenosis/PDA;
- CAVSD/DORV/pulmonary atresia;
- critical pulmonary stenosis.

Using the locked harmonized CCHD target:
- definite CCHD = PA/IVS x2;
- conditional/uncertain lesions lack the required 28-day death/intervention information;
- harmonized CCHD-negative denominator is therefore bounded from 9 to 14 rather than point-identifiable.

CAN-CCHD consequence:
- no specific treatment/escalation/disposition/follow-up consequence is reported for the alternative diagnoses;
- Strict CAN-CCHD = 0% across all admissible denominator mappings;
- Expanded CAN-CCHD = 100% across all admissible denominator mappings;
- exact meta-analysis weight cannot be assigned.

Independent primary-pooling exclusion:
- mixed Well Baby Unit + NICU outcomes are not separable.

Terminal status:
- `SENSITIVITY_ONLY`
- `QA_COMPLETE_SENSITIVITY_ONLY`
- no primary meta-analysis weight
- no remaining hold.

Canonical Mohsin resolution:
- `docs/PHASE5_R076_MOHSIN_RESOLUTION.md`

## Current counts

- Frozen Phase 5 units: **76**
- Structurally extracted: **11/76**
- QA-complete primary-poolable: **10**
- Sensitivity-only: **1**
- Unresolved holds among extracted units: **0**
- Not yet structurally extracted: **65**

## Exact next step

Proceed directly to the next Phase 5 extraction block. The preferred strategy is to continue with diagnostically complete units first, applying prospectively:

1. locked harmonized CCHD target mapping;
2. final-failed-screen denominator rule;
3. Strict versus Expanded CAN-CCHD distinction;
4. >=90% ascertainment rule;
5. well-baby versus mixed/NICU population flag;
6. no diagnosis-as-actionability inference.

This snapshot supersedes Snapshot A as the current safe resume point.
