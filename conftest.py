import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    options = webdriver.ChromeOptions()

    options.page_load_strategy = "eager"
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)

    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    # Take screenshot if the test failed
    if request.node.rep_call.failed:

        os.makedirs("screenshots", exist_ok=True)

        test_name = request.node.name
        screenshot_path = f"screenshots/{test_name}.png"

        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)