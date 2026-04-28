"""PubMed adapter using NCBI E-utilities (esearch + efetch XML)."""
import json
import time
import urllib.parse
import xml.etree.ElementTree as ET
from typing import List
from uuid import uuid4

import requests

from can_cchd.collection.base_adapter import BaseAdapter, now_iso
from can_cchd.collection.models import QuerySpec, QueryRunResult, RawRecord

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
BATCH_SIZE  = 100
MAX_RECORDS = 1000


class PubMedAdapter(BaseAdapter):
    source_name = "PubMed / MEDLINE"
    access_mode = "API-autonomous"

    def run_query(self, query_spec: QuerySpec) -> QueryRunResult:
        query_run_id = str(uuid4())
        params = {
            "db": "pubmed", "term": query_spec.query_string,
            "retmax": 1, "retmode": "json", "usehistory": "y"
        }
        search_url = f"{ESEARCH_URL}?{urllib.parse.urlencode(params)}"
        try:
            r = requests.get(ESEARCH_URL, params=params, timeout=30)
            r.raise_for_status()
            data = r.json()
            count = int(data["esearchresult"].get("count", 0))
        except Exception as e:
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

        # Step 1: esearch with usehistory to get WebEnv/query_key
        params = {
            "db": "pubmed", "term": qs.query_string,
            "retmax": MAX_RECORDS, "retmode": "json", "usehistory": "y"
        }
        try:
            r = requests.get(ESEARCH_URL, params=params, timeout=30)
            r.raise_for_status()
            data = r.json()
            pmids = data["esearchresult"].get("idlist", [])
            web_env = data["esearchresult"].get("webenv", "")
            query_key = data["esearchresult"].get("querykey", "")
        except Exception as e:
            return []

        # Step 2: efetch in batches
        for start in range(0, len(pmids), BATCH_SIZE):
            batch = pmids[start:start + BATCH_SIZE]
            try:
                fetch_params = {
                    "db": "pubmed", "id": ",".join(batch),
                    "retmode": "xml", "rettype": "abstract"
                }
                fr = requests.get(EFETCH_URL, params=fetch_params, timeout=60)
                fr.raise_for_status()
                records = self._parse_xml(fr.text, query_run.query_run_id)
                raw_records.extend(records)
                time.sleep(0.4)  # NCBI polite pool: max 3 req/s without API key
            except Exception as e:
                pass

        return raw_records

    def _parse_xml(self, xml_text: str, query_run_id: str) -> List[RawRecord]:
        records = []
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            return []

        for article in root.findall(".//PubmedArticle"):
            try:
                medline = article.find("MedlineCitation")
                art = medline.find("Article") if medline is not None else None

                # PMID
                pmid_el = medline.find("PMID") if medline is not None else None
                pmid = pmid_el.text.strip() if pmid_el is not None else ""

                # Title
                title_el = art.find("ArticleTitle") if art is not None else None
                title = "".join(title_el.itertext()).strip() if title_el is not None else ""

                # Abstract
                abstract_parts = []
                if art is not None:
                    for at in art.findall(".//AbstractText"):
                        label = at.get("Label", "")
                        text = "".join(at.itertext()).strip()
                        if label:
                            abstract_parts.append(f"{label}: {text}")
                        else:
                            abstract_parts.append(text)
                abstract = " ".join(abstract_parts)

                # Authors
                authors = []
                if art is not None:
                    for a in art.findall(".//Author"):
                        ln = a.findtext("LastName", "")
                        fn = a.findtext("ForeName", "")
                        name = f"{ln} {fn}".strip()
                        if name:
                            authors.append(name)
                authors_str = ", ".join(authors)

                # Journal + Year
                journal = ""
                year = ""
                journal_el = art.find("Journal") if art is not None else None
                if journal_el is not None:
                    journal = journal_el.findtext("Title", "") or journal_el.findtext("ISOAbbreviation", "")
                    ji = journal_el.find("JournalIssue")
                    if ji is not None:
                        pd = ji.find("PubDate")
                        if pd is not None:
                            year = pd.findtext("Year", "") or pd.findtext("MedlineDate", "")[:4]

                # DOI
                doi = ""
                if art is not None:
                    for eid in art.findall(".//ELocationID"):
                        if eid.get("EIdType") == "doi":
                            doi = eid.text or ""
                            break

                # PMCID
                pmcid = ""
                for aid in article.findall(".//ArticleId"):
                    if aid.get("IdType") == "pmc":
                        pmcid = aid.text or ""

                # MeSH
                mesh = []
                if medline is not None:
                    for mh in medline.findall(".//MeshHeading"):
                        dn = mh.findtext("DescriptorName", "")
                        if dn:
                            mesh.append(dn)

                # Publication types
                pub_types = []
                if art is not None:
                    for pt in art.findall(".//PublicationType"):
                        pub_types.append(pt.text or "")

                # Language
                language = ""
                if art is not None:
                    lang_el = art.find("Language")
                    language = lang_el.text if lang_el is not None else ""

                raw_meta = ET.tostring(article, encoding="unicode")

                records.append(RawRecord(
                    query_run_id=query_run_id,
                    source_database="PubMed",
                    source_record_id=pmid,
                    source_url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    raw_title=title,
                    raw_authors=authors_str,
                    raw_year=year,
                    raw_journal=journal,
                    raw_doi=doi,
                    raw_pmid=pmid,
                    raw_pmcid=pmcid,
                    raw_abstract=abstract,
                    raw_publication_type=", ".join(pub_types),
                    raw_language=language,
                    raw_metadata_json=raw_meta,
                ))
            except Exception:
                continue

        return records

    def normalize_record(self, raw: RawRecord, raw_record_id: str):
        norm = super().normalize_record(raw, raw_record_id)
        # Store MeSH and PubTypes from raw XML metadata
        try:
            root = ET.fromstring(raw.raw_metadata_json)
            # Re-extract MeSH
            mesh = []
            for mh in root.findall(".//MeshHeading"):
                dn = mh.findtext("DescriptorName", "")
                if dn:
                    mesh.append(dn)
            norm.mesh_terms_json = json.dumps(mesh)
            
            # Re-extract Publication Types
            pub_types = []
            for pt in root.findall(".//PublicationType"):
                pub_types.append(pt.text or "")
            norm.publication_type = ", ".join(pub_types)
        except Exception:
            pass
        return norm
