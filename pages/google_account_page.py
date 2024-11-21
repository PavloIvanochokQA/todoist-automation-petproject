import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support.ui import WebDriverWait


class GoogleAccountPage(BasePage):

    PAGE_URL = Links.GOOGLE_ACCOUNT_PAGE

    GMAIL_FIELD = ("xpath", "//input[@type='email']")
    PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    CONFIRM_GMAIL_BUTTON = ("xpath", "//div[@id='identifierNext']")
    CONFIRM_PASSWORD_BUTTON = ("xpath", "//div[@id='passwordNext']")

    @allure.step("Enter gmail")
    def enter_gmail(self, gmail):
        self.enter_text(self.GMAIL_FIELD, gmail)

    @allure.step("Click on the \"Confirm gmail\" button")
    def click_confirm_gmail_button(self):
        self.click_element(self.CONFIRM_GMAIL_BUTTON)

    @allure.step("Enter gmail password")
    def enter_gmail_password(self, gmail_password):
        self.enter_text(self.PASSWORD_FIELD, gmail_password)

    @allure.step("Click on the \"Confirm password\" button")
    def click_confirm_password_button(self):
        self.click_element(self.CONFIRM_PASSWORD_BUTTON)

    def is_opened(self):
        with allure.step(f"Verify that a page with a URL starting with {self.PAGE_URL} is opened"):
            WebDriverWait(self.driver, 3).until(
                lambda driver: driver.current_url.startswith(self.PAGE_URL))
