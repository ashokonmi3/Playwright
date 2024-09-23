from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

# Execute the test within sync_playwright context
with sync_playwright() as playwright:
    # Launch the browser and create a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    """
    Test case to demonstrate the usage of the expect API in Playwright
    for asserting the state of web elements on the Playwright Python page.

    Steps:
    - Navigate to the Playwright Python homepage.
    - Verify that the 'GET STARTED' link is visible and enabled.
    - Verify that the 'Get Python' link is hidden.
    """

    # Navigate to Playwright Python home page
    page.goto("https://playwright.dev/python")

    # Locate the 'GET STARTED' link by its role
    get_started_link = page.get_by_role("link", name="GET STARTED")

    # 1. Expect API: Check if the 'GET STARTED' link is visible
    expect(get_started_link).to_be_visible()
    print("GET STARTED link is visible.")

    # 2. Expect API: Check if the 'GET STARTED' link is enabled
    expect(get_started_link).to_be_enabled()
    print("GET STARTED link is enabled.")

    # Locate the 'Get Python' link by its role
    get_python_link = page.get_by_role("link", name="Get Python")

    # 3. Expect API: Check if the 'Get Python' link is hidden
    expect(get_python_link).to_be_hidden()
    print("Get Python link is hidden.")

    # 4. Expect API: Check if the 'Get Python' link is not visible (alternative check)
    expect(get_python_link).not_to_be_visible()
    print("Get Python link is confirmed not to be visible.")

    # Close the browser after the test
    browser.close()
