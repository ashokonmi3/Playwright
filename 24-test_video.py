import pytest
from playwright.sync_api import Browser, Page
from playwright.sync_api import sync_playwright


# Test Duration:
# The video duration is determined by how long your test runs. If your test takes an hour to complete,
# the video will capture the entire hour. There’s no built-in time limit on video recording.

# Storage Space:
# Long test runs will generate large video files. Be mindful of the available storage on your machine,
# as very long tests may consume a significant amount of disk space.

# Performance Impact:
# Recording long videos may impact performance, especially if the test runs for an extended period.
# This is something to monitor if you plan to record videos for lengthy tests.

# File Size:
# The longer the recording, the larger the video file. Ensure that your disk has enough space to
# handle the size of long-running test recordings.

# URL to verify after navigation
DOCS_URL = "https://playwright.dev/python/docs/intro"

# Function for testing the page and recording a video


def test_page_has_get_started_link():
    """
    This function navigates to the Playwright Python documentation page, 
    switches the theme, and clicks the 'GET STARTED' link. It also records a video 
    of the entire session.
    """

    # Start the Playwright session
    with sync_playwright() as playwright:
        # Launch the browser in non-headless mode with slow motion for better visibility
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000, args=["--start-maximized"]
        )

        # Create a browser context with video recording enabled
        # Video will be saved in the specified directory ('video/')
        context = browser.new_context(
            record_video_dir="video/"
        )

        # Create a new page (tab)
        page = context.new_page()

        # Navigate to the Playwright Python documentation website
        page.goto("https://playwright.dev/python")

        # Locate the button to switch between dark and light mode
        theme_btn = page.get_by_title(
            "Switch between dark and light mode (currently dark mode)"
        )

        # Click the theme switch button
        theme_btn.click()

        # Find the 'GET STARTED' link by its role and name
        link = page.get_by_role("link", name="GET STARTED")
        link.click()

        # Assert that the page navigates to the expected URL
        assert page.url == DOCS_URL

        # After the function finishes, the video will be saved in the "video/" directory


# Call the function to run the test
test_page_has_get_started_link()

# Additional Notes:
# - Ensure that the 'video/' directory exists before running the test to avoid any errors during video recording.
# - Adjust the 'slow_mo' parameter as needed to achieve the desired visibility during test execution.
# Playwright does not allow changing the video format directly. By default, videos captured in Playwright are saved in WebM format, which is widely supported for web media.
# context = browser.new_context(
#     record_video_dir="videos/",  # Video will be saved in WebM format
#     viewport=None  # This removes any viewport restrictions (full screen)
# )
# Interview Questions:
"""
1. How does the `record_video_dir` parameter work in Playwright?
   Answer: The `record_video_dir` parameter specifies the directory where the recorded videos will be saved. 
   Each video is associated with a browser context and is saved after the context is closed.

2. What considerations should you keep in mind when recording videos of tests?
   Answer: Consider the duration of the tests, available storage space, potential performance impact, 
   and the file size of the recordings. Long tests can create large video files and may affect the performance of the test run.

3. How do you ensure that the video recording does not impact the test's performance?
   Answer: You can monitor the performance during the test execution and adjust the complexity of the tests 
   or the length of the recordings as necessary. Additionally, running tests on a dedicated testing environment can help minimize impact.
"""
