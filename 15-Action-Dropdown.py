import time
from playwright.sync_api import sync_playwright


def test_select_options():
    """
    Demonstrates how to interact with select dropdowns using Playwright.

    Select Option Interaction Notes:
    ---------------------------------
    In Playwright, you can perform various actions on select dropdowns, such as:
    - `select_option`: Selects an option from a dropdown menu by its value, label, or index.
    - `multiple selection`: Handles selecting multiple options from a multi-select dropdown.

    Basic Actions:
    --------------
    - `element.select_option(value)`: Selects an option from the dropdown by its value attribute.
    - `element.select_option([value1, value2, ...])`: Selects multiple options from a multi-select dropdown.

    Workflow:
    ----------
    1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
    2. Creates a new page and navigates to "https://bootswatch.com/default/".
    3. Sets the viewport size to 1920x1080 pixels.
    4. Waits for 2 seconds to ensure the page is fully loaded.
    5. Scrolls down the page to make sure the dropdowns are visible.
    6. Selects options from a single-select dropdown and a multi-select dropdown.
    7. Closes the browser.

    Examples:
    ----------
    - Example 1: Select options from a single-select dropdown.
    - Example 2: Select multiple options from a multi-select dropdown.
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

        # Visit the website
        page.goto("https://bootswatch.com/default/")

        # Set the viewport size

        # Wait for 2 seconds to ensure the page is fully loaded
        time.sleep(2)

        # Example 1: Interact with a single-select dropdown
        # Locate the single-select dropdown by its label and select options
        dropdown = page.locator("button#btnGroupDrop1")
        dropdown.scroll_into_view_if_needed()
        dropdown.click()
        time.sleep(2)

        # this will highlight all
        # single_select = page.locator("div.dropdown-menu")
        # single_select.highlight()
        # time.sleep(2)
        # print('here')

        single_select = page.locator("div.dropdown-menu:visible")
        single_select.highlight()
        time.sleep(2)
        print('there')

        page.locator(
            "div.dropdown-menu:visible a:text('Dropdown link')").last.highlight()
        # single_select.click()
        time.sleep(5)

        # Close the browser
        browser.close()


# Execute the function
test_select_options()
