import streamlit as st
from can_cchd.mapping.manager import (
    get_mapping_queue,
    get_mappings,
    add_mapping,
    verify_mapping,
    delete_mapping,
    mark_study_mapped,
    get_mapping_progress,
    CATEGORIES
)

def render_phase8(conn):
    st.header("Phase 8: Diagnosis Mapping")
    
    progress = get_mapping_progress(conn)
    total = progress["total"]
    completed = progress["completed"]
    pending = progress["pending"]
    
    if total > 0:
        st.progress(completed / total, text=f"Progress: {completed} / {total} studies mapped ({pending} remaining)")
    else:
        st.warning("No studies available for mapping. Complete Phase 7 first.")
        return
        
    if pending == 0:
        st.success("✅ Diagnosis Mapping complete!")
        if st.button("Complete Phase 8 and Unlock QA Sentinel", type="primary"):
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "8", "completed")
            st.rerun()
        return
        
    queue = get_mapping_queue(conn)
    if not queue:
        st.info("Queue is empty.")
        return
        
    study = queue[0]
    st.subheader(f"Mapping Diagnoses for: {study['title']}")
    
    # 1. Add New Diagnosis Form
    with st.expander("➕ Add New Diagnosis Mapping", expanded=True):
        with st.form("add_mapping_form"):
            col1, col2 = st.columns([2, 1])
            with col1:
                term = st.text_input("Original Term (from the paper)")
            with col2:
                count = st.number_input("Case Count", min_value=1, value=1)
                
            quote = st.text_area("Source Quote")
            
            col3, col4, col5 = st.columns([2, 1, 1])
            with col3:
                category = st.selectbox("Map to CAN-CCHD Category", CATEGORIES)
            with col4:
                is_can = st.checkbox("Is CAN-CCHD?", value=True)
            with col5:
                overlap = st.checkbox("Overlap Possible?")
                
            if st.form_submit_button("Add Mapping"):
                if term.strip():
                    add_mapping(conn, study["study_id"], term, count, quote, category, is_can, overlap)
                    st.rerun()
                else:
                    st.error("Original Term is required.")
                    
    st.divider()
    
    # 2. List Existing Mappings
    st.markdown("### Existing Mappings")
    mappings = get_mappings(conn, study["study_id"])
    
    if not mappings:
        st.info("No diagnoses mapped yet. If the study has 0 secondary actionable diagnoses, you can complete the phase.")
    else:
        for m in mappings:
            card_col1, card_col2 = st.columns([3, 1])
            with card_col1:
                st.markdown(f"**{m['original_term']}** (n={m['case_count']}) ➔ `{m['mapped_category']}`")
                if m['source_quote']:
                    st.caption(f"\"{m['source_quote']}\"")
                st.caption(f"CAN-CCHD: {'Yes' if m['is_can_cchd'] else 'No'} | Overlap Possible: {'Yes' if m['overlap_possible'] else 'No'}")
                
            with card_col2:
                if m['status'] == 'pending':
                    if st.button("✅ Verify", key=f"vm_{m['mapping_id']}", use_container_width=True):
                        verify_mapping(conn, m['mapping_id'])
                        st.rerun()
                else:
                    st.success("Verified")
                    
                if st.button("🗑️ Delete", key=f"dm_{m['mapping_id']}", use_container_width=True):
                    delete_mapping(conn, m['mapping_id'])
                    st.rerun()
            st.divider()
            
    # 3. Complete Study
    pending_mappings = [m for m in mappings if m['status'] == 'pending']
    
    if len(pending_mappings) > 0:
        st.warning(f"You have {len(pending_mappings)} pending mappings. Verify them before completing this study.")
    else:
        if st.button("✅ Mark Study as Fully Mapped", type="primary", use_container_width=True):
            mark_study_mapped(conn, study["study_id"])
            st.success("Study mapped!")
            st.rerun()
