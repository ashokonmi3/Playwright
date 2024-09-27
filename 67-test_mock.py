from playwright.sync_api import *


def on_api_call(route: Route):
    response = route.fetch()
    user_data = response.json()
    print("*******"*10)
    print(user_data["lastName"])

    user_data["lastName"] = "Smith"
    user_data["age"] = 20

    route.fulfill(
        response=response,
        json=user_data,
    )


def test_user_api(page: Page):
    USERS_API_URL = "https://dummyjson.com/users/1"

    page.route(USERS_API_URL, on_api_call)

    response = page.goto(USERS_API_URL)
    print("######"*10)
    data = response.json()
    print(data["lastName"])

    print("Got data:", response.json())
