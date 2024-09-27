import pytest
from playwright.sync_api import sync_playwright

# Fixture to create a browser and page object


@pytest.fixture(scope="module")
def browser_page():
    with sync_playwright() as p:
        # Launch the browser in headful mode (visible)
        browser = p.chromium.launch(
            headless=False, slow_mo=2000)  # Set headless to False
        # Create a new page
        page = browser.new_page()
        yield page  # Yield the page object to the test
        # Close the browser after tests are done
        browser.close()


# Test data for parameterization
test_data = [
    ("https://example.com", "Example Domain"),
    ("https://www.wikipedia.org", "Wikipedia"),
    ("https://www.google.com", "Google")
]


@pytest.mark.parametrize("url, title", test_data)
def test_page_title(browser_page, url, title):
    page = browser_page  # Use the page object from the fixture
    page.goto(url)  # Navigate to the URL

    assert page.title() == title  # Assert the title
