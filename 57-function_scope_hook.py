import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
    """
    Fixture that navigates to the Playwright Python documentation page.

    This fixture automatically runs before each test in the module,
    ensuring that the page is set up correctly for testing. It also
    handles teardown by closing the page after the test is executed.

    Args:
        page (Page): The Playwright Page object representing the browser page.

    Yields:
        Page: The current Page object after navigating to the specified URL.

    Teardown:
        Closes the page after the test completes.
    """
    print("Launching the website")
    page.goto("https://playwright.dev/python")
    yield page
    page.close()
    print("\n[ Fixture ]: page closed!")


def test_page_has_docs_link(visit_playwright: Page):
    """
    Test that verifies the visibility of the Docs link on the Playwright page.

    Args:
        visit_playwright (Page): The page object from the fixture.
    """
    link = visit_playwright.get_by_role("link", name="Docs")
    assert link.is_visible()


def test_get_started_visits_docs(visit_playwright: Page):
    """
    Test that checks clicking the Get Started link redirects to the Docs page.

    Args:
        visit_playwright (Page): The page object from the fixture.
    """
    link = visit_playwright.get_by_role("link", name="GET STARTED")
    link.click()
    assert visit_playwright.url == DOCS_URL


#  Questions
# 1. What is a fixture in pytest?
#    Answer: A fixture in pytest is a reusable piece of code that sets up a precondition for tests.
# 2. How do you define a fixture in pytest?
#    Answer: A fixture is defined using the @pytest.fixture decorator.
# 3. What does the yield statement do in a fixture?
#    Answer: The yield statement allows the fixture to provide a value to the test and define a teardown section.
# 4. What is the significance of the scope parameter in a fixture?
#    Answer: The scope parameter defines how long the fixture will be alive, such as function, class, module, or session.
# Parameter Declaration: By declaring visit_playwright: Page in the test function, you are indicating that this test will utilize the Page object provided by the visit_playwright fixture. This allows you to interact with the browser page in your test.
