import allure
from base.base_test import BaseTest


@allure.suite("Registration Functionality")
class TestRegistration(BaseTest):

    @allure.title("TC01 Successful registration of a new account with valid information")
    def test_registration_account(self, delete_account):
        email = self.fake.email
        password = self.fake.password
        username = self.fake.username
        # Steps:
        self.signup_page.open()
        self.signup_page.is_page_heading_signup()
        self.signup_page.enter_email(email)
        self.signup_page.enter_password(password)
        self.signup_page.click_signup_button()
        self.signup_page.enter_username(username)
        self.signup_page.click_continue_button()
        self.signup_page.select_personal_checkbox()
        self.signup_page.select_education_checkbox()
        self.signup_page.click_launch_todoist_button()
        self.home_page.is_opened()
        self.home_page.is_sidebar_contains_username(username)
        # Postconditions:
        with allure.step("Postconditions: Delete the created account"):
            delete_account(email, password)
