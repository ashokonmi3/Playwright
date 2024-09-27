from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Set geolocation to London
    context.set_geolocation({"latitude": 51.5074, "longitude": -0.1278})

    # Optionally, grant geolocation permissions
    context.grant_permissions(["geolocation"])

    page = context.new_page()
    page.goto("https://example.com")  # Replace with your app's URL

    # Retrieve the geolocation values set in the browser using a Promise
    latitude = page.evaluate("""
        new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                (position) => resolve(position.coords.latitude),
                (error) => reject(error)
            );
        });
    """)

    longitude = page.evaluate("""
        new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                (position) => resolve(position.coords.longitude),
                (error) => reject(error)
            );
        });
    """)

    # Validate the set geolocation values
    expected_latitude = 51.5074
    expected_longitude = -0.1278

    assert latitude == expected_latitude, f"Expected latitude {
        expected_latitude}, but got {latitude}"
    assert longitude == expected_longitude, f"Expected longitude {
        expected_longitude}, but got {longitude}"

    print(f"Geolocation is set correctly: Latitude: {
          latitude}, Longitude: {longitude}")

    # Example: Test if a location-based service loads correctly
    # Your test logic here, e.g., check for content specific to London

    context.close()
    browser.close()
