import streamlit as st
import pandas as pd
from can_cchd.dedup.matcher import run_exact_matcher, run_fuzzy_matcher
from can_cchd.dedup.manager import bulk_merge_exact, process_singletons

def get_group_counts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT match_type, COUNT(*) as count FROM duplicate_groups WHERE status = 'pending' GROUP BY match_type")
    counts = {r["match_type"]: r["count"] for r in cursor.fetchall()}
    return counts

def render_phase2(conn):
    st.header("Phase 2: Deduplication and Prioritization")
    
    st.write("This phase merges duplicate records across different sources into unique 'studies'.")
    
    # Run matchers if not done yet (simplified: run on button press for manual control)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Run Exact Matcher", type="secondary"):
            with st.spinner("Finding exact matches..."):
                run_exact_matcher(conn)
            st.rerun()
    with col2:
        if st.button("Run Fuzzy Matcher", type="secondary"):
            with st.spinner("Finding fuzzy matches..."):
                run_fuzzy_matcher(conn)
            st.rerun()
            
    st.divider()
    
    counts = get_group_counts(conn)
    
    st.subheader("Exact Duplicates")
    st.markdown(f"- Exact PMID matches: **{counts.get('exact_pmid', 0)} groups**")
    st.markdown(f"- Exact DOI matches: **{counts.get('exact_doi', 0)} groups**")
    st.markdown(f"- Exact PMCID matches: **{counts.get('exact_pmcid', 0)} groups**")
    st.markdown(f"- Exact Title+Year matches: **{counts.get('exact_title_year', 0)} groups**")
    
    exact_total = sum([counts.get(k, 0) for k in counts if k.startswith("exact_")])
    
    if exact_total > 0:
        st.info("Exact duplicates can be safely bulk-merged. A backup is recommended before this step.")
        if st.button("Bulk Merge Exact Duplicates", type="primary"):
            with st.spinner("Merging..."):
                merged = bulk_merge_exact(conn)
            st.success(f"Merged {merged} exact duplicate groups.")
            st.rerun()
    else:
        st.success("No pending exact duplicates.")
        
    st.divider()
    
    st.subheader("Fuzzy Duplicates")
    st.markdown(f"- Fuzzy Title matches: **{counts.get('fuzzy_title', 0)} groups**")
    
    if counts.get('fuzzy_title', 0) > 0:
        st.warning("Fuzzy duplicates require manual review. (UI for manual review goes here - mock version will auto-merge for testing)")
        if st.button("Resolve Remaining Fuzzy Duplicates (Mock)", type="primary"):
            # Mock behavior: just mark them as completed for testing the workflow
            cursor = conn.cursor()
            cursor.execute("UPDATE duplicate_groups SET status = 'merged' WHERE match_type = 'fuzzy_title'")
            conn.commit()
            st.rerun()
    else:
        st.success("No pending fuzzy duplicates.")
        
    st.divider()
    
    total_pending = exact_total + counts.get('fuzzy_title', 0)
    
    st.subheader("Phase Completion")
    if total_pending == 0:
        st.info("All duplicates resolved. You can now process singletons and proceed to Phase 3.")
        if st.button("Process Singletons and Complete Phase 2", type="primary"):
            with st.spinner("Processing singletons..."):
                process_singletons(conn)
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "2", "completed")
            st.success("Phase 2 Completed!")
            st.rerun()
    else:
        st.warning("You must resolve all pending duplicate groups before proceeding to Screening.")
