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

    def get_price_list(self, month: str, start_day: int = 1):
        price_list = {}
        # calculate days in month (for Feb, April, etc.)
        year = datetime.datetime.now().year
        month_num = datetime.datetime.strptime(month, "%B").month
        days_in_month = calendar.monthrange(year, month_num)[1]

        for i in range(start_day, days_in_month + 1):
            day = str(i).zfill(2)
            raw_price = self.page.locator(
                f'//div[contains(@aria-label,"{month}")]//span[contains(text(),"{day}")]/span'
            ).text_content(timeout=3000)

            if raw_price:
                clean_price = raw_price.replace("₹", "").replace(",", "").strip()
                try:
                    price_list[day] = int(clean_price)
                except ValueError:
                    print(f"Skipping invalid price for {day}: {raw_price}")
            else:
                print(f"No price found for {day}")
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

    # Dates
    today = int(datetime.datetime.now().strftime("%d"))
    current_month = datetime.datetime.now().strftime("%B")
    next_month = (datetime.datetime.now() + datetime.timedelta(days=31)).strftime("%B")

    # Cheapest this month (start from today)
    best_day_curr, best_price_curr = yatra.get_cheapest_date(current_month, today)

    # Cheapest next month (start from 1)
    best_day_next, best_price_next = yatra.get_cheapest_date(next_month, 1)

    if best_day_curr and best_day_next:
        if best_price_curr < best_price_next:
            yatra.book_cheapest(best_day_curr, current_month)
            print(f"Cheapest in {current_month}: {best_day_curr} @ {best_price_curr}")
        else:
            yatra.book_cheapest(best_day_next, next_month)
            print(f"Cheapest in {next_month}: {best_day_next} @ {best_price_next}")

    page.wait_for_timeout(2000)
    page.close()
    context.close()
    browser.close()
