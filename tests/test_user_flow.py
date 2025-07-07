import time

import pytest
import logging
import allure
from tests.conftest import initialize
from dotenv import load_dotenv

load_dotenv()

"""
This file contains the main tests
"""

@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate the Orange HRM function")
class TestOrangeHRM:

    logger = logging.getLogger(__name__)
    username = f"testuser_{int(time.time())}"
    password = "Password123!"

    @allure.epic("User Management")
    @allure.feature("API User Creation")
    @allure.story("Create user via API")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(reruns=1)
    def test_create_user_via_api(self, initialize):
        self.logger.info("Running API user creation test.")
        assert initialize.api.login_admin(), "Admin login via API failed"
        assert initialize.api.create_user(self.username, self.password), "User creation failed via API"

    @allure.epic("User Management")
    @allure.feature("UI User Deletion")
    @allure.story("Delete user via UI")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(reruns=1)
    def test_delete_user_via_ui(self, initialize):
        self.logger.info("Running UI user deletion test.")

        # Login via UI
        initialize.login_page.login(initialize.admin_username, initialize.admin_password)

        # Delete via UI
        with allure.step("Navigate to Admin section"):
            initialize.admin_page.go_to_admin_section()

        with allure.step(f"Search and delete user: {self.username}"):
            initialize.admin_page.search_user(self.username)
            initialize.admin_page.delete_user(self.username)

        with allure.step("Verify user was deleted successfully"):
            assert not initialize.admin_page.is_user_present(
                self.username), f"User '{self.username}' still exists in the table"

