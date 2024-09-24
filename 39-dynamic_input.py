from playwright.sync_api import sync_playwright, expect, TimeoutError


def test_load_delay(page):
    """
    Test Case: Emulating physical keyboard input in Playwright

    This test demonstrates the difference between entering text with a physical keyboard 
    and sending DOM events to an input field. It highlights scenarios where DOM events may 
    fail and physical keyboard emulation is required.

    Scenario:
    1. Enter text into an input field.
    2. Press a button to change its name based on the input.
    """

    # Step 1: Navigate to the text input page
    print("Navigating to the text input page...")
    page.goto("http://uitestingplayground.com/textinput")

    # Step 2: Fill the input field with text
    query = 'great stuff'
    print(f"Entering text: '{query}' into the input field...")
    input_field = page.get_by_label("Set New Button Name")
    input_field.fill(query)

    # Step 3: Click the button to change its name
    print("Clicking the button to set the new name...")
    btn = page.locator("button.btn-primary")
    btn.click()

    # Step 4: Verify that the button's text has changed
    print("Verifying that the button text has changed...")
    expect(btn).to_have_text(query)
    print("Button successfully clicked and text changed!")


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for handling keyboard input.
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
    - **Keyboard Input Handling**: This example illustrates the importance of using physical 
      keyboard emulation when DOM events fail to work properly.
    - **Assertions**: Using Playwright’s `expect` API ensures that the input has been successfully 
      registered, enhancing the reliability of the test.
    """
