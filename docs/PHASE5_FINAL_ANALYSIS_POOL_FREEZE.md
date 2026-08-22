# CAN-CCHD Phase 5 — Final Analysis Pool Freeze

Date: 2026-08-22
Branch: `phase5-extraction`
Status: **FROZEN AFTER ALL-76 TARGET RERUN / READY FOR QUANTITATIVE SYNTHESIS**

## 1. Scope

This document freezes the Phase 5 analysis-set membership after:

1. structural extraction of all 76 frozen quantitative units;
2. formal d-TGA target amendment;
3. systematic all-76 d-TGA/TGA/ccTGA rerun;
4. systematic conditional-lesion <=28-day death/surgery/catheter audit;
5. pulmonary-atresia anatomy audit;
6. final resolution attempt for all inherited HOLD_PENDING_QA units;
7. creation of the structured post-rerun numerical overlay.

No meta-analysis has been run before this freeze.

## 2. Binding artifact precedence

For Phase 5 scientific values, use the following precedence:

1. `docs/PHASE5_HARMONIZED_CCHD_TARGET_MAPPING_LOCK.md`
2. `docs/PHASE5_PROTOCOL_AMENDMENT_2026-08-22_D_TGA_TARGET_RULE.md`
3. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH01_TGA_SWEEP.md`
4. `docs/PHASE5_ALL76_TARGET_RERUN_BATCH02_CONDITIONAL_LESIONS.md`
5. `docs/PHASE5_FINAL_HOLD_RESOLUTION_ATTEMPT.md`
6. `data/phase5/PHASE5_POST_RERUN_NUMERIC_OVERLAY_v0.1.csv`
7. historical Phase 5 extraction blocks for units not changed by the rerun.

Historical block CSVs and Snapshots R/S remain immutable provenance records. When an affected unit appears in the numeric overlay, the overlay supersedes its historical target/denominator/CAN values for the amended primary analysis.

The original Cochrane-literal simple-TGA mapping remains preserved as the pre-amendment sensitivity framework.

## 3. Final membership reconciliation

| Analysis class | n |
|---|---:|
| PRIMARY_POOLABLE | **28** |
| SENSITIVITY_ONLY | **40** |
| HOLD_PENDING_QA | **3** |
| NOT_POOLABLE | **5** |
| **Total** | **76** |

The four classes are mutually exclusive and collectively exhaustive across the 76 frozen quantitative extraction units.

## 4. PRIMARY_POOLABLE — frozen n=28

These units have a point-identifiable harmonized-CCHD-negative final-failed-screen denominator, a point Strict CAN-CCHD numerator, adequate terminal classification for the principal estimand, and no remaining structural exclusion from primary pooling.

1. U_R006 — Meberg 2008
2. U_R008 — de-Wahl Granelli 2009
3. U_R009 — Riede 2010
4. U_R010 — Ewer 2011
5. U_R013 — Turska-Kmiec 2012
6. U_R017 — Jawin 2015
7. U_R018 — Özalkaya 2016
8. U_R019 — South Africa / source R019
9. U_R023 — Morocco 2020
10. U_R025 — Colombia / source R025
11. U_R031 — Jordan / Abu Lehyah 2025
12. U_R036 — Arlettaz 2006
13. U_R049 — Hamilcikan 2018
14. U_R066 — Jones / Northwick Park
15. U_R067 — Klausner
16. U_R071 — Cubells 2018
17. U_R072 — Diller 2018
18. U_R089 — Johnson / Boston
19. U_R093 — Cawsey / Birmingham homebirth
20. U_R099 — Tekleab / Ethiopia
21. U_R100 — Cloete / New Zealand
22. U_R101 — Singh & Chen / Cambridge
23. U_R108 — India / source R108
24. U_R109 — Yogyakarta
25. U_R125_BARRANQUILLA_CO — SIBEN Barranquilla site
26. U_R125_ROSARIO_AR — SIBEN Rosario site
27. U_NR044 — Bangalore / Kumar 2017
28. U_NR058 — Hyderabad / Reddy

### Membership changes caused by the final rerun

Promoted from SENSITIVITY_ONLY to PRIMARY_POOLABLE:

- U_R006
- U_R008
- U_R013
- U_R023
- U_R036

Downgraded from PRIMARY_POOLABLE to SENSITIVITY_ONLY:

- U_R020 POLAR
- U_R024 Gopalakrishnan
- U_R043 Oakley

Net change versus Snapshot R/S: primary pool **26 -> 28**.

## 5. SENSITIVITY_ONLY — frozen n=40

These units remain quantitatively informative but are excluded from the principal pool because of one or more prespecified limitations such as mixed/NICU setting, <90% ascertainment, non-point target mapping, denominator convention, very incomplete clinical classification, or other structural heterogeneity.

1. U_R002
2. U_R007
3. U_R015
4. U_R020 — POLAR; five source-CCHD lesions unavailable -> target bound
5. U_R021
6. U_R022
7. U_R024 — Gopalakrishnan; generic PA anatomy unresolved
8. U_R026
9. U_R029
10. U_R030
11. U_R032
12. U_R034
13. U_R035
14. U_R037
15. U_R039
16. U_R041
17. U_R042
18. U_R043 — Oakley; seven source-CCHD lesions unavailable -> target bound
19. U_R053
20. U_R068
21. U_R069
22. U_R076
23. U_R077
24. U_R086
25. U_R087
26. U_R104
27. U_R126
28. U_R127
29. U_R128
30. U_R130
31. U_R135
32. U_NR002
33. U_NR007
34. U_NR008
35. U_NR050
36. U_NR059
37. U_NR062
38. U_NR064
39. U_R125_SAN_LUIS_AR
40. U_R125_GUADALAJARA_MX

`SENSITIVITY_ONLY` does not mean scientifically discarded. These units must remain available for prespecified robustness, setting/timing/altitude, missingness, and target-definition analyses where their data structure permits.

## 6. HOLD_PENDING_QA — frozen unresolved n=3

The final source-resolution attempt did not produce enough evidence to release these units. Their hold is now treated as a closed evidence limitation, not an active extraction queue.

1. **U_R033 Qatar** — source internal inconsistency: narrative 8 CCHD +26 false positives cannot be reconciled with Table 2 POCC distribution; four narrative cardiac cases cannot be lesion-mapped.
2. **U_R102 Turkey 2025** — cardiac lesions unavailable and 301 positive-screen flow not exhaustively/mutually exclusively reconstructable from accessible primary evidence.
3. **U_R125_SONORA_MX** — 22 positives but published diagnostic subtotal11 CCHD +8 PPHN +2 sepsis =21; source-CCHD lesions unavailable.

No primary meta-analysis weight may be assigned to these three units under the current evidence freeze.

## 7. NOT_POOLABLE — frozen n=5

1. **U_R001 Richmond** — terminal failed-screen denominator not reproducible because implemented repeat pathway diverges from stated protocol.
2. **U_R003 Reich** — terminal pulse-positive denominator and linked management outcomes cannot be reconstructed from the primary report.
3. **U_R105 Wardha** — final-failed-screen denominator not separable from repeat-normalized infants plus internal cardiac arithmetic conflict; mixed ward/NICU cohort.
4. **U_NR009 Tekgündüz 2021** — combined pulse-oximetry + perfusion-index positivity cannot be isolated as the review's POX final-failed-screen denominator.
5. **U_BIRMINGHAM_R027_MAIN** — outcome-selected admitted-positive subcohort; full final failed-screen denominator is absent.

These units may be used descriptively/contextually where useful but cannot contribute a CAN-CCHD proportion weight.

## 8. Principal estimands frozen for synthesis

For each PRIMARY_POOLABLE unit:

### Strict primary outcome

`Strict CAN-CCHD / harmonized-CCHD-negative final failed screens`

where:

`Strict CAN-CCHD = CAN-A + CAN-B + CAN-AB`.

### Expanded outcome

`Expanded CAN-CCHD / harmonized-CCHD-negative final failed screens`

where:

`Expanded CAN-CCHD = Strict + CAN-U`.

The Strict outcome remains the principal actionable endpoint. Expanded is an explicitly broader clinically relevant-diagnosis analysis.

## 9. Target sensitivity framework

The final quantitative synthesis must preserve both:

1. **Primary amended mapping** — d-TGA is unconditional target whether simple or complex/associated; unqualified neonatal TGA maps to d-TGA unless corrected/l-TGA evidence exists.
2. **Pre-amendment sensitivity mapping** — original Cochrane-literal simple-TGA rule represented by the historical extraction/Snapshot R values.

Any change in pooled effect attributable to the d-TGA amendment must be reported.

## 10. Other prespecified robustness dimensions retained

Pool membership does not erase heterogeneity metadata. Quantitative synthesis should retain, where data permit:

- screening timing: very early / <24 h / post-24 h / mixed;
- setting: well-baby versus community/homebirth versus mixed/high-acuity;
- altitude;
- program/site clustering;
- ascertainment threshold and missingness;
- source algorithm/denominator convention;
- d-TGA target-definition sensitivity;
- Strict versus Expanded CAN outcome.

R125 multisite units remain separate site-level quantitative units but share the `R125_SIBEN_2020` program/report cluster and must be available for cluster-aware robustness analysis rather than treated as unrelated publications.

## 11. Phase 5 closeout conclusion

Phase 5 is now frozen with:

- **76/76 structurally extracted**;
- **76/76 rerun under the amended d-TGA policy**;
- **76/76 audited for conditional <=28-day target logic**;
- **28 PRIMARY_POOLABLE**;
- **40 SENSITIVITY_ONLY**;
- **3 unresolved HOLD_PENDING_QA**;
- **5 NOT_POOLABLE**;
- a structured post-rerun numerical overlay for every changed unit;
- historical pre-amendment values preserved for sensitivity analysis.

**Next phase: quantitative synthesis / meta-analysis.**
