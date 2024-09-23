from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    """
    Test case demonstrating `expect` API assertions in Playwright:
    - Verifying visibility of a button with a dynamic ID.
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

    # 2. Navigate to the UI Testing Playground
    page.goto("http://uitestingplayground.com/dynamicid")

    # Locate the button with a dynamic ID
    button = page.get_by_role("button", name="Button with Dynamic ID")
    button.scroll_into_view_if_needed()

    # 3. Expect the button to be visible
    expect(button).to_be_visible()
    print("Button with dynamic ID is visible.")

    # 4. Click the button
    button.click()
    print("Button clicked.")

    # Optional: Wait for some result after clicking, if applicable
    # For example, checking for a change in text or appearance
    # new_element = page.get_by_text("Expected Result")
    # expect(new_element).to_be_visible()

    # Close the browser after the test
    browser.close()
