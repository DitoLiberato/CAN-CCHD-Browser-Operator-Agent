# CAN-CCHD Phase 5 — Progress Snapshot R

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **SAFE RESUME POINT — STRUCTURAL EXTRACTION COMPLETE 76/76 / TARGET ADJUDICATION NOT YET FROZEN**

## Binding scientific state

The restart legacy-data firewall remains binding. Phase5 scientific values derive only from the76 frozen Phase4.5 quantitative units and independently reverified restart-native/primary evidence.

The harmonized CCHD target lock remains unchanged:
- unconditional: HLHS, PA/IVS, simple TGA, IAA;
- conditional on death/surgery/catheterization <=28 days: CoA, aortic stenosis, pulmonary stenosis, TOF, PA/VSD, TAPVC/TAPVR;
- non-listed structural lesions are not automatically promoted;
- source labels such as critical/major/cyanotic/CCHD cannot substitute for locked lesion/event evidence.

CAN taxonomy remains unchanged:
- Strict = CAN-A + CAN-B + CAN-AB;
- Expanded = Strict + CAN-U;
- diagnosis alone is not actionability;
- screen-attributable management, disposition, treatment, escalation, or follow-up is qualifying evidence.

## Structural extraction milestone

All frozen units are now structurally extracted:

**76/76 = 100%.**

There is no remaining identity queue and no remaining unextracted-unit queue.

## Current provisional disposition

Before the final harmonized-target adjudication:

- PRIMARY_POOLABLE: **26**
- SENSITIVITY_ONLY: **42**
- HOLD_PENDING_QA: **3**
- NOT_POOLABLE: **5**
- unextracted: **0**

Total =76.

These labels remain provisional until the target audit is frozen.

## Blocks completed since Snapshot P

### Block18 — identity reconstruction
All11 pending bibliographic identities reconstructed exactly from restart-native artifacts. No analytical variables changed.

### Block19
- U_R002 Koppel -> SENSITIVITY_ONLY
- U_R037 Tautz -> SENSITIVITY_ONLY
- U_R067 Klausner -> PRIMARY_POOLABLE

### Block20
- U_R042 Bhola -> SENSITIVITY_ONLY
- U_R066 Jones -> PRIMARY_POOLABLE

### Block21
- U_R001 Richmond -> NOT_POOLABLE
- U_R003 Reich -> NOT_POOLABLE
- U_R006 Meberg -> SENSITIVITY_ONLY pending target adjudication
- U_R008 de-Wahl Granelli -> SENSITIVITY_ONLY pending target adjudication
- U_R013 Turska-Kmiec -> SENSITIVITY_ONLY pending target adjudication
- U_R036 Arlettaz -> SENSITIVITY_ONLY pending target adjudication

## Important Block21 findings

### U_R008 de-Wahl Granelli
- final failed screens88 =19 source duct-dependent positives +69 source false positives;
- locked target provisionally5-7 because HLHS3+IAA2 are certain and two isolated TGA labels remain deferred;
- denominator81-83;
- primary Table3 supports Strict42 invariant across all target scenarios;
- re-entered source-DDC12-14 -> CAN-U;
- Expanded54-56;
- ascertainment100%.

### U_R006 Meberg
- 324 final pathological screens reconcile43 CHD +134 pulmonary/other disorders +147 healthy transitional;
- generic TGA11 cannot yet be silently equated with simple TGA;
- target0-11; denominator313-324;
- screen-attributable early cardiologic examination makes harmonized-negative CHD CAN-B32-43;
- CAN-U134; NON_CAN147;
- Strict32-43; Expanded166-177; ascertainment100%.

### U_R013 Turska-Kmiec
-29 final positives =15 source CCHD +14 false positives;
- certain locked target IAA1+HLHS1=2; isolated TGA3 deferred -> target2-5;
- denominator24-27;
- Strict0; Expanded15-18; NON_CAN9; ascertainment100%.

### U_R036 Arlettaz
-24 final positives =17 CHD +5 PPHN +1 myocardial tumour +1 normal-heart echo;
- certain target HLHS3; isolated TGA2 deferred -> target3-5;
- denominator19-21;
- Strict0; Expanded18-20; UNKNOWN1;
- ascertainment94.7%-95.2%.

### U_R001 Richmond
The implemented repeat pathway diverged from the stated protocol and supports incompatible terminal positivity conventions (30 vs60). Raw pathology is informative, but no single locked final-failed-screen denominator can be reproduced without an arbitrary convention. NOT_POOLABLE.

### U_R003 Reich
Primary report does not link terminal pulse-positive infants to the all-echocardiogram management outcomes; external abstractions disagree3 vs4 terminal positives, and Cochrane identifies only a partial2x2 table. NOT_POOLABLE.

## Exact scientific stop point

The previously agreed stop point has been reached. Do **not** begin final meta-analysis yet.

The next movement is **Phase5 target adjudication / final QA**, beginning with the jointly deferred TGA question.

### Question 1 — isolated `TGA` label
The lock says `simple TGA` is unconditional. Several primary studies report an isolated lesion label `TGA` with no associated lesion in the table, but do not literally write `simple TGA`.

The final policy must decide whether:
A. an isolated primary-table label `TGA`, with no associated anatomy reported, is reproducibly treated as anatomically simple TGA; or
B. the word `simple` must be explicit, so generic isolated `TGA` remains unresolved/non-target unless further anatomy is found.

This decision affects at least Block21 units U_R006, U_R008, U_R013 and U_R036 and must be audited across all76 units.

### Question 2 — d-TGA with associated lesions
Complex TGA/d-TGA combinations should not automatically inherit `simple TGA` status merely because TGA is present. The target lock's explicit wording must be reconciled with the Cochrane anchor and applied consistently to combinations.

### Then
After freezing the TGA policy:
1. rerun target mapping across all76 rows;
2. audit every conditional lesion for actual <=28-day death/surgery/catheterization evidence;
3. resolve the three HOLD_PENDING_QA units where possible;
4. recompute exact denominators/numerators and ascertainment;
5. freeze final PRIMARY_POOLABLE / SENSITIVITY_ONLY / NOT_POOLABLE pools;
6. only then perform quantitative synthesis.

## New canonical artifacts

- Block21 CSV — commit `7a1396cfd8fc150e8bc327fea3417e77e2deb87b`
- Block21 audit — commit `53dcb0458eb1beba3498d9e007d813c9c5f8ddba`

Snapshot R supersedes Snapshot Q as the safe resume point.
