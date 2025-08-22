import pytest
from pytest_bdd import given, scenarios, then, when, parsers

from PageObjects.LoginPage import LoginPage
from utils.ApiBase import API_Utils


scenarios("features/orders.feature")

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('I place the item order with {username} and {password}'))
def place_order(playwright, username, password, shared_data):
    api_utils = API_Utils()
    user_credentials = {"userEmail": username, "password": password}
    order_id = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = order_id

@given('the user is on the landing page')
def user_on_landing_page(BrowserInstance, shared_data):
    page = BrowserInstance
    loginpage = LoginPage(page, "https://rahulshettyacademy.com/client")
    loginpage.goto()
    shared_data['loginpage'] = loginpage

@when(parsers.parse('I login to the Portal with {username} and {password}'))
def login_flow(BrowserInstance, username, password, shared_data):
    loginpage = shared_data['loginpage']
    page = BrowserInstance
    dashboard = loginpage.login(username, password)
    page.wait_for_timeout(2000)
    shared_data['dashboard'] = dashboard
    print(f"Shared data: {shared_data}")


@when("navigate to the order page")
def navigateOrderpage(shared_data):
    dashboard = shared_data['dashboard']
    orderpage = dashboard.selectOrdersNavLink()
    shared_data['orderpage'] = orderpage

@then("the order id is successfully displayed")
def orderfind(shared_data):
    orderpage = shared_data['orderpage']
    order_id = shared_data['order_id']
    assert order_id in orderpage.get_orders(), f"Order ID {order_id} not found in the table"

