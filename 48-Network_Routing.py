from playwright.sync_api import sync_playwright


def demo_network_routing():
    """
    Demonstrates how to use network routing in Playwright to control network requests.

    Network Routing Concepts:
    -------------------------
    - **Routing**: The ability to intercept network requests and define how they should be handled.
    - **Abort**: Cancelling a network request to prevent it from completing. Useful for blocking unwanted resources.
    - **Fulfill**: Responding to a network request with custom data.

    In this example:
    ----------------
    We will set up a route to block all PNG image requests and a specific image request while navigating to a webpage and taking a screenshot of the page.

    Workflow:
    ---------
    1. Launch a Chromium browser in non-headless mode.
    2. Create a new page.
    3. Attach a network route to block PNG image requests and a specific image request.
    4. Navigate to a webpage and observe the behavior.
    5. Take a screenshot of the loaded page.
    6. Close the page and the browser.
    """
    with sync_playwright() as playwright:
        # Launch the browser in non-headless mode
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Event listener function to block requests
        def on_route(route):
            print(f"Request aborted: {route.request.url}")
            route.abort()  # Abort the request

        # Attach the event listener to block all PNG image requests
        page.route("**/*.png", on_route)
        # To block a single file
      #   page.route("https://playwright.dev/img/playwright-logo.svg", on_route)

        # Navigate to a webpage (e.g., Playwright's official site)
        page.goto("https://playwright.dev/")

        # Take a screenshot of the page
        page.screenshot(path="playwright_with_out_png.jpg", full_page=True)

        # Close the page
        page.close()

        # Close the browser if done with all tasks
        browser.close()


# Execute the function
demo_network_routing()


"""
================================================
Example Questions for Students:
================================================

1. What is network routing in Playwright?
   - Answer: Network routing allows you to intercept network requests and define how they should be handled, such as modifying, blocking, or fulfilling them.

2. How can you block specific types of requests in Playwright?
   - Answer: You can block requests by using the `page.route(url_pattern, callback)` method, where `url_pattern` specifies the requests to intercept and `callback` defines how to handle them.

3. What does the `route.abort()` method do?
   - Answer: The `route.abort()` method cancels the network request, preventing it from completing and sending a response.

4. How would you fulfill a network request with custom data?
   - Answer: You can use the `route.fulfill()` method to respond to a request with custom headers, status, and body.

5. What types of network requests can you route in Playwright?
   - Answer: You can route any network request, including images, scripts, stylesheets, and API calls by using appropriate URL patterns.

================================================
Advanced Questions:
================================================

1. How can you log request and response headers using network routing?
   - Answer: You can access the request and response headers through the `request.headers` and `response.headers` properties within your route handler functions.

2. What are potential use cases for modifying or fulfilling network requests in tests?
   - Answer: Use cases include mocking API responses for testing, blocking ads or tracking scripts, and modifying request data for simulation purposes.

3. How can network routing be useful in testing single-page applications (SPAs)?
   - Answer: Network routing allows testers to control resource loading, simulate various server responses, and ensure that SPAs handle network interactions correctly during testing.
"""
