import time
from playwright.sync_api import Page, expect, sync_playwright

with sync_playwright() as playwright:
    """
    Test case demonstrating various `expect` API assertions in Playwright:
    - Verifying exact class names
    - Using regular expressions to validate partial class names
    - Checking for the presence of attributes and their values in web elements
    """

    # 1. Launch the Chromium browser (non-headless for visibility)
    browser = playwright.chromium.launch(headless=False)

    # 2. Create a new page instance (new browser tab)
    page = browser.new_page()

    # 3. Navigate to the Playwright Python documentation page
    page.goto("https://playwright.dev/python")

    """
    Test the visibility and functionality of the search input on Playwright's Python documentation page.

    Steps:
    1. Verify that the search input is hidden initially.
    2. Use the keyboard shortcut to focus on the search bar and verify its visibility and editability.
    3. Ensure the search input is initially empty.
    4. Fill the search input with a query and verify the input value matches the query.

    Assertions:
    - The search input is initially hidden.
    - After triggering the search, the input should be editable.
    - The input is empty before any typing.
    - After typing a query, the input should hold the expected value.
    """

    # Locate the search input using its placeholder
    input = page.get_by_placeholder("Search docs")

    # Initially, the search input should be hidden
    expect(input).to_be_hidden()
    time.sleep(2)

    # Locate the search button and simulate the keyboard shortcut to focus on the search input
    search_btn = page.get_by_role("button", name="Search")
    # search_btn.press("Control+KeyK")
    search_btn.click()
    time.sleep(2)

    # After pressing the shortcut, the search input should become visible and editable
    expect(input).to_be_visible()
    expect(input).to_be_editable()
    time.sleep(2)

    # The search input should be empty initially before any text is entered
    expect(input).to_be_empty()
    time.sleep(2)

    # Define a search query to fill into the input
    query = "assertions"

    # Fill the search input with the query
    input.fill(query)
    time.sleep(2)

    # Verify that the input value now matches the query
    expect(input).to_have_value(query)
    time.sleep(2)

    # Close the browser after the test
    browser.close()
