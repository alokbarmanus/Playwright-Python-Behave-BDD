from playwright.sync_api import sync_playwright
import configparser
import os

class BaseTest:
    def setup(self):
        self.playwright = sync_playwright().start()
        config = configparser.ConfigParser()
        config.read(os.path.join('configs', 'application.properties'))
        section = 'Application'
        browser_type = config.get(section, 'browser', fallback='chromium')
        # Use headless mode in CI (when HEADLESS env var is set to 'true'), headed locally
        headless = os.environ.get('HEADLESS', 'false').lower() == 'true'
        self.browser = getattr(self.playwright, browser_type).launch(headless=headless)

        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.set_default_navigation_timeout(60000)  # Set page load timeout to 60 seconds

        # Determine environment from ENV variable or default to dev
        env = os.environ.get('ENV', 'dev').lower()
        url_key = f"{env}_url"
        if not config.has_option(section, url_key):
            url_key = 'dev_url'  # fallback
        self.base_url = config.get(section, url_key)

    def teardown(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
