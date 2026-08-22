# CAN-CCHD Phase 6 — Secondary Etiologic Outcomes and Subgroup Audit

Date: 2026-08-22  
Branch: `phase6-analysis`  
Status: **SECONDARY ETIOLOGIC OUTCOMES COMPLETE / SUBGROUP FEASIBILITY AUDIT COMPLETE**

## 1. Boundary and provenance

This work begins only after the 28-unit primary database was frozen, database-readiness gates A-H passed, and the core Strict/Expanded GLMM plus S1-S6 sensitivities were completed. No value in `data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv` was changed.

Secondary etiologic analyses use the frozen 28-unit primary membership only. Diagnosis-category numerators were derived from restart-native Phase 5 extraction blocks plus the post-rerun numeric overlay where target remapping changed denominator membership.

Canonical derivation artifact:

`data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv`

Reproducible implementation:

`analysis/phase6/run_phase6_secondary.py`

Machine-readable outputs:

- `analysis/phase6/results/phase6_secondary_results.json`
- `analysis/phase6/results/phase6_etiology_study_results.csv`
- `analysis/phase6/results/phase6_subgroup_results.csv`

## 2. Secondary-outcome derivation rule locked before pooling

The protocol prespecified etiologic categories and explicitly allowed them to overlap. A diagnosis category is not itself an actionability label.

For these analyses, an outcome-specific study contribution is allowed only when its numerator is **point-identifiable** from frozen extraction evidence.

Binding rule:

> `not reported`, broad aggregate disease labels, and participant-level overlap that prevents an exact category count are **missing for that outcome, not zero**.

Each etiologic outcome therefore has its own eligible subset. The full harmonized-CCHD-negative denominator of an eligible unit remains the denominator for that category.

Operational definitions:

1. **PPHN / pulmonary hypertension** — explicit participant-level PPHN or pulmonary-hypertension diagnosis.
2. **Respiratory disease** — explicit pulmonary/respiratory disease such as TTN, pneumonia, meconium aspiration, pneumothorax or pulmonary hypoplasia. Respiratory symptoms alone do not qualify.
3. **Infection / sepsis** — explicit sepsis or infection. Pneumonia can contribute to both respiratory and infection categories when the diagnosis supports both.
4. **Other/non-target structural cardiac diagnosis** — structural cardiac disease remaining in the harmonized-CCHD-negative denominator. This operationalizes the protocol's `non-critical CHD` secondary category under the harmonized target. PFO and explicitly physiologic/transitional PDA findings are excluded.

Etiologic categories may overlap and must never be summed to reconstruct Expanded CAN-CCHD.

## 3. PPHN / pulmonary hypertension

Eligible: **22/28 units**; 6 were not point-identifiable for this outcome.

Observed in eligible units: **148 / 1,071** (crude 13.8%; descriptive only).

One-stage binomial-logistic-normal GLMM:

- median-study probability: **10.3%**;
- 95% profile-likelihood CI: **4.7% to 16.3%**;
- marginal mean probability: **12.5%**;
- tau: **0.790**;
- tau²: **0.625**;
- 95% prediction interval: **2.4% to 35.1%**.

The solution is stable across 21/31/41/61 adaptive quadrature points.

## 4. Respiratory disease

Eligible: **22/28 units**; 6 not point-identifiable.

Observed: **126 / 1,063** (crude 11.9%).

GLMM:

- median-study probability: **8.7%**;
- 95% CI: **1.6% to 23.0%**;
- marginal mean: **20.3%**;
- tau: **2.220**;
- tau²: **4.927**;
- 95% prediction interval: approximately **0.12% to 88.1%**.

Respiratory diagnoses show very large between-program heterogeneity. The median-study and marginal estimands should both be reported.

## 5. Infection / sepsis

Eligible: **22/28 units**; 6 not point-identifiable.

Observed: **212 / 1,063** (crude 19.9%).

GLMM:

- median-study probability: **16.7%**;
- 95% CI: **9.4% to 24.2%**;
- marginal mean: **18.9%**;
- tau: **0.720**;
- tau²: **0.518**;
- 95% prediction interval: **4.7% to 45.1%**.

## 6. Other/non-target structural cardiac diagnosis

Eligible: **26/28 units**; 2 not point-identifiable.

Observed: **280 / 1,952** (crude 14.3%).

GLMM:

- median-study probability: **26.6%**;
- 95% CI: **14.4% to 43.0%**;
- marginal mean: **33.0%**;
- tau: **1.556**;
- tau²: **2.422**;
- 95% prediction interval: **1.7% to 88.4%**.

This category follows the review's harmonized target rather than each source's historical terminology. A lesion called `critical` by a source can remain here when it does not meet the locked harmonized target/event rule.

## 7. Timing subgroup audit

Prespecified timing harmonization of the 28 primary units:

- predominantly `<24 h`: **13**;
- predominantly `>=24 h`: **6**;
- mixed/uncertain/predischarge-not-exact: **9**.

### Predominantly <24 h

Strict: 564/1,733 observed; median-study **28.4%**, 95% CI **5.0%-67.7%**, marginal mean **37.9%**, tau **2.444**.

Expanded: median-study **62.6%**, 95% CI **45.9%-80.4%**, marginal mean **60.4%**, tau **1.035**.

### Predominantly >=24 h

Strict: only **3/97** events. The fit is boundary-heavy; tau is approximately 6-7 across quadrature orders and the profile-likelihood CI does not bracket reproducibly. **No formal Strict pooled estimate is promoted for this subgroup.** Report 3/97 descriptively and label the GLMM numerically fragile.

Expanded: 61/97 observed; median-study **80.8%**, 95% CI **50.1%-99.2%**, marginal mean **74.7%**, tau **1.341**; numerically stable.

### Mixed / uncertain

Strict: 71/169; median-study **26.7%**, 95% CI **0.7%-90.4%**, marginal mean **39.5%**, tau **3.371**.

Expanded: median-study **73.3%**, 95% CI **52.2%-91.0%**, marginal mean **70.0%**, tau **0.975**.

The very wide Strict intervals show that timing alone does not explain the dominant heterogeneity.

## 8. Timing meta-regression diagnostic

A three-level one-stage GLMM meta-regression was used only as a feasibility/omnibus diagnostic, with mixed/uncertain as reference and two timing coefficients. Quadrature stability was checked at 21/31/41/61 points.

Strict:

- likelihood-ratio chi-square, 2 df: **2.67**;
- p = **0.263**;
- residual tau ≈ **3.06**.

Expanded:

- likelihood-ratio chi-square, 2 df: **1.41**;
- p = **0.493**;
- residual tau ≈ **1.07**.

No clear timing-group effect is demonstrated. This is **not evidence of equivalence**: the >=24 h group has only six units and its Strict fit is weakly identified.

## 9. Setting and altitude feasibility

Setting labels are heterogeneous and almost entirely hospital-based. There is only **one** truly out-of-hospital/homebirth primary unit. **No formal setting meta-regression** is defensible; post-hoc collapsing would be arbitrary.

Altitude is not reported in **25/28** primary units. There is one sea-level unit, one <250 m unit and one high-altitude 2600 m unit. **No formal altitude subgroup/meta-regression** is defensible. Addis Ababa remains descriptive context only.

## 10. Phase 6 consequence

Completed in this block:

- audited etiologic derivation across all 28 primary units;
- four outcome-specific etiologic GLMMs using exact-reporting subsets;
- timing subgroup GLMM audit;
- timing categorical meta-regression diagnostic;
- formal infeasibility decisions for setting and altitude;
- machine-readable reproducibility outputs.

No primary database amendment occurred.

## 11. Remaining Phase 6 work

1. decide whether publication-bias/small-study display is technically interpretable; exploratory only;
2. build manuscript-ready primary/secondary/sensitivity tables;
3. finalize figure captions and decide which secondary figures belong in the manuscript/supplement;
4. write final Phase 6 results summary and reporting QA;
5. freeze a Phase 6 analysis-complete snapshot;
6. proceed to SHA abstract and manuscript drafting.

**Secondary etiologic outcomes and subgroup audit are complete.**
