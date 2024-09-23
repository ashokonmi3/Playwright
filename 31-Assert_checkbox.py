import time
from playwright.sync_api import expect, sync_playwright

with sync_playwright() as playwright:
    """
    Test case demonstrating various `expect` API assertions in Playwright:
    - Verifying the checked state of checkboxes
    """

    # 1. Launch the Chromium browser (non-headless for visibility)
    browser = playwright.chromium.launch(
        headless=False, slow_mo=3000, args=["--start-maximized"]
    )

    # Create a new browser context and page
    context = browser.new_context(
        ignore_https_errors=True, no_viewport=True
    )
    page = context.new_page()

    # 2. Navigate to the Bootswatch page
    page.goto("https://bootswatch.com/default")
    time.sleep(2)
    # Locate the checkboxes using their labels
    default_checkbox = page.get_by_label("Default checkbox")
    checked_checkbox = page.get_by_label("Checked checkbox")

    # Scroll to the checked checkbox to ensure it's in view
    checked_checkbox.scroll_into_view_if_needed()
    time.sleep(2)
    # 3. Expect that the checked checkbox is checked
    expect(checked_checkbox).to_be_checked()
    print("Checked checkbox is checked.")
    time.sleep(2)
    # 4. Expect that the default checkbox is unchecked
    expect(default_checkbox).not_to_be_checked()
    print("Default checkbox is unchecked.")
    time.sleep(2)
    # Close the browser after the test
    browser.close()
