from PageObjects.Dashboard import Dashboard


class LoginPage:



    def __init__(self,page,url):
        self.page = page
        self.url = url

    def goto(self):
        self.page.goto(self.url)
    
    def login(self, email,password):
        self.page.fill("//input[@id='userEmail']",email)
        self.page.fill("//input[@id='userPassword']", password)
        self.page.click("//input[@id='login']")
        return Dashboard(self.page)

