# CAN-CCHD Review — Database Search Instructions and Query Set

## Study focus

**Review question**

Among newborns who fail pulse oximetry screening for critical congenital heart disease but are not diagnosed with CCHD, what proportion have clinically actionable non-CCHD diagnoses?

**Primary denominator**

```text
CCHD-negative failed screens
```

Equivalent wording:

```text
failed screens in which CCHD was excluded
```

**Primary outcome**

```text
Any Clinically Actionable Non-CCHD Diagnosis (CAN-CCHD)
```

**Secondary outcomes**

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

---

# General methodological rule

Primary searches should be broad and sensitive.

Focused searches are supplementary.

Do **not** exclude studies at title/abstract stage only because non-CCHD outcomes are not mentioned in the abstract. Many eligible studies may report these data only in the full text.

If a title/abstract appears to describe newborn CCHD pulse oximetry screening but the non-CCHD outcomes are unclear, mark:

```text
MAYBE
```

---

# Recommended source order

```text
1. PubMed / MEDLINE
2. Europe PMC
3. Embase
4. Scopus or Web of Science
5. LILACS / BVS
6. SciELO
7. IMEMR
8. Google Scholar, supplementary only
9. Citation chasing
```

---

# 1. PubMed / MEDLINE

## Access mode

```text
API-autonomous or manual browser search
```

## Export/import recommendation

If using browser manually, export as:

```text
PubMed XML
RIS
CSV
NBIB
```

Preferred for app import:

```text
PubMed XML or RIS
```

## PubMed — primary_broad

```text
("critical congenital heart disease"[Title/Abstract] OR CCHD[Title/Abstract]) AND ("pulse oximetry"[Title/Abstract] OR "oxygen saturation"[Title/Abstract]) AND (newborn[Title/Abstract] OR neonate[Title/Abstract] OR neonatal[Title/Abstract])
```

## PubMed — failed_screen_focused

```text
("critical congenital heart disease"[Title/Abstract] OR CCHD[Title/Abstract]) AND ("pulse oximetry"[Title/Abstract] OR "oxygen saturation"[Title/Abstract]) AND (newborn[Title/Abstract] OR neonate[Title/Abstract] OR neonatal[Title/Abstract]) AND ("false positive"[Title/Abstract] OR "failed screen"[Title/Abstract] OR "positive screen"[Title/Abstract] OR "screen positive"[Title/Abstract] OR "abnormal screen"[Title/Abstract] OR "secondary condition"[Title/Abstract] OR hypoxemia[Title/Abstract] OR hypoxaemia[Title/Abstract] OR "pulmonary hypertension"[Title/Abstract] OR PPHN[Title/Abstract] OR sepsis[Title/Abstract] OR respiratory[Title/Abstract])
```

## PubMed — pphn_sensitivity

```text
("critical congenital heart disease"[Title/Abstract] OR CCHD[Title/Abstract]) AND ("pulse oximetry"[Title/Abstract] OR "pulse oximetry screening"[Title/Abstract] OR "oxygen saturation"[Title/Abstract]) AND ("persistent pulmonary hypertension"[Title/Abstract] OR PPHN[Title/Abstract] OR "pulmonary hypertension"[Title/Abstract])
```

## PubMed — broader fallback without field tags

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal)
```

---

# 2. Europe PMC

## Access mode

```text
API-autonomous
```

## Export/import recommendation

Preferred:

```text
API JSON/XML
RIS if available
CSV if needed
```

## Europe PMC — primary_broad

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal)
```

## Europe PMC — failed_screen_focused

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal) AND ("false positive" OR "failed screen" OR "positive screen" OR "screen positive" OR "abnormal screen" OR "secondary condition" OR hypoxemia OR hypoxaemia OR "pulmonary hypertension" OR PPHN OR sepsis OR respiratory)
```

## Europe PMC — pphn_sensitivity

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "pulse oximetry screening" OR "oxygen saturation") AND ("persistent pulmonary hypertension" OR PPHN OR "pulmonary hypertension")
```

---

# 3. Embase

## Access mode

```text
Supervised-login
```

The agent should open the platform and pause for manual login. The user logs in. The agent must not store passwords.

## Export/import recommendation

Preferred:

```text
RIS
```

Alternatives:

```text
BibTeX
CSV
Excel
```

Export content:

```text
Full record
Citation and abstract
Keywords
DOI/PMID if available
```

## Embase.com — primary_broad

```text
('critical congenital heart disease':ti,ab,kw OR cchd:ti,ab,kw) AND ('pulse oximetry':ti,ab,kw OR 'oxygen saturation':ti,ab,kw) AND (newborn:ti,ab,kw OR neonate:ti,ab,kw OR neonatal:ti,ab,kw)
```

## Embase.com — failed_screen_focused

```text
('critical congenital heart disease':ti,ab,kw OR cchd:ti,ab,kw) AND ('pulse oximetry':ti,ab,kw OR 'oxygen saturation':ti,ab,kw) AND (newborn:ti,ab,kw OR neonate:ti,ab,kw OR neonatal:ti,ab,kw) AND ('false positive':ti,ab,kw OR 'failed screen':ti,ab,kw OR 'positive screen':ti,ab,kw OR 'screen positive':ti,ab,kw OR 'abnormal screen':ti,ab,kw OR 'secondary condition':ti,ab,kw OR hypoxemia:ti,ab,kw OR hypoxaemia:ti,ab,kw OR 'pulmonary hypertension':ti,ab,kw OR pphn:ti,ab,kw OR sepsis:ti,ab,kw OR respiratory:ti,ab,kw)
```

## Embase.com — pphn_sensitivity

```text
('critical congenital heart disease':ti,ab,kw OR cchd:ti,ab,kw) AND ('pulse oximetry':ti,ab,kw OR 'pulse oximetry screening':ti,ab,kw OR 'oxygen saturation':ti,ab,kw) AND ('persistent pulmonary hypertension':ti,ab,kw OR pphn:ti,ab,kw OR 'pulmonary hypertension':ti,ab,kw)
```

## Ovid Embase — primary_broad

```text
("critical congenital heart disease" OR CCHD).ti,ab,kw. AND ("pulse oximetry" OR "oxygen saturation").ti,ab,kw. AND (newborn OR neonate OR neonatal).ti,ab,kw.
```

## Ovid Embase — failed_screen_focused

```text
("critical congenital heart disease" OR CCHD).ti,ab,kw. AND ("pulse oximetry" OR "oxygen saturation").ti,ab,kw. AND (newborn OR neonate OR neonatal).ti,ab,kw. AND ("false positive" OR "failed screen" OR "positive screen" OR "screen positive" OR "abnormal screen" OR "secondary condition" OR hypoxemia OR hypoxaemia OR "pulmonary hypertension" OR PPHN OR sepsis OR respiratory).ti,ab,kw.
```

## Ovid Embase — pphn_sensitivity

```text
("critical congenital heart disease" OR CCHD).ti,ab,kw. AND ("pulse oximetry" OR "pulse oximetry screening" OR "oxygen saturation").ti,ab,kw. AND ("persistent pulmonary hypertension" OR PPHN OR "pulmonary hypertension").ti,ab,kw.
```

---

# 4. Scopus

## Access mode

```text
Supervised-login
```

The agent should open Scopus and pause for manual login. The user logs in. The agent resumes after user confirmation.

## Export/import recommendation

Preferred:

```text
RIS
```

Alternatives:

```text
CSV
BibTeX
```

Export fields:

```text
Citation information
Bibliographic information
Abstract
Keywords
DOI
PMID, if available
```

## Scopus — primary_broad

```text
TITLE-ABS-KEY(("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal))
```

## Scopus — failed_screen_focused

```text
TITLE-ABS-KEY(("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal) AND ("false positive" OR "failed screen" OR "positive screen" OR "screen positive" OR "abnormal screen" OR "secondary condition" OR hypoxemia OR hypoxaemia OR "pulmonary hypertension" OR PPHN OR sepsis OR respiratory))
```

## Scopus — pphn_sensitivity

```text
TITLE-ABS-KEY(("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "pulse oximetry screening" OR "oxygen saturation") AND ("persistent pulmonary hypertension" OR PPHN OR "pulmonary hypertension"))
```

---

# 5. Web of Science

## Access mode

```text
Supervised-login
```

The agent should open Web of Science and pause for manual login. The user logs in. The agent resumes after user confirmation.

## Export/import recommendation

Preferred:

```text
RIS
```

Alternatives:

```text
BibTeX
Excel
CSV
```

Export fields:

```text
Full record
Abstract
Cited references if available
DOI
PMID, if available
```

## Web of Science — primary_broad

```text
TS=(("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal))
```

## Web of Science — failed_screen_focused

```text
TS=(("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal) AND ("false positive" OR "failed screen" OR "positive screen" OR "screen positive" OR "abnormal screen" OR "secondary condition" OR hypoxemia OR hypoxaemia OR "pulmonary hypertension" OR PPHN OR sepsis OR respiratory))
```

## Web of Science — pphn_sensitivity

```text
TS=(("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "pulse oximetry screening" OR "oxygen saturation") AND ("persistent pulmonary hypertension" OR PPHN OR "pulmonary hypertension"))
```

---

# 6. LILACS / BVS

## Access mode

```text
Browser-supervised or manual export
```

The BVS interface may not support complex Boolean queries consistently. If the broad multilingual query fails, use the simpler language-specific searches.

## Export/import recommendation

Preferred:

```text
RIS
```

Alternatives:

```text
BibTeX
CSV
manual CSV
Zotero capture → RIS export
```

If BVS returns many MEDLINE results, apply database filter:

```text
LILACS
```

## LILACS/BVS — multilingual_broad

```text
("critical congenital heart disease" OR "cardiopatia congênita crítica" OR "cardiopatia congenita critica" OR "cardiopatía congénita crítica" OR "cardiopatia congenita critica") AND ("pulse oximetry" OR "oximetria de pulso" OR "oximetría de pulso") AND (newborn OR neonate OR neonatal OR "recém-nascido" OR "recem-nascido" OR "recien nacido" OR "recién nacido")
```

## LILACS/BVS — english_simple

```text
"critical congenital heart disease" AND "pulse oximetry" AND newborn
```

## LILACS/BVS — portuguese_simple

```text
"cardiopatia congênita" AND "oximetria de pulso" AND "recém-nascido"
```

## LILACS/BVS — portuguese_no_accents

```text
cardiopatia congenita AND oximetria de pulso AND recem-nascido
```

## LILACS/BVS — spanish_simple

```text
"cardiopatía congénita" AND "oximetría de pulso" AND "recién nacido"
```

## LILACS/BVS — spanish_no_accents

```text
cardiopatia congenita AND oximetria de pulso AND recien nacido
```

## LILACS/BVS — broader_portuguese

```text
cardiopatia AND oximetria AND neonatal
```

---

# 7. SciELO

## Access mode

```text
API if available, otherwise browser-supervised
```

## Export/import recommendation

Preferred:

```text
RIS
```

Alternatives:

```text
BibTeX
CSV
manual CSV
Zotero capture
```

## SciELO — multilingual_broad

```text
("critical congenital heart disease" OR "cardiopatia congênita crítica" OR "cardiopatia congenita critica" OR "cardiopatía congénita crítica") AND ("pulse oximetry" OR "oximetria de pulso" OR "oximetría de pulso") AND (newborn OR neonate OR neonatal OR "recém-nascido" OR "recem-nascido" OR "recién nacido" OR "recien nacido")
```

## SciELO — portuguese_simple

```text
"cardiopatia congênita" "oximetria de pulso" "recém-nascido"
```

## SciELO — portuguese_no_accents

```text
cardiopatia congenita oximetria pulso neonatal
```

## SciELO — english_simple

```text
"critical congenital heart disease" "pulse oximetry" newborn
```

## SciELO — spanish_simple

```text
"cardiopatía congénita" "oximetría de pulso" "recién nacido"
```

---

# 8. IMEMR

## Access mode

```text
Browser-supervised or manual export
```

IMEMR may work better with simple search lines than complex Boolean strings.

## Export/import recommendation

Preferred:

```text
RIS or CSV, if available
```

Fallback:

```text
manual CSV
Zotero capture, if supported
```

## IMEMR — simple_1

```text
critical congenital heart disease pulse oximetry newborn
```

## IMEMR — simple_2

```text
congenital heart disease pulse oximetry neonate
```

## IMEMR — simple_3

```text
pulse oximetry newborn screening
```

## IMEMR — saudi_regional

```text
Saudi pulse oximetry congenital heart disease newborn
```

## IMEMR — pphn_regional

```text
pulmonary hypertension pulse oximetry newborn screening
```

---

# 9. Google Scholar

## Access mode

```text
Browser-supervised only
```

Google Scholar is supplementary only. Do not treat it as a primary reproducible database search. Do not perform aggressive scraping.

Recommended approach:

```text
screen first 100–200 results, or another prespecified number
save clearly relevant records
export citations through Zotero, Google Scholar Library, Publish or Perish, BibTeX, or RIS
document number of results reviewed
```

## Export/import recommendation

Preferred:

```text
BibTeX
RIS
```

Alternatives:

```text
CSV
manual citation entry
Zotero export
```

## Google Scholar — broad

```text
"critical congenital heart disease" "pulse oximetry" newborn screening
```

## Google Scholar — false_positive

```text
"critical congenital heart disease" "pulse oximetry" "false positive"
```

## Google Scholar — failed_screen

```text
"CCHD screening" newborn "failed screen"
```

## Google Scholar — pphn

```text
"CCHD screening" PPHN
```

## Google Scholar — pulmonary_hypertension

```text
"CCHD screening" newborn "pulmonary hypertension"
```

## Google Scholar — secondary_conditions

```text
"pulse oximetry screening" newborn "secondary conditions"
```

## Google Scholar — regional_saudi

```text
"pulse oximetry" newborn congenital heart disease Saudi Arabia
```

## Google Scholar — regional_brazil

```text
"oximetria de pulso" recém-nascido cardiopatia congênita
```

---

# 10. Crossref

## Access mode

```text
API-autonomous
```

Crossref is supplementary for metadata discovery, DOI enrichment, and missing citation details. It is not the primary biomedical search source.

## Crossref — broad_metadata

```text
critical congenital heart disease pulse oximetry newborn neonatal screening
```

## Crossref — focused_metadata

```text
critical congenital heart disease pulse oximetry false positive newborn
```

## Crossref — pphn_metadata

```text
critical congenital heart disease pulse oximetry pulmonary hypertension newborn
```

---

# 11. OpenAlex

## Access mode

```text
API-autonomous
```

OpenAlex is supplementary for metadata discovery and citation-network enrichment.

## OpenAlex — broad_metadata

```text
critical congenital heart disease pulse oximetry newborn neonatal screening
```

## OpenAlex — focused_metadata

```text
critical congenital heart disease pulse oximetry false positive failed screen newborn
```

## OpenAlex — pphn_metadata

```text
critical congenital heart disease pulse oximetry pulmonary hypertension PPHN newborn
```

---

# 12. Semantic Scholar

## Access mode

```text
API-autonomous
```

Semantic Scholar is supplementary for metadata enrichment, citation discovery, and abstract retrieval where available.

## Semantic Scholar — broad

```text
critical congenital heart disease pulse oximetry newborn neonatal screening
```

## Semantic Scholar — focused

```text
critical congenital heart disease pulse oximetry false positive failed screen newborn
```

## Semantic Scholar — pphn

```text
critical congenital heart disease pulse oximetry pulmonary hypertension PPHN newborn
```

---

# 13. Citation Chasing

Citation chasing is not a database search but a structured review task.

## Citation chasing tasks

```text
Extract reference list from all included full-text studies.
```

```text
Extract reference list from major systematic reviews and meta-analyses.
```

```text
Identify studies cited by sentinel papers on newborn pulse oximetry screening for CCHD.
```

```text
Identify newer papers citing included landmark studies, when citation tools are available.
```

## Citation chasing status options

```text
not_started
in_progress
completed
completed_with_note
no_additional_records
```

---

# 14. Recommended execution order for the agent

```text
1. PubMed primary_broad
2. PubMed failed_screen_focused
3. PubMed pphn_sensitivity
4. Europe PMC primary_broad
5. Europe PMC failed_screen_focused
6. Europe PMC pphn_sensitivity
7. Embase primary_broad
8. Embase failed_screen_focused
9. Embase pphn_sensitivity
10. Scopus or Web of Science primary_broad
11. Scopus or Web of Science failed_screen_focused
12. Scopus or Web of Science pphn_sensitivity
13. LILACS/BVS multilingual_broad
14. LILACS/BVS simple variants
15. SciELO multilingual/simple variants
16. IMEMR simple/regional variants
17. Google Scholar supplementary searches
18. Citation chasing
```

---

# 15. Required logging for every query

For each query run, the agent/app must record:

```text
source_database
access_mode
query_label
query_string
date/time
URL
filters applied
result count
records exported
records imported
export format
download path, if applicable
warnings
human intervention required, if any
```

---

# 16. Search completion rule

A source is complete only when every planned query has one of these statuses:

```text
completed
completed_with_warnings
no_results_found_with_note
skipped_with_justification
unavailable_with_note
```

A source is incomplete if any query remains:

```text
not_started
running
waiting_for_login
waiting_for_human_export
failed_unresolved
```

Deduplication must remain locked until all required sources are complete or closed with justification.
