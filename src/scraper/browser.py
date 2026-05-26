from playwright.sync_api import sync_playwright


def start_browser(headless=False):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    return playwright, browser, page


def close_browser(playwright, browser):
    browser.close()
    playwright.stop()

