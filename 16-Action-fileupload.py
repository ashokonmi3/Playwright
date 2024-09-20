import time
from playwright.sync_api import sync_playwright


# def test_file_upload():
#     """
#     Demonstrates how to interact with file upload inputs using Playwright.

#     File Upload Interaction Notes:
#     ------------------------------
#     In Playwright, you can perform actions on file input elements to upload files:
#     - `set_input_files`: Sets the files to be uploaded by the file input element.

#     Basic Actions:
#     --------------
#     - `element.set_input_files(file_path)`: Sets the file to be uploaded by the file input element.
#     - `element.set_input_files([file_path1, file_path2, ...])`: Sets multiple files to be uploaded by the file input element.

#     Workflow:
#     ----------
#     1. Launches a browser in non-headless mode with a slow motion delay of 500ms.
#     2. Creates a new page and navigates to a page with a file input element.
#     3. Sets the viewport size to 1920x1080 pixels.
#     4. Waits for 2 seconds to ensure the page is fully loaded.
#     5. Scrolls down the page to make sure the file input element is visible.
#     6. Interacts with the file input element to upload files.
#     7. Closes the browser.

#     Examples:
#     ----------
#     - Example 1: Upload a single file.
#     - Example 2: Upload multiple files.
#     """
#     with sync_playwright() as playwright:
#         # Launch a browser in non-headless mode with a slow motion delay of 500ms
#         browser = playwright.chromium.launch(
#             headless=False, slow_mo=3000, args=["--start-maximized"]
#         )
#         context = browser.new_context(
#             ignore_https_errors=True, no_viewport=True
#         )
#         page = context.new_page()

#         # Visit the website with a file input element
#         page.goto("https://bootswatch.com/default/")

#         # Wait for 2 seconds to ensure the page is fully loaded
#         time.sleep(2)

#         # Locate the file input element by its ID and upload a file
#         file_input = page.locator("input[type='file']")
#         file_input.scroll_into_view_if_needed()

#         # file_input.set_input_files("8-Locator-css.py")
#         file_input.set_input_files(
#             "D:\\Study\\Playwright\\python-playwright\\test.txt")

#         # file_input.set_input_files(
#         #     r"D:\Study\Playwright\python-playwright\test.txt")

#         # file_input.set_input_files(["8-Locator-css.py", "1.txt"]) # To upload multiple files here it will not work

#         # Wait for a few seconds to observe the file upload
#         time.sleep(5)

#         # Optionally, you can verify if the file upload was successful
#         # For example, check if the file name appears in the UI

#         # Close the browser
#         browser.close()


# # Execute the function
# test_file_upload()

# ======================
def test_file_upload():
    """
    Demonstrates how to interact with file upload inputs using Playwright.

    File Upload Interaction Notes:
    ------------------------------
    In Playwright, you can perform actions on file input elements to upload files:
    - `set_input_files`: Sets the files to be uploaded by the file input element.
    - `page.expect_file_chooser()`: Handles file chooser dialogs that appear when interacting with file inputs.

    Basic Actions:
    --------------
    - `element.set_input_files(file_path)`: Sets the file to be uploaded by the file input element.
    - `element.set_input_files([file_path1, file_path2, ...])`: Sets multiple files to be uploaded by the file input element.
    - `page.expect_file_chooser()`: Waits for and handles file chooser dialogs, allowing you to specify files to be selected.

    Workflow:
    ----------
    1. Launches a browser in non-headless mode with a slow motion delay of 3000ms.
    2. Creates a new page and navigates to a page with a file input element.
    3. Waits for 2 seconds to ensure the page is fully loaded.
    4. Locates the file input element and triggers the file chooser dialog.
    5. Sets the files to be uploaded in the file chooser.
    6. Waits for 5 seconds to observe the file upload.
    7. Closes the browser.

    Examples:
    ----------
    - Example 1: Upload a single file by setting the file path directly.
    - Example 2: Handle file chooser dialogs and specify files to upload.
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

        # Visit the website with a file input element
        page.goto("https://bootswatch.com/default/")

        # Wait for 2 seconds to ensure the page is fully loaded
        time.sleep(2)

        # Locate the file input element
        file_input = page.locator("input[type='file']")
        file_input.scroll_into_view_if_needed()

        # Interact with the file input element

     
        with page.expect_file_chooser() as fc_info:
            file_input.click()  # Trigger the file chooser dialog
        file_chooser = fc_info.value
        print(f"fc_info.value : {fc_info.value}")
        # Set the file to be uploaded
        file_chooser.set_files("1-interactive.txt")

        # Wait for a few seconds to observe the file upload
        time.sleep(5)

        # Close the browser
        browser.close()


# Execute the function
test_file_upload()
