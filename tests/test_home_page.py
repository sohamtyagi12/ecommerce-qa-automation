from pages.home_page import HomePage


def test_open_homepage(driver):

    home_page = HomePage(driver)

    home_page.open()

    assert "Automation Exercise" in driver.title