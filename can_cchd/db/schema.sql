-- Core Tables
CREATE TABLE IF NOT EXISTS research_plans (
    research_plan_id TEXT PRIMARY KEY,
    title TEXT,
    review_question TEXT,
    objective TEXT,
    primary_denominator TEXT,
    primary_outcome TEXT,
    secondary_outcomes_json TEXT,
    criteria_json TEXT,
    case_report_policy TEXT,
    status TEXT,
    created_at TEXT,
    approved_at TEXT
);

CREATE TABLE IF NOT EXISTS protocol_versions (
    protocol_version_id TEXT PRIMARY KEY,
    research_plan_id TEXT,
    version_number INTEGER,
    protocol_markdown TEXT,
    query_plan_json TEXT,
    criteria_json TEXT,
    approved_at TEXT,
    approved_by TEXT
);

CREATE TABLE IF NOT EXISTS workflow_phases (
    phase_id TEXT PRIMARY KEY,
    phase_order INTEGER,
    phase_name TEXT,
    status TEXT,
    started_at TEXT,
    completed_at TEXT,
    completion_note TEXT,
    skip_justification TEXT,
    locked_reason TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS research_sources (
    source_id TEXT PRIMARY KEY,
    protocol_version_id TEXT,
    source_name TEXT,
    priority_order INTEGER,
    access_mode TEXT,
    required_status TEXT,
    status TEXT,
    rationale TEXT,
    records_found INTEGER,
    records_imported INTEGER,
    records_unique_after_dedup INTEGER,
    completed_at TEXT,
    closure_note TEXT
);

CREATE TABLE IF NOT EXISTS research_queries (
    query_id TEXT PRIMARY KEY,
    source_id TEXT,
    query_label TEXT,
    query_role TEXT,
    query_string TEXT,
    status TEXT,
    result_count INTEGER,
    records_imported INTEGER,
    run_at TEXT,
    notes TEXT
);

-- Agent Tables
CREATE TABLE IF NOT EXISTS agent_runs (
    agent_run_id TEXT PRIMARY KEY,
    protocol_version_id TEXT,
    phase_id TEXT,
    status TEXT,
    execution_mode TEXT,
    current_source TEXT,
    current_query_label TEXT,
    current_action TEXT,
    started_at TEXT,
    completed_at TEXT,
    records_found_total INTEGER,
    records_imported_total INTEGER,
    warnings_count INTEGER,
    human_interventions_count INTEGER,
    summary TEXT
);

CREATE TABLE IF NOT EXISTS agent_action_log (
    action_id TEXT PRIMARY KEY,
    agent_run_id TEXT,
    timestamp TEXT,
    source_database TEXT,
    source_access_mode TEXT,
    action_type TEXT,
    action_status TEXT,
    query_label TEXT,
    query_string TEXT,
    url TEXT,
    result_count INTEGER,
    records_exported INTEGER,
    records_imported INTEGER,
    duplicates_detected INTEGER,
    download_path TEXT,
    screenshot_path TEXT,
    html_snapshot_path TEXT,
    message TEXT,
    error_message TEXT,
    requires_human_intervention INTEGER
);

CREATE TABLE IF NOT EXISTS agent_interventions (
    intervention_id TEXT PRIMARY KEY,
    agent_run_id TEXT,
    source_database TEXT,
    query_label TEXT,
    intervention_type TEXT,
    message TEXT,
    status TEXT,
    created_at TEXT,
    resolved_at TEXT,
    resolution_note TEXT
);

-- Evidence Tables
CREATE TABLE IF NOT EXISTS studies (
    study_id TEXT PRIMARY KEY,
    title TEXT,
    first_author TEXT,
    year INTEGER,
    journal TEXT,
    doi TEXT,
    pmid TEXT,
    pmcid TEXT,
    country TEXT,
    study_design TEXT,
    status TEXT,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS records (
    record_id TEXT PRIMARY KEY,
    study_id TEXT,
    source_id TEXT,
    query_id TEXT,
    source_database TEXT,
    source_record_id TEXT,
    title TEXT,
    authors TEXT,
    year INTEGER,
    journal TEXT,
    doi TEXT,
    pmid TEXT,
    pmcid TEXT,
    abstract TEXT,
    url TEXT,
    pdf_url TEXT,
    is_open_access INTEGER,
    metadata_json TEXT,
    imported_at TEXT
);

-- Additional basic tables to avoid missing table errors later
CREATE TABLE IF NOT EXISTS duplicate_groups (
    group_id TEXT PRIMARY KEY,
    match_type TEXT,
    match_key TEXT,
    status TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS duplicate_group_members (
    group_id TEXT,
    record_id TEXT,
    is_representative INTEGER,
    PRIMARY KEY (group_id, record_id)
);

CREATE TABLE IF NOT EXISTS study_links (
    study_id TEXT,
    record_id TEXT,
    PRIMARY KEY (study_id, record_id)
);

CREATE TABLE IF NOT EXISTS screening_decisions (
    decision_id TEXT PRIMARY KEY,
    study_id TEXT,
    decision TEXT,
    reason TEXT,
    decided_by TEXT,
    decided_at TEXT
);

CREATE TABLE IF NOT EXISTS fulltext_records (
    study_id TEXT PRIMARY KEY,
    status TEXT,
    file_path TEXT,
    note TEXT,
    retrieved_at TEXT
);

CREATE TABLE IF NOT EXISTS eligibility_decisions (
    decision_id TEXT PRIMARY KEY,
    study_id TEXT,
    decision TEXT,
    checklist_json TEXT,
    reason TEXT,
    decided_by TEXT,
    decided_at TEXT
);

CREATE TABLE IF NOT EXISTS extraction_tasks (
    task_id TEXT PRIMARY KEY,
    study_id TEXT,
    status TEXT,
    assigned_to TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS extraction_fields (
    field_id TEXT PRIMARY KEY,
    study_id TEXT,
    field_name TEXT,
    value_raw TEXT,
    value_numeric REAL,
    source_location TEXT,
    supporting_quote TEXT,
    confidence REAL,
    status TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS diagnosis_mappings (
    mapping_id TEXT PRIMARY KEY,
    study_id TEXT,
    original_term TEXT,
    case_count INTEGER,
    source_quote TEXT,
    mapped_category TEXT,
    is_can_cchd INTEGER,
    overlap_possible INTEGER,
    status TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS qa_findings (
    finding_id TEXT PRIMARY KEY,
    rule_name TEXT,
    severity TEXT,
    description TEXT,
    study_id TEXT,
    status TEXT,
    resolution_note TEXT,
    created_at TEXT,
    updated_at TEXT
);

-- ============================================================
-- COLLECTION REFORM TABLES (Robust Search Collection Reform)
-- ============================================================

-- Tracks every executed query run with full provenance
CREATE TABLE IF NOT EXISTS query_runs (
    query_run_id TEXT PRIMARY KEY,
    protocol_version_id TEXT,
    source_id TEXT,
    source_database TEXT,
    query_label TEXT,
    query_role TEXT,
    query_string TEXT,
    access_mode TEXT,
    execution_mode TEXT,
    run_started_at TEXT,
    run_completed_at TEXT,
    search_url TEXT,
    filters_applied_json TEXT,
    result_count_reported INTEGER,
    records_harvested INTEGER DEFAULT 0,
    records_imported_raw INTEGER DEFAULT 0,
    records_enriched INTEGER DEFAULT 0,
    records_failed INTEGER DEFAULT 0,
    warnings_json TEXT,
    human_intervention_required INTEGER DEFAULT 0,
    status TEXT DEFAULT 'not_started'
);

-- Immutable source output — never edited after insertion
CREATE TABLE IF NOT EXISTS raw_records (
    raw_record_id TEXT PRIMARY KEY,
    query_run_id TEXT,
    source_database TEXT,
    source_record_id TEXT,
    source_url TEXT,
    raw_title TEXT,
    raw_authors TEXT,
    raw_year TEXT,
    raw_journal TEXT,
    raw_doi TEXT,
    raw_pmid TEXT,
    raw_pmcid TEXT,
    raw_abstract TEXT,
    raw_publication_type TEXT,
    raw_language TEXT,
    raw_metadata_json TEXT,
    harvested_at TEXT,
    raw_hash TEXT
);

-- Cleaned, standardized version of raw_records
CREATE TABLE IF NOT EXISTS normalized_records (
    record_id TEXT PRIMARY KEY,
    raw_record_id TEXT,
    query_run_id TEXT,
    source_database TEXT,
    source_record_id TEXT,
    title TEXT,
    title_normalized TEXT,
    authors_raw TEXT,
    first_author TEXT,
    year INTEGER,
    journal TEXT,
    doi TEXT,
    doi_normalized TEXT,
    pmid TEXT,
    pmcid TEXT,
    abstract TEXT,
    abstract_status TEXT DEFAULT 'unknown',
    publication_type TEXT,
    language TEXT,
    country TEXT,
    keywords_json TEXT,
    mesh_terms_json TEXT,
    landing_page_url TEXT,
    pdf_url TEXT,
    is_open_access INTEGER DEFAULT 0,
    oa_status TEXT,
    metadata_completeness_score REAL DEFAULT 0,
    metadata_warnings_json TEXT,
    normalization_status TEXT DEFAULT 'pending',
    enrichment_status TEXT DEFAULT 'pending',
    is_supplementary_source INTEGER DEFAULT 0,
    created_at TEXT,
    updated_at TEXT
);

-- Enrichment attempt log (one row per attempt per record)
CREATE TABLE IF NOT EXISTS record_enrichment_log (
    enrichment_id TEXT PRIMARY KEY,
    record_id TEXT,
    enrichment_source TEXT,
    identifier_used TEXT,
    identifier_value TEXT,
    fields_updated_json TEXT,
    warnings_json TEXT,
    status TEXT,
    started_at TEXT,
    completed_at TEXT
);

-- Collection QA findings (per record or per query_run)
CREATE TABLE IF NOT EXISTS collection_qa_findings (
    collection_qa_id TEXT PRIMARY KEY,
    record_id TEXT,
    query_run_id TEXT,
    severity TEXT,
    finding_type TEXT,
    message TEXT,
    recommended_action TEXT,
    status TEXT DEFAULT 'open',
    created_at TEXT,
    resolved_at TEXT,
    resolution_note TEXT
);

-- Collection QA gate status (one row, updated after each QA run)
CREATE TABLE IF NOT EXISTS collection_qa_gate (
    gate_id TEXT PRIMARY KEY DEFAULT 'main',
    status TEXT DEFAULT 'not_run',
    last_run_at TEXT,
    total_records INTEGER DEFAULT 0,
    screening_ready INTEGER DEFAULT 0,
    screening_ready_with_warning INTEGER DEFAULT 0,
    enrichment_needed INTEGER DEFAULT 0,
    collection_problem INTEGER DEFAULT 0,
    blocking_findings INTEGER DEFAULT 0,
    warning_findings INTEGER DEFAULT 0,
    summary_json TEXT
);

-- ============================================================
-- DEDUP REBUILD TABLES (normalized_records -> unique_studies)
-- ============================================================

CREATE TABLE IF NOT EXISTS dedup_groups (
    dedup_group_id TEXT PRIMARY KEY,
    match_type TEXT,
    match_key TEXT,
    confidence REAL,
    status TEXT,
    representative_record_id TEXT,
    representative_study_id TEXT,
    created_at TEXT,
    reviewed_at TEXT,
    reviewer_note TEXT
);

CREATE TABLE IF NOT EXISTS dedup_group_members (
    dedup_group_id TEXT,
    record_id TEXT,
    is_representative_candidate INTEGER DEFAULT 0,
    source_database TEXT,
    query_run_id TEXT,
    query_label TEXT,
    pmid TEXT,
    doi TEXT,
    pmcid TEXT,
    title TEXT,
    year INTEGER,
    journal TEXT,
    metadata_completeness_score REAL,
    PRIMARY KEY (dedup_group_id, record_id)
);

CREATE TABLE IF NOT EXISTS unique_studies (
    study_id TEXT PRIMARY KEY,
    representative_record_id TEXT,
    title TEXT,
    first_author TEXT,
    year INTEGER,
    journal TEXT,
    doi TEXT,
    pmid TEXT,
    pmcid TEXT,
    abstract TEXT,
    publication_type TEXT,
    language TEXT,
    source_databases_json TEXT,
    query_labels_json TEXT,
    query_run_ids_json TEXT,
    linked_record_count INTEGER,
    metadata_completeness_score REAL,
    dedup_status TEXT,
    screening_status TEXT DEFAULT 'not_started',
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS unique_study_record_links (
    study_id TEXT,
    record_id TEXT,
    raw_record_id TEXT,
    query_run_id TEXT,
    source_database TEXT,
    query_label TEXT,
    link_reason TEXT,
    created_at TEXT,
    PRIMARY KEY (study_id, record_id)
);

CREATE TABLE IF NOT EXISTS dedup_audit_log (
    audit_id TEXT PRIMARY KEY,
    timestamp TEXT,
    action_type TEXT,
    dedup_group_id TEXT,
    study_id TEXT,
    record_ids_json TEXT,
    previous_status TEXT,
    new_status TEXT,
    reason TEXT,
    reviewer_note TEXT
);
