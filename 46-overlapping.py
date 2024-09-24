from playwright.sync_api import sync_playwright, expect


def test_overlapped_element_input(page):
    """
    Test Input in Overlapped Element

    This test demonstrates how to interact with an input field that may be partially visible due to overlapping elements. 
    It involves scrolling the element into view before entering text. 

    Scenario:
    1. Navigate to the page containing the overlapped element.
    2. Hover over the scrolling area to ensure it is highlighted.
    3. Scroll the area to bring the input field into view.
    4. Fill the input field with text.
    5. Take a screenshot of the scrolling area.
    6. Verify that the text entered is correct.

    Key Learning Points:
    - Understanding how to interact with overlapped or partially visible elements.
    - Using the mouse wheel for scrolling to make elements interactable.
    - Taking screenshots for verification and documentation purposes.
    """

    # Navigate to the webpage for overlapped element testing
    page.goto("http://uitestingplayground.com/overlapped")

    # Locate the input field by its placeholder
    input_field = page.get_by_placeholder("Name")

    # Hover over the parent div of the input to highlight it
    parent_div = input_field.locator("..")
    parent_div.hover()

    # Scroll down by 200 pixels to bring the input into view
    page.mouse.wheel(0, 200)

    # Fill the input field with data
    data = "python"
    input_field.fill(data)

    # Take a screenshot of the scroll area
    parent_div.screenshot(path="test-overlapped.jpg")

    # Assert that the input field contains the expected value
    expect(input_field).to_have_value(data)


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for inputting text into an overlapped element.

    - Launches the Chromium browser in non-headless mode with slow motion for better visualization.
    - Runs the `test_overlapped_element_input` function to test input functionality.
    """

    # Launch the Chromium browser with slow motion for better visualization
    print("Launching the browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    print("Creating a new browser context and page...")
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()

    # Run the test case on the page
    print("Running the overlapped element test case...")
    test_overlapped_element_input(page)

    # Close the browser after the test completes
    print("Closing the browser...")
    browser.close()

    print("Test execution completed.")


"""
================================================
Example Questions for Students:
================================================

1. What challenges might arise when interacting with partially visible elements?
   - Answer: Partially visible elements may not be interactable until they are scrolled into view, requiring additional steps to ensure visibility.

2. How does the `mouse.wheel()` method work, and when would you use it?
   - Answer: The `mouse.wheel()` method simulates scrolling actions, allowing elements to be brought into view by adjusting the scroll position.

3. What is the significance of taking a screenshot during a test?
   - Answer: Screenshots provide visual documentation of the state of the application at a specific point in time, which can be useful for debugging and reporting.

4. How can you confirm that an input field contains the expected value after filling it?
   - Answer: You can use the `expect()` method to assert that the value of the input field matches the expected text.

5. What is the purpose of using `ignore_https_errors=True` in the context?
   - Answer: This option allows the browser to bypass HTTPS certificate errors, making it suitable for testing on sites with self-signed certificates or non-secure connections.

================================================
Advanced Questions:
================================================

1. How would you modify the test to handle scenarios where the element may not be visible at first?
   - Answer: You could implement a wait mechanism, such as `page.wait_for_selector()`, to wait until the element is visible before interacting with it.

2. What are some alternative methods for scrolling an element into view without using the mouse wheel?
   - Answer: You can use JavaScript execution to scroll the element into view, such as `page.evaluate()` to call `element.scrollIntoView()`.

3. Explain the importance of the `no_viewport=True` option when launching the browser context.
   - Answer: The `no_viewport=True` option allows the page to open without default size restrictions, ensuring the full content can be rendered for testing.

"""
