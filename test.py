from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="screenshot.png")
    page.wait_for_timeout(2000)
    browser.close()