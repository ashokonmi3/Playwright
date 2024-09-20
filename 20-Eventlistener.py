from playwright.sync_api import sync_playwright


def event_listener_demo():
    """
    Demonstrates how to use and remove event listeners in Playwright for various page events.

    Event Listener Concepts:
    -------------------------
    - **request**: Triggered when a network request is made.
    - **response**: Triggered when a network response is received.
    - **load**: Triggered when the page finishes loading.
    - **domcontentloaded**: Triggered when the DOM is fully loaded and parsed.
    - **close**: Triggered when the page is closed.

    In this example:
    ----------------
    We will listen for network requests, responses, page load, DOM content loaded, and page close events.
    After handling the events, we will remove the listeners.

    Workflow:
    ---------
    1. Launch a Chromium browser in non-headless mode.
    2. Create a new page.
    3. Attach event listeners.
    4. Navigate to a webpage and observe the events being logged.
    5. Remove the event listeners.
    6. Close the browser.
    """
    with sync_playwright() as playwright:
        # Launch the browser in non-headless mode
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Event listener functions
        def on_request(request):
            print(f"Request: {request.method} {request.url}")

        def on_response(response):
            print(f"Response: {response.status} {response.url}")

        def on_load():
            print("Page has finished loading!")

        def on_dom_content_loaded():
            print("DOM content has been fully loaded and parsed!")

        def on_close():
            print("Page has been closed!")

        # Attach the event listeners to the page
        page.on("request", on_request)
        page.on("response", on_response)
        page.on("load", on_load)
        page.on("domcontentloaded", on_dom_content_loaded)
        page.on("close", on_close)

        # Navigate to a webpage (e.g., Playwright's official site)
        page.goto("https://playwright.dev/")

        # Wait for the page to load
        page.wait_for_load_state("load")

        # Remove the event listeners
      

        # Close the page
        page.close()

        # Optionally close the browser if done with all tasks
        browser.close()


# Execute the function
event_listener_demo()
