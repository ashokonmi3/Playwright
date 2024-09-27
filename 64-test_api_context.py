from playwright.sync_api import *


def test_users_api(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    response = api_context.get("/users/1")

    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"
    api_context.dispose()


1 passed in 1.42s
1 passed in 12.86s

# In Playwright, request.new_context() is a method used to create a new request context.
# This context allows you to manage HTTP requests independently from other contexts,
#  which is particularly useful when you need to customize request settings or manage cookies and authentication.


# Key Features of request.new_context()
# Isolation of Requests: Each request context operates independently.
#  This means that cookies, headers, and other settings will not interfere with other contexts,
# allowing for clean testing scenarios.

# Custom Configuration: You can customize headers, user agent strings,
# and other settings specific to the request context. This is useful for testing APIs
#  with different authentication mechanisms or for simulating requests from different devices.

# Cookie Management: Each context can manage its own cookies. This is useful for testing scenarios that require different sessions or user states.

# Network Interception: Request contexts can also be used for intercepting network requests,
#  enabling you to modify requests and responses on the fly.
