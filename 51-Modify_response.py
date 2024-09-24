from playwright.sync_api import sync_playwright


def demo_network_fulfill():
    """
    Demonstrates how to use network routing in Playwright to fulfill network requests with custom responses.

    Network Fulfillment Concepts:
    ------------------------------
    - **Fulfill**: Responding to a network request with custom data instead of letting the original request proceed.

    In this example:
    ----------------
    We will intercept a specific API request and respond with a custom JSON object instead of the actual response.

    Workflow:
    ---------
    1. Launch a Chromium browser in non-headless mode.
    2. Create a new page.
    3. Attach a network route to fulfill a specific API request.
    4. Navigate to a webpage and observe the behavior.
    5. Close the page and the browser.
    """
    with sync_playwright() as playwright:
        # Launch the browser in non-headless mode
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Event listener function to fulfill specific API requests
        def on_route(route):
            # Check if the request URL matches the API we want to mock
            if route.request.url == "https://playwright.dev/":
                print(f"Fulfilling request for: {route.request.url}")
                # Respond with custom JSON data
                response = route.fetch()
                print(response)
               #  print(response.text())
                body = response.text().replace(
                    "enables reliable end-to-end testing for modern web apps.", "is an awsome framework for web automation!")
                route.fulfill(
                    response=response,
                    body=body
                )
            else:
                route.continue_()  # Continue other requests

        # Attach the event listener to fulfill the API request
        page.route("**/*", on_route)

        # Navigate to a webpage that triggers the API request
        # Replace with a real site that makes the request
        page.goto("https://playwright.dev/")

        # Wait for a moment to ensure the request is made and fulfilled
        # Adjust as necessary for the request timing
      #   page.wait_for_timeout(2000)
        page.screenshot(
            path="playwright_modified_content.jpg", full_page=False)

        # Close the page
        page.close()

        # Close the browser if done with all tasks
        browser.close()


# Execute the function
demo_network_fulfill()


"""
================================================
Example Questions for Students:
================================================

1. What does it mean to fulfill a network request in Playwright?
   - Answer: Fulfilling a network request means responding to a request with custom data instead of allowing the original request to proceed.

2. How can you customize the response when fulfilling a request?
   - Answer: You can customize the response by specifying the status code, content type, and body of the response using the `route.fulfill()` method.

3. What is the use of `route.continue_()` in the context of network routing?
   - Answer: The `route.continue_()` method allows other network requests to proceed without interference when the current request is not one we want to fulfill or modify.

4. When might you want to fulfill requests with custom data during testing?
   - Answer: Fulfilling requests with custom data is useful for mocking API responses in tests, allowing you to test different scenarios without relying on the actual server responses.

================================================
Advanced Questions:
================================================

1. How can you log request details when fulfilling a network request?
   - Answer: You can log the request URL, method, and other details within the `on_route` function before calling `route.fulfill()`.

2. What challenges might arise when fulfilling requests in tests for dynamic web applications?
   - Answer: Dynamic applications may change API endpoints or payloads, requiring frequent updates to the mocked responses in tests to stay relevant.

3. Can you fulfill requests based on specific request headers or parameters?
   - Answer: Yes, you can inspect the request headers or query parameters in the `on_route` function to conditionally fulfill requests based on their contents.
"""
