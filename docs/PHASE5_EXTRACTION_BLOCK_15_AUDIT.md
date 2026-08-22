# CAN-CCHD Phase 5 — Extraction Block 15 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 15 COMPLETE / QA-CLOSED**

## Scope

Block 15 contains four frozen Phase 4.5 units:

- `U_R010` — Ewer/PulseOx 2011, United Kingdom; R011 HTA companion supplies detail but no independent weight.
- `U_R026` — Schwartz 2021, Maryland, United States.
- `U_NR002` — Gamhewage 2021, Sri Lanka.
- `U_NR044` — Kumar 2017, Bangalore, India.

R008 and R013 were initially considered for this block, but their exact restart-native bibliographic identities were not sufficiently recoverable from the accessible canonical artifacts without inference. They were therefore moved to the restart-native identity-reconciliation queue and replaced by NR002/NR044. No legacy source was consulted.

Binding Phase 5 rules applied:

1. final failed screen is defined by the protocol repeat sequence, not a downstream clinical label;
2. the harmonized Ewer/Cochrane lesion target governs the denominator;
3. complex TGA is not automatically simple TGA;
4. conditional lesions require the locked <=28-day event;
5. diagnosis/severity alone does not establish Strict actionability;
6. source labels such as CCHD/CCCHD do not override lesion-level mapping;
7. normal echo is not globally healthy;
8. diagnostic-label arithmetic is never repaired by guessing overlap;
9. >=90% ascertainment is required for the principal fully classified analysis.

---

## U_R010 — Ewer/PulseOx 2011

Primary report: Ewer AK et al. *Pulse oximetry screening for congenital heart defects in newborn infants (PulseOx): a test accuracy study.* Lancet. 2011;378:785–794. PMID 21820732. DOI 10.1016/S0140-6736(11)60753-8.

Companion detail report: PulseOx HTA publication, PMID 22284744. Companion only; no additional weight.

### Screening flow

- 20,055 asymptomatic newborns >34 weeks were screened across six UK maternity units.
- Median screening age was 12.4 h.
- Final positive screens = **195**.
- Source major CHD among final positives = 26:
  - critical CHD18;
  - serious CHD8.
- The authors' 169 `false positives` mean absence of *major* CHD, not absence of clinically important disease. They include:
  - significant CHD6;
  - respiratory/infective disease requiring intervention40;
  - residual true false positives123.

Thus the source categories reconcile 18 + 8 + 6 + 40 + 123 =195.

### Harmonized target reconstruction

The source critical definition/list is the direct ancestor of the review's locked Ewer/Cochrane target. Nevertheless, each participant still has to satisfy the exact lesion rule.

Among the 18 source-critical screen-positive cases, 17 qualify as harmonized CCHD. The exception is a reported **TGA + VSD** case: under the lock, only *simple* TGA is unconditional, and this complex TGA case has no separate locked target component establishing harmonized CCHD.

The pulmonary-atresia cases with AVSD/double-inlet-LV or VSD are treated as PA with non-intact septum/PA-VSD-type anatomy. Because the source classifies these individual cases as critical under a definition requiring death or intervention within 28 days, they satisfy the conditional rule.

Therefore:

- harmonized CCHD = **17**;
- harmonized-negative denominator = **178**.

### CAN coding

- Respiratory/infective disease requiring medical intervention40 -> `CAN-A40`.
- Significant CHD6 -> `CAN-B6`, because the source category itself entails continued monitoring after 6 months and/or drug treatment and these diagnoses were established through the failed-screen pathway.
- Serious CHD8 -> `CAN-U8`, not automatically Strict. The source establishes clinical relevance/intervention within the first year, but participant-level screening-attributable management is not separable and some major lesions had antenatal suspicion.
- Re-entered critical TGA+VSD1 -> `CAN-U1`; it is clinically important, but the accessible evidence does not establish a qualifying management consequence attributable to the screening pathway.
- Residual source true false positives123 -> `NON_CAN123`; the source explicitly states they lacked significant CHD or intercurrent illness requiring treatment.

Final:

- Strict = **46/178**;
- CAN-U = **9**;
- Expanded = **55/178**;
- NON_CAN =123;
- ascertainment =100%.

### QA correction during Block 15

A provisional reading initially counted all eight serious CHD cases as Strict and produced 54/178. That was rejected before freeze because source seriousness/intervention-by-one-year does not establish participant-level **screening-attributable** actionability. Final frozen Strict is **46/178**.

### Decision

**PRIMARY_POOLABLE / QA_COMPLETE.**

Early screening at a median 12.4 h remains a heterogeneity covariate.

---

## U_R026 — Schwartz 2021, Maryland

Primary report: Schwartz BN et al. *Newborn Pulse Oximetry Screening at a Community Hospital: An 8-Year Experience.* Pediatrics. 2021;148(3):e2020049847. PMID 34429338. DOI 10.1542/peds.2020-049847.

### Flow

- 64,780 infants were screened in the well-infant nursery.
- Final failed screens =31.
- All 31 were reported to have a disorder:
  - source CCHD12;
  - non-CCHD diagnoses requiring further follow-up9;
  - noncardiac disorders10.

### Target limitation

The individual lesions among the 12 source-CCHD cases are not available in the accessible primary material. A historical source CCHD label cannot be substituted for the locked target.

Consequently:

- harmonized CCHD can range from 0 to12;
- harmonized-negative denominator = **19–31**.

This is target uncertainty, not participant missingness: every failed screen has a source clinical category.

### CAN coding

- Nine non-CCHD cases explicitly requiring further follow-up -> `CAN-B9`.
- Ten noncardiac disorders -> `CAN-U10` because the accessible report does not link diagnosis-specific treatment/escalation/disposition consequences.
- Any of the 12 source-CCHD cases that re-enter the harmonized-negative denominator are clinically relevant and add to CAN-U.

Therefore:

- Strict = **9** throughout;
- CAN-U =10–22;
- Expanded = **19–31**, equal to the admissible denominator;
- ascertainment =100% at source diagnostic-category level.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY** because the locked denominator is not point-identifiable.

---

## U_NR002 — Gamhewage 2021, Sri Lanka

Primary report: Gamhewage NC, Perera KSY, Weerasekera M. *Effectiveness of newborn pulse oximetry screening for the identification of critical congenital heart disease in a tertiary care hospital in Sri Lanka.* Sri Lanka J Child Health. 2021;50(4):699–703. DOI 10.4038/sljch.v50i4.9890.

### Population and flow

- 8,964 live births.
- Prenatal CHD and NICU admission before screening were excluded.
- 8,718 healthy term newborns were screened at 24–48 h.
- Final positives =19.
- Echo showed CHD18 and normal cardiac anatomy1.
- Source CCHD14:
  - TAPVD3;
  - pulmonary atresia3;
  - HLHS4;
  - AV canal1;
  - truncus1;
  - TOF1;
  - TGA1.
- Noncritical CHD4 included ASD/PDA-type diagnoses.

### Locked target mapping

Definite/qualified target cases:

- HLHS4;
- standalone TGA1;
- TAPVD2 with documented neonatal death;
- pulmonary atresia1 with documented neonatal death.

Thus at least8 harmonized CCHD are established.

Uncertainty remains for:

- third TAPVD without a documented qualifying <=28-day event;
- two surviving pulmonary-atresia cases with unspecified septal anatomy;
- TOF without a qualifying event;
- AV canal/truncus, which are not automatic target lesions.

Accordingly:

- harmonized CCHD = **8–11**;
- harmonized-negative denominator = **8–11**.

### CAN coding

The 3–6 source-CCHD infants who re-enter the denominator are covered by an explicit management pathway that included emergency surgery where indicated, follow-up toward elective surgery, and palliative/comfort care. Exact acute-versus-follow-up subtype cannot be separated -> `CAN-AB3–6`.

The four noncritical CHD cases lack case-specific qualifying management linkage -> `CAN-U4`.

The one normal echo has no noncardiac outcome ascertainment -> `UNKNOWN1`.

Therefore:

- Strict =3–6;
- Expanded =7–10;
- ascertainment =7/8 to10/11 = **87.5%–90.9%**.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

The unit crosses the 90% ascertainment boundary depending target mapping and lacks a single denominator weight.

---

## U_NR044 — Kumar 2017, Bangalore

Primary report: Kumar RK, Shenoi A, Yerur KV, Tajamul S, Kini P. *Routine Pulse Oximetry Screening to Detect Critical Cyanotic Congenital Heart Disease in Neonates After Birth – A Developing Country Perspective & Experience.* Neonatology Today. 2017;12(6).

### Population and flow

- Four tertiary maternity hospitals in Bangalore.
- Well newborns >36 weeks staying with their mothers; NICU admission excluded.
- 22,601 screened.
- Final persistent failed screens =14.
- Three had pulmonary disease requiring treatment:
  - PPHN1;
  - TTN1;
  - congenital pneumonia with sepsis1.
- Eleven underwent echo:
  - PDA only1;
  - VSD + small PDA1;
  - remaining nine participants labelled by the authors as CCCHD.

### Source diagnostic-label QA

The diagnoses reported for the authors' nine-case CCCHD group are:

- TGA3;
- TAPVD2;
- TOF1;
- VSD+ASD+PFO with PH1;
- severe PH1;
- pulmonary stenosis2.

These diagnostic labels sum to **10**, despite a nine-participant group. This is preserved as source overlap/count inconsistency. Phase 5 does not guess which diagnoses overlap.

Crucially, this does **not** prevent participant-level CAN classification.

### Harmonized target and CAN classes

- Standalone TGA3 -> definite harmonized CCHD, removed.
- Six remaining participants from the authors' nine-case group have clinically relevant TAPVD/TOF/PS/PH/septal-combination diagnoses, but no locked <=28-day qualifying event is documented for the conditional lesions -> `CAN-U6`.
- The three pulmonary-condition infants requiring treatment -> `CAN-A3`.
- PDA only1 and VSD+small PDA1 without qualifying consequence -> `NON_CAN2`.

Thus:

- harmonized CCHD =3;
- denominator = **11**;
- Strict = **3/11**;
- Expanded = **9/11**;
- NON_CAN2;
- ascertainment =100%.

The denominator reconciliation is participant-based: 3 actionable pulmonary +6 clinically relevant re-entered cardiac +2 minor/nonactionable =11. No diagnostic-label overlap is invented.

### Decision

**PRIMARY_POOLABLE / QA_COMPLETE.**

---

## Block 15 summary

| Unit | Status | Harmonized denominator | Strict | Expanded | Key limitation/strength |
|---|---|---:|---:|---:|---|
| U_R010 PulseOx | PRIMARY_POOLABLE | 178 | 46 | 55 | exact lesion/participant reconstruction, 100% ascertainment |
| U_R026 Maryland | SENSITIVITY_ONLY | 19–31 | 9 | 19–31 | source-CCHD lesions unavailable |
| U_NR002 Sri Lanka | SENSITIVITY_ONLY | 8–11 | 3–6 | 7–10 | PA anatomy/conditional-event mapping + one echo-normal unknown |
| U_NR044 Bangalore | PRIMARY_POOLABLE | 11 | 3 | 9 | participant classes exact despite source lesion-label overlap |

Block effect:

- new `PRIMARY_POOLABLE` =2;
- new `SENSITIVITY_ONLY` =2;
- new `HOLD_PENDING_QA` =0;
- new `NOT_POOLABLE` =0.

## Methodological conclusions reinforced

1. A source `false positive` definition based on absence of major CHD must not replace the review's harmonized denominator.
2. Even an exact source target definition still requires complex-anatomy adjudication; TGA+VSD is not simple TGA.
3. Source clinical importance or future intervention does not automatically establish screening-attributable Strict actionability.
4. Missing lesion identities create target bounds even when every failed screen has a clinical diagnosis.
5. Neonatal death can satisfy the locked event component for conditional lesions when lesion identity is sufficiently reported.
6. Diagnostic-label overlap need not invalidate an estimate when participant-level analytic class sizes are independently exact.
7. Normal echo remains UNKNOWN unless the noncardiac outcome is ascertained.
8. Companion reports can strengthen provenance but never add an independent weight.

Block 15 is QA-closed.