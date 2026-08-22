# CAN-CCHD Phase 5 — Extraction Block 17 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **BLOCK 17 COMPLETE / QA-CLOSED FOR EXTRACTED UNITS**

## Scope

Block 17 was planned around four remaining directly identified units:

- U_R036
- U_R037
- U_R125_BARRANQUILLA_CO
- U_R125_SONORA_MX

During provenance verification, R036 and R037 could not be tied to exact restart-native bibliographic identities from currently accessible canonical artifacts without inference. They were therefore **not extracted** and were transferred to the restart-native identity-reconciliation queue. This increases that queue from9 to11 units. No legacy data were consulted.

Two SIBEN site units were fully extracted from the primary multisite report.

## U_R125_BARRANQUILLA_CO — Barranquilla, Colombia

Primary source: Sola A et al. *CCHD Screening Implementation Efforts in Latin American Countries by the Ibero American Society of Neonatology (SIBEN).* Int J Neonatal Screen. 2020;6(1):21. PMCID PMC7422978; DOI 10.3390/ijns6010021.

Primary table:
- screened9241;
- positive38;
- hypoxemic conditions/PPHN8;
- ASD1;
- ASD+PS1;
- VSD+PDA1;
- VSD+PPHN1;
- TOF1;
- TAPVR2;
- single ventricle right1;
- single ventricle left2;
- IV-septal hypertrophy1;
- tricuspid atresia+hypoplastic RV1;
- true false positives18.

The rows sum exactly to38.

### Harmonized target

No lesion can be removed automatically from the available report under the locked target:
- TOF and TAPVR are conditional and lack documented <=28-day death/surgery/catheterization;
- single-ventricle/tricuspid-atresia/septal-hypertrophy labels are off-list;
- ASD/VSD/PDA-type lesions are not target lesions.

Therefore harmonized CCHD=0 and denominator=38.

### CAN coding

No diagnosis-specific qualifying management consequence is documented sufficiently for Strict coding.

CAN-U18:
- hypoxemic/PPHN8;
- ASD+PS1;
- VSD+PPHN1;
- TOF1;
- TAPVR2;
- single ventricle3;
- septal hypertrophy1;
- tricuspid-atresia complex1.

NON_CAN20:
- ASD alone1;
- VSD+PDA1;
- true false positives18.

Final:
- Strict0/38;
- Expanded18/38;
- ascertainment100%;
- PRIMARY_POOLABLE.

The inherited target/actionability hold is resolved.

## U_R125_SONORA_MX — Sonora, Mexico

Same primary multisite source.

Source states:
- screened9181;
- positive22;
- summary table: CCHD11 + PPHN8 + sepsis2.

Direct recheck therefore gives a subtotal of21, not24 as stated in the earlier Phase4 shorthand. The shorthand was inaccurate, but the primary-source arithmetic problem remains because 22 total positives are not reconciled by the printed categories.

### Target mapping

The 11 source-CCHD lesion identities are unavailable. Any number0–11 may satisfy the locked target.

Thus:
- harmonized CCHD0–11;
- denominator11–22.

### CAN coding

- PPHN8 + sepsis2 -> CAN-U10; diagnosis is clinically relevant, but participant-specific treatment/escalation/disposition evidence is not reported.
- any source-CCHD case that re-enters the denominator adds to CAN-U -> total CAN-U10–21;
- the unaccounted 22nd positive remains UNKNOWN1.
- Strict remains0.

Expanded=10–21 with denominator11–22; ascertainment remains >=90% across admissible scenarios.

### Hold decision

The inherited hold is **not cleared**. The direct source correction changes the stated discrepancy from `22 vs sum24` to `22 vs sum21`, but does not reconcile the source. Sonora remains `HOLD_PENDING_QA`.

## R036/R037 provenance correction

Snapshot O described R036/R037 as directly identified. Block17 verification found that the available canonical artifacts preserve only their unit IDs and generic `standard extraction` labels, not a sufficiently exact bibliographic identity for safe primary-source linkage.

Binding action:
- no extraction;
- no guessed identity;
- no legacy lookup;
- transfer both to identity reconciliation.

Revised identity queue:
U_R001, U_R002, U_R003, U_R006, U_R008, U_R013, U_R036, U_R037, U_R042, U_R066, U_R067.

## Block 17 disposition

- newly PRIMARY_POOLABLE: 1 — U_R125_BARRANQUILLA_CO
- newly HOLD_PENDING_QA: 1 — U_R125_SONORA_MX (pre-existing inherited hold retained)
- structurally extracted this block: 2
- transferred to identity reconciliation: 2 — U_R036/U_R037

## Next step

Direct-identity extraction is now exhausted. Proceed to restart-native identity reconstruction of the remaining **11 frozen units**, then extract each reconstructed unit. The d-TGA/simple-TGA policy question remains deliberately deferred for joint discussion after complete extraction, as requested, while current affected rows remain provisional and no final primary meta-analysis is run.
