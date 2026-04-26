# Phase 0 — Research Plan and Protocol

## Purpose
The app must start with a protocol-driven research plan. No search, import, screening, extraction, or analysis is allowed before the plan is approved.

## Default Project
Title:
```text
Clinically Actionable Non-CCHD Diagnoses After Failed Newborn Pulse Oximetry Screening for Critical Congenital Heart Disease: A Systematic Review and Meta-analysis
```
Concept:
```text
CAN-CCHD = Clinically Actionable Non-CCHD Diagnoses
```

## Review Question
```text
Among newborns who fail pulse oximetry screening for critical congenital heart disease but are not diagnosed with CCHD, what proportion have clinically actionable non-CCHD diagnoses?
```

Primary denominator:
```text
CCHD-negative failed screens
```
Primary outcome:
```text
Any CAN-CCHD diagnosis among CCHD-negative failed screens
number_can_cchd / number_cchd_negative_failed
```
Secondary outcomes:
```text
PPHN / pulmonary hypertension
respiratory disease
infection / sepsis / sepsis workup
non-critical congenital heart disease
NICU admission
oxygen therapy or respiratory support
antibiotic treatment or sepsis workup
delayed discharge
echocardiography / cardiology review
no actionable diagnosis
```
Subcategories may overlap. Do not assume PPHN + respiratory + sepsis = CAN-CCHD unless the original study reports mutually exclusive categories.

## Inclusion Criteria
Include studies that:
```text
1. include newborns/neonates or a newborn screening population;
2. evaluate/report pulse oximetry screening;
3. relate to CCHD screening;
4. report failed/positive/abnormal screen data;
5. allow identification of failed screens in which CCHD was not diagnosed, directly or by calculation;
6. report diagnosis, clinical outcome, management, or no-diagnosis category among CCHD-negative failed screens.
```
Eligible designs: prospective/retrospective cohort, population/hospital/regional/national screening programs, implementation studies, maternity/newborn screening studies.

## Exclusion Criteria
Exclude from quantitative synthesis:
```text
not newborn/neonatal population
not human
not pulse oximetry screening
not CCHD screening
no failed/positive screen data
cannot identify CCHD-negative failed screens
no non-CCHD diagnosis/outcome/management/no-diagnosis category
no extractable or calculable denominator
case report
editorial/commentary/letter without original data
review article without original data
overlapping cohort where better report exists
NICU-only cohort, unless protocol marks as separate analysis
```

## Case Reports Policy
Case reports are not eligible for quantitative synthesis. Allowed statuses:
```text
citation_mining_only
conceptual_background_only
rare_CAN_CCHD_signal
excluded_from_quantitative_synthesis
```
They may identify references or illustrate the concept, but not estimate frequency.

## Title/Abstract Screening Principle
Be sensitive. Do not exclude merely because the abstract does not mention PPHN, false positives, respiratory disease, sepsis, or non-CCHD outcomes. If it appears to be newborn CCHD pulse oximetry screening but outcome details are unclear, mark **MAYBE**.

## Source Hierarchy
```text
1. PubMed/MEDLINE
2. Europe PMC
3. Embase, if available
4. Scopus or Web of Science, if available
5. LILACS/BVS
6. SciELO
7. IMEMR
8. Google Scholar, supplementary
9. Citation chasing
```
The user may mark a source as unavailable only with justification.

## Query Plan
### PubMed primary broad
```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal)
```
### PubMed focused failed-screen
```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal) AND ("false positive" OR "failed screen" OR "positive screen" OR "secondary condition" OR hypoxemia OR hypoxaemia OR "pulmonary hypertension" OR sepsis OR respiratory)
```
### PubMed PPHN sensitivity
```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "pulse oximetry screening" OR "oxygen saturation") AND ("persistent pulmonary hypertension" OR PPHN OR "pulmonary hypertension")
```
### LILACS/BVS multilingual
```text
("critical congenital heart disease" OR "cardiopatia congênita crítica" OR "cardiopatía congénita crítica") AND ("pulse oximetry" OR "oximetria de pulso" OR "oximetría de pulso") AND (newborn OR neonate OR neonatal OR "recém-nascido" OR "recién nacido")
```
If complex query fails, run simpler separate queries in English, Portuguese, and Spanish.
### IMEMR
```text
critical congenital heart disease pulse oximetry newborn
congenital heart disease pulse oximetry neonate
pulse oximetry newborn screening
Saudi pulse oximetry congenital heart disease newborn
```
### Google Scholar supplementary
```text
"critical congenital heart disease" "pulse oximetry" newborn screening
"critical congenital heart disease" "pulse oximetry" "false positive"
"CCHD screening" newborn "pulmonary hypertension"
"CCHD screening" PPHN
```
Google Scholar is supplementary, not a primary reproducible search.

## Protocol UI Requirements
Show review question, denominator, outcomes, criteria, case-report policy, source hierarchy, query plan, and QA rules. Buttons: Edit protocol, Approve protocol, Export protocol markdown, Reset to default CAN-CCHD protocol. No later phase unlocks until `protocol.status = approved`.
