from playwright.sync_api import sync_playwright, expect, TimeoutError

# Playwright indeed provides an auto-waiting mechanism, which automatically waits for actions like clicking, typing, and navigating until the target element is ready(visible, enabled, etc.) before executing. However, there are still situations where using wait_for() or related manual wait functions is necessary.
# Sometimes, you need to wait for specific conditions that Playwright’s auto-waiting doesn't handle automatically, such as waiting for an element's content to update, for a network request to complete, or for data to appear after a delay.
# Dynamic Content: In cases where content dynamically loads or changes after the page appears to be ready, you may need to use wait_for() to pause the script until certain conditions are met.
# Playwright’s auto-wait applies to actions like click(), fill(), type(), and goto()—actions that inherently expect the page or element to be in a certain state(e.g., visible, enabled).
# For non-action-based checks(like waiting for an element to disappear or an element's text to change), you need manual waiting functions.


def test_load_delay(page):
    """
    Test Case: Handling delayed elements in Playwright

    This test demonstrates how to handle elements that take time to load on a page, 
    such as buttons that appear after a delay. It waits for an element to become visible 
    before interacting with it.

    Steps:
    1. Navigate to a page where an element takes time to load.
    2. Wait for the delayed button to appear.
    3. Verify that the button is visible.
    4. Perform actions on the button if necessary.
    """

    # Navigate to the base page
    page.goto("http://uitestingplayground.com/")

    # Find the link to the 'Load Delay' page and click it
    load_delay_link = page.get_by_role("link", name="Load Delay")
    load_delay_link.click()

    # Find the button that appears after a delay
    btn = page.get_by_role("button", name="Button Appearing After Delay")

    # Wait for the button to be available and visible
    btn.wait_for()

    # Assert that the button is visible
    expect(btn).to_be_visible()

    # Perform actions on the button if needed (like clicking it)
    btn.click()


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for handling delayed elements.
    """

    # Launch the Chromium browser with slow motion for visibility
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()

    # Run the test case on the page
    test_load_delay(page)

    # Close the browser after the test completes
    browser.close()

    """
    Important Notes for Learning:
    - **Delayed Elements**: This test demonstrates how to handle elements that may take time to load.
    - **Waiting for Elements**: Playwright's `wait_for` ensures the element is fully loaded before interaction.
    - **Assertions**: The `expect` API is used to confirm that the button is visible, making your test stable.
    """
