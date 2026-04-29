import streamlit as st
import pandas as pd
from can_cchd.dedup.matcher import run_exact_matcher, run_fuzzy_matcher
from can_cchd.dedup.manager import bulk_merge_exact, process_singletons

def get_group_counts(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT match_type, COUNT(*) as count
        FROM dedup_groups
        WHERE status IN ('pending', 'auto_merge_ready')
        GROUP BY match_type
    """)
    counts = {r["match_type"]: r["count"] for r in cursor.fetchall()}
    return counts

def render_phase2(conn):
    st.header("Phase 2: Deduplication and Prioritization")
    st.write("This phase merges duplicate normalized records into unique studies while preserving source/query provenance.")
    
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
                SELECT g.dedup_group_id, g.match_type, g.status, nr.title, nr.authors_raw, nr.year,
                       nr.source_database, nr.pmid, nr.doi, g.representative_record_id
                FROM dedup_groups g
                JOIN dedup_group_members m ON g.dedup_group_id = m.dedup_group_id
                JOIN normalized_records nr ON m.record_id = nr.record_id
                WHERE g.status IN ('pending', 'auto_merge_ready') AND g.match_type LIKE 'exact_%'
                ORDER BY g.dedup_group_id
            """)
            exact_data = cursor.fetchall()
            df_exact = pd.DataFrame([dict(r) for r in exact_data])
            st.dataframe(df_exact, use_container_width=True)

        st.info("This will not delete normalized records. It will create unique studies and link all duplicate records to them, preserving source/query provenance.")
        confirm_merge = st.checkbox(
            "I understand that exact duplicate groups will be merged into unique studies while preserving all source records."
        )
        if st.button("🚀 Merge selected exact groups", type="primary", use_container_width=True, disabled=not confirm_merge):
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
        cursor.execute("SELECT dedup_group_id, match_key FROM dedup_groups WHERE status = 'pending' AND match_type = 'fuzzy_title' LIMIT 1")
        group = cursor.fetchone()
        
        if group:
            gid = group["dedup_group_id"]
            cursor.execute("""
                SELECT nr.record_id, nr.title, nr.authors_raw, nr.year, nr.source_database, nr.pmid, nr.doi, nr.journal, g.confidence
                FROM dedup_group_members m
                JOIN normalized_records nr ON m.record_id = nr.record_id
                JOIN dedup_groups g ON g.dedup_group_id = m.dedup_group_id
                WHERE m.dedup_group_id = ?
            """, (gid,))
            members = cursor.fetchall()
            
            st.info(f"Reviewing Group: **{group['match_key']}**")
            
            # Display comparison cards
            for i, m in enumerate(members):
                with st.container():
                    st.markdown(f"**Record {i+1} from {m['source_database']}**")
                    st.write(f"**Title:** {m['title']}")
                    st.write(f"**Authors:** {m['authors_raw']}")
                    st.caption(f"Year: {m['year']} | Journal: {m['journal']} | DOI: {m['doi']} | Score: {m['confidence']:.2f}")
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
