import time
from playwright.sync_api import sync_playwright


def run(playwright):

    # Define the device you want to emulate

    device = playwright.devices['Pixel 5']

    # Launch the browser
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context with the device emulation
    context = browser.new_context(**device)

    # Create a new page
    page = context.new_page()

    # Navigate to a website
    page.goto("https://www.example.com")
    time.sleep(5)

    # Take a screenshot of the page for visual verification
    page.screenshot(path="example_pixel5.png")

    # Close the browser
    browser.close()


with sync_playwright() as playwright:
    for device_name in playwright.devices:
        print(device_name)

    run(playwright)
