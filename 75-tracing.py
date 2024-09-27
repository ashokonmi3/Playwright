import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
# browser_type_launch_args will be taken as command line argument this will be called autometically.
# This matching name(browser_type_launch_args) is used to capture and modify the browser launch arguments
#  passed to Playwright when tests are run.
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }


def test_page_has_docs_link(page: Page):
    page.goto("http://playwright.dev/python")

    docs_link = page.get_by_role("link1", name="Docs")

    expect(docs_link).to_be_visible()


def test_visits_google_account(page: Page):
    page.goto("https://accounts.google.com")


# pytest --tracing on .\75-tracing.py
# pytest --video on .\75-tracing.py
# pytest --screenshot on .\75-tracing.py # at end of test
# pytest --screenshot only-on-failure .\75-tracing.py # at end of test
