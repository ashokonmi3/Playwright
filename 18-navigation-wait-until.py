from playwright.sync_api import sync_playwright
from time import perf_counter


def measure_page_load_time(wait_until_option):
    """
    Measures the time taken for a page to load based on the 'wait_until' option.
    Returns the time taken.
    """
    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True
        )
        page = context.new_page()

        # Start the timer
        start = perf_counter()

        # Navigate to the page and wait for the condition specified by `wait_until`
        page.goto(
            "https://playwright.dev/python/",
            wait_until=wait_until_option
        )

        # Measure time taken
        time_taken = perf_counter() - start
        print(f"Page loaded with wait_until = '{
              wait_until_option}' in {round(time_taken, 2)} seconds")

        # Close the browser
        browser.close()

        return time_taken


if __name__ == "__main__":
    # List of wait_until options to test
    wait_until_options = ['commit', 'domcontentloaded', 'load', 'networkidle']

    # Dictionary to store the load times with respective wait_until option
    load_times = {}

    # Loop through each wait_until option and measure page load time
    for option in wait_until_options:
        time_taken = measure_page_load_time(option)
        load_times[option] = time_taken

    # Find the max and min load times
    max_time_option = max(load_times, key=load_times.get)
    min_time_option = min(load_times, key=load_times.get)

    print("\n--- Summary ---")
    print(f"Maximum load time: {round(
        load_times[max_time_option], 2)} seconds with wait_until = '{max_time_option}'")
    print(f"Minimum load time: {round(
        load_times[min_time_option], 2)} seconds with wait_until = '{min_time_option}'")


# Options for wait_until:
# 'commit':

# Waits until the first byte of the response is received from the server. The page content may not be fully loaded yet.
# This is the fastest option and waits for the bare minimum.
# 'domcontentloaded':

# Waits until the HTML is parsed, and the DOMContentLoaded event is fired. This means that the HTML is parsed and any < script > tags are executed.
# The page is considered interactive at this point, but external resources like images and stylesheets might still be loading.
# 'load' (default):

# Waits for the full page load, including all resources such as images, stylesheets, and iframes.
# This option ensures the entire page, along with its resources, is fully loaded and displayed.
# 'networkidle':

# Waits until there are no network requests for at least 500 milliseconds, meaning the page is completely loaded and no further requests are being made(e.g., for AJAX calls or other asynchronous resources).
# This is useful for more complex pages that continue to load resources after the initial page load.
