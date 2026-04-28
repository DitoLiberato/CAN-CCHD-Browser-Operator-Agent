"""
Phase 1 — Search Collection UI (Robust Reform version).

4 tabs:
  1. 🎯 Search Collection  — source/query selector, agent runner, live logs
  2. 📊 Collection Dashboard — per-source stats, completeness distribution
  3. 🔬 Enrichment Queue   — table of records needing enrichment, bulk enrich
  4. 🔒 QA Gate            — run QA checks, show results, unlock Phase 2
"""
import json
import streamlit as st
import pandas as pd

from can_cchd.collection import get_adapter
from can_cchd.collection.models import QuerySpec
from can_cchd.collection.adapters.ris_adapter import RISAdapter


# ─── helpers ───────────────────────────────────────────────

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
        SELECT query_id, query_label, query_role, query_string, status, result_count, records_imported
        FROM research_queries
        WHERE source_id = ?
        ORDER BY query_label ASC
    """, (source_id,))
    return cursor.fetchall()


def get_agent_logs(conn, limit=15):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp, action_type, message, query_label
        FROM agent_action_log
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()


def get_collection_stats(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            source_database,
            count(*) as harvested,
            sum(CASE WHEN pmid IS NOT NULL AND pmid != '' THEN 1 ELSE 0 END) as with_pmid,
            sum(CASE WHEN doi IS NOT NULL AND doi != '' THEN 1 ELSE 0 END) as with_doi,
            sum(CASE WHEN abstract IS NOT NULL AND abstract != '' THEN 1 ELSE 0 END) as with_abstract,
            sum(CASE WHEN year >= strftime('%Y', 'now') OR year IS NULL THEN 1 ELSE 0 END) as suspicious_year,
            sum(CASE WHEN enrichment_status = 'enriched' THEN 1 ELSE 0 END) as enriched,
            sum(CASE WHEN enrichment_status = 'enrichment_attempted' THEN 1 ELSE 0 END) as attempted,
            avg(metadata_completeness_score) as avg_score
        FROM normalized_records
        GROUP BY source_database
        ORDER BY harvested DESC
    """)
    return cursor.fetchall()


def get_total_normalized(conn):
    c = conn.cursor()
    c.execute("SELECT count(*) as c FROM normalized_records")
    return c.fetchone()["c"]


def get_enrichment_queue(conn, limit=200):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT record_id, source_database, title, pmid, doi, abstract_status,
               enrichment_status, metadata_completeness_score
        FROM normalized_records
        WHERE enrichment_status IN ('pending', 'needs_enrichment')
          AND (abstract IS NULL OR abstract = '')
        ORDER BY metadata_completeness_score ASC
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()


# ─── Main render ───────────────────────────────────────────

def render_phase1(conn):
    st.header("Phase 1: Robust Search Collection")
    st.caption("Collects complete, auditable metadata records before any deduplication.")

    total = get_total_normalized(conn)
    sources = get_sources(conn)

    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Search Collection",
        "📊 Collection Dashboard",
        "🔬 Enrichment Queue",
        "🔒 QA Gate"
    ])

    # ────────────────────────────────────────────────────────
    # TAB 1 — Search Collection
    # ────────────────────────────────────────────────────────
    with tab1:
        if not sources:
            st.warning("No sources found. Please run protocol initialization first.")
            return

        col_ctrl, col_stats = st.columns([2, 1])

        with col_ctrl:
            st.subheader("🤖 Agent Control Center")

            source_names = [s["source_name"] for s in sources]
            selected_source_name = st.selectbox("1. Select Platform", source_names, key="src_sel")
            selected_source = dict(next(s for s in sources if s["source_name"] == selected_source_name))

            queries = get_queries_for_source(conn, selected_source["source_id"])
            if not queries:
                st.info("No predefined queries for this source.")
            else:
                query_options = [f"{q['query_label']} ({q['status']})" for q in queries]
                selected_query_str = st.selectbox("2. Select Search Query", query_options, key="qry_sel")
                selected_label = selected_query_str.split(" (")[0]
                selected_query = dict(next(q for q in queries if q["query_label"] == selected_label))

                st.code(selected_query["query_string"], language="text")

                run_col, setup_col = st.columns(2)

                with run_col:
                    adapter = get_adapter(selected_source_name, conn)

                    if adapter:
                        if st.button("🚀 Run Query (New Pipeline)", type="primary", use_container_width=True):
                            spec = QuerySpec(
                                query_id=selected_query["query_id"],
                                source_id=selected_source["source_id"],
                                source_database=selected_source_name,
                                query_label=selected_query["query_label"],
                                query_role=selected_query.get("query_role", "primary"),
                                query_string=selected_query["query_string"],
                                access_mode=selected_source["access_mode"],
                            )
                            with st.status(f"Running '{selected_label}' on {selected_source_name}…", expanded=True) as status:
                                try:
                                    result = adapter.run(spec)
                                    # Mirror counts back to legacy research_queries table for sidebar display
                                    cursor = conn.cursor()
                                    cursor.execute(
                                        "UPDATE research_queries SET status='completed', records_imported=? WHERE query_id=?",
                                        (result["imported"], selected_query["query_id"])
                                    )
                                    conn.commit()
                                    status.update(
                                        label=f"✅ Done — {result['imported']} records imported ({result['findings']} QA findings)",
                                        state="complete", expanded=False
                                    )
                                except Exception as e:
                                    status.update(label=f"❌ Error: {e}", state="error")
                            st.rerun()
                    else:
                        st.info("⚠️ This source requires manual export. Upload a RIS file below.")

                with setup_col:
                    if st.button("🔑 Open Source in Browser", use_container_width=True):
                        import webbrowser
                        urls = {
                            "PubMed": "https://pubmed.ncbi.nlm.nih.gov/",
                            "Europe PMC": "https://europepmc.org/",
                            "Scopus": "https://www.scopus.com/",
                            "Embase": "https://www.embase.com/",
                            "Google Scholar": "https://scholar.google.com/",
                        }
                        url = next((v for k, v in urls.items() if k in selected_source_name), None)
                        if url:
                            webbrowser.open_new_tab(url)

                # RIS Upload (for manual sources)
                if selected_source["access_mode"] in ["Supervised-login", "Browser-supervised"]:
                    st.info("⚠️ Manual source. Run search in browser, export `.ris`, then upload here.")
                    uploaded_file = st.file_uploader("Upload RIS Export", type=["ris"], key="ris_up")
                    if uploaded_file and st.button("📥 Import RIS File", key="ris_import"):
                        content = uploaded_file.getvalue().decode("utf-8", errors="replace")
                        spec = QuerySpec(
                            query_id=selected_query["query_id"],
                            source_id=selected_source["source_id"],
                            source_database=selected_source_name,
                            query_label=selected_query["query_label"],
                            query_role=selected_query.get("query_role", "primary"),
                            query_string=selected_query["query_string"],
                            access_mode=selected_source["access_mode"],
                        )
                        ris_adapter = RISAdapter(conn)
                        result = ris_adapter.from_ris_content(content, spec, selected_source_name)
                        st.success(f"Imported {result['imported']} records from RIS file.")
                        st.rerun()

            st.divider()
            st.write("📋 **Live Agent Logs**")
            logs = get_agent_logs(conn)
            for log in logs:
                q_info = f" | {log['query_label']}" if log['query_label'] else ""
                st.caption(f"[{str(log['timestamp'])[11:19]}] {log['action_type'].upper()}{q_info}: {log['message']}")

        with col_stats:
            st.subheader("📈 Quick Stats")
            st.metric("Total normalized records", total)
            all_queries = []
            for s in sources:
                all_queries.extend([dict(q) for q in get_queries_for_source(conn, s["source_id"])])
            pending = [q for q in all_queries if q["status"] == "pending"]
            st.metric("Pending queries", len(pending))
            st.divider()

            st.subheader("🏁 Phase Control")
            if pending:
                st.warning(f"{len(pending)} queries still pending.")
                if st.button("Skip Remaining & Open QA Gate"):
                    pass  # User navigates to QA tab
            else:
                st.success("All queries executed. Go to QA Gate tab to proceed.")

    # ────────────────────────────────────────────────────────
    # TAB 2 — Collection Dashboard
    # ────────────────────────────────────────────────────────
    with tab2:
        st.subheader("📊 Collection Dashboard")
        if total == 0:
            st.info("No records collected yet.")
        else:
            stats = get_collection_stats(conn)
            df = pd.DataFrame([dict(r) for r in stats])
            df.columns = ["Source", "Harvested", "With PMID", "With DOI",
                          "With Abstract", "Suspicious Year", "Enriched", "Attempted", "Avg Score"]
            st.dataframe(df, use_container_width=True)

            st.divider()
            st.subheader("🎯 Metadata Completeness Distribution")
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    sum(CASE WHEN metadata_completeness_score >= 80 THEN 1 ELSE 0 END) as screening_ready,
                    sum(CASE WHEN metadata_completeness_score >= 60 AND metadata_completeness_score < 80 THEN 1 ELSE 0 END) as warn,
                    sum(CASE WHEN metadata_completeness_score >= 40 AND metadata_completeness_score < 60 THEN 1 ELSE 0 END) as enrichment_needed,
                    sum(CASE WHEN metadata_completeness_score < 40 THEN 1 ELSE 0 END) as problem
                FROM normalized_records
            """)
            dist = cursor.fetchone()
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("✅ Screening Ready (≥80)", dist["screening_ready"])
            c2.metric("⚠️ Ready w/ Warning (60–79)", dist["warn"])
            c3.metric("🔬 Needs Enrichment (40–59)", dist["enrichment_needed"])
            c4.metric("🚨 Collection Problem (<40)", dist["problem"])

            st.divider()
            st.subheader("🔍 Browse Normalized Records")
            cursor.execute("""
                SELECT source_database, title, authors_raw, year, pmid, doi,
                       abstract_status, metadata_completeness_score, enrichment_status
                FROM normalized_records
                ORDER BY metadata_completeness_score DESC
                LIMIT 500
            """)
            rows = cursor.fetchall()
            df_all = pd.DataFrame([dict(r) for r in rows])
            csv = df_all.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download Full Dataset (CSV)", data=csv,
                               file_name="can_cchd_normalized_records.csv", mime="text/csv")
            st.dataframe(df_all, use_container_width=True, height=400)

    # ────────────────────────────────────────────────────────
    # TAB 3 — Enrichment Queue
    # ────────────────────────────────────────────────────────
    with tab3:
        st.subheader("🔬 Enrichment Queue")
        # Get REAL total count
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) as c FROM normalized_records WHERE enrichment_status IN ('pending', 'needs_enrichment') AND (abstract IS NULL OR abstract = '')")
        real_total_pending = cursor.fetchone()["c"]
        st.write(f"Records missing abstracts, routed for enrichment via PubMed / Crossref / OpenAlex / Unpaywall.")
        st.info(f"📊 **Total Pending in Database: {real_total_pending}** (Showing top 200 below)")
        queue = get_enrichment_queue(conn)
        if not queue:
            st.success("No records pending enrichment.")
        else:
            df_q = pd.DataFrame([dict(r) for r in queue])
            st.write(f"**{len(df_q)} records** need enrichment.")
            st.dataframe(df_q[["source_database", "title", "pmid", "doi",
                                "abstract_status", "enrichment_status", "metadata_completeness_score"]],
                         use_container_width=True, height=300)

            batch_size = st.slider("Batch size per run", 10, 100, 50, 10)
            if st.button("▶️ Run Enrichment Batch", type="primary", use_container_width=True):
                from can_cchd.collection.enrichment import run_enrichment_queue
                with st.spinner(f"Enriching up to {batch_size} records…"):
                    stats = run_enrichment_queue(conn, limit=batch_size)
                st.success(f"Processed {stats['processed']} records — "
                           f"✅ {stats['enriched']} enriched, ❌ {stats['failed']} not found.")
                st.rerun()

            st.divider()
            st.subheader("📋 Enrichment Log (last 50)")
            cursor = conn.cursor()
            cursor.execute("""
                SELECT record_id, enrichment_source, identifier_used, identifier_value,
                       fields_updated_json, status, completed_at
                FROM record_enrichment_log
                ORDER BY completed_at DESC
                LIMIT 50
            """)
            logs = cursor.fetchall()
            if logs:
                df_log = pd.DataFrame([dict(r) for r in logs])
                st.dataframe(df_log, use_container_width=True, height=300)

    # ────────────────────────────────────────────────────────
    # TAB 4 — QA Gate
    # ────────────────────────────────────────────────────────
    with tab4:
        st.subheader("🔒 Collection QA Gate")
        st.write("All checks must pass (or warnings accepted) before deduplication is allowed.")

        from can_cchd.collection.qa_gate import run_qa_gate, get_gate_status
        gate = get_gate_status(conn)

        if gate.get("status") == "not_run":
            st.info("QA Gate has not been run yet.")
        else:
            status = gate.get("status", "not_run")
            if status == "pass":
                st.success("✅ QA Gate: PASSED — No blocking issues found.")
            elif status == "warn":
                st.warning("⚠️ QA Gate: PASSED WITH WARNINGS — Review warnings below.")
            elif status == "block":
                st.error("🚫 QA Gate: BLOCKED — Fix blocking issues before proceeding.")

            summary = json.loads(gate.get("summary_json") or "{}")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Total Records", summary.get("total_records", 0))
            c2.metric("Screening Ready", summary.get("screening_ready", 0))
            c3.metric("🚫 Blocking Issues", summary.get("blocking_findings", 0))
            c4.metric("⚠️ Warnings", summary.get("warning_findings", 0))

        col_run, col_proceed = st.columns(2)

        with col_run:
            if st.button("🔍 Run QA Gate Now", use_container_width=True, type="primary"):
                with st.spinner("Running collection QA checks…"):
                    result = run_qa_gate(conn)
                st.rerun()

        with col_proceed:
            gate = get_gate_status(conn)
            gate_ok = gate.get("status") in ("pass", "warn")
            if gate_ok:
                if st.button("➡️ Proceed to Phase 2: Deduplication",
                             type="primary", use_container_width=True):
                    from can_cchd.workflow.next_action import update_phase_status
                    update_phase_status(conn, "1", "completed_with_note",
                                       note=f"QA Gate status: {gate.get('status')}. "
                                            f"Total: {gate.get('total_records',0)} records.")
                    st.success("Phase 1 completed! Navigating to Phase 2…")
                    st.rerun()
            else:
                st.button("➡️ Proceed to Phase 2", disabled=True, use_container_width=True,
                          help="Run QA Gate and resolve blocking issues first.")

        # Show detail of last QA run
        if gate.get("status") not in ("not_run", None):
            cursor = conn.cursor()
            cursor.execute("""
                SELECT severity, finding_type, message, recommended_action, count(*) as count
                FROM collection_qa_findings
                WHERE status = 'open'
                GROUP BY finding_type
                ORDER BY severity DESC
            """)
            findings = cursor.fetchall()
            if findings:
                st.divider()
                st.subheader("📋 Open QA Findings")
                df_f = pd.DataFrame([dict(r) for r in findings])
                st.dataframe(df_f, use_container_width=True)
