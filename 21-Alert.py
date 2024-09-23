from playwright.sync_api import sync_playwright
import time


# def handle_alert_demo():
#     #     """
#     #     Demonstrates how to handle JavaScript alerts using Playwright.

#     #     This script performs the following steps:
#     #     1. Launches a Chromium browser instance.
#     #     2. Navigates to a test page with an alert button.
#     #     3. Sets up an event listener to handle dialog events (alerts).
#     #     4. Clicks the button to trigger the alert.
#     #     5. Waits for a few seconds to ensure the alert is handled.
#     #     6. Closes the browser.

#     #     Key Concepts:
#     #     --------------
#     #     - Handling alerts: Playwright allows interaction with JavaScript alerts by listening for dialog events.
#     #     - Event listeners: Using `page.on('dialog', handler_function)` to handle alerts.
#     #     - Synchronization: Using `time.sleep()` to wait for actions to complete.

#     #     Notes:
#     #     -------
#     #     - Ensure that the selector used for locating the button matches the element on the page.
#     #     - Adjust the sleep duration based on the time required for the alert to appear and be handled.
#     # """

#     def handle_dialog(dialog):
#         """
#         Handles the dialog event by printing the alert text and accepting the alert.

#         Parameters:
#         -----------
#         dialog (Dialog): The dialog object representing the JavaScript alert.
#         """
#         print(f"Alert text: {
#               dialog.message}")  # Print the alert text to the console
#         time.sleep(5)
#         dialog.accept()  # Accept the alert

#     with sync_playwright() as playwright:
#         # Launch the browser in non-headless mode with a slow motion delay of 500ms
#         browser = playwright.chromium.launch(headless=False, slow_mo=500)
#         page = browser.new_page()

#         # Navigate to the test page with the alert button
#         page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")

#         # Register the event listener for dialog events (alerts)
#         page.on('dialog', handle_dialog)

#         # Locate the button that triggers the alert
#         button_locator = page.get_by_text("Show alert box")

#         # Click the button to trigger the alert
#         button_locator.click()

#         # Wait for a few seconds to ensure the alert is handled
#         time.sleep(5)  # Adjust this time if needed based on alert appearance

#         # Close the browser
#         browser.close()


# # # Execute the function
# handle_alert_demo()
# ===================


# def handle_alert_demo():
#     #     """
#     #     Demonstrates how to handle JavaScript alerts using Playwright.

#     #     This script performs the following steps:
#     #     1. Launches a Chromium browser instance.
#     #     2. Navigates to a test page with an alert button.
#     #     3. Sets up an event listener to handle dialog events (alerts).
#     #     4. Clicks the button to trigger the alert.
#     #     5. Waits for a few seconds to ensure the alert is handled.
#     #     6. Closes the browser.

#     #     Key Concepts:
#     #     --------------
#     #     - Handling alerts: Playwright allows interaction with JavaScript alerts by listening for dialog events.
#     #     - Event listeners: Using `page.on('dialog', handler_function)` to handle alerts.
#     #     - Synchronization: Using `time.sleep()` to wait for actions to complete.

#     #     Notes:
#     #     -------
#     #     - Ensure that the selector used for locating the button matches the element on the page.
#     #     - Adjust the sleep duration based on the time required for the alert to appear and be handled.
#     #     """

#     def handle_dialog(dialog):
#         """
#         Handles the dialog event by printing the alert text and accepting the alert.

#         Parameters:
#         -----------
#         dialog (Dialog): The dialog object representing the JavaScript alert.
#         """
#         print(f"Alert text: {
#               dialog.message}")  # Print the alert text to the console
#         time.sleep(5)  # Adjust this time if needed based on alert appearance

#         dialog.dismiss()  # Dissmiss the alert

#     with sync_playwright() as playwright:
#         # Launch the browser in non-headless mode with a slow motion delay of 500ms
#         browser = playwright.chromium.launch(headless=False, slow_mo=500)
#         page = browser.new_page()

#         # Navigate to the test page with the alert button
#         page.goto(
#             "https://testpages.eviltester.com/styled/alerts/alert-test.html")

#         # Register the event listener for dialog events (alerts)
#         page.on('dialog', handle_dialog)

#         # Locate the button that triggers the alert
#         button_locator = page.get_by_text("Show confirm box")

#         # Click the button to trigger the alert
#         button_locator.click()

#         # Wait for a few seconds to ensure the alert is handled
#         # Adjust this time if needed based on alert appearance
#         time.sleep(5)

#         # Close the browser
#         browser.close()


# # Execute the function
# handle_alert_demo()
# =====================


def handle_alert_demo():
    """
    Demonstrates how to handle JavaScript alerts using Playwright.

    This script performs the following steps:
    1. Launches a Chromium browser instance.
    2. Navigates to a test page with an alert button.
    3. Sets up an event listener to handle dialog events (alerts).
    4. Clicks the button to trigger the alert.
    5. Waits for a few seconds to ensure the alert is handled.
    6. Closes the browser.

    Key Concepts:
    --------------
    - Handling alerts: Playwright allows interaction with JavaScript alerts by listening for dialog events.
    - Event listeners: Using `page.on('dialog', handler_function)` to handle alerts.
    - Synchronization: Using `time.sleep()` to wait for actions to complete.

    Notes:
    -------
    - Ensure that the selector used for locating the button matches the element on the page.
    - Adjust the sleep duration based on the time required for the alert to appear and be handled.
    """

    def handle_dialog(dialog):
        """
        Handles the dialog event by printing the alert text and accepting the alert.

        Parameters:
        -----------
        dialog (Dialog): The dialog object representing the JavaScript alert.
        """
        print(f"Alert text: {
              dialog.message}")  # Print the alert text to the console
        time.sleep(5)
        dialog.accept("hello")  # Enter the hello and Accept the alert

    with sync_playwright() as playwright:
        # Launch the browser in non-headless mode with a slow motion delay of 500ms
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True
        )
        page = context.new_page()

        # Navigate to the test page with the alert button
        page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")

        # Register the event listener for dialog events (alerts)
        page.on('dialog', handle_dialog)

        # Locate the button that triggers the alert
        button_locator = page.get_by_text("Show prompt box")

        # Click the button to trigger the alert
        button_locator.click()

        # Wait for a few seconds to ensure the alert is handled
        time.sleep(5)  # Adjust this time if needed based on alert appearance

        # Close the browser
        browser.close()


# Execute the function
handle_alert_demo()
