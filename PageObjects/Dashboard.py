from PageObjects.OrdersPage import OrdersPage


class Dashboard:

    def __init__(self,page):
        self.page = page
    
    def selectOrdersNavLink(self):
        self.page.locator("//button[@routerlink='/dashboard/myorders']").click()
        return OrdersPage(self.page)