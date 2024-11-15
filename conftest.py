import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.settings_pages import AccountSettingsPage, DeleteSettingsPage
from utils.fake_data_generator import FakeDataGenerator
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
    login_page.click_login_button()
    return home_page


@pytest.fixture(scope="function")
def create_account(driver, request):
    signup_page = SignupPage(driver)

    fake = FakeDataGenerator()
    email = fake.email
    password = fake.password
    username = fake.username

    signup_page.open()
    signup_page.enter_email(email)
    signup_page.enter_password(password)
    signup_page.click_signup_button()
    signup_page.enter_username(username)
    signup_page.click_continue_button()
    signup_page.select_personal_checkbox()
    signup_page.click_launch_todoist_button()
    return email, password, username


@pytest.fixture(scope="function")
def delete_account(driver):
    home_page = HomePage(driver)
    delete_settings_page = DeleteSettingsPage(driver)
    account_settings_page = AccountSettingsPage(driver)

    def _delete_account(email, password):
        try:
            home_page.open()
            home_page.click_username_button()
            home_page.click_settings_button()
            account_settings_page.click_delete_account_button()
            delete_settings_page.enter_todoist_email(email)
            delete_settings_page.enter_todoist_password(password)
            delete_settings_page.click_delete_account_button()
        except Exception as e:
            print(f"Error during account deletion: {e}")

    return _delete_account
