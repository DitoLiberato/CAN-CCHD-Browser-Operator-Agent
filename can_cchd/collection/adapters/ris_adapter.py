"""RIS file adapter for manual/browser source uploads."""
import json
from typing import List
from uuid import uuid4

from can_cchd.collection.base_adapter import BaseAdapter
from can_cchd.collection.models import QuerySpec, QueryRunResult, RawRecord


def parse_ris_content(content: str) -> List[dict]:
    """Parse RIS format into list of dicts."""
    records = []
    current = {}
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("ER  -"):
            if current:
                records.append(current)
                current = {}
        elif "  - " in line:
            parts = line.split("  - ", 1)
            if len(parts) == 2:
                tag, value = parts[0].strip(), parts[1].strip()
                if tag == "AU":
                    current.setdefault("authors", []).append(value)
                elif tag in current:
                    current[tag] = f"{current[tag]}; {value}"
                else:
                    current[tag] = value
    return records


class RISAdapter(BaseAdapter):
    source_name = "Manual Upload"
    access_mode = "Browser-supervised"

    def run_query(self, query_spec: QuerySpec) -> QueryRunResult:
        return QueryRunResult(
            query_run_id=str(uuid4()),
            query_spec=query_spec,
            search_url="manual_upload",
            result_count_reported=0,
            status="manual_pending"
        )

    def harvest_records(self, query_run: QueryRunResult) -> List[RawRecord]:
        # Not used for RIS — use from_ris_content() directly
        return []

    def from_ris_content(self, content: str, query_spec: QuerySpec, source_database: str) -> dict:
        """Full pipeline from RIS text string."""
        query_run = self.run_query(query_spec)
        ris_records = parse_ris_content(content)
        raw_records = []

        for rec in ris_records:
            authors = "; ".join(rec.get("authors", [])) or rec.get("AU", "")
            year = rec.get("PY", rec.get("Y1", ""))[:4] if rec.get("PY") or rec.get("Y1") else ""
            raw = RawRecord(
                query_run_id=query_run.query_run_id,
                source_database=source_database,
                source_record_id=rec.get("AN", rec.get("ID", "")),
                source_url=rec.get("UR", rec.get("L2", "")),
                raw_title=rec.get("TI", rec.get("T1", "")),
                raw_authors=authors,
                raw_year=year,
                raw_journal=rec.get("JO", rec.get("JF", rec.get("T2", ""))),
                raw_doi=rec.get("DO", rec.get("M3", "")),
                raw_pmid=rec.get("PM", ""),
                raw_abstract=rec.get("AB", rec.get("N2", "")),
                raw_language=rec.get("LA", ""),
                raw_metadata_json=json.dumps(rec),
            )
            raw_records.append(raw)

        return self.save_all(query_run, raw_records)
