from playwright.sync_api import sync_playwright, expect


def verify_progress_bar(page):
    """
    Progress Bar
    A web application may use a progress bar to reflect the state of some lengthy process. 
    Thus, a test may need to read the value of a progress bar to determine if it is time to proceed or not.

    Scenario:
    Create a test that clicks the Start button and then waits for the progress bar to reach 75%. 
    Then the test should click Stop. The less the difference between the value of the stopped 
    progress bar and 75%, the better your result.
    """

    # Step 1: Navigate to the progress bar test page
    page.goto("http://uitestingplayground.com/progressbar")

    progressbar = page.get_by_role("progressbar")

    start_btn = page.get_by_role("button", name="Start")
    stop_btn = page.get_by_role("button", name="Stop")

    # Start progress
    start_btn.click()

    # Check progress
    while True:
        valuenow = int(progressbar.get_attribute("aria-valuenow"))
        print(f"Percent: {valuenow}%")

        # Progress more than or equal to 75
        if valuenow >= 75:
            break

    # Stop progress
    stop_btn.click()

    assert valuenow >= 75
    print(f"Progress bar stopped at {valuenow}%, which is above 75%.")


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for verifying progress bar functionality.
    """

    # Launch the Chromium browser with slow motion for better visualization
    print("Launching the browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    print("Creating a new browser context and page...")
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()

    # Run the test case on the page
    print("Running the test case...")
    verify_progress_bar(page)

    # Close the browser after the test completes
    print("Closing the browser...")
    browser.close()

    print("Test execution completed.")

    """
    Important Notes for Learning:
    - **Progress Bar Handling**: This example demonstrates how to work with progress bars 
      and read their values during a lengthy process.
    - **Assertions**: Using assertions ensures that the progress meets the expected criteria.
    """
