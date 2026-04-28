"""Europe PMC adapter using their REST API."""
import json
import time
import urllib.parse
from typing import List
from uuid import uuid4

import requests

from can_cchd.collection.base_adapter import BaseAdapter
from can_cchd.collection.models import (
    QuerySpec, QueryRunResult, RawRecord, NormalizedRecord, CollectionQAFinding
)

SEARCH_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
MAX_RECORDS = 1000
PAGE_SIZE = 100


class EuropePMCAdapter(BaseAdapter):
    source_name = "Europe PMC"
    access_mode = "API-autonomous"

    def run_query(self, query_spec: QuerySpec) -> QueryRunResult:
        query_run_id = str(uuid4())
        params = {
            "query": query_spec.query_string,
            "resultType": "lite", "format": "json",
            "pageSize": 1, "cursorMark": "*"
        }
        search_url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
        try:
            r = requests.get(SEARCH_URL, params=params, timeout=30)
            r.raise_for_status()
            data = r.json()
            count = data.get("hitCount", 0)
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
                "query": qs.query_string,
                "resultType": "core",
                "format": "json",
                "pageSize": PAGE_SIZE,
                "cursorMark": cursor_mark
            }
            try:
                r = requests.get(SEARCH_URL, params=params, timeout=30)
                r.raise_for_status()
                data = r.json()
            except Exception:
                break

            items = data.get("resultList", {}).get("result", [])
            if not items:
                break

            for item in items:
                raw = self._item_to_raw(item, query_run.query_run_id)
                raw_records.append(raw)
                fetched += 1
                if fetched >= MAX_RECORDS:
                    break

            next_cursor = data.get("nextCursorMark")
            if not next_cursor or next_cursor == cursor_mark:
                break
            cursor_mark = next_cursor
            time.sleep(0.5)

        return raw_records

    def _item_to_raw(self, item: dict, query_run_id: str) -> RawRecord:
        pmid = str(item.get("pmid", "") or "")
        pmcid = item.get("pmcid", "") or ""
        doi = item.get("doi", "") or ""
        title = item.get("title", "") or ""
        journal = item.get("journalTitle", "") or ""
        year = str(item.get("pubYear", "") or "")
        authors = item.get("authorString", "") or ""
        abstract = item.get("abstractText", "") or ""
        is_oa = 1 if item.get("isOpenAccess") == "Y" else 0
        source_url = f"https://europepmc.org/article/MED/{pmid}" if pmid else ""

        # OA URLs
        pdf_url = ""
        full_text_urls = item.get("fullTextUrlList", {}).get("fullTextUrl", [])
        for u in full_text_urls:
            if u.get("documentStyle") == "pdf":
                pdf_url = u.get("url", "")
                break

        raw_meta = json.dumps(item)

        return RawRecord(
            query_run_id=query_run_id,
            source_database="Europe PMC",
            source_record_id=pmid or pmcid,
            source_url=source_url,
            raw_title=title,
            raw_authors=authors,
            raw_year=year,
            raw_journal=journal,
            raw_doi=doi,
            raw_pmid=pmid,
            raw_pmcid=pmcid,
            raw_abstract=abstract,
            raw_language=item.get("language", ""),
            raw_metadata_json=raw_meta,
        )

    def validate_record(self, norm: NormalizedRecord, query_run_id: str) -> List[CollectionQAFinding]:
        findings = super().validate_record(norm, query_run_id)
        import datetime
        current_year = datetime.datetime.now().year
        # Europe PMC specific: flag year == current_year more aggressively
        if norm.year and norm.year >= current_year and norm.pmid:
            findings.append(CollectionQAFinding(
                query_run_id=query_run_id,
                severity="warning",
                finding_type="suspicious_year",
                message=f"Europe PMC year={norm.year} with PMID present — likely default fill. Verify via PubMed.",
                recommended_action="Enrich via PubMed to get correct year.",
                record_id=None
            ))
        return findings
