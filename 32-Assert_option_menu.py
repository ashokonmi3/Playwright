from playwright.sync_api import expect, sync_playwright

with sync_playwright() as playwright:
    """
    Test case demonstrating various `expect` API assertions in Playwright:
    - Verifying the selected state of dropdown menus
    """

    # 1. Launch the Chromium browser (non-headless for visibility)
    browser = playwright.chromium.launch(
        headless=False, slow_mo=3000, args=["--start-maximized"]
    )

    # Create a new browser context and page
    context = browser.new_context(
        ignore_https_errors=True, no_viewport=True
    )
    page = context.new_page()

    # 2. Navigate to the Bootswatch page
    page.goto("https://bootswatch.com/default")

    # Locate the single select dropdown
    option_menu = page.get_by_label("Example select")
    option_menu.scroll_into_view_if_needed()

    # 3. Expect the selected option to be "1"
    expect(option_menu).to_have_value("1")
    print("Selected option in the dropdown is '1'.")

    # Locate the multiple select dropdown
    multi_option_menu = page.get_by_label("Example multiple select")

    # 4. Select options "2" and "4"
    multi_option_menu.select_option(["2", "4"])
    print("Selected options '2' and '4' in the multiple select.")

    # 5. Expect the selected options to be "2" and "4"
    expect(multi_option_menu).to_have_values(["2", "4"])
    print("Verified selected options in the multiple select.")

    # Close the browser after the test
    browser.close()
