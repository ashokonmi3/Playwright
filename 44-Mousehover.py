import time
from playwright.sync_api import sync_playwright, expect


def test_mouse_over_click_count(page):
    """
    Verifies the functionality of mouse-over and click events on a webpage.

    This function performs the following actions:
    - Navigates to a webpage that demonstrates mouse-over interactions.
    - Hovers over a link to trigger changes in the DOM.
    - Performs two consecutive clicks on the "Active link" to increment a click counter.
    - Asserts that the click counter increases by 2.

    Key Learning Points:
    - Understanding how to use the `hover()` and `click()` methods.
    - Handling dynamic DOM changes caused by mouse-over events.
    - Using Playwright's `expect()` method to validate test results.

    Mouse Hover Functionality:
    ---------------------------
    The `hover()` method in Playwright simulates placing the mouse pointer over a specified element on the page.
    This action can lead to changes in the webpage's DOM, such as displaying tooltips, changing styles, or
    revealing hidden elements. 

    Important Considerations:
    - When an element is hovered over, the element may change or be replaced in the DOM. If a reference to 
      the original element is kept and an action is attempted on it afterward, it may not work due to the 
      stale element problem.
    - It’s crucial to ensure that any subsequent interactions (like clicks) are performed on the currently 
      active or visible element, especially after a hover action that modifies the DOM.
    """

    # Navigate to the webpage for mouse-over testing
    page.goto("http://uitestingplayground.com/mouseover")

    # Hover over the "Click me" link
    link = page.get_by_title("Click me")
    link.hover()
    time.sleep(5)

    # Perform two consecutive clicks on the active link
    active_link = page.get_by_title("Active link")
    active_link.click(click_count=2)
    time.sleep(5)

    # Locate the click counter on the page
    click_count = page.locator("span#clickCount")
    time.sleep(5)

    # Assert that the click count equals 2
    expect(click_count).to_have_text("2")
    time.sleep(5)


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for verifying button visibility functionality.

    - Launches the Chromium browser in non-headless mode with slow motion for better visualization.
    - Runs the `test_mouse_over_click_count` function to test click functionality.
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
    test_mouse_over_click_count(page)

    # Close the browser after the test completes
    print("Closing the browser...")
    browser.close()

    print("Test execution completed.")


"""
================================================
Example Questions for Students:
================================================

1. What does the `.hover()` method do in Playwright?
   - Answer: The `.hover()` method moves the mouse pointer over the specified element, which can trigger hover-based interactions, such as tooltips or changes in the DOM.

2. Why do we use the `click_count=2` in the `.click()` method?
   - Answer: The `click_count=2` argument simulates a double-click on the element, ensuring that it registers two consecutive clicks.

3. What is the purpose of the `expect()` method in Playwright?
   - Answer: The `expect()` method in Playwright is used to make assertions in the test. In this case, it's used to verify that the click count is displayed as expected by checking the text in the `clickCount` span.

4. What happens if an element is hidden or not interactable during a test?
   - Answer: If an element is hidden or not interactable, Playwright will raise a `TimeoutError` or similar error. Proper error handling can be implemented to manage these scenarios.

5. Why is slow motion (`slow_mo=3000`) used when launching the browser?
   - Answer: Slow motion is added to make the execution slower (3 seconds in this case) for better visualization during testing.

6. What is the role of `no_viewport=True` in the browser context?
   - Answer: The `no_viewport=True` setting removes the default viewport size restrictions, allowing the page to open at the default browser window size.

7. What is a "stale element" in automated testing?
   - Answer: A stale element occurs when an element is modified or replaced in the DOM, making a previously captured reference invalid.

================================================
Advanced Questions:
================================================

1. How can you handle cases where an element is not interactable or hidden behind another element?
   - Answer: You can use Playwright's `wait_for()` methods to wait until an element becomes visible or interactable. You can also catch `TimeoutError` exceptions.

2. What changes would you make if you wanted to perform a triple-click instead of a double-click?
   - Answer: You would change the `click_count` argument to `click_count=3` to simulate a triple-click.

3. Explain how Playwright handles DOM changes during the execution of a test.
   - Answer: Playwright automatically waits for elements to be stable and interactable before performing actions. It handles dynamic DOM updates using methods like `.wait_for_selector()` to ensure elements are present.
"""
