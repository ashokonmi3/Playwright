from playwright.sync_api import sync_playwright


def on_download(download):
    """
    Event handler that is triggered when a download starts.

    Parameters:
    - download: A Playwright Download object representing the file being downloaded.

    This function saves the downloaded file as 'night.jpg'.
    """
    print("Download received!")
    # Saves the downloaded file after completion.
    download.save_as("night21.jpg")


def test_download():
    """
    Demonstrates how to handle file downloads in Playwright.

    Download Event Notes:
    ---------------------
    - The download event is triggered when Playwright detects a file download initiation.
    - This occurs when the server responds with a 'Content-Disposition: attachment' header or 
      when a file link is clicked that starts the download.
    - You can capture the download event using `page.expect_download()`, which gives access to
      a download object containing metadata and methods to handle the file.
      Timeout for Download Start:

When you use page.expect_download(timeout=...), the timeout defines how long Playwright will wait for the download to start (i.e., when the download is triggered by clicking a button or link).
If the download does not start within the specified timeout, Playwright raises a TimeoutError.
No Timeout for Download Completion:

Once the download starts, Playwright does not impose any timeout for how long it takes to complete the download.
Playwright will wait for the download to finish regardless of how long it takes (even if it's a large file).
The download.save_as() function can only be used after the download is fully completed.

    Key Playwright Features Demonstrated:
    -------------------------------------
    1. Browser interaction in non-headless mode with slow-motion.
    2. How to capture the download event using `page.once('download')` listener.
    3. Triggering and handling file download in a web page.
    4. `save_as()` method will only be callable after the download completes.

    Example Workflow:
    -----------------
    1. Open browser and navigate to the target URL.
    2. Register an event listener for the download.
    3. Trigger the download action using a button click.
    4. Handle the download and save the file locally after download completion.
    """
    with sync_playwright() as playwright:
        # Launch a browser in non-headless mode with a slow motion delay of 3000ms
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )
        context = browser.new_context(
            ignore_https_errors=True, no_viewport=True
        )
        page = context.new_page()

        # Navigate to the page where a file download can be triggered
        page.goto("https://unsplash.com/photos/NDRwHCC7JuI")

        # Register listener for the download event
        # This will trigger as soon as the download starts, but the file is saved only after it completes.
        page.once("download", on_download)

        # Locate and click the 'Download free' button
        btn = page.get_by_role("link", name="Download free")

        # Expect a download to happen after the button click
        # download_info captures metadata related to the download
        # Timeout set to 60 seconds
        with page.expect_download(timeout=60000) as download_info:
            btn.click()  # Trigger download by clicking the button

        # download = download_info.value
        # download.save_as("moon.jpg")  # Save the downloaded file

        # Close the browser after the actions are completed
        browser.close()


# Execute the function to demonstrate the download feature
test_download()
