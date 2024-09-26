import pytest
from playwright.sync_api import sync_playwright

# Fixture that launches a browser and creates a page for the entire test session


@pytest.fixture(scope="session")
def browser_page():
    """
    Fixture that sets up the browser and a page for the entire test session.

    This fixture is only invoked once per test session, providing a single
    instance of the browser and a page to all test functions.

    Yields:
        Page: The Playwright Page object representing the browser page.
    """
    with sync_playwright() as p:
        print("Initializing browser and page")  # This will show if -s is used
        browser = p.chromium.launch(headless=False)  # Launching the browser
        page = browser.new_page()                     # Creating a new page
        yield page                                     # Yielding the page for tests
        page.close()                                   # Closing the page after all tests
        browser.close()                               # Closing the browser after all tests
        print("Finished")


def test_navigate_to_playwright(browser_page):
    """
    Test that verifies navigation to the Playwright homepage.

    Args:
        browser_page (Page): The page object from the fixture.
    """
    browser_page.goto("https://playwright.dev")
    assert browser_page.title() == "Fast and reliable end-to-end testing for modern web apps"


def test_check_element_visibility(browser_page):
    """
    Test that checks if the "Get Started" button is visible on the Playwright page.

    Args:
        browser_page (Page): The page object from the fixture.
    """
    browser_page.goto("https://playwright.dev")
    assert browser_page.is_visible("text=Get Started")


def test_check_docs_link(browser_page):
    """
    Test that verifies the visibility of the Docs link on the Playwright page.

    Args:
        browser_page (Page): The page object from the fixture.
    """
    browser_page.goto("https://playwright.dev")
    docs_link = browser_page.locator("text=Docs")
    assert docs_link.is_visible()
