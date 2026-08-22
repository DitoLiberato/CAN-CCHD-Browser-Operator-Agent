# CAN-CCHD Phase 6 — Secondary Analysis Implementation Correction

Date: **2026-08-22**  
Status: **IMPLEMENTATION CORRECTED / SCIENTIFIC VALUES UNCHANGED**  
Branch target: `phase11-sha-abstract`  
Adversarial-review source commit: `0e0f6334abf7f75a3d9e65bc3785701aa194ffd6`

## Classification

This is an **analysis-implementation correction**, not a database amendment, protocol amendment, eligibility amendment, or re-analysis of the frozen scientific question.

The following remain unchanged:

- the 28-unit primary membership;
- all frozen Phase 5 and Phase 6 inputs;
- Strict and Expanded definitions;
- primary and etiologic estimands;
- all publication-facing Phase 6 numerical results.

`PHASE6_DATABASE_AMENDMENT` is **not** indicated.

## Defect identified

`analysis/phase6/run_phase6_secondary.py` forced a profile-likelihood confidence interval for every timing subgroup. The sparse/boundary-heavy Strict `>=24h_predominant` subgroup has:

- `k=6`;
- `3/97` events;
- median-unit probability `0.0036307691`;
- `tau=6.0872495`.

Its profile-likelihood limits cannot be bracketed numerically. The previous script therefore raised:

```text
ValueError: f(a) and f(b) must have different signs
```

and aborted before writing the complete secondary output set. The committed result files already treated this subgroup as fragile and did not promote it, but the executable did not reproduce that decision safely.

## Correction implemented

The secondary runner now:

1. attempts the prespecified profile-likelihood interval;
2. if numerical bracketing fails, refits the same model without fabricating an interval;
3. records `profile_status=NOT_ESTIMABLE_NUMERICALLY`;
4. leaves `ci_low` and `ci_high` blank;
5. retains the point estimate, marginal mean, tau, prediction interval and Hessian diagnostics;
6. continues the remaining subgroup, etiologic and timing meta-regression analyses;
7. writes a stable, publication-facing JSON schema matching the curated Phase 6 result package.

No fallback Wald interval or continuity correction was introduced.

## Reproduction command

```bash
python analysis/phase6/run_phase6_secondary.py \
  --primary-input data/phase6/PHASE6_PRIMARY_ANALYSIS_INPUT_v1.0.csv \
  --etiology-input data/phase6/PHASE6_ETIOLOGIC_SECONDARY_DERIVATION_v1.0.csv \
  --outdir analysis/phase6/results
```

The corrected command completed with exit status `0` and regenerated:

- `phase6_secondary_results.json`;
- `phase6_subgroup_results.csv`;
- `phase6_etiology_study_results.csv`.

## Scientific-value verification

The principal q=41 etiologic results reproduced the frozen values:

| Outcome | k | Median-unit probability | 95% CI | Marginal mean | tau |
|---|---:|---:|---:|---:|---:|
| PPHN | 22 | 10.2902% | 4.7222%–16.2797% | 12.5011% | 0.790404 |
| Respiratory | 22 | 8.7141% | 1.6034%–23.0394% | 20.2600% | 2.219665 |
| Infection | 22 | 16.7124% | 9.4375%–24.2227% | 18.9066% | 0.720005 |
| Other/non-target structural cardiac | 26 | 26.5918% | 14.3912%–43.0135% | 32.9620% | 1.556224 |

Lower-order quadrature-validation fits may differ in the last optimizer digits across runs; the largest observed difference was below `9e-6` in tau. No reported estimate, rounded value, interpretation or inference changed.

## SHA and manuscript consequence

The SHA abstract values remain valid. For the later manuscript, this correction establishes an executable provenance chain and preserves the numerically non-estimable subgroup state rather than concealing or replacing it.

