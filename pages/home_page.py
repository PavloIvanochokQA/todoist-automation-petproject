import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    USERNAME_BUTTON = ("xpath", "//button[@aria-haspopup='menu']")
    LOGOUT_BUTTON = ("xpath", "(//span[@class='user_menu_label'])[9]")
    SETTINGS_BUTTON = ("xpath", "(//span[@class='user_menu_label'])[1]")

    @allure.step("Click on the \"Username\" button")
    def click_username_button(self):
        self.click_element(self.USERNAME_BUTTON)

    @allure.step("Click on the \"Log out\" button")
    def click_logout_button(self):
        self.click_element(self.LOGOUT_BUTTON)

    @allure.step("Click on the \"Settings\" button")
    def click_settings_button(self):
        self.click_element(self.SETTINGS_BUTTON)

    @allure.step("Verify that the sidebar contains username")
    def is_sidebar_contains_username(self, username):
        sidebar_username = self.wait_for_visibility(self.USERNAME_BUTTON).text
        assert username in sidebar_username, \
            f"Username '{username}' not found in the sidebar"
