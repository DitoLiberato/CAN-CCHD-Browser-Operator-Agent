import streamlit as st
import os
import base64
from can_cchd.eligibility.manager import get_next_candidate, save_decision, get_eligibility_progress

CHECKLIST_ITEMS = [
    "Newborn/neonatal screening population",
    "Pulse oximetry used",
    "CCHD screening target",
    "Reports failed/positive/abnormal screens",
    "CCHD-positive and CCHD-negative failed screens identifiable",
    "Non-CCHD diagnosis/outcome/management/no-diagnosis category reported",
    "Denominator extractable or calculable"
]

EXCLUSION_REASONS = [
    "not_newborn_or_neonatal_screening",
    "not_pulse_oximetry_screening",
    "not_cchd_screening_program",
    "no_failed_or_positive_screen_data",
    "cannot_identify_cchd_negative_failed_screens",
    "no_non_cchd_diagnosis_outcome_or_management_reported",
    "no_extractable_or_calculable_denominator",
    "case_report",
    "review_article_citation_mining_only",
    "nicu_only_population_analyze_separately",
    "overlapping_cohort",
    "insufficient_data",
    "not_retrieved",
    "other"
]

def render_pdf_iframe(file_path):
    """Helper to embed a local PDF in Streamlit."""
    if not file_path or not os.path.exists(file_path):
        st.warning("No local PDF file available. Please view online.")
        return
        
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def render_phase5(conn):
    st.header("Phase 5: Full-Text Eligibility")
    
    progress = get_eligibility_progress(conn)
    total = progress["total"]
    completed = progress["completed"]
    pending = progress["pending"]
    
    if total > 0:
        st.progress(completed / total, text=f"Progress: {completed} / {total} studies reviewed ({pending} remaining)")
    else:
        st.warning("No studies available for full-text review. Did you complete Phase 4?")
        return
        
    if pending == 0:
        st.success("✅ Full-Text Eligibility complete!")
        if st.button("Complete Phase 5 and Unlock Data Extraction", type="primary"):
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "5", "completed")
            st.rerun()
        return
        
    st.divider()
    
    study = get_next_candidate(conn)
    if not study:
        st.error("Error retrieving next candidate.")
        return
        
    # Layout: PDF Viewer on Left, Form on Right
    col_pdf, col_form = st.columns([1.5, 1])
    
    with col_pdf:
        st.subheader(f"Document: {study['title']}")
        render_pdf_iframe(study.get('file_path'))
        
    with col_form:
        st.subheader("Eligibility Checklist")
        st.write("All must be checked for quantitative inclusion.")
        
        checklist_state = {}
        for item in CHECKLIST_ITEMS:
            checklist_state[item] = st.checkbox(item, key=f"chk_{item}")
            
        all_checked = all(checklist_state.values())
        
        st.divider()
        st.subheader("Decision")
        
        if st.button("✅ Include Quantitative", disabled=not all_checked, use_container_width=True, type="primary"):
            save_decision(conn, study["study_id"], "included_quantitative", checklist_state)
            st.rerun()
            
        if not all_checked:
            st.caption("You must check all criteria to include.")
            
        if st.button("⛔ Exclude Full Text", use_container_width=True):
            st.session_state.show_ft_exclusion = True
            
        with st.popover("More Options", use_container_width=True):
            if st.button("Citation Mining Only"):
                save_decision(conn, study["study_id"], "citation_mining_only", checklist_state)
                st.rerun()
            if st.button("Separate Analysis"):
                save_decision(conn, study["study_id"], "separate_analysis", checklist_state)
                st.rerun()
            if st.button("Not Retrieved"):
                save_decision(conn, study["study_id"], "not_retrieved", checklist_state)
                st.rerun()
                
        # Exclusion Sub-form
        if st.session_state.get("show_ft_exclusion", False):
            st.warning("Select reason for exclusion:")
            with st.form("ft_exclusion_form"):
                reason = st.selectbox("Reason", EXCLUSION_REASONS)
                if st.form_submit_button("Confirm Exclusion", type="primary"):
                    save_decision(conn, study["study_id"], "exclude_full_text", checklist_state, reason=reason)
                    st.session_state.show_ft_exclusion = False
                    st.rerun()
            if st.button("Cancel"):
                st.session_state.show_ft_exclusion = False
                st.rerun()
