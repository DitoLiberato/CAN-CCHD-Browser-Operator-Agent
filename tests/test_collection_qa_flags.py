import datetime
import sqlite3
import unittest
from pathlib import Path

from can_cchd.collection.adapters.europepmc_adapter import EuropePMCAdapter
from can_cchd.collection.base_adapter import BaseAdapter, determine_initial_enrichment_status
from can_cchd.collection.completeness import calculate_completeness_score
from can_cchd.collection.models import NormalizedRecord
from can_cchd.collection.qa_gate import run_qa_gate


SCHEMA_PATH = Path(__file__).resolve().parents[1] / 'can_cchd' / 'db' / 'schema.sql'


class DummyAdapter(BaseAdapter):
    source_name = 'Dummy'
    access_mode = 'api'

    def run_query(self, query_spec):  # pragma: no cover
        raise NotImplementedError

    def harvest_records(self, query_run):  # pragma: no cover
        raise NotImplementedError


def make_conn():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA_PATH.read_text(encoding='utf-8'))
    return conn


class CollectionQAFlagTests(unittest.TestCase):
    def setUp(self):
        self.conn = make_conn()
        self.adapter = DummyAdapter(self.conn)
        self.current_year = datetime.datetime.now().year

    def tearDown(self):
        self.conn.close()

    def _record(self, **overrides):
        base = {
            'raw_record_id': 'raw-1',
            'query_run_id': 'qr-1',
            'source_database': 'PubMed',
            'source_record_id': 'source-1',
            'title': 'Useful title',
            'title_normalized': 'useful title',
            'authors_raw': 'Author, A',
            'first_author': 'Author',
            'year': self.current_year,
            'journal': 'Journal',
            'doi': '10.1000/test',
            'doi_normalized': '10.1000/test',
            'pmid': '100',
            'pmcid': '',
            'abstract': 'This is a sufficiently long abstract for testing current year behaviour.',
            'abstract_status': 'available',
            'landing_page_url': 'https://example.test',
        }
        base.update(overrides)
        return NormalizedRecord(**base)

    def test_current_year_pubmed_is_info_not_warning(self):
        findings = self.adapter.validate_record(self._record(), 'qr-1')
        current_year = [f for f in findings if f.finding_type == 'current_year']
        future_year = [f for f in findings if f.finding_type == 'future_year']
        self.assertEqual(len(current_year), 1)
        self.assertEqual(current_year[0].severity, 'info')
        self.assertFalse(future_year)

    def test_future_year_is_warning(self):
        findings = self.adapter.validate_record(self._record(year=self.current_year + 1), 'qr-1')
        future_year = [f for f in findings if f.finding_type == 'future_year']
        self.assertEqual(len(future_year), 1)
        self.assertEqual(future_year[0].severity, 'warning')

    def test_europepmc_current_year_with_pmid_requires_verification(self):
        adapter = EuropePMCAdapter(self.conn)
        findings = adapter.validate_record(self._record(source_database='Europe PMC'), 'qr-1')
        finding_types = {finding.finding_type: finding for finding in findings}
        self.assertIn('europepmc_year_needs_verification', finding_types)
        self.assertEqual(finding_types['europepmc_year_needs_verification'].severity, 'warning')

    def test_raw_metadata_score_requires_raw_metadata_json(self):
        record = self._record()
        without_raw = calculate_completeness_score(record, raw_metadata_available=False)
        with_raw = calculate_completeness_score(record, raw_metadata_available=True)
        self.assertEqual(with_raw - without_raw, 5)

    def test_complete_pubmed_record_enrichment_status_not_required(self):
        status = determine_initial_enrichment_status(self._record(), raw_metadata_available=True)
        self.assertEqual(status, 'not_required')

    def test_missing_abstract_after_enrichment_is_warning_not_blocking(self):
        self.conn.execute(
            """
            INSERT INTO query_runs (query_run_id, source_id, source_database, query_label, query_role, query_string, access_mode, execution_mode, run_started_at, status)
            VALUES ('qr-1', 'src-1', 'PubMed', 'Primary', 'primary', 'query', 'api', 'api_automated', '2026-01-01T00:00:00+00:00', 'completed')
            """
        )
        self.conn.execute(
            """
            INSERT INTO normalized_records (
                record_id, raw_record_id, query_run_id, source_database, source_record_id, title, title_normalized,
                authors_raw, first_author, year, journal, doi, doi_normalized, pmid, pmcid, abstract,
                abstract_status, publication_type, language, country, keywords_json, mesh_terms_json,
                landing_page_url, pdf_url, is_open_access, oa_status, metadata_completeness_score,
                metadata_warnings_json, normalization_status, enrichment_status, is_supplementary_source,
                created_at, updated_at
            ) VALUES (
                'rec-1', 'raw-1', 'qr-1', 'PubMed', 'source-1', 'Title', 'title', 'Author, A', 'Author', ?, 'Journal', '', '', '', '', '',
                'unavailable_after_enrichment', 'Journal Article', 'en', '', '[]', '[]',
                'https://example.test', '', 0, '', 55, '[]', 'complete', 'enrichment_attempted', 0,
                '2026-01-01T00:00:00+00:00', '2026-01-01T00:00:00+00:00'
            )
            """,
            (self.current_year,),
        )
        self.conn.commit()

        result = run_qa_gate(self.conn)
        warning_types = {item['type'] for item in result['warnings']}
        blocking_types = {item['type'] for item in result['blocking']}
        self.assertIn('missing_abstract_after_enrichment', warning_types)
        self.assertNotIn('missing_abstract_after_enrichment', blocking_types)
        self.assertEqual(result['status'], 'warn')


if __name__ == '__main__':
    unittest.main()
