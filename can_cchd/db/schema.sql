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
