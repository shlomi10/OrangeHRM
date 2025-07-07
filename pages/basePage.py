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

    def press_enter_on_element(self, element: Locator):
        self.logger.debug(f"Pressing ENTER on element: {element}")
        element.press("Enter")

    def press_enter_on_page(self):
        self.logger.debug("Pressing ENTER on page.")
        self.page.keyboard.press("Enter")

    def get_title_of_page(self) -> str:
        title = self.page.title()
        self.logger.info(f"Current page title: {title}")
        return title

    def get_text(self, element: Locator) -> str:
        text = element.inner_text()
        self.logger.debug(f"Got text from element: {text}")
        return text

    def is_visible(self, element: Locator) -> bool:
        visible = element.is_visible()
        self.logger.debug(f"Element visible: {visible}")
        return visible

    def wait_for_element_to_be_visible(self, element: Locator, timeout: int = 5000):
        self.logger.debug(f"Waiting for element to be visible: {element}")
        element.wait_for(state="visible", timeout=timeout)

    def wait_for_element_to_be_detached(self, element: Locator, timeout: int = 5000):
        self.logger.debug(f"Waiting for element to be detached: {element}")
        element.wait_for(state="detached", timeout=timeout)

    def take_screenshot(self, path: str = "screenshot.png"):
        self.logger.info(f"Taking screenshot: {path}")
        self.page.screenshot(path=path)

    def switch_to_iframe(self, locator_str: str):
        self.logger.debug(f"Switching to iframe: {locator_str}")
        self.page.locator(locator_str).wait_for(state="visible")
        return self.page.frame_locator(locator_str)
