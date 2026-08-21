# CAN-CCHD Phase 5 — Progress Snapshot A

Date: 2026-08-21  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT**

## Phase 5 entry state

Phase 5 begins exclusively from the **76 frozen unique quantitative units** created at Phase 4.5 closure. No scientific value is imported from the legacy Browser Agent/database.

## Infrastructure completed

- Phase 5 branch created from Phase 4.5 closure commit `a64b9048aa45bf45ead575b1d658d13f507b3408`.
- Structured extraction schema created.
- 76-row frozen extraction matrix initialized.
- Restart Protocol Core v1.0 decisions reconstructed into the repository.
- Aggregate `NON_CAN` interpretation clarified for the v0.1 matrix.
- Exact harmonized CCHD lesion mapping restored from the pre-specified Phase 0.4 Cochrane 2018 anchor.

Key files:
- `docs/PHASE5_EXTRACTION_SCHEMA_AND_CODING_RULES.md`
- `data/phase5/PHASE5_STRUCTURED_EXTRACTION_MATRIX_v0.1.csv`
- `docs/PROTOCOL_CORE_v1.0_RESTART_LOCK_RECONSTRUCTED.md`
- `docs/PHASE5_SCHEMA_CLARIFICATION_01_NONCAN_FIELD.md`
- `docs/PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`

## Structured extraction completed so far

Eleven units have been structurally extracted in Blocks 01–03:

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

## Current quantitative QA status

### QA-complete / PRIMARY_POOLABLE = 10

- U_R009 — Strict 0/40; Expanded 28/40; healthy 12/40.
- U_R017 — Strict 13/13.
- U_R018 — Strict 0/1; PFO = NON_CAN. Harmonized CCHD denominator validated by the pre-specified Cochrane target extraction (TP=6, FP=1).
- U_R019 — Strict 1/1.
- U_R024 — Strict 0/13; Expanded 10/13; transitional/NON_CAN 3/13. Generic `managed as per standard guidelines` is insufficient for Strict actionability and therefore maps to CAN-U.
- U_R025 — Strict 1/3; explicitly healthy 2/3.
- U_R071 — Strict 2/2; both early-onset sepsis/respiratory-distress infants required NICU admission because of the screen.
- U_R072 — Strict 0/33; Expanded 10/33; aggregate NON_CAN 23/33. `Significant non-CCHD disease` without a specific documented management consequence maps to CAN-U rather than Strict.
- U_R089 — Strict 0/1; Expanded 1/1; PPHN without documented actionability consequence = CAN-U.
- U_R093 — Strict 2/2; both respiratory-illness infants admitted to neonatal unit.

### Extracted but held = 1

#### U_R076 — Mohsin 2019, Pakistan

Reason:
- study target = CHD broadly, not harmonized CCHD;
- raw lesions among eight pulse-positive structural-CHD infants have been recovered;
- exact Phase 0.4 harmonized mapping must now be applied, including the 28-day intervention/death requirement for conditional lesions;
- population mixes Well Baby Unit and NICU and therefore carries a prespecified sensitivity/heterogeneity concern.

Raw pulse-positive structural lesions recovered:
- TGA;
- PA/IVS x2;
- TOF;
- DORV/VSD;
- ASD/CAVSD/pulmonary stenosis/PDA;
- CAVSD/DORV/pulmonary atresia;
- critical pulmonary stenosis.

Other pulse-positive diagnoses:
- PPHN x6;
- congenital pneumonia x2.

Do not use the study's `8 true positives` as `8 harmonized CCHD` without applying the lesion mapping lock.

## Harmonized CCHD lock now restored

Unconditional harmonized CCHD:
- HLHS;
- PA/IVS;
- simple TGA;
- interrupted aortic arch.

Conditional harmonized CCHD only with death or surgery/catheterization within 28 days:
- coarctation;
- aortic valve stenosis;
- pulmonary valve stenosis;
- TOF;
- PA/VSD;
- TAPVC/TAPVR.

Other lesion labels are not automatically CCHD and require reproducible mapping/equivalence evidence.

## Important corrections made during Phase 5

Phase 5 does not inherit diagnosis-as-actionability shorthand from Phase 4.

Examples:
- R009 PPHN/sepsis are CAN-U unless management consequence is documented.
- R024 disease diagnoses remain CAN-U despite generic `managed as per standard guidelines` wording.
- R072's earlier Phase 4.5 note `exact actionable numerator 10/33` is corrected: the accessible primary report supports `significant non-CCHD disease`, not specific actionability.
- `normal echo` is never used as a synonym for healthy.

These are downstream quantitative-classification corrections, not changes to Phase 4.5 membership.

## Current count

- Frozen Phase 5 units: **76**
- Structurally extracted: **11/76**
- QA-complete primary-poolable: **10**
- Extracted/held: **1**
- Not yet extracted: **65**

## Exact resume point

1. Continue U_R076 lesion-level harmonized mapping by seeking early intervention/death evidence for the conditional lesions.
2. If conditional timing remains unresolvable, retain the denominator hold rather than infer.
3. Continue structured extraction in additional blocks, prioritizing diagnostically complete units and applying the restored harmonized target plus Strict/Expanded actionability rules prospectively.

This file is the current safe resume point if the conversation is interrupted again.
