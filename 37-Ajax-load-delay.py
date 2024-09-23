from playwright.sync_api import sync_playwright, expect, TimeoutError


def test_load_delay(page):
    """
    Test Case: Handling delayed elements in Playwright

    This test demonstrates how to handle elements that appear after a delay 
    on a webpage, such as those triggered by AJAX requests.

    Steps:
    1. Navigate to a page where an AJAX request triggers a delayed response.
    2. Wait for the delayed content (paragraph) to load.
    3. Verify that the content is visible.
    4. Optionally perform additional actions if needed.
    """

    # Step 1: Navigate to the AJAX request page
    print("Navigating to the AJAX request page...")
    page.goto("http://uitestingplayground.com/ajax")

    # Step 2: Click the button that triggers the AJAX request
    print("Clicking the 'Button Triggering AJAX Request'...")
    ajax_button = page.get_by_role(
        "button", name="Button Triggering AJAX Request")
    ajax_button.click()

    # Step 3: Wait for the delayed paragraph to appear after the AJAX request
    print("Waiting for the paragraph to load after the AJAX request...")
    paragraph = page.locator("p.bg-success")
    paragraph.wait_for()  # Wait until the paragraph becomes available

    # Step 4: Verify that the paragraph is visible
    print("Verifying if the paragraph is visible...")
    expect(paragraph).to_be_visible()
    print("Paragraph is visible!")

    # Optionally, perform further actions on the element if needed
    print("Test case completed successfully!")


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for handling delayed elements.
    """

    # Launch the Chromium browser with slow motion for better visualization
    print("Launching browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    print("Creating new browser context and page...")
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()

    # Run the test case on the page
    print("Running the test case...")
    test_load_delay(page)

    # Close the browser after the test completes
    print("Closing browser...")
    browser.close()

    print("Test execution completed.")
