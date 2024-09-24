from playwright.sync_api import sync_playwright


def demo_network_event_listeners():
    """
    Demonstrates how to use event listeners to monitor network events in Playwright.

    Network Event Concepts:
    ------------------------
    - **request**: Triggered when a network request is initiated. Useful for logging or modifying requests.
    - **response**: Triggered when a network response is received. Important for validating server responses.

    In this example:
    ----------------
    We will listen for network requests and responses while navigating to a webpage, logging relevant information.

    Workflow:
    ---------
    1. Launch a Chromium browser in non-headless mode.
    2. Create a new page.
    3. Attach event listeners for network request and response events.
    4. Navigate to a webpage and observe the events being logged.
    5. Close the page and the browser.
    """
    with sync_playwright() as playwright:
        # Launch the browser in non-headless mode
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Event listener functions for network events
        def on_request(request):
            print('')
            # print(f"Request: {request.method} {request.url}")

        def on_response(response):
            # print(dir(response))

            print(f"Response: {response.text} {
                  response.status} {response.url}")

        # Attach the event listeners to the page
        page.on("request", on_request)
        page.on("response", on_response)

        # Navigate to a webpage (e.g., Playwright's official site)
        page.goto("https://playwright.dev/")

        # Wait for the page to load
        page.wait_for_load_state("load")


# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#     '_dispatcher_fiber', '_impl_obj', '_loop', '_sync', '_wrap_handler',
# 'all_headers', 'failure', 'frame', 'header_value', 'headers', 'headers_array', 'is_navigation_request',
#  'method', 'on', 'once', 'post_data', 'post_data_buffer', 'post_data_json',
#  'redirected_from', 'redirected_to', 'remove_listener', 'resource_type', 'response', 'sizes', 'timing', 'url']
# Execute the function
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#     '__weakref__', '_dispatcher_fiber', '_impl_obj', '_loop', '_sync', '_wrap_handler',
#     'all_headers', 'body', 'finished', 'frame',
# 'from_service_worker', 'header_value', 'header_values',
# 'headers', 'headers_array', 'json', 'ok', 'on', 'once', 'remove_listener',
# 'request', 'security_details', 'server_addr', 'status', 'status_text', 'text', 'url']


demo_network_event_listeners()


"""
================================================
Example Questions for Students:
================================================

1. What is the purpose of monitoring network events in Playwright?
   - Answer: Monitoring network events allows you to track outgoing requests and incoming responses, which is crucial for debugging and validating the behavior of web applications.

2. How do you attach an event listener for a network request in Playwright?
   - Answer: You can attach an event listener using the `page.on("request", callback)` method, where `callback` is a function that handles the request event.

3. What information can you obtain from a network response event?
   - Answer: From a network response event, you can access the response status, URL, headers, and body, which can be used to verify the correctness of the server's response.

4. Why is it important to remove event listeners after they are no longer needed?
   - Answer: Removing event listeners helps prevent memory leaks and ensures that the callbacks do not execute unnecessarily, which can improve performance.

5. What types of network-related events can you listen for in Playwright?
   - Answer: In Playwright, you can listen for `request` and `response` events to monitor network activity.

================================================
Advanced Questions:
================================================

1. How can you log the time taken for a network request to complete?
   - Answer: You can store the timestamp when the request is initiated and calculate the duration when the corresponding response is received.

2. What challenges might arise when monitoring network events in a single-page application (SPA)?
   - Answer: In SPAs, requests may occur dynamically as the user interacts with the app, requiring careful management of event listeners to avoid stale references or excessive logging.

3. Can you modify requests or responses in Playwright? If so, how?
   - Answer: Yes, you can modify requests by intercepting them using `page.route()` to change request properties, and you can mock responses using `page.route()` to provide custom responses for specific requests.
"""
