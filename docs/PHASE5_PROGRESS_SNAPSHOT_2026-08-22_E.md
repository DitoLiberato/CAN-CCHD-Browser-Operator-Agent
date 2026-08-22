# CAN-CCHD Phase 5 — Progress Snapshot E

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT**

## Current state

Phase 5 continues exclusively from the 76 frozen unique quantitative units created at Phase 4.5 closure. No scientific value is imported from the legacy Browser Agent/database.

Twenty-three units have now been structurally extracted across Blocks 01-06.

## Current QA disposition

### PRIMARY_POOLABLE = 15

- U_R009
- U_R017
- U_R018
- U_R019
- U_R020
- U_R024
- U_R025
- U_R043
- U_R071
- U_R072
- U_R089
- U_R093
- U_R099
- U_R100
- U_R108

### SENSITIVITY_ONLY = 6

- U_R023 — Morocco; bounded harmonized denominator because conditional target timing is unavailable.
- U_R039 — Bradshaw; terminal ascertainment below 90%.
- U_R076 — Mohsin; mixed Well Baby/NICU plus non-point-identifiable target.
- U_R022 — Guatemala; 9/11 abnormal-echo infants have explicit cardiology follow-up but one normal echo lacks noncardiac outcome ascertainment and one infant was lost; ascertainment 81.8%.
- U_R034 — Denmark; pulmonary stenosis is a conditional target lesion without <=28-day intervention/death information; denominator 58-59 and Strict 42-43.
- U_R128 — southern Brazil; PFO/ASD findings NON_CAN, but two echo-normal infants lack noncardiac outcome ascertainment; ascertainment 80%.

### HOLD_PENDING_QA = 2

- U_R033 — Qatar; narrative/table internal inconsistency prevents defensible point denominator.
- U_R102 — Turkey/Sero; cardiac target and diagnostic-category exclusivity/exhaustiveness unresolved.

No new hold was created in Block 06.

## Block 06 additions

### U_R022 — Soto Torselli 2020, Guatemala
- 376 screened;
- 11 final fails;
- no harmonized CCHD;
- 10 echoes: 9 abnormal noncritical cardiac findings + 1 structurally normal;
- one infant lost before echo;
- explicit pediatric-cardiology outpatient follow-up after the abnormal findings -> CAN-B=9;
- normal echo not reclassified healthy;
- Strict=Expanded=9/11;
- UNKNOWN=2;
- ascertainment 81.8%;
- `SENSITIVITY_ONLY`.

### U_R034 — Havelund 2019, Denmark
- 2,855 screened;
- 59 final fails;
- median screen age 2.5 h;
- 16 assessment-only/no further treatment;
- 18 NICU observation until saturation normalized;
- 25 required treatment, including one pulmonary stenosis;
- pulmonary stenosis is conditional harmonized CCHD and <=28-day intervention/death is unreported;
- harmonized denominator 58-59;
- Strict=Expanded 42-43;
- 100% terminal classification within either admissible mapping;
- `SENSITIVITY_ONLY` because no single primary-analysis weight is defensible.

### U_R108 — Shah 2026, India
- 530 screened at 15 min and 6 h;
- 81 low at 15 min, 75 normalized by 6 h and are PASS;
- 6 persistent final fails;
- TGA with severe PAH mapped as simple TGA -> harmonized CCHD=1;
- tricuspid atresia lacks locked-target equivalence evidence -> remains denominator and CAN-U;
- 4 early PDA/PFO findings explicitly considered potentially physiologic/transitional -> NON_CAN;
- denominator=5;
- Strict=0/5;
- Expanded=1/5;
- `PRIMARY_POOLABLE`, with mandatory very-early-screening sensitivity flag.

### U_R128 — Witkowski et al. 2024, Brazil
- 5,667 asymptomatic >=35-week newborns;
- tests before 24 h excluded;
- 10 final positive screens;
- no screen-positive CCHD;
- PFO7 + incidental ostium-secundum IAC/ASD1 -> NON_CAN8 because no qualifying actionability consequence is documented;
- normal echo2 -> UNKNOWN2, not healthy;
- Strict=Expanded=0/10;
- terminal ascertainment 80%;
- `SENSITIVITY_ONLY`.

## Current counts

- Frozen Phase 5 units: **76**
- Structurally extracted: **23/76**
- QA-complete PRIMARY_POOLABLE: **15**
- SENSITIVITY_ONLY: **6**
- HOLD_PENDING_QA: **2**
- Not yet structurally extracted: **53**

## Operational Block count

Extraction Blocks are operational batches, not a protocol-defined unit. At the current working size of approximately four studies per Block, the 76 frozen units imply approximately **20 Blocks total**. After completion of Block 06, 53 units remain, corresponding to approximately 14 additional Blocks (Blocks 07-20), with the final Block likely smaller. Block size may be reduced when source QA requires deeper adjudication; this does not alter the Phase 5 protocol.

## Canonical Block 06 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_06.csv`
- `docs/PHASE5_EXTRACTION_BLOCK_06_AUDIT.md`

## Exact resume point

Proceed directly to Block 07 from the remaining 53 frozen units, continuing to apply:

1. locked harmonized CCHD lesion mapping;
2. final-failed-screen denominator;
3. Strict versus Expanded CAN-CCHD;
4. >=90% terminal ascertainment threshold;
5. no diagnosis-as-actionability inference;
6. normal echo is not healthy;
7. participant-level overlap control;
8. altitude, timing and setting heterogeneity flags.

This snapshot supersedes Snapshot D as the current safe resume point.
