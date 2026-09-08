from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):

    home_page = HomePage(driver)
    home_page.open()

    home_page.click_products()

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()

    cart_page = CartPage(driver)
    cart_page.open_cart()

    assert cart_page.get_cart_item_count() >= 1