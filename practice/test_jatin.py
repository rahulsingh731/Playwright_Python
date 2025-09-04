from playwright.sync_api import Playwright
import pytest
import datetime
import calendar


class YatraPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.yatra.com")
        self.close_popup()
        self.open_calendar()

    def close_popup(self):
        try:
            self.page.locator(
                '//section//span[starts-with(@class,"style_cross")]/img[@alt="cross"]'
            ).click(timeout=2000)
        except:
            print("No popup found")

    def open_calendar(self):
        self.page.locator("//div[@class='css-w7k25o']").click()

    def get_visible_months(self):
        """Return all visible month names currently rendered in the calendar"""
        months = self.page.locator('span.react-datepicker__current-month')
        return [m.text_content() for m in months.element_handles()]


    def click_next_month(self):
        next_button = self.page.locator('//button[contains(@class,"react-datepicker__navigation--next") and not(contains(@style, "visibility: hidden;"))]')
        if next_button.is_visible():
            next_button.click()
            return True
        return False
    
    def scrape_all_months(self, start_day: int = None):
        """Traverse all months by clicking next until button disappears"""
        all_prices = {}
        seen_months = set()

        while True:
            months = self.get_visible_months()
            for m in months:
                if m not in seen_months:
                    seen_months.add(m)
                    # if current month, start from today
                    if start_day and m.startswith(datetime.datetime.now().strftime("%B")):
                        prices = self.get_price_list(m, start_day)
                    else:
                        prices = self.get_price_list(m, 1)
                    all_prices.update(prices)

            if not self.click_next_month():
                break

        return all_prices

    def get_price_list(self, month: str, start_day: int = 1):
        price_list = {}
        # parse month-year safely
        dt = datetime.datetime.strptime(month, "%B %Y")
        days_in_month = calendar.monthrange(dt.year, dt.month)[1]

        for i in range(start_day, days_in_month + 1):
            month = str(month.split(" ")[0])
            day = str(i).zfill(2)
            try:
                raw_price = self.page.locator(
                f'//div[contains(@aria-label,"{month}")]//span[contains(text(),"{day}")]/span'
            ).text_content(timeout=1000)

                if raw_price:
                    clean_price = raw_price.replace("₹", "").replace(",", "").strip()
                    try:
                        price_list[f"{day}-{month}"] = int(clean_price)
                    except ValueError:
                        print(f"Skipping invalid price {raw_price} for {day}-{month}")
            except:
                print("There's no price for", day, month)
        return price_list

    def get_cheapest_date(self, month: str, start_day: int = 1):
        price_list = self.get_price_list(month, start_day)
        if not price_list:
            return None, None
        best_day, best_price = min(price_list.items(), key=lambda x: x[1])
        return best_day, best_price

    def book_cheapest(self, day: str, month: str):
        self.page.locator(
            f'//div[contains(@aria-label,"{month}")]//span[contains(text(),"{day}")]/span'
        ).click()
        print(f"Booked for {day}-{month}")


def test_assignment(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yatra = YatraPage(page)

    # Open site
    yatra.open()
    
    today = int(datetime.datetime.now().strftime("%d"))
    all_prices = yatra.scrape_all_months(start_day=today)

    if all_prices:
        cheapest_day, cheapest_price = min(all_prices.items(), key=lambda x: x[1])
        print(f"Cheapest overall: {cheapest_day} with price {cheapest_price}")
    else:
        print("No prices found")

    page.wait_for_timeout(2000)
    page.close()
    context.close()
    browser.close()
