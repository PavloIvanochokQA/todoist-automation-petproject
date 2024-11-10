import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.data import Data


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open()
    login_page.enter_email(Data.EMAIL)
    login_page.enter_password(Data.PASSWORD)
    login_page.click_submit_button()

    return home_page
