from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    """
    Test Case: Interacting with dynamic elements using Playwright

    This test demonstrates how to interact with dynamic elements that have
    changing attributes, such as buttons with dynamic classes or IDs. When i refresh the page the location will change and 
    hence the class as well

    Key Learning Points:
    1. How to locate elements using both CSS selectors and XPath.
    2. Best practices for working with dynamic elements.
    3. The use of the Playwright `expect` API for assertions, including checking visibility.

    Steps:
    1. Launch the Chromium browser in non-headless mode with slow motion to see the steps clearly.
    2. Navigate to a page where dynamic class attributes are present.
    3. Locate an element (a button) dynamically using both CSS selectors and XPath.
    4. Scroll the button into view if needed.
    5. Verify that the button is visible.
    6. Perform a click action on the button.
    """

    # 1. Launch the Chromium browser with slow motion for visualization
    browser = playwright.chromium.launch(
        headless=False, slow_mo=3000, args=["--start-maximized"]
    )

    # 2. Create a browser context and page (tab)
    context = browser.new_context(
        ignore_https_errors=True, no_viewport=True
    )
    page = context.new_page()

    # 3. Navigate to the target page that contains dynamic elements
    page.goto("http://uitestingplayground.com/classattr")

    # --- Dynamic Element Location: CSS Selector ---

    # CSS Selector: Locate the button using its dynamic class attribute
    # `btn-primary` is a class applied to the primary button
    primary_btn = page.locator("button.btn-primary")

    # Scroll the button into view to ensure it's accessible
    primary_btn.scroll_into_view_if_needed()

    # --- Dynamic Element Location: XPath ---
    # Alternatively, locate the button using XPath
    # The XPath looks for any button element containing 'btn-primary' in its class
    primary_btn = page.locator("//button[contains(@class, 'btn-primary')]")

    # 4. Assert that the button is visible on the page
    expect(primary_btn).to_be_visible()
    print("The dynamic button with class 'btn-primary' is visible.")

    # 5. Perform a click action on the button
    primary_btn.click()
    print("Dynamic button clicked.")

    # Close the browser after completion (optional)
    browser.close()

    """
    Important Notes :
    - **Dynamic Elements**: In many web applications, elements like buttons may have
      dynamic classes or IDs that change on page load. Using robust locators such as
      CSS classes and XPath allows you to locate these elements even when IDs are not static.
    
    - **CSS Selectors**: Ideal when you know the structure of the classes or attributes.
      In this case, `.btn-primary` targets the class directly.
    
    - **XPath**: Useful for more complex scenarios where the element has multiple classes,
      or the class is part of a dynamic set of attributes, as in this example using 
      `contains(@class, 'btn-primary')` to match any element with that partial class name.
    
    - **Scroll into View**: Playwright automatically scrolls elements into view if they're not
      visible on the current screen. Using `scroll_into_view_if_needed()` ensures the element
      is scrolled to before interaction.
    
    - **Assertions**: Using the `expect` API is a good practice to confirm the element’s state
      (e.g., visibility) before interacting with it, helping to prevent flaky tests.
    """
