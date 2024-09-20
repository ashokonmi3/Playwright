import time
from playwright.sync_api import sync_playwright


from playwright.sync_api import sync_playwright
import time


# def test_get_by_role_locator():
#     """
#     Demonstrates how to use Playwright's `get_by_role` locator to:
#     1. Launch a Chromium-based browser.
#     2. Navigate to a website.
#     3. Locate a button element using its role and name.
#     4. Scroll the page down.
#     5. Highlight and click the located button.
#     6. Print the current URL of the page.
#     7. Close the browser.

#     This example uses the synchronous Playwright API.
#     """
#     # Initialize Playwright
#     with sync_playwright() as playwright:
#         # Launch a Chromium-based browser instance
#         browser = playwright.chromium.launch(
#             headless=False,  # Run the browser in visible mode
#             slow_mo=500      # Slow down actions by 500 milliseconds for better visibility
#         )

#         # Open a new browser page (tab)
#         page = browser.new_page()

#         # Navigate to the specified website
#         page.goto("https://bootswatch.com/default/")

#         # Set the viewport size for the browser window

#         # Locate a button element using its role and name
#         # Role options:
#         # 'button': Represents a clickable button
#         # 'link': Represents a hyperlink
#         # 'dialog': Represents a modal dialog
#         # 'textbox': Represents an input field for text
#         docs_button = page.get_by_role('button', name="Default button")

#         # Scroll down the page by 1000 pixels
#         page.evaluate("window.scrollBy(0, 1000);")

#         # Highlight the located button for visual confirmation
#         docs_button.highlight()

#         # Wait for 5 seconds to observe the highlighted button
#         time.sleep(5)

#         # Click the located button
#         docs_button.click()

#         # Wait for 5 seconds to observe the action result
#         time.sleep(5)

#         # Print the current URL of the page after the click action
#         print("Current URL:", page.url)

#         # Close the browser to end the session
#         browser.close()


# # Execute the test function if the script is run directly
# if __name__ == "__main__":
#     test_get_by_role_locator()

# =======================
# Heading

# from playwright.sync_api import sync_playwright
# import time


# def test_get_by_role_heading():
#     """
#     Demonstrates how to use Playwright's `get_by_role` locator to:
#     1. Launch a Chromium-based browser.
#     2. Navigate to a website.
#     3. Scroll the page down by 1000 pixels.
#     4. Locate a heading element using its role and name.
#     5. Highlight the located heading element.
#     6. Print the current URL of the page.
#     7. Close the browser.

#     This example uses Playwright's synchronous API.
#     """
#     # Initialize Playwright
#     with sync_playwright() as playwright:
#         # Launch a Chromium-based browser instance
#         browser = playwright.chromium.launch(
#             headless=False,  # Set to False to see the browser window; True for headless mode
#             slow_mo=500      # Introduce a 500 millisecond delay between actions
#         )

#         # Open a new browser page (tab)
#         page = browser.new_page()

#         # Navigate to the specified website
#         page.goto("https://bootswatch.com/default/")

#         # Set the viewport size for the browser window
#
#         # Scroll down the page by 1000 pixels
#         page.evaluate("window.scrollBy(0, 1000);")

#         # Locate a heading element using its role and name
#         # Role options:
#         # 'heading': Represents a heading element (e.g., <h1>, <h2>, etc.)
#         # 'button': Represents a clickable button
#         # 'link': Represents a hyperlink
#         # 'dialog': Represents a modal dialog
#         # 'textbox': Represents an input field for text
#         heading = page.get_by_role(
#             'heading', name="Heading 2"
#         )

#         # Highlight the located heading element for visual confirmation
#         heading.highlight()

#         # Wait for 5 seconds to observe the highlighted heading
#         time.sleep(5)

#         # Print the current URL of the page (optional step)
#         print("Current URL:", page.url)

#         # Close the browser to end the session
#         browser.close()


# # Execute the test function if the script is run directly
# if __name__ == "__main__":
#     test_get_by_role_heading()

# ===============
from playwright.sync_api import sync_playwright
import time


def test_radio_and_checkbox_interaction():
    """
    Demonstrates how to use Playwright's `get_by_role` locator to:
    1. Launch a Chromium-based browser.
    2. Navigate to a website.
    3. Scroll the page down by 4000 pixels.
    4. Locate and interact with radio button and checkbox elements.
    5. Highlight the located elements.
    6. Print the current URL of the page.
    7. Close the browser.

    This example uses Playwright's synchronous API.
    """
    # Initialize Playwright
    with sync_playwright() as playwright:
        # Launch a Chromium-based browser instance
        browser = playwright.chromium.launch(
            headless=False,  # Set to False to see the browser window; True for headless mode
            slow_mo=500      # Introduce a 500 millisecond delay between actions
        )

        # Open a new browser page (tab)
        page = browser.new_page()

        # Navigate to the specified website
        page.goto("https://bootswatch.com/default/")

        # Set the viewport size for the browser window

        # Scroll down the page by 4000 pixels
        page.evaluate("window.scrollBy(0, 4000);")

        # Locate a radio button element using its role and name
        # Role options:
        # 'radio': Represents a radio button
        # 'checkbox': Represents a checkbox
        radio_button = page.get_by_role(
            'radio', name="Option one is this and that—be sure to include why it's great"
        )

        # Highlight the located radio button for visual confirmation
        radio_button.highlight()

        # Wait for 5 seconds to observe the highlighted radio button
        time.sleep(5)

        # Locate a checkbox element using its role and name
        check_box = page.get_by_role(
            'checkbox', name="Default checkbox"
        )

        # Highlight the located checkbox for visual confirmation
        check_box.highlight()

        # Check the checkbox
        check_box.check()

        # Wait for 5 seconds to observe the checked checkbox
        time.sleep(5)

        # Print the current URL of the page (optional step)
        print("Current URL:", page.url)

        # Close the browser to end the session
        browser.close()


# Execute the test function if the script is run directly
if __name__ == "__main__":
    test_radio_and_checkbox_interaction()

# =====================
