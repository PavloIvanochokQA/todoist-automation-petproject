import allure
import random
from base.base_test import BaseTest


class TestProfileManagement(BaseTest):

    @allure.feature("Profile Management")
    @allure.story("Account Deletion")
    @allure.description("""
    This test verifies that a user can successfully delete their account by accessing the account settings and following the deletion process
    """)
    @allure.title("TC07 Successful account deletion")
    def test_successful_accound_deletion(self, create_account):
        email, password, username = create_account
        # Steps:
        self.home_page.click_username_button()
        self.home_page.click_settings_button()
        self.account_management_page.click_delete_account_button()
        self.delete_management_page.is_opened()
        self.delete_management_page.enter_todoist_email(email)
        self.delete_management_page.enter_todoist_password(password)
        self.delete_management_page.click_delete_account_button()
        self.account_deleted_page.is_opened()
        self.account_deleted_page.is_page_heading_account_deleted()

    @allure.feature("Profile Management")
    @allure.story("Password Management")
    @allure.description("""
    This test verifies that a user can successfully change their password through the account settings by entering the current password and a new one
    """)
    @allure.title("TC05 Successful password change")
    def test_successful_password_change(self, create_account, delete_account):
        email, password, username = create_account
        new_password = str(random.randint(1000, 9999)) + password
        is_password_changed = False
        # Steps:
        try:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_change_password_button()
            self.password_management_page.is_opened()
            self.password_management_page.enter_current_password(password)
            self.password_management_page.enter_new_password(new_password)
            self.password_management_page.click_change_password_button()
            self.password_management_page.is_error_message_not_visible()
            self.account_management_page.is_opened()
            is_password_changed = True
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created account"):
                password_to_use = new_password if is_password_changed else password
                delete_account(email, password_to_use)

    @allure.feature("Profile Management")
    @allure.story("Account Information Management")
    @allure.description("""
    This test verifies that a user can successfully change their email address and username through the account settings
    """)
    @allure.title("TC06 Successful email and username change")
    def test_successful_email_and_username_change(self, create_account, delete_account):
        email, password, username = create_account
        new_email = str(random.randint(1000, 9999)) + email
        new_username = username + str(random.randint(10, 99))
        is_email_changed = False
        # Steps:
        try:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_change_email_button()
            self.email_management_page.is_opened()
            self.email_management_page.enter_new_email(new_email)
            self.email_management_page.enter_todoist_password(password)
            self.email_management_page.click_change_email_button()
            self.email_management_page.is_error_message_not_visible()
            self.account_management_page.is_opened()
            is_email_changed = True
            self.account_management_page.enter_new_username(new_username)
            self.account_management_page.click_update_button()
            self.account_management_page.click_close_settings_button()
            self.home_page.is_sidebar_contains_username(new_username)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created account"):
                email_to_use = new_email if is_email_changed else email
                delete_account(email_to_use, password)

    @allure.feature("Profile Management")
    @allure.story("Password Change Failure with Incorrect Current Password")
    @allure.description("""
    This test verifies that a user cannot change the current password when providing an incorrect current password
    """)
    @allure.title("TC10 Inability to change the current password with an incorrect password")
    def test_unsuccessful_password_change(self, create_account, delete_account):
        email, password, username = create_account
        new_password = password + str(random.randint(1000, 9999))
        invalid_password = "password" + str(random.randint(1000, 9999))
        invalid_new_password = str(random.randint(10000, 99999))
        # Steps:
        try:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_change_password_button()
            self.password_management_page.enter_current_password(invalid_password)
            self.password_management_page.enter_new_password(new_password)
            self.password_management_page.click_change_password_button()
            self.password_management_page.is_error_message_visible()
            self.password_management_page.is_opened()
            self.password_management_page.enter_current_password(password)
            self.password_management_page.enter_new_password(invalid_new_password)
            self.password_management_page.click_change_password_button()
            self.password_management_page.is_error_message_visible()
            self.password_management_page.is_opened()
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created account"):
                delete_account(email, password)

    @allure.feature("Profile Management")
    @allure.story("Account Deletion Failure with Incorrect Credentials")
    @allure.description("""
    This test verifies that a user cannot delete their account when providing an incorrect email or password
    """)
    @allure.title("TC11 Inability to delete the account with an incorrect email or password")
    def test_unsuccessful_account_deletion(self, create_account, delete_account):
        email, password, username = create_account
        invalid_email = str(random.randint(1000, 9999)) + email
        invalid_password = "password" + str(random.randint(1000, 9999))
        # Steps:
        try:
            self.home_page.click_username_button()
            self.home_page.click_settings_button()
            self.account_management_page.click_delete_account_button()
            self.delete_management_page.enter_todoist_email(email)
            self.delete_management_page.enter_todoist_password(invalid_password)
            self.delete_management_page.click_delete_account_button()
            self.delete_management_page.is_error_message_visible()
            self.delete_management_page.is_opened()
            self.delete_management_page.enter_todoist_email(invalid_email)
            self.delete_management_page.enter_todoist_password(password)
            self.delete_management_page.click_delete_account_button()
            self.delete_management_page.is_error_message_visible()
            self.delete_management_page.is_opened()
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created account"):
                delete_account(email, password)
