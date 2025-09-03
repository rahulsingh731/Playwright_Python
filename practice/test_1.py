from playwright.sync_api import sync_playwright,Page, expect
import pytest
@pytest.mark.skip
def test_website(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.locator("input#username").click()

    page.keyboard.press("Shift+A")

    page.wait_for_timeout(2000)

    page.locator("input#password").fill("Password123")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("text=Logged in successfully")).to_be_visible()

    page.wait_for_timeout(1000)
    page.screenshot(path="./screenshots/screenshot_1.png")

    page.wait_for_timeout(2000)

    page.close()
    context.close()
    browser.close()

def test_2(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshetty")
    page.get_by_label("Password:").fill("learning")
    # page.get_by_role("radio").locator("input[value='admin']").check()
    page.get_by_role("combobox").select_option("teach")
    page.locator("input#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()
    page.screenshot(path="./screenshots/screenshot_2.png")
    page.close()
