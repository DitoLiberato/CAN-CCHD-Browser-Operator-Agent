import streamlit as st
import os
from can_cchd.retrieval.manager import get_retrieval_queue, save_retrieval_status, get_retrieval_progress

def render_phase4(conn):
    st.header("Phase 4: Full-Text Retrieval")
    
    progress = get_retrieval_progress(conn)
    total = progress["total"]
    completed = progress["completed"]
    pending = progress["pending"]
    
    if total > 0:
        st.progress(completed / total, text=f"Progress: {completed} / {total} PDFs retrieved ({pending} remaining)")
    else:
        st.warning("No studies require full-text retrieval. Did you include any studies in Phase 3?")
        return
        
    if pending == 0:
        st.success("✅ Full-Text Retrieval complete!")
        if st.button("Complete Phase 4 and Unlock Full-Text Eligibility", type="primary"):
            from can_cchd.workflow.next_action import update_phase_status
            update_phase_status(conn, "4", "completed")
            st.rerun()
        return
        
    st.divider()
    
    queue = get_retrieval_queue(conn)
    
    st.subheader("Pending Retrievals")
    st.write("Expand each study to upload the PDF or mark it as unobtainable.")
    
    for study in queue:
        with st.expander(f"{study['title']} ({study['year']})"):
            st.markdown(f"**Authors:** {study['first_author']} et al. | **Journal:** {study['journal']}")
            
            links = []
            if study['doi']:
                links.append(f"[DOI: {study['doi']}](https://doi.org/{study['doi']})")
            if study['pmid']:
                links.append(f"[PMID: {study['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{study['pmid']})")
            
            if links:
                st.markdown(" | ".join(links))
                
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Upload PDF")
                uploaded_file = st.file_uploader("Attach local PDF", type="pdf", key=f"up_{study['study_id']}")
                if uploaded_file is not None:
                    if st.button("Save PDF", key=f"save_{study['study_id']}", type="primary"):
                        # Save file to data/fulltexts
                        os.makedirs("data/fulltexts", exist_ok=True)
                        file_path = os.path.join("data", "fulltexts", f"{study['study_id']}.pdf")
                        
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                            
                        save_retrieval_status(conn, study["study_id"], "manual_pdf_attached", file_path=file_path)
                        st.success("Saved!")
                        st.rerun()
            
            with col2:
                st.markdown("#### Unobtainable")
                note = st.text_input("Reason for inability to retrieve", key=f"note_{study['study_id']}")
                if st.button("Mark as Not Obtainable", key=f"unobtain_{study['study_id']}"):
                    if not note:
                        st.error("You must provide a note.")
                    else:
                        save_retrieval_status(conn, study["study_id"], "not_obtainable_with_note", note=note)
                        st.rerun()
