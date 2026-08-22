# CAN-CCHD Phase 5 — Extraction Block 10 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 10 COMPLETE / QA-CLOSED**

## Scope

Block 10 contains four frozen Phase 4.5 quantitative units:

- `U_R029` — Tsao 2023, Taipei extended program
- `U_R030` — Pico Mawyin 2025, Ecuador
- `U_R053` — Yao 2026, Ghana
- `U_R125_SAN_LUIS_AR` — SIBEN San Luis, Argentina

All values come from restart-native records or independently reverified primary/full-text sources. The legacy Browser Agent/database was not used.

Binding rules applied:

1. final failed screen is the analytic event;
2. the locked harmonized CCHD target overrides source labels;
3. conditional lesions require participant/category-level <=28-day death/surgery/catheterization evidence;
4. diagnosis alone is not Strict actionability;
5. normal echo is not healthy;
6. >=90% terminal ascertainment is required for the principal fully classified pool;
7. mixed nursery/NICU settings are sensitivity-only when inseparable;
8. management without an etiologic diagnosis is preserved but not automatically converted into a CAN diagnosis.

---

## U_R029 — Taipei extended program

Primary: Tsao PC et al. *Comparing Strategies for Critical Congenital Heart Disease Newborn Screening.* Pediatrics. 2023;151(3):e2022057862. PMID 36815269. DOI 10.1542/peds.2022-057862.

### Flow and independence

- Extended program: 1 April 2014 through 30 June 2017.
- 30 birthing facilities.
- 93,058 screened after prenatal-suspicion exclusion in the main cohort.
- 156 received a failed assessment/referral.
- R077 pilot ended 31 March 2014; therefore R077 and R029 are sequential/non-overlapping but share `program_cluster_id=TAIPEI_POX_PROGRAM`.

### Source-defined false-positive subset

The paper reports 114 source-defined CCHD false positives with a complete aggregate distribution:

- respiratory problems 58;
- other CHD 41;
- sepsis 2;
- other noncardiac diagnoses 3;
- no abnormal finding/disease 10.

Thus 63/114 are explicitly noncardiac illnesses. The discussion describes such secondary targets as clinically significant and associated with early intervention in general, but does not link qualifying treatment/escalation/disposition/follow-up consequences to these 63 cases sufficiently for Strict coding.

Coding within this source-defined subset:

- Strict = 0 on recovered case-linked evidence;
- CAN-U lower bound = 63;
- explicit no disease = 10;
- the 41 `other CHD` cases cannot be forced into CAN-U versus NON_CAN without lesion-level detail.

### Harmonized target problem

The source CCHD table provides aggregate diagnosis counts across 42 cases and states that six cases had >=2 CCHD diagnoses. Diagnoses include HLHS, PA/IVS, TGA, TOF, TAPVR, CoA, DORV, Ebstein and tricuspid atresia.

HLHS and PA/IVS are unconditional harmonized lesions. However, aggregate diagnosis counts do not reveal unique participant-level combinations for the six multi-diagnosis cases. TGA simplicity and conditional-lesion <=28-day qualifiers are not available at participant level.

Therefore a unique harmonized CCHD count and harmonized-CCHD-negative denominator cannot be reconstructed reproducibly.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

Use the source-defined 114-infant CCHD-negative subset only for sensitivity/descriptive analyses. Do not assign a primary harmonized weight.

---

## U_R030 — Pico Mawyin 2025, Ecuador

Primary: Pico Mawyin T et al. *La pulsioximetría como estrategia de tamizaje de las cardiopatías congénitas.* Horizonte Medico. 2025;25(1):e3068. DOI 10.24265/horizmed.2025.v25n1.02.

Duplicate/companion: 2024 RCCSH publication with the same N=4,897 and same 626 positives; no additional weight.

### Flow

- 4,897 term rooming-in newborns considered healthy at entry.
- 626 final reported positive screens.
- 497 had an echocardiographic diagnosis.
- 129 were echo-negative.

The diagnostic table reconciles exactly:

- PDA 127;
- VSD 34;
- ASD 25;
- secondary pulmonary hypertension 23;
- PFO 272;
- aortic aneurysm 4;
- coarctation 8;
- rhythm disorders 4;
- total diagnosed = 497.

### Harmonized target

No listed diagnosis is unconditional harmonized CCHD.

- CoA8 is conditional and no <=28-day intervention/death qualifier is reported.
- Aortic aneurysm is not a locked target lesion.

Therefore:

- harmonized CCHD = 0;
- harmonized denominator = 626.

### CAN coding

No diagnosis-specific treatment/escalation/disposition/follow-up consequence is documented.

- CAN-U = 39: secondary PH23 + CoA8 + aortic aneurysm4 + rhythm disorders4.
- NON_CAN aggregate = 458: PFO272 + early PDA127 + VSD34 + ASD25, none with qualifying hemodynamic/actionability evidence.
- UNKNOWN = 129 echo-negative infants; normal echo is not global health.
- Strict = 0/626.
- Expanded = 39/626.
- terminal ascertainment = 497/626 = 79.4%.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

Reason: exact denominator but ascertainment below the locked >=90% principal threshold. Transitional-period screening remains a heterogeneity flag.

---

## U_R053 — Yao 2026, Ghana

Primary: Yao NA et al. *A pilot implementation study to detect neonatal critical congenital heart disease using pulse oximetry screening in Accra, Ghana.* BMJ Glob Health. 2026;11(1):e022157. PMID 41605545; PMCID PMC12853520; DOI 10.1136/bmjgh-2025-022157.

R053 and NR048 are one Ghana cohort; the companion creates no additional weight.

### Population and flow

- 5,725 screened of 5,981 eligible infants.
- 74% screened before 24 h.
- Population included NICU infants if they were not receiving supplemental oxygen; mixed setting is inseparable.
- 29 final failed screens.
- Two infants died before echocardiography.
- 27 were imaged: source critical CHD9 + noncritical CHD10 + false positives8.

### Harmonized target

Participant-level lesions are available for the 19 CHD cases.

Only two are definite harmonized CCHD under the locked target:

- standalone TGA (case 3);
- HLHS (case 8).

Other source-critical lesions are complex/not automatic or conditional without a <=28-day qualifier, including complex TGA, TOF/PS and tricuspid/other complex anatomy.

Thus among the 27 imaged infants:

- definite harmonized CCHD = 2;
- known harmonized-negative denominator = 25.

The two pre-echo deaths may be harmonized CCHD or CCHD-negative, so final harmonized denominator is bounded **25-27**, not point-identifiable.

### CAN coding

Within the 25 confirmed imaged harmonized-negative infants:

- 17 structural CHD cases re-enter/stay in denominator and are CAN-U because diagnosis is clinically relevant but qualifying actionability is not case-linked;
- among the 8 source false positives, the main article identifies myocarditis1 and PPHN1 -> CAN-U2;
- six false positives remain etiologically unclassified in the recovered main article.

Generic monitoring/stabilization while awaiting echo is not used to promote diagnoses to Strict.

Therefore:

- Strict = 0 across admissible mappings;
- CAN-U / Expanded lower bound = 19;
- UNKNOWN = 6 among confirmed denominator, rising to 8 if both pre-echo deaths are harmonized-negative;
- ascertainment = 19/25 to 19/27 = 76.0%-70.4%.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

Independent reasons: mixed well-baby/NICU setting, bounded denominator due pre-echo deaths, and ascertainment <90%.

---

## U_R125_SAN_LUIS_AR — SIBEN San Luis, Argentina

Primary: Sola A et al. *CCHD Screening Implementation Efforts in Latin American Countries by the Ibero American Society of Neonatology (SIBEN).* Int J Neonatal Screen. 2020;6(1):21. PMCID PMC7422978. DOI 10.3390/ijns6010021.

Program cluster: `R125_SIBEN_2020`.

### Source facts

- >1,400 infants screened during approximately six months of systematic implementation.
- 4 hypoxemic final-positive infants.
- none had CCHD.
- all required supplemental oxygen and had good outcomes.
- etiologic diagnoses are not reported.

### CAN coding

The Phase 4.5 site-level freeze explicitly warned that treatment alone must not be converted automatically into confirmed actionable **diagnoses**.

Accordingly:

- harmonized denominator = 4;
- Strict = 0 on the locked diagnosis endpoint;
- Expanded = 0 on the locked diagnosis endpoint;
- UNKNOWN = 4 because etiologic diagnoses are not reported;
- management-only evidence is preserved separately: oxygen treatment 4/4.

This is not equivalent to saying the infants were clinically unimportant. It means that the paper supports a broader `clinically consequential failed screen` endpoint but not an etiologic CAN-CCHD diagnosis numerator.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_MANAGEMENT_ONLY_SENSITIVITY.**

Retain for management-only/broader-consequence sensitivity analysis and cluster-aware analyses of R125 sites.

---

## Block 10 summary

| Unit | Status | Harmonized denominator | Strict | Expanded | Main reason |
|---|---|---:|---:|---:|---|
| U_R029 Taipei extended | SENSITIVITY_ONLY | not point-identifiable; source FP subset 114 | 0/114 on recovered linked evidence | >=63/114 source-defined subset | aggregate multi-diagnosis target mapping + setting |
| U_R030 Ecuador | SENSITIVITY_ONLY | 626 | 0 | 39 | ascertainment 79.4% |
| U_R053 Ghana | SENSITIVITY_ONLY | 25-27 | 0 | >=19 | mixed NICU + pre-echo deaths + missingness |
| U_R125_SAN_LUIS_AR | SENSITIVITY_ONLY | 4 | 0 | 0 | diagnosis not reported; management-only evidence 4/4 |

### Block-level effect

- new `PRIMARY_POOLABLE` = 0
- new `SENSITIVITY_ONLY` = 4
- new `HOLD_PENDING_QA` = 0

## Methodological signals reinforced

1. A large source-defined false-positive subset does not repair a non-identifiable harmonized denominator.
2. Aggregate CCHD diagnosis tables cannot be converted into participant-level target counts when multi-diagnosis cases are present.
3. Echo-negative infants remain UNKNOWN unless noncardiac outcome is established.
4. Early/transitional minor cardiac findings should not inflate Expanded CAN without consequence evidence.
5. Pre-echo deaths stay in the final-fail flow and create denominator bounds when CCHD status is unresolved.
6. Treatment without etiologic diagnosis is clinically meaningful but is not automatically a CAN-CCHD diagnosis.

Block 10 is QA-closed.
