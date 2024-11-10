import allure
from base.base_test import BaseTest


@allure.feature("Authorization Functionality")
class TestAuthorization(BaseTest):

    @allure.title("Successful login to an existing account with valid information")
    def test_successful_authorization(self):
        self.login_page.open()
        self.login_page.is_page_heading_login()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_username(self.data.USERNAME)

    @allure.title("Successful logout from an account")
    def test_successful_logout(self, login):
        self.home_page.click_username_button()
        self.home_page.click_logout_button()
        self.login_page.is_opened()
        self.login_page.is_page_heading_login()
