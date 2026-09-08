from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")

    CONTINUE_SHOPPING = (
        By.XPATH,
        "//button[contains(text(),'Continue Shopping')]"
    )

    CART_MODAL = (By.ID, "cartModal")

    CART_ITEMS = (
        By.XPATH,
        "//table[@id='cart_info_table']//tbody/tr"
    )

    PRODUCT_NAME = (
        By.XPATH,
        ".//td[@class='cart_description']//h4/a"
    )

    PRODUCT_PRICE = (
        By.XPATH,
        ".//td[@class='cart_price']//p"
    )

    PRODUCT_QUANTITY = (
        By.XPATH,
        ".//td[@class='cart_quantity']//button"
    )

    PRODUCT_TOTAL = (
        By.XPATH,
        ".//td[@class='cart_total']//p"
    )
    REMOVE_PRODUCT = (
    By.XPATH,
    "//a[@class='cart_quantity_delete']"
)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def close_cart_modal(self):

        try:
            continue_button = WebDriverWait(
                self.driver, 5
            ).until(
                EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
            )

            continue_button.click()

            self.wait.until(
                EC.invisibility_of_element_located(self.CART_MODAL)
            )

        except Exception:
            pass

    def open_cart(self):
        self.driver.get("https://automationexercise.com/view_cart")
        self.wait.until(
            EC.url_contains("/view_cart")
            )

    def get_cart_items(self):

        return self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )

    def get_cart_item_count(self):

        return len(self.get_cart_items())

    def get_first_product_name(self):

        item = self.get_cart_items()[0]

        return item.find_element(
            *self.PRODUCT_NAME
        ).text

    def get_first_product_price(self):

        item = self.get_cart_items()[0]

        return item.find_element(
            *self.PRODUCT_PRICE
        ).text

    def get_first_product_quantity(self):

        item = self.get_cart_items()[0]

        return item.find_element(
            *self.PRODUCT_QUANTITY
        ).text


    def get_first_product_total(self):

        item = self.get_cart_items()[0]

        return item.find_element(
            *self.PRODUCT_TOTAL
        ).text


    def remove_first_product(self):

        remove_button = self.wait.until(
            EC.element_to_be_clickable(
                self.REMOVE_PRODUCT
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            remove_button
        )

        self.wait.until(
            EC.invisibility_of_element_located(
                self.REMOVE_PRODUCT
            )
        )


    def is_product_present(self):

        products = self.driver.find_elements(
            *self.CART_ITEMS
        )

        return len(products) > 0