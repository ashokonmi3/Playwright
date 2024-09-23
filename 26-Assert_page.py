import time
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

DOCS_URL = "https://playwright.dev/python/docs/intro"

# 1. assert API (Python Built-in Assertion)
# Purpose: assert is a built-in Python statement used to check if a given condition is True.
# If the condition is False, it raises an AssertionError and stops the execution of the test.
# Usage: It is used in general programming to check the validity of a condition or a value, not specific to Playwright.
# Example:
# value = page.locator("input#price").input_value()
# assert float(value) > 1000, f"Expected price to be greater than 1000, but got {value}"
# In the example above, if the value is not greater than 1000, the assert statement will raise an AssertionError, and the test will fail.
#
# Behavior:
# Immediate failure: If the condition in the assert statement fails, the test will fail immediately and stop further execution.
# Simple and synchronous: assert is a simple, synchronous operation with no built-in retry mechanism or timeout.
# 2. expect API (Playwright Assertion)
# Purpose: expect is part of Playwright's testing library and is used specifically for making assertions
# on the behavior and state of web elements. It is designed to handle conditions like waiting for elements
# to become visible, have specific text, or meet other conditions.
# Usage: It is used to assert conditions in a more dynamic and asynchronous way, especially when dealing
# with UI elements that might change state (e.g., loading, visibility) over time.
# Example:
# from playwright.sync_api import expect
# expect(page.locator("button#submit")).to_be_visible()
# In this example, Playwright will wait for the #submit button to become visible before passing the test.
# If the button doesn't become visible within the default timeout (usually 30 seconds), the test will fail.
#
# Behavior:
# Wait and retry mechanism: The expect API is built for UI testing, so it automatically waits for certain
# conditions to be met. It retries the condition for a specific duration (default is 30 seconds), allowing
# time for elements to load, appear, or change state.
# Asynchronous: Playwright's expect assertions are non-blocking and are well-suited for modern web applications
# where UI elements often load asynchronously.
# Specific to Playwright: The expect API is tailored for browser-based tests and offers various assertions
# to check the state of elements, like visibility, text content, attributes, etc.


def test_get_started_link():
    """
    Test case to verify that clicking the 'GET STARTED' link on the Playwright Python page
    navigates to the correct documentation page. It demonstrates the usage of both assert 
    and expect APIs for assertions.

    Steps:
    - Launches the browser and opens the Playwright Python homepage.
    - Locates the 'GET STARTED' link using a role-based locator.
    - Clicks the link and verifies the page's URL and title using both assert and expect APIs.
    """

    # Using sync_playwright to handle browser launch and automation tasks
    with sync_playwright() as playwright:
        # Launch the browser in non-headless mode to visualize actions
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to Playwright Python home page
        page.goto("https://playwright.dev/python")
        time.sleep(2)

        # Locate the 'GET STARTED' link by role and click it
        link = page.get_by_role("link", name="GET STARTED")
        link.click()
        time.sleep(2)
        print("Next validation is assertion of page")

        assert page.url == "playwright"

        # Check if the page URL matches the expected documentation URL
        assert page.url == DOCS_URL, f"Expected URL {
            DOCS_URL}, but got {page.url}"

        # Expect API: This automatically waits for the URL to change
        expect(page).to_have_url("playwright")
        print("Next validation is title of page")
        # Expect API: Verifies that the page title matches the expected value
        expect(page).to_have_title("Installation | Playwright Python")
        time.sleep(2)


test_get_started_link()

# Key Differences Between `assert` and `expect`:

# | Feature                | assert (Python)                            | expect (Playwright)                                  |
# |------------------------|--------------------------------------------|------------------------------------------------------|
# | Use Case               | General programming conditions             | Browser or web element-related conditions            |
# | Scope                  | Any condition in Python                    | Web page or browser-specific conditions              |
# | Retries/Timeouts       | No retry, fails immediately if False       | Automatically retries until timeout (default 30s)    |
# | Asynchronous Support   | No, synchronous                            | Yes, designed for async UI changes                   |
# | Custom Error Messages  | Can be defined in assert                   | Built-in detailed error messages                     |
# | Example Use            | assert value > 1000                        | expect(page.locator("button")).to_be_visible()       |
# | Error Handling         | Raises AssertionError immediately          | Waits for conditions to be met or timeouts           |

# When to Use:
# Use assert: When you want to check simple, immediate conditions that don’t depend on the state of a web page or browser.
# It's ideal for checking values, types, or performing simple condition checks in your Python code.

# Use expect: When you need to assert conditions related to web elements, such as visibility, text content, or attributes.
# It is specifically built for web automation and includes retry mechanisms, timeouts, and handling of dynamic content changes in modern web applications.
