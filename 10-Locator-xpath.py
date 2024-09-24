import time
from playwright.sync_api import sync_playwright

import time
from playwright.sync_api import sync_playwright


# def test_xpath_selectors():
#     """
#     Demonstrates the use of XPath selectors with Playwright to locate and interact with elements on a webpage.

#     XPath Notes:
#     -------------
#     XPath (XML Path Language) is used to navigate through elements and attributes in an XML document.
#     In Playwright, XPath can be used to locate elements in the DOM based on their structure or attributes.

#     Basic XPath Examples:
#     - `xpath=//tagName`: Selects all elements with the specified tag name in the document.
#     - `xpath=//input[@readonly]`: Selects all <input> elements with the 'readonly' attribute.
#     - `xpath=//input[@value="correct value"]`: Selects all <input> elements with a specific 'value' attribute.
#     - `xpath=//*[text()='Example Text']`: Selects elements with specific text content.

#     Workflow:
#     -------------
#     1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
#     2. Creates a new page and navigates to "https://bootswatch.com/default/".
#     3. Sets the viewport size to 1920x1080 pixels.
#     4. Waits for 2 seconds to ensure the page is fully loaded.
#     5. Selects and highlights elements using various XPath selectors.
#     6. Scrolls down the page to make more elements visible.
#     7. Closes the browser.

#     Examples:
#     -------------
#     - Example 1: Select and highlight an <h1> element by tag name.
#     - Example 2: Select and highlight an <input> element with the 'readonly' attribute.
#     - Example 3: Select and highlight an <input> element with a specific value (note: the value used in the example may not match any existing elements).
#     """
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(
#             headless=False, slow_mo=3000, args=["--start-maximized"])
#         context = browser.new_context(
#             ignore_https_errors=True, no_viewport=True)
#         page = context.new_page()

#         # Visit the website
#         page.goto("https://bootswatch.com/default/")

#         # Set the viewport size

#         # Wait for 2 seconds before performing actions
#         time.sleep(2)

#         # Example 1: Select and highlight an <h1> element by tag name
#         element_by_tag = page.locator('xpath=//h1')
#         element_by_tag.highlight()
#         time.sleep(2)
#         page.evaluate("window.scrollBy(0, 3000);")

#         # Example 2: Select and highlight an <input> element with the 'readonly' attribute
#         element_by_readonly = page.locator('xpath=//input[@readonly]')
#         element_by_readonly.highlight()
#         time.sleep(2)

#         # Example 3: Select and highlight an <input> element with a specific value (note: the value used in the example may not match any existing elements)
#         element_by_value = page.locator('xpath=//input[@value="wrong value"]')
#         element_by_value.highlight()
#         time.sleep(2)

#         # Close the browser
#         browser.close()


# # Execute the function
# test_xpath_selectors()

# =====================

import time
from playwright.sync_api import sync_playwright


def test_xpath_selectors():
    """
    Demonstrates how to use XPath selectors with Playwright to locate and interact with elements on a webpage.

    XPath Notes:
    -------------
    XPath (XML Path Language) is used to navigate through elements and attributes in an XML document.
    In Playwright, XPath can be used to locate elements in the DOM based on their structure or attributes.

    Basic XPath Examples:
    - `xpath=//h1[text()='Heading 1']`: Selects <h1> elements with exact text "Heading 1".
    - `xpath=//h1[contains(text(),'Head')]`: Selects <h1> elements containing the text "Head".
    - `xpath=//button[contains(@class,'btn-outline-primary')]`: Selects <button> elements with class name containing 'btn-outline-primary'.
    - `xpath=//input[contains(@value,'correct')]`: Selects <input> elements where the 'value' attribute contains 'correct'.

    Workflow:
    -------------
    1. Launches a browser in non-headless mode with a slow motion delay.
    2. Creates a new page and navigates to "https://bootswatch.com/default/".
    3. Sets the viewport size to 1920x1080 pixels.
    4. Waits for 2 seconds to ensure the page is fully loaded.
    5. Selects and highlights elements based on various XPath selectors.
    6. Scrolls the page down to make more elements visible.
    7. Closes the browser.
    """
    with sync_playwright() as playwright:
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

        # Example 1: Select and highlight an <h1> element with exact text "Heading 1"
        element_by_tag = page.locator("//h1[text()='Heading 1']")
        element_by_tag.highlight()
        time.sleep(2)

        # Example 2: Select and highlight an <h1> element that contains the text "Head"
        element_by_tag = page.locator("//h1[contains(text(),'Head')]")
        element_by_tag.highlight()
        time.sleep(2)

        # Example 3: Select and highlight a <button> element with class containing 'btn-outline-primary'
        element_by_tag = page.locator(
            "//button[contains(@class,'btn-outline-primary')]")
        element_by_tag.highlight()
        time.sleep(2)

        # Scroll down the page to make more elements visible
        page.evaluate("window.scrollBy(0, 3000);")

        # Example 4: Select and highlight an <input> element where the 'value' attribute contains 'correct'
        element_by_tag = page.locator("//input[contains(@value,'correct')]")
        element_by_tag.highlight()
        time.sleep(2)

        # Close the browser
        browser.close()


# Execute the function
test_xpath_selectors()
