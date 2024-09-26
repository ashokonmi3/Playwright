from playwright.sync_api import Page

# page: Page: This indicates that the function takes a parameter named page of type Page.
# Here, Page is likely an object provided by a testing framework like Playwright.
# It represents a single browser page and provides methods to interact with that page

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(page: Page):
    
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    #     context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    #     page = context.new_page()

    
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == DOCS_URL

# pip install pytest-playwright
# pytest .\54-test_app.py
# pytest --headed .\54-test_app.py
# pytest --headed --slowmo=3000 .\54-test_app.py
# pytest --headed --browser=firefox --slowmo=3000 .\54-test_app.py
# If we define these options in pytest.ini it will take automatecilly we just need to pass the pytest command
