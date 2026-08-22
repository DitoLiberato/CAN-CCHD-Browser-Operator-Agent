# CAN-CCHD Phase 5 — Progress Snapshot G

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT**

## Current state

Phase 5 continues exclusively from the 76 frozen unique quantitative units created at Phase 4.5 closure. No scientific value is imported from the legacy Browser Agent/database.

Eight extraction blocks are now complete.

## Current counts

- Frozen Phase 5 units: **76**
- Structurally extracted: **31/76**
- `PRIMARY_POOLABLE`: **16**
- `SENSITIVITY_ONLY`: **13**
- `HOLD_PENDING_QA`: **2**
- Not yet extracted: **45**

The two unresolved QA holds remain:
- U_R033 Qatar — internal source inconsistency between narrative and diagnostic table;
- U_R102 Turkey/Sero — broad cardiac target plus unresolved diagnostic-category exclusivity/full-text limitation.

No new hold was created in Block 08.

## Block 08 units

### U_R007 — Sendelbach 2008
- 15,233 screened;
- 859 initially <96%, but 767/768 rescreened infants normalized;
- only one persistent final failed screen;
- normal echocardiogram, no alternative clinical diagnosis reported;
- denominator 1;
- Strict 0/1; Expanded 0/1; UNKNOWN1;
- ascertainment 0%;
- `SENSITIVITY_ONLY`.

Key rule: initial screen abnormalities that resolve during the protocol-defined repeat sequence are PASS, not denominator events.

### U_R015 — Zuppa 2015
- 5,750 low-risk nursery newborns;
- 3 final pulse-oximetry positives;
- PFO2 -> NON_CAN;
- one structurally normal echo without noncardiac clinical ascertainment -> UNKNOWN1;
- Strict 0/3; Expanded 0/3;
- ascertainment 66.7%;
- `SENSITIVITY_ONLY`.

The older secondary interpretation that all three false positives had PPHN remains rejected because the primary report does not support it.

### U_R021 — Miranda Peralta, Panama
- reported total screened = 2,236, with source discussion discrepancy of 2,235;
- 16 final positives;
- PDA with hemodynamic repercussion x6, of which 2 required medical closure;
- anomalous pulmonary venous connections x3;
- structurally normal echo x6;
- one complex right-heart lesion described as PA versus critical pulmonary stenosis.

Harmonized target bound:
- if PA/IVS -> harmonized CCHD1 and denominator15;
- if critical pulmonary stenosis without documented <=28-day intervention/death -> harmonized CCHD0 and denominator16.

CAN coding:
- CAN-A2 (PDA requiring medical closure);
- CAN-U7 or 8 depending complex-lesion mapping;
- UNKNOWN6;
- Strict2 throughout;
- Expanded9/15 or10/16;
- ascertainment60.0%-62.5%;
- `SENSITIVITY_ONLY`.

### U_R086 — Garg/New Jersey
- 73,320 eligible births; 99.1% screened; exact screened integer is not reconstructed from rounded values;
- mixed WBN + NICU/SCN statewide population;
- 49 failed screens;
- authors label 7 as CCHD, but locked harmonized mapping removes only HLHS and interrupted aortic arch from the denominator based on reported information;
- harmonized denominator = 47.

Terminal coding:
- CAN-A3;
- CAN-U9;
- NON_CAN10;
- explicit no diagnosis12;
- UNKNOWN13;
- Strict3/47;
- Expanded12/47;
- ascertainment34/47 = 72.3%;
- `SENSITIVITY_ONLY` because of both incomplete terminal classification and inseparable mixed setting.

## Canonical Block 08 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_08.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_08_AUDIT.md`

## Identity-reconciliation queue preserved

The frozen units U_R001, U_R002, U_R003 and U_R006 remain unextracted because their exact bibliographic identities are not sufficiently preserved in the currently accessible restart-native artifacts. They must not be reconstructed from the legacy database or guessed from historical literature. Resolve them later through restart-native bibliographic provenance or independent re-verification.

## Exact resume point

Proceed to **Block 09** from the remaining 45 units with secure bibliographic identities, while continuing prospectively to enforce:

1. final-failed-screen rather than initial-abnormal denominator;
2. lesion-level harmonized CCHD mapping;
3. Strict versus Expanded actionability;
4. >=90% terminal ascertainment for principal pooling;
5. normal echo != healthy;
6. no diagnosis-as-actionability inference;
7. mixed/NICU setting sensitivity rules;
8. no legacy-data contamination.

This snapshot supersedes Snapshot F as the current safe resume point.
