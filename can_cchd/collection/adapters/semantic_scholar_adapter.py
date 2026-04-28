"""Semantic Scholar adapter using Graph API."""
import json
import time
import urllib.parse
from typing import List
from uuid import uuid4

import requests

from can_cchd.collection.base_adapter import BaseAdapter
from can_cchd.collection.models import QuerySpec, QueryRunResult, RawRecord

SS_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
MAX_RECORDS = 500
LIMIT = 100
FIELDS = "title,authors,year,abstract,externalIds,venue,paperId,url,citationCount,publicationTypes"


class SemanticScholarAdapter(BaseAdapter):
    source_name = "Semantic Scholar"
    access_mode = "API-autonomous"

    def run_query(self, query_spec: QuerySpec) -> QueryRunResult:
        query_run_id = str(uuid4())
        search_url = f"{SS_URL}?query={urllib.parse.quote(query_spec.query_string)}&limit=1"
        try:
            r = requests.get(SS_URL, params={"query": query_spec.query_string, "limit": 1, "fields": "title"}, timeout=30)
            count = r.json().get("total", 0)
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
        offset = 0
        retries = 0

        while len(raw_records) < MAX_RECORDS:
            params = {
                "query": qs.query_string,
                "limit": LIMIT,
                "offset": offset,
                "fields": FIELDS
            }
            try:
                r = requests.get(SS_URL, params=params, timeout=30)
                if r.status_code == 429:
                    if retries >= 3:
                        break
                    time.sleep(10)
                    retries += 1
                    continue
                r.raise_for_status()
                data = r.json()
                items = data.get("data", [])
                if not items:
                    break
                for item in items:
                    raw_records.append(self._item_to_raw(item, query_run.query_run_id))
                    if len(raw_records) >= MAX_RECORDS:
                        break
                next_offset = data.get("next")
                if not next_offset:
                    break
                offset = next_offset
                retries = 0
                time.sleep(1)
            except Exception:
                break

        return raw_records

    def _item_to_raw(self, item: dict, query_run_id: str) -> RawRecord:
        title = item.get("title") or ""
        authors = [a.get("name", "") for a in item.get("authors", []) if a.get("name")]
        authors_str = ", ".join(authors)
        year = str(item.get("year") or "")
        ext = item.get("externalIds") or {}
        doi = ext.get("DOI", "") or ""
        pmid = str(ext.get("PubMed", "") or "")
        abstract = item.get("abstract", "") or ""
        venue = item.get("venue", "") or ""
        url = item.get("url", "") or ""
        pub_types = ", ".join(item.get("publicationTypes") or [])
        return RawRecord(
            query_run_id=query_run_id,
            source_database="Semantic Scholar",
            source_record_id=item.get("paperId", ""),
            source_url=url,
            raw_title=title,
            raw_authors=authors_str,
            raw_year=year,
            raw_journal=venue,
            raw_doi=doi,
            raw_pmid=pmid,
            raw_abstract=abstract,
            raw_publication_type=pub_types,
            raw_metadata_json=json.dumps({
                "paperId": item.get("paperId"),
                "citationCount": item.get("citationCount"),
            }),
        )
