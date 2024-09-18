import time
import pytest
from playwright.sync_api import sync_playwright


def simple_script():
    """
    Demonstrates a basic Playwright script for navigating to a webpage and checking its title.

    Steps:
    1. Launches a Chromium browser in non-headless mode (i.e., a visible browser window).
    2. Opens a new page.
    3. Navigates to "https://example.com".
    4. Asserts that the page title is "Example Domain".
    5. Closes the browser.

    Notes:
    - `headless=False` allows you to see the browser window while the script is running.
    - `assert` is used to verify that the actual page title matches the expected title.
    """

    # Use the Playwright API to launch a Chromium browser
#     with sync_playwright() as p:
#         # Launch the browser with headless mode set to False
#         # This opens a visible browser window
#         browser = p.chromium.launch(headless=False)
        #   browser = p.firefox.launch(headless=False)


#         # Create a new page/tab in the browser
#         page = browser.new_page()

#         # Navigate to the specified URL
#         page.goto("https://example.com")

#         # Verify that the title of the page is as expected
#         assert page.title() == "Example Domain", "Title does not match the expected value"

#         # Close the browser window
#         browser.close()


# # Execute the function
# simple_script()
# ======================

# @pytest.mark.parametrize("browser_type", ["chromium", "firefox", "webkit"])
# def test_in_browser(browser_type):
#     with sync_playwright() as p:
#         # Choose browser based on parameter
#         browser = getattr(p, browser_type).launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto("https://example.com")
#         time.sleep(5)
#         assert page.title() == "Example Domain"
#         browser.close()


# # pytest .\2-test_Multiple-browser.py
