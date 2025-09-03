from playwright.sync_api import sync_playwright,Page, expect
import pytest


def test_1(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.amazon.in/s?k=iphone&crid=3EXJWEEB2S7HG&sprefix=iphon%2Caps%2C222&ref=nb_sb_noss_2")
    # black_iphones_cards = page.locator("//span[contains(text(),'Black')]/ancestor::div[contains(@class,'a-spacing-top-small')]")
    iphones_cards = page.locator("div.a-section.a-spacing-small.a-spacing-top-small").filter(has_text="Apple iPhone 15")
    count = iphones_cards.count()

    print("total count",count)

    for i in range(count):

        product = iphones_cards.nth(i)

        product.scroll_into_view_if_needed()

        add_button = product.locator("button[id*='a-autoid']")

        if add_button.is_visible():
            add_button.click()
            page.wait_for_timeout(5000)
            print("Added product to cart",i+1)
        else:
            print("Not Found")
            break
    page.screenshot(path="./screenshots/cart.png")
    page.wait_for_timeout(2000)
    page.close()
    context.close()
    browser.close()