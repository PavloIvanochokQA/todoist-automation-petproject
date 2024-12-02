import allure
import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    TASK_NAME_FIELD = ("xpath", "//div[@aria-label='Task name']")
    TASK_DESCRIPTION_FIELD = ("xpath", "//div[@aria-label='Description']")
    USERNAME_BUTTON = ("xpath", "//button[@aria-haspopup='menu']")
    LOGOUT_BUTTON = ("xpath", "(//span[@class='user_menu_label'])[9]")
    SETTINGS_BUTTON = ("xpath", "(//span[@class='user_menu_label'])[1]")
    ADD_TASK_BUTTON = ("xpath", "(//div/button[@type='button'])[3]")
    CANCEL_BUTTON = ("xpath", "//button[@aria-label='Cancel']")
    SUBMIT_ADD_TASK_BUTTON = ("xpath", "//button[@data-testid='task-editor-submit-button']")
    PRIORITY_DROPDOWN = ("xpath", "//div[@aria-label='Set priority']")
    SAVE_BUTTON = ("xpath", "//button[@data-testid='task-editor-submit-button']")
    DELETE_BUTTON = ("xpath", "//div[@data-action-hint='task-overflow-menu-delete']")
    CONFIRM_DELETION_BUTTON = ("xpath", "//div[@role='dialog']//button[@data-autofocus='true']")
    LABEL_HEADER = ("xpath", "//div[@data-testid='large-header']//h1")
    DUPLICATE_BUTTON = ("xpath", "//div[@data-action-hint='task-overflow-menu-duplicate']")
    MY_PROJECTS_BUTTON = ("xpath", "//div[@class='WwLx9J2']//a[@href='/app/projects']")

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
    def enter_task_description(self, task_description):
        self.enter_text(self.TASK_DESCRIPTION_FIELD, task_description)

    @allure.step("Set Task priority")
    def set_task_priority(self, task_priority):
        item_locator = ("xpath", f"//ul[@aria-label='Select a priority']/li[{task_priority}]")
        self.click_element(self.PRIORITY_DROPDOWN)
        self.click_element(item_locator)

    @allure.step("Click on the submit \"Add task\" button")
    def click_submit_add_task_button(self):
        self.click_element(self.SUBMIT_ADD_TASK_BUTTON)
        self.click_element(self.CANCEL_BUTTON)

    @allure.step("Verify that the task list contains task")
    def is_task_list_contains_task(self, task_name):
        task_locator = ("xpath", f"//div[@class='list_holder']//div[text()='{task_name}']")
        elements = self.driver.find_elements(*task_locator)
        assert len(elements) > 0, f"Task \"{task_name}\" not found"

    @allure.step("Open the task")
    def open_task(self, task_name):
        task_locator = ("xpath", f"//div[text()='{task_name}']")
        self.wait.until(EC.presence_of_element_located(task_locator))
        self.click_element(task_locator)
        time.sleep(1)

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

    @allure.step("Go to the \"Completed\" section")
    def open_completed_section(self):
        ActionChains(self.driver).key_down("c").key_down("g").key_up("g").key_up("c").perform()

    @allure.step("Verify that the task appears in the \"Completed\" section")
    def is_completed_section_contains_task(self, task_name):
        task_locator = ("xpath", f"//div[@id='activity_app']//div[text()='{task_name}']")
        elements = self.driver.find_elements(*task_locator)
        assert len(elements) > 0, f"Task '{task_name}' not found in the \"Completed\" section"

    @allure.step("Verify that the task is no longer visible in the task list")
    def is_task_list_not_contains_task(self, task_name):
        task_locator = ("xpath", f"//div[@class='list_holder']//div[text()='{task_name}']")
        task = self.driver.find_elements(*task_locator)
        assert len(task) == 0, f"Task \"{task_name}\" is still visible in the task list"

    @allure.step("Click on the more actions button on the task")
    def click_more_actions_button(self, task_name):
        task_element = self.driver.find_element("xpath", f"//div[contains(text(), '{task_name}')]")
        more_actions_button = (
            "xpath", f"//div[contains(text(),'{task_name}')]/ancestor::div[@role='button']//button[@aria-label='More actions']")
        ActionChains(self.driver).move_to_element(task_element).perform()
        self.click_element(more_actions_button)

    @allure.step("Click on the \"Delete\" button")
    def click_delete_button(self):
        self.click_element(self.DELETE_BUTTON)

    @allure.step("Confirm the deletion")
    def confirm_deletion(self):
        self.click_element(self.CONFIRM_DELETION_BUTTON)
        time.sleep(1)

    @allure.step("Click on the checkbox on the task")
    def click_checkbox_on_task(self, task_name):
        completed_checkbox = (
            "xpath", f"//div[text()='{task_name}']/ancestor::div[@role='button']//button[@aria-label='Mark task as complete']")
        self.click_element(completed_checkbox)
        time.sleep(1)

    @allure.step("Click on the link in task")
    def click_link_in_task(self, task_name):
        link_locator = ("xpath", f"//div[contains(text(), '{task_name}')]//a")
        self.click_element(link_locator)

    @allure.step("Verify that a new browser tab opens with the URL specified in the link")
    def is_link_opened(self, link):
        tabs = self.driver.window_handles
        assert len(tabs) > 1, "No new tab was opened"
        self.driver.switch_to.window(tabs[1])
        assert self.driver.current_url == link, \
            f"Expected URL: {link}, but got: {self.driver.current_url}"
        self.driver.switch_to.window(tabs[0])

    @allure.step("Verify that the page heading contains label")
    def is_page_heading_contains_label(self, label):
        label_text = self.driver.find_element(*self.LABEL_HEADER).text
        assert label == label_text, f"Expected label: {label}, but got: {label_text}"

    @allure.step("Click on the \"Duplicate\" button")
    def click_duplicate_button(self):
        self.click_element(self.DUPLICATE_BUTTON)

    @allure.step("Verify that a duplicate of the task appears in the task list")
    def is_task_list_contains_duplicate(self, task_name):
        task_locator = ("xpath", f"//div[@class='list_holder']//div[text()='{task_name}']")
        elements = self.driver.find_elements(*task_locator)
        assert len(elements) > 1, f"Duplicate \"{task_name}\" not found"

    @allure.step("Verify that the \"Add task\" button is disabled")
    def is_add_task_button_disabled(self):
        button = self.driver.find_element(*self.SUBMIT_ADD_TASK_BUTTON)
        aria_disabled = button.get_attribute("aria-disabled")
        assert aria_disabled == "true", f"The \"Add task\" button is not disabled"

    @allure.step("Click on the \"My Projects\" button")
    def click_my_projects_button(self):
        self.click_element(self.MY_PROJECTS_BUTTON)
