import allure
import os
from behave import given, when, then
from features.pages.login_page_objects import LoginPageObjects
from features.utilities.data_util import DataUtil

@given('I am on the login page')
def step_impl(context):
    allure.attach("Navigating to login page", name="INFO", attachment_type=allure.attachment_type.TEXT)
    context.login_page.goto(context.test.base_url)
    allure.attach("Arrived at login page", name="PASS", attachment_type=allure.attachment_type.TEXT)

@when('I enter valid username and password')
def step_impl(context):
    allure.attach("Entering valid username and password", name="INFO", attachment_type=allure.attachment_type.TEXT)
    context.login_page.login('Admin', 'admin123')
    allure.attach("Login action performed", name="PASS", attachment_type=allure.attachment_type.TEXT)

@when('user login with static username as "{username}" and password as "{password}"')
def step_impl(context, username, password):
    allure.attach(f"Static login with username: {username}", name="INFO", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"Static login with password: {password}", name="INFO", attachment_type=allure.attachment_type.TEXT)
    context.login_page.login(username, password)
    allure.attach("Login action performed", name="PASS", attachment_type=allure.attachment_type.TEXT)

@when('user login with "{username}" and "{password}"')
def step_impl(context, username, password):
    login_data = DataUtil.get_scenario_data(context)
    user = login_data.get(username, username)
    pwd = login_data.get(password, password)
    allure.attach(f"Using username: {user}", name="INFO", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"Using password: {pwd}", name="INFO", attachment_type=allure.attachment_type.TEXT)
    context.login_page.login(user, pwd)
    allure.attach("Login action performed", name="PASS", attachment_type=allure.attachment_type.TEXT)

@when('user enters address information from "{address_key}" data')
def step_impl(context, address_key):
    registration_data = DataUtil.get_json_data('registrationData.json')
    if isinstance(registration_data, list):
        registration_data = registration_data[0]
    address = registration_data.get(address_key, {})
    print(f"Address data for '{address_key}':")
    for k, v in address.items():
        print(f"  {k}: {v}")

@when('I click the login button')
def step_impl(context):
    pass

@then('I should see Invalid credentials message')
def step_impl(context):
    allure.attach("Verifying invalid credentials message", name="INFO", attachment_type=allure.attachment_type.TEXT)
    try:
        assert context.login_page.is_invalid_credentials_displayed(), "Invalid credentials message is not displayed or text does not match."
        allure.attach("Invalid credentials message is displayed and verified.", name="PASS", attachment_type=allure.attachment_type.TEXT)
    except AssertionError as e:
        allure.attach(str(e), name="FAIL", attachment_type=allure.attachment_type.TEXT)
        raise

