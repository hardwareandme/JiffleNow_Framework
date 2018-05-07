import pytest,os
from selenium import webdriver
from pages.login.login_page import loginPage


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        baseURL = "https://calendar.google.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on FF")
        # lp = loginPage(driver)
        # lp.login("testsel35","testme123")
    else:
        baseURL = "https://calendar.google.com"
        driverLocation = "/home/ravi/Downloads/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        lp = loginPage(driver)
        lp.login("testsel35","testme123")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")