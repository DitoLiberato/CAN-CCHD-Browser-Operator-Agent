"""Crossref adapter using REST API with cursor pagination."""
import json
import time
import urllib.parse
from typing import List
from uuid import uuid4

import requests

from can_cchd.collection.base_adapter import BaseAdapter
from can_cchd.collection.models import QuerySpec, QueryRunResult, RawRecord

CROSSREF_URL = "https://api.crossref.org/works"
MAX_RECORDS = 500
ROWS = 100
MAILTO = "researcher@cancchd.org"


class CrossrefAdapter(BaseAdapter):
    source_name = "Crossref"
    access_mode = "API-autonomous"

    def run_query(self, query_spec: QuerySpec) -> QueryRunResult:
        query_run_id = str(uuid4())
        search_url = f"{CROSSREF_URL}?query={urllib.parse.quote(query_spec.query_string)}&rows=1"
        try:
            r = requests.get(
                CROSSREF_URL,
                params={"query": query_spec.query_string, "rows": 1, "mailto": MAILTO},
                headers={"User-Agent": f"CAN-CCHD-Agent/2.0 (mailto:{MAILTO})"},
                timeout=30
            )
            count = r.json().get("message", {}).get("total-results", 0)
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
        headers = {"User-Agent": f"CAN-CCHD-Agent/2.0 (mailto:{MAILTO})"}
        retries = 0

        while fetched < MAX_RECORDS:
            params = {
                "query": qs.query_string,
                "select": "title,author,published,DOI,abstract,container-title,type,URL",
                "rows": ROWS,
                "cursor": cursor_mark,
                "mailto": MAILTO
            }
            try:
                r = requests.get(CROSSREF_URL, params=params, headers=headers, timeout=30)
                if r.status_code == 429:
                    if retries >= 3:
                        break
                    time.sleep(5)
                    retries += 1
                    continue
                r.raise_for_status()
                data = r.json()
                items = data.get("message", {}).get("items", [])
                if not items:
                    break
                for item in items:
                    raw_records.append(self._item_to_raw(item, query_run.query_run_id))
                    fetched += 1
                    if fetched >= MAX_RECORDS:
                        break

                next_cursor = data.get("message", {}).get("next-cursor")
                if not next_cursor or next_cursor == cursor_mark:
                    break
                cursor_mark = next_cursor
                retries = 0
                time.sleep(1)
            except Exception:
                break

        return raw_records

    def _item_to_raw(self, item: dict, query_run_id: str) -> RawRecord:
        title = (item.get("title") or [""])[0]
        authors = []
        for a in item.get("author", []):
            family = a.get("family", "")
            given = a.get("given", "")
            authors.append(f"{family} {given}".strip())
        authors_str = ", ".join(authors)
        year = ""
        dp = item.get("published", {}).get("date-parts", [[]])
        if dp and dp[0]:
            year = str(dp[0][0])
        doi = item.get("DOI", "") or ""
        journal = (item.get("container-title") or [""])[0]
        abstract = item.get("abstract", "") or ""
        url = item.get("URL", "") or ""
        return RawRecord(
            query_run_id=query_run_id,
            source_database="Crossref",
            source_record_id=doi,
            source_url=url,
            raw_title=title,
            raw_authors=authors_str,
            raw_year=year,
            raw_journal=journal,
            raw_doi=doi,
            raw_abstract=abstract,
            raw_metadata_json=json.dumps(item),
        )
