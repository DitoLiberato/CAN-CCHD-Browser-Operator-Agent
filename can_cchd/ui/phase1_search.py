import streamlit as st
import pandas as pd
from can_cchd.browser_agent.agent import BrowserAgent

def get_sources(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT source_id, source_name, priority_order, access_mode, required_status, 
               status, records_imported 
        FROM research_sources 
        ORDER BY priority_order ASC
    """)
    return cursor.fetchall()

def get_queries_for_source(conn, source_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT query_id, query_label, query_string, status, result_count, records_imported
        FROM research_queries 
        WHERE source_id = ?
        ORDER BY query_label ASC
    """, (source_id,))
    return cursor.fetchall()

def get_agent_logs(conn, limit=10):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp, action_type, message, query_label
        FROM agent_action_log 
        ORDER BY timestamp DESC 
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()

def get_latest_records(conn, limit=50):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.title, r.authors, r.year, r.pmid, s.source_name, q.query_label
        FROM records r
        JOIN research_sources s ON r.source_id = s.source_id
        LEFT JOIN research_queries q ON r.query_id = q.query_id
        ORDER BY r.imported_at DESC
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()

def render_phase1(conn):
    st.header("Phase 1: Multi-Query Search Collection")
    
    st.write("The agent will execute multiple search strings per platform and accumulate the results in the evidence database.")
    
    sources = get_sources(conn)
    if not sources:
        st.warning("No sources found. Please run the protocol initialization first.")
        return
        
    st.subheader("📡 Evidence Sources")
    df = pd.DataFrame([dict(s) for s in sources])
    st.dataframe(df[["source_name", "access_mode", "status", "records_imported"]], use_container_width=True)
    
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🤖 Agent Control Center")
        
        # 1. Select Source
        source_names = [s["source_name"] for s in sources]
        selected_source_name = st.selectbox("1. Select Platform", source_names)
        selected_source = next(s for s in sources if s["source_name"] == selected_source_name)
        
        # 2. Select Query
        queries = get_queries_for_source(conn, selected_source["source_id"])
        if not queries:
            st.info("No predefined queries for this source.")
            query_options = []
        else:
            query_options = [f"{q['query_label']} ({q['status']})" for q in queries]
            
        selected_query_str = st.selectbox("2. Select Search Query", query_options)
        
        if selected_query_str:
            selected_label = selected_query_str.split(" (")[0]
            selected_query = next(q for q in queries if q["query_label"] == selected_label)
            
            st.code(selected_query["query_string"], language="text")
            
            run_col, setup_col = st.columns(2)
            with run_col:
                if st.button("🚀 Run Query Agent", type="primary", use_container_width=True):
                    agent = BrowserAgent(conn)
                    with st.status(f"Executing '{selected_label}' on {selected_source_name}...", expanded=True) as status:
                        agent.run_search(selected_source["source_id"], selected_source_name, selected_query["query_id"])
                        status.update(label=f"Query '{selected_label}' Completed!", state="complete", expanded=False)
                    st.rerun()
                    
                if selected_query["status"] == "completed":
                    st.warning(f"This query already extracted {selected_query['records_imported']} records.")
                    if st.button("🗑️ Reset & Re-Run Query", type="secondary", use_container_width=True):
                        cursor = conn.cursor()
                        # Delete the records associated specifically with this query to prevent ghosts
                        cursor.execute("DELETE FROM records WHERE query_id = ?", (selected_query["query_id"],))
                        cursor.execute("UPDATE research_queries SET status = 'pending', result_count = 0, records_imported = 0 WHERE query_id = ?", (selected_query["query_id"],))
                        conn.commit()
                        st.rerun()
            
            with setup_col:
                if st.button("🔑 Assist API/Login Setup", use_container_width=True):
                    agent = BrowserAgent(conn)
                    st.info(f"Opening setup/login page for {selected_source_name}...")
                    agent.assist_setup_api(selected_source_name)
                    
            if selected_source["access_mode"] in ["Supervised-login", "Browser-supervised"]:
                st.info("⚠️ This source blocks automated bots. Run the search manually and upload the exported `.ris` file below.")
                uploaded_file = st.file_uploader("Upload RIS Export", type=["ris"])
                if uploaded_file is not None:
                    if st.button("📥 Import RIS File"):
                        from can_cchd.utils.ris_parser import parse_ris, save_manual_records
                        content = uploaded_file.getvalue().decode("utf-8")
                        parsed = parse_ris(content)
                        if parsed:
                            count = save_manual_records(conn, parsed, selected_source["source_id"], selected_query["query_id"], selected_source_name)
                            st.success(f"Successfully imported {count} new records from RIS file!")
                            agent = BrowserAgent(conn)
                            agent.log_action("extraction", f"Manually imported {count} records via RIS upload", result_count=count, query_label=selected_label)
                        else:
                            st.error("No valid records found in the RIS file.")
        
        st.divider()
        st.write("📋 **Live Agent Logs**")
        logs = get_agent_logs(conn)
        for log in logs:
            q_info = f" | {log['query_label']}" if log['query_label'] else ""
            st.caption(f"[{log['timestamp'][11:19]}] {log['action_type'].upper()}{q_info}: {log['message']}")

    with col2:
        st.subheader("📊 Statistics")
        st.write("**Records per Query**")
        all_queries = []
        for s in sources:
            all_queries.extend([dict(q) for q in get_queries_for_source(conn, s["source_id"])])
        
        if all_queries:
            qdf = pd.DataFrame(all_queries)
            # Add source name for context
            st.dataframe(qdf[qdf["records_imported"] > 0][["query_label", "records_imported"]], use_container_width=True)
        else:
            st.info("Run a query to see statistics.")

        st.divider()
        st.subheader("🏁 Phase Control")
        pending_queries = [q for q in all_queries if q["status"] == "pending"]
        
        if not pending_queries:
            st.success("All predefined queries have been executed!")
            if st.button("Proceed to Phase 2: Deduplication", type="primary", use_container_width=True):
                from can_cchd.workflow.next_action import update_phase_status
                update_phase_status(conn, "1", "completed")
                st.rerun()
        else:
            st.warning(f"{len(pending_queries)} queries still pending.")
            if st.button("Skip Remaining and Proceed"):
                from can_cchd.workflow.next_action import update_phase_status
                update_phase_status(conn, "1", "completed")
                st.rerun()

    st.divider()
    st.subheader("🔍 Review Collected Records")
    
    # Get all records instead of limit 50
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.title, r.authors, r.year, r.pmid, s.source_name, q.query_label, r.imported_at
        FROM records r
        JOIN research_sources s ON r.source_id = s.source_id
        LEFT JOIN research_queries q ON r.query_id = q.query_id
        ORDER BY r.imported_at DESC
    """)
    all_records = cursor.fetchall()
    
    if all_records:
        df_records = pd.DataFrame([dict(r) for r in all_records])
        st.write(f"Total Records in Database: **{len(df_records)}**")
        
        # Download Button
        csv = df_records.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Full Dataset as CSV",
            data=csv,
            file_name='can_cchd_raw_records.csv',
            mime='text/csv',
        )
        
        # Interactive DataFrame (handles thousands of rows efficiently)
        st.dataframe(df_records, use_container_width=True, height=400)
    else:
        st.info("No records in database.")
