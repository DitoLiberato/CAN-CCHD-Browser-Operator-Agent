# CAN-CCHD Phase 5 — All-76 Target Rerun — Batch 02: Conditional-Lesion / Anatomy Audit

Date: 2026-08-22
Branch: `phase5-extraction`
Parent rerun checkpoint: `docs/PHASE5_ALL76_TARGET_RERUN_BATCH01_TGA_SWEEP.md`
Status: **BATCH 02 COMPLETE / ALL 76 CONDITIONAL-LESION RULES RE-AUDITED / FINAL HOLD RESOLUTION NEXT**

## Purpose

Complete the second half of the post-Snapshot-S rerun: re-audit the 76 structurally extracted quantitative units for the binding conditional-target rule.

The d-TGA amendment from Batch 01 remains binding. This Batch 02 does **not** broaden any other target component.

## Binding conditional rule

The following lesions are harmonized CCHD only when the infant actually:

- dies within the first 28 days, or
- undergoes cardiac surgery within the first 28 days, or
- undergoes cardiac catheter intervention within the first 28 days:

1. CoA;
2. aortic valve stenosis;
3. pulmonary valve stenosis;
4. TOF;
5. PA/VSD;
6. TAPVC/TAPVR.

A study label such as `critical`, `CCHD`, `major`, `cyanotic`, `duct-dependent`, `requiring early intervention`, or `potentially fatal` does not substitute for an observed qualifying event when the lesion is conditional.

Pulmonary atresia is anatomy-dependent:

- PA/IVS -> unconditional target;
- PA with VSD/non-intact septum -> conditional;
- generic PA with septal anatomy unavailable -> target status remains genuinely unresolved unless an actual qualifying <=28-day event independently resolves it.

Missing event timing is coded as unknown, not as yes.

## Audit scope and method

All **76/76** latest structural-extraction records were re-read after the d-TGA sweep. Historical block CSVs were not overwritten.

For every conditional lesion present in the frozen extraction evidence, the rerun asked:

1. Is the lesion identity participant-level and reproducible?
2. Is it unconditional because another component independently qualifies (e.g. d-TGA, HLHS, IAA, PA/IVS)?
3. If not, is an actual death/surgery/catheter event <=28 days documented?
4. If neither, the lesion remains in the harmonized-CCHD-negative denominator.
5. If pulmonary atresia anatomy is unspecified, do not silently assume PA/IVS.

Primary reports/available full texts were revisited where an existing `PRIMARY_POOLABLE` weight had depended on an author/Cochrane CCHD count rather than lesion/event-level evidence.

## A. Existing mappings confirmed as already compliant

The previous structural extraction had already applied the conservative conditional rule correctly in many units. Important confirmed examples include:

- **U_R031 Jordan** — only HLHS23 + TGA17 removed; TOF/unspecified PA/PS/CoA/TAPVR remained denominator because participant-level <=28-day events were not reported.
- **U_R034 Denmark** — pulmonary stenosis remains conditional and produces a genuine 0-1 target bound.
- **U_R035 Hoke** — d-TGA target; TOF/CoA/PS remain denominator without qualifying events.
- **U_R087 Minnesota** — TOF/pulmonary-atresia complex remains denominator without qualifying <=28-day event.
- **U_R104 Baramati** — TGA target; TOF2 + TAPVR1 remain denominator.
- **U_R126 Hidalgo** — HLHS-equivalent anatomy target; TOF remains denominator because palliative-operation timing is not established as <=28 days.
- **U_R125_BARRANQUILLA_CO** — TOF/TAPVR remain denominator; target=0.
- **U_NR044 Bangalore** — TGA3 target; TAPVD/TOF/PS labels remain denominator because early event evidence is absent.
- **U_NR058 Hyderabad** — pulmonary stenosis remains denominator; target=0.

No correction is required for those mappings beyond the d-TGA changes already recorded in Batch 01.

## B. Conditional lesions with actual <=28-day evidence confirmed

These units retain their conditional target assignments because the required event criterion is supported:

### U_R017 Jawin 2015

- PA/VSD infant received ductal stenting at approximately 1 week -> conditional PA/VSD qualifies.
- second pulse-positive CCHD includes TGA -> target independently through d-TGA.
- no change from the current point target count.

### U_R041 Zhao/China multicentre 2014

The source's `critical CHD` analytic class is operationally defined by death or intervention before 28 days. Conditional PS/TOF/PA/CoA/AS/TAPVC cases inside that class therefore retain conditional-target status. Population remains mixed nursery/NICU and `SENSITIVITY_ONLY` for setting reasons.

### U_R066 Northwick Park/Jones 2016

- TAPVC repair day 14 -> qualifies.
- TGA+CoA infant had CoA repair day 7 and arterial switch day 21; d-TGA independently qualifies and the CoA event also meets the conditional rule.
- target count remains 2.

### U_R100 New Zealand/Cloete 2020

The study target is explicitly cardiac intervention and/or cardiac-related death within 28 days, and the mapped screen-positive target cases belong to that event-defined group. Existing target count3 remains accepted.

### U_R101 Cambridge/Singh & Chen 2022

Source critical CHD is explicitly defined by intervention/death within 28 days. Mapped CoA1 and critical PS2 therefore remain conditionally qualified alongside unconditional HLHS1 + IAA1. Existing target count5 remains accepted.

## C. Primary-pool corrections required by the conditional rerun

### C1. U_R009 — Riede 2010, Germany

Pre-rerun extraction:

- final fails54;
- target14;
- denominator40;
- Strict0;
- Expanded28;
- healthy12.

Primary lesion-level evidence among the 14 source true positives:

- TGA x2;
- TGA+VSD x2;
- HLHS x1;
- truncus arteriosus + IAA x1;
- PA/VSD x2;
- TAPVD x5;
- Taussig-Bing x1.

The article describes these as defects for which early intervention is mandatory, but does not document case-level death/surgery/catheterization <=28 days for the PA/VSD or TAPVD participants. Under the binding lock, clinical necessity is not the observed event.

Amended mapping:

- TGA-bearing x4 -> unconditional target;
- HLHS1 -> unconditional target;
- IAA-containing case1 -> unconditional target;
- PA/VSD2 -> denominator;
- TAPVD5 -> denominator;
- Taussig-Bing1 -> denominator/off-list.

**Final Batch-02 target = 6.**

**Denominator = 54 - 6 = 48.**

The 28 historical false-positive PPHN/sepsis diagnoses remain CAN-U and the 12 explicitly healthy infants remain healthy. The eight returned structural cases are clinically relevant but lack qualifying actionability evidence -> CAN-U8.

Final:

- Strict **0/48**;
- CAN-U **36**;
- Expanded **36/48**;
- explicitly healthy **12**;
- ascertainment **100%**;
- **PRIMARY_POOLABLE retained**.

### C2. U_R018 — Özalkaya 2016, Turkey

Pre-rerun extraction imported the source/Cochrane 6-TP / 1-FP framework as target6, denominator1.

The primary article's true-positive table identifies:

1. CoA + hypoplastic transverse aorta;
2. TGA;
3. TGA;
4. TAPVR;
5. pulmonary stenosis;
6. pulmonary hypoplasia.

The paper does not document actual <=28-day death/surgery/catheterization for the CoA, TAPVR, or PS cases. `Pulmonary hypoplasia` is not a locked cardiac target lesion.

Therefore:

- TGA x2 -> target;
- CoA -> denominator;
- TAPVR -> denominator;
- pulmonary stenosis -> denominator;
- pulmonary hypoplasia -> denominator;
- PFO historical false positive -> denominator/NON_CAN.

Final:

- target **2**;
- denominator **5**;
- Strict **0/5**;
- CAN-U **4**;
- Expanded **4/5**;
- NON_CAN **1**;
- ascertainment **100%**;
- **PRIMARY_POOLABLE retained**.

### C3. U_R071 — Cubells 2018, Spain

Pre-rerun:

- final fails5;
- target TAPVR3;
- denominator2;
- Strict2/2.

The source definition includes defects requiring invasive intervention **or capable of causing death** in approximately the first month, but the report does not document actual participant-level surgery/catheterization/death <=28 days for the three TAPVR infants.

Under the lock, theoretical risk does not satisfy the conditional event requirement.

Final:

- target **0**;
- denominator **5**;
- early-onset sepsis with respiratory distress x2 and screen-attributable NICU admission -> Strict CAN-A **2**;
- returned TAPVR x3 -> CAN-U **3**;
- Expanded **5/5**;
- ascertainment **100%**;
- **PRIMARY_POOLABLE retained**.

### C4. U_R072 — Diller 2018, United States

Pre-rerun:

- final fails34;
- source true-positive TAPVR1 removed;
- denominator33;
- CAN-U10;
- NON_CAN23.

No accessible primary case-level evidence establishes surgery/catheterization/death <=28 days for the TAPVR infant. The TAPVR case therefore returns to the denominator.

Final:

- target **0**;
- denominator **34**;
- Strict **0/34**;
- CAN-U **11** = historical significant non-CCHD disease10 + returned TAPVR1;
- Expanded **11/34**;
- NON_CAN **23**;
- ascertainment **100%**;
- **PRIMARY_POOLABLE retained**.

## D. Former PRIMARY_POOLABLE units downgraded because target is not point-identifiable

### D1. U_R020 — POLAR / Narayen 2018, Netherlands

The source reports:

- final failed screens226;
- source CCHD5;
- source false positives221.

The accessible primary/same-cohort material provides a complete 221-case false-positive clinical distribution but does not expose the five source-CCHD lesion identities sufficiently for the binding lesion/event mapping.

The source label `CCHD` cannot substitute for harmonized lesion/event evidence.

Therefore:

- harmonized target among the five source CCHD = **0-5**;
- denominator = **221-226**.

Within the known 221 source-defined false positives:

- Strict =131 (respiratory/infection/other pathology with source-linked referral/treatment evidence);
- CAN-U=3 noncritical CHD;
- healthy=87.

If any/all five source-CCHD infants re-enter the harmonized-negative denominator, they are clinically relevant structural diagnoses but lack sufficient mapped evidence for Strict CAN classification -> additional CAN-U0-5.

Final rerun representation:

- Strict **131**;
- CAN-U **3-8**;
- Expanded **134-139**;
- healthy **87**;
- denominator **221-226**;
- **SENSITIVITY_ONLY — TARGET_MAPPING_BOUND**.

This is a downgrade from `PRIMARY_POOLABLE` because no single harmonized analysis weight can be assigned without the five lesion identities.

### D2. U_R024 — Gopalakrishnan 2021, India

Primary article:

- final fails16;
- source true positives: TGA/IVS x2 + pulmonary atresia x1;
- source false positives: sepsis/congenital pneumonia8 + PPHN2 + transitional circulation3.

The two TGA cases are unconditional target.

The pulmonary-atresia case is reported only as `pulmonary atresia`; intact versus non-intact septal anatomy is not established. All three source true positives were stabilized with PGE1 and transferred to a cardiothoracic surgical centre. This is clinically actionable care, but it does not establish PA/IVS anatomy and it does not itself document surgery/catheterization/death <=28 days.

Two admissible harmonized scenarios remain:

**Scenario A — PA = PA/IVS**
- target3;
- denominator13;
- Strict0;
- CAN-U10;
- Expanded10;
- NON_CAN transitional3.

**Scenario B — PA does not establish PA/IVS and no <=28-day invasive/death event is documented**
- target2;
- denominator14;
- the returned PA infant has explicit screen-attributable PGE1 stabilization + transfer -> CAN-A1;
- CAN-U10;
- Strict1;
- Expanded11;
- NON_CAN3.

Thus:

- target **2-3**;
- denominator **13-14**;
- Strict **0-1**;
- Expanded **10-11**;
- ascertainment **100%**;
- **SENSITIVITY_ONLY — PA_ANATOMY_BOUND**.

This is a downgrade from `PRIMARY_POOLABLE` because the primary harmonized denominator is not point-identifiable.

### D3. U_R043 — Oakley 2015, United Kingdom

Source reports:

- final fails14;
- source CCHD7;
- source CCHD-negative7 = noncritical significant CHD3 + previously undiagnosed respiratory illness/sepsis4.

The accessible primary evidence does not provide the seven source-CCHD lesions or case-level <=28-day events. Cochrane's CCHD classification is useful secondary context but cannot manufacture lesion/event evidence under the binding rerun rule.

Therefore:

- target **0-7**;
- denominator **7-14**.

All seven known source false positives have clinically relevant pathology and remain CAN-U on the available actionability evidence. Any source-CCHD case that re-enters is likewise a clinically relevant structural diagnosis but lacks mapped Strict evidence -> CAN-U.

Thus:

- Strict **0**;
- Expanded **7-14**;
- Expanded proportion remains 100% across admissible mappings, but the analysis denominator/weight is not point-identifiable;
- **SENSITIVITY_ONLY — TARGET_LESIONS_UNAVAILABLE**.

This is a downgrade from `PRIMARY_POOLABLE`.

## E. d-TGA-trigger units promoted after the conditional pass

Batch 01 removed the former isolated/complex-TGA target uncertainty. Batch 02 confirms that no separate unresolved conditional component is needed to classify the d-TGA participants themselves. The following units now have point harmonized denominators and no remaining primary-pooling barrier:

### U_R006 — Meberg 2008

- d-TGA/TGA target11;
- other conditional/off-list cardiac diagnoses remain denominator because no qualifying <=28-day event is documented;
- denominator **313**;
- Strict CAN-B **32**;
- CAN-U134;
- Expanded **166**;
- NON_CAN healthy transitional147;
- ascertainment100%;
- **PRIMARY_POOLABLE** (promoted from SENSITIVITY_ONLY).

### U_R008 — de-Wahl Granelli 2009

- amended unique target union11 after full patient-table TGA audit;
- denominator **77**;
- Strict42;
- CAN-U8;
- Expanded50;
- NON_CAN3;
- explicitly healthy24;
- ascertainment100%;
- **PRIMARY_POOLABLE** (promoted).

### U_R013 — Turska-Kmiec 2012

- conventional TGA3 + IAA1 + HLHS1 -> target5;
- explicit ccTGA remains denominator;
- conditional TAPVD/CoA/TOF/unspecified PA remain denominator where no qualifying event is established;
- denominator **24**;
- Strict0;
- Expanded15;
- NON_CAN9;
- ascertainment100%;
- **PRIMARY_POOLABLE** (promoted).

### U_R023 — Morocco 2020

- d-TGA1 + DORV/TGA/PS1 + HLHS2 -> target4;
- CoA+PDA remains denominator because <=28-day event is not documented;
- denominator **11**;
- sepsis2 -> CAN-A2;
- three noncritical surgical-follow-up lesions + returned CoA case -> CAN-B4;
- Strict **6**;
- PPHN1 -> CAN-U;
- Expanded **7**;
- NON_CAN2 + explicitly normal2;
- ascertainment100%;
- **PRIMARY_POOLABLE** (promoted).

### U_R036 — Arlettaz 2006

- HLHS3 + TGA2 -> target5;
- CoA/critical PS/PA+VSD remain denominator without qualifying <=28-day events; off-list structural lesions remain denominator;
- denominator **19**;
- Strict0;
- CAN-U18;
- Expanded18;
- UNKNOWN1;
- ascertainment **94.7%**;
- **PRIMARY_POOLABLE** (promoted).

## F. Pulmonary-atresia/anatomy uncertainties that remain real sensitivity bounds

No silent resolution is made where the primary source does not establish septal anatomy.

### U_R021 Panama

Complex right-heart case remains a differential of PA/IVS versus critical PS. If PA/IVS -> target; if critical PS without actual <=28-day event -> denominator. Target0-1, denominator15-16. Already SENSITIVITY_ONLY because of both target bound and low clinical ascertainment.

### U_R024 Gopalakrishnan

See D2 above. PA anatomy remains unresolved; downgraded to SENSITIVITY_ONLY.

### U_R068 Almawazini 2017

Primary report lists generic pulmonary atresia as a CCHD diagnosis but does not establish intact versus non-intact septum. The paper's general definition says PA/TAPVR are CCHD needing urgent intervention; this does not substitute for participant-level anatomy or actual <=28-day event under the review lock.

- definite target = HLHS2 + TGA1 =3;
- generic PA may add1 only if PA/IVS;
- denominator110-111;
- SENSITIVITY_ONLY remains.

### U_R135 Salih/Sattar Iraq

Generic pulmonary atresia x2 lacks septal anatomy. TGA2 + HLHS1 are definite target3; PA can raise target to5 only if PA/IVS. TOF/CoA/PS remain denominator without qualifying events. Target3-5, denominator95-97. SENSITIVITY_ONLY remains.

### U_NR002 Gamhewage Sri Lanka

Primary Tables 2-3 provide lesion-specific neonatal outcomes:

- HLHS4 + TGA1 unconditional;
- TAPVD deaths2 and pulmonary-atresia neonatal death1 satisfy the conditional/death route;
- surviving pulmonary-atresia cases x2 remain anatomy-dependent because septal anatomy is not given;
- TOF lacks a qualifying event.

Existing target8-11 / denominator8-11 bound remains an appropriate conservative representation. SENSITIVITY_ONLY remains.

### U_NR059 West Virginia

After Batch 01, TGA+VSD is removed through d-TGA. Generic PA anatomy remains unresolved; CoA/TAPVR lack documented <=28-day events; two final failed screens had no TTE. Target4-7 / denominator12-15 remains sensitivity-only.

### U_R125_GUADALAJARA_MX

TGA1 definite target; pulmonary valve atresia lacks septal anatomy and no actual <=28-day event is documented. Target1-2 / denominator4-5 remains SENSITIVITY_ONLY.

## G. Units where source-CCHD lesions are unavailable

The conditional rerun cannot manufacture lesion identities that the source does not report. These remain sensitivity/hold as already coded:

- U_R026 — source CCHD12 lesions unavailable -> target0-12 / denominator19-31; SENSITIVITY_ONLY.
- U_R032 — source CCHD15 lesions unavailable + two pre-echo deaths -> harmonized denominator not point-identifiable; SENSITIVITY_ONLY.
- U_R037 — CHD9 lesions unavailable -> target0-9 / denominator9-18; SENSITIVITY_ONLY.
- U_R042 — major CHD4 lesions unavailable -> target0-4 / denominator11-15; SENSITIVITY_ONLY.
- U_NR062 — five source cyanotic/CCHD lesions not participant-identifiable -> target0-5 / denominator2-7; SENSITIVITY_ONLY.
- U_R125_SONORA_MX — CCHD11 lesions unavailable plus 22-vs-21 source arithmetic inconsistency -> HOLD_PENDING_QA.
- U_R102 — 23 cardiac cases combine CCHD/significant CHD without lesion identities/exhaustive category structure -> HOLD_PENDING_QA.

These are genuine evidence limitations, not unresolved methodological rules.

## H. Provisional pool counts after Batch 02

Starting Snapshot R/S provisional classes:

- PRIMARY_POOLABLE26
- SENSITIVITY_ONLY42
- HOLD_PENDING_QA3
- NOT_POOLABLE5

Changes now justified:

**Promotions SENSITIVITY_ONLY -> PRIMARY_POOLABLE (5):**
- U_R006
- U_R008
- U_R013
- U_R023
- U_R036

**Downgrades PRIMARY_POOLABLE -> SENSITIVITY_ONLY (3):**
- U_R020
- U_R024
- U_R043

Therefore the post-target-rerun provisional classes are:

- **PRIMARY_POOLABLE = 28**
- **SENSITIVITY_ONLY = 40**
- **HOLD_PENDING_QA = 3**
- **NOT_POOLABLE = 5**
- total = **76**

These counts are **not yet declared the final Phase-5 freeze** because the three inherited HOLD_PENDING_QA units must receive one closing resolution attempt and an overlay dataset must be created from the post-rerun values.

## I. What Batch 02 establishes

The all-76 target rerun is now methodologically complete with respect to:

1. the amended d-TGA ontology;
2. conditional lesion event timing <=28 days;
3. PA/IVS versus PA/non-intact/unspecified anatomy;
4. explicit protection against using source `CCHD` labels as substitutes for the locked target;
5. explicit retention of evidence-bounded studies in sensitivity rather than forcing a point denominator.

Historical extraction blocks remain immutable audit history. Batch 01 + Batch 02 jointly define the post-Snapshot-S target overlay.

## Exact next movement

1. one final QA attempt on the three `HOLD_PENDING_QA` units;
2. create a structured post-rerun target/CAN overlay for every numerically changed unit;
3. recompute and freeze final PRIMARY_POOLABLE / SENSITIVITY_ONLY / NOT_POOLABLE/HOLD sets;
4. only then begin quantitative synthesis.
