import pytest

def pytest_addoption(parser):
    # parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")
    # parser.addoption("--feature-flag", action="store_true", help="Enable feature flag")
    parser.addoption("--mybrowser", action="store", help="Select Browser by name")
    parser.addoption("--headless", action="store_true", help="Enable headless mode")


@pytest.fixture(scope="module")
def prework():
    print("Prework function executed.")

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture(scope="session")
def BrowserInstance(playwright,request):

    bname = request.config.getoption("--mybrowser") #from CLI
    mode = request.config.getoption("--headless")

    if bname == 'firefox':
        browser = playwright.firefox.launch(headless=mode)
    elif bname == 'webkit':
        browser = playwright.webkit.launch(headless=mode)
    else:
        browser = playwright.chromium.launch(headless=mode)
        
    context = browser.new_context()
    page = context.new_page()
    
    yield page

    page.close()
    context.close()
    browser.close()
