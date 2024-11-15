import allure
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator
fake = FakeDataGenerator()


@allure.suite("Settings Functionality")
class TestSettings(BaseTest):

    @allure.title("TC07 Successful account deletion")
    def test_successful_accound_deletion(self, create_account):
        email, password, username = create_account
        # Steps:
        self.home_page.click_username_button()
        self.home_page.click_settings_button()
        self.account_settings_page.click_delete_account_button()
        self.delete_settings_page.enter_todoist_email(email)
        self.delete_settings_page.enter_todoist_password(password)
        self.delete_settings_page.click_delete_account_button()
        self.account_deleted_page.is_opened()
        self.account_deleted_page.is_page_heading_account_deleted()

    @allure.title("TC05 Successful password change")
    def test_successful_password_change(self, create_account, delete_account):
        email, password, username = create_account
        new_password = "new" + password
        is_password_changed = False
        # Steps:
        try:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_settings_page.click_change_password_button()
            self.password_settings_page.enter_current_password(password)
            self.password_settings_page.enter_new_password(new_password)
            self.password_settings_page.click_change_password_button()
            self.password_settings_page.is_error_message_is_not_visible()
            self.account_settings_page.is_opened()
            is_password_changed = True
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created account"):
                password_to_use = new_password if is_password_changed else password
                delete_account(email, password_to_use)

    @allure.title("TC06 Successful email and username change")
    def test_successful_email_and_username_change(self, create_account, delete_account):
        email, password, username = create_account
        new_email = "new" + email
        new_username = "new_test_user"
        is_email_changed = False
        # Steps:
        try:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_settings_page.click_change_email_button()
            self.email_settings_page.enter_new_email(new_email)
            self.email_settings_page.enter_todoist_password(password)
            self.email_settings_page.click_change_email_button()
            self.email_settings_page.is_error_message_is_not_visible()
            self.account_settings_page.is_opened()
            is_email_changed = True
            self.account_settings_page.enter_new_username(new_username)
            self.account_settings_page.click_update_button()
            self.account_settings_page.click_close_settings_button()
            self.home_page.is_sidebar_contains_username(new_username)
        # Postconditions:
        finally:
            email_to_use = new_email if is_email_changed else email
            with allure.step("Postconditions: Delete the created account"):
                delete_account(email_to_use, password)
