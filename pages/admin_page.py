import logging
from pages.basePage import BasePage

"""
This file contains the admin page functions
"""

class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.admin_panel = page.locator("a[href*='admin']")
        self.username_table_field = page.locator(".oxd-table-filter-area input.oxd-input")
        self.search_button = page.locator("button:has-text('Search')")
        self.result_checkbox = page.locator(".oxd-table-card input[type='checkbox']")
        self.confirm_delete_button = page.locator("button:has-text('Yes, Delete')")

    def go_to_admin_section(self):
        self.logger.info("Navigating to Admin section.")
        self.admin_panel.click()
        self.wait_for_element_to_be_visible(self.username_table_field)

    def search_user(self, username):
        self.logger.info(f"Searching for user: {username}")
        self.username_table_field.fill(username)
        self.search_button.click()
        self.page.wait_for_selector(".oxd-table-card", timeout=5000)
        self.wait_for_element_to_be_visible(self.username_table_field)

    def delete_user(self, username):
        self.logger.info(f"Attempting to delete user: {username}")
        row = self.page.locator(f'.oxd-table-card:has-text("{username}")')
        delete_button = row.locator('.oxd-icon.bi-trash')
        self.wait_for_element_to_be_visible(delete_button)
        self.click(delete_button)
        self.click(self.confirm_delete_button)
        self.logger.info(f"User '{username}' deletion confirmed.")

    def is_user_present(self, username) -> bool:
        self.logger.info(f"Checking if user '{username}' is still present.")
        rows = self.page.locator(f".oxd-table-card:has-text('{username}')")
        count = rows.count()
        self.logger.info(f"Found {count} row(s) with username '{username}'.")
        return count > 0
