from playwright.sync_api import sync_playwright
import time


def handle_new_tab_demo():
    """
    This function demonstrates how to handle new tabs in Playwright.

    **Key Concepts Covered:**
    - **Opening a New Tab:** Learn how to trigger an action that opens a new tab.
    - **Switching Between Tabs:** Understand how to focus on different tabs during automation.

    **Example Use Case:**
    In web applications, clicking on certain links or buttons often opens new tabs. This function illustrates how to manage such scenarios effectively.

    **Steps Explained:**
    1. Launch the browser in non-headless mode and maximize the window.
    2. Open a specified webpage that contains a button to open a new tab.
    3. Click the button to open the new tab and switch focus between the original and new tabs.
    """

    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )

        # Create a new browser context
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True
        )
        page = context.new_page()

        # Navigate to the test page that opens a new tab
        page.goto("https://demoqa.com/browser-windows")

        # Click the button that opens a new tab and wait for it
        with context.expect_page() as new_page_info:
            page.click("#tabButton1")  # Button that opens a new tab

        # Get the new tab reference
        new_page = new_page_info.value
        new_page.wait_for_load_state()  # Wait for the new tab to fully load

        # Print the URL of the new tab
        print(f"New tab URL: {new_page.url}")
        time.sleep(5)

        # Switch back to the original page
        page.bring_to_front()  # Bring the original page to focus
        print(f"Original page URL: {page.url}")

        time.sleep(5)
        # Switch back to the new tab
        new_page.bring_to_front()  # Bring the new tab back to focus
        print(f"Switched back to new tab URL: {new_page.url}")

        time.sleep(5)
        # Close the new tab after use
      #   new_page.close()

        time.sleep(5)
        # Close the browser
      #   browser.close()
        time.sleep(5)
        print("waiting")


# Execute the function
handle_new_tab_demo()

# Interview Questions:
"""
1. What is the purpose of using `expect_page()` in Playwright?
   Answer: `expect_page()` is used to wait for a new page (or tab) to open after an action, allowing us to capture the new page reference immediately.

2. How do you switch between tabs in Playwright?
   Answer: You can switch between tabs by using the `bring_to_front()` method on the `Page` object corresponding to the tab you want to focus on.

3. What happens if you try to interact with a tab that has not fully loaded?
   Answer: If you attempt to interact with a tab that hasn't fully loaded, it may lead to errors or unexpected behavior. It's essential to use `wait_for_load_state()` to ensure the page is ready for interaction.
"""

# Explanation of Key Lines:
"""
1. with context.expect_page() as new_page_info:
   - Purpose: This line sets up a context manager that waits for a new page (or tab) to be opened as a result of the action that follows it. In Playwright, this is a convenient way to handle scenarios where an action (like clicking a button) results in the opening of a new tab.
   - Context Manager: The with statement ensures that the code block inside it is executed while monitoring for the event of a new page opening. If a new page opens during the execution of this block, the context manager captures that page.
   - new_page_info: This variable holds information about the newly opened page. It is an object that contains various properties and methods to interact with the new page once it has been created.

2. new_page = new_page_info.value
   - Accessing the New Page: After the click action, if a new page is opened, new_page_info.value will contain a reference to that new page object. This allows you to interact with the new page in subsequent lines of your code.
   - Storing the Reference: By assigning new_page_info.value to the variable new_page, you can now use this variable to call methods on the new page, such as checking its URL, clicking elements, or retrieving data.

3. new_page.wait_for_load_state()
   - Waiting for Load Completion: This method is called on the newly opened page object to ensure that the page has fully loaded before you try to interact with it.
   - Load States: Playwright defines different load states (like load, domcontentloaded, networkidle, etc.). By using wait_for_load_state(), you can specify which load state you want to wait for, ensuring that all necessary resources are loaded and the page is ready for interactions.
   - Importance: Waiting for the page to load is crucial because attempting to interact with elements that haven’t been fully loaded yet can lead to errors or unexpected behavior.
"""
