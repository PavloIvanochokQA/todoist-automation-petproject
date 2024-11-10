import allure
from base.base_test import BaseTest


@allure.feature("Registration Functionality")
class TestRegistration(BaseTest):

    @allure.title("Successful registration of a new account with valid information")
    def test_registration_account(self):
        self.signup_page.open()
        self.signup_page.is_page_heading_signup()
        self.signup_page.enter_fake_email()
        self.signup_page.enter_fake_password()
        self.signup_page.click_submit_button()
        self.signup_page.enter_fake_username()
        self.signup_page.click_continue_button()
        self.signup_page.select_personal_checkbox()
        self.signup_page.click_launch_todoist_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_fake_username()
