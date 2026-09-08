from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_remove_product_from_cart(driver):

    home_page = HomePage(driver)
    home_page.open()
    home_page.click_products()

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()

    cart_page = CartPage(driver)
    cart_page.open_cart()

    assert cart_page.is_product_present()

    cart_page.remove_first_product()

    assert not cart_page.is_product_present()