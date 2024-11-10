import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SignupPage(BasePage):
    PAGE_URL = Links.SIGNUP_PAGE

    EMAIL_FIELD = ("xpath", "//input[@type='email']")
    PASSWORD_FIELD = ("xpath", "//input[@type='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    USERNAME_FIELD = ("xpath", "//input[@type='text']")
    CONTINUE_BUTTON = ("xpath", "//button[@type='submit']")
    PERSONAL_CHECKBOX = ("xpath", "//button[@data-gtm-id='personal']")
    WORK_CHECKBOX = ("xpath", "//button[@data-gtm-id='work']")
    EDUCATION_CHECKBOX = ("xpath", "//button[@data-gtm-id='education']")
    LAUNCH_TODOIST_BUTTON = ("xpath", "//button[@aria-label='Launch Todoist']")
    PAGE_HEAD = ("xpath", "//div[@class='fb8d74bb']//h1")

    @allure.step("Enter email")
    def enter_fake_email(self):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD))\
            .send_keys(self.fake_data_generator.fake_email)

    @allure.step("Enter password")
    def enter_fake_password(self):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))\
            .send_keys(self.fake_data_generator.fake_password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))\
            .click()

    @allure.step("Enter username")
    def enter_fake_username(self):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))\
            .send_keys(self.fake_data_generator.fake_username)

    @ allure.step("Click Continue button")
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))\
            .click()

    @ allure.step("Select Personal checkbox")
    def select_personal_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.PERSONAL_CHECKBOX))\
            .click()

    @ allure.step("Select Work checkbox")
    def select_work_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.WORK_CHECKBOX))\
            .click()

    @ allure.step("Select Education checkbox")
    def select_education_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.EDUCATION_CHECKBOX))\
            .click()

    @ allure.step("Click Launch Todoist button")
    def click_launch_todoist_button(self):
        self.wait.until(lambda driver: driver.find_element(
            *self.LAUNCH_TODOIST_BUTTON).get_attribute("aria-disabled") == "false")
        self.driver.find_element(*self.LAUNCH_TODOIST_BUTTON).click()

    @allure.step("Verify that the page heading is 'Sign up'")
    def is_page_heading_signup(self):
        heading_element = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_HEAD))
        assert heading_element.text == "Sign up", f"Expected 'Sign up' but got '{
            heading_element.text}'"
