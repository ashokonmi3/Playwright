import time
from playwright.sync_api import sync_playwright


def test_xpath_selectors():
    """
    Demonstrates the use of various locators with Playwright to locate and interact with elements on a webpage.

    Locator Notes:
    ---------------
    Playwright provides several methods to locate elements on a webpage. These include:
    - `get_by_role`: Locates elements based on their ARIA role and accessible name.
    - `locator`: Provides a way to locate elements using CSS selectors or XPath.
    - `nth`: Selects an element based on its index in the list of matched elements.
    - `filter`: Filters a set of elements to match additional criteria.
    - `has_text`: Filters elements based on their visible text content.
    - `visible=true/false`: Filters elements based on their visibility status.
    - `get_by_label`: Locates form elements by their associated label.

    Basic Locator Examples:
    - `page.get_by_role('button', name="Primary")`: Selects a button element with the accessible name "Primary".
    - `page.locator('button').locator('nth=0')`: Selects the first button element on the page.
    - `page.get_by_role('Email address')`: Locates an element by its accessible name (e.g., label of an email input field).
    - `page.locator('div.dropdown-menu')`: Selects a <div> element with the class 'dropdown-menu'.

    Workflow:
    -------------
    1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
    2. Creates a new page and navigates to "https://bootswatch.com/default/".
    3. Sets the viewport size to 1920x1080 pixels.
    4. Waits for 2 seconds to ensure the page is fully loaded.
    5. Selects and highlights elements using various locator strategies.
    6. Scrolls down the page to make more elements visible.
    7. Closes the browser.

    Examples:
    -------------
    - Example 1: Select and highlight a button element with the accessible name "Primary".
    - Example 2: Select and highlight elements based on their visibility and label.
    - Example 3: Use advanced filtering to select elements with specific attributes or text content.
    """
    with sync_playwright() as playwright:
        # Launch a browser in non-headless mode with a slow motion delay of 500ms
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"])
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True)
        page = context.new_page()

        # Visit the website
        page.goto("https://bootswatch.com/default/")

        # Set the viewport size

        # Wait for 2 seconds before performing actions
        time.sleep(2)

        # Example 1: Select and highlight a button element with the accessible name "Primary"
        # all button with name primary will be highlighted
        element_by_tag = page.get_by_role('button', name="Primary")
        element_by_tag.highlight()
        time.sleep(2)

        # Highlight various buttons using nth index
        element_by_tag = page.get_by_role(
            'button', name="Primary").locator("nth=1")
        element_by_tag.highlight()
        time.sleep(2)

        element_by_tag = page.get_by_role(
            'button', name="Primary").locator("nth=0")
        element_by_tag.highlight()
        time.sleep(2)

        element_by_tag = page.get_by_role(
            'button', name="Primary").locator("nth=2")
        element_by_tag.highlight()
        time.sleep(2)

        # Scroll down the page to make more elements visible

        # Example 2: Select and highlight elements with specific attributes or text
        # Highlight an element by role and accessible name
        element_by_readonly = page.get_by_label('Example select')
        # element_by_readonly.scroll_into_view_if_needed()
        element_by_readonly.highlight()
        element_by_readonly.scroll_into_view_if_needed()

        time.sleep(2)

        # # Locate element by role and navigate to parent element
        element_by_readonly = page.get_by_label('Example select').locator(
            "..")  # Highlight the parent element containing this element
        element_by_readonly.highlight()
        element_by_readonly.scroll_into_view_if_needed()

        time.sleep(2)

        # # Highlight heading elements
        element_by_readonly = page.get_by_role("heading")
        element_by_readonly.highlight()
        time.sleep(2)

        # # Filter headings with specific text
        element_by_readonly = page.get_by_role(
            "heading").filter(has_text="Heading 2")
        element_by_readonly.highlight()
        element_by_readonly.scroll_into_view_if_needed()

        time.sleep(2)

        # Close the browser
        browser.close()


# Execute the function
test_xpath_selectors()
