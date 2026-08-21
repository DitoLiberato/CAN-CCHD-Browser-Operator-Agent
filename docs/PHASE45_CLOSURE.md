# CAN-CCHD Phase 4.5 — Closure

Date: 2026-08-21
Status: **PHASE 4.5 CLOSED / READY FOR PHASE 5**
Branch: `phase4-consolidation`

## Binding provenance

This closure applies exclusively to the August 2026 restarted systematic review. `RESTART_LEGACY_DATA_FIREWALL.md` remains binding. No legacy Browser Agent/database row contributes study membership, eligibility, numerator, denominator, diagnosis, overlap resolution, PRISMA count, or meta-analysis weight.

## Final Phase 4.5 evidence architecture

### Bibliographic master

`PHASE45_RESTART_REPORT_MASTER_v0.5_FROZEN.md`

- 219 resolved restart-native/reverified bibliographic reports.
- R001–R145 = 145 reports.
- NR001–NR074 = 74 reports.
- Two independent zero-new-primary waves achieved bibliographic saturation.
- Native occurrence PMID 22984710 remains `UNRESOLVED_NATIVE_EXPORT_OCCURRENCE`, without invented identity or scientific status, outside the 219.

### Terminal report eligibility

`PHASE45_TERMINAL_REPORT_STATUS_REGISTRY.md`

- INCLUDE_PRIMARY = **73**
- EXCLUDE_PRIMARY = **129**
- COMPANION_NONINDEPENDENT = **16**
- CONDITIONAL_SUPPORTING = **1**
- Total = **219**

Strict criterion-6 QA corrections are recorded in:
- `PHASE45_STRICT_QA_BORDERLINE_EARLY_REPORTS.md`
- `PHASE45_STRICT_QA_BORDERLINE_SECONDARY_SET.md`

Important corrections include exclusion of R004 Bakr, R005 Rosati, R012 Ruangritnamchai, R028 Janjua, R048 Taksande 2017 and R055 Taksande 2013 from primary synthesis under the final criterion-6 standard.

### Overlap/non-independence resolution

`PHASE45_OVERLAP_AND_NONINDEPENDENCE_RESOLUTION.md`

Key decisions:
- Birmingham R014/R027 has real April–July 2013 overlap → one main quantitative program unit represented by R027; R014 retained for supporting detail/sensitivity.
- Taipei R077 pilot (10/2013–3/2014) and R029 extended program (4/2014–6/2017) have no temporal participant overlap → two units, shared program-cluster ID.
- Dutch NR008 POLS (10/2013–10/2014) and R020 POLAR (7/2015–12/2016) have no participant overlap → two units, shared program-cluster ID.
- R125 SIBEN contains five quantitatively extractable site/program units: San Luis, Rosario, Barranquilla, Sonora, Guadalajara.

### Frozen unique extraction-unit inventory

`PHASE45_UNIQUE_QUANTITATIVE_UNITS_FROZEN.md`

- Eligible primary reports = 73.
- Birmingham overlap adjustment: −1 unit.
- R125 multisite expansion: +4 units relative to one report.
- **Frozen unique/non-overlapping Phase 5 extraction units = 76.**

The 76 units are unique/non-overlapping at the participant/sample level under currently available evidence. Program-level relatedness is retained with cluster identifiers for sensitivity/robust analyses.

## Important interpretation of 76

`76 extraction units` does **not** mean that 76 estimates will automatically enter the primary meta-analysis.

Phase 5 must determine, per unit:
- exact CCHD-negative failed-screen denominator;
- confirmed actionable CAN-CCHD numerator;
- transitional/non-actionable count;
- explicitly healthy/no-diagnosis count;
- diagnosis-not-reported/not-ascertained count;
- target-definition consistency;
- lesion-level actionability;
- category mutual exclusivity;
- missingness/ascertainment;
- timing, altitude, setting and population flags.

A unit can remain eligible for extraction while being held from a particular pooled analysis.

## Primary-pooling hold flags at Phase 5 entry

At minimum:
- R101: 360 algorithm-positive vs 189 study-defined true-positive denominator convention.
- R102: diagnostic-category mutual exclusivity.
- R126: abstract vs detailed CCHD-count discrepancy.
- R125 Sonora: 22 positives but reported categories sum to 24; no forced reconciliation.
- R030, R021, R023, R068, R069, R108, R109, R125 Barranquilla, R127, R128, R130, NR009, NR044, NR050, NR058, NR059 and NR062: lesion/target/actionability mapping as applicable.
- Missing/unascertained outcome fractions must remain explicit and never be recoded as healthy.

## Post-freeze amendments

A 2024 RCCSH article using the same Guayaquil cohort/data as R030 was found during strict QA. It is a duplicate/companion publication, creates no new independent cohort, and does not reopen bibliographic saturation.

Any genuinely new report discovered after this closure requires an explicit `POST_FREEZE_AMENDMENT` with provenance, rationale, and impact analysis; it cannot silently alter the frozen master.

## Phase 5 entry gate

Phase 5 starts from the 76-unit frozen inventory, not from the historical 156, raw 327 occurrences, or the legacy application database.

The first Phase 5 deliverable should be a structured extraction table with one row per quantitative unit and fields for:
- unit_id
- report_id(s)
- cohort/program cluster
- country/site
- screening population
- screening timing and algorithm
- total screened if reported
- final failed screens
- CCHD cases among failed screens
- CCHD-negative failed-screen denominator
- actionable CAN-CCHD numerator
- transitional/non-actionable
- explicitly healthy/no diagnosis
- diagnosis not reported/not ascertained
- diagnosis categories and overlap notes
- lesion/actionability mapping
- target-definition flag
- setting/NICU/mixed flag
- altitude flag
- missingness/ascertainment flag
- poolability status and hold reason
- source/full-text provenance

## Closure statement

**Phase 4.5 is closed.**

The systematic review now has a frozen, restart-native, legacy-firewalled, bibliographically saturated, strict-QA-adjudicated and overlap-resolved evidence base ready for structured Phase 5 extraction.