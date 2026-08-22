# CAN-CCHD Phase 5 — Progress Snapshot Q

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **ACTIVE / SAFE RESUME POINT AFTER IDENTITY BLOCK 18**

## Binding state

Phase5 remains derived exclusively from the 76 frozen Phase4.5 quantitative units. The restart legacy-data firewall remains binding. No legacy app/database source may resolve identity, eligibility, denominator, numerator, diagnosis, target mapping, actionability, overlap, PRISMA count or analysis weight.

## Current counts

After extraction Blocks01–17 plus identity-reconstruction Block18:

- frozen units: **76**
- structurally extracted: **65/76**
- PRIMARY_POOLABLE: **24**
- SENSITIVITY_ONLY: **35**
- HOLD_PENDING_QA: **3**
- NOT_POOLABLE: **3**
- unresolved bibliographic identities: **0**
- identified but still unextracted: **11**

Poolability remains provisional until complete extraction and final harmonized-target adjudication.

## Block18 result

Restart-native bibliographic reconstruction is complete for:

U_R001, U_R002, U_R003, U_R006, U_R008, U_R013, U_R036, U_R037, U_R042, U_R066, U_R067.

Every linkage is exact at report-ID/title/author-year/PMID level using restart-native public-corpus artifacts. No legacy source was used.

Block18 is identity-only and therefore does not change the 65/76 structural-extraction count.

## Remaining extraction queue =11

- U_R001 — Richmond 2002, PMID 12193511
- U_R002 — Koppel 2003, PMID 12612220
- U_R003 — Reich 2003, PMID 12640374
- U_R006 — Meberg 2008, PMID 18492511
- U_R008 — de-Wahl Granelli 2009, PMID 19131383
- U_R013 — Turska-Kmiec 2012, PMID 22528711
- U_R036 — Arlettaz 2006, PMID 16211399
- U_R037 — Tautz 2010, PMID 20458668
- U_R042 — Bhola 2014, PMID 24923996
- U_R066 — Jones 2016, PMID 26905447
- U_R067 — Klausner 2017, PMID 28250095

## Deferred d-TGA/simple-TGA discussion

The d-TGA/simple-TGA policy remains deliberately deferred until all 76 units are structurally extracted. Affected rows may carry explicit provisional target bounds/flags but no final policy adjudication will be made during reconstruction.

The broader conditional-lesion audit remains required before scientific Phase5 closure.

## Canonical Block18 artifacts

- `data/phase5/blocks/PHASE5_IDENTITY_RECONSTRUCTION_BLOCK_18.csv` — commit `0cd29950c27e0ef3fb930d655eab3e303febf37a`
- `docs/PHASE5_IDENTITY_RECONSTRUCTION_BLOCK_18_AUDIT.md` — commit `eb005afbc296196e12948766c10c765ff2a0b8c2`

## Exact resume point

Proceed to primary-source quantitative reconstruction of the 11 identified units. Preserve the locked Phase5 extraction schema and do not use legacy data. Once all 76 units are structurally extracted, perform final harmonized-target adjudication, including the deferred d-TGA/simple-TGA discussion, resolve remaining holds where possible, and then freeze the analysis pools.

Snapshot Q supersedes Snapshot P as the safe resume point.
