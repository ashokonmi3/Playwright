from playwright.sync_api import sync_playwright
from time import perf_counter


def custom_wait_demo():
    """
    Demonstrates the use of custom wait logic in Playwright for AJAX-driven web pages.

    Custom Wait Concept:
    --------------------
    Often, web pages use AJAX or JavaScript to load certain elements after the initial page load. 
    Playwright's automatic wait mechanisms handle many of these cases, but sometimes, 
    we need to wait for specific elements that load dynamically.
    Auto-waiting only works for actions related to DOM elements, such as clicking or typing. 
    If you need to wait for something that’s not directly related to an element, such as waiting for 
    a network request, page navigation, or JavaScript execution, you’ll need wait_for().

    For example:

    Waiting for a network request to finish before proceeding.
    Waiting for a specific event (like a page load or a custom JavaScript event).

    In this case:
    --------------
    - The page we are interacting with uses AJAX to load the movie data for the year 2015.
    - Instead of waiting for the entire page to load, we wait specifically for a table of movie titles to appear.

    Key Playwright Features Used:
    ------------------------------
    - `locator.wait_for()`: Waits for a specific element (like a table cell) to be available in the DOM.
    - `perf_counter()`: Used to measure the time taken for the custom wait.

    Workflow:
    ---------
    1. Launch a browser with a 500ms slow motion for better visualization.
    2. Navigate to the AJAX demo page.
    3. Click the link to load the 2015 movie data.
    4. Use `wait_for()` to wait for the table data to load.
    5. Record and print the time taken to load the movie data.
    6. Close the browser.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True
        )
        page = context.new_page()

        # Navigate to the AJAX demo page
        page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

        # Locate the link for loading movie data for the year 2015 and click it
        link = page.get_by_role("link", name="2015")
        link.click()

        print("Loading Oscars for 2015...")

        # Start the timer to measure the wait time
        start = perf_counter()

        # Locate the first table cell containing the movie title and wait for it to appear
        first_table_data = page.locator(
            "td.film-title").first  # first row in table of 2015
        first_table_data.wait_for()  # default time out 30 second

        # Calculate the time taken for the movies to load
        time_taken = perf_counter() - start
        print(f"...movies are loaded, in {round(time_taken, 2)}s!")

        # Close the browser once the action is complete
        browser.close()


# Execute the function
custom_wait_demo()
