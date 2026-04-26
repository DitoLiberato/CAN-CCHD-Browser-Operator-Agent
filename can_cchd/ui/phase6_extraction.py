import streamlit as st
from can_cchd.extraction.manager import (
    get_extraction_queue, 
    get_extracted_fields, 
    save_field, 
    mark_study_extracted, 
    mock_ai_extract, 
    get_extraction_progress,
    REQUIRED_FIELDS
)

def render_field_input(conn, study_id, field_name, existing_data):
    """Renders the input and evidence expander for a single field."""
    data = existing_data.get(field_name, {})
    
    val = st.text_input(f"{field_name.replace('_', ' ').title()}", value=data.get("value_raw", ""), key=f"val_{study_id}_{field_name}")
    
    with st.expander("Evidence & Source"):
        loc = st.text_input("Page/Location", value=data.get("source_location", ""), key=f"loc_{study_id}_{field_name}")
        quote = st.text_area("Supporting Quote", value=data.get("supporting_quote", ""), key=f"qte_{study_id}_{field_name}", height=68)
        
        # We auto-save when user interacts, but Streamlit rerun logic makes it tricky.
        # For simplicity, we just use a Save button per section or a global save.
        # We will use a global save button at the bottom in this implementation for simplicity.
        # BUT Streamlit loses state on rerun if not careful. We will just save directly on change via on_change callback.
        
    return {"value_raw": val, "source_location": loc, "supporting_quote": quote}

def render_phase6(conn):
    st.header("Phase 6: Data Extraction")
    
    progress = get_extraction_progress(conn)
    total = progress["total"]
    completed = progress["completed"]
    pending = progress["pending"]
    
    if total > 0:
        st.progress(completed / total, text=f"Progress: {completed} / {total} studies extracted ({pending} remaining)")
    else:
        st.warning("No studies available for extraction. Complete Phase 5 first.")
        return
        
    if pending == 0:
        st.success("✅ Data Extraction complete!")
        if st.button("Complete Phase 6 and Unlock Extraction Verification", type="primary"):
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "6", "completed")
            st.rerun()
        return
        
    st.divider()
    
    queue = get_extraction_queue(conn)
    if not queue:
        st.info("Queue is empty.")
        return
        
    study = queue[0]
    st.subheader(f"Extracting: {study['title']}")
    
    col_a, col_b = st.columns([3, 1])
    with col_b:
        if st.button("🤖 Auto-Fill with Mock AI", use_container_width=True):
            mock_ai_extract(conn, study["study_id"])
            st.rerun()
            
    existing_data = get_extracted_fields(conn, study["study_id"])
    
    tab1, tab2, tab3 = st.tabs(["Characteristics", "Denominators", "Outcomes"])
    
    form_data = {}
    
    with tab1:
        for f in REQUIRED_FIELDS["characteristics"]:
            form_data[f] = render_field_input(conn, study["study_id"], f, existing_data)
            
    with tab2:
        for f in REQUIRED_FIELDS["denominators"]:
            form_data[f] = render_field_input(conn, study["study_id"], f, existing_data)
            
    with tab3:
        for f in REQUIRED_FIELDS["outcomes"]:
            form_data[f] = render_field_input(conn, study["study_id"], f, existing_data)
            
    st.divider()
    if st.button("💾 Save & Submit Extraction", type="primary"):
        # Save all fields
        for f_name, f_data in form_data.items():
            if f_data["value_raw"]:  # only save if not empty
                # Try to parse numeric
                num_val = None
                try:
                    num_val = float(f_data["value_raw"])
                except:
                    pass
                save_field(conn, study["study_id"], f_name, f_data["value_raw"], num_val, f_data["source_location"], f_data["supporting_quote"])
                
        mark_study_extracted(conn, study["study_id"])
        st.success("Extraction saved!")
        st.rerun()
