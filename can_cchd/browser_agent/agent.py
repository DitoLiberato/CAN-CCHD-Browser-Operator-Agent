import os
import datetime
import asyncio
import re
from uuid import uuid4
from playwright.sync_api import sync_playwright
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class BrowserAgent:
    """
    Playwright-based Browser Operator Agent for CAN-CCHD.
    Supports accumulative multi-query search.
    """
    def __init__(self, conn, run_id=None):
        self.conn = conn
        self.run_id = run_id or str(uuid4())
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-pro-exp-02-05")
        self.browser_mode = os.getenv("BROWSER_MODE", "headful")
        
        self.client = None
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)

    def log_action(self, action_type, message, status="success", source_db=None, url=None, result_count=None, query_label=None):
        cursor = self.conn.cursor()
        now = datetime.datetime.now(datetime.UTC).isoformat()
        
        cursor.execute(
            """INSERT INTO agent_action_log (
                action_id, agent_run_id, timestamp, action_type, action_status, 
                message, source_database, url, result_count, query_label
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (str(uuid4()), self.run_id, now, action_type, status, message, source_db, url, result_count, query_label)
        )
        self.conn.commit()

    def assist_setup_api(self, source_name):
        """Opens the browser to help the user setup API keys or perform manual searches."""
        import webbrowser
        
        urls = {
            "PubMed": "https://pubmed.ncbi.nlm.nih.gov/",
            "Europe PMC": "https://europepmc.org/",
            "Embase": "https://www.embase.com/",
            "Scopus": "https://www.scopus.com/",
            "Web of Science": "https://www.webofscience.com/",
            "LILACS": "https://pesquisa.bvsalud.org/portal/",
            "SciELO": "https://search.scielo.org/",
            "IMEMR": "https://imemr.emro.who.int/",
            "Google Scholar": "https://scholar.google.com/",
            "Semantic Scholar": "https://www.semanticscholar.org/",
            "CrossRef": "https://search.crossref.org/",
            "OpenAlex": "https://explore.openalex.org/"
        }
        
        url = None
        for k, v in urls.items():
            if k in source_name:
                url = v
                break
                
        if not url:
            self.log_action("error", f"No setup URL mapped for source {source_name}")
            return
            
        try:
            # Use the system's default browser instead of Playwright
            # This prevents anti-bot systems (like BVS) from blocking the connection,
            # and allows the user to use their institutional login/VPN sessions.
            webbrowser.open_new_tab(url)
            self.log_action("navigation", f"Opened {source_name} in your default browser for manual access.", url=url)
        except Exception as e:
            self.log_action("error", f"Failed to open browser for {source_name}: {str(e)}")
            
        return True

    def run_search(self, source_id, source_name, query_id):
        """Performs a real search using a specific query_id."""
        cursor = self.conn.cursor()
        
        # Mark source as running
        cursor.execute("UPDATE research_sources SET status = 'running' WHERE source_id = ?", (source_id,))
        self.conn.commit()
        
        # Get query
        cursor.execute("SELECT query_label, query_string FROM research_queries WHERE query_id = ?", (query_id,))
        query_row = cursor.fetchone()
        if not query_row:
            self.log_action("error", "Query ID not found in database", status="error")
            return False
            
        query_label = query_row["query_label"]
        query_string = query_row["query_string"]
        
        self.log_action("start_search", f"Starting search: {query_label}", source_db=source_name, query_label=query_label)
        
        records_count = 0
        
        with sync_playwright() as p:
            headless = (self.browser_mode == "headless")
            browser = p.chromium.launch(headless=headless)
            
            # Use a longer timeout for supervised login sources
            cursor.execute("SELECT access_mode FROM research_sources WHERE source_id = ?", (source_id,))
            access_mode = cursor.fetchone()["access_mode"]
            
            page = browser.new_page()
            
            if access_mode == "Supervised-login":
                self.log_action("wait_login", f"Waiting for manual login to {source_name}...", query_label=query_label)
                # We'll just open the base URL and wait for the user
                # For Embase/Scopus, this is usually their login portals
                page.goto(self._get_base_url(source_name))
                # Wait for user to signal completion in Streamlit or a long timeout
                # For now, we'll wait 60s as a demo of "Supervised"
                page.wait_for_timeout(60000)
            
            if "PubMed" in source_name:
                records_count = self._scrape_pubmed(page, query_string, source_id, query_id, query_label)
            elif "Europe PMC" in source_name:
                records_count = self._scrape_europe_pmc(page, query_string, source_id, query_id, query_label)
            elif "Crossref" in source_name or "CrossRef" in source_name:
                records_count = self._scrape_crossref(query_string, source_id, query_id, query_label)
            elif "OpenAlex" in source_name:
                records_count = self._scrape_openalex(query_string, source_id, query_id, query_label)
            elif "Semantic Scholar" in source_name:
                records_count = self._scrape_semantic_scholar(query_string, source_id, query_id, query_label)
            elif "Google Scholar" in source_name:
                records_count = self._scrape_google_scholar(page, query_string, source_id, query_id, query_label)
            else:
                self.log_action("error", f"Automated scraping for {source_name} not implemented. Run manually and export RIS/CSV.", status="error", query_label=query_label)
                
            browser.close()
            
        # Update source stats (Cumulative)
        cursor.execute("UPDATE research_queries SET status = 'completed', result_count = ?, records_imported = ?, run_at = ? WHERE query_id = ?", 
                       (records_count, records_count, datetime.datetime.now(datetime.UTC).isoformat(), query_id))
        
        # Update source overall
        cursor.execute("SELECT sum(records_imported) as total FROM research_queries WHERE source_id = ?", (source_id,))
        total_imported = cursor.fetchone()["total"]
        cursor.execute("UPDATE research_sources SET status = 'completed', records_imported = ? WHERE source_id = ?", (total_imported, source_id))
        
        self.conn.commit()
        return True

    def _get_base_url(self, source_name):
        urls = {
            "PubMed": "https://pubmed.ncbi.nlm.nih.gov/",
            "Embase": "https://www.embase.com/",
            "Scopus": "https://www.scopus.com/",
            "Europe PMC": "https://europepmc.org/"
        }
        for k, v in urls.items():
            if k in source_name: return v
        return "https://www.google.com"

    def _scrape_pubmed(self, page, query, source_id, query_id, label):
        import urllib.parse
        search_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={urllib.parse.quote(query)}&sort=date"
        self.log_action("navigation", "Navigating to PubMed with Date Sort", url=search_url, query_label=label)
        
        page.goto(search_url)
        page.wait_for_load_state("networkidle")
        
        page_num = 1
        
        while True:
            self.log_action("extraction", f"Scraping PubMed page {page_num}...", query_label=label)
            page.wait_for_selector(".docsum-content", timeout=10000)
            results = page.query_selector_all(".docsum-content")
            
            for res in results:
                title_el = res.query_selector(".docsum-title")
                title = title_el.inner_text().strip() if title_el else "Unknown Title"
                
                pmid_el = res.query_selector(".docsum-pmid")
                pmid = pmid_el.inner_text().strip() if pmid_el else None
                
                authors_el = res.query_selector(".docsum-authors")
                authors = authors_el.inner_text().strip() if authors_el else ""
                
                year_el = res.query_selector(".docsum-journal-citation")
                year_text = year_el.inner_text() if year_el else ""
                year = 2024
                try:
                    year_match = re.search(r'\d{4}', year_text)
                    if year_match: year = int(year_match.group())
                except: pass
                    
                self._save_record(title, authors, year, pmid, None, source_id, query_id, "PubMed")
            
            # Check for Next Button
            next_button = page.query_selector(".next-page")
            if next_button:
                # Check if it is disabled
                is_disabled = next_button.get_attribute("disabled") is not None or "disabled" in (next_button.get_attribute("class") or "")
                if not is_disabled:
                    next_button.click()
                    page_num += 1
                    page.wait_for_timeout(2000) # Give it a breath
                    page.wait_for_load_state("networkidle")
                else:
                    break
            else:
                break
                
        # Get true count from database to avoid AJAX DOM duplication inflation
        cursor = self.conn.cursor()
        cursor.execute("SELECT count(*) as c FROM records WHERE query_id = ?", (query_id,))
        true_count = cursor.fetchone()["c"]
        
        self.log_action("extraction", f"Total extracted: {true_count} unique records from PubMed ({label})", result_count=true_count, query_label=label)
        return true_count

    def _scrape_europe_pmc(self, page, query, source_id, query_id, label):
        import urllib.parse
        search_url = f"https://europepmc.org/search?query={urllib.parse.quote(query)}"
        self.log_action("navigation", "Navigating to Europe PMC Search", url=search_url, query_label=label)
        
        page.goto(search_url)
        page.wait_for_load_state("networkidle")
        
        page_num = 1
        
        while True:
            self.log_action("extraction", f"Scraping Europe PMC page {page_num}...", query_label=label)
            try:
                page.wait_for_selector(".citation-title", timeout=10000)
            except:
                break
                
            results = page.query_selector_all(".citation-title")
            
            for title_el in results:
                title = title_el.inner_text().strip() if title_el else "Unknown Title"
                
                pmid = None
                link = title_el.query_selector("a")
                if link:
                    href = link.get_attribute("href") or ""
                    if "/MED/" in href:
                        pmid = href.split("/")[-1]
                
                wrapper = title_el.evaluate_handle('el => el.parentElement')
                authors_el = wrapper.query_selector(".citation-author-list")
                authors = authors_el.inner_text().strip() if authors_el else ""
                
                self._save_record(title, authors, 2024, pmid, None, source_id, query_id, "Europe PMC")
                
            # Check for Next Button
            next_button = page.query_selector("#search-results--pagination--link-next")
            if next_button:
                is_disabled = "disabled" in (next_button.get_attribute("class") or "")
                if not is_disabled:
                    next_button.click()
                    page_num += 1
                    page.wait_for_timeout(2000)
                    page.wait_for_load_state("networkidle")
                else:
                    break
            else:
                break
            
        cursor = self.conn.cursor()
        cursor.execute("SELECT count(*) as c FROM records WHERE query_id = ?", (query_id,))
        true_count = cursor.fetchone()["c"]
        
        self.log_action("extraction", f"Total extracted: {true_count} unique records from Europe PMC ({label})", result_count=true_count, query_label=label)
        return true_count

    def _scrape_crossref(self, query, source_id, query_id, label):
        import requests
        import urllib.parse
        import time
        
        # Crossref encourages 'mailto' in headers for their polite pool
        headers = {"User-Agent": "CAN-CCHD-Agent/1.0 (mailto:researcher@example.com)"}
        
        self.log_action("navigation", f"Calling Crossref API for '{label}'", query_label=label)
        
        rows = 100
        cursor_mark = "*"
        total_extracted = 0
        max_results = 500 # Prevent infinite loops
        
        while total_extracted < max_results:
            self.log_action("extraction", f"Fetching from Crossref API (cursor: {cursor_mark[:10]}...)", query_label=label)
            
            url = f"https://api.crossref.org/works?query={urllib.parse.quote(query)}&select=title,author,published,DOI&rows={rows}&cursor={urllib.parse.quote(cursor_mark)}"
            
            try:
                response = requests.get(url, headers=headers)
                if response.status_code != 200:
                    self.log_action("error", f"Crossref API returned status {response.status_code}", status="error", query_label=label)
                    break
                    
                data = response.json()
                items = data.get("message", {}).get("items", [])
                
                if not items:
                    break
                    
                for item in items:
                    title_list = item.get("title", [])
                    title = title_list[0] if title_list else "Unknown Title"
                    
                    authors_list = item.get("author", [])
                    author_names = []
                    for a in authors_list:
                        family = a.get("family", "")
                        given = a.get("given", "")
                        if family or given:
                            author_names.append(f"{family} {given}".strip())
                    authors = ", ".join(author_names) if author_names else ""
                    
                    year = 2024
                    published = item.get("published", {})
                    date_parts = published.get("date-parts", [])
                    if date_parts and date_parts[0]:
                        year = date_parts[0][0]
                        
                    doi = item.get("DOI")
                    
                    self._save_record(title, authors, year, None, doi, source_id, query_id, "Crossref")
                    total_extracted += 1
                    
                next_cursor = data.get("message", {}).get("next-cursor")
                if not next_cursor or next_cursor == cursor_mark:
                    break
                cursor_mark = next_cursor
                
                time.sleep(1) # Be polite
                
            except Exception as e:
                self.log_action("error", f"Error querying Crossref: {str(e)}", status="error", query_label=label)
                break
                
        cursor = self.conn.cursor()
        cursor.execute("SELECT count(*) as c FROM records WHERE query_id = ?", (query_id,))
        true_count = cursor.fetchone()["c"]
        
        self.log_action("extraction", f"Total extracted: {true_count} unique records from Crossref ({label})", result_count=true_count, query_label=label)
        return true_count

    def _scrape_openalex(self, query, source_id, query_id, label):
        import requests
        import urllib.parse
        import time
        
        self.log_action("navigation", f"Calling OpenAlex API for '{label}'", query_label=label)
        
        per_page = 100
        cursor_mark = "*"
        total_extracted = 0
        max_results = 500 # Prevent infinite loops
        mailto = "researcher@example.com" # Required for polite pool
        
        while total_extracted < max_results:
            self.log_action("extraction", f"Fetching from OpenAlex API (cursor: {cursor_mark[:10]}...)", query_label=label)
            
            url = f"https://api.openalex.org/works?search={urllib.parse.quote(query)}&per-page={per_page}&cursor={urllib.parse.quote(cursor_mark)}&mailto={mailto}"
            
            try:
                response = requests.get(url)
                if response.status_code != 200:
                    self.log_action("error", f"OpenAlex API returned status {response.status_code}", status="error", query_label=label)
                    break
                    
                data = response.json()
                results = data.get("results", [])
                
                if not results:
                    break
                    
                for item in results:
                    title = item.get("title") or "Unknown Title"
                    
                    authorships = item.get("authorships", [])
                    author_names = []
                    for a in authorships:
                        display_name = a.get("author", {}).get("display_name")
                        if display_name:
                            author_names.append(display_name)
                    authors = ", ".join(author_names) if author_names else ""
                    
                    year = item.get("publication_year") or 2024
                    
                    ids = item.get("ids", {})
                    doi = ids.get("doi")
                    if doi and doi.startswith("https://doi.org/"):
                        doi = doi.replace("https://doi.org/", "")
                        
                    pmid = ids.get("pmid")
                    if pmid and pmid.startswith("https://pubmed.ncbi.nlm.nih.gov/"):
                        pmid = pmid.replace("https://pubmed.ncbi.nlm.nih.gov/", "")
                    
                    self._save_record(title, authors, year, pmid, doi, source_id, query_id, "OpenAlex")
                    total_extracted += 1
                    
                meta = data.get("meta", {})
                next_cursor = meta.get("next_cursor")
                if not next_cursor or next_cursor == cursor_mark:
                    break
                cursor_mark = next_cursor
                
                time.sleep(1) # Be polite
                
            except Exception as e:
                self.log_action("error", f"Error querying OpenAlex: {str(e)}", status="error", query_label=label)
                break
                
        cursor = self.conn.cursor()
        cursor.execute("SELECT count(*) as c FROM records WHERE query_id = ?", (query_id,))
        true_count = cursor.fetchone()["c"]
        
        self.log_action("extraction", f"Total extracted: {true_count} unique records from OpenAlex ({label})", result_count=true_count, query_label=label)
        return true_count

    def _scrape_semantic_scholar(self, query, source_id, query_id, label):
        import requests
        import urllib.parse
        import time
        
        self.log_action("navigation", f"Calling Semantic Scholar API for '{label}'", query_label=label)
        
        limit = 100
        offset = 0
        total_extracted = 0
        max_results = 500 # Prevent infinite loops
        retries = 0
        max_retries = 3
        
        while total_extracted < max_results:
            self.log_action("extraction", f"Fetching from Semantic Scholar API (offset: {offset})...", query_label=label)
            
            url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&offset={offset}&fields=title,authors,year,externalIds"
            
            try:
                response = requests.get(url)
                if response.status_code == 429:
                    if retries >= max_retries:
                        self.log_action("error", "Semantic Scholar API Rate Limit Exceeded permanently. Aborting.", query_label=label)
                        break
                    self.log_action("error", f"Semantic Scholar API Rate Limit Exceeded. Waiting 5s... (Retry {retries+1}/{max_retries})", query_label=label)
                    time.sleep(5)
                    retries += 1
                    continue
                elif response.status_code != 200:
                    self.log_action("error", f"Semantic Scholar API returned status {response.status_code}", status="error", query_label=label)
                    break
                    
                # Reset retries on success
                retries = 0
                
                data = response.json()
                items = data.get("data", [])
                
                if not items:
                    break
                    
                for item in items:
                    title = item.get("title") or "Unknown Title"
                    
                    authors_list = item.get("authors", [])
                    author_names = []
                    for a in authors_list:
                        name = a.get("name")
                        if name:
                            author_names.append(name)
                    authors = ", ".join(author_names) if author_names else ""
                    
                    year = item.get("year") or 2024
                    
                    external_ids = item.get("externalIds", {})
                    doi = external_ids.get("DOI")
                    pmid = external_ids.get("PubMed")
                    
                    self._save_record(title, authors, year, pmid, doi, source_id, query_id, "Semantic Scholar")
                    total_extracted += 1
                    
                # Semantic Scholar pagination
                next_offset = data.get("next")
                if not next_offset:
                    break
                offset = next_offset
                
                time.sleep(1) # Be polite
                
            except Exception as e:
                self.log_action("error", f"Error querying Semantic Scholar: {str(e)}", status="error", query_label=label)
                break
                
        cursor = self.conn.cursor()
        cursor.execute("SELECT count(*) as c FROM records WHERE query_id = ?", (query_id,))
        true_count = cursor.fetchone()["c"]
        
        self.log_action("extraction", f"Total extracted: {true_count} unique records from Semantic Scholar ({label})", result_count=true_count, query_label=label)
        return true_count

    def _scrape_google_scholar(self, page, query, source_id, query_id, label):
        import urllib.parse
        search_url = f"https://scholar.google.com/scholar?q={urllib.parse.quote(query)}"
        self.log_action("navigation", "Navigating to Google Scholar", url=search_url, query_label=label)
        
        page.goto(search_url)
        page.wait_for_load_state("networkidle")
        
        page_num = 1
        total_extracted = 0
        max_results = 300 # Google Scholar blocks aggressively, keep it reasonable
        
        while total_extracted < max_results:
            self.log_action("extraction", f"Scraping Google Scholar page {page_num}... (Solve Captcha if it appears!)", query_label=label)
            
            # Check for hard block first
            if page.locator("text=unusual traffic").count() > 0:
                self.log_action("error", "Google Scholar Hard IP Block detected ('unusual traffic'). Stopping.", status="error", query_label=label)
                break
                
            # Wait for results OR captcha. We give the user 60 seconds to solve a captcha.
            try:
                page.wait_for_selector(".gs_ri", timeout=60000)
            except:
                if page.query_selector("form") or page.locator("text=unusual traffic").count() > 0:
                    self.log_action("error", "Google Scholar Captcha timeout or hard block. Stopping.", status="error", query_label=label)
                else:
                    self.log_action("error", "Google Scholar page timeout. Results not found.", status="error", query_label=label)
                break
                
            results = page.query_selector_all(".gs_ri")
            if not results:
                break
                
            for res in results:
                title_el = res.query_selector(".gs_rt a") or res.query_selector(".gs_rt")
                title = title_el.inner_text().strip() if title_el else "Unknown Title"
                
                authors_year_el = res.query_selector(".gs_a")
                authors_year = authors_year_el.inner_text().strip() if authors_year_el else ""
                
                # Format: "A Einstein, B Podolsky... - Physical review, 1935 - APS"
                authors = authors_year.split(" - ")[0] if " - " in authors_year else authors_year
                
                year = 2024
                import re
                year_match = re.search(r'\b(19|20)\d{2}\b', authors_year)
                if year_match:
                    year = int(year_match.group())
                    
                self._save_record(title, authors, year, None, None, source_id, query_id, "Google Scholar")
                total_extracted += 1
                if total_extracted >= max_results:
                    break
            
            if total_extracted >= max_results:
                break
                
            # Check for Next Button
            # Google scholar next button is a link with text "Next" or class "gs_ico_nav_next"
            next_button = page.query_selector("button.gs_btnPR") or page.query_selector("b:text('Next')")
            if not next_button:
                next_button = page.locator("a:has(span.gs_ico_nav_next)")
                if next_button.count() > 0:
                    next_button = next_button.first
                else:
                    next_button = None
                    
            if next_button:
                next_button.click()
                page_num += 1
                page.wait_for_timeout(3000) # Give it a breath
                page.wait_for_load_state("networkidle")
            else:
                break
                
        cursor = self.conn.cursor()
        cursor.execute("SELECT count(*) as c FROM records WHERE query_id = ?", (query_id,))
        true_count = cursor.fetchone()["c"]
        
        self.log_action("extraction", f"Total extracted: {true_count} unique records from Google Scholar ({label})", result_count=true_count, query_label=label)
        return true_count

    def _save_record(self, title, authors, year, pmid, doi, source_id, query_id, source_db):
        cursor = self.conn.cursor()
        now = datetime.datetime.now(datetime.UTC).isoformat()
        
        # 1. Deduplication logic (UPSERT)
        # Check if study already exists in 'studies' table by PMID or DOI
        existing_study = None
        if pmid:
            cursor.execute("SELECT study_id FROM studies WHERE pmid = ?", (pmid,))
            existing_study = cursor.fetchone()
        
        if not existing_study and doi:
            cursor.execute("SELECT study_id FROM studies WHERE doi = ?", (doi,))
            existing_study = cursor.fetchone()
            
        if existing_study:
            study_id = existing_study["study_id"]
        else:
            study_id = str(uuid4())
            cursor.execute(
                """INSERT INTO studies (study_id, title, first_author, year, status, pmid, doi, created_at)
                   VALUES (?, ?, ?, ?, 'initial_collection', ?, ?, ?)""",
                (study_id, title, authors.split(',')[0], year, pmid, doi, now)
            )
        
        # 2. Save to records (Always append, even if study exists, because it might be from a different query)
        # But check if this record (record-source-query) already exists
        cursor.execute("SELECT record_id FROM records WHERE study_id = ? AND query_id = ?", (study_id, query_id))
        if not cursor.fetchone():
            cursor.execute(
                """INSERT INTO records (record_id, study_id, source_id, query_id, source_database, title, authors, year, pmid, doi, imported_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (str(uuid4()), study_id, source_id, query_id, source_db, title, authors, year, pmid, doi, now)
            )
            
        self.conn.commit()
