# CAN-CCHD Phase 5 — Extraction Block 19 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 19 COMPLETE / QA-CLOSED**

## Scope

Following identity reconstruction Block18, Block19 quantitatively reconstructs three exact primary reports:

- U_R002 — Koppel 2003
- U_R037 — Tautz 2010
- U_R067 — Klausner 2017

No legacy data were consulted. Primary/public report evidence was independently reverified and interpreted under the locked Phase5 target and CAN taxonomy.

## U_R002 — Koppel 2003

Primary report:
- 11,281 asymptomatic newborns screened;
- four positive screens implied by three source true positives plus one reported false-positive screen;
- detected CCVM: TAPVR2 + truncus arteriosus1;
- one conventional false-positive screen without a terminal diagnosis reported in the accessible primary report.

### Locked-target remap

The historical source CCVM label is not accepted as the harmonized target:
- TAPVR is conditional and no <=28-day death/surgery/catheterization qualifier is reported;
- truncus arteriosus is not an automatic locked target lesion.

Therefore:
- harmonized CCHD=0;
- denominator=4.

### CAN coding

- TAPVR2 + truncus1 -> CAN-U3 because diagnoses are clinically relevant but participant-specific qualifying actionability is not demonstrated;
- conventional false positive1 -> UNKNOWN1, because a source false-positive label does not establish globally healthy/no diagnosis.

Final:
- Strict0/4;
- Expanded3/4;
- ascertainment3/4=75%;
- SENSITIVITY_ONLY.

## U_R037 — Tautz 2010

Primary report:
- 3,364 term neonates screened at 6-36 h;
- 18 final abnormal screens requiring echocardiography;
- CHD9;
- persistent fetal circulation2;
- neonatal infections7.

The printed positive outcomes reconcile exactly to18.

### Locked-target remap

The nine CHD lesion identities are not reported in accessible primary evidence. Therefore any number0-9 could satisfy the locked target:
- harmonized CCHD0-9;
- denominator9-18.

### CAN coding

All harmonized-negative cases are clinically relevant diagnoses, but no participant-specific qualifying treatment/escalation/disposition/follow-up consequence is linked:
- Strict0;
- CAN-U=9-18;
- Expanded=9-18;
- Expanded proportion remains100% under every admissible target scenario.

Positive diagnostic ascertainment is complete, but target mapping is not point-identifiable. Therefore SENSITIVITY_ONLY.

## U_R067 — Klausner 2017

Primary report:
- 10,589 live births;
- 171 had echocardiography before screening;
- 10,320 screened;
- 10,316 negative screens;
- therefore four positive POx screens;
- all four showed noncritical cardiac lesions by echocardiography;
- no CCHD was identified through POx screening alone.

### Locked-target remap

All four positive-screen findings are explicitly described as noncritical cardiac lesions and remain in the harmonized CCHD-negative denominator:
- harmonized CCHD=0;
- denominator=4.

### CAN coding

- noncritical cardiac lesions4 -> CAN-U4 because no participant-specific qualifying actionability consequence is reported;
- Strict0/4;
- Expanded4/4;
- positive-outcome ascertainment100%.

The reported 52.1% one-year retention concerns negative screens and does not reduce ascertainment of the four final-positive infants used in this CAN denominator.

Classification: PRIMARY_POOLABLE.

## Block19 disposition

Newly extracted: **3**.

- PRIMARY_POOLABLE: +1 — U_R067
- SENSITIVITY_ONLY: +2 — U_R002, U_R037
- HOLD_PENDING_QA: +0
- NOT_POOLABLE: +0

Updated Phase5 totals:
- structurally extracted: **68/76**
- PRIMARY_POOLABLE: **25**
- SENSITIVITY_ONLY: **37**
- HOLD_PENDING_QA: **3**
- NOT_POOLABLE: **3**
- remaining unextracted: **8**

## Remaining queue

U_R001, U_R003, U_R006, U_R008, U_R013, U_R036, U_R042, U_R066.

The d-TGA/simple-TGA policy remains deliberately deferred until 76/76 structural extraction. No final target freeze or primary meta-analysis is run at this stage.
