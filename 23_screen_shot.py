from playwright.sync_api import sync_playwright


# def take_full_page_screenshot():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://bootswatch.com/default/")

#         # Take a screenshot of the entire page
#         page.screenshot(
#             path=r"visible_page_screenshot.png", full_page=False)

#         browser.close()


# take_full_page_screenshot()
# ==============================
# from playwright.sync_api import sync_playwright


# def take_element_screenshot():
#     """
#     Takes a screenshot of a specific element on a webpage.

#     This function navigates to the given URL and captures a screenshot
#     of the <h1> element. When you take a screenshot of an element using
#     Playwright, it captures only the visible portion of that specific
#     element, including any styling applied to it (like borders or shadows).
#     The screenshot will not include anything outside of that element,
#     such as surrounding elements, text, or the overall webpage layout.

#     Key Points:
#     -----------
#     - Element Boundaries: Only the area defined by the element’s dimensions will be captured.
#     - Visibility: If part of the element is hidden (e.g., due to scrolling),
#       only the visible part will be included in the screenshot.
#     - Element Type: Regardless of whether the element is a div, image, or
#       any other type, the screenshot will reflect the specific area occupied
#       by that element.

#     Notes:
#     ------
#     - The screenshot is saved as 'element_screenshot.png'.
#     """
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://example.com")

#         # Locate the element
#         element = page.locator("h1")  # Change the selector as needed

#         # Take a screenshot of the specific element
#         element.screenshot(path="element_screenshot.png")

#         browser.close()


# take_element_screenshot()

# ======================


# def take_full_page_screenshot():
#     """
#     Takes a full-page screenshot of a specified webpage.

#     This function navigates to the given URL and captures the entire
#     scrollable area of the page.

#     Notes:
#     ------
#     - The screenshot is saved as 'full_page_screenshot.png'.
#     """
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://bootswatch.com/default/")

#         # Take a screenshot of the entire page
#         page.screenshot(path="full_page_screenshot.png", full_page=True)

#         browser.close()


# take_full_page_screenshot()
# # ================


def take_custom_screenshot():
    """
    Takes a custom screenshot of a webpage with specified options.

    This function navigates to a given URL and captures both the full
    page and the visible portion of the page.

    Notes:
    ------
    - The first screenshot is a full-page capture.
    - The second screenshot captures only the visible portion of the page.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://bootswatch.com/default/")

        # Take a full page screenshot without background
        page.screenshot(path="full_page_custom_screenshot.png",
                        full_page=True, omit_background=False)

        # Take a screenshot of the visible viewport
        page.screenshot(path="viewport_custom_screenshot.png",
                        full_page=False, omit_background=True)

        browser.close()


take_custom_screenshot()
# =================
# In Playwright, the omit_background parameter in the page.screenshot() method specifies whether to capture the screenshot without the background color of the page. Here's a breakdown:

# omit_background=True: The screenshot will be taken with a transparent background. This is useful when you want to overlay the screenshot on a different background or if the background color of the page is not needed.

# omit_background=False: The screenshot will include the background color of the page as it appears in the browser. This is the default behavior.

# Using omit_background=True can be particularly beneficial when you're capturing UI components that you plan to use in different contexts or background
# page.screenshot(path="screenshot.jpg", type="jpeg")
# type: You can specify either 'png' or 'jpeg'. If the type is not provided, Playwright defaults to png.
