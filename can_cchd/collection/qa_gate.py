"""
Collection QA Gate — evaluates collection quality before allowing deduplication.

Implements blocking and warning conditions per Reform doc Section 9.
Updates collection_qa_gate table with final status.
"""
import datetime
import json
from uuid import uuid4

from can_cchd.collection.completeness import get_readiness_class


def _now():
    return datetime.datetime.now(datetime.UTC).isoformat()


def run_qa_gate(conn) -> dict:
    """
    Run all QA checks. Returns:
        {
          "status": "pass" | "warn" | "block",
          "blocking": [...],
          "warnings": [...],
          "summary": {...}
        }
    Updates collection_qa_gate table.
    """
    cursor = conn.cursor()
    blocking = []
    warnings = []

    # --- Total records ---
    cursor.execute("SELECT count(*) as c FROM normalized_records")
    total = cursor.fetchone()["c"]

    if total == 0:
        blocking.append({
            "type": "no_records",
            "message": "No normalized records found. Run at least one query first.",
            "action": "Run Phase 1 search collection."
        })
        return _finalize(conn, "block", blocking, warnings, total, 0, 0, 0, 0)

    # --- Missing title check (blocking if >10%) ---
    cursor.execute("SELECT count(*) as c FROM normalized_records WHERE title IS NULL OR title = ''")
    missing_title = cursor.fetchone()["c"]
    pct_missing_title = (missing_title / total) * 100
    if pct_missing_title > 10:
        blocking.append({
            "type": "missing_title_rate",
            "message": f"{missing_title} records ({pct_missing_title:.1f}%) are missing a title (threshold: 10%).",
            "action": "Investigate source adapters — title must be harvested for all records."
        })

    # --- Missing provenance check (blocking if >25%) ---
    cursor.execute("""
        SELECT count(*) as c FROM normalized_records
        WHERE (query_run_id IS NULL OR query_run_id = '')
    """)
    missing_prov = cursor.fetchone()["c"]
    pct_missing_prov = (missing_prov / total) * 100
    if pct_missing_prov > 25:
        blocking.append({
            "type": "missing_provenance_rate",
            "message": f"{missing_prov} records ({pct_missing_prov:.1f}%) are missing query provenance (threshold: 25%).",
            "action": "Ensure all records are linked to a query_run."
        })

    # --- Missing query_string in any query_run (blocking) ---
    cursor.execute("SELECT count(*) as c FROM query_runs WHERE query_string IS NULL OR query_string = ''")
    missing_qs = cursor.fetchone()["c"]
    if missing_qs > 0:
        blocking.append({
            "type": "query_string_missing",
            "message": f"{missing_qs} query run(s) are missing the query string.",
            "action": "Ensure query strings are persisted in query_runs."
        })

    # --- Completeness distribution ---
    cursor.execute("SELECT metadata_completeness_score FROM normalized_records")
    scores = [row["metadata_completeness_score"] or 0 for row in cursor.fetchall()]

    screening_ready = sum(1 for s in scores if s >= 80)
    screening_ready_warn = sum(1 for s in scores if 60 <= s < 80)
    enrichment_needed = sum(1 for s in scores if 40 <= s < 60)
    collection_problem = sum(1 for s in scores if s < 40)

    # --- Missing abstract (non-blocking warning) ---
    cursor.execute("""
        SELECT count(*) as c FROM normalized_records
        WHERE abstract IS NULL OR abstract = ''
    """)
    missing_abstract = cursor.fetchone()["c"]
    pct_missing_abs = (missing_abstract / total) * 100
    if pct_missing_abs > 50:
        warnings.append({
            "type": "high_missing_abstract_rate",
            "message": f"{missing_abstract} records ({pct_missing_abs:.1f}%) are missing abstracts.",
            "action": "Run enrichment queue to attempt abstract recovery."
        })

    # --- Suspicious year warnings ---
    current_year = datetime.datetime.now().year
    cursor.execute("""
        SELECT count(*) as c FROM normalized_records
        WHERE year >= ? OR year IS NULL
    """, (current_year,))
    suspicious_year_count = cursor.fetchone()["c"]
    if suspicious_year_count > 0:
        warnings.append({
            "type": "suspicious_year",
            "message": f"{suspicious_year_count} records have year={current_year} or NULL (possible default fill).",
            "action": "Run enrichment to verify years via PubMed/Crossref."
        })

    # --- Missing identifier warnings ---
    cursor.execute("""
        SELECT count(*) as c FROM normalized_records
        WHERE (pmid IS NULL OR pmid = '') AND (doi IS NULL OR doi = '') AND (pmcid IS NULL OR pmcid = '')
    """)
    missing_id = cursor.fetchone()["c"]
    if missing_id > 0:
        warnings.append({
            "type": "missing_identifier",
            "message": f"{missing_id} records have no PMID, DOI, or PMCID.",
            "action": "These records will use title/year fallback in deduplication."
        })

    status = "pass"
    if blocking:
        status = "block"
    elif warnings:
        status = "warn"

    return _finalize(conn, status, blocking, warnings, total,
                     screening_ready, screening_ready_warn, enrichment_needed, collection_problem)


def _finalize(conn, status, blocking, warnings, total,
              screening_ready, screening_ready_warn, enrichment_needed, collection_problem):
    cursor = conn.cursor()
    summary = {
        "total_records": total,
        "screening_ready": screening_ready,
        "screening_ready_with_warning": screening_ready_warn,
        "enrichment_needed": enrichment_needed,
        "collection_problem": collection_problem,
        "blocking_findings": len(blocking),
        "warning_findings": len(warnings),
    }

    cursor.execute("""
        INSERT OR REPLACE INTO collection_qa_gate (
            gate_id, status, last_run_at, total_records,
            screening_ready, screening_ready_with_warning,
            enrichment_needed, collection_problem,
            blocking_findings, warning_findings, summary_json
        ) VALUES ('main', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        status, datetime.datetime.now(datetime.UTC).isoformat(),
        total, screening_ready, screening_ready_warn,
        enrichment_needed, collection_problem,
        len(blocking), len(warnings), json.dumps(summary)
    ))
    conn.commit()

    return {
        "status": status,
        "blocking": blocking,
        "warnings": warnings,
        "summary": summary
    }


def get_gate_status(conn) -> dict:
    """Returns current gate status from DB."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM collection_qa_gate WHERE gate_id = 'main'")
    row = cursor.fetchone()
    if not row:
        return {"status": "not_run"}
    return dict(row)
