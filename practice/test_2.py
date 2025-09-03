from playwright.sync_api import Playwright
import pytest

def test_childwindows(playwright:Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    
    with page.expect_popup() as popup_info:
        page.locator(".blinkingText[href='https://rahulshettyacademy.com/documents-request']").click()
        childpage = popup_info.value
        text = childpage.locator(".red").text_content()
        print(type(text ))
    page.wait_for_timeout(2000)
    context.close()
    browser.close()


@pytest.mark.skip
def test_alerts(playwright:Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/js-dialogs")
    
    # Click the alert button
    
    # Handle the alert
    
    page.locator("button#js-confirm").click()
    page.on("dialog", lambda dialog: dialog.accept())
    text = page.locator("p#dialog-response").text_content()
    assert text == "Cancel"
    page.wait_for_timeout(1000)
    page.close()
    context.close()
    browser.close()

def test_frames(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/Frames.html")

    pageframe = page.frame_locator("#singleframe")
    pageframe.locator("input").fill("Hello World")
    page.screenshot(path="./screenshots/frames.png")
    page.wait_for_timeout(3000)

    page.close()
    context.close()
    browser.close()

def test_scroll(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/infinite_scroll")
    i=10
    while i>0:
        page.mouse.wheel(delta_x=0, delta_y=500)
        page.screenshot(path = "./screenshots/scrollbottom{}.png".format(i)) #./screenshots/scrollbottom{}.png")
        page.wait_for_timeout(1000)
        i-=1;
        
    
    page.wait_for_timeout(1000)
    page.close()
    context.close() 
    browser.close()
