import allure
import time
from base.base_page import BasePage
from pages.home_page import HomePage
from config.links import Links
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ProjectsPage(HomePage):

    PAGE_URL = Links.PROJECTS_PAGE

    MY_PROJECTS_MENU_BUTTON = (
        "xpath", "//div[@class='imKBXQv fb8d74bb _4e9ab24b']//button[@aria-label='My projects menu']")
    ADD_PROJECT_BUTTON = ("xpath", "//div[@role='menuitem']")
    PROJECT_NAME_FIELD = ("xpath", "//input[@name='name']")
    CHOOSE_LIST_BUTTON = ("xpath", "//label[@for='LIST']")
    ADD_BUTTON = ("xpath", "//button[@type='submit']")
    CHOOSE_BOARD_BUTTON = ("xpath", "//label[@for='BOARD']")
    NAME_THIS_SECTION_FIELD = ("xpath", "//input[@aria-label='Name this section']")
    ADD_SECTION_BUTTON = ("xpath", "//span[@class='board_add_section_button__label']")
    CONFIRM_ADD_SECTION_BUTTON = ("xpath", "//button[@type='submit']")
    MORE_ACTIONS_BUTTON = ("xpath", "//button[@aria-label='Project options menu']")
    EDIT_BUTTON = ("xpath", "(//div[@role='menuitem'])[1]")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    BOARD_SECTION = ("xpath", "//div[@class='board_view__sections']")
    DELETE_BUTTON = ("xpath", "(//div[@role='menuitem'])[11]")
    CONFIRM_DELETION_BUTTON = ("xpath", "//button[@data-autofocus='true']")
    DUPLICATE_BUTTON = ("xpath", "(//div[@role='menuitem'])[3]")

    @allure.step("Click on the \"+\" (My projects menu) button")
    def click_my_projects_menu_button(self):
        self.click_element(self.MY_PROJECTS_MENU_BUTTON)

    @allure.step("Click on the \"Add\" project button")
    def click_add_project_button(self):
        self.click_element(self.ADD_PROJECT_BUTTON)

    @allure.step("Enter Project name")
    def enter_project_name(self, project_name):
        self.enter_text(self.PROJECT_NAME_FIELD, project_name)

    @allure.step("Choose List as the project type")
    def choose_list(self):
        self.click_element(self.CHOOSE_LIST_BUTTON)

    @allure.step("Click on the \"Add\" button")
    def click_add_button(self):
        self.click_element(self.ADD_BUTTON)

    @allure.step("Verify that a project appears in the My Projects section")
    def is_my_projects_section_contains_project(self, project_name):
        project_locator = ("xpath", f"//div[@class='WwLx9J2']//span[text()='{project_name}']")
        elements = self.driver.find_elements(*project_locator)
        assert len(elements) > 0, f"Project \"{project_name}\" not found"

    @allure.step("Choose Board as the project type")
    def choose_board(self):
        self.click_element(self.CHOOSE_BOARD_BUTTON)

    @allure.step("Enter Board section name")
    def enter_section_name(self, section_name):
        self.enter_text(self.NAME_THIS_SECTION_FIELD, section_name)

    @allure.step("Click on the confirm \"Add section\" button")
    def click_confirm_add_section_button(self):
        self.click_element(self.CONFIRM_ADD_SECTION_BUTTON)
        time.sleep(1)

    @allure.step("Click on the \"Add section\" button")
    def click_add_section_button(self):
        self.click_element(self.ADD_SECTION_BUTTON)

    @allure.step("Verify that the section appear on the Board")
    def is_board_contains_section(self, section_name):
        section_locator = (
            "xpath", f"//div[@data-testid='project-board-view']//span[text()='{section_name}']")
        elements = self.driver.find_elements(*section_locator)
        assert len(elements) > 0, f"Section \"{section_name}\" not found"

    @allure.step("Open the project")
    def open_project(self, project_name):
        project_locator = ("xpath", f"//div[text()='{project_name}']")
        self.click_element(project_locator)

    @allure.step("Click on the \"More actions\" button")
    def click_more_action_button(self):
        time.sleep(1)
        self.click_element(self.MORE_ACTIONS_BUTTON)

    @allure.step("Click on the \"Edit\" button")
    def click_edit_button(self):
        self.click_element(self.EDIT_BUTTON)

    @allure.step("Click on the \"Save\" button")
    def click_save_button(self):
        self.click_element(self.SAVE_BUTTON)
        time.sleep(1)

    @allure.step("Verify that the board sections are visible")
    def is_board_sections_visible(self):
        self.wait_for_visibility(self.BOARD_SECTION)

    @allure.step("Click on the \"Delete\" button and confirm the deletion")
    def click_delete_button(self):
        self.click_element(self.DELETE_BUTTON)
        self.click_element(self.CONFIRM_DELETION_BUTTON)
        time.sleep(1)

    @allure.step("Verify that the Project is no longer visible in the My Projects section")
    def is_my_project_section_not_contains_project(self, project_name):
        project_locator = ("xpath", f"//div[@class='WwLx9J2']//span[text()='{project_name}']")
        project = self.driver.find_elements(*project_locator)
        assert len(project) == 0, \
            f"Project \"{project_name}\" is still visible in the My Projects section"

    @allure.step("Verify that the \"Add\" button is disabled")
    def is_add_button_disabled(self):
        button = self.driver.find_element(*self.ADD_BUTTON)
        aria_disabled = button.get_attribute("aria-disabled")
        assert aria_disabled == "true", f"The \"Add\" button is not disabled"

    @allure.step("Click on the \"Duplicate\" button")
    def click_duplicate_button(self):
        self.click_element(self.DUPLICATE_BUTTON)
