# CAN-CCHD Phase 11 — Manuscript Authorship and Publication-Language Lock

Date: 2026-08-25  
Branch: `phase11-manuscript`  
Status: **AUTHORSHIP/DECLARATIONS UPDATED; PUBLICATION-FACING LANGUAGE NORMALIZED**

## Manuscript title

**Beyond CCHD: Clinically Relevant Disease After Failed Newborn Pulse Oximetry Screening — A Systematic Review and Meta-analysis**

The manuscript is now presented as a scientific article only. Award- or conference-specific wording must not appear in the manuscript body or title page.

## Author order

1. Rodrigo Liberato de Oliveira, MD
2. Mansour Almotairi
3. Mohammed Aloqmani
4. Abdullah Alrashidi
5. Saeed Alghamdi
6. Adnan Aselan
7. Shaimaa Rakha

## Affiliations

1. Madinah Cardiac Center, Madinah, Saudi Arabia
2. Madinah Maternity and Children's Hospital, King Salman Medical City, Madinah, Saudi Arabia
3. Department of Pediatrics, Faculty of Medicine, Mansoura University, Egypt
4. Ohud Hospital, Madinah, Saudi Arabia

Author-affiliation mapping:

- Rodrigo Liberato de Oliveira — 2
- Mansour Almotairi — 1
- Mohammed Aloqmani — 1
- Abdullah Alrashidi — 1
- Saeed Alghamdi — 2
- Adnan Aselan — 2
- Shaimaa Rakha — 2, 3, 4

## Professional titles retained for portal metadata

- Mansour Almotairi — Pediatric Interventional Cardiology Consultant, Madinah Cardiac Center
- Mohammed Aloqmani — Pediatric Cardiology Consultant; Medical Director, Madinah Cardiac Center
- Abdullah Alrashidi — Pediatric Cardiology Consultant; Head of Pediatric Cardiology Department, Madinah Cardiac Center
- Saeed Alghamdi — Pediatric Cardiology Consultant; Head of Pediatric Cardiology Department, Madinah Maternity and Children's Hospital, King Salman Medical City
- Adnan Aselan — Pediatric Cardiology Consultant, Madinah Maternity and Children's Hospital, King Salman Medical City
- Shaimaa Rakha — Professor of Pediatric Cardiology, Mansoura University, Egypt; Pediatric Cardiology Consultant, Ohud Hospital; Pediatric Cardiology Consultant, Madinah Maternity and Children's Hospital, King Salman Medical City

These professional titles are not placed in the manuscript byline unless a target journal explicitly requests them.

## Declarations

**Funding:** This research received no external funding.

**Competing interests:** The authors declare no competing interests.

## Publication-facing terminology rule

Repository state labels and engineering/audit vocabulary must not leak into the submitted scientific manuscript.

The following internal labels remain valid in the repository but are prohibited in publication-facing prose and tables:

- `PRIMARY_POOLABLE`
- `SENSITIVITY_ONLY`
- `HOLD_PENDING_QA`
- `NOT_POOLABLE`
- Phase-number shorthand when not scientifically necessary
- internal report IDs such as `R125` when the study/program name can be used instead
- `restart-native` when ordinary scientific provenance language is sufficient

Publication-facing replacements are descriptive scientific prose, for example:

- `PRIMARY_POOLABLE` → **units included in the primary meta-analysis**
- `SENSITIVITY_ONLY` → **units retained for sensitivity analyses only**
- `HOLD_PENDING_QA` → **units withheld because of unresolved data-quality questions**
- `NOT_POOLABLE` → **units not suitable for quantitative pooling**
- `R125/SIBEN` → **SIBEN multisite report cluster**
- `Phase 6 database freeze` → **final analytic dataset lock**
- `restart-native corpus` → **reconstructed/verified review corpus**

This is a writing-layer change only. No scientific value, eligibility decision, numerator, denominator, model, result, sensitivity analysis, or frozen Phase 6 estimate is altered.

## Scientific QA statement

The neutral manuscript version has been checked to ensure that none of the four underscore-style internal disposition labels remain in the manuscript text or tables. Funding and competing-interest placeholders have been replaced with the confirmed declarations above. Award-specific wording has been removed.
