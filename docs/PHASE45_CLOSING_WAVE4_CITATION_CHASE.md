# CAN-CCHD Phase 4.5 — Closing Wave 4: Citation Chasing

Date: 2026-08-21
Status: COMPLETE / SATURATION COUNTER RESET

## Purpose

Run a citation-chasing and Google-Scholar-style discovery wave independent of the native PubMed and regional reconciliations, with emphasis on reports containing final failed-screen outcomes, conventional false positives, alternative diagnoses, and non-CCHD pathology.

Legacy Browser Agent data were not used. `RESTART_LEGACY_DATA_FIREWALL.md` applies.

## New report identities recovered

### NR044 — Kishore Kumar et al. 2017 — INCLUDE

**Citation:** Kumar RK, Shenoi A, Yerur KV, Tajamul S, Kini P. *Routine Pulse Oximetry Screening to Detect Critical Cyanotic Congenital Heart Disease in Neonates After Birth – A Developing Country Perspective & Experience.* Neonatology Today. 2017;12(6).

Primary report: Neonatology Today June 2017.

Key data:
- 22,601 well newborns screened in four tertiary maternity hospitals in Bangalore, June 2012–October 2016.
- 14 persistent failed screens after repeat testing.
- Three had pulmonary disease requiring treatment: one PPHN, one TTN, one congenital pneumonia with sepsis.
- Eleven underwent echocardiography: one PDA only, one VSD + small PDA, and nine reported by the authors as having “CCCHD”.
- The authors' lesion list includes diagnoses that require re-mapping under the review's locked CCHD definition; therefore their reported “nine CCCHD” count must not be imported blindly.

**Decision:** INCLUDE / target-definition and lesion-level mapping flag.

### NR045 — Walsh 2011 — EXCLUDE PRIMARY / RETAIN IMPLEMENTATION CONTEXT

**Citation:** Walsh W. *Evaluation of pulse oximetry screening in Middle Tennessee: cases for consideration before universal screening.* J Perinatol. 2011;31(2):125–129. PMID 20508595. DOI 10.1038/jp.2010.70.

Key data:
- 14,564 asymptomatic infants screened after 24 h.
- 112 conventional false positives and one true-positive CCHD.
- The 112 CCHD-negative positives are not given a complete clinical diagnosis/outcome/no-diagnosis distribution.

**Decision:** EXCLUDE PRIMARY — criterion 6; retain implementation/referral context.

### NR046 — Song et al. 2021 — EXCLUDE PRIMARY / RETAIN COMBINED-SCREEN CONTEXT

**Citation:** Song J, Huang X, Zhao S, et al. *Diagnostic value of pulse oximetry combined with cardiac auscultation in screening congenital heart disease in neonates.* J Int Med Res. 2021;49(5). PMID 34044642. PMCID PMC8165855. DOI 10.1177/03000605211016137.

Key data:
- 3,327 neonates with usable screening data.
- 276 abnormal pulse-oximetry results.
- Study target is CHD broadly and primary analysis uses pulse oximetry plus auscultation.
- Clinical outcomes among POX-positive/CHD-negative infants are not reported in a form usable for CAN-CCHD.

**Decision:** EXCLUDE PRIMARY — criterion 6 / target mismatch; retain accuracy/context.

### NR047 — Bin-Nun et al. 2021 — EXCLUDE PRIMARY / RETAIN IMPLEMENTATION CONTEXT

**Citation:** Bin-Nun A, Hammerman C, Mimouni FB, Wasserteil N, Kasirer YM. *The Saga of Pulse Oximetry Screening for Critical Congenital Heart Disease in Israel: A Historical Perspective.* Isr Med Assoc J. 2021;23(4):229–232. PMID 33899355.

Embedded Shaare Zedek cohort:
- 20,385 eligible newborns; 19,763 screened.
- 48 screen-positive.
- One true-positive CCHD (HLHS); another HLHS was a false negative.
- The 47 CCHD-negative positives are not clinically classified.

**Decision:** EXCLUDE PRIMARY — criterion 6; retain implementation context.

### NR048 — Adaboh et al. 2026 — COMPANION / NO INDEPENDENT COHORT

**Citation:** Adaboh A, Celestin D, Agyekum A, et al. *Experience with Implementation of Pulse Oximetry Screening for Critical Congenital Heart Disease in a Low–Middle-Income Country.* Int J Neonatal Screen. 2026;12(3):62. DOI 10.3390/ijns12030062.

- Implementation report from the Ghana program.
- Explicitly refers to a separate quantitative manuscript reporting screening results from nearly 6,000 neonates: Yao et al. 2026, already R053.
- Does not contribute an independent quantitative cohort.

**Decision:** COMPANION / NO INDEPENDENT COHORT vs R053 Yao 2026.

## Secondary/context references encountered but not promoted into the report master

Current guidelines/reviews (e.g., Ewer 2026 algorithm review, AAP updated clinical report, BAPM framework) were used as citation-chasing sources. They are not added merely because they cite the topic unless they were direct records in a defined native search/export or contain an independent primary cohort. This prevents an infinite expansion of the bibliographic master through secondary-to-secondary citation chains.

## Wave result

- New independent primary candidate meeting the CAN-CCHD full-text criterion: **1 (NR044)**.
- New primary/context reports failing criterion 6: **3 (NR045–NR047)**.
- New companion report: **1 (NR048)**.
- Therefore this wave is **not a zero-new-primary wave**.
- Saturation counter reset.

## Next saturation requirement

After incorporating NR044–NR048, run two independent discovery waves with no new independent primary report:

1. recent/current 2024–2026 screening literature with failed-screen/non-CCHD outcome terms;
2. seed/author/backward-forward citation chasing using NR044, NR007–NR009 and high-yield primary anchors.

Any newly identified independent primary report resets the counter again.