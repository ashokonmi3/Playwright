import time
from playwright.sync_api import sync_playwright


# def test_input_fields():
#     """
#     A label is typically a separate HTML element that describes or identifies an input field.
#     The label is usually placed before, after, or above the input field and is visible outside of 
#    the input, not inside it.
#     Demonstrates how to use Playwright's `get_by_label` locator to:
#     1. Launch a Chromium-based browser.
#     2. Navigate to a specified website.
#     3. Scroll down the page to ensure visibility of input fields.
#     4. Locate input fields by their labels.
#     5. Highlight each input field for visual confirmation.
#     6. Close the browser after the test.

#     This example uses Playwright's synchronous API.
#     """
#     # Initialize Playwright
#     with sync_playwright() as playwright:
#         # Launch a Chromium-based browser instance
#         browser = playwright.chromium.launch(
#             headless=False, slow_mo=3000, args=["--start-maximized"]
#         )

#         context = browser.new_context(
#             ignore_https_errors=True, no_viewport=True)
#         page = context.new_page()

#         # Navigate to the specified website
#         page.goto("https://bootswatch.com/default/")

#         # Scroll down the page by 3000 pixels to ensure visibility of input fields
#         page.evaluate("window.scrollBy(0, 3000);")

#         # Locate the email input field by its label
#         email_input = page.get_by_label("Email address")
#         # Highlight the located email input field for visual confirmation
#         email_input.highlight()
#         # Wait for 5 seconds to observe the highlighted email input field
#         time.sleep(5)

#         # Locate the select dropdown by its label
#         example_select = page.get_by_label("Example select")
#         # Highlight the located dropdown for visual confirmation
#         example_select.highlight()
#         time.sleep(5)  # Wait for 5 seconds to observe the highlighted dropdown

#         # Locate the password field by its label (if present on the page)
#         password_input = page.get_by_label("Password", strict=False)
#         if password_input:
#             password_input.highlight()
#             time.sleep(5)

#         # Close the browser to end the session
#         browser.close()


# # Execute the test function if the script is run directly
# if __name__ == "__main__":
#     test_input_fields()

# ====================================
# Placeholder-based Example
# A placeholder in HTML is an attribute of input fields that provides a short hint or description to the user about what they are expected to enter in the field.
#  This hint is displayed inside the input field as a light, gray text that disappears once the user starts typing.
# <input type = "text" placeholder = "Enter your email" >

def test_input_field_highlight():
    """
    Demonstrates how to interact with input fields using placeholders in Playwright.
    This script performs the following actions:
    1. Launches a Chromium-based browser.
    2. Opens a new page and navigates to the specified URL.
    3. Sets the viewport size.
    4. Scrolls down the page.
    5. Locates input fields by their placeholder text.
    6. Highlights the located input fields for demonstration.
    7. Closes the browser.
    """
    with sync_playwright() as playwright:
        # Launch a Chromium-based browser with headless mode disabled
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )

        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True)
        page = context.new_page()

        # Navigate to the specified URL
        page.goto("https://bootswatch.com/default/")

        # Set the viewport size to 1920x1080 pixels

        # Scroll down by 3000 pixels for visibility of elements
        page.evaluate("window.scrollBy(0, 3000);")

        # Locate the input field with the placeholder text "Email address"
        email_input = page.get_by_placeholder("Enter email")
        # Highlight the email input field
        email_input.highlight()
        # Pause for 5 seconds to visually verify the highlighted input field
        time.sleep(5)

        # Locate the input field with the placeholder text "Password"
        password_input = page.get_by_placeholder("Password")
        # Highlight the password input field
        password_input.highlight()
        time.sleep(5)

        # Close the browser
        browser.close()


if __name__ == "__main__":
    test_input_field_highlight()
