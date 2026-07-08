from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD = (By.ID, "password")

    DAY = (By.ID, "days")
    MONTH = (By.ID, "months")
    YEAR = (By.ID, "years")
    NEWSLETTER = (By.ID, "newsletter")
    OFFERS = (By.ID, "optin")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")

    CREATE_ACCOUNT = (By.XPATH, "//button[@data-qa='create-account']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_title(self):
        self.click(self.TITLE_MR)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def select_date_of_birth(self, day, month, year):
        self.select_by_visible_text(self.DAY, day)
        self.select_by_visible_text(self.MONTH, month)
        self.select_by_visible_text(self.YEAR, year)

    def subscribe_newsletter(self):
        self.click(self.NEWSLETTER)

    def subscribe_offers(self):
        self.click(self.OFFERS)

    def enter_address_information(
            self,
            first_name,
            last_name,
            company,
            address,
            country,
            state,
            city,
            zipcode,
            mobile):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.COMPANY, company)
        self.type(self.ADDRESS, address)

        self.select_by_visible_text(self.COUNTRY, country)

        self.type(self.STATE, state)
        self.type(self.CITY, city)
        self.type(self.ZIPCODE, zipcode)
        self.type(self.MOBILE, mobile)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT)