"""Metadata completeness scoring for normalized records."""
from can_cchd.collection.models import NormalizedRecord


def calculate_completeness_score(
    record: NormalizedRecord,
    raw_metadata_available: bool | None = None,
) -> float:
    """Returns a completeness score from 0 to 100."""
    score = 0.0
    if raw_metadata_available is None:
        raw_metadata_available = bool(getattr(record, "raw_metadata_available", 0))
    if record.title and len(record.title.strip()) > 3:
        score += 20
    if record.pmid or record.doi or record.pmcid:
        score += 20
    if record.abstract and len(record.abstract.strip()) > 20:
        score += 20
    if record.year and 1900 < record.year < 2100:
        score += 10
    if record.journal:
        score += 10
    if record.authors_raw:
        score += 10
    if record.landing_page_url or record.pdf_url:
        score += 5
    if raw_metadata_available:
        score += 5
    return score


def get_readiness_class(score: float) -> str:
    if score >= 80:
        return "screening_ready"
    elif score >= 60:
        return "screening_ready_with_warning"
    elif score >= 40:
        return "enrichment_needed"
    else:
        return "collection_problem"
