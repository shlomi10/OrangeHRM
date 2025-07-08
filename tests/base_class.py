import logging
import os

from dotenv import load_dotenv

from api.users_api import UserAPI
from pages.admin_page import AdminPage
from pages.login_page import LoginPage

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

"""
This file contains the base class
"""

class BaseClass:
    def __init__(self, page):
        self.page = page
        self.logger = logging.getLogger(__name__)
        self.base_url = os.getenv("BASE_URL")
        self.login_path = os.getenv("LOGIN_PATH")
        self.admin_username = os.getenv("ADMIN_USERNAME")
        self.admin_password = os.getenv("ADMIN_PASSWORD")
        self.users_table = os.getenv("USERS_TABLE")
        self.users = os.getenv("USERS")
        self.system_users = os.getenv("SYSTEM_USERS")
        self.employees = os.getenv("EMPLOYEES")
        self.admin_page = AdminPage(self.page)
        self.login_page = LoginPage(self.page)
        self.api = UserAPI(
            page=self.page,
            base_url=self.base_url,
            login_path=self.login_path,
            admin_username=self.admin_username,
            admin_password=self.admin_password
        )