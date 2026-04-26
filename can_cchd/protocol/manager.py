import json
import datetime
from uuid import uuid4

DEFAULT_PROTOCOL = {
    "title": "Clinically Actionable Non-CCHD Diagnoses After Failed Newborn Pulse Oximetry Screening for Critical Congenital Heart Disease: A Systematic Review and Meta-analysis",
    "review_question": "Among newborns who fail pulse oximetry screening for critical congenital heart disease but are not diagnosed with CCHD, what proportion have clinically actionable non-CCHD diagnoses?",
    "primary_denominator": "CCHD-negative failed screens",
    "primary_outcome": "Any CAN-CCHD diagnosis among CCHD-negative failed screens (number_can_cchd / number_cchd_negative_failed)",
    "secondary_outcomes": [
        "PPHN / pulmonary hypertension",
        "respiratory disease",
        "infection / sepsis / sepsis workup",
        "non-critical congenital heart disease",
        "NICU admission",
        "oxygen therapy or respiratory support",
        "antibiotic treatment or sepsis workup",
        "delayed discharge",
        "echocardiography / cardiology review",
        "no actionable diagnosis"
    ],
    "inclusion_criteria": [
        "include newborns/neonates or a newborn screening population",
        "evaluate/report pulse oximetry screening",
        "relate to CCHD screening",
        "report failed/positive/abnormal screen data",
        "allow identification of failed screens in which CCHD was not diagnosed, directly or by calculation",
        "report diagnosis, clinical outcome, management, or no-diagnosis category among CCHD-negative failed screens"
    ],
    "case_report_policy": "citation_mining_only, conceptual_background_only, rare_CAN_CCHD_signal, excluded_from_quantitative_synthesis"
}

def get_current_protocol(conn):
    """Fetches the current protocol from the database, or returns the default if none exists."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM research_plans ORDER BY created_at DESC LIMIT 1")
    row = cursor.fetchone()
    
    if row:
        return {
            "research_plan_id": row["research_plan_id"],
            "title": row["title"],
            "review_question": row["review_question"],
            "primary_denominator": row["primary_denominator"],
            "primary_outcome": row["primary_outcome"],
            "secondary_outcomes": json.loads(row["secondary_outcomes_json"]) if row["secondary_outcomes_json"] else [],
            "inclusion_criteria": json.loads(row["criteria_json"]) if row["criteria_json"] else [],
            "case_report_policy": row["case_report_policy"],
            "status": row["status"]
        }
    return DEFAULT_PROTOCOL.copy()

def initialize_default_protocol(conn):
    cursor = conn.cursor()
    plan_id = str(uuid4())
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    cursor.execute(
        """INSERT INTO research_plans (
            research_plan_id, title, review_question, primary_denominator, primary_outcome,
            secondary_outcomes_json, criteria_json, case_report_policy, status, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            plan_id, 
            DEFAULT_PROTOCOL["title"], 
            DEFAULT_PROTOCOL["review_question"],
            DEFAULT_PROTOCOL["primary_denominator"],
            DEFAULT_PROTOCOL["primary_outcome"],
            json.dumps(DEFAULT_PROTOCOL["secondary_outcomes"]),
            json.dumps(DEFAULT_PROTOCOL["inclusion_criteria"]),
            DEFAULT_PROTOCOL["case_report_policy"],
            "draft",
            now
        )
    )
    conn.commit()
    return get_current_protocol(conn)

def approve_protocol(conn, plan_id):
    """Approves the protocol and unlocks Phase 1."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    cursor.execute(
        "UPDATE research_plans SET status = 'approved', approved_at = ? WHERE research_plan_id = ?",
        (now, plan_id)
    )
    
    # Also create a protocol_version entry
    version_id = str(uuid4())
    cursor.execute(
        """INSERT INTO protocol_versions (
            protocol_version_id, research_plan_id, version_number, approved_at, approved_by
        ) VALUES (?, ?, 1, ?, 'human_physician')""",
        (version_id, plan_id, now)
    )
    
    # Initialize sources required for Phase 1 based on spec
    init_research_sources(cursor, version_id)
    
    conn.commit()
    
    # Unlock phase 1
    from can_cchd.workflow.next_action import update_phase_status
    update_phase_status(conn, "0", "completed", "Protocol Approved")

def init_research_sources(cursor, version_id):
    """Initializes the default research sources required by the protocol."""
    sources = [
        ("PubMed/MEDLINE", 1, "api_autonomous", "required"),
        ("Europe PMC", 2, "api_autonomous", "required"),
        ("Embase", 3, "supervised_login", "optional"),
        ("Scopus", 4, "supervised_login", "optional"),
        ("LILACS/BVS", 5, "browser_supervised", "required"),
        ("SciELO", 6, "browser_supervised", "required"),
        ("IMEMR", 7, "browser_supervised", "required"),
        ("Google Scholar", 8, "browser_supervised", "supplementary")
    ]
    
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    for name, priority, access_mode, required_status in sources:
        cursor.execute(
            """INSERT INTO research_sources (
                source_id, protocol_version_id, source_name, priority_order, access_mode, required_status, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (str(uuid4()), version_id, name, priority, access_mode, required_status, "not_started")
        )

def update_protocol(conn, plan_id, data):
    """Updates an existing draft protocol."""
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE research_plans 
           SET title = ?, review_question = ?, primary_denominator = ?, primary_outcome = ?,
               secondary_outcomes_json = ?, criteria_json = ?, case_report_policy = ?
           WHERE research_plan_id = ? AND status = 'draft'""",
        (
            data["title"],
            data["review_question"],
            data["primary_denominator"],
            data["primary_outcome"],
            json.dumps(data["secondary_outcomes"]),
            json.dumps(data["inclusion_criteria"]),
            data["case_report_policy"],
            plan_id
        )
    )
    conn.commit()
