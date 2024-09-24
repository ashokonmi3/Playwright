from playwright.sync_api import sync_playwright, expect


def verify_chrome_cpu_value(page):
    """
    Test Case: Ensuring the CPU value for Chrome matches the displayed value in a dynamic table.

    This test demonstrates how to extract and verify values from a dynamically generated table.

    Scenario:
    1. Navigate to a page with a dynamic table.
    2. Extract the CPU percentage from the warning label.
    3. Locate the CPU column header.
    4. Find the row for "Chrome" and verify its CPU value.
    """

    # Step 1: Navigate to the dynamic table test page
    print("Navigating to the dynamic table page...")
    page.goto("http://uitestingplayground.com/dynamictable")

    # Step 2: Extract the CPU percentage from the warning label
    label = page.locator("p.bg-warning").inner_text()
    print(f"Extracted label text: {label}")
    # Get the last word which is the CPU percentage
    # label = " Chrome CPU: 5.7%"
    print(label.split())  # [Chrome,CPU:,5.7%]
    print(label.split()[-1])

    percentage = label.split()[-1]

    print(f"CPU Percentage extracted: {percentage}")

    # Step 3: Locate all column headers and find the index for the CPU column
    column_headers = page.get_by_role("columnheader")
    cpu_column = None

    for index in range(column_headers.count()): # column_header.count() = 5  for i in range(5)
        column_header = column_headers.nth(index)
        if column_header.inner_text() == "CPU":
            cpu_column = index
            print(f"Found CPU column at index: {cpu_column}")
            break

    # Ensure CPU column is found
    assert cpu_column is not None, "CPU column not found!"

    # Step 4: Locate the row group for values and find the Chrome row
    rowgroup = page.get_by_role("rowgroup").last
    chrome_row = rowgroup.get_by_role("row").filter(has_text="Chrome")
    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    # Step 5: Verify the CPU value for Chrome matches the extracted percentage
    print("Verifying CPU value for Chrome...")
    expect(chrome_cpu).to_have_text(percentage)
    print("CPU value for Chrome verified successfully!")


# Use Playwright to execute the test
with sync_playwright() as playwright:
    """
    Executes the test scenario for verifying CPU values in a dynamic table.
    """

    # Launch the Chromium browser with slow motion for better visualization
    print("Launching the browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    # Create a new browser context and page
    print("Creating a new browser context and page...")
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()

    # Run the test case on the page
    print("Running the test case...")
    verify_chrome_cpu_value(page)

    # Close the browser after the test completes
    print("Closing the browser...")
    browser.close()

    print("Test execution completed.")

    """
    Important Notes for Learning:
    - **Dynamic Table Handling**: This example demonstrates how to work with dynamic tables 
      and extract values for verification.
    - **Assertions**: Using Playwright’s `expect` API ensures that the CPU value matches 
      the expected output.
    """
