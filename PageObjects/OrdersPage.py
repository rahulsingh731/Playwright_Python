class OrdersPage:
    def __init__(self,page):
        self.page = page

    def get_orders(self):
        return self.page.locator("tr.ng-star-inserted th").all_text_contents()