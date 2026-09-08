from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.account_data import TEST_EMAIL, TEST_PASSWORD


def test_logout(driver):

    home_page = HomePage(driver)
    home_page.open()

    home_page.click_login()

    login_page = LoginPage(driver)

    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    login_page.logout()

    assert "/login" in driver.current_url