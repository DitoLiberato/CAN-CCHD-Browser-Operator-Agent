from playwright.sync_api import sync_playwright

def get_classes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://pesquisa.bvsalud.org/portal/?q=cardiopatia+congenita")
        page.wait_for_load_state("networkidle")
        
        # Titles are usually in a tag inside a class .title
        links = page.query_selector_all(".title a")
        for a in links[:3]:
            print(a.inner_text().strip())
                
        browser.close()

if __name__ == "__main__":
    get_classes()
