# CAN-CCHD Phase 4.5 — Zero Wave 1 Reconciliation

Date: 2026-08-21
Status: COMPLETE — ZERO NEW INDEPENDENT PRIMARY REPORTS
Branch: `phase4-consolidation`

## Purpose

After the recent/typo/grey expansion added NR049–NR066 and reset the saturation counter, run an independent recall strategy that does not simply repeat prior CCHD/false-positive queries.

`RESTART_LEGACY_DATA_FIREWALL.md` applies. No legacy app/database data were used.

## Search logic

The wave emphasized consequence/diagnosis language and spelling/translation variants rather than only disease labels:

- failed screen / failed pulse oximetry / persistent hypoxemia;
- PPHN / pulmonary hypertension;
- sepsis / pneumonia / respiratory disease;
- normal echocardiogram / structurally normal heart / other pathology;
- `oximetry` and `oxymetry`;
- English plus Spanish/Portuguese/French/regional phrasing;
- regional and grey-literature discovery;
- screening populations without requiring the acronym CCHD in the title.

Each candidate was reconciled against R001–R145 + NR001–NR066 before any new ID could be created.

## Important reconciliations

### PMID 27928258 — NOT NEW

*Evaluation of Pulse Oximetry in the Early Detection of Cyanotic Congenital Heart Disease in Newborns* (Movahedian et al., Iran, 2016) initially appeared as a possible delta.

Restart-native corpus reconciliation definitively maps it to **R079**. The v0.6 corpus already records R079 / PMID 27928258 with a note that persistent pulmonary hypertension occurs among positive screens.

No new report ID is created.

### Zuppa / Italy — NOT NEW

The Italian low-risk-newborn screen initially resurfaced through title variants. Restart-native metadata reconciliation confirms it is **R015 Zuppa**, PMID 24588079, DOI 10.3109/14767058.2014.899573.

No new report ID is created.

### Other consequence-language hits

Relevant hits converged to already represented reports/cohorts including Riede, Ewer/PulseOx, Meberg, Oakley, Jain, Qatar, Jordan, Morocco, West Virginia, Bagalkot, Nellore and other established R/NR identities.

No candidate survived bibliographic reconciliation as a new independent primary report.

## Result

- New independent primary report: **0**.
- New companion/context report requiring master expansion from this wave itself: **0**.
- Saturation counter after this wave: **1 consecutive zero-new-independent-primary wave**.

## Independence from prior discovery waves

This wave used diagnosis/consequence language, spelling variants and regional/grey phrasing rather than the recent-publication and direct citation-chasing strategies that discovered NR044 and NR049–NR066. It therefore counts as an independent zero wave under the prespecified two-zero-wave rule.

## Next step

Run Zero Wave 2 using seed/author/backward-forward citation chasing from the newest high-yield anchors and established primary studies. Any new independent primary report resets the counter to zero.