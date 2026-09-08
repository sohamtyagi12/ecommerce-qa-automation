from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_search_product(driver):

    home_page = HomePage(driver)

    home_page.open()

    home_page.click_products()

    products_page = ProductsPage(driver)

    products_page.search_product("Tshirt")

    assert products_page.is_search_result_visible()