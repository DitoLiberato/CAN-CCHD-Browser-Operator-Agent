# CAN-CCHD Phase 6 — Small-study / Reporting-bias Decision

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **DECISION COMPLETE — NO FORMAL FUNNEL-ASYMMETRY TEST PROMOTED**

## 1. Prespecified boundary

The locked Statistical Analysis Plan stated that the endpoint is a single proportion, not a comparative treatment effect, and that funnel-plot asymmetry tests would be exploratory only if technically interpretable. They were never allowed to determine inclusion/exclusion or alter the primary conclusion.

This decision is made after the primary/secondary synthesis but without changing any frozen scientific value.

## 2. Decision

**Do not perform or report Egger regression, Begg rank-correlation, trim-and-fill, or a conventional funnel plot as an inferential test of publication bias for the CAN-CCHD proportional meta-analysis.**

A descriptive effect-versus-size diagnostic may be generated for internal/supplementary visualization if desired, but it must be labelled as a small-study pattern display rather than a publication-bias test.

No bias-adjusted pooled estimate will be generated.

## 3. Why conventional funnel inference is not defensible here

The dataset has several features that directly violate or destabilize the usual funnel/asymmetry interpretation:

1. **Single-group proportional endpoint.** There is no natural positive-versus-negative treatment-effect result whose statistical significance plausibly governs publication selection.
2. **Boundary proportions.** The primary data contain many 0/n and n/n observations. Any conventional logit funnel requires continuity corrections or transformations that are not part of the primary exact-binomial GLMM.
3. **Strong genuine heterogeneity.** Strict CAN-CCHD has extreme between-study heterogeneity and an exceptionally wide prediction interval; respiratory secondary outcomes are also highly heterogeneous. Funnel asymmetry under these conditions can reflect clinical/design differences rather than selective publication.
4. **Mean-variance dependence of proportions.** For a binomial proportion, sampling variance depends on the underlying proportion and denominator. A conventional effect-versus-standard-error funnel can therefore acquire structure even without selective publication.
5. **Very heterogeneous study denominators and screening pathways.** Small studies are not exchangeable miniatures of large programs; they differ in setting, timing, diagnostic detail, and reporting granularity.
6. **No defensible selection-model target.** Trim-and-fill would assume symmetry and invent missing studies around an arbitrary center, which would be especially misleading with this endpoint and heterogeneity structure.

## 4. Methodological support

This decision is consistent with proportional-meta-analysis guidance stating that Egger/Begg/funnel methods were developed for comparative data and that their assumptions are not established for proportional meta-analysis:

- Barker TH, Migliavaca CB, Stein C, et al. *Conducting proportional meta-analysis in different types of systematic reviews: a guide for synthesisers of evidence.* BMC Med Res Methodol. 2021;21:189. doi:10.1186/s12874-021-01381-z.

It is also consistent with methodological work warning that conventional funnel plots can be inaccurate or non-interpretable for prevalence/proportion syntheses:

- Cheema HA, Shahid A, Ehsan M, Ayyan M. *The misuse of funnel plots in meta-analyses of proportions: are they really useful?* Clin Kidney J. 2022;15(6):1209-1210. doi:10.1093/ckj/sfac035.
- Hunter JP, Saratzis A, Sutton AJ, et al. *In meta-analyses of proportion studies, funnel plots were found to be an inaccurate method of assessing publication bias.* J Clin Epidemiol. 2014;67:897-903.

## 5. What will be reported instead

The manuscript should report that:

- formal funnel-asymmetry tests were not used because this was a single-proportion synthesis with boundary observations and substantial genuine heterogeneity;
- reporting bias cannot therefore be excluded statistically;
- risk was addressed structurally through broad multi-source searching, regional/public databases, citation chasing, duplicate/companion reconciliation, and preservation of non-poolable/sensitivity evidence rather than through post-hoc funnel correction.

Suggested Methods sentence:

> Because this was a meta-analysis of single proportions with multiple boundary estimates and substantial genuine between-study heterogeneity, conventional funnel-plot asymmetry tests and trim-and-fill were considered non-interpretable and were not used as inferential tests of publication bias.

Suggested Discussion limitation sentence:

> Selective publication or selective etiologic reporting cannot be excluded; however, conventional funnel-based tests are poorly interpretable for this single-proportion evidence structure, so reporting-bias risk was addressed primarily through broad source retrieval and transparent outcome-specific missingness rather than statistical funnel correction.

## 6. Phase 6 consequence

The small-study/publication-bias decision is now closed. No additional inferential bias model is required before Phase 6 closeout.
