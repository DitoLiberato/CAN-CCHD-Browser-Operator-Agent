"""Abstract base adapter for all collection sources."""
import datetime
import hashlib
import json
import re
from abc import ABC, abstractmethod
from typing import List
from uuid import uuid4

from can_cchd.collection.models import (
    QuerySpec, QueryRunResult, RawRecord, NormalizedRecord, CollectionQAFinding
)


def now_iso():
    return datetime.datetime.now(datetime.UTC).isoformat()


def normalize_title(title: str) -> str:
    if not title:
        return ""
    t = title.lower()
    t = re.sub(r'[^\w\s]', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def normalize_doi(doi: str) -> str:
    if not doi:
        return ""
    doi = doi.strip()
    for prefix in ["https://doi.org/", "http://doi.org/", "doi:"]:
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix):]
    return doi.lower()


def hash_raw_record(raw: RawRecord) -> str:
    key = f"{raw.source_database}|{raw.raw_pmid}|{raw.raw_doi}|{raw.raw_title}"
    return hashlib.md5(key.encode()).hexdigest()


def determine_initial_enrichment_status(norm: NormalizedRecord, raw_metadata_available: bool) -> str:
    """Assign the first enrichment status for a normalized record."""
    if (
        norm.title
        and (norm.pmid or norm.doi or norm.pmcid)
        and norm.abstract
        and norm.year
        and norm.journal
        and norm.authors_raw
        and raw_metadata_available
    ):
        return "not_required"
    return "needs_enrichment"


class BaseAdapter(ABC):
    source_name: str
    access_mode: str

    def __init__(self, conn):
        self.conn = conn

    @abstractmethod
    def run_query(self, query_spec: QuerySpec) -> QueryRunResult:
        """Execute the search and return query run metadata."""
        ...

    @abstractmethod
    def harvest_records(self, query_run: QueryRunResult) -> List[RawRecord]:
        """Collect raw records from the source."""
        ...

    def normalize_record(self, raw: RawRecord, raw_record_id: str) -> NormalizedRecord:
        """Default normalization. Adapters can override."""
        year = None
        if raw.raw_year:
            match = re.search(r'\b(19|20)\d{2}\b', str(raw.raw_year))
            if match:
                year = int(match.group())

        authors_raw = raw.raw_authors or ""
        first_author = authors_raw.split(',')[0].split(';')[0].strip() if authors_raw else ""

        doi_norm = normalize_doi(raw.raw_doi)

        abstract_status = "available" if raw.raw_abstract else "not_collected"

        norm = NormalizedRecord(
            raw_record_id=raw_record_id,
            query_run_id=raw.query_run_id,
            source_database=raw.source_database,
            source_record_id=raw.source_record_id,
            title=raw.raw_title,
            title_normalized=normalize_title(raw.raw_title),
            authors_raw=authors_raw,
            first_author=first_author,
            year=year,
            journal=raw.raw_journal,
            doi=raw.raw_doi,
            doi_normalized=doi_norm,
            pmid=raw.raw_pmid,
            pmcid=raw.raw_pmcid,
            abstract=raw.raw_abstract,
            abstract_status=abstract_status,
            publication_type=raw.raw_publication_type,
            language=raw.raw_language,
            landing_page_url=raw.source_url,
        )
        return norm

    def validate_record(self, norm: NormalizedRecord, query_run_id: str) -> List[CollectionQAFinding]:
        findings = []
        if not norm.title:
            findings.append(CollectionQAFinding(
                query_run_id=query_run_id, severity="blocking",
                finding_type="missing_title", message="Record has no title.",
                recommended_action="Investigate source harvest."
            ))
        if not norm.pmid and not norm.doi and not norm.pmcid:
            findings.append(CollectionQAFinding(
                query_run_id=query_run_id, severity="warning",
                finding_type="missing_identifier",
                message="Record has no PMID, DOI, or PMCID.",
                recommended_action="Will require enrichment or title/year fallback for dedup."
            ))
        if not norm.abstract:
            findings.append(CollectionQAFinding(
                query_run_id=query_run_id, severity="warning",
                finding_type="missing_abstract",
                message="Abstract not collected at source.",
                recommended_action="Route to enrichment queue."
            ))
        if not norm.year:
            findings.append(CollectionQAFinding(
                query_run_id=query_run_id, severity="warning",
                finding_type="missing_year",
                message="Year could not be parsed.",
                recommended_action="Verify via enrichment."
            ))
        current_year = datetime.datetime.now().year
        if norm.year and norm.year > current_year:
            findings.append(CollectionQAFinding(
                query_run_id=query_run_id, severity="warning",
                finding_type="future_year",
                message=f"Year {norm.year} is in the future.",
                recommended_action="Verify via PubMed/Crossref enrichment."
            ))
        elif norm.year == current_year:
            findings.append(CollectionQAFinding(
                query_run_id=query_run_id, severity="info",
                finding_type="current_year",
                message=f"Year {norm.year} matches the current year.",
                recommended_action="Review only if the source shows other metadata conflicts."
            ))
        return findings

    def save_all(self, query_run: QueryRunResult, raw_records: List[RawRecord]) -> dict:
        """
        Persist query_run, raw_records, normalized_records, and QA findings.
        Returns summary dict.
        """
        cursor = self.conn.cursor()
        ts = now_iso()
        qs = query_run.query_spec

        # 1. Upsert query_run
        cursor.execute("""
            INSERT OR REPLACE INTO query_runs (
                query_run_id, source_id, source_database, query_label, query_role,
                query_string, access_mode, execution_mode, run_started_at,
                search_url, result_count_reported, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            query_run.query_run_id, qs.source_id, qs.source_database,
            qs.query_label, qs.query_role, qs.query_string, qs.access_mode,
            "api_automated", ts, query_run.search_url,
            query_run.result_count_reported, "running"
        ))

        imported = 0
        failed = 0
        all_findings = []

        for raw in raw_records:
            try:
                raw_record_id = str(uuid4())
                raw_hash = hash_raw_record(raw)

                # 2. Insert raw_record (immutable)
                cursor.execute("""
                    INSERT OR IGNORE INTO raw_records (
                        raw_record_id, query_run_id, source_database, source_record_id,
                        source_url, raw_title, raw_authors, raw_year, raw_journal,
                        raw_doi, raw_pmid, raw_pmcid, raw_abstract, raw_publication_type,
                        raw_language, raw_metadata_json, harvested_at, raw_hash
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    raw_record_id, raw.query_run_id, raw.source_database,
                    raw.source_record_id, raw.source_url, raw.raw_title,
                    raw.raw_authors, raw.raw_year, raw.raw_journal,
                    raw.raw_doi, raw.raw_pmid, raw.raw_pmcid, raw.raw_abstract,
                    raw.raw_publication_type, raw.raw_language,
                    raw.raw_metadata_json, ts, raw_hash
                ))

                # 3. Normalize
                norm = self.normalize_record(raw, raw_record_id)
                raw_metadata_available = bool(raw.raw_metadata_json)
                norm.raw_metadata_available = int(raw_metadata_available)

                # 4. Calculate completeness score
                from can_cchd.collection.completeness import calculate_completeness_score
                norm.metadata_completeness_score = calculate_completeness_score(
                    norm,
                    raw_metadata_available=raw_metadata_available,
                )
                norm.enrichment_status = determine_initial_enrichment_status(
                    norm,
                    raw_metadata_available=raw_metadata_available,
                )

                record_id = str(uuid4())

                # 5. Insert normalized_record
                cursor.execute("""
                    INSERT OR IGNORE INTO normalized_records (
                        record_id, raw_record_id, query_run_id, source_database,
                        source_record_id, title, title_normalized, authors_raw,
                        first_author, year, journal, doi, doi_normalized, pmid, pmcid,
                        abstract, abstract_status, publication_type, language, country,
                        keywords_json, mesh_terms_json, landing_page_url, pdf_url,
                        is_open_access, oa_status, metadata_completeness_score,
                        metadata_warnings_json, normalization_status, enrichment_status,
                        is_supplementary_source, created_at, updated_at
                    ) VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )
                """, (
                    record_id, raw_record_id, raw.query_run_id, raw.source_database,
                    norm.source_record_id, norm.title, norm.title_normalized,
                    norm.authors_raw, norm.first_author, norm.year, norm.journal,
                    norm.doi, norm.doi_normalized, norm.pmid, norm.pmcid,
                    norm.abstract, norm.abstract_status, norm.publication_type,
                    norm.language, norm.country, norm.keywords_json, norm.mesh_terms_json,
                    norm.landing_page_url, norm.pdf_url, norm.is_open_access,
                    norm.oa_status, norm.metadata_completeness_score,
                    norm.metadata_warnings_json, norm.normalization_status,
                    norm.enrichment_status, norm.is_supplementary_source, ts, ts
                ))

                # 6. QA Findings
                findings = self.validate_record(norm, raw.query_run_id)
                for f in findings:
                    f.record_id = record_id
                    cursor.execute("""
                        INSERT INTO collection_qa_findings (
                            collection_qa_id, record_id, query_run_id, severity,
                            finding_type, message, recommended_action, status, created_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, 'open', ?)
                    """, (
                        str(uuid4()), record_id, raw.query_run_id, f.severity,
                        f.finding_type, f.message, f.recommended_action, ts
                    ))
                all_findings.extend(findings)
                imported += 1

            except Exception as e:
                failed += 1
                print(f"[BaseAdapter] Error saving record: {e}")

        # 7. Update query_run stats
        cursor.execute("""
            UPDATE query_runs SET
                records_harvested = ?,
                records_imported_raw = ?,
                records_failed = ?,
                run_completed_at = ?,
                status = 'completed'
            WHERE query_run_id = ?
        """, (len(raw_records), imported, failed, now_iso(), query_run.query_run_id))

        self.conn.commit()

        return {
            "query_run_id": query_run.query_run_id,
            "harvested": len(raw_records),
            "imported": imported,
            "failed": failed,
            "findings": len(all_findings),
        }

    def run(self, query_spec: QuerySpec) -> dict:
        """Full pipeline: run_query → harvest_records → save_all."""
        query_run = self.run_query(query_spec)
        raw_records = self.harvest_records(query_run)
        return self.save_all(query_run, raw_records)
