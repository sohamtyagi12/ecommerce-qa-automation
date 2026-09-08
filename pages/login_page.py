from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    LOGIN_EMAIL = (
        By.XPATH,
        "//input[@data-qa='login-email']"
    )

    LOGIN_PASSWORD = (
        By.XPATH,
        "//input[@data-qa='login-password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@data-qa='login-button']"
    )

    LOGOUT_LINK = (
        By.XPATH,
        "//a[@href='/logout']"
    )

    LOGIN_ERROR = (
        By.XPATH,
        "//p[contains(text(),'Your email or password is incorrect!')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def login(self, email, password):

        email_field = self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_EMAIL)
        )

        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_PASSWORD)
        )

        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_button
        )

    def logout(self):

        logout_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout_button
        )

    def is_login_error_visible(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_ERROR)
        ).is_displayed()

    def get_login_error(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_ERROR)
        ).text