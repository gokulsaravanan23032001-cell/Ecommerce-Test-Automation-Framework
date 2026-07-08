from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger.get_logger()

    def open(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        self.wait.until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def type(self, locator, text):
        self.logger.info(f"Typing into element: {locator}")

        self.find(locator).clear()
        self.find(locator).send_keys(text)

    def select_by_visible_text(self, locator, text):
        from selenium.webdriver.support.ui import Select

        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)

    def get_title(self):
        return self.driver.title