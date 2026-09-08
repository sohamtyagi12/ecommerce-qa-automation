from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")

    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//div[@class='features_items']//div[contains(@class,'productinfo')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def search_product(self, product_name):

        search_box = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )

        search_box.clear()
        search_box.send_keys(product_name)

        search_button = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_BUTTON)
        )

        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(
                iframe => iframe.remove()
            );
        """)

        self.driver.execute_script(
            "arguments[0].click();",
            search_button
        )

    def is_search_result_visible(self):

        return self.wait.until(
            EC.presence_of_element_located(
                self.SEARCHED_PRODUCTS
            )
        ).is_displayed()

    def add_first_product_to_cart(self):

        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(
                iframe => iframe.remove()
            );
        """)

        first_product = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//div[contains(@class,'product-image-wrapper')])[1]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            first_product
        )

        ActionChains(self.driver).move_to_element(
            first_product
        ).perform()

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[contains(@class,'product-image-wrapper')])[1]//a[contains(@class,'add-to-cart')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_to_cart_button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "cartModal")
            )
        )