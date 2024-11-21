import allure
import random
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


class TestTaskManagement(BaseTest):

    @allure.feature("Task Management")
    @allure.story("Task Creation")
    @allure.description("""
    This test verifies that a task can be successfully created with all required fields filled
    """)
    @allure.title("TC12 Successful task creation")
    def test_task_creation(self, login):
        fake = FakeDataGenerator()
        name = fake.task_name
        description = fake.task_description
        priority = random.randint(1, 4)
        # Steps:
        self.home_page.click_add_task_button()
        self.home_page.enter_task_name(name)
        self.home_page.enter_task_description(description)
        self.home_page.set_priority(priority)
        self.home_page.click_submit_add_task_button()
        self.home_page.is_task_list_contains_task(name)
        self.home_page.open_task(name)
        self.task_page.is_opened()
        self.task_page.is_task_contains_description(description)
        self.task_page.is_task_has_priority(priority)

    @allure.feature("Task Management")
    @allure.story("Task Editing")
    @allure.description("""
    This test verifies that the name, description, and priority of a task can be successfully updated
    """)
    @allure.title("TC13 Successful change of name, description, and priority for a task")
    def test_task_editing(self, login, create_task):
        name, description, priority = create_task
        fake = FakeDataGenerator()
        new_name = fake.task_name
        new_description = fake.task_description
        new_priority = random.randint(1, 4)
        # Steps:
        self.home_page.click_edit_button(name)
        self.home_page.enter_task_name(new_name)
        self.home_page.enter_task_description(new_description)
        self.home_page.set_priority(new_priority)
        self.home_page.click_save_button()
        self.home_page.open_task(new_name)
        self.task_page.is_opened()
        self.task_page.is_task_contains_description(new_description)
        self.task_page.is_task_has_priority(new_priority)
