import streamlit as st
from can_cchd.verification.manager import (
    get_verification_queue,
    get_fields_for_verification,
    verify_field,
    calculate_denominator_suggestion,
    apply_calculated_denominator,
    mark_study_verified,
    get_verification_progress
)

def render_field_row(conn, field):
    """Renders a single row for verification."""
    st.markdown(f"#### {field['field_name'].replace('_', ' ').title()}")
    st.markdown(f"**Extracted Value:** `{field['value_raw']}`")
    
    if field['source_location'] or field['supporting_quote']:
        st.info(f"📍 **{field['source_location']}**: \"{field['supporting_quote']}\"")
        
    status_colors = {
        "verified": "🟢 Verified",
        "corrected": "🔵 Corrected",
        "rejected": "🔴 Rejected",
        "needs_second_look": "🟡 Needs Second Look",
        "unavailable_with_note": "⚪ Unavailable",
        "ai_suggested": "🟣 Pending (AI)",
        "human_extracted": "🟣 Pending (Human)"
    }
    
    st.caption(f"Status: **{status_colors.get(field['status'], field['status'])}**")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("✅ Verify", key=f"v_{field['field_id']}", use_container_width=True):
            verify_field(conn, field['field_id'], "verified")
            st.rerun()
    with col2:
        if st.button("✏️ Correct", key=f"c_{field['field_id']}", use_container_width=True):
            st.session_state[f"show_correct_{field['field_id']}"] = True
    with col3:
        if st.button("❌ Reject", key=f"r_{field['field_id']}", use_container_width=True):
            verify_field(conn, field['field_id'], "rejected")
            st.rerun()
    with col4:
        if st.button("⚠️ Second Look", key=f"s_{field['field_id']}", use_container_width=True):
            verify_field(conn, field['field_id'], "needs_second_look")
            st.rerun()
            
    if st.session_state.get(f"show_correct_{field['field_id']}", False):
        with st.form(key=f"form_{field['field_id']}"):
            new_val = st.text_input("New Value", value=field['value_raw'])
            if st.form_submit_button("Save Correction"):
                num_val = None
                try:
                    num_val = float(new_val)
                except:
                    pass
                verify_field(conn, field['field_id'], "corrected", corrected_value_raw=new_val, corrected_value_numeric=num_val)
                st.session_state[f"show_correct_{field['field_id']}"] = False
                st.rerun()
                
    st.divider()

def render_phase7(conn):
    st.header("Phase 7: Extraction Verification")
    
    progress = get_verification_progress(conn)
    total = progress["total"]
    completed = progress["completed"]
    pending = progress["pending"]
    
    if total > 0:
        st.progress(completed / total, text=f"Progress: {completed} / {total} studies verified ({pending} remaining)")
    else:
        st.warning("No studies available for verification. Complete Phase 6 first.")
        return
        
    if pending == 0:
        st.success("✅ Extraction Verification complete!")
        if st.button("Complete Phase 7 and Unlock Diagnosis Mapping", type="primary"):
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "7", "completed")
            st.rerun()
        return
        
    queue = get_verification_queue(conn)
    if not queue:
        st.info("Queue is empty.")
        return
        
    study = queue[0]
    st.subheader(f"Verifying: {study['title']}")
    
    fields = get_fields_for_verification(conn, study["study_id"])
    
    # Render fields
    for field in fields:
        render_field_row(conn, field)
        
    # Check if calculation is possible
    calc_val = calculate_denominator_suggestion(conn, study["study_id"])
    if calc_val is not None:
        # Check if number_cchd_negative_failed already verified/corrected
        cchd_neg_field = next((f for f in fields if f["field_name"] == "number_cchd_negative_failed"), None)
        
        if cchd_neg_field and cchd_neg_field["status"] in ["ai_suggested", "human_extracted"]:
            st.success(f"🧮 **System Calculation:** Verified Failed Screens minus Verified CCHD = **{calc_val}**.")
            st.info("Do you want to apply this calculation to the `number_cchd_negative_failed` field?")
            if st.button("Apply Calculation & Verify", type="primary"):
                apply_calculated_denominator(conn, study["study_id"], calc_val)
                st.rerun()
    
    st.markdown("### Finish Verification")
    
    # Check if any fields are still pending (ai_suggested or human_extracted)
    pending_fields = [f for f in fields if f["status"] in ["ai_suggested", "human_extracted"]]
    
    if len(pending_fields) > 0:
        st.warning(f"{len(pending_fields)} fields still need review before you can complete this study.")
    else:
        if st.button("✅ Mark Study as Fully Verified", type="primary", use_container_width=True):
            mark_study_verified(conn, study["study_id"])
            st.success("Study verified!")
            st.rerun()
