# Case Report 01 — Phase 1 Native Backfill Plan v1.0

**Date:** 2026-09-03  
**Branch:** `case-report-01`  
**Purpose:** close the remaining Phase 1 technical reproducibility subgate without reopening scientific discovery.

## Decision

Use one **final union collection query per bibliographic source** rather than treating each calibration family as an independent PRISMA source search.

Rationale:

- the Phase 1 calibration log already documents the component search families and why each was introduced;
- repeated family-level native exports would create avoidable within-source duplication;
- a single union query per source provides one reproducible raw collection and one exact source count for PRISMA accounting;
- the union query preserves the sensitivity concepts that produced the saturation corpus: modern Morgagni terminology, historical/anatomic terminology, broad congenital diaphragmatic hernia sensitivity, and Cantrell/anterior-midline sensitivity;
- syndrome terms such as Down syndrome remain non-mandatory and are not required in the final source query.

## PubMed final native union query

```text
(
  "Tetralogy of Fallot"[Mesh]
  OR "tetralogy of Fallot"[Title/Abstract]
  OR "Fallot's tetralogy"[Title/Abstract]
)
AND
(
  Morgagni[All Fields]
  OR Larrey[All Fields]
  OR subcostosternal[All Fields]
  OR subcosto-sternal[All Fields]
  OR retrosternal[All Fields]
  OR parasternal[All Fields]
  OR "anterior diaphragmatic hernia"[All Fields]
  OR "congenital diaphragmatic hernia"[Title/Abstract]
  OR "diaphragmatic hernia"[Title/Abstract]
  OR "Pentalogy of Cantrell"[Title/Abstract]
  OR "Cantrell syndrome"[Title/Abstract]
)
```

### PubMed native capture requirements

Preserve:

- exact run date;
- exact query string;
- exact native hit count;
- PubMed query translation if available;
- complete PMID list/export;
- raw export file or machine-readable equivalent;
- checksum/hash of the preserved export when practical.

## Europe PMC final native union query

```text
(
  "tetralogy of Fallot"
  OR "Fallot's tetralogy"
)
AND
(
  Morgagni
  OR Larrey
  OR subcostosternal
  OR subcosto-sternal
  OR retrosternal
  OR parasternal
  OR "anterior diaphragmatic hernia"
  OR "congenital diaphragmatic hernia"
  OR "diaphragmatic hernia"
  OR "Pentalogy of Cantrell"
  OR "Cantrell syndrome"
)
```

Europe PMC is intentionally broader in field scope than the PubMed expression because it is used as an independent recall source and may index abstracts/full-text/metadata differently. Any extra noise is handled in Phase 2/3; it must not be removed retrospectively from the raw collection.

### Europe PMC native capture requirements

Preserve:

- exact run date;
- exact query string;
- exact native `hitCount`;
- complete result identifier list with source (`MED`, `PMC`, preprint/other source as applicable);
- PMID/PMCID/DOI where supplied;
- raw JSON/XML export or machine-readable equivalent;
- checksum/hash when practical.

## Reconciliation rules

After both native exports are available:

1. preserve each source export unchanged;
2. normalize identifiers only in a derived reconciliation table;
3. exact PMID matches are deterministic cross-source duplicates;
4. DOI/PMCID/title-based matches are reconciled without deleting provenance;
5. records absent from one source remain source-specific records, not errors;
6. compare the native union collection against the scientific saturation registry;
7. every saturation sentinel/candidate must either be recovered natively or have an explicit provenance explanation (e.g. non-PubMed conference abstract, clinical case repository, journal-only record, citation discovery);
8. native collection does not replace the supplementary/citation-discovered corpus; it anchors the formal database component.

## Gate-closing condition

Formal Gate 1 can close when:

- PubMed native count/export is preserved;
- Europe PMC native count/export is preserved;
- both are reconciled;
- sentinel coverage is audited;
- supplementary/citation-only records are appended with provenance;
- a frozen Phase 1 raw collection snapshot is written for Phase 2.

Scientific discovery remains closed at saturation throughout this backfill.
