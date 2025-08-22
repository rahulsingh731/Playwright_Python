# import playwright
from playwright.sync_api import Page
import pytest

def test_PositiveFlow(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("//input[@id='username']", "student")
    page.fill("//input[@id='password']", "Password123")
    page.click("//button[@id='submit']")
    assert page.url == "https://practicetestautomation.com/logged-in-successfully/"
    page.wait_for_timeout(2000)  # Wait for results to load
    page.close()
    context.close()
    browser.close()

def test_NegativeFlow_1(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("//input[@id='username']", "student")
    page.fill("//input[@id='password']", "Password1234")  # Incorrect password
    page.click("//button[@id='submit']")
    assert page.text_content("//div[@id='error']") == "Your password is invalid!"
    page.wait_for_timeout(2000)  # Wait for results to load
    page.close()
    context.close()
    browser.close()
@pytest.mark.smoke
def test_NegativeFlow_2(page:Page):

    #pass --headed in terminal to run the test in headed mode
    # Here, I am using the page fixture directly instead of playwright
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("//input[@id='username']", "student123")
    page.fill("//input[@id='password']", "Password123")  # Incorrect password
    page.get_by_role("button", name="Submit").click()
    assert page.text_content("//div[@id='error']") == "Your username is invalid!"
    page.wait_for_timeout(2000)
    # page.get_by_role("link", name="CONTACT").click()
    # page.wait_for_timeout(2000)
    # No need to close context and browser here, as the page fixture handles it
@pytest.mark.validations
def test_PositiveFlow_2(page:Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.fill("//input[@id='firstName']", "John")
    page.fill("//input[@id='lastName']", "Doe")
    page.fill("//input[@id='userEmail']", "john.doe@example.com")
    page.fill("//input[@id='userNumber']", "1234567890")
    page.click("//label[@for='gender-radio-1']")
    page.click("//div[contains(text(),'Select State')]")
    page.click("//div[text()='NCR']")
    page.click("//div[contains(text(),'Select City')]")
    page.click("//div[text()='Delhi']")
    page.click("//button[@id='submit']")
    page.wait_for_timeout(2000)
    # assert "Thanks for submitting the form" in page.text_content("//div[@class='modal-body']")
    page.screenshot(path="form_submission.png")