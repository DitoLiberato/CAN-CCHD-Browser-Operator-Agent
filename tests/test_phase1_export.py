import sqlite3
import unittest
from pathlib import Path

from can_cchd.collection.exports import (
    NORMALIZED_RECORD_EXPORT_COLUMNS,
    get_full_normalized_records_export_df,
    get_normalized_records_preview_df,
    get_query_runs_export_df,
    get_raw_records_export_df,
)


SCHEMA_PATH = Path(__file__).resolve().parents[1] / 'can_cchd' / 'db' / 'schema.sql'


def make_conn():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA_PATH.read_text(encoding='utf-8'))
    return conn


class Phase1ExportTests(unittest.TestCase):
    def setUp(self):
        self.conn = make_conn()
        self._insert_query_run('qr-1', 'Primary query')
        self._insert_raw_record('raw-1', 'qr-1')
        for index in range(501):
            self._insert_normalized_record(
                record_id=f'rec-{index}',
                raw_record_id='raw-1',
                query_run_id='qr-1',
                title=f'Record {index}',
                pmid=f'{1000 + index}',
                doi=f'10.1000/{index}',
                pmcid=f'PMC{index}',
                abstract='This is a sufficiently long abstract for export testing.',
            )

    def tearDown(self):
        self.conn.close()

    def _insert_query_run(self, query_run_id, query_label):
        self.conn.execute(
            """
            INSERT INTO query_runs (
                query_run_id, source_id, source_database, query_label, query_role,
                query_string, access_mode, execution_mode, run_started_at, status
            ) VALUES (?, 'src-1', 'PubMed', ?, 'primary', 'heart disease', 'api', 'api_automated', '2026-01-01T00:00:00+00:00', 'completed')
            """,
            (query_run_id, query_label),
        )

    def _insert_raw_record(self, raw_record_id, query_run_id):
        self.conn.execute(
            """
            INSERT INTO raw_records (
                raw_record_id, query_run_id, source_database, source_record_id, source_url,
                raw_title, raw_authors, raw_year, raw_journal, raw_doi, raw_pmid, raw_pmcid,
                raw_abstract, raw_metadata_json, harvested_at, raw_hash
            ) VALUES (?, ?, 'PubMed', 'src-rec', 'https://example.test', 'Raw title', 'A. Author', '2024', 'Journal', '10.1000/base', '9000', 'PMC9000', 'Raw abstract text', '{"a":1}', '2026-01-01T00:00:00+00:00', 'hash-1')
            """,
            (raw_record_id, query_run_id),
        )

    def _insert_normalized_record(self, **overrides):
        base = {
            'record_id': 'rec-1',
            'raw_record_id': 'raw-1',
            'query_run_id': 'qr-1',
            'source_database': 'PubMed',
            'source_record_id': 'source-1',
            'title': 'Title',
            'title_normalized': 'title',
            'authors_raw': 'Author, A',
            'first_author': 'Author',
            'year': 2024,
            'journal': 'Journal',
            'doi': '10.1000/test',
            'doi_normalized': '10.1000/test',
            'pmid': '1000',
            'pmcid': 'PMC1000',
            'abstract': 'This is a sufficiently long abstract for testing.',
            'abstract_status': 'available',
            'publication_type': 'Journal Article',
            'language': 'en',
            'country': 'US',
            'keywords_json': '[]',
            'mesh_terms_json': '[]',
            'landing_page_url': 'https://example.test',
            'pdf_url': '',
            'is_open_access': 0,
            'oa_status': '',
            'metadata_completeness_score': 100,
            'metadata_warnings_json': '[]',
            'normalization_status': 'complete',
            'enrichment_status': 'not_required',
            'is_supplementary_source': 0,
            'created_at': '2026-01-01T00:00:00+00:00',
            'updated_at': '2026-01-01T00:00:00+00:00',
        }
        base.update(overrides)
        columns = ', '.join(base.keys())
        placeholders = ', '.join('?' for _ in base)
        self.conn.execute(f"INSERT INTO normalized_records ({columns}) VALUES ({placeholders})", tuple(base.values()))
        self.conn.commit()

    def test_full_normalized_export_has_no_limit(self):
        exported = get_full_normalized_records_export_df(self.conn)
        self.assertEqual(len(exported), 501)

    def test_preview_query_can_have_limit_but_export_query_cannot(self):
        preview = get_normalized_records_preview_df(self.conn)
        exported = get_full_normalized_records_export_df(self.conn)
        self.assertEqual(len(preview), 500)
        self.assertEqual(len(exported), 501)

    def test_export_includes_abstract_and_identifier_columns(self):
        exported = get_full_normalized_records_export_df(self.conn)
        for column in ('abstract', 'pmid', 'doi', 'pmcid'):
            self.assertIn(column, exported.columns)
        self.assertEqual(list(exported.columns), NORMALIZED_RECORD_EXPORT_COLUMNS)

    def test_query_runs_export_available(self):
        exported = get_query_runs_export_df(self.conn)
        self.assertEqual(len(exported), 1)
        self.assertIn('query_string', exported.columns)
        self.assertEqual(exported.iloc[0]['query_label'], 'Primary query')

    def test_raw_records_export_available(self):
        exported = get_raw_records_export_df(self.conn)
        self.assertEqual(len(exported), 1)
        self.assertIn('raw_metadata_json', exported.columns)
        self.assertEqual(exported.iloc[0]['raw_record_id'], 'raw-1')


if __name__ == '__main__':
    unittest.main()
