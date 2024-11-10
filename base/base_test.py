import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.home_page import HomePage


class BaseTest:

    data: Data
    login_page: LoginPage
    signup_page: SignupPage
    home_page: HomePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data
        request.cls.login_page = LoginPage(driver)
        request.cls.signup_page = SignupPage(driver)
        request.cls.home_page = HomePage(driver)
