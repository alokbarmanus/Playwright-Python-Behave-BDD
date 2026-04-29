from tests.base_page import BasePage
from playwright.sync_api import expect

class DashboardPageObjects(BasePage):
    DASHBOARD_HEADER = "h6:has-text('Dashboard')"
    WELCOME_MESSAGE = "div.oxd-topbar-header-userarea span.oxd-userdropdown-tab"

    def is_dashboard_displayed(self):
        return self.page.locator(self.DASHBOARD_HEADER).is_visible()

    def is_welcome_message_visible(self):
        return self.page.locator(self.WELCOME_MESSAGE).is_visible()
