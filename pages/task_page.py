import allure
from pages.home_page import HomePage
from config.links import Links
from selenium.webdriver.support.ui import WebDriverWait


class TaskPage(HomePage):

    PAGE_URL = Links.TASK_PAGE

    PRIORITY_DROPDOWN = ("xpath", "(//div[@class='DHmDvjK']//button[@aria-haspopup='listbox'])[2]")
    TASK_NAME_CONTAINER = ("xpath", "//div[@class='task-overview-content']")
    TASK_DESCRIPTION_CONTAINER = ("xpath", "//div[@class='task_content']/p")
    TASK_NAME_FIELD = ("xpath", "//div[@aria-label='Task name']")
    TASK_DESCRIPTION_FIELD = ("xpath", "//div[@aria-label='Description']")

    def is_opened(self):
        with allure.step(f"Verify that a page with a URL starting with {self.PAGE_URL} is opened"):
            WebDriverWait(self.driver, 3).until(
                lambda driver: driver.current_url.startswith(self.PAGE_URL))

    @allure.step("Verify that the task contains the appropriate description")
    def is_task_contains_description(self, description):
        description_content = self.driver.find_element(*self.TASK_DESCRIPTION_CONTAINER).text
        assert description_content == description, \
            f"Expected: \"{description}\", but got \"{description_content}\""

    @allure.step("Verify that the task has the appropriate priority")
    def is_task_has_priority(self, priority):
        self.click_element(self.PRIORITY_DROPDOWN)
        item_locator = ("xpath", f"//li[@aria-label='Priority {priority}']")
        priority = self.driver.find_element(*item_locator)
        assert priority.get_attribute('aria-selected') == 'true', \
            f"The task does not have the appropriate Priority set"
