from playwright.sync_api import sync_playwright, expect


def verify_button_visibility(page):
    """
    Verify Button Visibility After Clicking 'Hide' Button

    Scenario:
    A web application may alter the visibility of elements in various ways: removing elements from the DOM,
    adjusting their size, hiding them via styles (opacity, visibility), or moving them offscreen. 

    In this test, we:
    1. Navigate to the 'Visibility' page.
    2. Click the 'Hide' button.
    3. Verify the visibility or CSS properties of other buttons, which are hidden or manipulated in different ways.

    The goal is to learn how to check the visibility of DOM elements using Playwright's `expect` API.

    Buttons checked:
    - Removed
    - Zero Width
    - Overlapped
    - Opacity 0
    - Visibility Hidden
    - Display None
    - Offscreen
    """

    print("Navigating to the visibility test page...")
    page.goto("http://uitestingplayground.com/visibility")

    # Locate all the buttons
    hide_button = page.get_by_role("button", name="Hide")
    removed_button = page.get_by_role("button", name="Removed")
    zero_width_button = page.get_by_role("button", name="Zero Width")
    overlapped_button = page.get_by_role("button", name="Overlapped")
    opacity_0_button = page.get_by_role("button", name="Opacity 0")
    hidden_button = page.get_by_role("button", name="Visibility Hidden")
    display_none_button = page.get_by_role("button", name="Display None")
    offscreen_button = page.get_by_role("button", name="Offscreen")

    # Step 1: Click the 'Hide' button to hide all other buttons
    print("Clicking the 'Hide' button...")
    hide_button.click()

    # Step 2: Verify visibility or CSS properties of the other buttons

    # Button removed from DOM
    print("Verifying 'Removed' button is no longer in the DOM...")
    expect(removed_button).to_be_hidden()

    # Button has zero width
    print("Verifying 'Zero Width' button has zero width...")
    expect(zero_width_button).to_have_css("width", "0px")

    # Button is overlapped by another element
    print("Verifying 'Overlapped' button is overlapped...")
    try:
        overlapped_button.click(timeout=2000)
    except :
        print("'Overlapped' button is not clickable (overlapped).")

    # Button has opacity set to 0
    print("Verifying 'Opacity 0' button has opacity set to 0...")
    expect(opacity_0_button).to_have_css("opacity", "0")

    # Button visibility set to hidden
    print("Verifying 'Visibility Hidden' button is hidden...")
    expect(hidden_button).to_be_hidden()

    # Button display set to none
    print("Verifying 'Display None' button is not displayed...")
    expect(display_none_button).to_be_hidden()

    # Button is offscreen
    print("Verifying 'Offscreen' button is off the visible viewport...")
    expect(offscreen_button).not_to_be_in_viewport()

    print("All button visibility checks completed successfully.")


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for verifying button visibility functionality.
    """

    # Launch the Chromium browser with slow motion for better visualization
    print("Launching the browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    print("Creating a new browser context and page...")
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()

    # Run the test case on the page
    print("Running the visibility test case...")
    verify_button_visibility(page)

    # Close the browser after the test completes
    print("Closing the browser...")
    browser.close()

    print("Test execution completed.")

    """
    Important Notes for Learning:
    - **Element Visibility**: This example shows how to check different types of visibility (hidden, zero width, opacity, etc.).
    - **Error Handling**: An example of handling a `TimeoutError` for when an element is not interactable due to being overlapped.
    - **Assertions**: Using Playwright’s `expect` API to check for hidden elements and CSS properties.
    """
