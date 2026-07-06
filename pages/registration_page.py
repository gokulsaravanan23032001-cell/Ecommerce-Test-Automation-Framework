from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    NAME = (By.NAME, "name")
    EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def signup(self, name, email):
        self.enter_text(self.NAME, name)
        self.enter_text(self.EMAIL, email)
        self.click(self.SIGNUP_BUTTON)