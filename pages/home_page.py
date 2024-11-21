import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    TASK_NAME_FIELD = ("xpath", "//div[@aria-label='Task name']")
    TASK_DESCRIPTION_FIELD = ("xpath", "//div[@aria-label='Description']")
    USERNAME_BUTTON = ("xpath", "//button[@aria-haspopup='menu']")
    LOGOUT_BUTTON = ("xpath", "(//span[@class='user_menu_label'])[9]")
    SETTINGS_BUTTON = ("xpath", "(//span[@class='user_menu_label'])[1]")
    ADD_TASK_BUTTON = ("xpath", "(//div/button[@type='button'])[3]")
    CANCEL_BUTTON = ("xpath", "//button[@aria-label='Cancel']")
    SUBMIT_ADD_TASK_BUTTON = ("xpath", "(//div/button[@type='submit'])")
    PRIORITY_DROPDOWN = ("xpath", "//div[@aria-label='Set priority']")
    SAVE_BUTTON = ("xpath", "//button[@data-testid='task-editor-submit-button']")

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

    @allure.step("Click on the \"Add task\" button")
    def click_add_task_button(self):
        self.click_element(self.ADD_TASK_BUTTON)

    @allure.step("Enter Task name")
    def enter_task_name(self, task_name):
        self.enter_text(self.TASK_NAME_FIELD, task_name)

    @allure.step("Enter Task description")
    def enter_task_description(self, description):
        self.enter_text(self.TASK_DESCRIPTION_FIELD, description)

    @allure.step("Set Priority")
    def set_priority(self, priority):
        item_locator = ("xpath", f"//ul[@aria-label='Select a priority']/li[{priority}]")
        self.click_element(self.PRIORITY_DROPDOWN)
        self.click_element(item_locator)

    @allure.step("Click on the submit \"Add task\" button")
    def click_submit_add_task_button(self):
        self.click_element(self.SUBMIT_ADD_TASK_BUTTON)
        self.click_element(self.CANCEL_BUTTON)

    @allure.step("Verify that the task list contains task")
    def is_task_list_contains_task(self, task_name):
        task_locator = ("xpath", f"//div[@class='list_holder']//div[text()='{task_name}']")
        element = self.wait.until(EC.presence_of_element_located(task_locator))
        assert element is not None, f"Task \"{task_name}\" not found"

    @allure.step("Open the task")
    def open_task(self, task_name):
        task_locator = ("xpath", f"//div[text()='{task_name}']")
        self.wait.until(EC.presence_of_element_located(task_locator))
        self.click_element(task_locator)

    @allure.step("Click on the \"Edit\" button on the task")
    def click_edit_button(self, task_name):
        task_element = self.driver.find_element("xpath", f"//div[text()='{task_name}']")
        edit_button = (
            "xpath", f"//div[text()='{task_name}']/ancestor::div[@role='button']//button[@aria-label='Edit']")
        ActionChains(self.driver).move_to_element(task_element).perform()
        self.click_element(edit_button)

    @allure.step("Click on the \"Save\" button")
    def click_save_button(self):
        self.click_element(self.SAVE_BUTTON)
