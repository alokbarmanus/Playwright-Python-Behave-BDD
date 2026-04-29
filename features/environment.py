from features.utilities.memory_manager import MemoryManager
import os
from behave import fixture, use_fixture
from tests.base_test import BaseTest
from features.pages.login_page_objects import LoginPageObjects
from features.pages.dashboard_page_objects import DashboardPageObjects

# def after_all(context):
#     os.system('allure generate allure-results -o allure-report --clean')

@fixture
def browser_context(context):
    context.test = BaseTest()
    context.test.setup()
    context.page = context.test.page
    yield context.page
    context.test.teardown()

def before_scenario(context, scenario):
    use_fixture(browser_context, context)
    context.login_page = LoginPageObjects(context.page)
    context.dashboard_page = DashboardPageObjects(context.page)
    context.memory = MemoryManager()

import allure
from allure_commons.types import AttachmentType

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        # Take screenshot using Playwright
        screenshot_path = 'failed_screenshot.png'
        try:
            context.page.screenshot(path=screenshot_path, full_page=True)
            with open(screenshot_path, 'rb') as image_file:
                allure.attach(image_file.read(), name="Failure Screenshot", attachment_type=AttachmentType.PNG)
            os.remove(screenshot_path)
        except Exception as e:
            print(f"Could not capture screenshot: {e}")
    # Clear memory after each scenario
    if hasattr(context, 'memory'):
        context.memory.clear()
