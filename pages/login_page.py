import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    EMAIL_FIELD = ("xpath", "//input[@type='email']")
    PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    USERNAME_BUTTON = ("xpath", "//button[@aria-label='Settings']")
    PAGE_HEAD = ("xpath", "//div[@class='fb8d74bb']//h1")

    @allure.step("Enter login")
    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)) \
            .send_keys(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)) \
            .send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)) \
            .click()

    @allure.step("Verify that the page heading is 'Log in'")
    def is_page_heading_login(self):
        heading_element = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_HEAD))
        assert heading_element.text == "Log in", f"Expected 'Log in' but got '{
            heading_element.text}'"
