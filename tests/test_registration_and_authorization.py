import allure
import time
from base.base_test import BaseTest


@allure.feature("Reg and Auth Functionality")
class TestRegAuth(BaseTest):

    @allure.title("Successful login to an existing account")
    def test_login_to_account(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.make_screenshot("Success")
