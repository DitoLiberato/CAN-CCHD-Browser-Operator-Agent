# CAN-CCHD Phase 5 — Progress Snapshot P

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER BLOCK 17**

## Binding state

Phase5 remains derived exclusively from the76 frozen Phase4.5 quantitative units. The restart legacy-data firewall remains binding. No legacy app/database source may resolve identity, eligibility, denominator, numerator, diagnosis, target mapping, actionability, overlap, PRISMA count or analysis weight.

## Current counts

After Blocks01–17:

- frozen units: **76**
- structurally extracted: **65/76**
- PRIMARY_POOLABLE: **24**
- SENSITIVITY_ONLY: **35**
- HOLD_PENDING_QA: **3**
- NOT_POOLABLE: **3**
- unextracted: **11**

Poolability remains provisional until complete extraction and final harmonized-target adjudication.

## Block17 additions

### U_R125_BARRANQUILLA_CO

- SIBEN Barranquilla, Colombia;
- 9241 screened;
- 38 positive;
- source rows reconcile exactly to38;
- no reported lesion is automatically removable under the locked target from available evidence;
- denominator38;
- CAN-U18;
- NON_CAN20;
- Strict0/38;
- Expanded18/38;
- ascertainment100%;
- PRIMARY_POOLABLE / QA_COMPLETE.

### U_R125_SONORA_MX

- SIBEN Sonora, Mexico;
- 9181 screened;
- 22 positive;
- direct source summary gives CCHD11 + PPHN8 + sepsis2 =21;
- earlier Phase4 shorthand incorrectly stated that categories summed24; direct source recheck corrects the subtotal but not the underlying nonreconciliation;
- lesion identities for CCHD11 unavailable;
- harmonized CCHD0–11;
- denominator11–22;
- Strict0;
- CAN-U10–21;
- UNKNOWN1;
- Expanded10–21;
- HOLD_PENDING_QA retained.

## Identity-governance correction

R036 and R037 were previously described in Snapshot O as directly identified. Block17 verification found that the accessible canonical restart-native artifacts preserve only their IDs and generic `standard extraction` notes, not exact bibliographic identities sufficient for safe primary-source linkage.

They were not extracted and were moved to the identity-reconciliation queue.

## Remaining unextracted frozen units =11

- U_R001
- U_R002
- U_R003
- U_R006
- U_R008
- U_R013
- U_R036
- U_R037
- U_R042
- U_R066
- U_R067

Every remaining unit therefore requires restart-native bibliographic reconstruction before extraction. Legacy lookup is prohibited.

## Current PRIMARY_POOLABLE =24

U_R009, U_R010, U_R017, U_R018, U_R019, U_R020, U_R024, U_R025, U_R031, U_R043, U_R049, U_R071, U_R072, U_R089, U_R093, U_R099, U_R100, U_R101, U_R108, U_R109, U_R125_BARRANQUILLA_CO, U_R125_ROSARIO_AR, U_NR044, U_NR058.

## Current HOLD_PENDING_QA =3

- U_R033 — Qatar internal narrative/table inconsistency.
- U_R102 — Turkey2025 category/target/exclusivity unresolved.
- U_R125_SONORA_MX — 22 positives vs21 categorized cases plus source-CCHD lesion identities unavailable.

## Current NOT_POOLABLE =3

- U_R105 — final-fail denominator unreconstructable.
- U_NR009 — combined SpO2/perfusion-index positivity not POX-separable.
- U_BIRMINGHAM_R027_MAIN — outcome-selected admitted-positive subcohort; full final-positive denominator absent.

## Deferred d-TGA/simple-TGA discussion

Per user instruction, the substantive d-TGA/simple-TGA policy question will be discussed **after all remaining identities are reconstructed and all76 units are structurally extracted**. Until then:

- affected units remain provisional;
- no final target-audit freeze is declared;
- no final primary meta-analysis is run;
- existing strict/simple-TGA flags remain visible rather than silently amended.

The broader conditional-lesion audit (TAPVR/TAPVC, pulmonary atresia anatomy, PS, TOF, CoA, etc.) also remains required before final Phase5 closure.

## Canonical Block17 artifacts

- `data/phase5/blocks/PHASE5_EXTRACTION_BLOCK_17.csv` — commit `335435c0f6c3b312f3c7703adf44122ce803571a`
- `docs/PHASE5_EXTRACTION_BLOCK_17_AUDIT.md` — commit `e84a838edb4e617412dd94a6beba27ee237303c9`

## Exact resume point

Proceed to **restart-native identity reconstruction of the remaining11 units**. Once identities are recovered, extract those units in auditable reconstruction/extraction blocks. After all76 units are structurally extracted, perform final harmonized-target adjudication, including the deferred d-TGA/simple-TGA discussion, resolve remaining holds where possible, and only then close Phase5 and freeze the analysis pools.

Snapshot P supersedes Snapshot O as the safe resume point.
