from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart_details(driver):

    home_page = HomePage(driver)
    home_page.open()
    home_page.click_products()

    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()

    cart_page = CartPage(driver)
    cart_page.open_cart()

    product_name = cart_page.get_first_product_name()
    product_price = cart_page.get_first_product_price()
    product_quantity = cart_page.get_first_product_quantity()
    product_total = cart_page.get_first_product_total()

    assert product_name != ""
    assert product_price.startswith("Rs.")
    assert product_quantity == "1"
    assert product_total == product_price