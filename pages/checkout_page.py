from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    PROCEED_TO_CHECKOUT = (
        By.XPATH,
        "//a[contains(text(),'Proceed To Checkout')]"
    )

    PLACE_ORDER = (
        By.XPATH,
        "//a[contains(text(),'Place Order')]"
    )

    ORDER_COMMENT = (
        By.NAME,
        "message"
    )

    PAYMENT_NAME = (
        By.NAME,
        "name_on_card"
    )

    PAYMENT_CARD_NUMBER = (
        By.NAME,
        "card_number"
    )

    PAYMENT_CVC = (
        By.NAME,
        "cvc"
    )

    PAYMENT_EXPIRY_MONTH = (
        By.NAME,
        "expiry_month"
    )

    PAYMENT_EXPIRY_YEAR = (
        By.NAME,
        "expiry_year"
    )

    PAY_AND_CONFIRM = (
        By.ID,
        "submit"
    )

    ORDER_SUCCESS = (
        By.XPATH,
        "//p[contains(text(),'Congratulations! Your order has been confirmed!')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def proceed_to_checkout(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.PROCEED_TO_CHECKOUT)
        )

        button.click()

    def place_order(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.PLACE_ORDER)
        )

        button.click()

    def enter_payment_details(
        self,
        name,
        card_number,
        cvc,
        expiry_month,
        expiry_year
    ):

        self.wait.until(
            EC.visibility_of_element_located(self.PAYMENT_NAME)
        ).send_keys(name)

        self.driver.find_element(
            *self.PAYMENT_CARD_NUMBER
        ).send_keys(card_number)

        self.driver.find_element(
            *self.PAYMENT_CVC
        ).send_keys(cvc)

        self.driver.find_element(
            *self.PAYMENT_EXPIRY_MONTH
        ).send_keys(expiry_month)

        self.driver.find_element(
            *self.PAYMENT_EXPIRY_YEAR
        ).send_keys(expiry_year)

    def pay_and_confirm(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.PAY_AND_CONFIRM)
        )

        button.click()

    def is_order_successful(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.ORDER_SUCCESS)
        ).is_displayed()