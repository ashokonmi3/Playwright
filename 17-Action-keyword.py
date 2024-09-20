import time
from playwright.sync_api import sync_playwright


def test_keypress():
    """
    Demonstrates how to simulate key presses using Playwright.

    Key Press Interaction Notes:
    -----------------------------
    In Playwright, you can perform various actions to simulate keyboard input:
    - `press`: Sends a key press event to an element.
    - `fill`: Directly sets the value of an input field or textarea.

    Basic Actions:
    --------------
    - `element.press(key)`: Simulates pressing a key on the keyboard.
    - `element.fill(text)`: Sets the text content of an input field or textarea.

    Workflow:
    ----------
    1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
    2. Creates a new page and navigates to a page with an input or textarea element.
    3. Sets the viewport size to 1920x1080 pixels.
    4. Waits for 2 seconds to ensure the page is fully loaded.
    5. Interacts with the input or textarea element by simulating key presses.
    6. Closes the browser.

    Examples:
    ----------
    - Example 1: Simulate typing text into a textarea.
    - Example 2: Simulate pressing specific keys.
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

        # Visit the website with a file input element
        page.goto("https://bootswatch.com/default/")

        # Set the viewport size

        # Wait for 2 seconds to ensure the page is fully loaded
        time.sleep(2)

        # Locate the textarea element by its label
        textarea = page.get_by_label("Example textarea")
        textarea.scroll_into_view_if_needed()

        # Clear any existing text
        textarea.fill("")

        # Simulate typing text into the textarea
        textarea.type("Hello, World!")

        # Simulate pressing specific keys
        textarea.press("KeyW")  # Press 'W'
        time.sleep(1)
        textarea.press("KeyA")  # Press 'A'
        time.sleep(1)
        textarea.press("KeyB")  # Press 'B'
        time.sleep(1)
        textarea.press("KeyC")  # Press 'C'
        textarea.press("Shift+KeyC")  # Press 'Shift + C' for C (capital)

        # Wait for a few seconds to observe the input
        time.sleep(5)

        # Close the browser
        browser.close()


# Execute the function
test_keypress()
