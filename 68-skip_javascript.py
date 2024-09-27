import pytest
from playwright.sync_api import Page, sync_playwright, expect


@pytest.fixture(scope="session")
def page():
    """
    Fixture to create a browser context with JavaScript disabled and provide a page object.
    This combines the browser context and page creation.
    """
    with sync_playwright() as p:
        # Launch the browser (not headless for visibility)
        browser = p.chromium.launch(headless=False)

        # Create a new context with JavaScript disabled
        context = browser.new_context(java_script_enabled=True)

        # Create a new page in the context
        page = context.new_page()

        yield page

        # Close the page and browser context after the test session
        page.close()
        context.close()
        browser.close()


def test_page_has_docs_link(page: Page):
    """
    Test that verifies the visibility of the link for loading movie data for the year 2015.
    """
    # Navigate to the website
    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

    # Locate the link for loading movie data for the year 2015 and click it
    link = page.get_by_role("link", name="2015")
    print("Clicking on the link...")
    link.click()

    print("Loading Oscars for 2015...")
    # Wait for a specific element to appear after clicking
    page.wait_for_selector("text=Oscars")

    # Check if the link is still visible after clicking
    expect(link).to_be_visible()
