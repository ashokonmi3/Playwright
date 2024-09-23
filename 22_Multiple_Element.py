from playwright.sync_api import sync_playwright


def find_elements_by_attribute():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a sample page
        page.goto("https://bootswatch.com/default/")

        # Find all elements with a specific attribute value
        # element = page.locator("//h1[contains(text(),'Head')]")

        button = page.get_by_role('button')
        # Count the number of elements found
        count = button.count()
        print(f"Found {count} elements with button.")
        print(f"First element test is {button.first.text_content()}")
        # Iterate over each element
        for i in range(count):
            element = button.nth(i)
            print(f"Element {i}: {element.text_content()}")

        # Close the browser
        browser.close()


if __name__ == "__main__":
    find_elements_by_attribute()
