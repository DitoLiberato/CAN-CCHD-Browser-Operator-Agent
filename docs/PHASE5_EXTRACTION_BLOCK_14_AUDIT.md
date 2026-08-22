# CAN-CCHD Phase 5 — Extraction Block 14 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 14 COMPLETE / QA-CLOSED**

## Scope

Block 14 contains four frozen Phase 4.5 quantitative units:

- `U_R101` — Singh & Chen 2022, Cambridge, United Kingdom
- `U_NR009` — Tekgündüz 2021, Erzurum, Turkey
- `U_NR059` — John et al. 2016, West Virginia, United States
- `U_BIRMINGHAM_R027_MAIN` — Henderson 2022 representative, with R014 Singh 2014 overlap-supporting only

All extraction obeys the restart legacy-data firewall. No legacy Browser Agent/database value was used.

Binding rules applied:

1. final failed screen is defined by completion of the source screening algorithm, not by later clinician reclassification;
2. harmonized CCHD mapping is lesion-specific;
3. source CCHD time windows broader than 28 days do not satisfy the locked conditional-lesion rule;
4. final failed infants without definitive evaluation remain in the flow;
5. combined-test positivity is not automatically a pulse-ox final-fail denominator;
6. outcome-selected subcohorts cannot estimate the CAN-CCHD proportion among all failed screens;
7. participant overlap in diagnostic groups must be explicitly reconciled before constructing CAN numerators;
8. detailed primary flow overrides abstract shorthand when the two differ.

---

## U_R101 — Singh & Chen 2022, Cambridge

Primary source: Singh Y, Chen SE. *Impact of pulse oximetry screening to detect congenital heart defects: 5 years’ experience in a UK regional neonatal unit.* Eur J Pediatr. 2022;181:813–821. PMID 34618229; PMCID PMC8821483; DOI 10.1007/s00431-021-04275-w.

### Population and screening sequence

- 27,170 births during the study period.
- 25,185 eligible newborns.
- 23,614 screened.
- Gestation >=35 weeks; antenatal CHD and NICU admission before 4 h excluded.
- Screening age 4–12 h.
- Abnormal first screen was repeated after 1–2 h in clinically well infants.
- The source protocol explicitly defines a persistent abnormality on the second screening measurement as a positive screen.

Flow:

- abnormal first screen = 1,393;
- normalized on protocol repeat = 1,033 -> PASS;
- persistent abnormality after the protocol repeat = **360 final failed screens**.

The article later reports that paediatrician assessment classified 171 of these 360 as clinically well with normal saturation and calls the remaining 189 `true positive`. That assessment is downstream evaluation after the protocol-positive screen; it is not another screening repeat. Therefore Phase 5 uses **360**, not 189, as the locked final-fail count.

This resolves the inherited R101 denominator-convention flag without arbitrary choice.

### Participant-level outcome reconstruction

Among the 189 downstream source `true positives`:

- 21 had cardiovascular abnormalities;
- 156 unique infants had significant noncardiac diagnoses requiring further intervention;
- 11 infants belonged to both groups.

Unique disease union:

`156 + 21 - 11 = 166 infants`.

The remaining 23 had brief respiratory symptoms / short antibiotic exposure but the source explicitly reports no significant pathology.

Among the 171 downstream clinician-reclassified infants:

- 169 remained clinically well without later diagnosis;
- 2 later had CHD detected through a murmur.

Thus all 360 final failures are terminally accounted for.

### Harmonized target mapping

The source reports six critical CHD:

- HLHS 1;
- hypoplastic aortic arch 1;
- interrupted aortic arch 1;
- coarctation 1;
- critical pulmonary stenosis 2.

Source critical status is defined by intervention or death within 28 days.

Review mapping:

- HLHS1 -> unconditional harmonized CCHD;
- IAA1 -> unconditional harmonized CCHD;
- CoA1 -> conditional lesion, but source critical definition establishes the <=28-day qualifier;
- critical PS2 -> conditional lesions, likewise qualified by source critical definition;
- isolated hypoplastic aortic arch -> not in the locked target and remains in the harmonized-negative denominator.

Harmonized CCHD = **5**.

Therefore:

`360 - 5 = 355 harmonized-CCHD-negative final failed screens`.

The only source CCHD among negative pulse-ox results was a critical CoA presenting in collapse at day 12. Consequently the two CHDs later discovered by murmur among the 171 downstream clinician-reclassified infants are not source critical CCHD and remain harmonized-negative.

### CAN-CCHD coding

The unique actionable union among the 189 is 166. Removing the five harmonized CCHD leaves:

- `CAN-AB = 161`.

This includes the non-target hypoplastic-aortic-arch case and other non-target CHD because the source documents intervention or required cardiology follow-up, and the significant noncardiac group explicitly required further intervention.

The two CHDs detected later by murmur are clinically relevant diagnoses but the failed-screen pathway did not produce the actionability:

- `CAN-U = 2`.

Other terminal categories:

- aggregate NON_CAN = 23;
- explicitly clinically well / no later diagnosis = 169.

Reconciliation:

`161 + 2 + 23 + 169 = 355`.

Final:

- Strict = **161/355**;
- Expanded = **163/355**;
- ascertainment = **100%**.

### Decision

**PRIMARY_POOLABLE / QA_COMPLETE.**

Important heterogeneity flag: very early screening at 4–12 h.

---

## U_NR009 — Tekgündüz 2021, Erzurum

Primary source: Tekgündüz KŞ et al. *Oxygen saturation and perfusion index screening in neonates at high altitudes: can PDA be predicted?* Eur J Pediatr. 2021;180(1):31–38. PMID 32504134; DOI 10.1007/s00431-020-03698-1.

### Source design

- 501 neonates >35 weeks.
- High-altitude setting, Erzurum.
- Screening at 24–48 h.
- The study evaluates **oxygen saturation together with peripheral perfusion index** as a combined screening strategy.
- Combined-screen positives = 21.
- No CCHD detected.
- PDA was present in 10 infants overall, nine of whom belonged to the combined-positive group.
- The other 12 combined-positive infants are not adequately clinically characterized in the accessible report.

### Why no CAN-CCHD effect is created

The accessible primary report does not separate which of the 21 combined positives were positive because of pulse oximetry versus perfusion index. The review denominator requires pulse-ox final failed screens.

Therefore:

- the 21 cannot be assumed to be POX final failures;
- a POX-specific harmonized denominator is not identifiable;
- the nine PDA findings would be NON_CAN absent a qualifying consequence if they were confirmed POX failures, but this conditional classification is not converted into a quantitative effect;
- 12 combined positives remain clinically uncharacterized.

### Decision

**NOT_POOLABLE / QA_COMPLETE_NOT_POOLABLE.**

Retain descriptively for high-altitude and PDA/perfusion-index context. This is a structural source limitation, not a pending QA problem.

---

## U_NR059 — John et al. 2016, West Virginia

Primary source: John C, Phillips J, Hamilton C, Lastliger A. *Implementing Universal Pulse Oximetry Screening in West Virginia: Findings from Year One.* W V Med J. 2016;112(4):42–46. PMID 27491102.

### Population and flow

- Statewide implementation in 28 birthing hospitals.
- Newborn nursery population; infants born in or admitted to NICU during the first 24 h were not eligible.
- Source used the CDC/DHHR screening algorithm.

A source-count discrepancy was resolved during Block 14:

- 19,283 infants were eligible / present in the program data frame;
- detailed flow reports **17,120 with an actual screening result**;
- 17,101 passed + 19 failed = 17,120.

The abstract uses 19,283 loosely as screened, but Phase 5 follows the detailed primary flow and records `total_screened = 17,120`.

Final failed screens = **19**.

- TTE available =17;
- no TTE =2.

### Raw cardiac diagnoses among the 17 evaluated failures

Source CCHD7:

- HLHS + TAPVR1;
- pulmonary atresia + hypoplastic pulmonary artery stenosis1;
- truncus + interrupted aortic arch1;
- critical CoA + VSD1;
- TAPVR1;
- HLHS1;
- TGA + VSD1.

Source non-CCHD findings include ASD, mild Ebstein anomaly, PDA, PPHN, VSD/PFO, pulmonary hypertension and PFO.

The source defines CCHD by surgery or catheter intervention within the **first year**, which is broader than the locked 28-day target.

### Harmonized target mapping

Definite harmonized CCHD among evaluated infants:

- HLHS-containing cases =2;
- IAA-containing truncus case =1.

Definite minimum = **3**.

Uncertainties:

- pulmonary atresia does not report septal anatomy; if PA/IVS it is unconditional CCHD;
- critical CoA lacks a documented <=28-day event under the source's first-year definition;
- TAPVR lacks a documented <=28-day event;
- TGA+VSD is not simple TGA;
- the two failed infants without TTE can themselves be harmonized CCHD or harmonized-negative.

Thus:

- harmonized CCHD = **3–6**;
- harmonized-negative denominator = **13–16**.

### CAN-CCHD coding

No qualifying treatment/escalation/disposition/follow-up consequence is linked to the CCHD-negative diagnoses in the primary report.

Clinically relevant diagnoses therefore remain CAN-U:

- mild Ebstein;
- PPHN;
- pulmonary hypertension;
- re-entered CoA;
- re-entered TAPVR;
- TGA+VSD;
- pulmonary atresia if it remains harmonized-negative.

Therefore:

- Strict = **0** throughout;
- CAN-U / Expanded = **6–7**;
- NON_CAN =7;
- UNKNOWN =0–2 depending the harmonized status of the two no-TTE failures;
- denominator =13–16;
- ascertainment across admissible mappings = approximately **86.7%–100%**.

### Decision

**SENSITIVITY_ONLY / QA_COMPLETE_SENSITIVITY_ONLY.**

The well-baby setting is appropriate, but the target mapping and two no-TTE final failures prevent a single principal weight.

---

## U_BIRMINGHAM_R027_MAIN — Henderson 2022 with R014 overlap support

Representative primary source: Henderson A et al. *Temporal trends in routine predischarge pulse oximetry screening: 6 years’ experience in a UK regional neonatal unit.* Arch Dis Child Fetal Neonatal Ed. 2022;107(3):256–261. PMID 34686534; DOI 10.1136/archdischild-2021-322303.

R014 Singh 2014 remains supporting only because of April–July 2013 participant-period overlap. Counts from R014 and R027 are never summed.

### Critical denominator-selection issue

The routine program screened eligible babies >34 weeks and excluded infants already admitted to the neonatal unit before screening.

However, the research cohort was assembled from the neonatal-unit database after the positive screen:

- all test-positive babies were clinically reviewed;
- **only babies requiring further investigation or treatment were admitted**;
- the study identified and analysed the positive-screen infants who were admitted because of the positive result.

Thus the published 253 infants are not all final failed screens. They are an **outcome-selected admitted positive-screen subcohort**.

The number and outcomes of positive-screen babies reviewed but not admitted are not enumerated. The full final-failed-screen denominator required by CAN-CCHD therefore cannot be recovered.

### Admitted-subset information

Within the selected admitted subset:

- admitted positives =253;
- CCHD =8;
- serious CHD =9;
- significant CHD =5;
- other significant diagnosis =225;
- transitional/no pathological diagnosis =6;
- 247/253 had a significant condition requiring treatment;
- 239/253 received supplemental oxygen.

The source uses the exact Ewer/PulseOx CCHD lesion/timeframe definition locked by this review. Therefore in the selected admitted subset:

- harmonized CCHD =8;
- admitted harmonized-negative subset =245;
- Strict CAN-CCHD within that selected subset =239;
- NON_CAN =6.

Descriptive yield:

`239/245`.

This number must **never** be used as the CAN-CCHD proportion among all failed screens because inclusion in the study cohort depended on the need for investigation/treatment — closely aligned with the review outcome itself.

### PDF provenance note

The primary author-proof PDF was independently reverified. As required for PDF analysis, screenshot retrieval was attempted repeatedly. The web source returned cache-miss/content-type failures, so no screenshot could be obtained; machine-readable primary PDF text was available. The failed screenshot attempts are preserved as a provenance limitation rather than represented as successful visual verification.

### Decision

**NOT_POOLABLE / QA_COMPLETE_NOT_POOLABLE.**

Retain as high-value descriptive evidence that admitted positive screens commonly represented clinically consequential disease, and retain R014 as overlap-supporting/sensitivity-replacement context only.

---

## Block 14 summary

| Unit | Status | Harmonized denominator | Strict | Expanded | Main reason |
|---|---|---:|---:|---:|---|
| U_R101 Cambridge | PRIMARY_POOLABLE | 355 | 161 | 163 | protocol final-fail flow and full participant accounting resolved |
| U_NR009 Erzurum | NOT_POOLABLE | not POX-isolatable | — | — | combined POX+perfusion-index positives not separable |
| U_NR059 West Virginia | SENSITIVITY_ONLY | 13–16 | 0 | 6–7 | target bounds + 2 no-TTE failures |
| U_BIRMINGHAM_R027_MAIN | NOT_POOLABLE | full denominator unavailable | — | — | outcome-selected admitted positive-screen subcohort |

Block-level effect:

- new `PRIMARY_POOLABLE` =1;
- new `SENSITIVITY_ONLY` =1;
- new `NOT_POOLABLE` =2;
- new unresolved holds =0.

## Methodological conclusions reinforced

1. The protocol-defined repeat sequence governs final-fail status; a later clinical reclassification cannot redefine screening positivity.
2. Overlapping disease groups can be reconciled only when participant overlap is explicitly reported: Cambridge uses `156 + 21 - 11 = 166` unique actionable infants.
3. A source's <=28-day critical definition can satisfy the conditional timing rule only for lesions included in the locked target; off-list lesions still re-enter.
4. Combined POX + perfusion-index positivity is not a POX final-fail denominator unless the tests are separable.
5. A source first-year CCHD definition does not establish the locked <=28-day criterion.
6. Final failed screens without TTE remain in the analytic flow.
7. An outcome-selected admitted positive subgroup cannot estimate a disease/actionability proportion among all failed screens even when its internal classification is excellent.
8. R014/R027 overlap remains represented by one main quantitative unit; no double counting.
9. Detailed primary flow overrides abstract shorthand when source counts differ.
10. PDF screenshot failures are documented transparently and do not become invented visual verification.

Block 14 is QA-closed.