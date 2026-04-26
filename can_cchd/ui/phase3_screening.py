import streamlit as st
from can_cchd.screening.manager import get_next_candidate, save_decision, get_screening_progress

EXCLUSION_REASONS = [
    "not_newborn_or_neonatal",
    "not_human",
    "not_pulse_oximetry",
    "not_cchd_screening",
    "no_failed_or_positive_screen_data_clearly",
    "case_report",
    "editorial_commentary_letter_no_original_data",
    "clearly_unrelated",
    "duplicate",
    "other"
]

def render_phase3(conn):
    st.header("Phase 3: Title/Abstract Screening")
    
    progress = get_screening_progress(conn)
    total = progress["total"]
    completed = progress["completed"]
    pending = progress["pending"]
    
    if total > 0:
        st.progress(completed / total, text=f"Progress: {completed} / {total} studies screened ({pending} remaining)")
    else:
        st.warning("No studies available for screening. Did you complete Phase 2?")
        return
        
    if pending == 0:
        st.success("✅ Screening complete! All studies have been reviewed.")
        if st.button("Complete Phase 3 and Unlock Full-Text Retrieval", type="primary"):
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "3", "completed")
            st.rerun()
        return
        
    st.divider()
    
    # Get current study to screen
    study = get_next_candidate(conn)
    if not study:
        st.error("Error retrieving next candidate.")
        return
        
    # Screening Card UI
    st.subheader(study.get("title", "No Title"))
    st.markdown(f"**Authors:** {study.get('first_author', 'Unknown')} et al.  |  **Year:** {study.get('year', 'Unknown')}  |  **Journal:** {study.get('journal', 'Unknown')}")
    if study.get("pmid"):
        st.markdown(f"**PMID:** [{study['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{study['pmid']})")
        
    st.markdown("### Abstract")
    st.info(study.get("abstract", "No abstract available."))
    
    st.divider()
    
    # Action Buttons
    st.markdown("### Decision")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("✅ Include", use_container_width=True):
            save_decision(conn, study["study_id"], "include")
            st.rerun()
            
    with col2:
        if st.button("🤔 Maybe", use_container_width=True):
            save_decision(conn, study["study_id"], "maybe")
            st.rerun()
            
    with col3:
        if st.button("⛔ Exclude", use_container_width=True):
            st.session_state.show_exclusion_form = True
            
    with col4:
        with st.popover("More Options", use_container_width=True):
            if st.button("Citation Mining Only"):
                save_decision(conn, study["study_id"], "citation_mining_only")
                st.rerun()
            if st.button("Separate Analysis"):
                save_decision(conn, study["study_id"], "separate_analysis")
                st.rerun()
                
    # Exclusion Sub-form
    if st.session_state.get("show_exclusion_form", False):
        st.warning("Please select an exclusion reason:")
        with st.form("exclusion_form"):
            reason = st.selectbox("Reason", EXCLUSION_REASONS)
            if st.form_submit_button("Confirm Exclusion", type="primary"):
                save_decision(conn, study["study_id"], "exclude", reason=reason)
                st.session_state.show_exclusion_form = False
                st.rerun()
        if st.button("Cancel"):
            st.session_state.show_exclusion_form = False
            st.rerun()
