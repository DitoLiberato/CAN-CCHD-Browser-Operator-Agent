# Supplementary Appendix 1. Search sources, query strategy, and AI-assisted workflow provenance

Searches and citation chasing were completed through 21 August 2026. This appendix reproduces the prespecified source-specific query set preserved in the project repository. It distinguishes public sources actually used in the review from subscription sources that were prespecified but unavailable.

## A. Sources used

Primary/public bibliographic and regional sources:
- PubMed/MEDLINE
- Europe PMC
- LILACS/BVS
- SciELO
- IMEMR / Eastern Mediterranean regional public sources

Supplementary discovery/enrichment:
- Google Scholar (supplementary only)
- backward and forward citation chasing
- Crossref, OpenAlex, and Semantic Scholar for metadata/citation-network enrichment when useful

Prespecified but unavailable/not searched:
- Embase
- Scopus or Web of Science

## B. PubMed/MEDLINE

Primary broad:

```text
("critical congenital heart disease"[Title/Abstract] OR CCHD[Title/Abstract]) AND ("pulse oximetry"[Title/Abstract] OR "oxygen saturation"[Title/Abstract]) AND (newborn[Title/Abstract] OR neonate[Title/Abstract] OR neonatal[Title/Abstract])
```

Focused failed-screen:

```text
("critical congenital heart disease"[Title/Abstract] OR CCHD[Title/Abstract]) AND ("pulse oximetry"[Title/Abstract] OR "oxygen saturation"[Title/Abstract]) AND (newborn[Title/Abstract] OR neonate[Title/Abstract] OR neonatal[Title/Abstract]) AND ("false positive"[Title/Abstract] OR "failed screen"[Title/Abstract] OR "positive screen"[Title/Abstract] OR "screen positive"[Title/Abstract] OR "abnormal screen"[Title/Abstract] OR "secondary condition"[Title/Abstract] OR hypoxemia[Title/Abstract] OR hypoxaemia[Title/Abstract] OR "pulmonary hypertension"[Title/Abstract] OR PPHN[Title/Abstract] OR sepsis[Title/Abstract] OR respiratory[Title/Abstract])
```

PPHN sensitivity:

```text
("critical congenital heart disease"[Title/Abstract] OR CCHD[Title/Abstract]) AND ("pulse oximetry"[Title/Abstract] OR "pulse oximetry screening"[Title/Abstract] OR "oxygen saturation"[Title/Abstract]) AND ("persistent pulmonary hypertension"[Title/Abstract] OR PPHN[Title/Abstract] OR "pulmonary hypertension"[Title/Abstract])
```

Broader fallback:

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal)
```

## C. Europe PMC

Primary broad:

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal)
```

Focused failed-screen:

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "oxygen saturation") AND (newborn OR neonate OR neonatal) AND ("false positive" OR "failed screen" OR "positive screen" OR "screen positive" OR "abnormal screen" OR "secondary condition" OR hypoxemia OR hypoxaemia OR "pulmonary hypertension" OR PPHN OR sepsis OR respiratory)
```

PPHN sensitivity:

```text
("critical congenital heart disease" OR CCHD) AND ("pulse oximetry" OR "pulse oximetry screening" OR "oxygen saturation") AND ("persistent pulmonary hypertension" OR PPHN OR "pulmonary hypertension")
```

## D. LILACS/BVS

Multilingual broad:

```text
("critical congenital heart disease" OR "cardiopatia congênita crítica" OR "cardiopatia congenita critica" OR "cardiopatía congénita crítica") AND ("pulse oximetry" OR "oximetria de pulso" OR "oximetría de pulso") AND (newborn OR neonate OR neonatal OR "recém-nascido" OR "recem-nascido" OR "recien nacido" OR "recién nacido")
```

Simpler variants used where the interface did not reliably accept complex Boolean syntax:

```text
"critical congenital heart disease" AND "pulse oximetry" AND newborn
"cardiopatia congênita" AND "oximetria de pulso" AND "recém-nascido"
cardiopatia congenita AND oximetria de pulso AND recem-nascido
"cardiopatía congénita" AND "oximetría de pulso" AND "recién nacido"
cardiopatia congenita AND oximetria de pulso AND recien nacido
cardiopatia AND oximetria AND neonatal
```

## E. SciELO

Multilingual broad:

```text
("critical congenital heart disease" OR "cardiopatia congênita crítica" OR "cardiopatia congenita critica" OR "cardiopatía congénita crítica") AND ("pulse oximetry" OR "oximetria de pulso" OR "oximetría de pulso") AND (newborn OR neonate OR neonatal OR "recém-nascido" OR "recem-nascido" OR "recién nacido" OR "recien nacido")
```

Simpler variants:

```text
"cardiopatia congênita" "oximetria de pulso" "recém-nascido"
cardiopatia congenita oximetria pulso neonatal
"critical congenital heart disease" "pulse oximetry" newborn
"cardiopatía congénita" "oximetría de pulso" "recién nacido"
```

## F. IMEMR / Eastern Mediterranean regional searching

```text
critical congenital heart disease pulse oximetry newborn
congenital heart disease pulse oximetry neonate
pulse oximetry newborn screening
Saudi pulse oximetry congenital heart disease newborn
pulmonary hypertension pulse oximetry newborn screening
```

The regional search was expanded country-by-country after an initial generic saturation impression was shown to be premature. Multilingual, author/title, and regional waves were reconciled before two closing waves identified no new routine potentially eligible cohorts. Public-web saturation was not treated as proof of native-platform completeness.

## G. Google Scholar - supplementary only

```text
"critical congenital heart disease" "pulse oximetry" newborn screening
"critical congenital heart disease" "pulse oximetry" "false positive"
"CCHD screening" newborn "failed screen"
"CCHD screening" PPHN
"CCHD screening" newborn "pulmonary hypertension"
"pulse oximetry screening" newborn "secondary conditions"
"pulse oximetry" newborn congenital heart disease Saudi Arabia
"oximetria de pulso" recém-nascido cardiopatia congênita
```

Google Scholar was treated as supplementary discovery rather than a primary reproducible database source.

## H. Citation chasing

Reference lists of included full-text studies and major reviews/meta-analyses were examined. Citation-network tools were used where available to identify later papers citing sentinel or included studies. All candidate reports were reconciled against the evolving report inventory before eligibility assessment.

## I. Prespecified but unavailable subscription searches

Embase and Scopus/Web of Science had source-specific query syntax defined in the protocol, but these databases were not available and were not searched. Their absence is reported as a review limitation rather than represented as completed searching.

## J. Query-level provenance fields

The workflow specification required each query run, when captured by the collection layer, to preserve the source, access mode, query label and string, date/time, URL, filters, result count, records exported/imported, export format, warnings, and human intervention. The review manuscript does not infer missing native-platform counts where the restart-era corpus did not retain an auditable value.

## K. AI-assisted workflow controls

The review was organized as a 12-stage phase-gated process (Phases 0-11). Generative AI could support mechanical, reversible, and auditable tasks but could not autonomously make final scientific decisions. AI-suggested extraction fields were segregated from verified data and were barred from analysis until human verification/correction. Final eligibility, extraction acceptance, diagnosis mapping, overlap adjudication, dataset locking, model selection, and interpretation were human-controlled.
