"""Collection export helpers for the Phase 1 UI and tests."""
from __future__ import annotations

import json
from collections import Counter

import pandas as pd


NORMALIZED_RECORD_EXPORT_COLUMNS = [
    "record_id",
    "raw_record_id",
    "query_run_id",
    "source_database",
    "source_record_id",
    "title",
    "title_normalized",
    "authors_raw",
    "first_author",
    "year",
    "journal",
    "doi",
    "doi_normalized",
    "pmid",
    "pmcid",
    "abstract",
    "abstract_status",
    "publication_type",
    "language",
    "country",
    "keywords_json",
    "mesh_terms_json",
    "landing_page_url",
    "pdf_url",
    "is_open_access",
    "oa_status",
    "metadata_completeness_score",
    "metadata_warnings_json",
    "normalization_status",
    "enrichment_status",
    "is_supplementary_source",
    "created_at",
    "updated_at",
]

QUERY_RUN_EXPORT_COLUMNS = [
    "query_run_id",
    "protocol_version_id",
    "source_id",
    "source_database",
    "query_label",
    "query_role",
    "query_string",
    "access_mode",
    "execution_mode",
    "run_started_at",
    "run_completed_at",
    "search_url",
    "filters_applied_json",
    "result_count_reported",
    "records_harvested",
    "records_imported_raw",
    "records_enriched",
    "records_failed",
    "warnings_json",
    "human_intervention_required",
    "status",
]

RAW_RECORD_EXPORT_COLUMNS = [
    "raw_record_id",
    "query_run_id",
    "source_database",
    "source_record_id",
    "source_url",
    "raw_title",
    "raw_authors",
    "raw_year",
    "raw_journal",
    "raw_doi",
    "raw_pmid",
    "raw_pmcid",
    "raw_abstract",
    "raw_publication_type",
    "raw_language",
    "raw_metadata_json",
    "harvested_at",
    "raw_hash",
]

ENRICHMENT_LOG_EXPORT_COLUMNS = [
    "enrichment_id",
    "record_id",
    "enrichment_source",
    "identifier_used",
    "identifier_value",
    "fields_updated_json",
    "warnings_json",
    "status",
    "started_at",
    "completed_at",
]

QA_FINDINGS_EXPORT_COLUMNS = [
    "collection_qa_id",
    "record_id",
    "query_run_id",
    "severity",
    "finding_type",
    "message",
    "recommended_action",
    "status",
    "created_at",
    "resolved_at",
    "resolution_note",
]


def _to_dataframe(rows) -> pd.DataFrame:
    return pd.DataFrame([dict(row) for row in rows])


def _select_dataframe(conn, table: str, columns: list[str], *, order_by: str | None = None, limit: int | None = None) -> pd.DataFrame:
    query = f"SELECT {', '.join(columns)} FROM {table}"
    if order_by:
        query += f" ORDER BY {order_by}"
    if limit is not None:
        query += f" LIMIT {int(limit)}"
    cursor = conn.cursor()
    cursor.execute(query)
    return _to_dataframe(cursor.fetchall())


def get_normalized_records_preview_df(conn, limit: int = 500) -> pd.DataFrame:
    return _select_dataframe(
        conn,
        "normalized_records",
        NORMALIZED_RECORD_EXPORT_COLUMNS,
        order_by="metadata_completeness_score DESC, created_at DESC",
        limit=limit,
    )


def get_full_normalized_records_export_df(conn) -> pd.DataFrame:
    return _select_dataframe(
        conn,
        "normalized_records",
        NORMALIZED_RECORD_EXPORT_COLUMNS,
        order_by="metadata_completeness_score DESC, created_at DESC",
    )


def get_query_runs_export_df(conn) -> pd.DataFrame:
    return _select_dataframe(conn, "query_runs", QUERY_RUN_EXPORT_COLUMNS, order_by="run_started_at DESC")


def get_raw_records_export_df(conn) -> pd.DataFrame:
    return _select_dataframe(conn, "raw_records", RAW_RECORD_EXPORT_COLUMNS, order_by="harvested_at DESC")


def get_enrichment_log_export_df(conn) -> pd.DataFrame:
    return _select_dataframe(conn, "record_enrichment_log", ENRICHMENT_LOG_EXPORT_COLUMNS, order_by="completed_at DESC")


def get_collection_qa_findings_export_df(conn) -> pd.DataFrame:
    return _select_dataframe(conn, "collection_qa_findings", QA_FINDINGS_EXPORT_COLUMNS, order_by="created_at DESC")


def get_collection_qa_gate_payload(conn) -> dict:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM collection_qa_gate WHERE gate_id = 'main'")
    row = cursor.fetchone()
    return dict(row) if row else {"status": "not_run"}


def build_collection_readiness_report(conn) -> str:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS c FROM raw_records")
    raw_total = cursor.fetchone()["c"]
    cursor.execute("SELECT COUNT(*) AS c FROM normalized_records")
    normalized_total = cursor.fetchone()["c"]

    cursor.execute("""
        SELECT source_database, COUNT(*) AS c
        FROM normalized_records
        GROUP BY source_database
        ORDER BY c DESC, source_database ASC
    """)
    by_source = cursor.fetchall()

    cursor.execute("""
        SELECT qr.query_label, COUNT(*) AS c
        FROM normalized_records nr
        LEFT JOIN query_runs qr ON qr.query_run_id = nr.query_run_id
        GROUP BY qr.query_label
        ORDER BY c DESC, qr.query_label ASC
    """)
    by_query = cursor.fetchall()

    cursor.execute("""
        SELECT
            SUM(CASE WHEN abstract IS NOT NULL AND abstract != '' THEN 1 ELSE 0 END) AS with_abstract,
            SUM(CASE WHEN pmid IS NOT NULL AND pmid != '' THEN 1 ELSE 0 END) AS with_pmid,
            SUM(CASE WHEN doi IS NOT NULL AND doi != '' THEN 1 ELSE 0 END) AS with_doi,
            SUM(CASE WHEN pmcid IS NOT NULL AND pmcid != '' THEN 1 ELSE 0 END) AS with_pmcid,
            SUM(CASE WHEN journal IS NOT NULL AND journal != '' THEN 1 ELSE 0 END) AS with_journal,
            SUM(CASE WHEN year IS NOT NULL THEN 1 ELSE 0 END) AS with_year
        FROM normalized_records
    """)
    availability = dict(cursor.fetchone() or {})

    cursor.execute("SELECT metadata_completeness_score FROM normalized_records")
    scores = [row["metadata_completeness_score"] or 0 for row in cursor.fetchall()]
    completeness = Counter(
        "80-100" if score >= 80 else "60-79" if score >= 60 else "40-59" if score >= 40 else "0-39"
        for score in scores
    )

    cursor.execute("""
        SELECT enrichment_status, COUNT(*) AS c
        FROM normalized_records
        GROUP BY enrichment_status
        ORDER BY c DESC, enrichment_status ASC
    """)
    enrichment = cursor.fetchall()

    gate = get_collection_qa_gate_payload(conn)
    summary = json.loads(gate.get("summary_json") or "{}") if gate.get("summary_json") else {}

    recommended_next_step = (
        "Proceed to Phase 2 deduplication."
        if gate.get("status") in {"pass", "warn"}
        else "Resolve blocking QA findings before deduplication."
    )

    return "\n".join(
        [
            "# Collection Readiness Report",
            "",
            f"- total raw records: {raw_total}",
            f"- total normalized records: {normalized_total}",
            "",
            "## records by source",
            *[f"- {row['source_database']}: {row['c']}" for row in by_source],
            "",
            "## records by query",
            *[f"- {row['query_label'] or 'unassigned'}: {row['c']}" for row in by_query],
            "",
            "## availability",
            f"- abstract availability: {availability.get('with_abstract', 0)}",
            f"- PMID availability: {availability.get('with_pmid', 0)}",
            f"- DOI availability: {availability.get('with_doi', 0)}",
            f"- PMCID availability: {availability.get('with_pmcid', 0)}",
            f"- journal availability: {availability.get('with_journal', 0)}",
            f"- year availability: {availability.get('with_year', 0)}",
            "",
            "## metadata completeness distribution",
            *[f"- {bucket}: {count}" for bucket, count in sorted(completeness.items())],
            "",
            "## enrichment status distribution",
            *[f"- {row['enrichment_status'] or 'unknown'}: {row['c']}" for row in enrichment],
            "",
            "## collection QA",
            f"- status: {gate.get('status', 'not_run')}",
            f"- warnings: {summary.get('warning_findings', 0)}",
            f"- blocking issues: {summary.get('blocking_findings', 0)}",
            "",
            f"recommended next step: {recommended_next_step}",
        ]
    ).strip() + "\n"
