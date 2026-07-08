from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config_reader import ConfigReader

class HomePage(BasePage):

    URL = ConfigReader.get_base_url()

    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Signup / Login')]")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open(self.URL)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)