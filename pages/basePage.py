import logging
from playwright.sync_api import Page, Locator

"""
This file contains the base page functions
"""

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    def click(self, element: Locator):
        self.logger.debug(f"Clicking on element: {element}")
        element.click()

    def type(self, element: Locator, text: str):
        self.logger.debug(f"Typing into element: {element}, text: {text}")
        element.type(text)

    def fill(self, element: Locator, text: str):
        self.logger.debug(f"Filling element: {element}, text: {text}")
        element.fill(text)

    def wait_for_element_to_be_visible(self, element: Locator, timeout: int = 5000):
        self.logger.debug(f"Waiting for element to be visible: {element}")
        element.wait_for(state="visible", timeout=timeout)

