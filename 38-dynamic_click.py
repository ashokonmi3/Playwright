from playwright.sync_api import sync_playwright, expect, TimeoutError


def test_load_delay(page):
    """
    Test Case: Emulating physical mouse clicks in Playwright

    This test demonstrates the difference between physical mouse clicks 
    and DOM event emulated clicks, specifically on a button designed to ignore 
    event-based clicks.

    Scenario:
    1. Navigate to a page where a button becomes green after being clicked.
    2. Execute a test to ensure that the button can be clicked successfully.

    Steps:
    1. Navigate to the click test page.
    2. Click the button that ignores DOM click events.
    3. Verify that the button changes its class to indicate success.
    """

    # Step 1: Navigate to the AJAX request page
    print("Navigating to the click test page...")
    page.goto("http://uitestingplayground.com/click")

    # Step 2: Find the button and click it
    print("Clicking the 'Button That Ignores DOM Click Event'...")
    btn = page.get_by_role(
        "button", name="Button That Ignores DOM Click Event")
    btn.click()

    # Step 3: Verify that the button has changed its class
    print("Verifying that the button has changed to 'btn btn-success'...")
    expect(btn).to_have_class("btn btn-success")
    print("Button successfully clicked and class changed!")


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for handling delayed elements.
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
    test_load_delay(page)

    # Close the browser after the test completes
    print("Closing the browser...")
    browser.close()

    print("Test execution completed.")

    """
    Important Notes for Learning:
    - **Mouse Click Handling**: This example illustrates how emulating a physical mouse click
      can sometimes be necessary for buttons that ignore event-based clicks.
    - **Assertions**: Using Playwright’s `expect` API ensures that the button's state
      is as expected after the click, enhancing test reliability.
    """
