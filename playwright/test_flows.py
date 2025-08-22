from playwright.sync_api import expect
import pytest

@pytest.mark.skip(reason="Skipping this test for now")
def test_rahulshettyCart(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.fill("//input[@id='userEmail']", "rahulsingh@test.com")
    page.fill("//input[@id='userPassword']", "Test@123")
    page.get_by_role("button", name="Login").click()

    page.locator(".card-body").filter(has_text="ZARA COAT 3") \
        .get_by_role("button", name="Add To Cart").click()
    page.wait_for_timeout(2000)

    page.locator(".card-body").filter(has_text="ADIDAS") \
        .get_by_role("button", name="Add To Cart").click()
    page.wait_for_timeout(2000)

    page.locator(".btn-custom").filter(has_text="Cart").click()
    page.wait_for_timeout(2000)

    expect(page.locator(".cartWrap.ng-star-inserted")).to_have_count(2)

    # Proceed to checkout
    page.get_by_role("button", name="Checkout").click()
    page.get_by_placeholder("Select Country").type("India")

    # Wait for dropdown results to appear
    page.wait_for_selector("//button[normalize-space()='India']")
    page.locator("//button[normalize-space()='India']").first.click()

    page.locator(".actions a").click()
    expect(page.locator('//label[contains(text(),"Order")]/following::label')).to_have_count(2)

    page.close()
    context.close()
    browser.close()
@pytest.mark.skip(reason="Skipping this test for now")
def test_childWindows(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as popup_info:
        page.locator("a", has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
        childPage = popup_info.value
        text = childPage.locator(".red").text_content()
        # email = text.split("at")[1].strip()
        childPage.close()
    page.close()
    context.close()
    browser.close()

# def test_alrt(playwright):
#     browser = playwright.webkit.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    
#     # Click the alert button
#     page.get_by_role("button", name="Alert").click()
    
#     # Handle the alert
#     with page.expect_popup() as popup_info:
#         page.on("dialog", lambda dialog: dialog.accept())
#     page.wait_for_timeout(3000)
#     page.close()
#     context.close()
#     browser.close()


def test_frames(playwright):

    browser = playwright.webkit.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    

    # page.evaluate("window.scrollBy(0, 1000)")  # Scroll down to make the iframe visible

    # # Switch to the frame
    # frame = page.frame_locator("courses-iframe")
    
    # # Click the link inside the frame
    # # frame.wait_for_timeout(2000)
    # frame.locator("//div[@class='nav-outer clearfix']//a[normalize-space()='Courses']").click()
    
    # # Wait for a while to see the result
    # page.wait_for_timeout(3000)
    
    #WEbtables

    name = ["Ivory","Jack","Alex"]
    for i in name:
        price = page.locator("//*[contains(text(),'{}')]/following-sibling::td[3]".format(i)).text_content()
        print(i, " ", price)

    #MouseHover
    page.locator("#mousehover").hover()

    page.screenshot(path="screenshots/mouse-2.png")


    page.close()
    context.close()
    browser.close()

    
