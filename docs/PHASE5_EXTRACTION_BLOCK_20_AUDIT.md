# CAN-CCHD Phase 5 — Extraction Block 20 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 20 COMPLETE / QA-CLOSED**

## Scope

Block20 quantitatively reconstructs two primary reports from the post-identity queue:

- U_R042 — Bhola 2014
- U_R066 — Jones 2016

The restart legacy-data firewall was respected. Primary/public report evidence was independently reverified and interpreted under the binding Phase5 target and CAN taxonomy.

## U_R042 — Bhola 2014

Primary report:
- 18,801 well newborns screened;
- four source true-positive major CHD cases diagnosed before discharge;
- 11 source false-positive/no-CHD screens;
- six of those 11 had respiratory pathology;
- one large-VSD false negative had normal saturation and is outside the final-failed-screen denominator.

Therefore final failed screens =15.

### Locked-target remap

The four source-major-CHD lesions are not individualized in accessible primary evidence, and the source ascertainment horizon is surgery in the first 12 months rather than the locked <=28-day target event horizon. Therefore those four cannot be automatically removed:
- harmonized CCHD0-4;
- denominator11-15.

### CAN coding

- respiratory pathology6 -> CAN-U6 because no participant-specific treatment/disposition/escalation/follow-up consequence is reported;
- five remaining source false positives -> UNKNOWN5 because their terminal diagnoses/outcomes are not reported;
- if any of the four source-major-CHD cases re-enter the harmonized-negative denominator, they remain clinically relevant but actionability-undemonstrated -> CAN-U.

Thus:
- Strict0;
- CAN-U6-10;
- Expanded6-10;
- ascertainment6-10 / denominator11-15 =54.5%-66.7%;
- SENSITIVITY_ONLY.

Diagnostic consultant review alone was not promoted to Strict actionability.

## U_R066 — Jones 2016

Primary report:
- 11,233 live births;
- 973 neonatal-unit admissions before screening and unrelated to screening;
- screening population10,260;
- 23 asymptomatic newborns admitted to the neonatal unit because of a positive pulse-ox screen;
- participant-level table identifies two critical CHD and 21 noncritical/alternative outcomes.

Table reconciliation:
- CCHD2;
- pneumonia10;
- normal transitional circulation5;
- trisomy21 2;
- TTN1;
- congenital diaphragmatic hernia1;
- ASD+PDA1;
- pneumothorax1;
=23.

### Locked-target remap without using the deferred d-TGA policy

Both source critical-CHD cases independently satisfy the locked target:
1. infracardiac TAPVC -> repair day14;
2. TGA+VSD+ASD+CoA -> CoA repair day7 and arterial switch day21.

Therefore the second infant qualifies through event-qualified CoA even before any final d-TGA/simple-TGA adjudication.

Final:
- harmonized CCHD=2;
- denominator=21.

### CAN coding

All 21 harmonized-negative newborns were asymptomatic before screening and were admitted to the neonatal unit **because of the screen-positive result**. This is explicit acute disposition change attributable to screening and satisfies the binding actionability rule.

Therefore:
- CAN-A21;
- Strict21/21;
- Expanded21/21;
- ascertainment100%.

The five infants whose eventual label was normal transitional circulation are not NON_CAN in this unit because the screening pathway caused NNU admission; moreover all five underwent blood tests and received antibiotics for >=48h. CAN classification follows observed screen-attributable actionability, not diagnostic severity alone.

Classification: PRIMARY_POOLABLE.

## Block20 disposition

Newly extracted: **2**.

- PRIMARY_POOLABLE: +1 — U_R066
- SENSITIVITY_ONLY: +1 — U_R042
- HOLD_PENDING_QA: +0
- NOT_POOLABLE: +0

Updated Phase5 totals:
- structurally extracted: **70/76 (92.1%)**
- PRIMARY_POOLABLE: **26**
- SENSITIVITY_ONLY: **38**
- HOLD_PENDING_QA: **3**
- NOT_POOLABLE: **3**
- remaining unextracted: **6**

## Remaining queue

U_R001, U_R003, U_R006, U_R008, U_R013, U_R036.

The d-TGA/simple-TGA policy remains deliberately deferred until 76/76 structural extraction. Jones does not require that adjudication because its TGA participant independently meets the locked target via event-qualified coarctation.
