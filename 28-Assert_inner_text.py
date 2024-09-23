import time
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

# Execute the test within the sync_playwright context
with sync_playwright() as playwright:
    # Launch the browser and create a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the Playwright Python page
    page.goto("https://playwright.dev/python")
    time.sleep(2)

    # Locate the dropdown menu that contains programming languages
    dropdown_menu = page.locator("ul.dropdown__menu")

    # Expect API: Check if the dropdown menu contains the text "Python"
    expect(dropdown_menu).to_contain_text("Python")
    print("Dropdown menu contains 'Python'.")
    time.sleep(2)

    # Expect API: Check if the dropdown menu contains the text "Node.js"
    expect(dropdown_menu).to_contain_text("Node.js")
    print("Dropdown menu contains 'Node.js'.")
    time.sleep(2)

    # Expect API: Check if the dropdown menu contains the text "Java"
    expect(dropdown_menu).to_contain_text("Java")
    print("Dropdown menu contains 'Java'.")

    # Expect API: Check if the dropdown menu contains the text ".NET"
    expect(dropdown_menu).to_contain_text(".NET")
    print("Dropdown menu contains '.NET'.")

    # Locate the main heading of the page
    heading = page.locator("h1.hero__title")

    time.sleep(2)

    # Expect API: Verify that the main heading has the exact text
    expect(heading).to_have_text(
        "Playwright enables reliable end-to-end testing for modern web apps.")
    print("Heading has the exact expected text.")
    time.sleep(2)

    # Close the browser after the test
    browser.close()
