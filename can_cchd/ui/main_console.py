import streamlit as st
import os
import sys

# Ensure module can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from can_cchd.db.connection import get_connection, init_db
from can_cchd.workflow.next_action import get_next_action

def render_sidebar():
    """Renders the workflow phases in the sidebar."""
    st.sidebar.title("Workflow Phases")
    
    conn = get_connection()
    try:
        import sqlite3
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT phase_id, phase_order, phase_name, status FROM workflow_phases ORDER BY phase_order ASC")
            phases = cursor.fetchall()
            
            if not phases:
                init_db()
                cursor.execute("SELECT phase_id, phase_order, phase_name, status FROM workflow_phases ORDER BY phase_order ASC")
                phases = cursor.fetchall()
        except sqlite3.OperationalError:
            init_db()
            cursor.execute("SELECT phase_id, phase_order, phase_name, status FROM workflow_phases ORDER BY phase_order ASC")
            phases = cursor.fetchall()
        for phase in phases:
            status = phase["status"]
            name = phase["phase_name"]
            
            icon = "🔒"
            if status == "completed":
                icon = "✅"
            elif status == "completed_with_note":
                icon = "☑️"
            elif status == "skipped_with_justification":
                icon = "⏭️"
            elif status in ["available", "in_progress"]:
                icon = "🟦"
            elif status == "blocked":
                icon = "🚫"
                
            st.sidebar.markdown(f"{icon} **{name}**")
            
    finally:
        conn.close()

def render_main_console():
    """Renders the main workflow console, deciding what to display based on next_action."""
    st.title("Workflow Console")
    
    conn = get_connection()
    try:
        action = get_next_action(conn)
        
        # --- DEV MODE OVERRIDE ---
        st.sidebar.divider()
        st.sidebar.subheader("🛠️ Developer Options")
        dev_override = st.sidebar.checkbox("Enable Dev Mode (Bypass Gating)")
        
        phase_id = action["phase_id"]
        
        if dev_override:
            # Let the user pick any phase
            phases_list = [str(i) for i in range(12)]
            phase_id = st.sidebar.selectbox("Force Active Phase", phases_list, index=int(phase_id) if int(phase_id) < 12 else 0)
            st.warning(f"DEV MODE ACTIVE: Forcing Phase {phase_id}")
        else:
            st.info(action["message"])
        # -------------------------
        
        # Phase Routing
        if phase_id == "0":
            from can_cchd.ui.phase0_protocol import render_phase0
            render_phase0(conn)
        elif phase_id == "1":
            from can_cchd.ui.phase1_search import render_phase1
            render_phase1(conn)
        elif phase_id == "2":
            from can_cchd.ui.phase2_dedup import render_phase2
            render_phase2(conn)
        elif phase_id == "3":
            from can_cchd.ui.phase3_screening import render_phase3
            render_phase3(conn)
        elif phase_id == "4":
            from can_cchd.ui.phase4_retrieval import render_phase4
            render_phase4(conn)
        elif phase_id == "5":
            from can_cchd.ui.phase5_eligibility import render_phase5
            render_phase5(conn)
        elif phase_id == "6":
            from can_cchd.ui.phase6_extraction import render_phase6
            render_phase6(conn)
        elif phase_id == "7":
            from can_cchd.ui.phase7_verification import render_phase7
            render_phase7(conn)
        elif phase_id == "8":
            from can_cchd.ui.phase8_mapping import render_phase8
            render_phase8(conn)
        elif phase_id == "9":
            from can_cchd.ui.phase9_qa import render_phase9
            render_phase9(conn)
        else:
            st.warning(f"UI for Phase {phase_id} is not yet implemented.")
            if st.button(f"Mock Complete Phase {phase_id}"):
                from can_cchd.workflow.next_action import update_phase_status
                update_phase_status(conn, phase_id, "completed")
                st.rerun()
                
    finally:
        conn.close()
