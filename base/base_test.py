import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.home_page import HomePage
from pages.google_account_page import GoogleAccountPage
from pages.settings_pages import AccountSettingsPage
from pages.settings_pages import PasswordSettingsPage
from pages.settings_pages import EmailSettingsPage
from pages.settings_pages import DeleteSettingsPage
from pages.settings_pages import AccountDeletedPage
from utils.fake_data_generator import FakeDataGenerator


class BaseTest:

    data: Data
    login_page: LoginPage
    signup_page: SignupPage
    home_page: HomePage
    google_account_page: GoogleAccountPage
    account_settings_page: AccountSettingsPage
    password_settings_page: PasswordSettingsPage
    email_settings_page: EmailSettingsPage
    delete_settings_page: DeleteSettingsPage
    account_deleted_page: AccountDeletedPage

    fake = FakeDataGenerator()

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data
        request.cls.login_page = LoginPage(driver)
        request.cls.signup_page = SignupPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.google_account_page = GoogleAccountPage(driver)
        request.cls.account_settings_page = AccountSettingsPage(driver)
        request.cls.password_settings_page = PasswordSettingsPage(driver)
        request.cls.email_settings_page = EmailSettingsPage(driver)
        request.cls.delete_settings_page = DeleteSettingsPage(driver)
        request.cls.account_deleted_page = AccountDeletedPage(driver)
        
