import time
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://google.com")
    # time.sleep(5)
    print("Title of the page:", page.title())
    browser.close()
