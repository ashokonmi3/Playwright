from playwright.sync_api import sync_playwright, expect


def test_non_breaking_space_button(page):
    """
    Verifies the handling of non-breaking spaces in XPath selectors.
Prevent Line Breaks: Unlike a regular space, a non-breaking space prevents the text 
on either side from being separated onto different lines. This is useful for keeping phrases
 or important text together, ensuring they stay on the same line.

Alignment and Formatting: It can be used to create spacing in layouts without allowing the browser to break the text flow, which can help with formatting elements on a webpage.

Preserving Whitespace: When dealing with programming or text processing, using &nbsp; ensures that the space is retained as intended, especially when formatting strings or outputs where spaces might otherwise be collapsed.

Improving Readability: In some cases, it can enhance readability by controlling how text is presented, particularly in tables or lists where consistent spacing is desired
    This function performs the following actions:
    - Navigates to a webpage that demonstrates non-breaking spaces.
    - Attempts to click a button using a normal space in the XPath, which should fail.
    - Clicks the same button using a non-breaking space in the XPath, which should succeed.

    Key Learning Points:
    - Understanding how non-breaking spaces can affect element selection in automated tests.
    - Recognizing the importance of correct XPath syntax when dealing with dynamic content.

    Scenario:
    1. Use the following XPath to find the button in your test:
       //button[text()='My Button']
       Notice that the XPath does not work. 
    2. Change the space between 'My' and 'Button' to a non-breaking space. 
       This time the XPath should be valid.
    """

    # Navigate to the webpage for non-breaking space testing
    page.goto("http://uitestingplayground.com/nbsp")

    # Attempt to click the button using a normal space
   #  page.locator("//button[text()='My Button']").click(timeout=2000)

   #  try:
   #      page.locator("//button[text()='My Button']").click(timeout=2000)
   #  except Exception as e:
   #      print(f"Expected error when using normal space: {e}")

    # Click the button using a non-breaking space
    page.locator("//button[text()='My\u00a0Button']").click()


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for verifying button functionality with non-breaking spaces.

    - Launches the Chromium browser in non-headless mode with slow motion for better visualization.
    - Runs the `test_non_breaking_space_button` function to test the click functionality.
    """

    # Launch the Chromium browser with slow motion for better visualization
    print("Launching the browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    print("Creating a new browser context and page...")
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()

    # Run the test case on the page
    print("Running the non-breaking space test case...")
    test_non_breaking_space_button(page)

    # Close the browser after the test completes
    print("Closing the browser...")
    browser.close()

    print("Test execution completed.")


"""
================================================
Example Questions for Students:
================================================

1. What issue might arise when using a normal space in an XPath selector?
   - Answer: A normal space may not match the actual text in the DOM if the text contains a non-breaking space, causing the selector to fail.

2. How does a non-breaking space differ from a normal space in HTML?
   - Answer: A non-breaking space (`&nbsp;` or `\u00a0`) prevents the text from being wrapped to a new line, while a normal space allows wrapping.

3. What is the purpose of the try-except block in the test?
   - Answer: It is used to catch any exceptions raised when clicking the button with a normal space, allowing the test to continue and handle the situation gracefully.

4. Why is slow motion (`slow_mo=3000`) used when launching the browser?
   - Answer: Slow motion is used to slow down the test execution (3 seconds in this case) to make it easier to visualize the actions taking place.

5. What does the `ignore_https_errors=True` option do?
   - Answer: This option allows the browser context to ignore HTTPS certificate errors, which is useful for testing on non-secure sites.

================================================
Advanced Questions:
================================================

1. How can you verify that an element is present on the page before attempting to interact with it?
   - Answer: You can use methods like `page.wait_for_selector()` to ensure the element is present before attempting to click or interact with it.

2. What would you do if you encounter a `StaleElementReferenceError`?
   - Answer: You should try to locate the element again to get a fresh reference, as the original reference is no longer valid due to changes in the DOM.

3. Explain how XPath differs from CSS selectors in element selection.
   - Answer: XPath allows for more complex queries and can navigate through the DOM hierarchy, while CSS selectors are generally simpler and based on element attributes, classes, and IDs.

"""
