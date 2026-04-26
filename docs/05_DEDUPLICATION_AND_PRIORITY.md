# Phase 2 — Deduplication and Prioritization

## Purpose
After Search Collection is complete, the app deduplicates records and creates a manageable screening set. The user cannot proceed to Title/Abstract Screening until deduplication is completed.

## Philosophy
```text
records = database hits/reports
studies = unique underlying studies/articles after deduplication
```
Preserve all records but merge them into one unique study when appropriate.

## Exact Deduplication
Exact matches may be bulk-merged with checkbox confirmation.

Exact match bases:
```text
same PMID
same DOI
same PMCID
same source_record_id within same source
same normalized exact title + same year
```
For 100% identifier match:
```text
create large duplicate group
select representative automatically
show checkbox list
allow bulk merge
```
Default representative selection:
```text
1. PMID present
2. DOI present
3. PMCID present
4. longest/most complete abstract
5. most complete metadata
6. source priority: PubMed > Embase > Scopus/WoS > Europe PMC > LILACS/BVS > SciELO > IMEMR > Google Scholar
```

## Bulk Merge UI
Show counts like:
```text
Exact PMID duplicates: 312 records in 96 groups
Exact DOI duplicates: 204 records in 72 groups
Exact PMCID duplicates: 15 records in 5 groups
Exact title/year duplicates: 48 records in 19 groups
```
User can select all exact groups, review representative, and bulk merge selected. Before merge, create database backup.

The app must show:
```text
This will not delete records. It will link records to representative studies and mark duplicate studies as merged_duplicate.
```

## Fuzzy Deduplication
Fuzzy title thresholds:
```text
>= 0.97 likely duplicate
0.90–0.96 possible duplicate
< 0.90 no automatic cluster unless author/year also match
```
Fuzzy groups require human review unless very high confidence and same year/author.
Actions: merge, keep separate, mark possible overlapping cohort, needs later review, reject suggestion.

## Merge Behavior
When merging:
```text
keep representative study
link all records to representative study
mark non-representative studies as merged_duplicate
preserve all source records
create study_links rows
write audit log
```
Never delete source records.

## Completion Conditions
Deduplication completes only when exact duplicates are merged/kept separate, high-confidence fuzzy groups are resolved, possible groups are resolved/deferred with justification, backup exists before bulk merge, and audit log is complete.

## Prioritization
After deduplication, calculate priority scores for unique studies. Priority orders work; it is not exclusion.

High relevance features include CCHD, critical congenital heart disease, pulse oximetry, oxygen saturation, newborn/neonate/neonatal, screening, program, cohort, population, prospective, implementation, false positive, failed screen, positive screen, PPHN, pulmonary hypertension, respiratory, sepsis, hypoxemia, NICU, echocardiography.

Negative relevance features include adult, prenatal only, fetal diagnosis only, animal, surgery only, postoperative outcome only, device engineering only, case report, editorial, commentary, not screening, not pulse oximetry, not CCHD.

Priority tiers:
```text
high
medium
low
very_low
needs_human_review
citation_mining_only
```

## Do-Not-Discard Protection
Mark `do_not_discard = true` if CCHD + pulse oximetry + newborn terms are present, or sentinel/landmark match, or major cohort/program signal, or regional relevance, or PPHN/failed-screen signal. Protected records cannot be excluded in bulk.

## Completion Gate
Unlock screening only when exact duplicates are complete, high-confidence fuzzy duplicates complete, priority scores calculated, do-not-discard applied, and deduplication report generated.
