import allure
from behave import given, when, then
from playwright.sync_api import expect
from features.pages.dashboard_page_objects import DashboardPageObjects
from features.pages.login_page_objects import LoginPageObjects
from features.utilities.data_util import DataUtil


@then('I should see the dashboard')
def step_impl(context):
    allure.attach("Checking if dashboard is displayed", name="INFO", attachment_type=allure.attachment_type.TEXT)
    try:
        assert context.dashboard_page.is_dashboard_displayed(), "Dashboard is not displayed."
        allure.attach("Dashboard is displayed", name="PASS", attachment_type=allure.attachment_type.TEXT)
    except AssertionError as e:
        allure.attach(str(e), name="FAIL", attachment_type=allure.attachment_type.TEXT)
        raise

@then('I should see the welcome message on dashboard')
def step_impl(context):
    allure.attach("Checking if welcome message is visible on dashboard", name="INFO", attachment_type=allure.attachment_type.TEXT)
    try:
        assert context.dashboard_page.is_welcome_message_visible(), "Welcome message is not visible on dashboard."
        allure.attach("Welcome message is visible on dashboard", name="PASS", attachment_type=allure.attachment_type.TEXT)
    except AssertionError as e:
        allure.attach(str(e), name="FAIL", attachment_type=allure.attachment_type.TEXT)
        raise
