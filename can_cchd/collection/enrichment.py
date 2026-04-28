"""
Enrichment engine — fills missing metadata in normalized_records.

Priority order per Reform doc Section 10:
  1. PMID → PubMed E-utilities (abstract, journal, year, DOI, PMCID, MeSH)
  2. DOI → Crossref (abstract, journal, year)
  3. DOI → OpenAlex (abstract from inverted index, OA status, pdf_url)
  4. DOI → Unpaywall (OA status, pdf_url)
"""
import datetime
import json
import time
import xml.etree.ElementTree as ET
from typing import Optional
from uuid import uuid4

import requests

EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
CROSSREF_URL = "https://api.crossref.org/works"
OPENALEX_URL = "https://api.openalex.org/works"
UNPAYWALL_URL = "https://api.unpaywall.org/v2"
MAILTO = "researcher@cancchd.org"


def _now():
    return datetime.datetime.now(datetime.UTC).isoformat()


def _log_enrichment(conn, record_id, source, identifier_type, identifier_value, fields_updated, status, warnings=None):
    conn.cursor().execute("""
        INSERT INTO record_enrichment_log (
            enrichment_id, record_id, enrichment_source, identifier_used,
            identifier_value, fields_updated_json, warnings_json, status,
            started_at, completed_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        str(uuid4()), record_id, source, identifier_type, identifier_value,
        json.dumps(fields_updated), json.dumps(warnings or []), status, _now(), _now()
    ))
    conn.commit()


def enrich_by_pmid(conn, record_id: str, pmid: str) -> dict:
    """Fetch full metadata from PubMed using PMID."""
    try:
        params = {"db": "pubmed", "id": pmid, "retmode": "xml", "rettype": "abstract"}
        r = requests.get(EFETCH_URL, params=params, timeout=30)
        r.raise_for_status()
        root = ET.fromstring(r.text)
        article = root.find(".//PubmedArticle")
        if not article:
            _log_enrichment(conn, record_id, "PubMed", "pmid", pmid, {}, "not_found")
            return {}

        medline = article.find("MedlineCitation")
        art = medline.find("Article") if medline else None
        updates = {}

        # Abstract
        abstract_parts = []
        if art:
            for at in art.findall(".//AbstractText"):
                label = at.get("Label", "")
                text = "".join(at.itertext()).strip()
                abstract_parts.append(f"{label}: {text}" if label else text)
        if abstract_parts:
            updates["abstract"] = " ".join(abstract_parts)
            updates["abstract_status"] = "available"

        # Year
        journal_el = art.find("Journal") if art else None
        if journal_el:
            ji = journal_el.find("JournalIssue")
            if ji:
                pd = ji.find("PubDate")
                if pd:
                    y = pd.findtext("Year", "")
                    if y:
                        updates["year"] = int(y)
            updates["journal"] = journal_el.findtext("Title", "") or journal_el.findtext("ISOAbbreviation", "")

        # DOI
        if art:
            for eid in art.findall(".//ELocationID"):
                if eid.get("EIdType") == "doi":
                    updates["doi"] = eid.text or ""
                    updates["doi_normalized"] = (eid.text or "").lower()

        # PMCID
        for aid in article.findall(".//ArticleId"):
            if aid.get("IdType") == "pmc":
                updates["pmcid"] = aid.text or ""

        # MeSH
        mesh = []
        if medline:
            for mh in medline.findall(".//MeshHeading"):
                dn = mh.findtext("DescriptorName", "")
                if dn:
                    mesh.append(dn)
        if mesh:
            updates["mesh_terms_json"] = json.dumps(mesh)

        if updates:
            set_clause = ", ".join(f"{k} = ?" for k in updates)
            values = list(updates.values()) + [_now(), record_id]
            conn.cursor().execute(
                f"UPDATE normalized_records SET {set_clause}, updated_at = ?, enrichment_status = 'enriched' WHERE record_id = ?",
                values
            )
            conn.commit()
            _log_enrichment(conn, record_id, "PubMed", "pmid", pmid, list(updates.keys()), "success")
        else:
            _log_enrichment(conn, record_id, "PubMed", "pmid", pmid, {}, "not_found")

        return updates

    except Exception as e:
        _log_enrichment(conn, record_id, "PubMed", "pmid", pmid, {}, "failed", [str(e)])
        return {}


def enrich_by_doi_crossref(conn, record_id: str, doi: str) -> dict:
    """Enrich from Crossref using DOI."""
    try:
        doi_enc = requests.utils.quote(doi, safe="")
        r = requests.get(f"{CROSSREF_URL}/{doi_enc}", timeout=30,
                         headers={"User-Agent": f"CAN-CCHD-Agent/2.0 (mailto:{MAILTO})"})
        if r.status_code == 404:
            _log_enrichment(conn, record_id, "Crossref", "doi", doi, {}, "not_found")
            return {}
        r.raise_for_status()
        item = r.json().get("message", {})
        updates = {}
        if item.get("abstract"):
            updates["abstract"] = item["abstract"]
            updates["abstract_status"] = "available"
        title_list = item.get("title", [])
        if title_list and not updates.get("title"):
            updates["title"] = title_list[0]
        container = item.get("container-title", [])
        if container:
            updates["journal"] = container[0]
        dp = item.get("published", {}).get("date-parts", [[]])
        if dp and dp[0]:
            updates["year"] = dp[0][0]

        if updates:
            set_clause = ", ".join(f"{k} = ?" for k in updates)
            values = list(updates.values()) + [_now(), record_id]
            conn.cursor().execute(
                f"UPDATE normalized_records SET {set_clause}, updated_at = ? WHERE record_id = ?",
                values
            )
            conn.commit()
            _log_enrichment(conn, record_id, "Crossref", "doi", doi, list(updates.keys()), "success")
        else:
            _log_enrichment(conn, record_id, "Crossref", "doi", doi, {}, "partial_success")
        return updates
    except Exception as e:
        _log_enrichment(conn, record_id, "Crossref", "doi", doi, {}, "failed", [str(e)])
        return {}


def enrich_by_doi_openalex(conn, record_id: str, doi: str) -> dict:
    """Enrich from OpenAlex (abstract + OA status)."""
    try:
        doi_enc = requests.utils.quote(f"https://doi.org/{doi}", safe="")
        r = requests.get(f"{OPENALEX_URL}/{doi_enc}", timeout=30,
                         params={"mailto": MAILTO, "select": "abstract_inverted_index,open_access,primary_location"})
        if r.status_code == 404:
            _log_enrichment(conn, record_id, "OpenAlex", "doi", doi, {}, "not_found")
            return {}
        r.raise_for_status()
        item = r.json()
        updates = {}

        inv_idx = item.get("abstract_inverted_index")
        if inv_idx:
            from can_cchd.collection.adapters.openalex_adapter import reconstruct_abstract
            abstract = reconstruct_abstract(inv_idx)
            if abstract:
                updates["abstract"] = abstract
                updates["abstract_status"] = "available"

        oa = item.get("open_access", {})
        if oa:
            updates["is_open_access"] = 1 if oa.get("is_oa") else 0
            updates["oa_status"] = oa.get("oa_status", "")
            updates["pdf_url"] = oa.get("oa_url", "")

        if updates:
            set_clause = ", ".join(f"{k} = ?" for k in updates)
            values = list(updates.values()) + [_now(), record_id]
            conn.cursor().execute(
                f"UPDATE normalized_records SET {set_clause}, updated_at = ? WHERE record_id = ?",
                values
            )
            conn.commit()
            _log_enrichment(conn, record_id, "OpenAlex", "doi", doi, list(updates.keys()), "success")
        else:
            _log_enrichment(conn, record_id, "OpenAlex", "doi", doi, {}, "partial_success")
        return updates
    except Exception as e:
        _log_enrichment(conn, record_id, "OpenAlex", "doi", doi, {}, "failed", [str(e)])
        return {}


def enrich_by_doi_unpaywall(conn, record_id: str, doi: str) -> dict:
    """Enrich OA status from Unpaywall."""
    try:
        r = requests.get(f"{UNPAYWALL_URL}/{doi}", params={"email": MAILTO}, timeout=30)
        if r.status_code == 404:
            _log_enrichment(conn, record_id, "Unpaywall", "doi", doi, {}, "not_found")
            return {}
        r.raise_for_status()
        data = r.json()
        updates = {
            "is_open_access": 1 if data.get("is_oa") else 0,
            "oa_status": data.get("oa_status", ""),
        }
        best_loc = data.get("best_oa_location") or {}
        if best_loc.get("url_for_pdf"):
            updates["pdf_url"] = best_loc["url_for_pdf"]
        if best_loc.get("url_for_landing_page"):
            updates["landing_page_url"] = best_loc["url_for_landing_page"]

        set_clause = ", ".join(f"{k} = ?" for k in updates)
        values = list(updates.values()) + [_now(), record_id]
        conn.cursor().execute(
            f"UPDATE normalized_records SET {set_clause}, updated_at = ? WHERE record_id = ?",
            values
        )
        conn.commit()
        _log_enrichment(conn, record_id, "Unpaywall", "doi", doi, list(updates.keys()), "success")
        return updates
    except Exception as e:
        _log_enrichment(conn, record_id, "Unpaywall", "doi", doi, {}, "failed", [str(e)])
        return {}


def run_enrichment_queue(conn, limit: int = 50) -> dict:
    """
    Process records needing enrichment following the priority order.
    Returns stats dict.
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT record_id, pmid, doi, abstract, enrichment_status
        FROM normalized_records
        WHERE enrichment_status IN ('pending', 'needs_enrichment')
          AND (abstract IS NULL OR abstract = '' OR abstract_status = 'not_collected')
        LIMIT ?
    """, (limit,))
    records = cursor.fetchall()

    stats = {"processed": 0, "enriched": 0, "failed": 0}

    for rec in records:
        record_id = rec["record_id"]
        pmid = rec["pmid"]
        doi = rec["doi"]
        enriched = False

        if pmid:
            result = enrich_by_pmid(conn, record_id, pmid)
            if result.get("abstract"):
                enriched = True

        if not enriched and doi:
            result = enrich_by_doi_crossref(conn, record_id, doi)
            if result.get("abstract"):
                enriched = True

        if not enriched and doi:
            result = enrich_by_doi_openalex(conn, record_id, doi)
            if result.get("abstract"):
                enriched = True

        if doi and not rec["abstract"]:
            enrich_by_doi_unpaywall(conn, record_id, doi)

        # Recalculate completeness score
        cursor.execute("SELECT * FROM normalized_records WHERE record_id = ?", (record_id,))
        row = cursor.fetchone()
        if row:
            from can_cchd.collection.models import NormalizedRecord
            from can_cchd.collection.completeness import calculate_completeness_score
            norm = NormalizedRecord(
                raw_record_id=row["raw_record_id"],
                query_run_id=row["query_run_id"],
                source_database=row["source_database"],
                title=row["title"] or "",
                pmid=row["pmid"] or "",
                doi=row["doi"] or "",
                pmcid=row["pmcid"] or "",
                abstract=row["abstract"] or "",
                year=row["year"],
                journal=row["journal"] or "",
                authors_raw=row["authors_raw"] or "",
                landing_page_url=row["landing_page_url"] or "",
            )
            score = calculate_completeness_score(norm)
            enrichment_status = "enriched" if enriched else "enrichment_attempted"
            cursor.execute(
                "UPDATE normalized_records SET metadata_completeness_score = ?, enrichment_status = ? WHERE record_id = ?",
                (score, enrichment_status, record_id)
            )
            conn.commit()

        stats["processed"] += 1
        if enriched:
            stats["enriched"] += 1
        else:
            stats["failed"] += 1

        time.sleep(0.3)

    return stats
