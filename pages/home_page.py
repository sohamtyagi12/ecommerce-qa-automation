from selenium.webdriver.common.by import By


class HomePage:

    URL = "https://automationexercise.com"

    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_products(self):
        self.driver.get("https://automationexercise.com/products")

    def click_login(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def click_cart(self):
        self.driver.find_element(*self.CART_LINK).click()