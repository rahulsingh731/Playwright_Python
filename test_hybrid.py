import json
import time
from playwright.sync_api import Playwright
from PageObjects.LoginPage import LoginPage
from conftest import user_credentials
from utils.ApiBase import API_Utils  # Adjusted import based on your folder structure
import pytest


with open("data/credentials.json") as file:
        testdata = json.load(file)
        userData = testdata['user-credentials']

@pytest.mark.parametrize('user_credentials',userData)
def test_e2e_test_create_order(BrowserInstance, user_credentials,playwright):

    email = user_credentials['userEmail']
    password = user_credentials['password']
    page = BrowserInstance


    api_utils = API_Utils()
    order_id = api_utils.createOrder(playwright,user_credentials)
    

    
    loginpage = LoginPage(page,"https://rahulshettyacademy.com/client")

    loginpage.goto()
    dashboard = loginpage.login(email, password)
    page.wait_for_timeout(2000)
    orderpage = dashboard.selectOrdersNavLink()
    page.wait_for_timeout(2000)
    
    assert order_id in orderpage.get_orders(), f"Order ID {order_id} not found in the table"
    page.wait_for_timeout(2000)

    
