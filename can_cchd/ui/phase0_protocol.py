import streamlit as st
from can_cchd.protocol.manager import get_current_protocol, initialize_default_protocol, approve_protocol, update_protocol

def render_phase0(conn):
    st.header("Phase 0: Research Plan and Protocol")
    
    protocol = get_current_protocol(conn)
    if "research_plan_id" not in protocol:
        # First run, initialize
        protocol = initialize_default_protocol(conn)
        
    is_draft = protocol.get("status") != "approved"
    
    if is_draft:
        edit_mode = st.toggle("Edit Protocol", value=False)
    else:
        edit_mode = False
        st.success("✅ Protocol is approved and locked.")
        
    if edit_mode:
        with st.form("edit_protocol_form"):
            st.subheader("Edit Research Protocol")
            
            new_title = st.text_input("Title", value=protocol.get("title", ""))
            new_rq = st.text_area("Review Question", value=protocol.get("review_question", ""))
            
            col1, col2 = st.columns(2)
            with col1:
                new_denom = st.text_input("Primary Denominator", value=protocol.get("primary_denominator", ""))
                new_outcome = st.text_input("Primary Outcome", value=protocol.get("primary_outcome", ""))
                new_policy = st.text_area("Case Report Policy", value=protocol.get("case_report_policy", ""))
            
            with col2:
                sec_outcomes_str = "\n".join(protocol.get("secondary_outcomes", []))
                new_sec_outcomes = st.text_area("Secondary Outcomes (one per line)", value=sec_outcomes_str, height=150)
                
            criteria_str = "\n".join(protocol.get("inclusion_criteria", []))
            new_criteria = st.text_area("Inclusion Criteria (one per line)", value=criteria_str, height=150)
            
            submit = st.form_submit_button("Save Changes", type="primary")
            if submit:
                data = {
                    "title": new_title,
                    "review_question": new_rq,
                    "primary_denominator": new_denom,
                    "primary_outcome": new_outcome,
                    "case_report_policy": new_policy,
                    "secondary_outcomes": [o.strip() for o in new_sec_outcomes.split("\n") if o.strip()],
                    "inclusion_criteria": [c.strip() for c in new_criteria.split("\n") if c.strip()]
                }
                update_protocol(conn, protocol["research_plan_id"], data)
                st.success("Protocol updated successfully!")
                st.rerun()
    else:
        st.subheader(protocol.get("title", "No Title"))
        
        st.markdown("**Review Question:**")
        st.info(protocol.get("review_question", ""))
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Primary Denominator:**")
            st.write(protocol.get("primary_denominator", ""))
            
            st.markdown("**Primary Outcome:**")
            st.write(protocol.get("primary_outcome", ""))
            
            st.markdown("**Case Report Policy:**")
            st.write(protocol.get("case_report_policy", ""))
            
        with col2:
            st.markdown("**Secondary Outcomes:**")
            for outcome in protocol.get("secondary_outcomes", []):
                st.markdown(f"- {outcome}")
                
        st.markdown("**Inclusion Criteria:**")
        for criterion in protocol.get("inclusion_criteria", []):
            st.markdown(f"1. {criterion}")
            
        st.divider()
        
        if is_draft:
            st.warning("Protocol is currently in draft. You must approve it to unlock Phase 1.")
            if st.button("Approve Protocol", type="primary"):
                approve_protocol(conn, protocol["research_plan_id"])
                st.rerun()
