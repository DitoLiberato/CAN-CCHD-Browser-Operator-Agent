# CAN-CCHD Phase 5 — Identity Reconstruction Block 18 Audit

Date: 2026-08-22  
Branch: `phase5-extraction`  
Status: **IDENTITY RECONSTRUCTION COMPLETE / EXTRACTION NOT YET PERFORMED**

## Scope

Snapshot P left 11 frozen Phase4.5 quantitative units structurally unextracted because exact bibliographic identity had to be reconstructed from restart-native artifacts:

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

The binding restart legacy-data firewall was respected. No legacy app/database source was consulted for identity or any analytical variable.

## Method

Identity reconstruction was performed only from the restart-native public-corpus layer, using exact report-ID linkage and concordant bibliographic fields preserved in `Raw_Public_Corpus` and/or `PubMed_Reconciliation` artifacts. Exact title + author/year + PMID concordance was required where available. No match was accepted by thematic similarity alone.

## Reconstructed identities

| Unit | Exact identity | PMID | Result |
|---|---|---:|---|
| U_R001 | Richmond 2002 — *Routine pulse oximetry in the asymptomatic newborn* | 12193511 | exact |
| U_R002 | Koppel 2003 — *Effectiveness of pulse oximetry screening for congenital heart disease in asymptomatic newborns* | 12612220 | exact |
| U_R003 | Reich 2003 — *The use of pulse oximetry to detect congenital heart disease* | 12640374 | exact |
| U_R006 | Meberg 2008 — *First day of life pulse oximetry screening to detect congenital heart defects* | 18492511 | exact |
| U_R008 | de-Wahl Granelli 2009 — *Impact of pulse oximetry screening on the detection of duct dependent congenital heart disease: a Swedish prospective screening study in 39,821 newborns* | 19131383 | exact |
| U_R013 | Turska-Kmiec 2012 — *Early screening for critical congenital heart defects in asymptomatic newborns in Mazovia province* | 22528711 | exact |
| U_R036 | Arlettaz 2006 — *The contribution of pulse oximetry to the early detection of congenital heart disease in newborns* | 16211399 | exact |
| U_R037 | Tautz 2010 — *Implication of pulse oxymetry screening for detection of congenital heart defects* | 20458668 | exact |
| U_R042 | Bhola 2014 — *Post-implementation review of pulse oximetry screening of well newborns in an Australian tertiary maternity hospital* | 24923996 | exact |
| U_R066 | Jones 2016 — *The impact and efficacy of routine pulse oximetry screening for CHD in a local hospital* | 26905447 | exact |
| U_R067 | Klausner 2017 — *Evaluation of a Screening Program to Detect Critical Congenital Heart Defects in Newborns* | 28250095 | exact |

## R036/R037 governance correction

Block 17 correctly refused to infer identities from the then-consulted operational Phase5 matrix because that layer preserved only unit IDs and generic `standard extraction` notes. The broader restart-native corpus, however, preserves exact bibliographic records for both units:

- R036 = Arlettaz 2006, PMID 16211399;
- R037 = Tautz 2010, PMID 20458668.

Thus Block 17 was methodologically correct at the time: it did not guess. Block 18 resolves the provenance gap by using an independent restart-native artifact, not legacy data.

## Analytical firewall

This block changes **identity state only**. It does not import or infer:

- total screened;
- final failed-screen denominator;
- harmonized CCHD exclusions;
- CAN-A/B/AB/U classification;
- Strict or Expanded numerators;
- ascertainment;
- poolability;
- hold status.

Those variables must be reconstructed from primary reports under the locked Phase5 rules.

## Disposition

- identities reconstructed: **11/11**;
- unresolved identity queue: **0**;
- structurally extracted remains: **65/76**;
- remaining primary-source extraction queue: **11**;
- d-TGA/simple-TGA policy remains deliberately deferred until **76/76** structural extraction, exactly as specified in Snapshot P.

## Next step

Proceed to primary-source quantitative reconstruction of these 11 units in auditable extraction blocks. Do not reopen the final harmonized-target policy or run the final meta-analysis until all 76 units are structurally extracted.
