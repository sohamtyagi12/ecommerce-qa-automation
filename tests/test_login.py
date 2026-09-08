from pages.login_page import LoginPage
from test_data.account_data import TEST_EMAIL, TEST_PASSWORD


def test_valid_login(driver):

    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)

    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    assert "Logged in as" in driver.page_source