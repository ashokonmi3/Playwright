from playwright.sync_api import sync_playwright


from playwright.sync_api import sync_playwright


# def test_playwright_navigation():
#     """
#     This function demonstrates how to use Playwright to:
#     1. Launch a Chromium-based browser.
#     2. Navigate to the Playwright website.
#     3. Locate and click the "Docs" link on the website.
#     4. Print the current URL of the page.
#     5. Close the browser.

#     The function uses synchronous Playwright API to perform these actions.
#     """
#     # Initialize Playwright
#     with sync_playwright() as playwright:
#         # Launch a Chromium-based browser
#         browser = playwright.chromium.launch(
#             headless=False,  # Set to False to open the browser in a visible mode
#             slow_mo=1000      # Slow down operations by 500 milliseconds to observe actions
#         )

#         # Create a new browser context and page
#         page = browser.new_page()

#         # Navigate to the Playwright website
#         page.goto("https://playwright.dev/python")

#         # Locate the "Docs" link element by its role and name
#         docs_button = page.get_by_role('link', name="Docs")

#         # Click on the "Docs" link
#         docs_button.click()

#         # Print the current URL of the page after clicking the link
#         print("Docs:", page.url)

#         # Close the browser
#         browser.close()


# # Run the test function if the script is executed directly
# if __name__ == "__main__":
#     test_playwright_navigation()
# ==============================================
# from playwright.sync_api import sync_playwright


# def test_playwright_navigation():
#     """
#     Demonstrates how to use Playwright to:
#     1. Launch a Chromium-based browser.
#     2. Navigate to the Playwright documentation website.
#     3. Locate and click the "Get Started" link.
#     4. Print the URL of the page after clicking the link.
#     5. Close the browser.

#     This function uses Playwright's synchronous API.
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

#         # Navigate to the Playwright documentation website
#         page.goto("https://playwright.dev/python")

#         # Locate the "Get Started" link element by its role and accessible name
#         get_started_button = page.get_by_role('link', name="Get Started")

#         # Click the "Get Started" link
#         get_started_button.click()

#         # Print the current URL of the page after clicking the link
#         print("Current URL after clicking 'Get Started':", page.url)

#         # Close the browser to end the session
#         browser.close()


# # Execute the test function if this script is run directly
# if __name__ == "__main__":
#     test_playwright_navigation()

# =============================
# Interactive mode
# open terminal
# type python

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False,slow_mo=500)
browser
page = browser.new_page() 
# new page will open
page.goto("https://playwright.dev/python")
button = page.get_by_role("link",name="GET STARTED")
button.click()
browser.close()
playwright.stop()
