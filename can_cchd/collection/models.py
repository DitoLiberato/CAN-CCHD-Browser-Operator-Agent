"""Data models for the collection pipeline."""
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class QuerySpec:
    query_id: str
    source_id: str
    source_database: str
    query_label: str
    query_role: str
    query_string: str
    access_mode: str


@dataclass
class QueryRunResult:
    query_run_id: str
    query_spec: QuerySpec
    search_url: str = ""
    result_count_reported: int = 0
    status: str = "not_started"
    warnings: List[str] = field(default_factory=list)


@dataclass
class RawRecord:
    query_run_id: str
    source_database: str
    source_record_id: str = ""
    source_url: str = ""
    raw_title: str = ""
    raw_authors: str = ""
    raw_year: str = ""
    raw_journal: str = ""
    raw_doi: str = ""
    raw_pmid: str = ""
    raw_pmcid: str = ""
    raw_abstract: str = ""
    raw_publication_type: str = ""
    raw_language: str = ""
    raw_metadata_json: str = ""


@dataclass
class NormalizedRecord:
    raw_record_id: str
    query_run_id: str
    source_database: str
    source_record_id: str = ""
    title: str = ""
    title_normalized: str = ""
    authors_raw: str = ""
    first_author: str = ""
    year: Optional[int] = None
    journal: str = ""
    doi: str = ""
    doi_normalized: str = ""
    pmid: str = ""
    pmcid: str = ""
    abstract: str = ""
    abstract_status: str = "unknown"
    publication_type: str = ""
    language: str = ""
    country: str = ""
    keywords_json: str = ""
    mesh_terms_json: str = ""
    landing_page_url: str = ""
    pdf_url: str = ""
    is_open_access: int = 0
    oa_status: str = ""
    metadata_completeness_score: float = 0.0
    metadata_warnings_json: str = ""
    normalization_status: str = "complete"
    enrichment_status: str = "pending"
    is_supplementary_source: int = 0
    raw_metadata_available: int = 0


@dataclass
class CollectionQAFinding:
    query_run_id: str
    severity: str          # "blocking" | "warning" | "info"
    finding_type: str
    message: str
    recommended_action: str = ""
    record_id: Optional[str] = None
