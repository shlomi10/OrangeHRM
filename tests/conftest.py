import logging
import os
import shutil

import pytest
from playwright.sync_api import sync_playwright
from tests.base_class import BaseClass
from allure_commons.types import AttachmentType
import allure

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

@pytest.fixture(scope="function")
def initialize(request):
    with sync_playwright() as playwright:
        user_data_dir = os.path.join(os.getcwd(), "user_data")
        context = playwright.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,
            args=["--start-maximized", "--disable-blink-features=AutomationControlled"],
            viewport=None,
            locale="en-US",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.pages[0]
        page.add_init_script("""Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""")
        page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.availWidth, screen.availHeight);")
        window_size = page.evaluate("""() => {return { width: window.innerWidth, height: window.innerHeight };}""")
        page.set_viewport_size(window_size)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        base = BaseClass(page)
        page.goto(base.base_url + base.login_path)

        yield base

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_dir = "../screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="screenshot", attachment_type=AttachmentType.PNG)

        context.tracing.stop(path="../trace/trace.zip")
        page.close()
        context.close()

        # Delete the user_data directory
        if os.path.exists(user_data_dir):
            shutil.rmtree(user_data_dir)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
