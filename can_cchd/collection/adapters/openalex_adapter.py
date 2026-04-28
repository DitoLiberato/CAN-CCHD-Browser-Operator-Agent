"""OpenAlex adapter — reconstructs abstracts from inverted index."""
import json
import time
import urllib.parse
from typing import List, Optional
from uuid import uuid4

import requests

from can_cchd.collection.base_adapter import BaseAdapter
from can_cchd.collection.models import QuerySpec, QueryRunResult, RawRecord

OPENALEX_URL = "https://api.openalex.org/works"
MAX_RECORDS = 500
PER_PAGE = 100
MAILTO = "researcher@cancchd.org"


def reconstruct_abstract(inverted_index: Optional[dict]) -> str:
    """Rebuild abstract text from OpenAlex abstract_inverted_index."""
    if not inverted_index:
        return ""
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort(key=lambda x: x[0])
    return " ".join(w for _, w in word_positions)


class OpenAlexAdapter(BaseAdapter):
    source_name = "OpenAlex"
    access_mode = "API-autonomous"

    def run_query(self, query_spec: QuerySpec) -> QueryRunResult:
        query_run_id = str(uuid4())
        params = {"search": query_spec.query_string, "per-page": 1, "mailto": MAILTO}
        search_url = f"{OPENALEX_URL}?{urllib.parse.urlencode(params)}"
        try:
            r = requests.get(OPENALEX_URL, params=params, timeout=30)
            count = r.json().get("meta", {}).get("count", 0)
        except Exception:
            count = 0
        return QueryRunResult(
            query_run_id=query_run_id,
            query_spec=query_spec,
            search_url=search_url,
            result_count_reported=count,
            status="running"
        )

    def harvest_records(self, query_run: QueryRunResult) -> List[RawRecord]:
        qs = query_run.query_spec
        raw_records = []
        cursor_mark = "*"
        fetched = 0

        while fetched < MAX_RECORDS:
            params = {
                "search": qs.query_string,
                "per-page": PER_PAGE,
                "cursor": cursor_mark,
                "mailto": MAILTO,
                "select": "id,title,authorships,publication_year,doi,ids,primary_location,abstract_inverted_index,open_access,type"
            }
            try:
                r = requests.get(OPENALEX_URL, params=params, timeout=30)
                r.raise_for_status()
                data = r.json()
                results = data.get("results", [])
                if not results:
                    break
                for item in results:
                    raw_records.append(self._item_to_raw(item, query_run.query_run_id))
                    fetched += 1
                    if fetched >= MAX_RECORDS:
                        break

                next_cursor = data.get("meta", {}).get("next_cursor")
                if not next_cursor or next_cursor == cursor_mark:
                    break
                cursor_mark = next_cursor
                time.sleep(0.5)
            except Exception:
                break

        return raw_records

    def _item_to_raw(self, item: dict, query_run_id: str) -> RawRecord:
        title = item.get("title") or ""
        authors = []
        for a in item.get("authorships", []):
            name = a.get("author", {}).get("display_name", "")
            if name:
                authors.append(name)
        authors_str = ", ".join(authors)
        year = str(item.get("publication_year") or "")

        ids = item.get("ids", {})
        doi = ids.get("doi", "") or ""
        if doi.startswith("https://doi.org/"):
            doi = doi[len("https://doi.org/"):]
        pmid = ids.get("pmid", "") or ""
        if pmid.startswith("https://pubmed.ncbi.nlm.nih.gov/"):
            pmid = pmid[len("https://pubmed.ncbi.nlm.nih.gov/"):]

        abstract = reconstruct_abstract(item.get("abstract_inverted_index"))

        oa = item.get("open_access", {})
        is_oa = 1 if oa.get("is_oa") else 0
        pdf_url = oa.get("oa_url", "") or ""
        oa_status = oa.get("oa_status", "") or ""

        source = item.get("primary_location", {}) or {}
        journal = (source.get("source") or {}).get("display_name", "") or ""
        landing_url = source.get("landing_page_url", "") or ""

        return RawRecord(
            query_run_id=query_run_id,
            source_database="OpenAlex",
            source_record_id=item.get("id", ""),
            source_url=landing_url,
            raw_title=title,
            raw_authors=authors_str,
            raw_year=year,
            raw_journal=journal,
            raw_doi=doi,
            raw_pmid=pmid,
            raw_abstract=abstract,
            raw_publication_type=item.get("type", ""),
            raw_metadata_json=json.dumps({
                "openalex_id": item.get("id"), "oa_status": oa_status,
                "is_oa": is_oa, "pdf_url": pdf_url
            }),
        )

    def normalize_record(self, raw: RawRecord, raw_record_id: str):
        norm = super().normalize_record(raw, raw_record_id)
        try:
            meta = json.loads(raw.raw_metadata_json)
            norm.is_open_access = meta.get("is_oa", 0)
            norm.oa_status = meta.get("oa_status", "")
            norm.pdf_url = meta.get("pdf_url", "")
        except Exception:
            pass
        return norm
