from playwright.sync_api import sync_playwright


def test_auto_waiting():
    """
    Demonstrates how Playwright automatically waits for elements to be ready before interacting with them.

    Auto-Waiting Notes:
    -------------------
    Playwright automatically waits for the following:
    - Element to be attached to the DOM.
    - Element to be visible.
    - Element to be enabled.
    - Element to stop moving or receiving animations.(stable)
    - For clickable elements, it waits for the element to receive pointer events.The element should be clickable stable visible

    Workflow:
    ----------
    1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
    2. Creates a new page and navigates to a page with a dropdown element.
    3. Demonstrates Playwright's auto-waiting mechanism by interacting with an element without manually adding wait time.
    4. Closes the browser.

    Examples:
    ----------
    - Example 1: Click on a dropdown element and interact without manual delays.
    """
    with sync_playwright() as playwright:
        # Launch a browser in non-headless mode with a slow motion delay of 500ms
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True
        )
        page = context.new_page()

        # Visit the target website
        page.goto("https://bootswatch.com/default/")

        # Playwright will automatically wait for the element to be visible and clickable
        # Here, we click on the first dropdown item without manual wait
        dropdown_item = page.locator("a.dropdown-item").first
        # this is the element in Theme--> Default its not visible in the main page so playwright
        # will wait for default 30 seconds and than throw exception
        # dropdown_item.click(force=True)  # no waiting here
        # we can change the timeout here 2 second
        dropdown_item.click(timeout=2000)

       # As an example, wait for the dropdown item to be clickable (auto-waiting applied by Playwright)
        # dropdown_item.click()

        # Close the browser
        browser.close()


# Execute the function
test_auto_waiting()

# Logs will show
# waiting for locator("a.dropdown-item").first
# -   locator resolved to < a href = "../default/" class = "dropdown-item" > Default < /a >
# - attempting click action
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 1
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 2
# -   waiting 20ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 3
# -   waiting 100ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 4
# -   waiting 100ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 5
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 6
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 7
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 8
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 9
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 10
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 11
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 12
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 13
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 14
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 15
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 16
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 17
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 18
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 19
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 20
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 21
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 22
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 23
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 24
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 25
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 26
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 27
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 28
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 29
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 30
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 31
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 32
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 33
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 34
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 35
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 36
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 37
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 38
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 39
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 40
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 41
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 42
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 43
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 44
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 45
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 46
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 47
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 48
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 49
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 50
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 51
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 52
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 53
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 54
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 55
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 56
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 57
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 58
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 59
# -   waiting 500ms
# -   waiting for element to be visible, enabled and stable
# -   element is not visible
# - retrying click action, attempt  # 60
# -   waiting 500ms
