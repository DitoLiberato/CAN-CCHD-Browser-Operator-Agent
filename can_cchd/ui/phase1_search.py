import streamlit as st
import pandas as pd
from can_cchd.browser_agent.agent import BrowserAgent

def get_sources(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT source_id, source_name, priority_order, access_mode, required_status, 
               status, records_found, records_imported 
        FROM research_sources 
        ORDER BY priority_order ASC
    """)
    return cursor.fetchall()

def render_phase1(conn):
    st.header("Phase 1: Search Collection")
    
    st.write("The agent will perform or guide search tasks based on the approved protocol.")
    
    sources = get_sources(conn)
    if not sources:
        st.warning("No sources found. Protocol might not be initialized correctly.")
        return
        
    df = pd.DataFrame([dict(s) for s in sources])
    st.dataframe(df[["source_name", "access_mode", "required_status", "status", "records_found", "records_imported"]], use_container_width=True)
    
    st.subheader("Source Control")
    
    col1, col2 = st.columns(2)
    
    # Simple form to trigger a mock agent run
    with col1:
        st.write("Run Agent on a specific source:")
        pending_sources = [s for s in sources if s["status"] not in ["completed", "skipped_with_justification"]]
        
        if pending_sources:
            selected_source_name = st.selectbox("Select Source", [s["source_name"] for s in pending_sources])
            selected_source = next(s for s in pending_sources if s["source_name"] == selected_source_name)
            
            if st.button("Run Agent", type="primary"):
                agent = BrowserAgent(conn)
                with st.spinner(f"Running agent on {selected_source_name}..."):
                    agent.run_source(selected_source["source_id"], selected_source["source_name"])
                st.success(f"Agent completed {selected_source_name}.")
                st.rerun()
        else:
            st.success("All sources are completed!")
            
    with col2:
        st.write("Complete Phase 1")
        if not pending_sources:
            if st.button("Proceed to Deduplication"):
                from can_cchd.workflow.next_action import update_phase_status
                update_phase_status(conn, "1", "completed")
                st.rerun()
        else:
            st.info("You must complete all required sources to proceed.")
