import time
from playwright.sync_api import sync_playwright


def test_radio_and_checkbox():
    """
    Demonstrates how to interact with radio buttons and checkboxes using Playwright.

    Radio Button and Checkbox Interaction Notes:
    ---------------------------------------------
    In Playwright, you can perform various actions on radio buttons and checkboxes, such as:
    - `check`: Selects a checkbox or radio button.
    - `uncheck`: Deselects a checkbox.
    - `is_checked`: Checks if a checkbox is selected.
    - `click`: Clicks on an element, which can also be used to select radio buttons.

    Basic Actions:
    --------------
    - `element.check()`: Selects the checkbox or radio button.
    - `element.uncheck()`: Deselects the checkbox.
    - `element.is_checked()`: Retrieves the checked status of the checkbox.
    - `element.click()`: Simulates a click on the element.

    Workflow:
    ----------
    1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
    2. Creates a new page and navigates to "https://bootswatch.com/default/".
    3. Sets the viewport size to 1920x1080 pixels.
    4. Waits for 2 seconds to ensure the page is fully loaded.
    5. Scrolls down the page to make sure the radio buttons and checkboxes are visible.
    6. Selects and interacts with radio buttons and checkboxes using various actions.
    7. Retrieves and prints the checked status of checkboxes.
    8. Closes the browser.

    Examples:
    ----------
    - Example 1: Check and uncheck checkboxes and verify their state.
    - Example 2: Select and deselect radio buttons.
    """

    # Step 1: Launch the browser in non-headless mode with slow motion
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True
        )
        page = context.new_page()

        # Step 2: Navigate to the website
        page.goto("https://bootswatch.com/default/")

        # Step 3: Wait for 2 seconds before interacting with elements
        time.sleep(2)

        # Example 1: Interact with checkboxes
        # -----------------------------------
        # Locate the checkbox using its label
        radiobutton1 = page.get_by_label(
            "Option two can be something else and selecting it will deselect option one"
        )
        # Scroll to ensure the checkbox is visible
        radiobutton1.scroll_into_view_if_needed()

        # Check the checkbox
        radiobutton1.check()
        time.sleep(2)  # Add delay for clarity during teaching

        # Interact with another checkbox
        radiobutton2 = page.get_by_label(
            "Option one is this and that—be sure to include why it's great"
        )
        radiobutton2.check()
        time.sleep(2)

        # Example 2: Check the state of a checkbox
        # -----------------------------------------
        # Locate another checkbox
        checkbox3 = page.get_by_label("Default checkbox")
        checkbox3.check()  # Check it first
        time.sleep(2)

        # Print whether the checkbox is checked
        print("Is 'Default checkbox' checked?:", checkbox3.is_checked())

        # Uncheck the checkbox and check the state again
        checkbox3.uncheck()
        time.sleep(2)
        print("Is 'Default checkbox' checked after unchecking?:",
              checkbox3.is_checked())

        # Example 3: Interact with radio buttons
        # --------------------------------------
        # Locate and check a radio button
        radio1 = page.get_by_label("Default switch checkbox input")
        radio1.check()
        time.sleep(2)

        # Close the browser after interaction
        browser.close()


# Execute the function to run the example
test_radio_and_checkbox()


# Notes for students:
# -------------------
# check():
# - Purpose: Specifically for selecting checkboxes or radio buttons.
# - Functionality: Ensures the checkbox/radio button is selected (if unchecked, it checks).
# - Use Case: To ensure the checkbox/radio button is checked.

# click():
# - Purpose: Simulates a click on any web element (including checkboxes/radio buttons).
# - Functionality: Toggles the state (for checkboxes, if checked, it will uncheck).
# - Use Case: General clicking of elements like buttons, links, etc.

# Key Differences:
# ----------------
# Aspect    | check()                         | click()
# --------------------------------------------------------
# Purpose   | For checkboxes/radio buttons    | For any clickable element
# Effect    | Ensures element is selected     | Toggles the element's state
# Use Case  | Checkbox/radio selection        | Generic click functionality
# Idempotent| Yes (does nothing if already checked) | No (toggling may change state)
