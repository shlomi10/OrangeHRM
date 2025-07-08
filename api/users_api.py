import allure
import requests
import logging

from pages.basePage import BasePage

"""
This file contains the users api calls
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("users api calls")
class UserAPI(BasePage):
    def __init__(self, page, base_url, login_path, admin_username, admin_password):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session()
        self.username_field = page.locator('input[name="username"]')
        self.password_field = page.locator('input[name="password"]')
        self.submitBTN = page.locator('button[type="submit"]')
        self.base_url = base_url
        self.login_path = login_path
        self.admin_username = admin_username
        self.admin_password = admin_password

    @allure.step("get browser session cookie")
    def get_browser_session_cookie(self) -> None:
        self.logger.info(f"Logging in with user: {self.admin_username}")
        self.navigate(self.base_url + self.login_path)
        self.fill(self.username_field, self.admin_username)
        self.fill(self.password_field, self.admin_password)
        self.click(self.submitBTN)
        self.logger.info("Login submitted.")

        self.page.wait_for_load_state('networkidle')

        cookies = self.page.context.cookies()
        for c in cookies:
            if c["name"] == "orangehrm":
                self.logger.info("Session cookie retrieved successfully.")
                return c["value"]
        self.logger.error("Session cookie 'orangehrm' not found.")
        return None

    def login_admin(self) -> bool:
        cookie = self.get_browser_session_cookie()
        if cookie:
            self.session.cookies.set("orangehrm", cookie)
            self.logger.info("Admin session initialized from browser.")
            return True
        self.logger.error("Failed to get session cookie from browser login.")
        return False

    def get_existing_emp_number(self, initialize):
        url = initialize.base_url + initialize.employees
        response = self.session.get(url)
        self.logger.info(f"Get employees response: {response.status_code} - {response.text}")

        try:
            data = response.json()
            employees = data.get("data", [])  # <-- fixed
            for emp in employees:
                emp_number = emp.get("empNumber")
                if emp_number:
                    print("Using empNumber:", emp_number)
                    return emp_number
        except Exception as e:
            self.logger.error(f"Failed to parse employee list: {e}")

        return None

    def create_user(self, initialize, username, password):
        self.logger.info(f"Creating user: {username}")

        emp_number = self.get_existing_emp_number(initialize)
        if not emp_number:
            self.logger.error("No valid employee found.")
            return False

        url = initialize.base_url + initialize.users
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Origin": initialize.base_url,
            "Referer": initialize.base_url + initialize.system_users
        }

        payload = {
            "username": username,
            "password": password,
            "status": True,
            "userRoleId": 1,
            "empNumber": emp_number
        }

        response = self.session.post(url, headers=headers, json=payload)

        print("RESPONSE CODE:", response.status_code)
        print("RESPONSE TEXT:", response.text)

        self.logger.info(f"Create user response: {response.status_code} - {response.text}")
        return response.status_code in [200, 201]
