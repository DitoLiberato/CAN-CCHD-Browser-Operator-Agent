import streamlit as st
from can_cchd.qa.sentinel import run_all_checks, get_open_findings, override_finding

def render_phase9(conn):
    st.header("Phase 9: QA Sentinel")
    st.write("The automated Sentinel will scan the entire evidence database to ensure compliance with the research protocol.")
    
    if st.button("🔍 Run Full QA Scan", type="primary", use_container_width=True):
        with st.spinner("Running protocol checks..."):
            run_all_checks(conn)
            st.session_state["qa_run"] = True
            st.rerun()
            
    if not st.session_state.get("qa_run", False):
        st.info("Click the button above to start the scan.")
        return
        
    findings = get_open_findings(conn)
    
    if len(findings) == 0:
        st.success("🟢 **ALL CHECKS PASSED!** The database is perfectly compliant.")
        st.balloons()
        
        st.divider()
        st.markdown("### Evidence Generation Complete")
        st.write("You have successfully constructed the CAN-CCHD evidence database. You may now proceed to statistical analysis and manuscript writing.")
        if st.button("Complete Workflow", type="primary"):
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "9", "completed")
            st.success("Workflow completed!")
            # Would typically redirect or show a final screen here.
    else:
        st.error(f"🔴 **QA FAILED!** Found {len(findings)} blocking issues.")
        st.warning("You must resolve these issues or provide a written override note to proceed to Analysis.")
        
        for f in findings:
            with st.expander(f"{f['severity'].upper()} - {f['rule_name']} (Study: {f.get('title', f['study_id'])})", expanded=True):
                st.write(f"**Issue:** {f['description']}")
                
                with st.form(f"form_override_{f['finding_id']}"):
                    note = st.text_input("Override Justification Note")
                    if st.form_submit_button("Override & Accept Risk"):
                        if len(note.strip()) < 5:
                            st.error("A detailed justification is required.")
                        else:
                            override_finding(conn, f['finding_id'], note)
                            st.rerun()
