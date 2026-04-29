from tests.base_page import BasePage
from playwright.sync_api import expect
from features.utilities.data_util import DataUtil

class LoginPageObjects(BasePage):
    
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    DASHBOARD_HEADER = "h6:has-text('Dashboard')"
    INVALID_CREDENTIALS_MSG = "text=Invalid credentials"  # Adjust selector as needed

    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.wait_for_timeout(3000)  # Small wait to ensure inputs are filled before clicking
        self.page.click(self.LOGIN_BUTTON)
        self.page.wait_for_timeout(5000)

    def is_dashboard_displayed(self):
        return self.page.locator(self.DASHBOARD_HEADER).is_visible()

    def is_invalid_credentials_displayed(self):
        self.page.wait_for_timeout(5000)  # Wait for the message to appear
        locator = self.page.locator(self.INVALID_CREDENTIALS_MSG)
        return locator.is_visible() and locator.inner_text() == "Invalid credentials"

    def print_login_data(self, env=None):
        data = DataUtil.get_login_data(env)
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"{key}: {value}")
        elif isinstance(data, list):
            for row in data:
                for key, value in row.items():
                    print(f"{key}: {value}")
                print("---")
