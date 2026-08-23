import json
import sqlite3
import unittest
from pathlib import Path

from can_cchd.dedup.manager import bulk_merge_exact, process_singletons
from can_cchd.dedup.matcher import run_exact_matcher, run_fuzzy_matcher
from can_cchd.screening.manager import get_next_candidate, get_screening_progress, save_decision


SCHEMA_PATH = Path(__file__).resolve().parents[1] / 'can_cchd' / 'db' / 'schema.sql'


def make_conn():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA_PATH.read_text(encoding='utf-8'))
    conn.execute(
        """
        INSERT INTO collection_qa_gate (
            gate_id, status, last_run_at, total_records, screening_ready, screening_ready_with_warning,
            enrichment_needed, collection_problem, blocking_findings, warning_findings, summary_json
        ) VALUES ('main', 'pass', '2026-01-01T00:00:00+00:00', 0, 0, 0, 0, 0, 0, 0, '{}')
        """
    )
    return conn


class DedupFromNormalizedRecordsTests(unittest.TestCase):
    def setUp(self):
        self.conn = make_conn()
        self._insert_query_run('qr-1', 'Primary')
        self._insert_query_run('qr-2', 'Secondary')

    def tearDown(self):
        self.conn.close()

    def _insert_query_run(self, query_run_id, query_label):
        self.conn.execute(
            """
            INSERT INTO query_runs (
                query_run_id, source_id, source_database, query_label, query_role,
                query_string, access_mode, execution_mode, run_started_at, status
            ) VALUES (?, 'src-1', 'PubMed', ?, 'primary', 'query', 'api', 'api_automated', '2026-01-01T00:00:00+00:00', 'completed')
            """,
            (query_run_id, query_label),
        )
        self.conn.commit()

    def _insert_normalized_record(self, record_id, query_run_id='qr-1', source_database='PubMed', **overrides):
        raw_record_id = overrides.pop('raw_record_id', f'raw-{record_id}')
        self.conn.execute(
            """
            INSERT OR IGNORE INTO raw_records (
                raw_record_id, query_run_id, source_database, source_record_id, source_url,
                raw_title, raw_authors, raw_year, raw_journal, raw_doi, raw_pmid, raw_pmcid,
                raw_abstract, raw_metadata_json, harvested_at, raw_hash
            ) VALUES (?, ?, ?, ?, 'https://example.test', ?, 'Author, A', '2024', 'Journal', ?, ?, ?, ?, '{"raw": true}', '2026-01-01T00:00:00+00:00', ?)
            """,
            (
                raw_record_id,
                query_run_id,
                source_database,
                f'source-{record_id}',
                overrides.get('title', 'Shared Title'),
                overrides.get('doi', ''),
                overrides.get('pmid', ''),
                overrides.get('pmcid', ''),
                overrides.get('abstract', 'This is a sufficiently long abstract for dedup tests.'),
                f'hash-{record_id}',
            ),
        )
        values = {
            'record_id': record_id,
            'raw_record_id': raw_record_id,
            'query_run_id': query_run_id,
            'source_database': source_database,
            'source_record_id': f'source-{record_id}',
            'title': overrides.get('title', 'Shared Title For Dedup Testing'),
            'title_normalized': overrides.get('title_normalized', overrides.get('title', 'Shared Title For Dedup Testing').lower()),
            'authors_raw': overrides.get('authors_raw', 'Author, A'),
            'first_author': overrides.get('first_author', 'Author'),
            'year': overrides.get('year', 2024),
            'journal': overrides.get('journal', 'Journal'),
            'doi': overrides.get('doi', ''),
            'doi_normalized': overrides.get('doi_normalized', overrides.get('doi', '').lower()),
            'pmid': overrides.get('pmid', ''),
            'pmcid': overrides.get('pmcid', ''),
            'abstract': overrides.get('abstract', 'This is a sufficiently long abstract for dedup tests.'),
            'abstract_status': overrides.get('abstract_status', 'available'),
            'publication_type': 'Journal Article',
            'language': 'en',
            'country': 'US',
            'keywords_json': '[]',
            'mesh_terms_json': '[]',
            'landing_page_url': 'https://example.test',
            'pdf_url': '',
            'is_open_access': 0,
            'oa_status': '',
            'metadata_completeness_score': overrides.get('metadata_completeness_score', 95),
            'metadata_warnings_json': '[]',
            'normalization_status': 'complete',
            'enrichment_status': 'not_required',
            'is_supplementary_source': 0,
            'created_at': '2026-01-01T00:00:00+00:00',
            'updated_at': '2026-01-01T00:00:00+00:00',
        }
        columns = ', '.join(values.keys())
        placeholders = ', '.join('?' for _ in values)
        self.conn.execute(f"INSERT INTO normalized_records ({columns}) VALUES ({placeholders})", tuple(values.values()))
        self.conn.commit()

    def _group_types(self):
        rows = self.conn.execute('SELECT match_type, status FROM dedup_groups').fetchall()
        return [(row['match_type'], row['status']) for row in rows]

    def test_exact_pmid_groups_created_from_normalized_records(self):
        self._insert_normalized_record('rec-1', pmid='12345')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmid='12345')
        run_exact_matcher(self.conn)
        rows = self.conn.execute("SELECT match_type FROM dedup_groups WHERE match_type = 'exact_pmid'").fetchall()
        self.assertEqual(len(rows), 1)

    def test_exact_doi_groups_created_from_normalized_records(self):
        self._insert_normalized_record('rec-1', doi='10.1000/x')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', doi='10.1000/x', doi_normalized='10.1000/x')
        run_exact_matcher(self.conn)
        rows = self.conn.execute("SELECT match_type FROM dedup_groups WHERE match_type = 'exact_doi'").fetchall()
        self.assertEqual(len(rows), 1)

    def test_exact_pmcid_groups_created_from_normalized_records(self):
        self._insert_normalized_record('rec-1', pmcid='PMC123')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmcid='PMC123')
        run_exact_matcher(self.conn)
        rows = self.conn.execute("SELECT match_type FROM dedup_groups WHERE match_type = 'exact_pmcid'").fetchall()
        self.assertEqual(len(rows), 1)

    def test_exact_title_groups_created_from_normalized_records(self):
        title = 'A very long shared title for normalized record deduplication'
        self._insert_normalized_record('rec-1', title=title, title_normalized=title.lower())
        self._insert_normalized_record('rec-2', query_run_id='qr-2', title=title, title_normalized=title.lower(), pmid='', doi='', pmcid='')
        run_exact_matcher(self.conn)
        rows = self.conn.execute("SELECT match_type FROM dedup_groups WHERE match_type = 'exact_title'").fetchall()
        self.assertEqual(len(rows), 1)

    def test_dedup_does_not_use_legacy_records_table(self):
        self._insert_normalized_record('rec-1', pmid='777')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmid='777')
        run_exact_matcher(self.conn)
        count = self.conn.execute('SELECT COUNT(*) AS c FROM records').fetchone()['c']
        self.assertEqual(count, 0)
        groups = self.conn.execute('SELECT COUNT(*) AS c FROM dedup_groups').fetchone()['c']
        self.assertEqual(groups, 1)

    def test_bulk_merge_creates_unique_study(self):
        self._insert_normalized_record('rec-1', pmid='12345')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmid='12345')
        run_exact_matcher(self.conn)
        merged = bulk_merge_exact(self.conn)
        studies = self.conn.execute('SELECT COUNT(*) AS c FROM unique_studies').fetchone()['c']
        self.assertEqual(merged, 1)
        self.assertEqual(studies, 1)

    def test_bulk_merge_preserves_all_record_links(self):
        self._insert_normalized_record('rec-1', pmid='12345')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmid='12345')
        run_exact_matcher(self.conn)
        bulk_merge_exact(self.conn)
        links = self.conn.execute('SELECT COUNT(*) AS c FROM unique_study_record_links').fetchone()['c']
        self.assertEqual(links, 2)

    def test_unique_study_aggregates_source_databases(self):
        self._insert_normalized_record('rec-1', pmid='12345', source_database='PubMed')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmid='12345', source_database='Europe PMC')
        run_exact_matcher(self.conn)
        bulk_merge_exact(self.conn)
        row = self.conn.execute('SELECT source_databases_json FROM unique_studies').fetchone()
        self.assertEqual(json.loads(row['source_databases_json']), ['Europe PMC', 'PubMed'])

    def test_unique_study_aggregates_query_labels(self):
        self._insert_normalized_record('rec-1', pmid='12345', query_run_id='qr-1')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmid='12345')
        run_exact_matcher(self.conn)
        bulk_merge_exact(self.conn)
        row = self.conn.execute('SELECT query_labels_json FROM unique_studies').fetchone()
        self.assertEqual(json.loads(row['query_labels_json']), ['Primary', 'Secondary'])

    def test_fuzzy_match_requires_human_review(self):
        title_1 = 'evaluation of pulse oximetry for congenital heart disease screening in newborns'
        title_2 = 'evaluation of pulse oximetry in congenital heart disease screening among newborns'
        self._insert_normalized_record('rec-1', title=title_1, title_normalized=title_1)
        self._insert_normalized_record('rec-2', query_run_id='qr-2', title=title_2, title_normalized=title_2, pmid='', doi='', pmcid='')
        run_fuzzy_matcher(self.conn)
        row = self.conn.execute("SELECT status FROM dedup_groups WHERE match_type = 'fuzzy_title'").fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row['status'], 'pending')

    def test_singletons_created_after_groups_resolved(self):
        self._insert_normalized_record('rec-1', pmid='12345')
        self._insert_normalized_record('rec-2', query_run_id='qr-2', pmid='12345')
        self._insert_normalized_record('rec-3', title='A singleton record title long enough for screening', pmid='', doi='', pmcid='')
        run_exact_matcher(self.conn)
        bulk_merge_exact(self.conn)
        created = process_singletons(self.conn)
        total = self.conn.execute('SELECT COUNT(*) AS c FROM unique_studies').fetchone()['c']
        self.assertEqual(created, 1)
        self.assertEqual(total, 2)

    def test_screening_input_is_unique_studies(self):
        self._insert_normalized_record('rec-1', title='A singleton record title long enough for screening', pmid='', doi='', pmcid='')
        process_singletons(self.conn)
        candidate = get_next_candidate(self.conn)
        self.assertIsNotNone(candidate)
        self.assertEqual(candidate['title'], 'A singleton record title long enough for screening')
        save_decision(self.conn, candidate['study_id'], 'include')
        progress = get_screening_progress(self.conn)
        self.assertEqual(progress['completed'], 1)
        self.assertEqual(progress['pending'], 0)


if __name__ == '__main__':
    unittest.main()
