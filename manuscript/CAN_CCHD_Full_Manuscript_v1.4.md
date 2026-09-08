# Beyond Critical Congenital Heart Disease: Clinically Relevant Disease After Failed Newborn Pulse Oximetry Screening - A Systematic Review and Meta-analysis

Rodrigo Liberato de Oliveira<sup>1</sup>; Mansour Almotairi<sup>2</sup>; Mohammad Allugmani<sup>2</sup>; Abdullah Alrashidi<sup>2</sup>; Saeed Alghamdi<sup>1</sup>; Adnan Aselan<sup>1</sup>; Shaimaa Rakha<sup>1,3,4</sup>

1 Madinah Maternity and Children's Hospital, King Salman Medical City, Madinah, Saudi Arabia  
2 Madinah Cardiac Center, Madinah, Saudi Arabia  
3 Department of Pediatrics, Faculty of Medicine, Mansoura University, Egypt  
4 Ohud Hospital, Madinah, Saudi Arabia

# Abstract

**Introduction:** Newborn pulse oximetry is designed to detect critical congenital heart disease (CCHD), yet many infants with final failed screens do not have target CCHD and are conventionally classified as false positives. We quantified clinically relevant alternative disease and documented management consequences among these infants.

**Methods:** We systematically reviewed newborn CCHD pulse-oximetry screening studies reporting outcomes after final failed screens. Review conduct used a version-controlled, phase-gated, human-supervised workflow with artificial-intelligence assistance restricted to auditable support tasks and physician verification of scientific decisions. The primary outcome was Strict clinically actionable non-CCHD (CAN-CCHD), requiring documented treatment, escalation, altered disposition, or clinically required follow-up. Expanded CAN-CCHD was a prespecified secondary/sensitivity outcome that additionally included clinically relevant diagnoses without documented qualifying actionability. Random-effects proportions were synthesized using a one-stage exact-binomial logistic-normal model.

**Results:** Twenty-eight independent primary analytic units contributed 1,999 harmonized-CCHD-negative final failed screens. For the primary outcome, Strict CAN-CCHD had a median-study probability of 17.0% (95% confidence interval [CI], 3.1%-46.8%) and marginal mean of 33.8%; between-study heterogeneity was extreme (tau=3.369). Expanded CAN-CCHD was more common and less heterogeneous: median-study probability 69.4% (95% CI, 57.7%-81.4%), marginal mean 65.8%, tau=1.110. Secondary etiologic median-study probabilities were 26.6% for other/non-target structural cardiac diagnoses, 16.7% for infection/sepsis, 10.3% for persistent pulmonary hypertension/pulmonary hypertension, and 8.7% for respiratory disease. Prespecified sensitivity analyses did not reverse the interpretation.

**Conclusions:** Among final failed CCHD screens without target CCHD, clinically relevant alternative disease was common, whereas specifically documented management consequences varied markedly across programs. For pediatric cardiologists and neonatal teams involved after a failed screen, the encounter may therefore represent more than exclusion of target heart disease: it is also an opportunity to recognize clinically important alternative neonatal disease and expedite multidisciplinary care.

**Keywords:** critical congenital heart disease; pulse oximetry; newborn screening; neonatal hypoxemia; false-positive screen; pediatric cardiology; meta-analysis

# Introduction

Pulse oximetry screening is an established component of newborn assessment for critical congenital heart disease (CCHD), complementing prenatal ultrasonography and physical examination in the early detection of hypoxemic congenital heart lesions.[1,2] Diagnostic-accuracy evidence shows high specificity with moderate sensitivity for CCHD, supporting its use as a population screening tool.[3] At the population level, implementation of mandatory CCHD screening policies has also been associated with reduced early infant cardiac mortality.[4]

Within a conventional diagnostic-accuracy framework, a newborn who fails a CCHD screen but is not ultimately diagnosed with target CCHD is classified as a false positive. That label is statistically correct for the target condition but can be clinically incomplete. Large prospective screening cohorts reported substantial alternative pathology among such infants, including structural cardiac disease outside the target definition, pulmonary disease, infection, and persistent pulmonary hypertension.[5,6] A subsequent review of implementation studies similarly emphasized that clinically important noncardiac pathology may account for a substantial fraction of CCHD false-positive screens.[7]

This distinction has become increasingly relevant. The 2025 American Academy of Pediatrics (AAP) clinical report explicitly identifies detection of hypoxemic non-CCHD conditions as a secondary benefit of screening and recommends that programs capture the presence and type of non-CCHD conditions after failed screens.[1] Saudi Arabia approved a national universal CCHD pulse-oximetry screening program in 2015 and began universal implementation in 2016; Saudi program reports also describe structured evaluation after positive screens, including pediatric-cardiology assessment in local pathways.[8,9] These developments create a practical question that conventional sensitivity and specificity analyses do not answer: among newborns who complete a screening protocol, have a final failed result, and do not have harmonized target CCHD, how often is clinically relevant alternative disease identified, and how often is a qualifying management consequence actually documented?

We therefore conducted a systematic review and random-effects meta-analysis focused specifically on the downstream clinical yield of harmonized-CCHD-negative final failed pulse-oximetry screens. The prespecified primary outcome was Strict clinically actionable non-CCHD (CAN-CCHD), requiring documented treatment, escalation, disposition change, or clinically required follow-up. Expanded CAN-CCHD was a prespecified key secondary/sensitivity outcome that additionally captured clinically relevant diagnoses when qualifying actionability was not explicitly documented. We also synthesized prespecified secondary etiologic outcomes and examined robustness to alternative analytic assumptions.

# Methods

## Protocol, reporting framework, and review question

The review was conducted under a version-controlled protocol locked before evidence extraction and quantitative synthesis. The protocol, subsequent ontology clarifications, final statistical analysis plan, extraction/audit artifacts, analytic code, and machine-readable results are publicly archived in the project GitHub repository. Reporting was structured with reference to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 statement,[10] and reporting of the literature search was informed by PRISMA-S.[11] The review question was: among newborns who fail pulse-oximetry screening for CCHD but are not diagnosed with CCHD under a harmonized lesion-level target definition, what proportion have a clinically actionable non-CCHD diagnosis?

## Phase-gated, AI-assisted, human-supervised workflow

Review conduct was organized in a public GitHub repository as a version-controlled 12-stage, phase-gated workflow (Phases 0-11): research planning; search collection; deduplication; title/abstract screening; full-text retrieval; full-text eligibility; data extraction; extraction verification; diagnosis mapping; quality-assurance gating; statistical analysis; and manuscript/abstract drafting. Progression to a subsequent stage required completion of the preceding stage or an explicitly documented human decision.

Generative artificial intelligence (AI) accessed through ChatGPT (OpenAI), deterministic scripts, browser/database tools, and structured physician review were used as complementary components of the workflow. AI assistance was used for non-final tasks such as development and adaptation of search queries, browser/search support, metadata reconciliation, duplicate-candidate detection and prioritization, extraction suggestions, diagnosis-mapping suggestions, quality-control checks, statistical-code drafting and checking, and manuscript drafting or editing. The AI system was not treated as an independent reviewer or as an evidentiary source. No study was excluded solely on the basis of an AI recommendation; no AI-suggested extracted value entered the analytic dataset unless it had been verified or corrected by the physician investigator; and final decisions regarding protocol changes, eligibility, cohort overlap, numerator and denominator adjudication, diagnosis mapping, analytic-dataset locking, model selection, and scientific interpretation remained human-controlled. Quantitative results were generated by version-controlled deterministic Python scripts operating on frozen analytic inputs rather than by language-model arithmetic.

The exact AI model version was not prospectively fixed across all AI-assisted sessions; therefore, no retrospective single-version identifier is asserted. This limitation of tool-version provenance is reported explicitly rather than reconstructed from inference.

## Information sources and search strategy

Searches and citation chasing were completed through 21 August 2026. The public-source search used PubMed/MEDLINE, Europe PMC, Latin American and Caribbean Health Sciences Literature (LILACS) via the Biblioteca Virtual em Saude/Virtual Health Library (BVS), Scientific Electronic Library Online (SciELO), and regional/Eastern Mediterranean sources including the Index Medicus for the Eastern Mediterranean Region (IMEMR). Google Scholar was used as a supplementary discovery source, followed by backward and forward citation chasing. Crossref, OpenAlex, and Semantic Scholar were used for supplementary metadata or citation-network enrichment where useful. Embase and Scopus/Web of Science were prespecified in the source hierarchy but were not available and were not searched.

The search strategy used broad CCHD/pulse-oximetry/newborn concepts followed by focused failed-screen and alternative-diagnosis searches. The principal PubMed broad query was:

```text
("critical congenital heart disease"[Title/Abstract] OR CCHD[Title/Abstract]) AND ("pulse oximetry"[Title/Abstract] OR "oxygen saturation"[Title/Abstract]) AND (newborn[Title/Abstract] OR neonate[Title/Abstract] OR neonatal[Title/Abstract])
```

A focused PubMed search added false-positive/failed-screen, hypoxemia/hypoxaemia, pulmonary-hypertension/PPHN, sepsis, and respiratory terms; an additional sensitivity query targeted persistent pulmonary hypertension. Equivalent source-specific syntax was used in Europe PMC. LILACS/BVS and SciELO searches included English, Portuguese, and Spanish variants, and IMEMR searches used simpler regional strings because the interface was less reliable with complex Boolean syntax. Google Scholar searches were supplementary and were not treated as a primary reproducible database search. The exact prespecified source-specific query strings, simpler language variants, source access modes, and notes on databases that were unavailable are reproduced in Supplementary Appendix 1 and preserved in the repository.

Search expansion was iterative. Recent-literature, regional/country-specific, spelling/typographical, grey-literature, seed-author/title, multilingual, and citation-chasing waves were reconciled against the evolving report inventory. An early generic regional saturation impression was withdrawn after country-by-country Eastern Mediterranean searching recovered additional reports; two subsequent separate closing waves then identified no new routine potentially eligible screening cohorts. The final search record therefore distinguishes public-web saturation from native-platform completeness rather than equating the two. One PubMed record identifier (22984710) present in a source export could not be linked to a verifiable bibliographic record and was retained as an unresolved search occurrence without a scientific eligibility assignment.

## Eligibility and analytic unit

Eligible reports included newborn or neonatal screening populations evaluating pulse oximetry for CCHD, with final failed/positive screen data that permitted identification of CCHD-negative failed screens and reported at least one diagnosis, clinical outcome, management consequence, or explicit no-diagnosis category in that group. Prospective and retrospective cohorts, hospital or population screening programs, implementation studies, and maternity/newborn screening studies were eligible. Case reports, reviews without original data, studies without an extractable CCHD-negative failed-screen denominator, and overlapping reports without independent participant contribution were excluded from quantitative synthesis.

The analytic unit was the unique newborn after completion of the study's protocol-defined measurement/repeat sequence. An initially abnormal measurement that normalized on a protocol-defined repeat was classified as a pass and was not included in the final failed-screen denominator. Companion publications and potentially overlapping cohorts were linked and adjudicated separately from bibliographic deduplication. Multisite publications could contribute separate site/program units only when participant-level independence was supported.

## Primary denominator and outcomes

The primary denominator was the number of harmonized-CCHD-negative final failed screens. Historical study labels such as critical congenital heart disease, major congenital heart disease, or CCHD were retained for provenance but did not automatically determine the review denominator. Lesions were mapped under a harmonized target ontology. A documented protocol amendment clarified d-transposition of the great arteries and related lesion mapping; all 76 quantitative units were re-adjudicated under the amended rule before the final analytic dataset was locked and before any authoritative pooled estimates were generated.

The prespecified primary outcome was Strict CAN-CCHD. Strict CAN-CCHD required a clinically relevant non-CCHD condition accompanied by a documented qualifying management consequence, including treatment, respiratory or other organ support, escalation of care, neonatal intensive care unit (NICU) or special-care admission, altered or delayed disposition, or a clinically required follow-up pathway. Diagnosis alone was insufficient for Strict classification.

Expanded CAN-CCHD was a prespecified key secondary/sensitivity outcome. It included all Strict CAN-CCHD events plus clinically relevant non-CCHD diagnoses for which the primary report did not document a qualifying management consequence. Expanded CAN-CCHD therefore represents broader clinically relevant disease and must not be interpreted as documented actionability.

Prespecified secondary etiologic outcomes synthesized quantitatively were persistent pulmonary hypertension of the newborn (PPHN)/pulmonary hypertension (PH), respiratory disease, infection/sepsis, and other/non-target structural cardiac diagnoses. These categories were not assumed to be mutually exclusive and were never summed to reconstruct Expanded CAN-CCHD. A category that was not reported or not point-identifiable was treated as missing for that etiologic synthesis, not as zero.

## Data extraction, verification, and quality safeguards

Study-level extraction preserved total screened population, final failed screens, study-defined and harmonized CCHD counts, CAN-CCHD classification, explicit healthy/no-diagnosis status, unknown/unascertained outcomes, etiologic diagnoses, timing, setting, altitude, program-cluster identity, actionability evidence, and source/full-text provenance. For each extracted field, the workflow preserved the raw value, numeric value when applicable, source location, supporting source text, and verification status. Normal echocardiography was not equated with global health, and absence of a reported diagnosis was not recoded as healthy. No individual-level imputation was performed.

AI-generated extraction suggestions were segregated from verified data. Every analysis-relevant field required human verification or correction before it could enter the analytic dataset. Inclusion in the primary meta-analysis additionally required at least 90% ascertainment of outcomes among harmonized-CCHD-negative final failed screens and resolution of participant arithmetic, denominator convention, lesion mapping, and overlap/non-independence. Eligible units that did not satisfy these requirements were retained for sensitivity analysis, withheld because of unresolved data-quality questions, or considered unsuitable for quantitative pooling rather than receiving primary-analysis weight.

Because the evidence base consisted predominantly of heterogeneous screening implementation cohorts and the review estimand depended heavily on downstream diagnosis and actionability reporting, no single generic study-level risk-of-bias instrument was imposed post hoc. Instead, prespecified domain-specific quality-control criteria addressed outcome identifiability, ascertainment, missingness, overlap, target mapping, actionability documentation, and exclusion of unverified AI-suggested data. The absence of a separate validated risk-of-bias instrument is acknowledged as a limitation.

## Statistical analysis

The authoritative synthesis used a one-stage random-effects binomial-logistic-normal generalized linear mixed model (GLMM) with exact binomial likelihood, logit link, and no continuity correction. The inverse-logit of the model intercept is reported as the median-study probability: the probability corresponding to a study at the median of the random-effects distribution. Because this estimand can differ materially from the population-average probability when between-study heterogeneity is large, we also report the marginal mean obtained by integrating over the fitted random-effects distribution. Between-study heterogeneity is expressed as tau, the standard deviation of the random effect on the logit scale, together with a 95% prediction interval.

Profile-likelihood confidence intervals were used for the GLMM intercept. Numerical integration used 41-point Gauss-Hermite quadrature, with stability checks at 21, 31, 41, and 61 points and multiple optimizer starting values. Prespecified robustness analyses included the Expanded secondary/sensitivity outcome, a preserved historical pre-amendment framework, aggregation of the related Ibero-American Society of Neonatology (SIBEN) multisite report cluster,[12] leave-one-out refitting, beta-binomial random-effects modeling, and a conventional two-stage logit restricted maximum-likelihood (REML) model with Hartung-Knapp inference. Screening timing (<24 hours, >=24 hours, or mixed/uncertain) was examined using subgroup models and an omnibus GLMM meta-regression diagnostic. Setting and altitude meta-regression were prespecified but judged infeasible because covariate structure was sparse and unbalanced. Analyses were implemented in Python with NumPy, pandas, and SciPy; executable scripts and machine-readable outputs are archived in the repository.

Conventional funnel asymmetry tests, Egger/Begg tests, and trim-and-fill were not promoted because this was a single-proportion synthesis with boundary observations and strong genuine heterogeneity; under these conditions, funnel geometry is not a reliable diagnostic of publication bias. Reporting bias therefore cannot be statistically excluded and was treated as a limitation rather than adjusted with a funnel-derived pooled estimate.

# Results

## Evidence flow and primary analysis set

The final bibliographic corpus contained 219 resolved reports. Report-level adjudication classified 73 as eligible primary reports, 129 as excluded, 16 as companion or non-independent reports, and one as supporting material only. After cohort-overlap adjudication and multisite expansion, the eligible literature yielded 76 independent quantitative units. Twenty-eight units met all requirements for the primary meta-analysis; 40 were retained for sensitivity analyses only, three were withheld because of unresolved data-quality questions, and five were not suitable for quantitative pooling. None of the latter categories contributed primary-analysis weight.

The 28 independent primary units represented screening programs from Europe, Asia, Africa, North and South America, and Oceania. Most were well-baby or maternity screening programs, with limited out-of-hospital/home-birth representation; timing ranged from the first hours of life to post-24-hour or predischarge protocols. Together they contributed 1,999 harmonized-CCHD-negative final failed screens. Descriptively, 638 met the Strict CAN-CCHD primary outcome and 1,015 met the Expanded CAN-CCHD secondary/sensitivity outcome; these crude aggregate ratios are not the random-effects pooled estimates.

## Primary outcome: Strict CAN-CCHD

For the prespecified primary outcome, the one-stage GLMM yielded a median-study Strict CAN-CCHD probability of 17.0% (95% profile-likelihood confidence interval [CI], 3.1%-46.8%). The marginal mean probability was 33.8%. Between-study heterogeneity was extreme (tau=3.369), and the 95% prediction interval spanned approximately 0.03%-99.34%. Accordingly, 17.0% should not be interpreted as a universal patient-level prevalence; rather, it is the fitted probability for a study at the median of a very broad random-effects distribution.

## Key secondary/sensitivity outcome: Expanded CAN-CCHD

Expanded CAN-CCHD was markedly more common and less heterogeneous. The median-study probability was 69.4% (95% CI, 57.7%-81.4%), the marginal mean was 65.8%, tau was 1.110, and the 95% prediction interval was 20.4%-95.2%. The narrower separation between the median-study and marginal mean estimates and the less extreme prediction interval indicate a substantially more stable cross-program signal for the presence of clinically relevant alternative disease than for explicitly documented qualifying management consequences. Because Expanded CAN-CCHD does not require documented management consequences, this result must not be interpreted as a pooled estimate of actionability.

## Secondary etiologic outcomes

Outcome-specific exact-reporting syntheses demonstrated clinically recognizable alternative causes of failed screening. The median-study probability of other/non-target structural cardiac diagnoses was 26.6% (95% CI, 14.4%-43.0%; k=26), with marginal mean 33.0% and tau=1.556. Infection/sepsis was 16.7% (95% CI, 9.4%-24.2%; k=22), marginal mean 18.9%, tau=0.720. PPHN/PH was 10.3% (95% CI, 4.7%-16.3%; k=22), marginal mean 12.5%, tau=0.790. Respiratory disease was 8.7% (95% CI, 1.6%-23.0%; k=22), with a substantially higher marginal mean of 20.3% and tau=2.220, reflecting strong heterogeneity and high-yield programs. Because etiologic categories could overlap and reporting subsets differed, these percentages are not additive.

## Robustness and subgroup analyses

Core sensitivity analyses did not reverse the interpretation. Aggregating the related SIBEN multisite report cluster produced median-study probabilities of 17.2% for Strict and 69.0% for Expanded CAN-CCHD. In the preserved historical pre-amendment framework, estimates were 18.4% and 69.7%, respectively. Leave-one-out Strict estimates ranged from 14.8% to 21.1%, and Expanded estimates from 65.3% to 70.9%. Beta-binomial marginal means (33.5% Strict and 66.3% Expanded) closely matched the GLMM marginal means. Conventional two-stage logit REML models with Hartung-Knapp inference were supportive but not authoritative.

Timing-group distributions were 13 predominantly <24-hour units, six predominantly >=24-hour units, and nine mixed/uncertain units. The omnibus timing diagnostics did not demonstrate a clear subgroup association (Strict p=0.263; Expanded p=0.493). This is not evidence of equivalence. In particular, the >=24-hour Strict subgroup contained only three events among 97 observations and produced a boundary-heavy, numerically unstable GLMM; no authoritative pooled Strict estimate was promoted for that subgroup.

# Discussion

## Principal findings

This systematic review reframes a familiar diagnostic-accuracy category. A final failed CCHD pulse-oximetry screen that is negative for harmonized target CCHD is often not clinically uninformative. Across 28 independent primary units, the broader presence of clinically relevant alternative disease was common: the Expanded CAN-CCHD median-study probability was 69.4%. By contrast, the prespecified primary outcome - documented Strict CAN-CCHD - was lower and extremely heterogeneous, with a median-study probability of 17.0%, a marginal mean of 33.8%, and an exceptionally wide prediction interval. The distinction between these outcomes is central. Expanded CAN-CCHD describes broader disease recognition; Strict CAN-CCHD describes documented downstream actionability and is therefore strongly influenced by program design and reporting completeness.

The secondary etiologic analyses give clinical context to the broader signal. Other structural cardiac diagnoses outside the harmonized target were common, while infection/sepsis, PPHN/PH, and respiratory disease also contributed substantially in outcome-specific reporting subsets. This pattern is consistent with the physiology of pulse oximetry: the test detects hypoxemia rather than CCHD itself. CCHD is therefore one important cause of a failed screen, but not the only clinically important one.

## Relation to previous evidence and contemporary guidance

Previous systematic reviews appropriately focused on test accuracy for CCHD. Plana and colleagues found high specificity and moderate sensitivity, with a lower false-positive rate when screening occurred after 24 hours.[3] Earlier large prospective cohorts nevertheless repeatedly described clinically significant alternative pathology among CCHD false-positive screens. In the Swedish study by de-Wahl Granelli et al., 31 of 69 pulse-oximetry false positives had another significant cardiac, pulmonary, or infectious pathology.[5] In the PulseOx study, 40 of 169 false-positive infants had other illnesses requiring urgent medical intervention, in addition to six significant non-major congenital heart defects.[6] Arlettaz et al. found persistent pulmonary hypertension in five of seven infants with repeated low saturation who did not have congenital heart disease.[13] In an out-of-hospital/early-discharge program, important noncritical cardiac or other noncardiac pathology was identified in 62% of false-positive screens,[14] while a high-altitude Ethiopian cohort identified PPHN in 10 of 56 screen-positive newborns, with two of those infants subsequently found to have sepsis.[15]

The present review differs from those observations in two ways. First, it treats downstream clinical yield as the primary scientific question rather than an incidental description of false positives. Second, it separates documented actionability from the mere presence of clinically relevant disease. This distinction helps explain why an informal statement that many false positives have important disease can coexist with extreme heterogeneity in Strict CAN-CCHD: many screening publications were designed to establish CCHD accuracy, not to document every treatment, transfer, delayed discharge, or follow-up consequence in the CCHD-negative group.

The findings also align closely with contemporary AAP guidance. The 2025 AAP clinical report explicitly identifies non-CCHD hypoxemic conditions as a secondary benefit of screening and includes infection/sepsis, lung disease, noncritical congenital heart defects, and persistent pulmonary hypertension among secondary conditions detected by the screening pathway.[1] Our analysis provides a quantitative synthesis for that policy direction and suggests that downstream non-CCHD yield is not a marginal phenomenon.

## Clinical implications for pediatric cardiology and neonatal care

A failed CCHD screen is a clinical escalation event requiring evaluation of the cause of hypoxemia. Contemporary AAP guidance notes that non-CCHD causes should continue to be evaluated when CCHD is excluded,[1] and Saudi reports describe local pathways in which positive screens may prompt pediatric-cardiology referral or echocardiography.[8,9] The role of the pediatric cardiologist varies across health systems and should not be overstated. Nevertheless, when cardiology is involved early, the clinical task is broader than simply declaring the absence of target CCHD. A structurally reassuring echocardiogram does not resolve the reason for hypoxemia. Recognition of PPHN, infection, respiratory disease, or non-target structural heart disease may require communication, referral, treatment, altered disposition, or coordinated follow-up.

This point is particularly relevant in Saudi Arabia, where universal CCHD screening has been implemented nationally.[8] For pediatric cardiologists, the screening encounter can therefore be viewed as a diagnostic junction: exclusion of target CCHD is one objective, but recognition and expedited routing of alternative neonatal disease may contribute materially to the final care delivered. The current data do not show that cardiology involvement itself improves outcomes, and they do not assign ownership of noncardiac disease to cardiologists; they identify a population in which clinically relevant alternative disease is common.

## Implications for screening metrics and program evaluation

The term false positive should retain its standard statistical meaning when reporting CCHD screening specificity. The present findings do not argue for redefining diagnostic-accuracy metrics. They do suggest, however, that program evaluation should distinguish test-error burden from downstream clinical yield. A failed screen that does not detect target CCHD can simultaneously be a false positive for the target condition and a clinically useful signal of another hypoxemic disorder. Program dashboards and future studies could therefore report both the CCHD false-positive rate and structured downstream outcomes among CCHD-negative failed screens.

The extreme heterogeneity in Strict CAN-CCHD also provides a methodological lesson. It likely reflects a combination of real differences in populations, timing, referral thresholds, altitude, and program structure, as well as major differences in what investigators chose to document after CCHD was excluded. Standardized minimum datasets that capture alternative diagnosis, management, disposition, and follow-up after failed screening would permit more transportable estimates and more meaningful comparison among programs. The AAP recommendation to collect non-CCHD conditions is an important step in this direction.[1]

## Strengths and limitations

This review has several strengths. The evidence database was reconstructed independently from verified source records, with report identity, companion relationships, cohort overlap, and multisite structure adjudicated before quantitative weighting. The primary denominator was harmonized at lesion level rather than accepting each publication's historical target label. Actionability required explicit source evidence and was not inferred from diagnosis alone. Missing or non-point-identifiable outcomes were preserved rather than recoded as zero or healthy. The primary model used exact binomial likelihood without continuity correction, and extensive sensitivity analyses, quadrature validation, and leave-one-out analyses did not reverse the interpretation. The complete primary input, extraction audit trail, code, and machine-readable results are publicly available.

The review also has important limitations. First, Strict CAN-CCHD is documentation-sensitive. Many source studies were designed to assess CCHD screening accuracy and did not systematically record downstream treatment or disposition for CCHD-negative infants; Strict actionability is therefore likely to be under-ascertained in some programs. Expanded CAN-CCHD addresses diagnostic underdocumentation but must not be interpreted as proven actionability. Second, between-study heterogeneity, especially for Strict and respiratory outcomes, was very high; pooled values are summaries of a broad distribution rather than universal patient-level frequencies. Third, etiologic categories were variably reported and could overlap, requiring outcome-specific denominators. Fourth, no separate validated study-level risk-of-bias instrument or formal certainty-of-evidence framework was applied; quality control instead relied on prespecified criteria for outcome identifiability, ascertainment, missingness, overlap, and actionability. Fifth, Embase and Scopus/Web of Science were not available, although the search incorporated multiple public bibliographic and regional sources, supplementary Google Scholar, citation chasing, recent and grey-literature searches, and closing search waves. Sixth, final scientific adjudication was performed by a single physician investigator rather than two independent human reviewers; AI assistance did not constitute an independent reviewer. The human-verification gates reduced but cannot eliminate error associated with single-reviewer adjudication. Seventh, the exact ChatGPT model version was not prospectively frozen across all AI-assisted sessions, limiting tool-level reproducibility despite preservation of the scientific protocol, query specifications, decision rules, frozen datasets, and deterministic analysis code. Eighth, conventional funnel-based small-study bias inference was not considered valid for this boundary-heavy, highly heterogeneous single-proportion synthesis, so reporting bias cannot be excluded. Finally, the reconstructed review corpus contained 219 resolved reports but did not retain a fully auditable exact pre-deduplication source-occurrence denominator suitable for a conventional identification-stage PRISMA count; we therefore do not infer one.

# Conclusions

Among newborns with final failed pulse-oximetry screens who did not have harmonized target CCHD, clinically relevant alternative disease was common. The broader Expanded CAN-CCHD signal was relatively consistent across programs, whereas the prespecified primary outcome of specifically documented actionability varied markedly. CCHD false-positive screens should therefore not automatically be equated with clinically uninformative encounters. For neonatal teams and pediatric cardiologists involved in post-failure evaluation, exclusion of target CCHD may be only one part of the diagnostic task. Standardized reporting of alternative diagnoses and management consequences after failed screens would improve future program evaluation and clarify the full clinical value of newborn pulse-oximetry screening.

## Table 1. Primary and key secondary CAN-CCHD outcomes

| Outcome role | Outcome | k | Events / denominator* | Median-study probability, % (95% CI) | Marginal mean, % | tau | 95% prediction interval, % |
|---|---|---:|---:|---:|---:|---:|---:|
| Primary | Strict CAN-CCHD | 28 | 638 / 1,999 | 17.0 (3.1-46.8) | 33.8 | 3.369 | 0.03-99.34 |
| Secondary/sensitivity | Expanded CAN-CCHD | 28 | 1,015 / 1,999 | 69.4 (57.7-81.4) | 65.8 | 1.110 | 20.4-95.2 |

*Observed event/denominator totals are descriptive aggregates, not random-effects estimates. Strict CAN-CCHD is the prespecified primary outcome. Expanded CAN-CCHD is a prespecified secondary/sensitivity outcome and includes clinically relevant diagnoses without documented qualifying actionability. k denotes the number of contributing analytic units; CI, confidence interval.*

## Table 2. Secondary etiologic outcomes

| Secondary etiologic outcome | k | Events / denominator* | Median-study probability, % (95% CI) | Marginal mean, % | tau | 95% prediction interval, % |
|---|---:|---:|---:|---:|---:|---:|
| Other/non-target structural cardiac diagnosis | 26 | 280 / 1,952 | 26.6 (14.4-43.0) | 33.0 | 1.556 | 1.7-88.4 |
| Infection / sepsis | 22 | 212 / 1,063 | 16.7 (9.4-24.2) | 18.9 | 0.720 | 4.7-45.1 |
| PPHN / pulmonary hypertension | 22 | 148 / 1,071 | 10.3 (4.7-16.3) | 12.5 | 0.790 | 2.4-35.1 |
| Respiratory disease | 22 | 126 / 1,063 | 8.7 (1.6-23.0) | 20.3 | 2.220 | 0.12-88.1 |

*Observed event/denominator totals are descriptive aggregates, not random-effects estimates. Etiologic categories use outcome-specific reporting subsets, may overlap, and must not be summed to reconstruct Expanded CAN-CCHD. A diagnosis that was not reported or not point-identifiable was treated as missing for that outcome, not as zero. PPHN, persistent pulmonary hypertension of the newborn; k, number of contributing analytic units; CI, confidence interval.*

## Table 3. Core sensitivity and robustness analyses

| Analysis | Endpoint | k | Estimate | Interpretation |
|---|---|---:|---:|---|
| Historical pre-amendment framework | Strict | 26 | 18.4% (1.9-59.5) | No reversal; historical framework |
| Historical pre-amendment framework | Expanded | 26 | 69.7% (56.0-83.7) | No reversal |
| SIBEN multisite report-cluster aggregation | Strict | 27 | 17.2% (3.8-43.8) | No material change |
| SIBEN multisite report-cluster aggregation | Expanded | 27 | 69.0% (57.2-81.0) | No material change |
| Beta-binomial random-effects | Strict | 28 | 33.5% marginal mean | GLMM marginal mean 33.8% |
| Beta-binomial random-effects | Expanded | 28 | 66.3% marginal mean | GLMM marginal mean 65.8% |
| Conventional logit REML with Hartung-Knapp | Strict | 28 | 29.9% (16.8-47.4) | Supportive two-stage comparison |
| Conventional logit REML with Hartung-Knapp | Expanded | 28 | 60.4% (51.1-69.0) | Supportive two-stage comparison |
| Leave-one-out | Strict | 28 refits | 14.8%-21.1% | No single unit reverses conclusion |
| Leave-one-out | Expanded | 28 refits | 65.3%-70.9% | No single unit reverses conclusion |

*SIBEN, Ibero-American Society of Neonatology; GLMM, generalized linear mixed model; REML, restricted maximum likelihood.*

## Table 4. Evidence-set disposition and analytic inclusion

| Stage | Count | Role |
|---|---:|---|
| Resolved reports in the final review corpus | 219 | Bibliographic review corpus |
| Eligible primary reports | 73 | Primary-study eligibility |
| Companion or non-independent reports | 16 | Linked to primary reports; no independent report weight |
| Supporting report | 1 | Supporting material only |
| Excluded reports | 129 | Excluded after full eligibility adjudication |
| Independent quantitative units | 76 | After overlap resolution and multisite expansion |
| Units included in the primary meta-analysis | 28 | Authoritative primary synthesis |
| Units retained for sensitivity analyses only | 40 | No primary-analysis weight |
| Units withheld for unresolved data-quality questions | 3 | Excluded from primary synthesis |
| Units not suitable for quantitative pooling | 5 | No primary-analysis weight |

The 28 primary analytic units shown in Figures 1 and 2 derive from 27 unique primary reports because the Rosario and Barranquilla SIBEN site-level units originate from the same multicenter report. Study labels in both figures include the corresponding bibliography number.[5,6,12,13,15-37]

![Figure 1. Strict CAN-CCHD study-level proportions](../analysis/phase6/figures/forest_strict.svg)

*Figure 1. Study-level Strict CAN-CCHD proportions among harmonized-CCHD-negative final failed pulse-oximetry screens. Bracketed numbers after study labels are bibliography reference numbers. Points show observed unit proportions; the authoritative random-effects synthesis used a one-stage exact-binomial logistic-normal GLMM. The pooled median-study probability was 17.0% (95% CI, 3.1%-46.8%), marginal mean 33.8%, tau 3.369, with extreme between-study heterogeneity.*

![Figure 2. Expanded CAN-CCHD study-level proportions](../analysis/phase6/figures/forest_expanded.svg)

*Figure 2. Study-level Expanded CAN-CCHD proportions among harmonized-CCHD-negative final failed pulse-oximetry screens. Bracketed numbers after study labels are bibliography reference numbers. Expanded CAN-CCHD includes Strict CAN-CCHD plus clinically relevant diagnoses for which qualifying actionability was not directly demonstrated. The median-study probability was 69.4% (95% CI, 57.7%-81.4%), marginal mean 65.8%, tau 1.110.*

# Declarations

Ethics approval: Not applicable. This systematic review synthesized published aggregate data and did not involve direct enrollment of human participants or access to identifiable patient-level data.

Funding: This research received no external funding.

Competing interests: The authors declare no competing interests.

AI use: Generative AI was used as described in the Methods for auditable research-support and writing tasks. Human authors retained responsibility for all scientific decisions, source verification, analysis, interpretation, and final manuscript content.

Data and code availability: The protocol, search specifications, final analysis inputs, extraction and audit documents, executable analysis scripts, and machine-readable results are available in the public CAN-CCHD repository: https://github.com/DitoLiberato/CAN-CCHD-Browser-Operator-Agent

# References

1. Oster ME, Pinto NM, Pramanik AK, Markowsky A, Schwartz BN, Kemper AR, et al. Newborn Screening for Critical Congenital Heart Disease: A New Algorithm and Other Updated Recommendations: Clinical Report. Pediatrics. 2025;155(1):e2024069667. doi:10.1542/peds.2024-069667.

2. Mahle WT, Newburger JW, Matherne GP, Smith FC, Hoke TR, Koppel R, et al. Role of pulse oximetry in examining newborns for congenital heart disease: a scientific statement from the American Heart Association and American Academy of Pediatrics. Circulation. 2009;120(5):447-458. doi:10.1161/CIRCULATIONAHA.109.192576.

3. Plana MN, Zamora J, Suresh G, Fernandez-Pineda L, Thangaratinam S, Ewer AK. Pulse oximetry screening for critical congenital heart defects. Cochrane Database Syst Rev. 2018;3(3):CD011912. doi:10.1002/14651858.CD011912.pub2.

4. Abouk R, Grosse SD, Ailes EC, Oster ME. Association of US State Implementation of Newborn Screening Policies for Critical Congenital Heart Disease With Early Infant Cardiac Deaths. JAMA. 2017;318(21):2111-2118. doi:10.1001/jama.2017.17627.

5. de-Wahl Granelli A, Wennergren M, Sandberg K, Mellander M, Bejlum C, Inganas L, et al. Impact of pulse oximetry screening on the detection of duct dependent congenital heart disease: a Swedish prospective screening study in 39,821 newborns. BMJ. 2009;338:a3037. doi:10.1136/bmj.a3037.

6. Ewer AK, Middleton LJ, Furmston AT, Bhoyar A, Daniels JP, Thangaratinam S, et al. Pulse oximetry screening for congenital heart defects in newborn infants (PulseOx): a test accuracy study. Lancet. 2011;378(9793):785-794. doi:10.1016/S0140-6736(11)60753-8.

7. Narayen IC, Blom NA, Ewer AK, Vento M, Manzoni P, te Pas AB. Aspects of pulse oximetry screening for critical congenital heart defects: when, how and why? Arch Dis Child Fetal Neonatal Ed. 2016;101(2):F162-F167. doi:10.1136/archdischild-2015-309205.

8. AlAql F, Khaleel H, Peter V. Universal Screening for CCHD in Saudi Arabia: The Road to a 'State of the Art' Program. Int J Neonatal Screen. 2020;6(1):13. doi:10.3390/ijns6010013.

9. Almawazini AM, Hanafi HK, Madkhali HA, Majrashi NB. Effectiveness of the critical congenital heart disease screening program for early diagnosis of cardiac abnormalities in newborn infants. Saudi Med J. 2017;38(10):1019-1024. doi:10.15537/smj.2017.10.20295.

10. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71.

11. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, et al.; PRISMA-S Group. PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. Syst Rev. 2021;10(1):39. doi:10.1186/s13643-020-01542-z.

12. Sola A, Golombek SG, Montes Bueno MT, Lemus-Varela L, Zuluaga C, Dominguez F, et al. CCHD Screening Implementation Efforts in Latin American Countries by the Ibero American Society of Neonatology (SIBEN). Int J Neonatal Screen. 2020;6(1):21. doi:10.3390/ijns6010021.

13. Arlettaz R, Bauschatz AS, Monkhoff M, Essers B, Bauersfeld U. The contribution of pulse oximetry to the early detection of congenital heart disease in newborns. Eur J Pediatr. 2006;165(2):94-98. doi:10.1007/s00431-005-0006-y.

14. Narayen IC, Blom NA, Bourgonje MS, Haak MC, Smit M, Posthumus F, et al. Pulse Oximetry Screening for Critical Congenital Heart Disease after Home Birth and Early Discharge. J Pediatr. 2016;170:188-192.e1. doi:10.1016/j.jpeds.2015.12.004.

15. Tekleab AM, Sewnet YC. Role of pulse oximetry in detecting critical congenital heart disease among newborns delivered at a high altitude setting in Ethiopia. Pediatr Health Med Ther. 2019;10:83-88. doi:10.2147/PHMT.S217987.

16. Reddy GC, Devaraj KN. Can pulse oxymetry be used as a routine screening tool in early diagnosis of critical congenital heart diseases in newborns? Int J Contemp Pediatr. 2018;5(3):867-872. doi:10.18203/2349-3291.ijcp20181504.

17. Carlson T, compiler and reviewer. Routine Pulse Oximetry Screening to Detect Critical Cyanotic Congenital Heart Disease in Neonates After Birth - Why is it Important for an Obstetrician to be Aware? Neonatology Today. May 2017:10-14.

18. Murni IK, et al. Feasibility of screening for critical congenital heart disease using pulse oximetry in Indonesia. BMC Pediatr. 2022;22:369. doi:10.1186/s12887-022-03404-0.

19. Shah H, Mansukhlal DV, Modi N, Haodijam SD, Singhvi A, Jasani JR, Bhavsar N. Role of Pulse Oximetry Screening for Term Healthy Newborns During Transitional Period to Detect Critical Congenital Heart Disease (CCHD): A Prospective Observational Study in a Tertiary Care Hospital. Cureus. 2026;18(5):e108873. doi:10.7759/cureus.108873.

20. Singh Y, Chen SE. Impact of pulse oximetry screening to detect congenital heart defects: 5 years' experience in a UK regional neonatal unit. Eur J Pediatr. 2022;181(2):813-821. doi:10.1007/s00431-021-04275-w.

21. Cloete E, Gentles TL, Webster DR, Davidkova S, Dixon LA, Alsweiler JM, et al. Pulse oximetry screening in a midwifery-led maternity setting with high antenatal detection of congenital heart disease. Acta Paediatr. 2020;109(1):100-108. doi:10.1111/apa.14934.

22. Cawsey MJ, Noble S, Cross-Sudworth F, Ewer AK. Feasibility of pulse oximetry screening for critical congenital heart defects in homebirths. Arch Dis Child Fetal Neonatal Ed. 2016;101(4):F349-F351. doi:10.1136/archdischild-2015-309936.

23. Johnson LC, Lieberman E, O'Leary E, Geggel RL. Prenatal and newborn screening for critical congenital heart disease: findings from a nursery. Pediatrics. 2014;134(5):916-922. doi:10.1542/peds.2014-1461.

24. Diller CL, Kelleman MS, Kupke KG, Quary SC, Kochilas LK, Oster ME. A Modified Algorithm for Critical Congenital Heart Disease Screening Using Pulse Oximetry. Pediatrics. 2018;141(5):e20174065. doi:10.1542/peds.2017-4065.

25. Cubells E, Torres B, Nunez-Ramiro A, Sanchez-Luna M, Izquierdo I, Vento M. Congenital Critical Heart Defect Screening in a Health Area of the Community of Valencia (Spain): A Prospective Observational Study. Int J Neonatal Screen. 2018;4(1):3. doi:10.3390/ijns4010003.

26. Klausner R, Shapiro ED, Elder RW, Colson E, Loyal J. Evaluation of a Screening Program to Detect Critical Congenital Heart Defects in Newborns. Hosp Pediatr. 2017;7(4):214-218. doi:10.1542/hpeds.2016-0176.

27. Jones AJ, Howarth C, Nicholl R, Mat-Ali E, Knowles R. The impact and efficacy of routine pulse oximetry screening for CHD in a local hospital. Cardiol Young. 2016;26(7):1397-1405. doi:10.1017/S1047951115002784.

28. Hamilcikan S, Can E. Critical congenital heart disease screening with a pulse oximetry in neonates. J Perinat Med. 2018;46(2):203-207. doi:10.1515/jpm-2017-0006.

29. Abu Lehyah NAA, Hasan AA, Abbad MY, Al-Jammal RA, Al Tarawneh MK, Abu Nasrieh D, et al. Prospective Evaluation of Pulse Oximetry Screening for Critical Congenital Heart Disease in a Jordanian Tertiary Hospital: High Incidence and Early Detection Challenges. Pediatr Rep. 2025;17(1):23. doi:10.3390/pediatric17010023.

30. Florez-Munoz SL, Rubiano-Pedroza JA, Molina-Medina CN, Lozada-Munoz A, Rocha-Pacheco LM. Tamizaje con oximetria de pulso en el diagnostico de cardiopatias congenitas criticas en recien nacidos. Rev Colomb Cardiol. 2021;28(6):583-589. doi:10.24875/rccar.m21000100.

31. El Idrissi Slitine N, Bennaoui F, Sable CA, Martin GR, Hom LA, Fadel A, et al. Pulse Oximetry and Congenital Heart Disease Screening: Results of the First Pilot Study in Morocco. Int J Neonatal Screen. 2020;6(3):53. doi:10.3390/ijns6030053.

32. van Niekerk AM, Cullis RM, Linley LL, Zuhlke L. Feasibility of Pulse Oximetry Pre-discharge Screening Implementation for detecting Critical Congenital heart Lesions in newborns in a secondary-level maternity hospital in the Western Cape, South Africa: The 'POPSICLe' study. S Afr Med J. 2016;106(8):817-821. doi:10.7196/SAMJ.2016.v106i8.10071.

33. Ozalkaya E, Akdag A, Sen I, Comert E, Yaren HM. Early screening for critical congenital heart defects in asymptomatic newborns in Bursa province. J Matern Fetal Neonatal Med. 2016;29(7):1105-1107. doi:10.3109/14767058.2015.1035642.

34. Jawin V, Ang HL, Omar A, Thong MK. Beyond Critical Congenital Heart Disease: Newborn Screening Using Pulse Oximetry for Neonatal Sepsis and Respiratory Diseases in a Middle-Income Country. PLoS One. 2015;10(9):e0137580. doi:10.1371/journal.pone.0137580.

35. Turska-Kmiec A, Borszewska-Kornacka MK, Blaz W, Kawalec W, Zuk M. Early screening for critical congenital heart defects in asymptomatic newborns in Mazovia province: experience of the POLKARD pulse oximetry programme 2006-2008 in Poland. Kardiol Pol. 2012;70(4):370-376.

36. Riede FT, Worner C, Dahnert I, Mockel A, Kostelka M, Schneider P. Effectiveness of neonatal pulse oximetry screening for detection of critical congenital heart disease in daily clinical routine-results from a prospective multicenter study. Eur J Pediatr. 2010;169(8):975-981. doi:10.1007/s00431-010-1160-4.

37. Meberg A, Brugmann-Pieper S, Due R Jr, Eskedal L, Fagerli I, Farstad T, et al. First day of life pulse oximetry screening to detect congenital heart defects. J Pediatr. 2008;152(6):761-765. doi:10.1016/j.jpeds.2007.12.043.
