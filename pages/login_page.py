import logging
import allure
from pages.basePage import BasePage

"""
This file contains the login page functions
"""

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("login to the system")
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.username_field = page.locator('input[name="username"]')
        self.password_field = page.locator('input[name="password"]')
        self.loginBTN = page.locator('button[type="submit"]')

    @allure.step("login to system")
    def login(self, username: str, password: str) -> None:
        self.logger.info(f"Logging in with user: {username}")
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.loginBTN)
        self.logger.info("Login submitted successfully.")
