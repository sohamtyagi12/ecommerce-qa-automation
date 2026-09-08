from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage

from test_data.account_data import TEST_EMAIL, TEST_PASSWORD


def test_complete_checkout(driver):

    home_page = HomePage(driver)
    home_page.open()

    home_page.click_login()

    login_page = LoginPage(driver)
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    products_page = ProductsPage(driver)
    driver.get("https://automationexercise.com/products")

    products_page.add_first_product_to_cart()

    cart_page = CartPage(driver)
    cart_page.open_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.proceed_to_checkout()

    checkout_page.place_order()

    checkout_page.enter_payment_details(
        "Test User",
        "4111111111111111",
        "123",
        "12",
        "2030"
    )

    checkout_page.pay_and_confirm()

    assert checkout_page.is_order_successful()