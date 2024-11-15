import allure
from base.base_test import BaseTest


@allure.suite("Authorization Functionality")
class TestAuthorization(BaseTest):

    @allure.title("TC02 Successful login to an existing account with valid information")
    def test_successful_authorization(self):
        # Steps:
        self.login_page.open()
        self.login_page.is_page_heading_login()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_username(self.data.USERNAME)

    @allure.title("TC03 Successful logout from an account")
    def test_successful_logout(self, login):
        # Steps:
        self.home_page.click_username_button()
        self.home_page.click_logout_button()
        self.login_page.is_opened()
        self.login_page.is_page_heading_login()

    @allure.title("TC04 Ability to login using a Google account")
    def test_successful_authorization_using_google(self):
        # Steps:
        self.login_page.open()
        self.login_page.click_continue_with_google_button()
        self.google_account_page.is_opened()
        self.google_account_page.enter_gmail(self.data.GMAIL)
        self.google_account_page.click_confirm_gmail_button()
        self.google_account_page.enter_gmail_password(self.data.GMAIL_PASSWORD)
        self.google_account_page.click_confirm_password_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_username(self.data.GMAIL_USERNAME)
        