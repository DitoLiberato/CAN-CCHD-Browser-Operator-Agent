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
    
    # 1. Matching Controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔍 Run Exact Matcher", use_container_width=True):
            with st.spinner("Finding exact matches..."):
                run_exact_matcher(conn)
            st.rerun()
    with col2:
        if st.button("🧠 Run Fuzzy Matcher (AI-ready)", use_container_width=True):
            with st.spinner("Finding fuzzy matches..."):
                run_fuzzy_matcher(conn)
            st.rerun()
            
    st.divider()
    
    counts = get_group_counts(conn)
    
    # 2. Exact Duplicates Audit & Bulk Action
    st.subheader("📋 Exact Duplicates Audit")
    exact_total = sum([counts.get(k, 0) for k in counts if k.startswith("exact_")])
    
    if exact_total > 0:
        with st.expander(f"View {exact_total} pending exact groups"):
            cursor = conn.cursor()
            cursor.execute("""
                SELECT g.group_id, g.match_type, r.title, r.authors, r.year, r.source_database, r.pmid, r.doi
                FROM duplicate_groups g
                JOIN duplicate_group_members m ON g.group_id = m.group_id
                JOIN records r ON m.record_id = r.record_id
                WHERE g.status = 'pending' AND g.match_type LIKE 'exact_%'
                ORDER BY g.group_id
            """)
            exact_data = cursor.fetchall()
            df_exact = pd.DataFrame([dict(r) for r in exact_data])
            st.dataframe(df_exact, use_container_width=True)
            
        st.info("These groups have 100% matches on unique identifiers (PMID/DOI/PMCID).")
        if st.button("🚀 Bulk Merge All Exact Matches", type="primary", use_container_width=True):
            with st.spinner("Merging..."):
                merged = bulk_merge_exact(conn)
            st.success(f"Successfully merged {merged} exact groups!")
            st.rerun()
    else:
        st.success("No pending exact duplicates found.")
        
    st.divider()
    
    # 3. Fuzzy Duplicates Manual Review Board
    st.subheader("🧐 Fuzzy Duplicates Review Board")
    fuzzy_count = counts.get('fuzzy_title', 0)
    
    if fuzzy_count > 0:
        st.warning(f"There are {fuzzy_count} groups requiring manual audit.")
        
        # Fetch the first pending fuzzy group
        cursor = conn.cursor()
        cursor.execute("SELECT group_id, match_key FROM duplicate_groups WHERE status = 'pending' AND match_type = 'fuzzy_title' LIMIT 1")
        group = cursor.fetchone()
        
        if group:
            gid = group["group_id"]
            cursor.execute("""
                SELECT r.record_id, r.title, r.authors, r.year, r.source_database, r.pmid, r.doi, r.journal
                FROM duplicate_group_members m
                JOIN records r ON m.record_id = r.record_id
                WHERE m.group_id = ?
            """, (gid,))
            members = cursor.fetchall()
            
            st.info(f"Reviewing Group: **{group['match_key']}**")
            
            # Display comparison cards
            for i, m in enumerate(members):
                with st.container():
                    st.markdown(f"**Record {i+1} from {m['source_database']}**")
                    st.write(f"**Title:** {m['title']}")
                    st.write(f"**Authors:** {m['authors']}")
                    st.caption(f"Year: {m['year']} | Journal: {m['journal']} | DOI: {m['doi']}")
                    st.divider()
            
            # Decision Buttons
            from can_cchd.dedup.manager import merge_group_manual, reject_group_manual
            
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                if st.button("✅ Merge into Single Study", use_container_width=True, type="primary"):
                    merge_group_manual(conn, gid)
                    st.toast("Merged!")
                    st.rerun()
            with btn_col2:
                if st.button("❌ Keep as Separate Studies", use_container_width=True):
                    reject_group_manual(conn, gid)
                    st.toast("Marked as unique!")
                    st.rerun()
    else:
        st.success("All fuzzy matches have been reviewed.")
        
    st.divider()
    
    # 4. Phase Completion
    st.subheader("🏁 Finalize Phase 2")
    total_pending = exact_total + fuzzy_count
    
    if total_pending == 0:
        st.success("Audit complete! You can now finalize the study list.")
        if st.button("✨ Process Singletons and Complete Phase 2", type="primary", use_container_width=True):
            with st.spinner("Finalizing unique studies..."):
                process_singletons(conn)
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "2", "completed")
            st.success("Phase 2 Completed! Proceeding to Screening.")
            st.rerun()
    else:
        st.warning(f"Please resolve the remaining {total_pending} groups before proceeding.")
