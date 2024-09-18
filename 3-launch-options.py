from playwright.sync_api import sync_playwright


def run(playwright):
    # Launch a Chromium browser with custom parameters
    browser = playwright.chromium.launch(
        headless=False,               # Run browser with GUI
        args=['--no-sandbox'],       # Disable sandboxing
        slow_mo=5000,                  # Slow down operations
        devtools=True                # Open DevTools automatically
    )

    # Open a new page
    page = browser.new_page()
    page.goto('https://example.com')

    print(page.title())

    # Close the browser
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
