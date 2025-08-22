from playwright.sync_api import Playwright

order_payLoad = {"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}


class API_Utils:

    base_url = "https://rahulshettyacademy.com/"

    def get_token(self, playwright: Playwright,user_credentials):

        api_req_context = playwright.request.new_context(base_url=self.base_url)
        response = api_req_context.post("api/ecom/auth/login", data={"userEmail": user_credentials['userEmail'], "userPassword": user_credentials['password']})
        assert response.ok, f"Failed to get token: {response.status} {response.text}"
        return response.json()["token"]

    def createOrder(self, playwright:Playwright,user_credentials):
        api_req_context = playwright.request.new_context(base_url=self.base_url)
        response = api_req_context.post("api/ecom/order/create-order", data=order_payLoad,headers ={"Authorization":self.get_token(playwright,user_credentials),"Content-Type":"application/json"})
        return response.json()["orders"][0]


