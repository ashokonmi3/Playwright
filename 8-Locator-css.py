import time
from playwright.sync_api import sync_playwright


# def css_selectors_example():
#     """
#     Demonstrates how to use CSS selectors in Playwright to locate and interact with web elements.

#     CSS Selectors Examples:
#     - Tag Name: Select elements based on their tag name.
#     - Class Name: Select elements based on their CSS class.
#     - ID: Select elements based on their unique ID.
#     - Attribute Value: Select elements based on specific attribute values.

#     This script:
#     1. Launches a browser and navigates to a webpage.
#     2. Demonstrates various CSS selector methods:
#         - By Tag Name
#         - By Class Name
#         - By ID
#         - By Attribute Value
#     3. Interacts with these elements and performs some actions.
#     4. Closes the browser.
#     #     """
#     with sync_playwright() as playwright:
#         # Launch a browser in non-headless mode with a slow motion delay of 500ms
#         browser = playwright.chromium.launch(
#             headless=False, slow_mo=3000, args=["--start-maximized"])
#         context = browser.new_context(
#             ignore_https_errors=True, no_viewport=True)
#         page = context.new_page()
#         # Visit the website
#         page.goto("https://bootswatch.com/default/")

#         # Wait for 2 seconds before scrolling down
#         time.sleep(2)

#         # Example 1: Select and highlight an element by tag name (h1)
#         # CSS Selector: 'h1' targets all <h1> elements
#         element_by_tag = page.locator('css=h1')
#         element_by_tag.highlight()
#         time.sleep(2)

#         # Scroll down the page by 1000 pixels
#         page.evaluate("window.scrollBy(0, 1000);")
#         time.sleep(2)

#         # Example 2: Select an element by class and highlight it
#         # CSS Selector: '.btn-outline-success' targets elements with the class 'btn-outline-success'
#         element_by_class = page.locator(
#             'button.btn-outline-success')  # Success button (3rd row)
#         element_by_class.highlight()
#         time.sleep(2)

#         # Click the button with class 'btn-outline-success'
#         element_by_class.click()
#         time.sleep(2)

#         # Example 3: Select an element by ID and click it
#         # CSS Selector: '#btnGroupDrop1' targets the element with ID 'btnGroupDrop1'
#         # Button by ID , DROPDOWN next to Primary
#         element_by_id = page.locator('button#btnGroupDrop1')
#         element_by_id.click()
#         time.sleep(2)

#         # Scroll down again by 1000 pixels
#         page.evaluate("window.scrollBy(0, 2000);")
#         time.sleep(2)

#         # Example 4: Select an input element with the 'readonly' attribute and highlight it
#         # CSS Selector: 'input[readonly]' targets input elements with the 'readonly' attribute
#         # email@example.com
#         element_by_tag = page.locator('input[readonly]')
#         element_by_tag.highlight()
#         time.sleep(2)

#         # Example 5: Select an input element by attribute value and highlight it
#         # CSS Selector: "input[value='correct value']" targets input elements with the value 'correct value'
#         element_by_attr = page.locator("input[value='correct value']")
#         element_by_attr.highlight()
#         time.sleep(2)

#         # Close the browser
#         browser.close()

# if __name__ == "__main__":
#     css_selectors_example()

# ==============================
# from playwright.sync_api import sync_playwright
# import time


def parent_child_selectors_example():
    """
    Demonstrates how to use parent and child CSS selectors in Playwright to locate and interact with web elements.

    CSS Selectors Examples:
    - Parent and Child: Selects elements based on their hierarchical relationship.

    This script:
    1. Launches a browser and navigates to a webpage.
    2. Demonstrates selecting elements using parent and child CSS selectors.
    3. Highlights selected elements to visualize them.
    4. Closes the browser.
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

        # Wait for 2 seconds before scrolling down
        time.sleep(2)

        # Example 1: Select and highlight an element by tag name (h1)
        # CSS Selector: 'h1' targets all <h1> elements
        element_by_tag = page.locator('css=h1')
        element_by_tag.highlight()
        time.sleep(2)

        # Example 2: Select a child element within a specific parent element
        # CSS Selector: 'nav.bg-dark a.nav-link.active' targets <a> elements with class 'nav-link active' within a <nav> with class 'bg-dark'
        element_by_parent_child = page.locator(
            'nav.bg-dark a.nav-link.active')  # home link
        element_by_parent_child.highlight()
        time.sleep(2)

        # Close the browser
        browser.close()


if __name__ == "__main__":
    parent_child_selectors_example()
