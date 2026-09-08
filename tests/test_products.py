from pages.home_page import HomePage


def test_navigate_to_products(driver):

    home_page = HomePage(driver)

    home_page.open()

    home_page.click_products()

    assert driver.current_url.endswith("/products")