# HANDOFF — CAN-CCHD Phase 4.5

Date: 2026-08-21
Conversation handoff status: CLOSED / SAFE TO CONTINUE IN NEW CHAT
Branch: `phase4-consolidation`

## 1. Project question and locked outcome

Systematic review/meta-analysis of newborn pulse-oximetry screening for critical congenital heart disease (CCHD), focused on what conventional `false positives` actually represent clinically.

Primary denominator:

`CCHD-negative failed screens`

Primary outcome:

`clinically actionable non-CCHD diagnosis / CCHD-negative failed screens`

Required mutually exclusive conceptual categories for CCHD-negative failed screens:

1. actionable CAN-CCHD;
2. transitional / non-actionable physiology;
3. explicitly healthy / no diagnosis;
4. diagnosis not reported / not ascertained.

Critical rules:

- `echo normal` is **not** equivalent to healthy;
- absence of a reported diagnosis is **not** healthy;
- treatment/management alone is not a diagnosis unless the source supports the clinical category;
- a calculable CCHD false-positive count alone does **not** satisfy eligibility unless diagnosis/outcome/management/explicit no-diagnosis is available for the CCHD-negative failed-screen subgroup;
- bibliographic reports and unique quantitative cohorts are different units;
- companion/overlapping reports are never blindly summed;
- NICU-only cohorts are excluded from the primary meta-analysis and retained for secondary/sensitivity use.

Protocol source:

`docs/01_RESEARCH_PLAN_AND_PROTOCOL.md`

## 2. Hard legacy-data firewall

The systematic review was restarted from zero in August 2026. The old Browser Agent/app and its SQLite database are **legacy/historical only**.

Binding file:

`docs/RESTART_LEGACY_DATA_FIREWALL.md`

Commit creating the firewall: `4169c934910ad4aa3e29f551f1e47d1bec1e0f3c`

The legacy app/database may never be used to:

- add/remove a study;
- determine INCLUDE/EXCLUDE/COMPANION status;
- supply numerators/denominators/diagnoses;
- establish cohort overlap;
- determine PRISMA or meta-analysis counts;
- resolve any scientific disagreement.

A temporary legacy SQLite inspection was performed only to determine whether it contained the missing restart corpus artifact. It did not: it contained 2,301 normalized rows and clearly belonged to the abandoned app. The temporary workflow was removed, its PR was closed without merge, and no scientific data were imported. The only retained lesson was software QA: PMCID must not be trusted as an unconditional deduplication key.

All current scientific identities are restart-native (`Rxxx`) or independently reverified citation-chasing additions (`NRxxx`).

## 3. Why the historical `156` is no longer the closure denominator

Earlier Phase 4 work referenced an old normalized queue of 156 records (`49 include + 107 maybe`). During QA we discovered that the exact post-normalization artifact that generated that count is not available and that report-level identity reconciliation could double-count or include context reports outside that historical queue.

Therefore:

- `149/156`, `156/156`, or similar countdowns are **withdrawn**;
- the historical 156 is retained only as audit history;
- Phase 4.5 now freezes a restart-native **bibliographic report master**, then derives final eligibility and unique cohorts from that master.

Binding reconciliation document:

`docs/PHASE4_MEMBERSHIP_RECONCILIATION.md`

Current consolidation ledger:

`docs/PHASE4_CONSOLIDATION_LEDGER_v0.1.md`

Do not revive the old 156 as the primary denominator.

## 4. Restart-native corpus lineage

The public restart corpus reached:

- R001–R132 in public corpus v0.6;
- R133–R145 in the v0.7 regional/IMEMR consolidation manifest.

Thus the stable restart public-corpus base is:

**R001–R145 = 145 bibliographic reports**

The Rxxx lineage predates the Phase 4 consolidation branch and is independent of the legacy app database.

Regional v0.7 manifest:

`docs/CAN-CCHD_Public_Corpus_v0.7_MANIFEST.md`

## 5. Phase 4 adjudication status before Phase 4.5

Extensive full-text adjudication was completed across the Rxxx reports in multiple tranches. Those individual study decisions remain valid report-level evidence.

Canonical tranche files include:

- `PHASE4_TRANCHE_R016_R025.md`
- `PHASE4_TRANCHE_R033_R052_R065.md`
- `PHASE4_TRANCHE_R038_R047.md`
- `PHASE4_TRANCHE_R077_R085.md`
- `PHASE4_TRANCHE_R086_R096.md`
- `PHASE4_TRANCHE_R097_R115.md`
- `PHASE4_TRANCHE_R116_R132.md`

Do **not** use the old aggregate INCLUDE/EXCLUDE counts as final Phase 4 numbers until the master is frozen and every report identity is reconciled.

## 6. Phase 4.5 closing waves completed

### Wave 1 — Cochrane / Saganski / van Vliet reference reconciliation

File:

`docs/PHASE45_CLOSING_WAVE1_REVIEW_RECON.md`

Commit: `a87121317f984837a82c3e51067c283a58025c15`

Outcome:

- primary reference lists reconciled;
- non-PubMed deltas recovered and verified;
- no remaining unresolved primary bibliographic identity from those review/reference sets.

Initial non-R additions included:

- NR001 Donia & Tolba 2016 — CONDITIONAL / SUPPORTING;
- NR002 Gamhewage 2021 — INCLUDE;
- NR003 Zayachnikova 2020 — EXCLUDE PRIMARY / accuracy context;
- NR004 Gunaratne 2021 — EXCLUDE PRIMARY / accuracy context;
- NR005 Chen/Hainan English report — EXCLUDE PRIMARY / program context;
- NR006 Zhang/Hainan Chinese report — COMPANION to NR005.

Important: Gamhewage and Gunaratne are distinct Sri Lankan reports and must never be merged.

### Wave 2 — Native PubMed 81-PMID reconciliation

File:

`docs/PHASE45_NATIVE_PUBMED_81_RECON.md`

Canonical correction commit: `6a07839b2059b99aad1e825b294d35f204eb183c`

Outcome:

- 81/81 native PMID occurrences accounted for;
- 43 already represented by Rxxx;
- 37 new resolved bibliographic reports became NR007–NR043;
- 1 occurrence remains unresolved: PMID `22984710`.

Three important new primary INCLUDE reports from this wave:

#### NR007 Williams et al. 2021 — INCLUDE

`Newborn Pulse Oximetry for Infants Born Out-of-Hospital`

- 3,019 newborns;
- 3 CCHD detected;
- 12 false-positive cases had other pathology;
- denominator convention differs between field interpretation and strict algorithm interpretation;
- retain denominator-convention flag.

#### NR008 Narayen et al. 2016 — INCLUDE

`Pulse Oximetry Screening for Critical Congenital Heart Disease after Home Birth and Early Discharge`

- 3,059 screened;
- 32 false-positive screens;
- clinically important alternate conditions reported;
- retain numerator-discrepancy QA flag;
- study dates precede later POLAR cohort, so no current evidence of temporal overlap.

#### NR009 Tekgündüz et al. 2021 — INCLUDE with flags

- 501 neonates at high altitude;
- 21 positive screens;
- no CCHD;
- 9 PDA;
- remaining 12 incompletely characterized;
- flags: altitude, partial ascertainment, PDA actionability.

Other notable native-PubMed reconciliation:

- NR034 Majani 2022 = preliminary/protocol companion of definitive R032 Majani 2025;
- metadata correction R131 PMID = 39411017;
- metadata correction R033 Abu Jarir/Qatar PMID = 41890244.

### Wave 3 — LILACS/BVS + SciELO + IMEMR/regional

File:

`docs/PHASE45_CLOSING_WAVE3_REGIONAL_RECON.md`

Commit: `ed0a0fda17d7bb1a10c051f51862b178e090dd9c`

Outcome:

- all explicitly retained LILACS/BVS gains mapped to Rxxx/NRxxx;
- all SciELO gains mapped;
- IMEMR/Eastern Mediterranean R133–R145 fully represented;
- new unmapped bibliographic identity = 0;
- new primary report from this reconciliation = 0.

Important limitation:

`PUBLIC_WEB_RECONCILIATION_COMPLETE_AND_SATURATED = YES`

but

`NATIVE_PLATFORM_EXACT_EXPORT_COMPLETE = NOT DEMONSTRATED`

Do not overclaim native LILACS/SciELO/IMEMR platform completeness.

### Wave 4 — Google-Scholar-style citation chasing

File:

`docs/PHASE45_CLOSING_WAVE4_CITATION_CHASE.md`

Commit: `47775e4c548a8f31cb851ba548d649f54728c02e`

Outcome: five new bibliographic reports, including one new independent primary INCLUDE. Therefore the saturation counter was reset.

#### NR044 Kishore Kumar et al. 2017 — INCLUDE

Bangalore / Neonatology Today.

- 22,601 well newborns screened;
- 14 persistent failed screens;
- 3 pulmonary diagnoses requiring treatment: PPHN, TTN, congenital pneumonia + sepsis;
- 11 underwent echo;
- authors label 9 as “CCCHD”, but their lesion list must be re-mapped to the review's locked CCHD definition;
- INCLUDE with target-definition + lesion-level mapping flag.

#### NR045 Walsh 2011 — EXCLUDE PRIMARY / retain implementation context

- 14,564 asymptomatic infants;
- 112 conventional false positives;
- no complete clinical distribution among those 112;
- fails criterion 6.

#### NR046 Song et al. 2021 — EXCLUDE PRIMARY / combined-screen context

- 3,327 neonates;
- 276 abnormal POX;
- target = CHD broadly and combined POX + auscultation;
- CCHD-negative POX outcomes not usable for CAN-CCHD.

#### NR047 Bin-Nun et al. 2021 — EXCLUDE PRIMARY / implementation context

Embedded Shaare Zedek cohort:

- 19,763 screened;
- 48 positive;
- 1 true-positive CCHD;
- 47 CCHD-negative positives not clinically classified;
- criterion 6 not met.

#### NR048 Adaboh et al. 2026 — COMPANION

- Ghana implementation report;
- points explicitly to separate quantitative report R053 Yao 2026;
- no independent quantitative cohort.

## 7. Current canonical report master

Newest master:

`docs/PHASE45_RESTART_REPORT_MASTER_v0.3.md`

Commit: `3e7dff7bb1b19207a03eda55c87de6f5412d1b22`

Current inventory:

- R001–R145 = 145;
- NR001–NR048 = 48;
- **193 resolved bibliographic reports**;
- plus **1 unresolved native PMID occurrence: 22984710**.

The `193` is a bibliographic inventory only. It is **not**:

- the number of eligible primary studies;
- the number of quantitative studies;
- the number of unique cohorts.

## 8. Saturation status at handoff

Because Wave 4 found NR044, the saturation counter reset.

**Current counter = 0 consecutive zero-new-independent-primary waves after latest discovery.**

Phase 4.5 is NOT frozen yet.

## 9. Exact next actions in the next chat

Do not restart Phase 4.5 planning. Continue directly with these actions.

### Action A — Saturation Wave A: recent/current 2024–2026 literature

Search specifically for newborn CCHD pulse-ox screening studies reporting:

- failed screen / screen positive;
- false positive;
- alternative diagnosis;
- secondary diagnosis;
- non-CCHD illness;
- PPHN;
- sepsis/infection;
- respiratory disease;
- transitional circulation;
- treatment/admission among CCHD-negative positives.

Prioritize:

- 2024–2026;
- ahead-of-print;
- regional/non-PubMed literature;
- reports not already R001–R145 or NR001–NR048.

If zero new independent primary reports: saturation counter becomes 1.

If any new independent primary report appears:

1. verify primary source/full text;
2. assign NR049 onward;
3. adjudicate criterion 6;
4. add to master;
5. reset saturation counter to 0.

### Action B — Saturation Wave B: seed/author backward-forward citation chasing

Independent seeds:

- NR044 Kishore Kumar/Bangalore;
- NR007 Williams/out-of-hospital;
- NR008 Narayen/home birth;
- NR009 Tekgündüz/altitude;
- R009 Riede;
- R010 Ewer;
- R017 Jawin;
- R020 POLAR;
- R024 Gopalakrishnan;
- R029 Tsao;
- R099 Tekleab;
- R101 Singh & Chen;
- R102 Turkey 2025.

Do not recursively promote reviews/guidelines simply because they cite the topic. The purpose is to find direct independent primary reports.

If Wave A = 0 and Wave B independently = 0, saturation counter = 2 and the bibliographic master may be frozen, subject to PMID 22984710 handling.

### Action C — one final direct attempt to resolve PMID 22984710

Do not guess its identity.

Try direct NCBI/PubMed verification. If still unrecoverable:

- retain `UNRESOLVED_NATIVE_EXPORT_OCCURRENCE`;
- do not count it among resolved reports;
- only classify as invalid/export anomaly if evidence supports that conclusion.

## 10. What happens immediately after two-zero-wave saturation

Once saturation is achieved:

1. freeze the report master as the final Phase 4.5 bibliographic inventory;
2. recompute report-level Phase 4 dispositions from the master;
3. run strict criterion-6 QA on every INCLUDE report;
4. resolve companion/overlap clusters;
5. derive the **unique quantitative cohort list**;
6. only then close Phase 4 and begin Phase 5 structured extraction.

## 11. Major overlap/companion clusters already known

Must be resolved before pooling:

- Birmingham: Singh 2014 + Henderson 2022 partial temporal overlap;
- PulseOx: Ewer 2011 + Ewer 2012 same cohort/companion;
- Meberg 2008 + 2009 probable companion/overlap;
- Taksande 2013 + 2017 possible cumulative extension;
- Saxena + Arvind same 19,009-newborn cohort;
- El Bakry R141 + R145 same enriched Egypt/UAE cohort;
- Shanghai R116 + R117 overlap 2019–2021;
- R125 SIBEN site-level units need overlap audit;
- Wisconsin/out-of-hospital cluster: Miller 2016 / SHINE and related reports; Williams and Narayen require date/program comparison but are not automatically companions;
- Majani R032 definitive + NR034 preliminary/protocol;
- Ghana R053 Yao definitive + NR048 Adaboh implementation companion.

## 12. High-value CAN-CCHD anchors already adjudicated

Examples worth preserving during Phase 5:

- R009 Riede 2010: 40 CCHD false positives = 15 PPHN, 13 sepsis, 12 healthy;
- R017 Jawin 2015: 13/13 CCHD-negative positives with significant disease (2 sepsis, 11 respiratory);
- R019 POPSICLe: 1 CCHD-negative final fail = sepsis;
- R020 POLAR: 221 CCHD false positives; 134 noncardiac illness;
- R023 Morocco: 10 CCHD-negative = 5 noncritical CHD, 1 PPHN, 2 sepsis, 2 normal;
- R024 Gopalakrishnan: 13 CCHD-negative = 8 sepsis/pneumonia, 2 PPHN, 3 transitional;
- R025 Flórez-Muñoz: 3 CCHD-negative = 1 pulmonary hypertension, 2 explicitly healthy;
- R043 Oakley: 7/7 CCHD-negative had pathology;
- R089 Johnson: 1/1 CCHD-negative = PPHN;
- R093 Cawsey: 2/2 CCHD-negative = significant respiratory disease;
- R099 Tekleab: 56 persistent fails, no CCHD; 10 PPHN (2 also sepsis), 11 PDA, 2 ASD, 33 clinically unremarkable;
- R100 New Zealand: 48 failed; 37 significant pathology, 11 no pathology;
- R101 Singh & Chen: 189 study-defined true-positive, 156 significant noncardiac diagnoses; denominator convention still needs resolution;
- R102 Turkey 2025: sepsis, pneumonia, polycythaemia, TTN; mutual-exclusivity flag;
- R135 Salih 2018: 55 CCHD false positives; 28 other pathology;
- NR044 Kishore Kumar 2017: new high-yield primary found by citation chasing.

## 13. Important unresolved QA issues before meta-analysis

- R101 denominator: 360 algorithm-positive vs 189 study-defined true-positive;
- R099 PPHN/sepsis overlap;
- R100 lesion-level cardiac classification;
- R102 diagnostic-category mutual exclusivity;
- R108 early/transitional PDA without follow-up;
- R125 site-level overlap;
- R127 altitude heterogeneity;
- R128 PFO/transitional coding;
- R130 lesion-level actionability + early timing;
- R018 PFO/transitional coding;
- R021 PDA/anomalous pulmonary venous connection classification;
- R022 one lost-to-echo positive and mostly non-actionable findings;
- R023 noncritical-CHD actionability;
- R020 remaining false positives not classified as noncardiac illness;
- R039 three failed screens without further diagnostic work-up;
- R043 actionability of significant noncritical CHD;
- R053 Ghana: actionability of non-CCHD CHD + echo-negative infants clinically unclassified + two pre-echo deaths;
- NR007 denominator convention;
- NR008 numerator discrepancy;
- NR009 PDA actionability + 12 incompletely characterized positives;
- NR044 target-definition/lesion re-mapping.

## 14. Current GitHub state

Repository:

`DitoLiberato/CAN-CCHD-Browser-Operator-Agent`

Working branch:

`phase4-consolidation`

At handoff creation, the branch already contained the Wave 4 commit and master v0.3. Continue on this branch; do not use legacy-app tables as scientific input.

## 15. One-sentence restart instruction for the next chat

**Continue CAN-CCHD Phase 4.5 from `PHASE45_RESTART_REPORT_MASTER_v0.3.md`: execute saturation Wave A (2024–2026 recent literature), then independent seed/citation Wave B; assign NR049+ only to genuinely new bibliographic reports, reset the counter if any new independent primary is found, otherwise freeze after two zero-new-primary waves plus final PMID 22984710 handling.**
