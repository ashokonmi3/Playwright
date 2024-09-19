import time
from playwright.sync_api import sync_playwright


# with sync_playwright() as playwright:
#     # Launch a browser
#     browser = playwright.chromium.launch(
#         headless=False, slow_mo=3000, args=["--start-maximized"]
#     )

#     context = browser.new_context(
#         ignore_https_errors=True, no_viewport=True)
#     page = context.new_page()
#     # Visit the playwright website
#     page.goto("https://bootswatch.com/default/")
#      #     page.evaluate("window.scrollBy(0, 1000);")  # Scrolls down by 1000 pixels

#     # Locate a link element with "Docs" text
#     page.get_by_text("with faded secondary text").highlight()

#     time.sleep(5)
#     page.get_by_text("Small button").highlight()
#     time.sleep(5)
#     page.get_by_text("Middle").click()
#     time.sleep(5)

#     page.get_by_text("fine print", exact=False).highlight()
#     time.sleep(5)

#     browser.close()
# ====================
# Alt Text
# The get_by_alt_text() method in Playwright is used to locate elements based on their alt attribute,
# which is commonly associated with images ( < img > tags). The alt (alternative) text provides a textual description of the image, and it is displayed or read out by screen readers if the image cannot be loaded or for users with visual impairments.

# Usage and Purpose:
# The get_by_alt_text() method is particularly useful for finding images or other elements with an alt attribute when the visual content is important but you cannot directly rely on the visual appearance for automation.
# with sync_playwright() as playwright:
#     # Launch a browser
#     browser = playwright.chromium.launch(
#         headless=False, slow_mo=3000, args=["--start-maximized"]
#     )

#     context = browser.new_context(
#         ignore_https_errors=True, no_viewport=True)
#     page = context.new_page()
#     # Visit the playwright website
#     page.goto("https://google.com/")

#     page.get_by_alt_text("Google").highlight()

#     time.sleep(5)

#     browser.close()
# ======================
# Title locator
# The get_by_title() method in Playwright is used to locate an HTML element based on its title attribute. The title attribute is often used to provide additional information about an element, such as a tooltip that appears when a user hovers over the element.

# Purpose:
# The title attribute gives supplementary information or descriptions for elements, especially those where a tooltip is useful for accessibility or clarification.
# The get_by_title() method helps in identifying such elements in automated tests by matching the exact title value.

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(
        headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()
    # Visit the playwright website
    page.goto("https://bootswatch.com/default/")
    page.evaluate("window.scrollBy(0, 1000);")  # Scrolls down by 1000 pixels

    page.get_by_title("attribute").highlight()

    time.sleep(5)
    page.evaluate("window.scrollBy(0, 1000);")  # Scrolls down by 1000 pixels

    page.get_by_title("Source Title").highlight()

    time.sleep(5)

    browser.close()
