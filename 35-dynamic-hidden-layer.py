from playwright.sync_api import sync_playwright, expect, TimeoutError

with sync_playwright() as playwright:
    """
    Test Case: Interacting with hidden layers in Playwright

    This test demonstrates how to interact with elements that may become hidden after an action,
    such as buttons with dynamic layers. It showcases how to handle situations where an element
    is not interactable due to becoming hidden.

    Key Learning Points:
    1. Handling elements that dynamically change state (e.g., become hidden after an interaction).
    2. Best practices for interacting with elements that have hidden layers.
    3. Use of the Playwright `expect` API for assertions.

    Steps:
    1. Launch the Chromium browser in non-headless mode with slow motion to visualize interactions.
    2. Navigate to a page where a button may become hidden after an action.
    3. Perform an initial click on a button.
    4. Attempt to click the button again to demonstrate how hidden layers are handled.
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

    # 3. Navigate to the target page that contains hidden layers
    page.goto("http://uitestingplayground.com/hiddenlayers")

    # Locate the green button using CSS selector
    green_btn = page.locator("button#greenButton")

    # 4. Click the green button for the first time
    green_btn.click()

    # 5. Attempt to click the button again - this should fail since the button may become hidden
    try:
        # Will raise TimeoutError if the button is not clickable
        green_btn.click(timeout=2000)
    except TimeoutError:
        print("The green button is hidden and not clickable.")

    # Close the browser after completion (optional)
    browser.close()

    """
    Important Notes:
    - **Dynamic Elements**: In many web applications, buttons or elements may become hidden
      after an action, preventing further interaction. You should handle such cases gracefully.
    
    - **Handling TimeoutError**: Playwright will raise a `TimeoutError` if it cannot interact
      with an element (e.g., due to it becoming hidden). It’s good practice to wrap such actions
      in a try-except block to handle the error gracefully.
    
    - **Assertions**: Using the `expect` API ensures that the element’s state (e.g., visibility)
      is correct before interacting with it, reducing the chance of flaky tests.
    """
