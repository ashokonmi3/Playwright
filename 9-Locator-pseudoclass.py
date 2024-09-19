import time
from playwright.sync_api import sync_playwright

# Pseudo classes

with sync_playwright() as playwright:
    # Launch a browser in non-headless mode with a slow motion delay of 500ms
    browser = playwright.chromium.launch(
        headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(
        ignore_https_errors=True, no_viewport=True)
    page = context.new_page()
    # Visit the website
    page.goto("https://bootswatch.com/default/")

    # Set the viewport size

    # Wait for 2 seconds before scrolling down
    time.sleep(2)

    # Example 1: Select and highlight an element by text (Navbars in h1)
    element_by_tag = page.locator('h1:has-text("Navbars")')
    element_by_tag.highlight()
    time.sleep(2)

    element_by_tag = page.locator('h1:has-text("Navs")')
    element_by_tag.highlight()
    time.sleep(2)
    # Example 2: Select and highlight another h1 by text (Navs)
    # has-text-is select elements whose text content exactly matches a specific string this will fail
    # element_by_tag = page.locator('h1:has-text-is("Navs")')
    # element_by_tag.highlight()
    # time.sleep(2)

    # Example 3: Select and highlight a visible dropdown menu
    # drop down after success , we need to click on that
    # page.evaluate("window.scrollBy(0, 1000);")  # Scrolls down by 1000 pixels

    # element_by_tag = page.locator('div.dropdown-menu:visible')
    # element_by_tag.highlight()
    # time.sleep(2)

    # Example 4: Select the 4th button with class 'btn-primary'
    element_by_tag = page.locator(':nth-match(button.btn-primary, 4)')
    element_by_tag.highlight()
    time.sleep(2)

    # Example 5: Select the 1st button with text 'Primary'
    element_by_tag = page.locator(":nth-match(button:has-text('Primary'), 1)")
    element_by_tag.highlight()
    time.sleep(2)

    # Example 6: Select the 3rd button with text 'Primary'
    element_by_tag = page.locator(":nth-match(button:has-text('Primary'), 3)")
    element_by_tag.highlight()
    time.sleep(2)

    # Close the browser
    browser.close()
