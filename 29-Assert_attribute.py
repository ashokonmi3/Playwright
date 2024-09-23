import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

# Entry point for running Playwright in a synchronous mode
with sync_playwright() as playwright:
    """
    Test case demonstrating various `expect` API assertions in Playwright:
    - Verifying exact class names
    - Using regular expressions to validate partial class names
    - Checking for the presence of attributes and their values in web elements
    """

    # 1. Launch the Chromium browser (non-headless for visibility)
    browser = playwright.chromium.launch(headless=False)

    # 2. Create a new page instance (new browser tab)
    page = browser.new_page()

    # 3. Navigate to the Playwright Python documentation page
    page.goto("https://playwright.dev/python")

    # 4. Locate the 'Docs' link element by its role and name
    docs_link = page.get_by_role("link", name="Docs")

    # 5. Assertion: Check if the 'Docs' link has the exact class value
    # Using the `expect` assertion from Playwright to ensure the link has the exact class names
    expect(docs_link).to_have_class("navbar__item navbar__link")
    print("Verified that the 'Docs' link has the exact class: 'navbar__item navbar__link'.")

    # 6. Assertion: Use regular expression to check if the 'Docs' link class contains a partial class value
    # This checks if any class value contains "navbar__link", even if there are other classes present
    expect(docs_link).to_have_class(re.compile(r"navbar__link"))
    print("Verified that the 'Docs' link class contains 'navbar__link' using regex.")

    # 7. Assertion: Check if the 'href' attribute has a specific value
    # Here, we assert the 'href' attribute value is exactly '/python/docs/intro'
    expect(docs_link).to_have_attribute("href", "/python/docs/intro")
    print("Verified that the 'Docs' link has the correct href attribute value: '/python/docs/intro'.")

    # After the tests, close the browser to free up resources
    browser.close()

# The script demonstrates how to use Playwright's `expect` API to perform various checks:
# 1. Exact class match using `to_have_class`
# 2. Partial class match using a regular expression
# 3. Checking for attributes like 'href'
# 4. Validating the attribute value
