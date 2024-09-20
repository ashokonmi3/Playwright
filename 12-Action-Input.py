import time
from playwright.sync_api import sync_playwright


def test_input_fields():
    """
    Demonstrates how to interact with input fields using Playwright.

    Input Field Interaction Notes:
    ------------------------------
    In Playwright, you can perform various actions on input fields, such as:
    - `fill`: Sets the value of an input field, clearing any existing value.
    - `type`: Types text into an input field, simulating user keystrokes.
    - `clear`: Clears the value of an input field.
    - `input_value`: Retrieves the current value of an input field.

    Basic Actions:
    --------------
    - `element.fill("value")`: Sets the input field's value to "value", clearing any existing value.
    - `element.type("value")`: Types "value" into the input field, with optional delay between keystrokes.
    - `element.clear()`: Clears the current value of the input field.
    - `element.input_value()`: Retrieves the current value from the input field.

    Workflow:
    ----------
    1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
    2. Creates a new page and navigates to "https://bootswatch.com/default/".
    3. Sets the viewport size to 1920x1080 pixels.
    4. Waits for 2 seconds to ensure the page is fully loaded.
    5. Selects an input field using various locator strategies.
    6. Performs actions such as filling, typing, and clearing values in the input field.
    7. Retrieves and prints the value of an input field.
    8. Closes the browser.

    Examples:
    ----------
    - Example 1: Fill an input field identified by placeholder text and perform various actions (fill, type, clear).
    - Example 2: Retrieve and print the value from an input field identified by label.
    """

    with sync_playwright() as playwright:
        # Launch a browser in non-headless mode with a slow motion delay of 3000ms
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True)
        page = context.new_page()

        # Visit the website
        page.goto("https://bootswatch.com/default/")

        # Wait for 2 seconds before performing actions
        time.sleep(2)

        # Example 1: Interact with an input field by placeholder text
        # Locate the input field using placeholder text and perform various actions
        element_by_placeholder = page.get_by_placeholder("Enter email")
        element_by_placeholder.highlight()
        element_by_placeholder.scroll_into_view_if_needed()

        # Fill the input field with a value, clearing any existing value
        element_by_placeholder.fill("ashokonmi@gmail.com")
        time.sleep(2)

        # Clear the input field
        element_by_placeholder.clear()
        time.sleep(2)

        # Type into the input field with simulated keystrokes
        element_by_placeholder.type("ashokonmi@gmail.com")
        time.sleep(2)

        # Clear the input field again
        element_by_placeholder.clear()
        time.sleep(2)

        # Type into the input field with a delay between keystrokes
        element_by_placeholder.type(
            "ashokonmi@gmail.com", delay=200)  # delay in milliseconds
        time.sleep(2)

        # Clear the input field one more time
        element_by_placeholder.clear()

        # Example 2: Retrieve and print the value from an input field by label
        element_by_label = page.get_by_label(
            "Valid input").first  # 2 elements are there
        element_by_label.highlight()

        # Retrieve and print the current value of the input field
        valid_input_value = element_by_label.input_value()
        print("Current value of the input field:", valid_input_value)

        # Close the browser
        browser.close()


# Execute the function
test_input_fields()
