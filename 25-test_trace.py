from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import sync_playwright


# screenshots:

# Type: bool
# Default: False
# Description: This parameter indicates whether to capture screenshots at every step of the tracing.
# Purpose: When set to True, it records screenshots of the page as it changes, which can be helpful for visual debugging. You can see exactly what the page looked like at various points during the test.

# Define the URL you expect after clicking the "GET STARTED" link
DOCS_URL = "https://playwright.dev/python/docs/intro"


# def main():
#     with sync_playwright() as playwright:
#         # Launch a Chromium-based browser instance
#         browser = playwright.chromium.launch(headless=False)

#         # Create a new browser context and page
#         context = browser.new_context()
#         page = context.new_page()

#         # Start tracing for the current context
#         context.tracing.start(
#             name="playwright",
#             screenshots=True,
#             snapshots=True,
#             sources=True,
#         )

#         # Navigate to the specified website
#         page.goto("https://playwright.dev/python")

#         # Locate the link with the role "link" and name "GET STARTED", then click it
#         link = page.get_by_role("link", name="GET STARTED")
#         link.click()

#         # Assert that the URL is the expected URL after clicking the link
#         if page.url == DOCS_URL:
#             print("Navigation successful. The URL is correct.")
#         else:
#             print(f"Navigation failed. Current URL: {page.url}")

#         # Stop tracing and save it to a file
#         context.tracing.stop(path="trace333.zip")

#         # Close the browser
#         browser.close()


# # Run the main function
# if __name__ == "__main__":
#     main()

# Traces can be viewed in
# https: //trace.playwright.dev/


def test_successful_login(page):
    """
    Test Successful Login.

    Scenario:
    This test verifies that a user can successfully log in with the correct username and password.

    Steps:
    1. Navigate to the sample app login page.
    2. Fill in the username and password fields.
    3. Click the 'Log In' button.
    4. Verify that the correct welcome message is displayed.

    Expected Outcome:
    - The page should display "Welcome, [username]!" upon successful login.
    """
    print("Starting test: Successful Login...")
    page.goto("http://uitestingplayground.com/sampleapp")

    # Credentials
    username = "dan"
    password = "pwd"

    # Locate input fields and button
    username_input = page.get_by_placeholder("User Name")
    password_input = page.get_by_placeholder("********")
    login_btn = page.get_by_role("button", name="Log In")

    # Fill inputs and click login
    print(f"Filling in username: {username} and password.")
    username_input.fill(username)
    password_input.fill(password)

    print("Clicking the 'Log In' button...")
    login_btn.click()

    # Verify successful login
    label = page.locator("label#loginstatus")
    print("Verifying the welcome message...")
    expect(label).to_have_text(f"Welcome, {username}!")

    print("Successful login test completed.")


def test_failed_login(page):
    """
    Test Failed Login.

    Scenario:
    This test verifies that an incorrect username or password results in an error message.

    Steps:
    1. Navigate to the sample app login page.
    2. Fill in the incorrect username and password fields.
    3. Click the 'Log In' button.
    4. Verify that the error message is displayed.

    Expected Outcome:
    - The page should display "Invalid username/password" upon failed login.
    """
    print("Starting test: Failed Login...")
    page.goto("http://uitestingplayground.com/sampleapp")

    # Incorrect credentials
    username = "dan"
    password = "cnasdjc"

    # Locate input fields and button
    username_input = page.get_by_placeholder("User Name")
    password_input = page.get_by_placeholder("********")
    login_btn = page.get_by_role("button", name="Log In")

    # Fill inputs and click login
    print(f"Filling in username: {username} and incorrect password.")
    username_input.fill(username)
    password_input.fill(password)

    print("Clicking the 'Log In' button...")
    login_btn.click()

    # Verify failed login message
    label = page.locator("label#loginstatus")
    print("Verifying the error message...")
    expect(label).to_have_text("Invalid username/password")

    print("Failed login test completed.")


# Use Playwright to execute the test cases
with sync_playwright() as playwright:
    """
    Executes test scenarios for verifying login functionality (both successful and failed cases).
    """

    print("Launching the browser with slow motion for better visualization...")
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    print("Creating a new browser context and opening a new page...")
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    page = context.new_page()

    # Run the test cases
    print("Running the successful login test case...")
    test_successful_login(page)

    print("Running the failed login test case...")
    test_failed_login(page)

    # Close the browser after all tests
    print("Closing the browser...")
    context.tracing.stop(path="trace_complex.zip")

    browser.close()

    print("All test cases executed successfully.")
