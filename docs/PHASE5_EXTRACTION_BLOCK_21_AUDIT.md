# CAN-CCHD Phase 5 — Extraction Block 21 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 21 COMPLETE / STRUCTURAL EXTRACTION 76/76**

## Scope

Block21 closes the six remaining structurally unextracted frozen Phase4.5 quantitative units:

- U_R001 — Richmond 2002
- U_R003 — Reich 2003
- U_R006 — Meberg 2008
- U_R008 — de-Wahl Granelli 2009
- U_R013 — Turska-Kmiec 2012
- U_R036 — Arlettaz 2006

No legacy app/database source was consulted. Primary reports were independently reverified. The harmonized target lock and CAN taxonomy remained binding. The deferred simple-TGA policy was **not adjudicated** in this block.

## U_R001 — Richmond 2002

Primary-source reconstruction shows that the implemented repeat pathway does not map cleanly to a single locked terminal failed-screen denominator:

- 5,626 screened;
- 296 first measurements <95%;
- nine had clinical concern after the first low saturation;
- among the remaining infants, 51 had a second saturation <95%;
- nine of these51 then raised clinical concern;
- among the remaining42, 12 underwent normal echocardiography and30 underwent a third measurement that normalized.

Thus two historically used positivity conventions can be reconstructed:

- 60 = nine initial clinical concerns +51 second-low screens;
- 30 = nine initial concerns + nine concerns after second-low +12 downstream echocardiograms, with30 second-low infants ultimately normalizing on a third measure.

The stated protocol says an unsatisfactory repeat should lead to echocardiography, but the implemented pathway allowed a third saturation in30 infants. The locked Phase5 analytic unit is the infant after completion of the study repeat sequence; forcing either historical convention would therefore be arbitrary.

The article nevertheless provides valuable pathology detail among19 infants first identified as unwell through saturation measurement, including TTN7, PA2, PPHN2, simple TGA1, CoA+VSD1, TOF1, PDA2, pneumothorax1, septo-optic dysplasia1 and surgically evacuated arachnoid-cyst hemorrhage1. Those diagnoses cannot be reconciled to one reproducible terminal denominator.

Disposition: **NOT_POOLABLE**.

## U_R003 — Reich 2003

Primary report:

- 2,114 screened;
- 88 echocardiograms overall;
- 43 abnormal echocardiograms;
- 12 echocardiographic findings required management;
- three cyanotic-CHD births during the study year;
- pulse oximetry detected one cyanotic CHD but missed one TAPVR.

The 88 echocardiograms are not equivalent to terminal pulse-positive screens because echocardiography also arose from routine clinical indications. The primary article does not link the 12 management-requiring findings to the terminal pulse-positive infants.

Independent evidence abstractions disagree on whether the terminal pulse-positive count is3 or4. Cochrane explicitly notes that Reich provides only a partial2x2 diagnostic table.

The binding restart rules prohibit using secondary abstractions to manufacture a primary denominator or CAN numerator.

Disposition: **NOT_POOLABLE**.

## U_R006 — Meberg 2008

Primary report:

- 50,008 screened;
- 324 final pathological screens;
- CHD43;
- pulmonary/other disorders134;
- healthy transitional circulation147;
- exact top-level reconciliation43+134+147=324.

Raw CHD lesions among failed screens:
- TGA11;
- AVSD8;
- VSD6;
- TAPVR5;
- CoA4;
- pulmonary atresia3;
- aortic stenosis2;
- pulmonary stenosis1;
- truncus1;
- TOF1;
- single ventricle1.

Under the locked target, generic `TGA` cannot yet be automatically equated with `simple TGA`; this exact policy is deliberately deferred. Pulmonary atresia is not specified IVS versus VSD. Conditional lesions lack participant-level <=28-day death/intervention timing. Consequently the provisional harmonized target count is0-11 and denominator313-324.

Actionability remains independently recoverable. The primary report states that low SpO2 prompted early cardiologic examination for CHD and that valuable time may have been gained. This is a screen-attributable follow-up change:

- CAN-B = harmonized-negative CHD32-43;
- CAN-U134 = pulmonary/other disorders without participant-specific treatment/disposition detail;
- NON_CAN147 = explicitly healthy transitional circulation.

Thus:
- Strict32-43;
- Expanded166-177;
- ascertainment100%;
- **SENSITIVITY_ONLY** pending final target adjudication.

## U_R008 — de-Wahl Granelli 2009

Primary report:

- 39,821 screened;
-19 source duct-dependent pulse-positive infants;
-69 source false positives;
- final failed screens88.

For the69 source false positives, primary Table3 provides both diagnosis and subsequent management:

- other critical CHD4 — all NICU >=5d and surgery;
- milder CHD10 — every infant had NICU admission and/or follow-up; surgery in4;
- PPHN6 —3 NICU >=5d,3 follow-up;
- transitional circulation8 —3 NICU <5d,2 follow-up,3 no qualifying action;
- infections10 — all NICU;
- pulmonary pathology7 —6 NICU,1 follow-up;
- verified normal24.

Therefore, invariant across target scenarios:
- Strict CAN-A42;
- NON_CAN3;
- explicitly healthy24.

Among19 source duct-dependent positives, the locked unconditional mapping establishes HLHS3 + IAA2 =5. Two isolated rows labelled only `TGA` are left for the deferred simple-TGA policy, producing provisional harmonized target5-7 and denominator81-83. The remaining12-14 source-DDC infants that re-enter the harmonized-negative denominator have clinically important structural diagnoses but insufficient participant-level qualifying management timing in the screening table -> CAN-U12-14.

Final:
- Strict42;
- Expanded54-56;
- ascertainment100%;
- **SENSITIVITY_ONLY** pending final target adjudication.

This unit is particularly important because target uncertainty does **not** contaminate the observed Strict numerator.

## U_R013 — Turska-Kmiec 2012

Primary report:

- 51,698 screened;
- 29 final positives;
- source CCHD15;
- false positives14 = transitional8 + ASD ostium secundum1 + intrauterine infection2 + pneumonia3.

Detected source-CCHD lesions:
- TGA3;
- TAPVD3;
- pulmonary atresia2;
- IAA1;
- HLHS1;
- CoA1;
- truncus1;
- congenitally corrected TGA1;
- TOF1;
- right-pulmonary-artery fistula1.

The source definition refers to first-month intervention, but the harmonized lock requires actual lesion/event evidence for conditional lesions and cannot substitute a broad study label.

Locked unconditional evidence currently establishes IAA1 + HLHS1 =2. The three isolated TGA labels are reserved for joint simple-TGA adjudication -> provisional target2-5; denominator24-27.

CAN mapping:
- infection/pneumonia5 -> CAN-U5; detected before symptoms, but no participant-specific treatment/escalation is reported;
- transitional8 explicitly described as not requiring early intervention -> NON_CAN8;
- incidental ASD1 -> NON_CAN1;
- re-entered source-CCHD10-13 -> CAN-U because clinically relevant but qualifying screen-attributable actionability is not individually documented.

Final:
- Strict0;
- Expanded15-18;
- NON_CAN9;
- ascertainment100%;
- **SENSITIVITY_ONLY** pending final target adjudication.

## U_R036 — Arlettaz 2006

Primary report:

- 3,262 screened;
- 24 final low-saturation echocardiograms;
- CHD17;
- PPHN5;
- myocardial tumour1;
- normal heart1;
- exact reconciliation17+5+1+1=24.

The primary figure permits lesion recovery among the17 CHD positives, including HLHS3, TGA2, DORV3, truncus3, CoA1, AVSD1, VSD1, critical PS1, aortic atresia1 and PA+VSD1.

Locked unconditional evidence establishes HLHS3. The two isolated TGA labels remain deferred -> provisional target3-5; denominator19-21. Conditional lesions lack documented <=28-day event timing.

CAN mapping:
- PPHN5 -> CAN-U; authors discuss careful evaluation/correct management but do not provide participant-specific qualifying management;
- myocardial tumour1 -> CAN-U;
- normal heart1 -> UNKNOWN, not healthy, because noncardiac outcome is not ascertained;
- re-entered source-CHD12-14 -> CAN-U.

Final:
- Strict0;
- Expanded18-20;
- UNKNOWN1;
- ascertainment94.7%-95.2%;
- **SENSITIVITY_ONLY** pending final target adjudication.

## Block21 disposition

Newly structurally extracted: **6**.

- PRIMARY_POOLABLE: +0
- SENSITIVITY_ONLY: +4 — U_R006, U_R008, U_R013, U_R036
- HOLD_PENDING_QA: +0
- NOT_POOLABLE: +2 — U_R001, U_R003

## Phase5 structural-extraction milestone

**76/76 frozen quantitative units are now structurally extracted.**

Current provisional classes before final target adjudication:

- PRIMARY_POOLABLE: **26**
- SENSITIVITY_ONLY: **42**
- HOLD_PENDING_QA: **3**
- NOT_POOLABLE: **5**
- unextracted: **0**

Total =76.

These are not yet the frozen final analysis pools.

## Mandatory stop point reached

Per Snapshot P/Q and the user's explicit instruction, Phase5 now pauses **before** final simple-TGA/d-TGA policy adjudication.

The next scientific movement is not another extraction block. It is a joint target-policy audit covering:

1. whether an isolated primary-report label `TGA`, without explicit `simple` or associated anatomy, may reproducibly be treated as the lock's `simple TGA`;
2. whether `d-TGA` with associated lesions should be treated differently from anatomically simple d-TGA under the Cochrane anchor;
3. how that decision propagates through all76 extracted rows, not only Block21;
4. conditional-lesion target audit (actual <=28-day death/surgery/catheterization evidence);
5. resolution of remaining HOLD_PENDING_QA units where possible;
6. only then freezing final primary/sensitivity/not-poolable pools and proceeding to quantitative synthesis.

No final meta-analysis should be run before this adjudication is frozen.
