import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    USERNAME_BUTTON = ("xpath", "//button[@aria-label='Settings']")
    LOGOUT_BUTTON = ("xpath", "(//span[@class='user_menu_label'])[9]")

    @allure.step("Verify that the username from registration is displayed in the sidebar")
    def is_sidebar_contains_fake_username(self):
        sidebar_username = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_BUTTON)).text
        assert self.fake_data_generator.fake_username in sidebar_username, f"Username '{
            self.fake_data_generator.fake_username}' not found in the sidebar"

    @allure.step("Verify that the sidebar contains the username")
    def is_sidebar_contains_username(self, username):
        sidebar_username = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_BUTTON)).text
        assert username in sidebar_username, f"Username '{
            username}' not found in the sidebar"

    @allure.step("Click on the username button")
    def click_username_button(self):
        self.wait.until(EC.element_to_be_clickable(
            self.USERNAME_BUTTON)).click()

    @allure.step("Click on the Log out button")
    def click_logout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
