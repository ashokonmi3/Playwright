import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.mark.only_browser("firefox")
def test_chromium_only(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()


@pytest.mark.skip_browser("firefox")
def test_skip_firefox(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()


@pytest.mark.browser("firefox")
def test_firefox_only(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()


@pytest.mark.parametrize("browser_name", ["firefox", "webkit"])
def test_all_browser(page, browser_name):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.close()


# pytest -v --browser=chromium .\54-browser_marker.py
# pytest -v --browser=firefox .\54-browser_marker.py
