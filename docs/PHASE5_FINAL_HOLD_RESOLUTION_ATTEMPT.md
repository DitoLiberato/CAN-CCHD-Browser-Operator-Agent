# CAN-CCHD Phase 5 — Final Resolution Attempt for Remaining HOLD_PENDING_QA Units

Date: 2026-08-22
Branch: `phase5-extraction`
Status: **FINAL HOLD ATTEMPT COMPLETE / 3 HOLDS RETAINED**

## Purpose

After completion of the all-76 d-TGA and conditional-lesion rerun, make one final primary-source resolution attempt on the three inherited `HOLD_PENDING_QA` units before final pool freezing.

No hold may be cleared by arithmetic completion, clinical plausibility, secondary-source substitution, or treating source `CCHD` labels as harmonized target evidence.

## 1. U_R033 — Qatar / Abu Jarir et al. 2026

Primary open-access article rechecked in full.

### Stable source facts

- 68,150 live births;
- article reports 68,116 infants screened by POCC;
- 34 POCC-positive cases;
- narrative states **8 CCHD true positives + 26 false positives**;
- source PPV reported as 23.5%.

### Table 2 POCC column

The same article's Table 2 assigns the 34 POCC-detected cases as:

- d-TGA1;
- Ebstein anomaly1;
- HLHS1;
- PPHN28;
- TAPVR1;
- Non-CCHD2.

These table cells sum exactly to34, but they do **not** reconcile with the narrative 8-CCHD/26-false-positive split:

- the table visibly contains only four named cardiac-anomaly rows among POCC cases (d-TGA, Ebstein, HLHS, TAPVR);
- PPHN28 + Non-CCHD2 already account for30 cases, whereas the narrative states only26 false positives;
- four of the narrative eight CCHD cases are therefore not recoverable as lesion identities from the table;
- conversely, the table cannot be converted into the narrative 8/26 split without inventing or reassigning cases.

### Harmonized target implication

From the visible table alone:

- d-TGA1 -> unconditional target;
- HLHS1 -> unconditional target;
- TAPVR1 -> conditional and no participant-level <=28-day death/surgery/catheter event is reported;
- Ebstein1 -> not an automatic locked target.

But this does not solve the unit because the source itself says eight POCC CCHD cases while four are lesion-unidentified and the non-CCHD arithmetic conflicts.

### Final decision

**HOLD_PENDING_QA retained.**

Reason:

`PRIMARY_SOURCE_INTERNAL_INCONSISTENCY: narrative 8 CCHD + 26 FP versus Table2 4 named cardiac rows + 28 PPHN + 2 non-CCHD; four narrative cardiac cases cannot be lesion-mapped and false-positive arithmetic cannot be reconciled without invention.`

Primary source: Abu Jarir R et al. Cureus. 2026;18(3):e105810. PMID 41890244; PMCID PMC13014115; DOI 10.7759/cureus.105810.

## 2. U_R102 — Turkey / Şero et al. 2025

Primary publisher abstract and PubMed record rechecked. Full article text was not available for a complete participant/category audit in this final pass.

### Stable source facts

- 34,806 live births;
- 29,840 infants with documented POS results;
- 301 positive POS results;
- 23 reported jointly as `CCHD and significant congenital heart disease`;
- noncardiac diagnoses reported among failed screens:
  - sepsis101;
  - congenital pneumonia16;
  - polycythaemia32;
  - TTN52.

The four named noncardiac groups total201. Together with the 23 cardiac cases they account for224 of the301 positive screens, leaving77 not represented if the categories are interpreted as mutually exclusive/exhaustive.

The abstract does not state that these diagnosis groups are exhaustive or mutually exclusive, and it does not provide the 23 cardiac lesion identities.

### Harmonized target implication

- the 23 combined `CCHD + significant CHD` cannot be subtracted as a block under the harmonized lesion/event lock;
- the 201 named noncardiac diagnosis counts cannot be assumed mutually exclusive;
- the remaining77 cannot be labelled healthy, unknown, or any CAN class by subtraction;
- no exact harmonized denominator or CAN numerator is defensible from the accessible evidence.

### Final decision

**HOLD_PENDING_QA retained.**

Reason:

`CARDIAC_LESIONS_UNAVAILABLE + DIAGNOSTIC_CATEGORY_EXHAUSTIVENESS/EXCLUSIVITY_NOT_ESTABLISHED + 301 POSITIVE FLOW NOT RECONCILABLE FROM ACCESSIBLE PRIMARY REPORT.`

Primary source: Şero L, Tunçel D, Akdeniz O, Okur N. Klin Padiatr. 2025. DOI 10.1055/a-2695-8865. PMID 41101352.

## 3. U_R125_SONORA_MX — Sonora / SIBEN implementation report

Primary SIBEN implementation article and table rechecked.

### Stable source facts

- 9,181 apparently healthy newborns screened;
- 22 positive tests;
- published Sonora summary lists:
  - CCHD11;
  - PPHN8;
  - sepsis2.

The printed categories total **21**, not22.

No additional diagnosis/category for the 22nd positive is supplied in the accessible report. No individual lesion identities are supplied for the11 source-CCHD cases.

### Harmonized target implication

- any number0-11 of source-CCHD cases may satisfy the harmonized lesion/event target;
- target0-11;
- denominator11-22;
- PPHN8 + sepsis2 -> clinically relevant CAN-U10 on available management evidence;
- any source-CCHD case that re-enters the denominator is CAN-U, yielding CAN-U10-21;
- the one uncategorized positive remains UNKNOWN1;
- Strict remains0.

This bounded extraction is useful for sensitivity description but does not repair the source arithmetic or create a point analysis weight.

### Final decision

**HOLD_PENDING_QA retained.**

Reason:

`SOURCE_ARITHMETIC_NONRECONCILIATION: 22 positives versus 11+8+2=21 categorized cases; source-CCHD lesion identities unavailable.`

Primary source: Sola A et al. Int J Neonatal Screen. 2020;6(1):21. PMCID PMC7422978; DOI 10.3390/ijns6010021.

## Final hold state

After the final resolution attempt:

- U_R033 Qatar -> **HOLD_PENDING_QA**
- U_R102 Turkey 2025 -> **HOLD_PENDING_QA**
- U_R125_SONORA_MX -> **HOLD_PENDING_QA**

**HOLD_PENDING_QA = 3 remains unchanged.**

These holds are now closed as unresolved evidence limitations rather than active search tasks. They must not receive primary meta-analysis weights unless new primary-source information becomes available before analysis freeze.

## Next movement

Create the structured post-rerun overlay for all numerically changed units, reconcile the final 76-unit pool registry, and freeze Phase 5 analysis sets.
